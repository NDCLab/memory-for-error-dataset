
% INPUT
% data = single trial wavelet decomposed signal; frequency x time x trial x channel
%The input will come from the output of the strial_timefreq_decomposition_script.m
data=[];
data = phase_data_strial_ch;
                                               
% OUTPUT: wPLI_all
% frequency x non-seed channel 


%% Initialize output matrices depending on type of connectivity
%over time, seed-based
wPLI_all = zeros(size(data, 1), length(Elecs4Connect));

%% Kia has edited below this line to adapt for trial-level analyses.  
% SEED-BASED
fprintf('\n\n\n*** Calculating wPLI for subject %d (%s) ***\n\n\n', sub, subject);

%Find index of seed electrode
Seed_idx = find(strcmpi({EEG.chanlocs.labels},Seed));

% Find indices of the non-seed channels
for i=1:length(Elecs4Connect)
    Elecs_idx (i)= find(strcmp({EEG.chanlocs.labels}, Elecs4Connect{i}));
end
% Find indices of the time window that we want to the compute the mean
% over. 
time_window_for_wpli = [0 800]; 
if Downsample ==1
    time_window_idx = dsearchn(ds_time',time_window_for_wpli');
elseif Downsample ==0
    time_window_idx = dsearchn(time',time_window_for_wpli');
end

% take cross-spectral density
for chanj=1:length(Elecs4Connect)
    % take cross-spectral density between two channels - one being the seed for wPLI
    crossspecden = squeeze(data(:,:,:,Seed_idx) .* conj(data(:,:,:,Elecs_idx(chanj))));
    % take imaginary part of signal only
    crossspecden_imag = imag(crossspecden);
    %initialize matrix
    weighted_phaselagidx_seed = zeros(size(data, 1),1);
    for freq=1:size(data, 1)
        %wPLI for nonsubsampled seed-based over time
        weighted_phaselagidx_seed(freq) = abs(mean(exp(1i*angle(crossspecden_imag(freq,time_window_idx(1,1):time_window_idx(2,1),:))),2));
    end %end loop through frequencies
    wPLI_all(:,chanj) = weighted_phaselagidx_seed;
end % end loop through channels

%% Baseline Correct, Downsample, and Save Data
%Baseline Correction
if BaselineCorrect == 1
    %% baseline time indices
    basetimeidx   = dsearchn(EEG.times', BaselineTime');
    
    %% To perform baseline correction, we create another wPLI dataframe that is computed over the baseline period.
    wPLI_baseline = zeros(size(data, 1), length(Elecs4Connect));

    % take cross-spectral density
    for chanj=1:length(Elecs4Connect)
        % take cross-spectral density between two channels - one being the seed for wPLI
        crossspecden = squeeze(data(:,:,:,Seed_idx) .* conj(data(:,:,:,Elecs_idx(chanj))));
        % take imaginary part of signal only
        crossspecden_imag = imag(crossspecden);
        %initialize matrix
        weighted_phaselagidx_seed = zeros(size(data, 1),1);
        for freq=1:size(data, 1)
            %wPLI for nonsubsampled seed-based over time
            weighted_phaselagidx_seed(freq) = abs(mean(exp(1i*angle(crossspecden_imag(freq,basetimeidx(1):basetimeidx(end),:))),2));
        end %end loop through frequencies
        wPLI_baseline(:,chanj) = weighted_phaselagidx_seed;
    end % end loop through channels

    %Initialize wPLI_blncorr
    wPLI_blncorr = zeros(size(wPLI_all));

    %Baseline Correct
    for chanj=1:size(wPLI_all,2)
        for fi = 1:size(wPLI_all,1)
            wPLI_blncorr(fi,chanj) = ( wPLI_all(fi,chanj) - wPLI_baseline(fi,chanj) );
        end
    end

    if Downsample ==0
        %save out trial level and baseline corrected wPLI data for this subject
        save_data =[save_location, subject(1:end-4),DatasetName,'_wPLI_baselinecorrected_','resp_',Conds{dispImage}];
        save(save_data, 'wPLI_blncorr', 'frequency', 'time','channel_location', '-v7.3');
    elseif Downsample==1
        % Kia commented below
%         %Downsample
%         wPLI_blncorr=wPLI_blncorr(:,1:2:size(wPLI_blncorr,2),:,:);
% 
%         %Downsample time variable
%         ds_time = downsample(time,2);
% 
%         %save out trial level, downsampled, and baseline corrected wPLI data for this subject
%         save_data =[save_location, subject(1:end-4),DatasetName,'_wPLI_baselinecorrected_','resp_',Conds{dispImage}];
%         save(save_data, 'wPLI_blncorr', 'frequency', 'ds_time','channel_location', '-v7.3');
    end

elseif BaselineCorrect == 0
    if Downsample ==0
        %save out trial averaged and baseline corrected wPLI data for this subject
        save_data =[save_location, subject(1:end-4),DatasetName,'_wPLI_nobaselinecorrection_','resp_',Conds{dispImage}];
        save(save_data, 'wPLI_all', 'frequency', 'time','channel_location', '-v7.3');
    elseif Downsample ==1
        % Kia commented below
%         %Downsample
%         wPLI_all = wPLI_all(:,1:2:size(wPLI_all,2),:,:);
% 
%         %Downsample time variable
%         ds_time = downsample(time,2);
% 
%         %save out trial averaged and baseline corrected wPLI data for this subject
%         save_data =[save_location, subject(1:end-4),DatasetName,'_wPLI_nobaselinecorrection_','resp_',Conds{dispImage}];
%         save(save_data, 'wPLI_all', 'frequency', 'ds_time','channel_location', '-v7.3');
    end %end if downsampling
end %end if you want baseline correction


