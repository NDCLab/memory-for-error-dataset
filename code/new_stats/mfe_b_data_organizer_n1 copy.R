# This script will load, and organize the pavlovia data for mfe_b study.
# For each participant, a single, new, organized csv file that has all the necessary information will be generated.
# Author: Kianoosh Hosseini at NDCLab @FIU (https://Kianoosh.info; https://NDClab.com)
# Last Update: 2023-09-24 (YYYY-MM-DD)



library(tidyverse)
library(dplyr)
library(stringr)

#Working directory should be the Psychopy experiment directory.
proje_wd <- "/Users/kihossei/Documents/GitHub/memory-for-error-dataset"
setwd(proje_wd)

today <- Sys.Date()
today <- format(today, "%Y%m%d")
#
# Defining the input and output folders.
input_path <- paste(proje_wd, "sourcedata", "raw","psychopy", sep ="/", collapse = NULL) # input data directory
output_path <- paste(proje_wd, "derivatives", "preprocessed", "psychopy", "organizer_output", sep ="/", collapse = NULL) # Directory that each new csv file will be stored
flanker_csv_fileName <- "_mfe_b_flankerDat_n1.csv" # each output csv file will have this on its filename
surprise_csv_fileName <- "_mfe_b_surpriseDat_n1.csv" # each output csv file will have this on its filename


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
  surprise_df <- setNames(data.frame(matrix(ncol = 7, nrow = 0)), c("participant_id", "face", "is_new", "identified_as_new", "how_confident",
                                                                    "how_confident_all", "memory_surp_rt"))

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
  psychopyDatTrim <- psychopyDatTrim %>%
    add_column(surp_response_id = NA, surp_response_conf = NA, surp_response_conf_all = NA) #adds 3 columns consisting NAs
  # copying the surprise response column into the new columns added above so that I can replace the values according to the guide below (see If block below)
  psychopyDatTrim$surp_response_id <- psychopyDatTrim$firstStim_sliderA1.response # will include only new (1) and old (0)
  psychopyDatTrim$surp_response_conf <- psychopyDatTrim$firstStim_sliderA1.response # will include only def, prob, and maybe
  psychopyDatTrim$surp_response_conf_all <- psychopyDatTrim$firstStim_sliderA1.response # will include all 6 categories
  # These columns will be updated using the guide below:
  # surp_response_id -> new: -1; old: 1
  # surp_conf -> 5:definitely; 3: Probably; 1: Maybe
  # surp_response_conf_all -> # -5: Definitely new; -3: Probably new; -1: maybe new; 5: Definitely old; 3: Probably old; 1: maybe old
  ###################################
  # In counterbalance A: Left: New ; Right side: Old. So, numbers 1-3 below will be -1 and numbers 4-6 will be 1.
  if (psychopyDatTrim$cb[1] == "A"){
    psychopyDatTrim$surp_response_id <- replace(psychopyDatTrim$surp_response_id, psychopyDatTrim$surp_response_id == 1, -1)
    psychopyDatTrim$surp_response_id <- replace(psychopyDatTrim$surp_response_id, psychopyDatTrim$surp_response_id == 2, -1)
    psychopyDatTrim$surp_response_id <- replace(psychopyDatTrim$surp_response_id, psychopyDatTrim$surp_response_id == 3, -1)
    psychopyDatTrim$surp_response_id <- replace(psychopyDatTrim$surp_response_id, psychopyDatTrim$surp_response_id == 4, 1)
    psychopyDatTrim$surp_response_id <- replace(psychopyDatTrim$surp_response_id, psychopyDatTrim$surp_response_id == 5, 1)
    psychopyDatTrim$surp_response_id <- replace(psychopyDatTrim$surp_response_id, psychopyDatTrim$surp_response_id == 6, 1)

    psychopyDatTrim$surp_response_conf <- replace(psychopyDatTrim$surp_response_conf, psychopyDatTrim$surp_response_conf == 1, 5)
    psychopyDatTrim$surp_response_conf <- replace(psychopyDatTrim$surp_response_conf, psychopyDatTrim$surp_response_conf == 2, 3)
    psychopyDatTrim$surp_response_conf <- replace(psychopyDatTrim$surp_response_conf, psychopyDatTrim$surp_response_conf == 3, 1)
    psychopyDatTrim$surp_response_conf <- replace(psychopyDatTrim$surp_response_conf, psychopyDatTrim$surp_response_conf == 4, 1)
    psychopyDatTrim$surp_response_conf <- replace(psychopyDatTrim$surp_response_conf, psychopyDatTrim$surp_response_conf == 5, 3)
    psychopyDatTrim$surp_response_conf <- replace(psychopyDatTrim$surp_response_conf, psychopyDatTrim$surp_response_conf == 6, 5)

    psychopyDatTrim$surp_response_conf_all <- replace(psychopyDatTrim$surp_response_conf_all, psychopyDatTrim$surp_response_conf_all == 1, -5)
    psychopyDatTrim$surp_response_conf_all <- replace(psychopyDatTrim$surp_response_conf_all, psychopyDatTrim$surp_response_conf_all == 2, -3)
    psychopyDatTrim$surp_response_conf_all <- replace(psychopyDatTrim$surp_response_conf_all, psychopyDatTrim$surp_response_conf_all == 3, -1)
    psychopyDatTrim$surp_response_conf_all <- replace(psychopyDatTrim$surp_response_conf_all, psychopyDatTrim$surp_response_conf_all == 4, 1)
    psychopyDatTrim$surp_response_conf_all <- replace(psychopyDatTrim$surp_response_conf_all, psychopyDatTrim$surp_response_conf_all == 5, 3)
    psychopyDatTrim$surp_response_conf_all <- replace(psychopyDatTrim$surp_response_conf_all, psychopyDatTrim$surp_response_conf_all == 6, 5)

  } else if (psychopyDatTrim$cb[1] == "B"){
    # In counterbalance B: Left: Old ; Right side: New. So, numbers 1-3 below will be 1 and numbers 4-6 will be -1.
    psychopyDatTrim$surp_response_id <- replace(psychopyDatTrim$surp_response_id, psychopyDatTrim$surp_response_id == 1, 1)
    psychopyDatTrim$surp_response_id <- replace(psychopyDatTrim$surp_response_id, psychopyDatTrim$surp_response_id == 2, 1)
    psychopyDatTrim$surp_response_id <- replace(psychopyDatTrim$surp_response_id, psychopyDatTrim$surp_response_id == 3, 1)
    psychopyDatTrim$surp_response_id <- replace(psychopyDatTrim$surp_response_id, psychopyDatTrim$surp_response_id == 4, -1)
    psychopyDatTrim$surp_response_id <- replace(psychopyDatTrim$surp_response_id, psychopyDatTrim$surp_response_id == 5, -1)
    psychopyDatTrim$surp_response_id <- replace(psychopyDatTrim$surp_response_id, psychopyDatTrim$surp_response_id == 6, -1)

    psychopyDatTrim$surp_response_conf <- replace(psychopyDatTrim$surp_response_conf, psychopyDatTrim$surp_response_conf == 1, 5)
    psychopyDatTrim$surp_response_conf <- replace(psychopyDatTrim$surp_response_conf, psychopyDatTrim$surp_response_conf == 2, 3)
    psychopyDatTrim$surp_response_conf <- replace(psychopyDatTrim$surp_response_conf, psychopyDatTrim$surp_response_conf == 3, 1)
    psychopyDatTrim$surp_response_conf <- replace(psychopyDatTrim$surp_response_conf, psychopyDatTrim$surp_response_conf == 4, 1)
    psychopyDatTrim$surp_response_conf <- replace(psychopyDatTrim$surp_response_conf, psychopyDatTrim$surp_response_conf == 5, 3)
    psychopyDatTrim$surp_response_conf <- replace(psychopyDatTrim$surp_response_conf, psychopyDatTrim$surp_response_conf == 6, 5)

    psychopyDatTrim$surp_response_conf_all <- replace(psychopyDatTrim$surp_response_conf_all, psychopyDatTrim$surp_response_conf_all == 1, 5)
    psychopyDatTrim$surp_response_conf_all <- replace(psychopyDatTrim$surp_response_conf_all, psychopyDatTrim$surp_response_conf_all == 2, 3)
    psychopyDatTrim$surp_response_conf_all <- replace(psychopyDatTrim$surp_response_conf_all, psychopyDatTrim$surp_response_conf_all == 3, 1)
    psychopyDatTrim$surp_response_conf_all <- replace(psychopyDatTrim$surp_response_conf_all, psychopyDatTrim$surp_response_conf_all == 4, -1)
    psychopyDatTrim$surp_response_conf_all <- replace(psychopyDatTrim$surp_response_conf_all, psychopyDatTrim$surp_response_conf_all == 5, -3)
    psychopyDatTrim$surp_response_conf_all <- replace(psychopyDatTrim$surp_response_conf_all, psychopyDatTrim$surp_response_conf_all == 6, -5)
  }

  #remove practice trials and any rows that do not reflect experiment data
  remove_first_row <- psychopyDatTrim[c(-1),]
  remove_prac_trials <- subset(remove_first_row, !complete.cases(remove_first_row$bigFace.started)) # removes practice trials

  flankerDat <- subset(remove_prac_trials, complete.cases(remove_prac_trials$congruent)) # only keeps flanker trials and removes trials from surprise
  # memory and friendly tasks. # For this study, flankerDat should have only (12*32 =) 384 rows!
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
  # We have one surprise task in this study (i.e., Surprise memory)
  surprise_memory_dat <- subset(remove_prac_trials, complete.cases(remove_prac_trials$new)) # keeps rows from the surprise memory task

  # Looping through surprise memory trials.
  for (surpTrial in 1:nrow(surprise_memory_dat)){
    face <- surprise_memory_dat$surpriseFaces[surpTrial]
    is_new <- surprise_memory_dat$new[surpTrial] # 0 = This face is Old (shown during the flanker task); 1 = This face is New (not shown during the flanker task)
    memory_surp_rt <- surprise_memory_dat$firstStim_sliderA1.rt[surpTrial]
    how_confident <- surprise_memory_dat$surp_response_conf[surpTrial]
    how_confident_all <- surprise_memory_dat$surp_response_conf_all[surpTrial]
    # surp_response_id -> new: -1; old: 1
    if (surprise_memory_dat$surp_response_id[surpTrial] == -1){
      identified_as_new <- 1 # 1 = Participant has identified this face as New
    } else if(surprise_memory_dat$surp_response_id[surpTrial] == 1){
      identified_as_new <- 0  # 0 = Participant has identified this face as Old;
    }


    surprise_df[nrow(surprise_df) + 1,] <-c(participant_id, face, is_new, identified_as_new, how_confident, how_confident_all, memory_surp_rt)

  } # closing the surprise memory trial loop
  # Adding two additional columns to surprise_df to identify whether we should keep that trial in the surprise memory and friendly tasks or not.

  # Compute the mean Surprize RT for this subject
  mean_surp_rt <- mean(as.numeric(surprise_df$memory_surp_rt))
  surprise_df$mean_surp_rt <- mean_surp_rt
  # Compute the SD Surprize RT for this subject
  sd_surp_rt <- sd(as.numeric(surprise_df$memory_surp_rt))
  # Identifying the trials that needs to be excluded based too fast or too slow responses.
  num_tooFast_surpTrials <- 0
  num_tooSlow_surpTrials <- 0
  for (kk in 1:nrow(surprise_df)){
    if (surprise_df$memory_surp_rt[kk] <= (mean_surp_rt - 3*sd_surp_rt)){
      num_tooFast_surpTrials <- num_tooFast_surpTrials + 1
    } else if (surprise_df$memory_surp_rt[kk] >= (mean_surp_rt + 3*sd_surp_rt)){
      num_tooSlow_surpTrials <- num_tooSlow_surpTrials + 1
    }
    surprise_df$keep_surp_memory_trial_based_on_subjectLevel_rt[kk] <- ifelse (surprise_df$memory_surp_rt[kk] >= (mean_surp_rt - 3*sd_surp_rt) && surprise_df$memory_surp_rt[kk] <= (mean_surp_rt + 3*sd_surp_rt), 1, 0)
  }
  surprise_df$num_tooSlow_surpTrials <- num_tooSlow_surpTrials
  surprise_df$num_tooFast_surpTrials <- num_tooFast_surpTrials

  # Participants who choose one response in >= 90% cases in a given surprise task block, that block will be excluded. If they
  # have two blocks excluded because of this criterion, that participant will be excluded.
  surprise_df <- surprise_df %>%
    add_column(exclude_block_based_on_surp_response_frequency = NA, number_of_surp_resp_items_used = NA, num_repeated_ans_streaks = NA, each_streak_length = NA)
  surprise_df$number_of_surp_resp_items_used <- length(group_size(group_by(surprise_df,how_confident_all)))
  num_sub_blocks_excluded <- 0 # will count the number of to-be-excluded blocks for the current participant
  for (surp_block in 1:8){
    start_trial <- 1 + ((surp_block - 1) * 72)
    end_trial <- surp_block * 72
    current_surp_block <- surprise_df[start_trial:end_trial,]
    percent_of_max_surp_response <- (max(group_size(group_by(current_surp_block,how_confident_all)))/sum(group_size(group_by(current_surp_block,how_confident_all)))) * 100 # Percentage of the most chosen response in this block
    # if this percentage is >= 90, we label this block to be excluded later.
    if (percent_of_max_surp_response >= 90){
      surprise_df$exclude_block_based_on_surp_response_frequency[start_trial:end_trial] <- 1
      ### Printing output
      print(paste("Block ", surp_block," of participant", participant_id," was excluded due to response frequency criterion."))
      #### end of printing output
      num_sub_blocks_excluded <- num_sub_blocks_excluded + 1
    } else if (percent_of_max_surp_response < 90){
      surprise_df$exclude_block_based_on_surp_response_frequency[start_trial:end_trial] <- 0
    }

    # The other measure to identify if a subject is attending the task in a given block, is to see if they have select the same answer for
    # 12 consecutive trials.
    # If a subject loses 2 blocks because of this, they will be excluded.
    # As the counter tests the 12 following trials, we do not need to check the last 12 trials in a surp block.
    # So, I pick the "end_trial - 11" as the last trial in the loop below.
    last_trial_to_check <- end_trial - 12
    for (surprise_block_trial in start_trial:last_trial_to_check){

      # we take the chosen answer from every surprise trial in a block and keep it as a reference answer.
      # Then, we compare the answers from the 12 following trials.
      # we have a counter for this, if the response is the same and the counter reaches 12, this block will be labeled to be excluded.
      # However, if any following response (in less than 12 trials) is different, the counter will reset to 0.
      the_same_surp_answer_counter <- 0
      ref_surp_answer <- surprise_df$how_confident_all[surprise_block_trial]
      for (following_surp_trial in 1:12){
        following_surp_answer <- surprise_df$how_confident_all[following_surp_trial + surprise_block_trial]
        same_answer <- ifelse (ref_surp_answer == following_surp_answer, 1, 0)
        if (same_answer == 1){
          the_same_surp_answer_counter <- the_same_surp_answer_counter + 1
        } else {
          break # the answer is different. so, I break the counter loop to proceed with the following surprise_block_trial.
        }
      }

      # Count the number of times in a given block that participant has chosen the same answe for 12 consecutive times.
      if (the_same_surp_answer_counter == 12){
        ### Printing output
        print(paste("Participant ", participant_id, " has repeated ans in block ", surp_block))
        #### end of printing output
        break
      }
      if (surprise_block_trial == last_trial_to_check){
        break
      }
    }
  }



  surprise_name <- paste0(participant_id, surprise_csv_fileName, sep = "", collapse = NULL)
  write.csv(surprise_df, paste(output_path, surprise_name, sep = "/", collapse = NULL), row.names=FALSE) # Writing the surprise CSV file to disk


} # closing the loop for each participant

# Load each subject's surprise data to identify outlier subjects based on the sample mean surprise RT.
# So, if a subject's mean_surp_rt is smaller than or larger than 3SD of the mean_sample_surp_rt, that subject will be labeled to be excluded later.

## creating a list of all data csv files in the input folder.
datafiles_list <- c() # an empty list that will be filled in the next "for" loop!
csvSelect <- list.files(output_path, pattern = ".csv") # listing only csv files
for (i in 1:length(csvSelect)){
  temp_for_file <- ifelse (str_detect(csvSelect[i], "_mfe_b_surpriseDat_n1", negate = FALSE), 1, 0)
  if (temp_for_file == 1){
    temp_list <- csvSelect[i]
    datafiles_list <- c(datafiles_list, temp_list)
  }
}

# create an empty data frame that has 2 columns. One is subject ID and the other is the mean_surp_rt.
surprise_rt_dat <- setNames(data.frame(matrix(ncol = 2, nrow = 0)), c("participant_id", "mean_surp_rt"))

for (surprise_subject in 1:length(datafiles_list)){

  #for this participant, find the surprise csv file
  surprise_file <- paste(output_path,datafiles_list[surprise_subject], sep = "/", collapse = NULL)

  #read in the data for this participant, establish id, and remove extraneous variables
  current_sub_surp_dat <- read.csv(file = surprise_file, stringsAsFactors = FALSE, na.strings=c("", "NA"))

  participant_id <- current_sub_surp_dat$participant_id[1]
  mean_surp_rt <- current_sub_surp_dat$mean_surp_rt[1]
  surprise_rt_dat[nrow(surprise_rt_dat) + 1,] <- c(participant_id, mean_surp_rt)
}

# Compute the sample mean and SD of the surprise rt to identify which participants are outlier in terms of +-3SD of sample mean surp rt.
sample_mean_surp_rt <- mean(as.numeric(surprise_rt_dat$mean_surp_rt))
sample_sd_surp_rt <- sd(as.numeric(surprise_rt_dat$mean_surp_rt))

# Load surprise data and add a column telling whether this subject is an outlier based on sample surprise rt or not.
for (surprise_subject in 1:length(datafiles_list)){

  #for this participant, find the surprise csv file
  surprise_file <- paste(output_path,datafiles_list[surprise_subject], sep = "/", collapse = NULL)

  #read in the data for this participant, establish id, and remove extraneous variables
  surprise_df <- read.csv(file = surprise_file, stringsAsFactors = FALSE, na.strings=c("", "NA"))

  participant_id <- surprise_df$participant_id[1]
  surprise_df$sample_mean_surp_rt <- sample_mean_surp_rt
  subject_mean_surp_rt <- surprise_df$mean_surp_rt[1]
  surprise_df$keep_this_sub_based_on_sample_surp_rt <- ifelse (subject_mean_surp_rt >= (sample_mean_surp_rt - 3*sample_sd_surp_rt) && subject_mean_surp_rt <= (sample_mean_surp_rt + 3*sample_sd_surp_rt), 1, 0)

  surprise_name <- paste0(participant_id, surprise_csv_fileName, sep = "", collapse = NULL)
  write.csv(surprise_df, paste(output_path, surprise_name, sep = "/", collapse = NULL), row.names=FALSE) # Writing the surprise CSV file to disk
}



