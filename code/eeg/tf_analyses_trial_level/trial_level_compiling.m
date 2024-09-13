%%to Run on FIU HPC%
% create a local cluster object
cluster = parcluster('local');

% start matlabpool with max workers set in the slurm file
parpool(cluster, str2num(getenv('SLURM_CPUS_ON_NODE')))



%% This script compiles a dataset with all conditions and all participants 
%and plots results as time frequency surfaces and topo plots
% Kia Hosseini edited this script for the mfe_b study on Feb 15, 2024.
% This script runs locally (not on the HPC).

% This script is for the wPLI computed from 0-250 ms.
clear
clc;

%% 1. Data Location - this is the location of the .mat files for each participant for each condition
data_location = '/home/data/NDClab/datasets/memory-for-error-dataset/derivatives/preprocessed/eeg/TF_outputs_trial_level/main';

% 2. Save Location - this is the location where you would like your
% datasets to be stored. We recommend this to be in a separate folder than
% where the .mat files are stored.
save_location = '/home/data/NDClab/datasets/memory-for-error-dataset/derivatives/preprocessed/eeg/TF_outputs_trial_level/compiled/';

% 3. Set EEGLab path
addpath(genpath('/home/data/NDClab/datasets/memory-for-error-dataset/code/eeg/preprocessing/eeglab2023'));

% 4. Conditions for Event-Related Data - this should be the same name used in the main script
Conds = readcell('/home/data/NDClab/datasets/memory-for-error-dataset/code/eeg/tf_analyses_trial_level/dispImages_listed.csv');

% 5. Was TF baseline corrected?
TF_bln = 1; %0=no, 1=yes

% 6. Did you calculate wPLI and want it compiled?
wPLI_calc = 1; %0=no, 1=yes
% 6a. Was wPLI baseline corrected? 
wPLI_bln = 1; %0=no, 1=yes

% 7. Did you downsample your data?
Downsample = 0; %0=no; 1=yes
%%
% Theta (4-7 Hz); elecs [1 2 34 33]; time [0-250] - done

% Theta (4-7 Hz); elecs [22 53 24 55]; time [0-250] - done

% 8. Choose which channels to average for TF surface. (If more than one electrode, then those electrodes will be averaged).
chans2extract_TF = {'1' '2' '34' '33'};  
 
% 9. Choose which channels to extract for wPLI surface. 
chans2extract_ICPSwpli =  {'22' '53' '24' '55'};  % Posterior


% 10. Choose what time period to average over for the CSV file. NOTE: It
% is probably advantageous to examine the TF surfaces first before choosing this time period.
time_window_for_csv = [0 250]; % this is just for TF power


% 11. Choose what frequency range to average over for the CSV file. NOTE:
%This is probably an apriori decision based on hypotheses.
freq_window_for_csv = [4 7]; 
%%
% File list
cd(data_location)
subnum=dir('*.mat');
sub_list={subnum.name};
for i =1:length(sub_list)
    sub = sub_list{i};
    % subject_list{i}= sub(1:end-11);
    subjects{i}= sub(1:end-4);
end
unique_subjects=unique(extractBefore(subjects,'_'));
%participants after 170040 have 'sub-' before their ID. So, I need to
%remove that part to have exact ID.
for uu = 1:length(unique_subjects)
    if contains(unique_subjects(1, uu),'sub-')
        unique_subjects(1, uu) = extractAfter(unique_subjects(1, uu),'-');
    end
end

%%%%%%%%%%%%%%%% Compiling STARTS BELOW HERE %%%%%%%%%%%%%%%%%%%
% Kia: for simplicity, I have assumed that each image is a condition.


% An empty table that will have length(unique_subjects) rows and
% columns for the images, and the subjects'IDs!
colNames = ['sub_id', Conds]; % prepend 'sub_id' to the cell array
extracted_tf_power = array2table(nan(length(unique_subjects), length(colNames)));
extracted_tf_power.Properties.VariableNames = colNames;
extracted_tf_wpli = extracted_tf_power; 

% Looping through images. 
for cond=1:length(Conds)
    col_index = find(ismember(extracted_tf_power.Properties.VariableNames, Conds{cond}));


    %%%%%%%%%% COMPILE TIME FREQUENCY DATA %%%%%%%%%%%%%%%%%
    fprintf('\n\n\n*** Processing Image %s ***\n\n\n', char(Conds{cond}));
    % Looping through subjects
    for subj = 1:length(unique_subjects) 
        timefreqs_baselinecorr=[];
        timefreqs_data=[];
        %Find files for this subject
        sub_file_list =   contains(subjects,unique_subjects{subj});
        currentsubs = subjects(sub_file_list);
        %Find TF files for this subjects
        tf_file_list =  contains(currentsubs,'TF');
        currentTF = currentsubs(tf_file_list);
        %Find current condition TF files for this subject
        cond_file_list = contains(currentTF, Conds{cond});
        currentcond = char(currentTF(cond_file_list));
        % Current subject ID
        current_subject_id = str2num(unique_subjects{subj}); 
        extracted_tf_power(subj,1) = {current_subject_id};
        

        %load appropriate file
        cd(data_location)
        % To load channel location to the workspace, we load a wpli file.
        load('sub-170040_mfe_eeg-flanker_s1-r1-e1_ica_data_processed_data_trial_level_mfe_b_trial_level_wPLI_baselinecorrected_resp_CFD-BF-039-031-N.mat');

        try % for some participants certain trials (images have been removed. So, they do not have that image.
            % I have this try catch in order to prevent the script from
            % erroring and stopping.
            load([currentcond '.mat']); % loads the current condition .mat file


            % pull out time, frequency, and channel indices for extraction
            freq_window_idx = dsearchn(frequency',freq_window_for_csv');
            if Downsample ==1
                time_window_idx = dsearchn(ds_time',time_window_for_csv');
            elseif Downsample ==0
                time_window_idx = dsearchn(time',time_window_for_csv');
            end
            % Find indices of the channels to extract
            for i=1:length(chans2extract_TF)
                Elecs_idx (i)= find(strcmp({channel_location.labels}, chans2extract_TF{i}));
            end

            % Time Frequency surface
            % Dimensions of timefreqs_baselinecorr are : freqs x time pnts x channels
            extracted_tf_power(subj, col_index) = {squeeze(mean(mean(mean(timefreqs_baselinecorr(freq_window_idx(1,1):freq_window_idx(2,1) ,time_window_idx(1,1):time_window_idx(2,1) ,Elecs_idx),3),1),2))};


        catch exception
            continue % Pass control to the next loop iteration
        end % end of try catch
    end % end of looping through subjects for TF
end % End of looping through images (conditions)

% Saving extracted theta powers
writetable(extracted_tf_power, [save_location filesep 'allSubs_theta_power.csv'])

% Looping through images. 
for cond=1:length(Conds)
    col_index = find(ismember(extracted_tf_wpli.Properties.VariableNames, Conds{cond}));

    %%%%%%%%%% COMPILE wPLI DATA %%%%%%%%%%%%%%%%%
    if wPLI_calc == 1
        % Looping through subjects
        for subj = 1:length(unique_subjects)
            wPLI_blncorr=[]; wPLI_all=[];

            sub_file_list =   contains(subjects,unique_subjects{subj});
            currentsubs = subjects(sub_file_list);
            wpli_file_list =  contains(currentsubs,'wPLI');
            currentwpli = currentsubs(wpli_file_list);


            cond_file_list = contains(currentwpli, Conds{cond});
            currentcond = char(currentwpli(cond_file_list));
            % Current subject ID
            current_subject_id = str2num(unique_subjects{subj});
            extracted_tf_wpli(subj,1) = {current_subject_id};

            cd(data_location)
            try % for some participants certain trials (images have been removed. So, they do not have that image.
                % I have this try catch in order to prevent the script from
                % erroring and stopping.

                load([currentcond '.mat']);

                % pull out time, frequency, and channel indices for extraction
                freq_window_idx = dsearchn(frequency',freq_window_for_csv');
                
                % Find indices of the channels to extract
                for i=1:length(chans2extract_ICPSwpli)
                    Elecs_idx (i)= find(strcmp({channel_location.labels}, chans2extract_ICPSwpli{i}));
                end
                % wPLI_blncorr has 2 dimensions: freqs x channels
                extracted_tf_wpli(subj, col_index) = {squeeze(mean(mean(wPLI_blncorr(freq_window_idx(1,1):freq_window_idx(2,1) ,Elecs_idx),2),1))};
    
            catch exception
                continue % Pass control to the next loop iteration
            end % end of try catch
        end % end of looping through subjects for wPLI
    end % end of wPLI compilig
end % End of looping through images (conditions)
% Looping to create a file that has all subjects' matrices in them
        
% Saving extracted theta powers
writetable(extracted_tf_wpli, [save_location filesep 'allSubs_theta_wpli.csv'])



      




