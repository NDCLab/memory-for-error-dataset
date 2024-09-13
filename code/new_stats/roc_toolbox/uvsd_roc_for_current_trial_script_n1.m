% Author: Kianoosh Hosseini at NDCLab @FIU (https://Kianoosh.info; https://NDClab.com)
% Last Update: 2023-09-05 (YYYY-MM-DD)

%% Clear workspace and command window
clear all;
clc;

%% Main directory
mainDir = '/Users/kihossei/Documents/GitHub/memory-for-error-dataset/';

%% Define the directory to save the data to, and a variable to store file names
saveDir = fullfile(mainDir,'derivatives', 'preprocessed', 'roc_dat', 'uvsd_n1', 'current_trial');
% 
roc_startup
%% Load the data
rawData = roc_import_data('/Users/kihossei/Documents/GitHub/memory-for-error-dataset/derivatives/preprocessed/organized_csvDat_for_roc_toolbox/longDat_current_trial_n1_without_headers.csv');
% Note that rawData is a cell array of structures with the fields
% condLabels, subID, groupID, targf, and luref.

% For  this data, Condition 1 is 'Correct' and Condition 2 is 'error'.
%% Define some information about the design based on the first subject
[nConds,nBins] = size(rawData{1}.targf); % Number of conditions and rating bins
nSubs = length(rawData); % Number of subjects
fitStat = '-LL'; % The two options are '-LL' and 'SSE'

%% Fit the models to each subjects data, and save the rodData structure
subFiles = {};
for i = 1:length(rawData)
    % Initialize rocData anew for each subject
    rocData = [];
    
    % Fit the UVSD model to the data
    model = 'uvsd';
    modelID = 'uvsd_model';
    parNames = {'Dprime' 'Vo'};
    [x0, LB, UB] = gen_pars(model,nBins,nConds,parNames);
    rocData = roc_solver(rawData{i}.targf,rawData{i}.luref, ...
        model,fitStat,x0,LB,UB, ...
        'subID',rawData{i}.subID, ...
        'groupID',rawData{i}.groupID, ...
        'condLabels',rawData{i}.condLabels, ...
        'modelID',modelID, ...
        'saveFig',saveDir, ...
        'figTimeout',2, ...
        'append',rocData);
    
    
    % Save rocData to a .mat file for the current subject
    matFile = fullfile(saveDir,strcat(rawData{i}.subID,'_rocData.mat'));
    subFiles{i} = matFile;
    save(matFile,'rocData');
end

%% Extract the UVSD data
uvsdPrefix = fullfile(saveDir,'uvsd_group_data');
uvsdData = get_group_data(subFiles,'uvsd',1,'rocData','saveCSV',uvsdPrefix);
 
