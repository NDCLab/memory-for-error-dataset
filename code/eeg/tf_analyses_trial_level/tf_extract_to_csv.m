%% This script will load outputs of the 'compiling and plotting' script, extract measures of interest, and then save them as a CSV file. 
% Written by Kianoosh Hosseini (Kianoosh.info; NDCLAB.com)
% Last Update: 01/16/2024

% Theta (4-7 Hz); elecs [1 2 34 33]; time [0-250]

% Theta (4-7 Hz); elecs [22 53 24 55]; time [0-250]


clear
clc;

%% Data Location - this is the location of the .mat files that you will need to load
data_location = '/Users/kihossei/Documents/GitHub/memory-for-error-dataset/derivatives/preprocessed/eeg/TF_outputs/compiled/mfc/theta';

%% Save Location - this is the location where you would like your csv files to be stored. 
save_location = '/Users/kihossei/Documents/GitHub/memory-for-error-dataset/derivatives/preprocessed/eeg/TF_outputs/csv_for_stats/mfc/theta';


%% Load .mat files
cd (data_location)

TF_AllSubs = load("TF_AllSubs.mat");
wPLI_AllSubs = load("wPLI_AllSubs.mat");

%% Setting up 
% 1. Conditions for Event-Related Data - this should be the same name used in the main script
Conds = readcell('/home/data/NDClab/datasets/memory-for-error-dataset/code/eeg/tf_analyses_trial_level/dispImages_listed.csv');

% 3. Did you downsample your data?
Downsample = 0; %0=no; 1=yes

% Theta (4-7 Hz); elecs [1 2 34 33]; time [0-250] - done

% Theta (4-7 Hz); elecs [22 53 24 55]; time [0-250] - done



% 4. Choose which channels to average for TF surface. (If more than one electrode, then those electrodes will be averaged).
chans2extract_TF = {'1' '2' '34' '33'};  
%chans2extract_TF = {'22' '53' '24' '55'}; 
 
% 6. Choose which channels to extract for wPLI surface. 
%chans2extract_ICPSwpli =  {'4' '6' '36' '39'};  % MFC (Frontal-lateral)
chans2extract_ICPSwpli =  {'22' '53' '24' '55'};  % Posterior


% 7. Choose what time period to average over for the CSV file. NOTE: It
% is probably advantageous to examine the TF surfaces first before choosing this time period.
time_window_for_csv = [0 250]; 


% 8. Choose what frequency range to average over for the CSV file. NOTE:
%This is probably an apriori decision based on hypotheses.
freq_window_for_csv = [4 7]; 


%% File list
cd('/Users/kihossei/Documents/GitHub/memory-for-error-dataset/derivatives/preprocessed/eeg/TF_outputs/main') % location of the files that are outputs of the 'mainscript_calculate_TF_ITPS_ICPS' script!
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


%% Extract Time-Frequency data
% pull out time, frequency, and channel indices for extraction
    freq_window_idx = dsearchn(TF_AllSubs.frequency',freq_window_for_csv');
    if Downsample ==1
        time_window_idx = dsearchn(TF_AllSubs.ds_time',time_window_for_csv');
    elseif Downsample ==0
        time_window_idx = dsearchn(TF_AllSubs.time',time_window_for_csv');
    end
% Find indices of the channels to extract
    for i=1:length(chans2extract_TF)
        Elecs_idx (i)= find(strcmp({TF_AllSubs.channel_location.labels}, chans2extract_TF{i}));
    end
    
% Time Frequency surface
% Dimensions are : subs, cond, to-be-extracted frequency window indices,
% to-be-extracted time window indices, to-be-extracted electrodes

% A zeros matrix that has length(unique_subjects) and columns for each
% condition, the difference score and subjects ID!
extracted_TF = zeros(length(unique_subjects), length(Conds) + 2 ); % This matrix will be updated in loop below 

TF_allsubs = TF_AllSubs.TF_allsubs;
% Loop over subjects:
for subj = 1:length(unique_subjects)
    % 1st column is the ID column
    extracted_TF(subj,1) = str2double(unique_subjects(subj));

    % Condition 1 : Incong error response
    extracted_TF(subj,2) = squeeze(mean(mean(mean(TF_allsubs(subj, 1, freq_window_idx(1,1):freq_window_idx(2,1) ,time_window_idx(1,1):time_window_idx(2,1) ,Elecs_idx),5),3),4));
    
    % Condition 2 : Incong correct response
    extracted_TF(subj,3) = squeeze(mean(mean(mean(TF_allsubs(subj, 2, freq_window_idx(1,1):freq_window_idx(2,1) ,time_window_idx(1,1):time_window_idx(2,1) ,Elecs_idx),5),3),4));
    
    % the difference score (incong_error - incong_correct)
    extracted_TF(subj,4) = extracted_TF(subj,2) - extracted_TF(subj,3);
end % closing the loop over subjects

% converting the extracted_TF matrix to a table
extracted_TF = array2table (extracted_TF, 'VariableNames', {'id', 'incong_error_theta_power', 'incong_correct_theta_power', 'difference_score'});
% Saving extracted theta powers
writetable(extracted_TF, [save_location filesep 'theta_power.csv'])


%% Extract wPLI data

% pull out time, frequency, and channel indices for extraction
    freq_window_idx = dsearchn(wPLI_AllSubs.frequency',freq_window_for_csv');
    if Downsample ==1
        time_window_idx = dsearchn(wPLI_AllSubs.ds_time',time_window_for_csv');
    elseif Downsample ==0
        time_window_idx = dsearchn(wPLI_AllSubs.time',time_window_for_csv');
    end

% Find indices of the channels to extract
    for i=1:length(chans2extract_ICPSwpli)
        Elecs_idx (i)= find(strcmp({wPLI_AllSubs.channel_location.labels}, chans2extract_ICPSwpli{i}));
    end

% A zeros matrix that has length(unique_subjects) and columns for each
% condition, the difference score and subjects ID! 
extracted_wPLI = zeros(length(unique_subjects), length(Conds) + 2 ); % This matrix will be updated in loop below 

wPLI_allsubs = wPLI_AllSubs.wpli_allsubs;
% Loop over subjects:
for subj = 1:length(unique_subjects)
    % 1st column is the ID column
    extracted_wPLI(subj,1) = str2double(unique_subjects(subj));

    % Condition 1 : Incong error response
    extracted_wPLI(subj,2) = squeeze(mean(mean(mean(wPLI_allsubs(subj, 1, freq_window_idx(1,1):freq_window_idx(2,1) ,time_window_idx(1,1):time_window_idx(2,1) ,Elecs_idx),5),3),4));
    
    % Condition 2 : Incong correct response
    extracted_wPLI(subj,3) = squeeze(mean(mean(mean(wPLI_allsubs(subj, 2, freq_window_idx(1,1):freq_window_idx(2,1) ,time_window_idx(1,1):time_window_idx(2,1) ,Elecs_idx),5),3),4));
    
    % the difference score (incong_error - incong_correct)
    extracted_wPLI(subj,4) = extracted_wPLI(subj,2) - extracted_wPLI(subj,3);
end % closing the loop over subjects

% converting the extracted_TF matrix to a table
extracted_wPLI = array2table (extracted_wPLI, 'VariableNames', {'id', 'incong_error_wPLI', 'incong_correct_wPLI', 'difference_score'});
% Saving extracted theta powers
writetable(extracted_wPLI, [save_location filesep 'wPLI.csv'])


