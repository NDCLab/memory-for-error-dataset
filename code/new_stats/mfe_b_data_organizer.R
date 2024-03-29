# This script will load, and organize the pavlovia data for mfe_b study.
# For each participant, a single, new, organized csv file that has all the necessary information will be generated.
# Author: Kianoosh Hosseini at NDCLab @FIU (https://Kianoosh.info; https://NDClab.com)
# Last Update: 2023-02-21 (YYYY-MM-DD)



library(tidyverse)
library(dplyr)
library(stringr)

#Working directory should be the Psychopy experiment directory.
proje_wd <- "/Users/kihossei/Documents/GitHub/memory-for-error-dataset/materials/experiments/mfe_b"
setwd(proje_wd)

today <- Sys.Date()
today <- format(today, "%Y%m%d")

# Defining the input and output folders.
input_path <- paste(proje_wd, "data", sep ="/", collapse = NULL) # input data directory
output_path <- paste(proje_wd, "csv_output", sep ="/", collapse = NULL) # Directory that each new csv file will be stored
flanker_csv_fileName <- "_mfe_b_flankerDat.csv" # each output csv file will have this on its filename
surprise_csv_fileName <- "_mfe_b_surpriseDat.csv" # each output csv file will have this on its filename


## creating a list of all data csv files in the input folder.
datafiles_list <- c() # an empty list that will be filled in the next "for" loop!
csvSelect <- list.files(input_path, pattern = ".csv") # listing only csv files
for (i in 1:length(csvSelect)){
  temp_for_file <- ifelse (str_detect(csvSelect[i], "mfe_b", negate = FALSE), 1, 0)
  if (temp_for_file == 1){
    temp_list <- csvSelect[i]
    datafiles_list <- c(datafiles_list, temp_list)
  }
}



# will loop over all participant datafiles.
for(subject in 1:length(datafiles_list)){
  # creating an empty data frame that will store all the information drawn from the flanker task of a participant.
  # This data frame will be saved as a csv file for this participant.
  flanker_df <- setNames(data.frame(matrix(ncol = 22, nrow = 0)), c("participant_id", "current_trial_face", "pre_trial_face", "post_trial_face",
                                                                    "current_trial_accuracy", "pre_trial_accuracy", "post_trial_accuracy",
                                                                    "current_trial_congruency", "pre_trial_congruency", "post_trial_congruency",
                                                                    "current_trial_rt", "pre_trial_rt", "post_trial_rt",
                                                                    "current_trial_responded", "pre_trial_responded", "post_trial_responded",
                                                                    "current_trial_legitResponse", "pre_trial_legitResponse", "post_trial_legitResponse",
                                                                    "current_trial_resp_nums", "pre_trial_resp_nums", "post_trial_resp_nums"))
  # creating an empty data frame that will store all the information drawn from the surprise task of a participant.
  # This data frame will be saved as a csv file for this participant.
  surprise_df <- setNames(data.frame(matrix(ncol = 5, nrow = 0)), c("participant_id", "face", "is_new", "identified_as_new",
                                                                    "memory_surp_rt"))

  #for this participant, find the csv file
  psychopy_file <- paste(input_path,datafiles_list[subject], sep = "/", collapse = NULL)

  #read in the data for this participant, establish id, and remove extraneous variables
  psychopyDat <- read.csv(file = psychopy_file, stringsAsFactors = FALSE, na.strings=c("", "NA"))
  participant_id <- psychopyDat$id[1]

  psychopyDatTrim <- psychopyDat[c("id",
                                   "new", # The displayed face is new? This column stores the correct value of the task not the response from the subject
                                   "firstStim_sliderA1.response", # Which answer was selected as an answer in the surprise!
                                   "firstStim_sliderA1.rt",
                                   "congruent",
                                   "stimNum",
                                   "accuracy",
                                   "task1_stim_keyResp.keys",
                                   "textbox_errorNum.text", # stores the number of reported errors by subjects
                                   "bigFace.started",
                                   "surpriseFaces",
                                   "straightFace",
                                   "task1_stim_keyResp.rt", #  this stores reaction time for each trial
                                   "task_trial_loop.thisTrialN",
                                   "cb", "textbox_errorPercent.text")]
  ###################################
  if (psychopyDatTrim$cb[1] == "A"){
    #firstStim_sliderA1.response
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 1, 'New')
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 2, 'New')
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 3, 'New')
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 4, 'Old')
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 5, 'Old')
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 6, 'Old')

  } else if (psychopyDatTrim$cb[1] == "B"){
    #firstStim_sliderA1.response
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 1, 'Old')
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 2, 'Old')
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 3, 'Old')
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 4, 'New')
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 5, 'New')
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 6, 'New')
  }

  #remove practice trials and any rows that do not reflect experiment data
  remove_first_row <- psychopyDatTrim[c(-1),]
  remove_prac_trials <- subset(remove_first_row, !complete.cases(remove_first_row$bigFace.started)) # removes practice trials

  flankerDat <- subset(remove_prac_trials, complete.cases(remove_prac_trials$congruent)) # only keeps flanker trials and removes trials from surprise
  # memory and friendly tasks. # For this study, flankerDat should have only 160 rows!
  flankerDat$task1_stim_keyResp.rt <- str_replace_all(flankerDat$task1_stim_keyResp.rt,"\\[", "") # removes the bracket
  flankerDat$task1_stim_keyResp.rt <- str_replace_all(flankerDat$task1_stim_keyResp.rt,"\\]", "") # removes the bracket
  flankerDat$task1_stim_keyResp.rt <- gsub(",.*","",flankerDat$task1_stim_keyResp.rt) # removing the RT for the second response within the same trial.
  flankerDat$task1_stim_keyResp.rt <- as.numeric(flankerDat$task1_stim_keyResp.rt)


  # Lets add a column that tells how many responses have been made in a given flanker trial
  for (flanker_sub in 1:nrow(flankerDat)){
    response_keys <- str_extract_all(flankerDat$task1_stim_keyResp.keys[flanker_sub], "\\d+\\.?\\d*") # to extract all sequences of digits from the input string
    response_keys <- parse_number(response_keys[[1]]) # to convert the extracted numbers from character strings to numeric values.
    flankerDat$number_of_responses[flanker_sub] <- length(response_keys)
  }
   flankerDat$task1_stim_keyResp.keys <- as.numeric( str_extract(flankerDat$task1_stim_keyResp.keys, '[[:digit:]]')) #extracts the first number (first response) and converts them to numeric


  # loop over all flanker trials.
  for (trial in 1:nrow(flankerDat)){
    current_trial_face <- flankerDat$straightFace[trial]
    current_trial_congruency <- flankerDat$congruent[trial]
    current_trial_rt <- flankerDat$task1_stim_keyResp.rt[trial]
    current_trial_resp_nums <- flankerDat$number_of_responses[trial] # number of responses for the current trial

    if (flankerDat$task_trial_loop.thisTrialN[trial] == 0){ # if the trial is the first in its block
      pre_trial_face <- NA
      pre_trial_congruency <- NA
      pre_trial_rt <- NA
      pre_trial_resp_nums <- NA
    } else {
      pre_trial_face <- flankerDat$straightFace[trial - 1]
      pre_trial_congruency <- flankerDat$congruent[trial - 1]
      pre_trial_rt <- flankerDat$task1_stim_keyResp.rt[trial - 1]
      pre_trial_resp_nums <- flankerDat$number_of_responses[trial - 1]
    }
    if (flankerDat$task_trial_loop.thisTrialN[trial] == 31){ # if the trial is the last in its block
      post_trial_face <- NA
      post_trial_congruency <- NA
      post_trial_rt <- NA
      post_trial_resp_nums <- NA
    } else {
      post_trial_face <- flankerDat$straightFace[trial + 1]
      post_trial_congruency <- flankerDat$congruent[trial + 1]
      post_trial_rt <- flankerDat$task1_stim_keyResp.rt[trial + 1]
      post_trial_resp_nums <- flankerDat$number_of_responses[trial + 1]
    }

    if (is.na(flankerDat$task1_stim_keyResp.keys[trial])){ # When no response made in a flanker task trial
      current_trial_responded <- 0 # 0 = not responded; 1 = responded
      # Because of an error in the Python code for the Psychopy task, the accuracy values reported by Psychopy are not correct in trials with no response.
      # Thus, I am putting NAs for accuracy in trials in which no response has been made!
      current_trial_accuracy <- 0 # Accuracy is considered 0 when there is no response
    } else if (!is.na(flankerDat$task1_stim_keyResp.keys[trial])){ # When a response made in a flanker task trial
      current_trial_responded <- 1
      current_trial_accuracy <- flankerDat$accuracy[trial]
    }
    if (flankerDat$task_trial_loop.thisTrialN[trial] == 0){ # if the trial is the first in its block
      pre_trial_responded <- NA
      pre_trial_accuracy <- NA
    } else {
      if (is.na(flankerDat$task1_stim_keyResp.keys[trial - 1])){ # When no response made in a flanker task trial
        pre_trial_responded <- 0 # 0 = not responded; 1 = responded
        pre_trial_accuracy <- 0 # Accuracy is considered 0 when there is no response
      } else if (!is.na(flankerDat$task1_stim_keyResp.keys[trial - 1 ])){ # When a response made in a flanker task trial
        pre_trial_responded <- 1
        pre_trial_accuracy <- flankerDat$accuracy[trial - 1]
      }
    }
    if (flankerDat$task_trial_loop.thisTrialN[trial] == 31){ # if the trial is the last in its block
      post_trial_responded <- NA
      post_trial_accuracy <- NA
    } else {
      if (is.na(flankerDat$task1_stim_keyResp.keys[trial + 1])){ # When no response made in a flanker task trial
        post_trial_responded <- 0 # 0 = not responded; 1 = responded
        post_trial_accuracy <- 0 # Accuracy is considered 0 when there is no response
      } else if (!is.na(flankerDat$task1_stim_keyResp.keys[trial + 1 ])){ # When a response made in a flanker task trial
        post_trial_responded <- 1
        post_trial_accuracy <- flankerDat$accuracy[trial + 1]
      }
    }

    if (current_trial_responded == 1 && current_trial_rt > 0.15 ){
      current_trial_legitResponse <- 1
    } else {
      current_trial_legitResponse <- 0
    }
    if (flankerDat$task_trial_loop.thisTrialN[trial] == 0){
      pre_trial_legitResponse <- NA
    } else {
      if (pre_trial_responded == 1 && pre_trial_rt > 0.15 ){
        pre_trial_legitResponse <- 1
      } else {
        pre_trial_legitResponse <- 0
      }
    }

    if (flankerDat$task_trial_loop.thisTrialN[trial] == 31){
      post_trial_legitResponse <- NA
    } else {
      if (post_trial_responded == 1 && post_trial_rt > 0.15 ){
        post_trial_legitResponse <- 1
      } else {
        post_trial_legitResponse <- 0
      }
    }


    flanker_df[nrow(flanker_df) + 1,] <-c(participant_id, current_trial_face, pre_trial_face, post_trial_face,
                                          current_trial_accuracy, pre_trial_accuracy, post_trial_accuracy,
                                          current_trial_congruency, pre_trial_congruency, post_trial_congruency,
                                          current_trial_rt, pre_trial_rt, post_trial_rt,
                                          current_trial_responded, pre_trial_responded, post_trial_responded,
                                          current_trial_legitResponse, pre_trial_legitResponse, post_trial_legitResponse,
                                          current_trial_resp_nums, pre_trial_resp_nums, post_trial_resp_nums)
  } # Closing the loop for each trial

  flanker_name <- paste0(participant_id, flanker_csv_fileName, sep = "", collapse = NULL)
  write.csv(flanker_df, paste(output_path, flanker_name, sep = "/", collapse = NULL), row.names=FALSE) # Writing the flanker CSV file to disk

  ## Creating the Surprise csv file for each participant
  # We have two surprise tasks in this study. One is Surprise memory and the other is surprise friendly.
  surprise_memory_dat <- subset(remove_prac_trials, complete.cases(remove_prac_trials$new)) # keeps rows from the surprise memory task
  # Because of the code below, I replace new with 1 and Old with 0 in firstStim_sliderA1.response column.
  surprise_memory_dat$firstStim_sliderA1.response <- replace(surprise_memory_dat$firstStim_sliderA1.response, surprise_memory_dat$firstStim_sliderA1.response == 'Old', 0)
  surprise_memory_dat$firstStim_sliderA1.response <- replace(surprise_memory_dat$firstStim_sliderA1.response, surprise_memory_dat$firstStim_sliderA1.response == 'New', 1)

  # Looping through surprise memory trials.
  for (surpTrial in 1:nrow(surprise_memory_dat)){
    face <- surprise_memory_dat$surpriseFaces[surpTrial]
    is_new <- surprise_memory_dat$new[surpTrial] # 0 = This face is Old (shown during the flanker task); 1 = This face is New (not shown during the flanker task)
    memory_surp_rt <- surprise_memory_dat$firstStim_sliderA1.rt[surpTrial]

    if (surprise_memory_dat$new[surpTrial] == surprise_memory_dat$firstStim_sliderA1.response[surpTrial]){
      identified_as_new <- 1 # 1 = Participant has identified this face as New
    } else if(surprise_memory_dat$new[surpTrial] != surprise_memory_dat$firstStim_sliderA1.response[surpTrial]){
      identified_as_new <- 0 # 0 = Participant has identified this face as Old;
    }


    surprise_df[nrow(surprise_df) + 1,] <-c(participant_id, face, is_new, identified_as_new, memory_surp_rt)

  } # closing the surprise memory trial loop
  # Adding two additional columns to surprise_df to identify whether we should keep that trial in the surprise memory and friendly tasks or not.

  for (kk in 1:nrow(surprise_df)){
    surprise_df$keep_surp_memory_trial_based_on_rt[kk] <- ifelse (surprise_df$memory_surp_rt[kk] > 0.2, 1, 0)
  }

  surprise_name <- paste0(participant_id, surprise_csv_fileName, sep = "", collapse = NULL)
  write.csv(surprise_df, paste(output_path, surprise_name, sep = "/", collapse = NULL), row.names=FALSE) # Writing the surprise CSV file to disk


} # closing the loop for each participant


