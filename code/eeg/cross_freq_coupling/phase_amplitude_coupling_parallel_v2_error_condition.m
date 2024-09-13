
% This script is written by Kianoosh Hosseini (https://Kianoosh.info) at
% NDCLab (https://ndclab.com) based on Mike X. Cohen's code that accompanies the
% Analyzing Neural Time Series book (https://mikexcohen.com/book) and the code
% available with (https://doi.org/10.1016/j.dcn.2022.101067) in April 2024.


% This code just computes error condition (i.e., cond1)
clear all;
clc;

%% Section 1a. Set the Directories
% Main Directory
main_dir = '/home/data/NDClab/datasets/memory-for-error-dataset';
%main_dir = '/Users/kihossei/Documents/GitHub/memory-for-error-dataset';

% Data Location (preprocessd EEG data)
data_location = [main_dir filesep 'derivatives' filesep 'preprocessed' filesep 'eeg' filesep 'relabeled_for_TF'];

% Save Data Location
save_location = [main_dir filesep 'derivatives' filesep 'preprocessed' filesep 'eeg' filesep 'cfc' filesep 'main2' filesep ];


% Set EEGLab path
addpath(genpath([main_dir filesep 'code' filesep 'eeg' filesep 'preprocessing' filesep 'eeglab2023']));

%% Section 1b: Set the parameters

% 1. What are your conditions of interest if using Event-Related Data? This
% naming convention should come from the Edit_events.m script provided.
% Note: not needed for resting state data.
myConds = {'resp_i_0','resp_i_1'}; % resp_i_0 = incong error response; resp_i_1 = incong correct response
% Note about conditions in the codes below: 
% cond1 refers to incong error response
% cond2 refers to incong correct response

% 2. Minimum and Maximum Frequency, Number of Frequency Bins, and range cycles to calculate complex Morlet wavelet decomposition
min_freq = 4;
max_freq = 50; % check with George
num_frex = 40; % number of frequency bins between minimum and maximum frequency
% For CFC, temporal precision matters the most and because of that we use
% lower number of wavelet cycles to improve temporal precision although
% this acts against the frequency precision.
range_cycles = [3 5]; % wavelet cycles: min 3 max 5

% 3. We will subsample trials as we have uneven numbers of trials in conditions.
% How many trials to pull for each subsample?
numPulledTrials = 10;
% How many times to do subsampling? We recommend doing at least 10 subsamples and to have the possiblility of using all your data
% (e.g., if you have 150 trials, do 15 subsamples of 10 trials).
numSubsamples = 100; % My task has 384 trials. So, 100 subsamples seems to be good to cover them all.


% 4. What are the lower (frequency for phase) and upper (frequency for
% power) bands?
freq4Phase = [4 7]; % frequency range for the lower frequency band.
freq4Power = [8 50]; % frequency range for the upper frequency band.

% 5. What is the electrode to extract the lower frequency phase?
% One electrode must be chosen.
elecs4Phase = {'1'}; % MFC

% 6. What is/are the electrodes to extract the upper frequency amplitude?
elecs4Amp = {'1', '6', '9', '19', '20', '21', '22', '24', '39', '42', '50', '51', '52', '53', '55'};

% 7. Use the electrodes listed in Q5 and Q6 above to list all the
% electrodes that will be needed.
% Frontolateral elecs: 6, 9, 39, 42
% MFC: 1
% Posteriolateral: 22, 24, 53, 55
elecs4PAC = {'1', '6', '9', '19', '20', '21', '22', '24', '39', '42', '50', '51', '52', '53', '55'};
lels = length(elecs4PAC);

% 8. What is the minimum number of trials per condition?
% If aparticipant has less than this number of trials per conditions of
% interest, their data will not be processed.
min_trialNum_perCondition = 10;

% 9. Choose the time points for which you want to compute PAC?
times4PAC = -50:50:500;
% 10. Number of iteration for the non-parametric permutation testing that
% allows to compute PACz.
num_perm_iter = 100;




%% Section 1c: List the preprocessed EEG data files to be able to loop through later.
subnum = dir([data_location filesep '*.set']); % Use regex to find your files
subject= {subnum.name};
already_processed = []; % add the name of the subjects already processed here. Example: ["sub-200100_mfe_b_eeg-flanker_s1-r1-e1_processed_data.set", "sub-200088_mfe_b_eeg-flanker_s1-r1-e1_processed_data.set"]

for ii=1:length(subject)
    subject_list{ii}=subject{ii};
    if ismember(subject_list{ii}, already_processed)
        subject_list{ii} = '';
    end
end

%% Load the EEGLAB
eeglab

%% Loop through all subjects
cluster = parcluster('local');
parpool(cluster, str2num(getenv('SLURM_CPUS_ON_NODE')))
parfor sub=1:length(subject_list)

    % Initialize objects for this participant:
    timefreqs_data = [];
    phase_data=[];
    EEG=[];

    subject = subject_list{sub};
    if isempty(subject) %skip over already-processed subs
        continue
    end
    fprintf('\n\n\n*** In the error condition: processing subject %d (%s) ***\n\n\n', sub, subject);
    subjStart = tic;
    % There is a single subject that does not have sub- in their file name.
    % To prevent empty subject ID fields, I check for sub- in their file
    % name before extracting their subject ID. 
    if contains(subject, "sub-")
        subject_id = extractAfter(extractBefore(subject,'_mfe'), 'sub-'); % will be needed when we save files
    else
        subject_id = extractBefore(subject,'_mfe'); % will be needed when we save files
    end
    

    % Load data
    EEG=pop_loadset('filename', [subject], 'filepath', data_location);
    % Note: Event latencies are stored in units of data sample points
    % relative to (1) the beginning of the continuous data matrix (EEG.data).
    EEG = pop_selectevent( EEG, 'latency','-.1 <= .1','deleteevents','on');
    
    % Trials that are labeled as responded and validRt (trials that have larger than 150 ms RT) 
    % will only be included.
    try 
        EEG = pop_selectevent( EEG, 'validRt',1, 'deleteevents','on','deleteepochs','on','invertepochs','off');
        EEG = eeg_checkset( EEG );

    catch ME
        warning('Error occurred when selecting only valid trials (vlaidRt) for subject %d: %s', subject, ME.message);
        continue; % This will skip to the next iteration of the loop (next subject)
    end

    try 
        EEG = pop_selectevent( EEG, 'responded',1, 'deleteevents','on','deleteepochs','on','invertepochs','off');
        EEG = eeg_checkset( EEG );

    catch ME
        warning('Error occurred when selecting only valid trials (responded) for subject %d: %s', subject, ME.message);
        continue; % This will skip to the next iteration of the loop (next subject)
    end
    % If no error occurred during selecting only valid trials, the code
    % will continue from here.

    % Keep only markers of interest (i.e., conditions of interest)
    try
        EEG = pop_selectevent( EEG, 'Condition',myConds, 'deleteevents','on','deleteepochs','on','invertepochs','off');
        EEG = eeg_checkset( EEG );
    catch ME
        warning('Error occurred when selecting only conditions of interest for subject %d: %s', subject, ME.message);
        continue; % This will skip to the next iteration of the loop (next subject)
    end
    % If no error occurred during selecting only conditions of interest, the code
    % will continue from here.
    

    elecs4PAC_idx = [1, 6, 9, 19 ,20, 21, 22, 24, 39, 42, 50, 51, 52, 53, 55];

    % save times
    epoch_time = EEG.times;

    % save channel locations
    channel_location = EEG.chanlocs;

    %% Compute complex morlet wavelet time frequency decomposition
    all_data = EEG.data; % data = data matrix; channel x time/data points x trials
    srate = EEG.srate; % srate = sampling rate;

    % pull out condition data
    % creating the following empty arrays so that we can reuse them in each iteration
    % of the loop
    cond1_data = []; cond2_data = []; cond1_EEG =[]; cond2_EEG =[];

    try
        cond1_EEG = pop_selectevent( EEG, 'Condition',(myConds{1}), 'deleteevents','on','deleteepochs','on','invertepochs','off');
        cond1_data = eeg_checkset( cond1_EEG.data ); % data from the condition 1
    catch ME
        warning('Error occurred when selecting only conditions 1 data for subject %d: %s', subject, ME.message);
        continue; % This will skip to the next iteration of the loop (next subject)
    end
    % If no error occurred during selecting only conditions 1 data, the code
    % will continue from here.

    elecs4PAC_idx_cond1 = zeros(1,lels);
    for i=1:lels
        elecs4PAC_idx_cond1(i) = find(strcmp({cond1_EEG.chanlocs.labels}, elecs4PAC{i}));
    end

    try
        cond2_EEG = pop_selectevent( EEG, 'Condition',(myConds{2}), 'deleteevents','on','deleteepochs','on','invertepochs','off');
        cond2_data = eeg_checkset( cond2_EEG.data ); % data from the condition 2
    catch ME
        warning('Error occurred when selecting only conditions 2 data for subject %d: %s', subject, ME.message);
        continue; % This will skip to the next iteration of the loop (next subject)
    end
    % If no error occurred during selecting only conditions 2 data, the code
    % will continue from here.

    elecs4PAC_idx_cond2 = zeros(1,lels);
    for i=1:lels
        elecs4PAC_idx_cond2(i) = find(strcmp({cond2_EEG.chanlocs.labels}, elecs4PAC{i}));
    end

    % Check to see if this subject has the minimum number of trials per
    % conditions of interest.
    if size(cond1_data, 3) >= min_trialNum_perCondition
        if size(cond2_data, 3) >= min_trialNum_perCondition

            % frequencies vector
            frex = linspace(min_freq, max_freq, num_frex);
            % Gaussian widths (Standard deviation) vector
            % Eq. to compute gaussian width is: (number of wavelet
            % cycles)/(2*pi*frex)
            gaussian_width_vector = linspace(range_cycles(1),range_cycles(end), num_frex)./ (2*pi*frex);

            % wavelet parameters
            wavtime = -1:1/srate:1; % wavelet timepoints (samples)
            % When we compute the convolution between a signal and a kernel, the length
            % of the output becomes [length(signal) + length(kernel) - 1]. So, we need to
            % trim the half of kernel from the beginning and half of the kernel + 1 from
            % the end so that the length of the convolution ouput equals the length of
            % the input signal. So, we need to calculate the half of the kernel
            % (wavelet here).
            halfwaveletsize = (length(wavtime)-1)/2;

            % FFT parameters
            wavelet_length = length(wavtime); % number of time points (samples) in the wavelet
            epoch_data_length = size(all_data, 2); % number of time points (samples) in each epoch
            conv_output_length = wavelet_length + epoch_data_length - 1;

            %% Prepare condition 1 data for wavelet
            % Loop through epochs and remove the epochs that are NaN
            epochs2remove = [];
            %for i=1:lels
            %    elecs4PAC_idx_cond1 (i)= find(strcmp({cond1_EEG.chanlocs.labels}, elecs4PAC{i}));
            %end
            for e=1:size(cond1_data,3) % begin loop through epochs
                %loop through and find indices of the electrodes of interest (i.e.,
                %elecs4PAC)
                %do any of these electrodes have NaNs in them?
                if min(sum(isnan(cond1_EEG.data(elecs4PAC_idx_cond1,:,e)))) > 0
                    %if so, add that epoch to vector of epochs to be removed
                    epochs2remove = [epochs2remove e];
                else
                    %do nothing
                end %end if loop for if channel within epoch is NaN
            end % end loop through epochs
            % remove all epochs with NaNs for channels of interest
            cond1_data(:,:,unique(epochs2remove))=[];
            % keep only channels of interest
            cond1_data = cond1_data(elecs4PAC_idx_cond1,:,:); % channel x time/data points x trials

            
            %% Starting to calculate TF
            fprintf('\n\n\n*** Calculating TF for subject %d (%s) ***\n\n\n', sub, subject);
            % Initiating the empty table that will store the current
            % subject's data
            
            variable_names = {'subject_id', 'subsample_iteration', 'lower_frequency', 'upper_frequency', 'lower_frequency_channel', 'upper_frequency_channel', 'time_point', 'is_error_condition', 'PACz'};
            % variable_types = {'string','double','double', 'double', 'string', 'string', 'double', 'double'};
            

            
            for subsample = 1:numSubsamples
                % This script computes PAC by collapsing across conditions in order
                % to pick the lower and upper frequency bands showing the maximal
                % PAC. This helps to reduce the number of multiple comparisons.
                % Thus, we, randomly, subsample equal number of epochs from each condition of interest.
                % Creating the following empty arrays so that we can reuse them in each iteration
                % of the loop.
                fprintf('\n\n\n*** Calculating TF for subsample %d of subject %d (%s) ***\n\n\n', subsample, sub, subject);
                
                current_subject_data_cond1 = table;

                subtrials_cond2=[]; data_cond1_temp=[]; 

                % Get indices of trials from this condition
                subtrials_cond1 = randsample(1:size(cond1_data,3),(numPulledTrials),false); % random sampling without replacement
                % Index into those trials and pull them out
                data_cond1_temp = cond1_data(:,:,subtrials_cond1);

                %% Condition 1: 
                %% Run wavelet convolution
                timefreqs = zeros(length(frex), epoch_data_length, size(data_cond1_temp, 3)); % freqs x time points x trials
                phase_data = zeros(length(frex), epoch_data_length, size(data_cond1_temp, 3)); % freqs x time points x trials
                timefreqs_strial_ch = zeros(length(frex), epoch_data_length, size(data_cond1_temp, 3), size(data_cond1_temp, 1)); % freqs x time points x trials x channels
                phase_data_strial_ch = zeros(length(frex), epoch_data_length, size(data_cond1_temp, 3), size(data_cond1_temp, 1)); % freqs x time points x trials x channels
                for ch=1:size(data_cond1_temp, 1) % Loop through all channels
                    for fi=1:length(frex) % loop through all frequencies
                        trial_conv = zeros(epoch_data_length, size(data_cond1_temp, 3));

                        %% Create wavelet
                        wavelet  = exp(2*1i*pi*frex(fi).*wavtime) .* exp(-wavtime.^2./(2*gaussian_width_vector(fi)^2));
                        waveletX = fft(wavelet, conv_output_length); % fft of wavelet
                        waveletX = waveletX ./ max(waveletX); % normalize fft of wavelet

                        %% Loop through all trials
                        trial_temppow = zeros(size(data_cond1_temp, 2), size(data_cond1_temp, 3));
                        for trl=1:size(data_cond1_temp, 3)
                            temp_data = fft(squeeze(data_cond1_temp(ch,:,trl)), conv_output_length);

                            %% run convolution
                            temp_conv = ifft(waveletX .* temp_data, conv_output_length);
                            temp_conv2 = temp_conv(halfwaveletsize+1:end-halfwaveletsize);

                            %% extract phase angles
                            temp_phase_angle = angle(temp_conv2);
                            trial_conv (:,trl) = temp_phase_angle;

                            %% compute power
                            trial_temppow (:,trl) = abs(temp_conv(halfwaveletsize+1:end-halfwaveletsize)).^2;
                        end % end looping through trials

                        % Build dataset for phase data
                        phase_data(fi,:,:) = trial_conv; % frequencies x time points x trials

                        % Build dataset for TF power
                        timefreqs(fi,:,:) = trial_temppow; % frequencies x time points x trials


                    end % end looping through frequencies

                    % Build dataset for phase data with channels
                    phase_data_strial_ch(:,:,:,ch) = phase_data; % frequencies x time points x trials x channels

                    % Build dataset for TF with channels
                    timefreqs_strial_ch(:,:,:,ch) = timefreqs; % frequencies x time points x trials x channels

                end % end looping through channels

                % loop through lower and upper freqs.

                % Define the range of lower frequncy band
                lfb_lower_bound = freq4Phase(1);
                lfb_upper_bound = freq4Phase(2);
                % Find the indices of elements within the range of the
                % lower freq. bands
                lower_freq_band_indices = find(floor(frex) >= lfb_lower_bound & floor(frex) <= lfb_upper_bound);

                % Define the range of upper frequncy band
                ufb_lower_bound = freq4Power(1);
                ufb_upper_bound = freq4Power(2);
                % Find the indices of elements within the range of the
                % upper freq. bands
                upper_freq_band_indices = find(floor(frex) >= ufb_lower_bound & floor(frex) <= ufb_upper_bound);

                % Loop through the lower frequency band
                for lfb_counter = 1:length(lower_freq_band_indices)
                    temp_lower_freq_idx = lower_freq_band_indices(lfb_counter);
                    % pick the channel from which the lower freq. phase will be used
                    % to compute PAC.
                    freq4Phase_elec_idx = [];
                    for elec_idx_finder = 1:numel(elecs4PAC)
                        if strcmp(elecs4PAC{elec_idx_finder}, elecs4Phase{1})
                            freq4Phase_elec_idx = elec_idx_finder;
                            break; % Exit the loop once a match is found
                        end
                    end % end the loop that allows to find freq4Phase_elec_idx
                    % Extract Phase angle data for the chosen lower frequency from the picked channel
                    phase_data_lowerFreq_chosenElec = squeeze(phase_data_strial_ch(temp_lower_freq_idx,:,:,freq4Phase_elec_idx)); % time points x trials

                    % Loop through the upper frequency band
                    for ufb_counter = 1:length(upper_freq_band_indices)
                        temp_upper_freq_idx = upper_freq_band_indices(ufb_counter);

                        % loop through the channels from which we will take the
                        % upper frequency power.
                        freq4Power_elec_idx = [];
                        for elecs4Amp_idx = 1:length(elecs4Amp)
                            tempElec_from_elecs4Amp = elecs4Amp(elecs4Amp_idx); % find the electrode for this iteration
                            for iii = 1:numel(elecs4PAC)
                                if strcmp(elecs4PAC{iii}, tempElec_from_elecs4Amp) % find the index of this iteration's electrode in elecs4PAC.
                                    freq4Power_elec_idx = iii; % the index of this iteration's electrode in elecs4PAC

                                    % Extract TF Power data for the chosen upper frequency from the picked channel
                                    power_data_upperFreq_chosenElec = squeeze(timefreqs_strial_ch(temp_upper_freq_idx,:,:,freq4Power_elec_idx)); % time points x trials

                                    % loop through the time points for which we
                                    % want to compute PAC (times4PAC)
                                    cfc_numcycles  = 3;   % number of cycles at phase-frequency
                                    % convert cfc times to indices
                                    current_freq4Phase = frex(temp_lower_freq_idx);
                                    current_freq4Power = frex(temp_upper_freq_idx);

                                    cfc_time_window = cfc_numcycles*(1000/current_freq4Phase);
                                    cfc_time_window_idx = round(cfc_time_window/(1000/srate));

                                    for timei=1:length(times4PAC)
                                        cfc_centertime_idx  = dsearchn(epoch_time',times4PAC(timei));
                                        % extract temporally localized power and phase from task data
                                        power_ts = power_data_upperFreq_chosenElec(cfc_centertime_idx-round(cfc_time_window_idx/2):cfc_centertime_idx+round(cfc_time_window_idx/2),:);
                                        phase_ts = phase_data_lowerFreq_chosenElec(cfc_centertime_idx-round(cfc_time_window_idx/2):cfc_centertime_idx+round(cfc_time_window_idx/2),:);

                                        % compute observed PAC for this time point,
                                        % lower freq., upper freq., and channel.
                                        obsPAC = abs(mean( power_ts(:).*exp(1i*phase_ts(:)) ));


                                        permutedPAC = zeros(1,num_perm_iter);
                                        for iter_counter=1:num_perm_iter

                                            % in contrast to the previous code, this time-shifts the power time series only within trials. Results are similar using either method.
                                            random_timepoint = randsample(round(cfc_time_window_idx*.8),size(data_cond1_temp,3),1)+round(cfc_time_window_idx*.1);
                                            for triali=1:size(data_cond1_temp,3)
                                                power_ts(:,triali) = power_ts([random_timepoint(triali):end 1:random_timepoint(triali)-1],triali);
                                            end

                                            permutedPAC(iter_counter) = abs(mean( power_ts(:).*exp(1i*phase_ts(:)) ));
                                        end % end the loop computing permuted PAC per iteration

                                        PACz = (obsPAC-mean(permutedPAC))/std(permutedPAC);
                                        % Condition variable
                                        % Note about conditions in the codes below:
                                        % cond1 refers to incong error response
                                        % cond2 refers to incong correct response
                                        
                                        is_this_error_resp_condition = 1; % error is 1 and correct is 0!

                                        % Create a new table row with the data for this iteration
                                        new_row = table(string(subject_id), subsample, current_freq4Phase, current_freq4Power, elecs4PAC(freq4Phase_elec_idx), elecs4PAC(freq4Power_elec_idx), times4PAC(timei), is_this_error_resp_condition, PACz, 'VariableNames', variable_names);
                                        % Append the new row to the current
                                        % subject's data table
                                        current_subject_data_cond1 = [current_subject_data_cond1; new_row];

                                    end % end the loop computing PACz per timepoint
                                end % end the if condition for tempElec_from_elecs4Amp
                            end % end the loop that allows to find tempElec_from_elecs4Amp
                        end % end the loop that finds the 
                    end % end upper frequency band loop
                end % end lower frequency band loop
                
                %% Save current subsample for this subject's data
                current_output_name_cond1 = append(save_location, 'sub-', string(subject_id), 'cond1_subsample_', string(subsample),'_PACz', '.csv');
                writetable(current_subject_data_cond1, current_output_name_cond1);
                
                %% END Condition 1
            end % end of the loop for subsampling
            subjEnd = toc(subjStart);
            fprintf('Processing error condition (cond1) completed for subject %s in %d hours %.3f minutes, continuing.\n', subject_id, floor(subjEnd/3600), rem(subjEnd,3600)/60);
            %fprintf('Processing completed on subject %s\n', subject_id);
            % perform convolution and obtain, phase, and power values for each TF
            % point.

            % Concatenate the data from the time-window of interest using these
            % num_pulled_trials trials.

            % compute observed PAC using this concatenated time-series data.
            % then compute PACz using the trials from this subsample

            % end this for the loop num_subsamples

            % then, compute the average observed PACz from the PACzs from each loop.

            % As this is an exploratory analyses (without a priori hypothesis
            % regarding exactly which frequency phase couples with the power of
            % exactly which upper frequency), we have an exploratory/exploratory
            % approach here.
            % Essentially, this is an a priori/exploratory approach as we pick
            % theta oscillations frequency range for the lower frequency band. However, we do not specify the
            % exact single frequency. So, it becomes an exploratory/exploratory
            % approach in practice.

            % In order to reduce the number of multiple comparisons, we compute
            % PACz across all conditions in order to identify the exact lower and
            % upper frequencies that have the highest coupling. See Cohen's book
            % pages 421 and 424 for more details.

            % PACz is computed across all conditions (equall number of trials from
            % both conditions).
            % Number of comparisons = (number of lower freq. bins) * (number of
            % upper freqs. bins) * (number of electrodes of interest)
            % So, here the Number of comparisons is
            % Number of comparisons = round(2.6 * 33.0435 * 12)


            % There are cases that power of the upper frequency band is time-locked
            % to the event of interest while there is an increase in the lower
            % frequency ITPC which is also time-locked to the event of interest. In
            % these cases, we may misinterpret and think that there is a phase
            % amplitude coupling between these two frequencies while there is not.
            % In order to avoid these, there are three solutions. Here, I
            % use a mixed method:
            % First, I compute ITPC for the TF ROI (4–7 Hz, 0–500 ms) with
            % subsampling (10 trials, 100 repitions). Then, I test to see if there
            % is a significant increase in the ITPC from this period relative to a baseline
            % period (-400 to -200 ms). If there is not a significant increase, we are good
            % and we don't need to do anything. However, if there is an increase in
            % ITPC, I subtract the ERP from the single trial EEG data before
            % computing PAC. (see chapter 20 to implement this in the code.)

            % PAC will be computed per channel of interest (not an average of channels of interets).

        else
            % do nothing (skip processing for this subject)
            disp(['Subject ', subject_id, ' did not have enough trials in condition 2']);
        end % end checking the mininmum number of trials per condition 2
    else
        % do nothig (skip processing for this subject)
        disp(['Subject ', subject_id, ' did not have enough trials in condition 1']);
    end % end checking the mininmum number of trials per condition 1

end % end of looping through all subjects


