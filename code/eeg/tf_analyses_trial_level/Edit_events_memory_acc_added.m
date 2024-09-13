%%to Run on FIU HPC%
% create a local cluster object
cluster = parcluster('local');

% start matlabpool with max workers set in the slurm file
parpool(cluster, str2num(getenv('SLURM_CPUS_ON_NODE')))
% Kia Hosseini edited this script for mfe_b study to be run on the HPC!

%  This script changes the event structure of epoched EEG to include a
%  "Condition" field that will be used in TF, ITPS, ICPS/wPLI script

% Kia edits this script to also add another column that tells whether the image
% displayed during a trial was remembered during the subsequent memory task
% or not. 

clear all

main_dir = '/home/data/NDClab/datasets/memory-for-error-dataset'; %directory on the HPC
%main_dir = '/Users/kihossei/Documents/GitHub/memory-for-error-dataset'; %directory on the HPC

% Where the epoched data are located
data_location = [main_dir filesep 'derivatives' filesep 'preprocessed' filesep 'eeg' filesep 'preprocessed' filesep 'processed_data_trial_level'];

% Memory data location

memory_dat_location = [main_dir filesep 'derivatives' filesep 'preprocessed' filesep 'psychopy' filesep 'memoryDat' filesep];

% Where you would like your epoched and newly labeled data saved
save_location = [main_dir filesep 'derivatives' filesep 'preprocessed' filesep 'eeg' filesep 'added_markers_for_memory'];

%Location of EEGlab
addpath(genpath([main_dir filesep 'code' filesep 'eeg' filesep 'preprocessing' filesep 'eeglab2023']));% enter the path of the EEGLAB folder in this line

%remove path to octave functions inside matlab to prevent errors when
rmpath([main_dir filesep 'code' filesep 'eeg' filesep 'preprocessing' filesep 'eeglab2023' filesep 'functions' filesep 'octavefunc' filesep 'signal'])

% Create List of subjects to loop through
subnum = dir([data_location filesep '*.set']); % Use regex to find your files
subject= {subnum.name};
for ii=1:length(subject)
    subject_list{ii}=subject{ii};
end

% Loop through each subject
for sub=1:length(subject_list)

    subject = subject_list{sub};
    fprintf('\n\n\n*** Processing subject %d (%s) ***\n\n\n', sub, subject);

    % extract subject ID
    subject_id = extractAfter(extractBefore(subject,'_mfe'), 'sub-');
    % Load the Surprise Memory data
    current_sub_memory_dat_name = append(memory_dat_location, string(subject_id), '_mfe_b_surpriseDat_v6.csv');
    current_sub_memory_dat = readtable(current_sub_memory_dat_name);

    % Load the EEG data
    EEG=pop_loadset('filename', [subject], 'filepath', data_location);
    EEG = pop_selectevent( EEG, 'latency','-.1 <= .1','deleteevents','on');


    % add label to the event structure
    EEG = pop_editeventfield( EEG, 'indices',  strcat('1:', int2str(length(EEG.event))), 'Condition','NaN');
    EEG = eeg_checkset( EEG );

    % add another label to the event structure
    EEG = pop_editeventfield( EEG, 'indices',  strcat('1:', int2str(length(EEG.event))), 'memoryAcc','NaN');
    EEG = eeg_checkset( EEG );
    % check the event structure for consistency
    EEG = eeg_checkset(EEG, 'eventconsistency');

    % Looping through each trial
    for t=1:length(EEG.event)

        % Condition that we want to concatenate into one variable - THIS WILL
        % NEED TO BE CHANGED FOR EACH STUDY !!!!
        eventType = {EEG.event.eventType};
        congruency = {EEG.event.congruency};
        accuracy = {EEG.event.accuracy};

        % Selecting specific variables for this trial
        vars_to_join = {eventType{t}, num2str(congruency{t}), num2str(accuracy{t}) };
        EEG.event(t).Condition = strjoin(vars_to_join, '_');
        % Kia: outputs will b like 'resp_i_0','resp_i_1', 'resp_c_1','stim_i_0', 'stim_i_1','stim_c_1'!

        %% find the displayed image in this trial
        % Check to see if the current value in dispImage is NaN
        % isnan does not work as it will yield an error when it is not NaN. 
        % To solve this issue, first convert to an string. If it is NaN, the output of string() will be
        % <missing>. So, ismissing function can be used to determine
        % whether it is NaN or not. 
        if ismissing(string(EEG.event(t).dispImage))
            % do nothing
        else
            current_dispImage = string(EEG.event(t).dispImage); 
            % find the current dispImage in the memory data table and see
            % if this subject remembered this image or not. 
            the_row_current_image_found_in_memory_table = current_sub_memory_dat.face == current_dispImage;
            % Select the row that match the condition
            temp_memory_row = current_sub_memory_dat(the_row_current_image_found_in_memory_table, :);
            % Check whether the image is remembered or not
            if temp_memory_row.identified_as_new == 1 % not remembered
                EEG.event(t).memoryAcc = 'not_remembered';
            elseif temp_memory_row.identified_as_new == 0 % remembered
                EEG.event(t).memoryAcc = 'remembered';
            end % end of checking whether the image is remembered or not

        end % end of checking whether the the current value in dispImage is NaN
        
        
    end

    %save data with added event field "Condition"
    EEG = pop_editset(EEG, 'setname', [subject]);
    EEG = pop_saveset( EEG, 'filename',[subject],'filepath', save_location);

end %end loop through subjects
