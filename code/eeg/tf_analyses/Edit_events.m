%%to Run on FIU HPC%
% create a local cluster object
cluster = parcluster('local');

% start matlabpool with max workers set in the slurm file
parpool(cluster, str2num(getenv('SLURM_CPUS_ON_NODE')))
% Kia Hosseini edited this script for mfe_b study to be run on the HPC!

%  This script changes the event structure of epoched EEG to include a
%  "Condition" field that will be used in TF, ITPS, ICPS/wPLI script

clear all

main_dir = '/home/data/NDClab/datasets/memory-for-error-dataset'; %directory on the HPC

% Where the epoched data are located
data_location = [main_dir filesep 'derivatives' filesep 'preprocessed' filesep 'eeg' filesep 'preprocessed' filesep 'processed_data'];

% Where you would like your epoched and newly labeled data saved
save_location = [main_dir filesep 'derivatives' filesep 'preprocessed' filesep 'eeg' filesep 'relabeled_for_TF'];

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

    % Load data
    EEG=pop_loadset('filename', [subject], 'filepath', data_location);
    EEG = pop_selectevent( EEG, 'latency','-.1 <= .1','deleteevents','on');
    
    
% add label to the event structure
EEG = pop_editeventfield( EEG, 'indices',  strcat('1:', int2str(length(EEG.event))), 'Condition','NaN');
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
    
end

%save data with added event field "Condition"
        EEG = pop_editset(EEG, 'setname', [subject]);
        EEG = pop_saveset( EEG, 'filename',[subject],'filepath', save_location);

end %end loop through subjects
