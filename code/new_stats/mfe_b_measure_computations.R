# This script will load, and organize the pavlovia data. Then, computes measures of interest.
# For each participant, a single, new, organized csv file that has all the necessary information will be generated.
# Author: Kianoosh Hosseini at NDCLab @FIU (https://Kianoosh.info; https://NDClab.com)
# Last Update: 2023-02-23 (YYYY-MM-DD)

library(tidyverse)
library(dplyr)
library(stringr)
library(psycho) # to compute d' measures, etc.

#Working directory should be the Psychopy experiment directory.
proje_wd <- "/Users/kihossei/Documents/GitHub/memory-for-error-dataset/materials/experiments/mfe_b"
setwd(proje_wd)

input_raw_path <- paste(proje_wd, "data", sep ="/", collapse = NULL) # input data directory
input_organized_path <- paste(proje_wd, "csv_output", sep ="/", collapse = NULL) # input directory for data files generated by the organizer script!
output_path <- paste(proje_wd, "stat_output", sep ="/", collapse = NULL) # output directory
proc_fileName <- "processed_data_mfe_b_Proj.csv" # output filename
flanker_csv_fileName <- "_mfe_b_flankerDat.csv" # each output csv file will have this on its filename
surprise_csv_fileName <- "_mfe_b_surpriseDat.csv" # each output csv file will have this on its filename


## creating a list of all raw data csv files in the input folder.
raw_datafiles_list <- c() # an empty list that will be filled in the next "for" loop!
csvSelect <- list.files(input_raw_path, pattern = ".csv") # listing only csv files
for (i in 1:length(csvSelect)){
  temp_for_file <- ifelse (str_detect(csvSelect[i], "mfe_b", negate = FALSE), 1, 0)
  if (temp_for_file == 1){
    temp_list <- csvSelect[i]
    raw_datafiles_list <- c(raw_datafiles_list, temp_list)
  }
}
# Creating the main empty dataframe that will be filled with the data from the loop below:
main_df <- setNames(data.frame(matrix(ncol = 1, nrow = 0)), c("participant_id"))

# Counters for the number of excluded people based on each criterion
num_of_participants_removed_based_on_memory_surp_trial_removal <- 0 # Will be updated in the loop below
num_of_participants_removed_based_on_accuracy <- 0 # Will be updated in the loop below
num_of_participants_removed_based_on_incong_error_num <- 0 # Will be updated in the loop below
num_participants_removed_based_on_num_incong_error_faces_in_memory_surp <- 0 # Will be updated in the loop below

# Looping over all participants
for (subject in 1:length(raw_datafiles_list)){
  #for this participant, find the raw csv file
  psychopy_file <- paste(input_raw_path,raw_datafiles_list[subject], sep = "/", collapse = NULL)

  #read in the data for this participant, establish id, and remove extraneous variables
  psychopyDat <- read.csv(file = psychopy_file, stringsAsFactors = FALSE, na.strings=c("", "NA"))
  participant_id <- psychopyDat$id[1]

  # Load this participant's flanker and surprise data frames
  flanker_name <- paste0(participant_id, flanker_csv_fileName, sep = "", collapse = NULL)
  surprise_name <- paste0(participant_id, surprise_csv_fileName, sep = "", collapse = NULL)
  flanker_df <- read.csv(file = paste(input_organized_path, flanker_name, sep = "/", collapse = NULL), stringsAsFactors = FALSE, na.strings=c("", "NA"))
  surprise_df <- read.csv(file = paste(input_organized_path, surprise_name, sep = "/", collapse = NULL), stringsAsFactors = FALSE, na.strings=c("", "NA"))

  # removing participants based on whether they just pressed the keys without actually paying attention to the task.
  # We check this by "keep_surp_memory_trial_based_on_rt" and "keep_surp_friendly_trial_based_on_rt" variables
  # in the surprise_df data frame. O means that they have responded faster than 200 ms during the given trial
  # and therefore, we need to remove that surprise trial.
  # In this study, we will remove people based on the surprise memory task not surprise friendly task.
  # If more than 20% of surprise trials are removed, we exclude that participant.
  number_of_removed_trials_in_the_memory_surp <- nrow(surprise_df) - (sum(surprise_df$keep_surp_memory_trial_based_on_rt))
  number_of_faces_in_surp_memory_task <- nrow(surprise_df)
  twenty_percent_threshold <- round(0.2 * number_of_faces_in_surp_memory_task)

  if (number_of_removed_trials_in_the_memory_surp <= twenty_percent_threshold){ # Participants who have less than twenty_percent_threshold surprise
    # trials removed, will be included.

    # Check to see if this participant has the flanker accuracy above 60%
    if (mean(as.numeric(flanker_df$current_trial_accuracy)) >= 0.6){

      # check to see if the participant has at least 8 legit incongruent errors or not.
      incong_flankerDat <- filter(flanker_df, current_trial_congruency == 0)
      cong_flankerDat <- filter(flanker_df, current_trial_congruency == 1)
      error_incong_flankerDat <- filter(incong_flankerDat, current_trial_accuracy == 0)
      legit_error_incong_flankerDat <- filter(error_incong_flankerDat, current_trial_legitResponse == 1)
      if (nrow(legit_error_incong_flankerDat) >= 8 ){

        # Checking to see if there are at least 6 incongruent error faces in the surprise_df of this participant.
        # First we need to remove the trials that are marked based on rt!
        surprise_df <- filter(surprise_df, keep_surp_memory_trial_based_on_rt == 1)
        num_incong_error_faces_in_surp <- 0
        # Counting the number of legit incong error faces available in surprise_df!
        for (rr in 1:nrow(legit_error_incong_flankerDat)){
          temp_face <- legit_error_incong_flankerDat$current_trial_face[rr]
          temp_for_surp <- filter(surprise_df, face == temp_face)
          errorFace_exist_in_surpDat <- ifelse(nrow(temp_for_surp) == 1, 1,0)
          if (errorFace_exist_in_surpDat == 1){
            num_incong_error_faces_in_surp <- num_incong_error_faces_in_surp + 1
          }
        } # Closing the loop that counts the number of incong error faces available in surprise_df!
        if (num_incong_error_faces_in_surp >= 8){

          #### filling the main data frame
          main_df[nrow(main_df) + 1,] <-c(participant_id)


        } else { # If a participant has been excluded because they had less than 8 legit incong error faces in the surprise memory task, we add 1 to the counter below.
          num_participants_removed_based_on_num_incong_error_faces_in_memory_surp <- num_participants_removed_based_on_num_incong_error_faces_in_memory_surp + 1
        }
      } else { # If a participant has been excluded because they had less than 8 legit incong errors, we add 1 to the counter below.
        num_of_participants_removed_based_on_incong_error_num <- num_of_participants_removed_based_on_incong_error_num + 1
      }
    } else { # If a participant has been excluded because they had less than 60% flanker accuracy, we add 1 to the counter below.
      num_of_participants_removed_based_on_accuracy <- num_of_participants_removed_based_on_accuracy + 1
    }
  } else { # If a participant has been excluded because they had more than 20% surp trial removed, we add 1 to the counter below.
    num_of_participants_removed_based_on_memory_surp_trial_removal <- num_of_participants_removed_based_on_memory_surp_trial_removal + 1
  }
} # Closing the loop for each participant

####################
# Save the dataset
#write the extracted and computed summary scores to disk
write.csv(main_df, paste(output_path, proc_fileName, sep = "/", collapse = NULL), row.names=FALSE)
##################

