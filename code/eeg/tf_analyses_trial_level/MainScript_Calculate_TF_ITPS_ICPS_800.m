%%to Run on FIU HPC%
% create a local cluster object
cluster = parcluster('local');

% start matlabpool with max workers set in the slurm file
parpool(cluster, str2num(getenv('SLURM_CPUS_ON_NODE')))


%Compute TF, ITPS, ICPS, and wPLI measures for EEG data
%Maureen Bowers 6/29/2021 based on scripts by Ranjan Debnath
% Kianoosh Hosseini has edited this script for mfe_b trial level study Dec. 8, 2023!
clear all;
clc;

%%
%%%%% Setting paths %%%%%

main_dir = '/home/data/NDClab/datasets/memory-for-error-dataset'; % main directory 

%1. Data Location
data_location = [main_dir filesep 'derivatives' filesep 'preprocessed' filesep 'eeg' filesep 'preprocessed' filesep 'processed_data_trial_level'];

%2. Save Data Location
% Saves just wPLI output [time windows 800 ms]
save_location = [main_dir filesep 'derivatives' filesep 'preprocessed' filesep 'eeg' filesep 'TF_outputs_trial_level' filesep 'main800' filesep];


%3. Scripts Location
scripts_location = [main_dir filesep 'code' filesep 'eeg' filesep 'tf_analyses_trial_level'];

%4. Set EEGLab path
addpath(genpath([main_dir filesep 'code' filesep 'eeg' filesep 'preprocessing' filesep 'eeglab2023']));% enter the path of the EEGLAB folder in this line

%remove path to octave functions inside matlab to prevent errors when
rmpath([main_dir filesep 'code' filesep 'eeg' filesep 'preprocessing' filesep 'eeglab2023' filesep 'functions' filesep 'octavefunc' filesep 'signal'])



%%
%%%%% Information about dataset and analysis procedures %%%%%%
%5. Number of channels
nbchan = 64;

%6. What kind of data? Resting State or Event-Related Data
RestorEvent = 0; %1 = rest, 0 = event

% 7. Kia has changed this to load a cell array of all images shown during
% the Flanker task. 
% So, Conds will list all the displayed images during the face flanker
% task.
Conds = readcell([scripts_location filesep 'dispImages_listed.csv']);
Conds_full = readcell([scripts_location filesep 'dispImages_listed_full.csv']);

%8. Minimum number of trials to analyze
mintrialnum = 1; %If the participant does not have enough trials in a condition based on this cutoff, a "notenoughdata.mat" file will be saved into save_location.

%9. Would you like to baseline correct your data? NOTE: ICPS calculated over time will not be baseline corrected.
BaselineCorrect = 1; %1=Yes, 0=No

%10. What time period would you like to use to baseline correct
BaselineTime = [-1000 -200];
%Put in time in ms for event-related data. For example, if you want to baseline correct from -100 to 0ms before the 
% event for evernt-related paradigms, put [-100 0].
% Kia: Baseline correction will be done based on each trial not average of
% all trials.

%11. Would you like to downsample the output to 125Hz? This is done after the time-frequency computations and will have minor impacts on the resolution. 
%We recommend downsampling to reduce file size for ease of storage. 
% All data will be initially downsampled to 250 Hz. 
Downsample = 0; %0=No, 1=Yes  

%12. Dataset Name - will be appended to the saved files
DatasetName = '_mfe_b_trial_level';


%%
%%%%% Settings for Time-Frequency Meres %%%%%

%13. Minimum and Maximum Frequency, Number of Frequency Bins, and range cycles to calculate complex Morlet wavelet decomposition
min_freq = 1;
max_freq = 30; % check
num_frex = 59; % number of frequency bins between minimum and maximum frequency
range_cycles = [3 10]; % wavelet cycles: min 3 max 10


%%
%%%%% Questions about phase-based measures %%%%%

%14. Would you like to calculate inter-trial phase synchrony (ITPS) in addition to TF?
ITPS_calc = 0; %(1=yes,0=no)


%16. Would you like to calculate inter-channel phase synchrony (ICPS or wPLI) in addition to TF?
ICPS_calc = 1; %(1=yes,0=no) 

%17. Would you like to caluclate coherence or weighted phaselagidx?
ICPS_or_wPLI = 0; %(1=coherence, 0=wPLI)

%19. Type of Connectivity to compute 
ConnectType = 1; %(0= all-to-all connectivity; 1=seed-based connectivity)
%If seed based, choose seed and which electrodes to compute connectivity:
Seed = '1'; % Kia: FCz (i.e, 1 on the BV electrode system) as an MFC seed electrode.  
Elecs4Connect = { '1' '2' '3' '4' '5' '6' '7' '8' '9' '10' '11' '12' '13' '14' '15' '16' '17' '18' '19' '20' '21' '22' '23' '24' '25' '26' '27' '28' '29' '30' '31' '32' '33' '34' '35' '36' '37' '38' '39' '40' '41' '42' '43' '44' '45' '46' '47' '48' '49' '50' '51' '52' '53' '54' '55' '56' '57' '58' '59' '60' '61' '62' '63' '64'};

% 20. Create List of subjects to loop through
subnum = dir([data_location filesep '*.set']); % Use regex to find your files 
subject= {subnum.name};
for ii=1:length(subject)
    subject_list{ii}=subject{ii};   
end

% 21. Single trial TF?
TF_singletrial_save = 1;
% We recommend checking that your subject list looks like you would expect:
% subject_list

eeglab % Loading EEGLAB

%%%%%%%%%%%%%%%%%%%% COMPUTATIONS BEGIN BELOW HERE %%%%%%%%%%%%%%%%
%% loop through all subject
for sub=1:length(subject_list)
    
    % Initialize objects for this participant:
    timefreqs_data = [];
    phase_data=[];
    ITPS_all=[];
    ICPS_all=[];
    wPLI_all=[];
    EEG=[];
    
    subject = subject_list{sub};
    fprintf('\n\n\n*** Processing subject %d (%s) ***\n\n\n', sub, subject);

    % Load data
    EEG=pop_loadset('filename', [subject], 'filepath', data_location);
    EEG = pop_selectevent( EEG, 'latency','-.1 <= .1','deleteevents','on');
    
    %Downsample to 250Hz
    % Kia: Here we downsample to 250 Hz and then later if we choose to downsample, we
    % downsample to 125 Hz after TF compuations!
    EEG = pop_resample(EEG, 250); 
    EEG = eeg_checkset( EEG );
    
    % Kia Code below
    for image = 1:size(EEG.event,2)
        temp_val = string(EEG.event(image).dispImage);
        if ~ismissing(temp_val)
            temp_name = extractBefore(extractAfter(temp_val, 'neutralC/'), '.jpg');
            EEG.event(image).dispImage = char(temp_name);
        elseif ismissing(temp_val)
            EEG.event(image).dispImage = char('NaN');
        end
    end

    %Keep only markers of interest
    EEG = pop_selectevent( EEG, 'dispImage',Conds, 'deleteevents','on','deleteepochs','on','invertepochs','off');
    EEG = eeg_checkset( EEG );

    % Keep only response epochs
    response_epochs = {'resp'};
    EEG = pop_selectevent( EEG, 'eventType',response_epochs, 'deleteevents','on','deleteepochs','on','invertepochs','off');
    EEG = eeg_checkset( EEG );
    
    %save times
    time = EEG.times;
    
    %save channel locations
    channel_location = EEG.chanlocs;
    
    %% Compute complex morlet wavelet time frequency decomposition
    cd(scripts_location)
    trial_level_timefreq_script;
 
end
    
%Save out table with trial numbers
TrialNums_table = struct2table(TrialNums);
writetable(TrialNums_table,[save_location 'TrialNums.csv']);

    
    

