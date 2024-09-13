% Kia has edited this script to compute trial level TF power for mfe_b
% study in Dec. 2023.

% INPUT
data = EEG.data; % data = data matrix; channel x time/data points x trials
srate = EEG.srate; % srate = sampling rate;
% times = time vector / data time window;
% baseline = [xx xx]; time range/window to be used for baseline normalization
% min_freq = lowest frequency to analysis;
% max_freq = highest frequency to analysis;

% OUTPUT
% timefreq_data = frequency x time x channel matrix;
% times = time vector;
% frex = frequency vector;

% frequencies vector
frex = linspace(min_freq, max_freq, num_frex);
frequency = frex;

% cycles vector
cylvec = linspace(range_cycles(1),range_cycles(end), num_frex)./ (2*pi*frex);

%% wavelet parameters
wavtime = -1:1/srate:1; % length of wavelet
half_wave = (length(wavtime)-1)/2;

%% FFT parameters
nWave = length(wavtime);
nData = size(data, 2);
nConv = nWave + nData - 1;

%% Prepare data for wavelet
%Resting Data - only one trial type
%All to all connectivity
if ConnectType == 0
    %Loop through epochs and pull only epochs with appropriate number of
    %channels
    epochs2remove = [];
    for e=1:size(data,3) %begin loop through epochs
        %Only keep epoch if none of channels are NaNs
        for elec = 1:nbchan %begin loop through electrodes
            %check if the electrode is NaN within that epoch
            if sum(isnan(EEG.data(elec,:,e)))
                %add that epoch to vector
                epochs2remove = [epochs2remove e];
            else
                %do nothing
            end %end if loop for if channel within epoch is NaN
        end %end loop through electrodes
    end %end loop through epochs
    %remove all epochs with NaNs for channels of interest
    data(:,:,unique(epochs2remove))=[];
    %Seed-based connectivity
elseif ConnectType == 1
    epochs2remove=[];
    for e=1:size(data,3) %begin loop through epochs
        %Channel indices
        %concatenate Elecs4Connect and Seed to have vector of all
        %channels of interest
        Elecs4SeedBased = [Seed Elecs4Connect];

        %loop through and find indices of these electrodes
        for i=1:length(Elecs4SeedBased)
            Chan_idx (i)= find(strcmp({EEG.chanlocs.labels}, Elecs4SeedBased{i}));
        end
        %do any of these channels have NaNs in them?
        if min(sum(isnan(EEG.data(Chan_idx,:,e)))) > 0
            %if so, add that epoch to vector of epochs to be removed
            epochs2remove = [epochs2remove e];
        else
            %do nothing
        end %end if loop for if channel within epoch is NaN
    end %end loop through epochs
    %remove all epochs with NaNs for channels of interest
    data(:,:,unique(epochs2remove))=[];
    %keep only channels of interest
    data = data(Chan_idx,:,:);
end % end if all-to-all connectivity for rest

fprintf('\n\n\n*** Calculating TF for subject %d (%s) ***\n\n\n', sub, subject);

%% Run wavelet convolution
%%%%%%%%   Kia has changed below this line a lot.
% Kia: instead of condition, I will use dispImage. So, we have 384
% trials (displayed images in the flanker).
for dispImage=1:length(Conds)
    % Kia: Conds are actually trials from the flanker task.
    % check whether this image still exist in the loaded EEG data.

    for image_checker = 1:length(EEG.event)
        if strcmp(EEG.event(image_checker).dispImage, Conds{dispImage}) % True when the image was found in this trial:
            
            %pull out condition data
            cond_data = []; cond_EEG=[];
            cond_EEG = pop_selectevent( EEG, 'dispImage', Conds{dispImage}, 'deleteevents','on','deleteepochs','on','invertepochs','off');
            cond_data = eeg_checkset( cond_EEG.data );%add pulling out condition specific data
            % Kia: cond_data is a 2D matrix with channels x time points
      

            %Create TrialNums structure to be saved out
            TrialNums( sub+(dispImage-1)+((sub-1)*(length(Conds)-1)) ).subject = subject;
            TrialNums( sub+(dispImage-1)+((sub-1)*(length(Conds)-1)) ).condition = Conds{dispImage};
            TrialNums( sub+(dispImage-1)+((sub-1)*(length(Conds)-1)) ).TrialNum = size(cond_data,3);

            %initialize matrices
            timefreqs = zeros(length(frex), nData);
            phase_data = zeros(length(frex), nData);
            phase_data_strial_ch = zeros(length(frex),  nData, size(cond_data,1));
            timefreqs_strial_ch = zeros(length(frex),  nData, size(cond_data,1));
            timefreqs_data = zeros(length(frex),  nData,  size(cond_data,1));

            if size(cond_data,3)< mintrialnum
                data2save='';
                save([save_location subject(1:end-4) '_notenoughdata.mat'],data2save)
                break %go onto next subject if one condition doesn't have enough trials
            else
                %             if exist([save_location subject(1:end-4) '_notenoughdata.mat'],'file')==2
                %                 continue %skip any condition if the participant has already been deemed to not have enough data
                %             else
                for ch=1:size(cond_data, 1) % Loop through all channels
                    for fi=1:length(frex) % loop through all frequencies
                        trial_conv = zeros(nData, 1);
                        trial_temppow = zeros(nData,1);

                        %% Create wavelet
                        wavelet  = exp(2*1i*pi*frex(fi).*wavtime) .* exp(-wavtime.^2./(2*cylvec(fi)^2));
                        waveletX = fft(wavelet, nConv); % fft of wavelet
                        waveletX = waveletX ./ max(waveletX); % normalize fft of wavelet

                        temp_data = fft(squeeze(cond_data(ch,:)), nConv);

                        %% run convolution
                        temp_conv = ifft(waveletX .* temp_data);
                        temp_conv2 = temp_conv(half_wave+1:end-half_wave);

                        %% data for phase analysis
                        trial_conv (:) = temp_conv2;

                        %% compute power
                        trial_temppow (:) = abs(temp_conv(half_wave+1:end-half_wave)).^2;


                        %Build dataset for phase data
                        % Kia: phase data frex x time pnts
                        phase_data(fi,:) = trial_conv;

                        %Build dataset for TF
                        % Kia: TF data frex x time pnts
                        timefreqs(fi,:) = trial_temppow;

                    end % end loop through all frequencies

                    %Build dataset for phase data with channels
                    % Kia: phase data with channels is frex x time pnts x
                    % channels
                    phase_data_strial_ch(:,:,ch) = phase_data;

                    %Build dataset for TF with channels
                    timefreqs_strial_ch(:,:,ch) = timefreqs;
                end %end loop through channels


                %Inter-trial phase synchrony
                if ITPS_calc == 1
                    cd(scripts_location)
                    ITPS_script;
                    ITPS_all=[]; %blank out matrix when done
                else
                    %do nothing
                end


                %Inter-channel calculations
                if ICPS_calc == 1
                    cd(scripts_location)
                    if ICPS_or_wPLI == 1 %calculate coherence
                        ICPS_script;
                        ICPS_all=[]; %blank out matrix when done
                    elseif ICPS_or_wPLI == 0 %calculate wPLI
                        trial_level_wPLI_script;
                        wPLI_all=[]; %blank out matrix when done
                    end
                else
                    %do nothing
                end

            end %end if there is enough data for this condition
        elseif ~strcmp(EEG.event(image_checker).dispImage, Conds{dispImage}) % True when the image was not found in this trial:
            if image_checker == length(Conds) % check to see if this is the last trial for this subject.
                % If this is the last trial and not found the image,
                % display below:
                disp(['The image ',Conds{dispImage}, ' does not exist for participant ', subject])
            end
        end
    end % end the 'for' loop for checking whether this image exist for this subject
end %end loop through conditions

