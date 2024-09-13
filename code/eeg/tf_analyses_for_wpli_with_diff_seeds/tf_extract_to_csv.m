
%% This script will load outputs of the 'compiling and plotting' script, extract measures of interest, and then save them as a CSV file. 
% Written by Kianoosh Hosseini (Kianoosh.info; NDCLAB.com)
% Last Update: 07/18/2023 

% Theta (4-7 Hz); elecs [1 2 34 33]; time [0-250]

% Theta (4-7 Hz); elecs [22 53 24 55]; time [0-250]


clear
clc;

%% Data Location - this is the location of the .mat files that you will need to load
data_location = '/Users/kihossei/Documents/GitHub/memory-for-error-dataset/derivatives/preprocessed/eeg/TF_outputs/compiled';

%% Save Location - this is the location where you would like your csv files to be stored. 
save_location = '/Users/kihossei/Documents/GitHub/memory-for-error-dataset/derivatives/preprocessed/eeg/TF_outputs/csv_for_stats';


%% Load .mat files
cd (data_location)

TF_AllSubs = load("TF_AllSubs.mat");
ITPS_AllSubs = load("ITPS_AllSubs.mat");
wPLI_AllSubs = load("wPLI_AllSubs.mat");

%% Setting up 
% 1. Conditions for Event-Related Data - this should be the same name used in the main script
Conds = {'resp_i_0','resp_i_1'}; %leave blank if resting data

% 2. Name of Conditions to be used for plotting - this such make the order
% that the conditions are named above
ConditionNames = {'Incong error response' 'Incong correct response'}; %If resting, just put one condition name here (e.g., Resting)

% 3. Did you downsample your data?
Downsample = 1; %0=no; 1=yes

% Theta (4-7 Hz); elecs [1 2 34 33]; time [0-250]; MFC

% Theta (4-7 Hz); elecs [22 53 24 55]; time [0-250]; lateral occipital
% [19 23 50]; % medial occipital
% [20 21 51 52]; % Parietal
% [6 9 39 42]; %  lateral frontal


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
% pull out time, and frequency indices for extraction
    freq_window_idx = dsearchn(TF_AllSubs.frequency',freq_window_for_csv');
    if Downsample ==1
        time_window_idx = dsearchn(TF_AllSubs.ds_time',time_window_for_csv'); % Although initially data was downsampled to 250 Hz, the data after TF decomposition was downsampled to 125 and then saved.
    elseif Downsample ==0
        time_window_idx = dsearchn(TF_AllSubs.time',time_window_for_csv');
    end
%% %%%%%%%%%%%%%%% Extract TF Power for MFC %%%%%%%%%%%%%%%%%%%%%%%
chans2extract_TF = {'1' '2' '34' '33'};
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
writetable(extracted_TF, [save_location filesep 'theta_power_mfc.csv'])

%% %%%%%%%%%%%%%%% Extract TF Power for lateral occipital%%%%%%%%%%%%%%%%%%%%%%%
chans2extract_TF = {'22' '53' '24' '55'};
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
writetable(extracted_TF, [save_location filesep 'theta_power_lat_occipital.csv'])

%% %%%%%%%%%%%%%%% Extract TF Power for medial occipital%%%%%%%%%%%%%%%%%%%%%%%
chans2extract_TF = {'19' '50' '23'};
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
writetable(extracted_TF, [save_location filesep 'theta_power_med_occipital.csv'])

%% %%%%%%%%%%%%%%% Extract TF Power for parietal%%%%%%%%%%%%%%%%%%%%%%%
chans2extract_TF = {'20' '21' '51' '52'};
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
writetable(extracted_TF, [save_location filesep 'theta_power_parietal.csv'])

%% %%%%%%%%%%%%%%% Extract TF Power for lateral frontal%%%%%%%%%%%%%%%%%%%%%%%
chans2extract_TF = {'6' '9' '39' '42'};
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
writetable(extracted_TF, [save_location filesep 'theta_power_lat_frontal.csv'])


%% Extract ITPS
% pull out time, and frequency indices for extraction
    freq_window_idx = dsearchn(ITPS_AllSubs.frequency',freq_window_for_csv');
    if Downsample ==1
        time_window_idx = dsearchn(ITPS_AllSubs.ds_time',time_window_for_csv');
    elseif Downsample ==0
        time_window_idx = dsearchn(ITPS_AllSubs.time',time_window_for_csv');
    end

%% %%%%%%%%%%%%%%% Extract ITPS for MFC %%%%%%%%%%%%%%%%%%%%%%%
chans2extract_ITPS =  {'1' '2' '34' '33'};  
% Find indices of the channels to extract
    for i=1:length(chans2extract_ITPS)
        Elecs_idx (i)= find(strcmp({ITPS_AllSubs.channel_location.labels}, chans2extract_ITPS{i}));
    end

% A zeros matrix that has length(unique_subjects) and columns for each
% condition, the difference score and subjects ID! 
extracted_ITPS = zeros(length(unique_subjects), length(Conds) + 2 ); % This matrix will be updated in loop below 

ITPS_allsubs = ITPS_AllSubs.ITPS_allsubs;
% Loop over subjects:
for subj = 1:length(unique_subjects)
    % 1st column is the ID column
    extracted_ITPS(subj,1) = str2double(unique_subjects(subj));

    % Condition 1 : Incong error response
    extracted_ITPS(subj,2) = squeeze(mean(mean(mean(ITPS_allsubs(subj, 1, freq_window_idx(1,1):freq_window_idx(2,1) ,time_window_idx(1,1):time_window_idx(2,1) ,Elecs_idx),5),3),4));
    
    % Condition 2 : Incong correct response
    extracted_ITPS(subj,3) = squeeze(mean(mean(mean(ITPS_allsubs(subj, 2, freq_window_idx(1,1):freq_window_idx(2,1) ,time_window_idx(1,1):time_window_idx(2,1) ,Elecs_idx),5),3),4));
    
    % the difference score (incong_error - incong_correct)
    extracted_ITPS(subj,4) = extracted_ITPS(subj,2) - extracted_ITPS(subj,3);
end % closing the loop over subjects

% converting the extracted_TF matrix to a table
extracted_ITPS = array2table (extracted_ITPS, 'VariableNames', {'id', 'incong_error_ITPS', 'incong_correct_ITPS', 'difference_score'});
% Saving extracted theta powers
writetable(extracted_ITPS, [save_location filesep 'ITPS_mfc.csv'])

%% %%%%%%%%%%%%%%% Extract ITPS for lateral occipital%%%%%%%%%%%%%%%%%%%%%%%
chans2extract_ITPS =  {'22' '53' '24' '55'};
% Find indices of the channels to extract
    for i=1:length(chans2extract_ITPS)
        Elecs_idx (i)= find(strcmp({ITPS_AllSubs.channel_location.labels}, chans2extract_ITPS{i}));
    end

% A zeros matrix that has length(unique_subjects) and columns for each
% condition, the difference score and subjects ID! 
extracted_ITPS = zeros(length(unique_subjects), length(Conds) + 2 ); % This matrix will be updated in loop below 

ITPS_allsubs = ITPS_AllSubs.ITPS_allsubs;
% Loop over subjects:
for subj = 1:length(unique_subjects)
    % 1st column is the ID column
    extracted_ITPS(subj,1) = str2double(unique_subjects(subj));

    % Condition 1 : Incong error response
    extracted_ITPS(subj,2) = squeeze(mean(mean(mean(ITPS_allsubs(subj, 1, freq_window_idx(1,1):freq_window_idx(2,1) ,time_window_idx(1,1):time_window_idx(2,1) ,Elecs_idx),5),3),4));
    
    % Condition 2 : Incong correct response
    extracted_ITPS(subj,3) = squeeze(mean(mean(mean(ITPS_allsubs(subj, 2, freq_window_idx(1,1):freq_window_idx(2,1) ,time_window_idx(1,1):time_window_idx(2,1) ,Elecs_idx),5),3),4));
    
    % the difference score (incong_error - incong_correct)
    extracted_ITPS(subj,4) = extracted_ITPS(subj,2) - extracted_ITPS(subj,3);
end % closing the loop over subjects

% converting the extracted_TF matrix to a table
extracted_ITPS = array2table (extracted_ITPS, 'VariableNames', {'id', 'incong_error_ITPS', 'incong_correct_ITPS', 'difference_score'});
% Saving extracted theta powers
writetable(extracted_ITPS, [save_location filesep 'ITPS_lat_occipital.csv'])
%% %%%%%%%%%%%%%%% Extract ITPS for medial occipital%%%%%%%%%%%%%%%%%%%%%%%
chans2extract_ITPS =  {'19' '23' '50'};
% Find indices of the channels to extract
    for i=1:length(chans2extract_ITPS)
        Elecs_idx (i)= find(strcmp({ITPS_AllSubs.channel_location.labels}, chans2extract_ITPS{i}));
    end

% A zeros matrix that has length(unique_subjects) and columns for each
% condition, the difference score and subjects ID! 
extracted_ITPS = zeros(length(unique_subjects), length(Conds) + 2 ); % This matrix will be updated in loop below 

ITPS_allsubs = ITPS_AllSubs.ITPS_allsubs;
% Loop over subjects:
for subj = 1:length(unique_subjects)
    % 1st column is the ID column
    extracted_ITPS(subj,1) = str2double(unique_subjects(subj));

    % Condition 1 : Incong error response
    extracted_ITPS(subj,2) = squeeze(mean(mean(mean(ITPS_allsubs(subj, 1, freq_window_idx(1,1):freq_window_idx(2,1) ,time_window_idx(1,1):time_window_idx(2,1) ,Elecs_idx),5),3),4));
    
    % Condition 2 : Incong correct response
    extracted_ITPS(subj,3) = squeeze(mean(mean(mean(ITPS_allsubs(subj, 2, freq_window_idx(1,1):freq_window_idx(2,1) ,time_window_idx(1,1):time_window_idx(2,1) ,Elecs_idx),5),3),4));
    
    % the difference score (incong_error - incong_correct)
    extracted_ITPS(subj,4) = extracted_ITPS(subj,2) - extracted_ITPS(subj,3);
end % closing the loop over subjects

% converting the extracted_TF matrix to a table
extracted_ITPS = array2table (extracted_ITPS, 'VariableNames', {'id', 'incong_error_ITPS', 'incong_correct_ITPS', 'difference_score'});
% Saving extracted theta powers
writetable(extracted_ITPS, [save_location filesep 'ITPS_med_occipital.csv'])
%% %%%%%%%%%%%%%%% Extract ITPS for parietal%%%%%%%%%%%%%%%%%%%%%%%
chans2extract_ITPS =  {'20' '21' '51' '52'};
% Find indices of the channels to extract
    for i=1:length(chans2extract_ITPS)
        Elecs_idx (i)= find(strcmp({ITPS_AllSubs.channel_location.labels}, chans2extract_ITPS{i}));
    end

% A zeros matrix that has length(unique_subjects) and columns for each
% condition, the difference score and subjects ID! 
extracted_ITPS = zeros(length(unique_subjects), length(Conds) + 2 ); % This matrix will be updated in loop below 

ITPS_allsubs = ITPS_AllSubs.ITPS_allsubs;
% Loop over subjects:
for subj = 1:length(unique_subjects)
    % 1st column is the ID column
    extracted_ITPS(subj,1) = str2double(unique_subjects(subj));

    % Condition 1 : Incong error response
    extracted_ITPS(subj,2) = squeeze(mean(mean(mean(ITPS_allsubs(subj, 1, freq_window_idx(1,1):freq_window_idx(2,1) ,time_window_idx(1,1):time_window_idx(2,1) ,Elecs_idx),5),3),4));
    
    % Condition 2 : Incong correct response
    extracted_ITPS(subj,3) = squeeze(mean(mean(mean(ITPS_allsubs(subj, 2, freq_window_idx(1,1):freq_window_idx(2,1) ,time_window_idx(1,1):time_window_idx(2,1) ,Elecs_idx),5),3),4));
    
    % the difference score (incong_error - incong_correct)
    extracted_ITPS(subj,4) = extracted_ITPS(subj,2) - extracted_ITPS(subj,3);
end % closing the loop over subjects

% converting the extracted_TF matrix to a table
extracted_ITPS = array2table (extracted_ITPS, 'VariableNames', {'id', 'incong_error_ITPS', 'incong_correct_ITPS', 'difference_score'});
% Saving extracted theta powers
writetable(extracted_ITPS, [save_location filesep 'ITPS_parietal.csv'])
%% %%%%%%%%%%%%%%% Extract ITPS for lateral frontal%%%%%%%%%%%%%%%%%%%%%%%
chans2extract_ITPS =  {'6' '9' '39' '42'};
% Find indices of the channels to extract
    for i=1:length(chans2extract_ITPS)
        Elecs_idx (i)= find(strcmp({ITPS_AllSubs.channel_location.labels}, chans2extract_ITPS{i}));
    end

% A zeros matrix that has length(unique_subjects) and columns for each
% condition, the difference score and subjects ID! 
extracted_ITPS = zeros(length(unique_subjects), length(Conds) + 2 ); % This matrix will be updated in loop below 

ITPS_allsubs = ITPS_AllSubs.ITPS_allsubs;
% Loop over subjects:
for subj = 1:length(unique_subjects)
    % 1st column is the ID column
    extracted_ITPS(subj,1) = str2double(unique_subjects(subj));

    % Condition 1 : Incong error response
    extracted_ITPS(subj,2) = squeeze(mean(mean(mean(ITPS_allsubs(subj, 1, freq_window_idx(1,1):freq_window_idx(2,1) ,time_window_idx(1,1):time_window_idx(2,1) ,Elecs_idx),5),3),4));
    
    % Condition 2 : Incong correct response
    extracted_ITPS(subj,3) = squeeze(mean(mean(mean(ITPS_allsubs(subj, 2, freq_window_idx(1,1):freq_window_idx(2,1) ,time_window_idx(1,1):time_window_idx(2,1) ,Elecs_idx),5),3),4));
    
    % the difference score (incong_error - incong_correct)
    extracted_ITPS(subj,4) = extracted_ITPS(subj,2) - extracted_ITPS(subj,3);
end % closing the loop over subjects

% converting the extracted_TF matrix to a table
extracted_ITPS = array2table (extracted_ITPS, 'VariableNames', {'id', 'incong_error_ITPS', 'incong_correct_ITPS', 'difference_score'});
% Saving extracted theta powers
writetable(extracted_ITPS, [save_location filesep 'ITPS_lat_frontal.csv'])

%% Extract wPLI
% pull out time and frequency indices for extraction
    freq_window_idx = dsearchn(wPLI_AllSubs.frequency',freq_window_for_csv');
    if Downsample ==1
        time_window_idx = dsearchn(wPLI_AllSubs.ds_time',time_window_for_csv');
    elseif Downsample ==0
        time_window_idx = dsearchn(wPLI_AllSubs.time',time_window_for_csv');
    end
%% %%%%%%%%%%%%%%% Extract wPLI for MFC-Lateral Occipital %%%%%%%%%%%%%%%%%%%%%
chans2extract_ICPSwpli =  {'22' '53' '24' '55'};  % 
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
writetable(extracted_wPLI, [save_location filesep 'wPLI_lat_occipital.csv'])
%% %%%%%%%%%%%%%%% Extract wPLI for MFC-Medial Occipital %%%%%%%%%%%%%%%%%%%%%%
chans2extract_ICPSwpli =  {'19' '23' '50'};  % 
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
writetable(extracted_wPLI, [save_location filesep 'wPLI_med_occipital.csv'])

%% %%%%%%%%%%%%%%% Extract wPLI for MFC-parietal %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
chans2extract_ICPSwpli =  {'20' '21' '51' '52'};  % 
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
writetable(extracted_wPLI, [save_location filesep 'wPLI_parietal.csv'])

%% %%%%%%%%%%%%%%% Extract wPLI for MFC-lateral frontal %%%%%%%%%%%%%%%%%%%%%%%
chans2extract_ICPSwpli =  {'6' '9' '39' '42'};  % 
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
writetable(extracted_wPLI, [save_location filesep 'wPLI_lat_frontal.csv'])


