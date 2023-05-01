# This script allows to run statistical analysis on Psychopy output of the big memory for error project.
# Author: Kianoosh Hosseini at NDCLab @FIU (May-September 2022; https://Kianoosh.info; https://NDClab.com)
# Last Update: 2022-11-07 (YYYY-MM-DD)

library(tidyverse)
library(dplyr)
library(stringr)
library(ggplot2)


#Working directory should be the Psychopy experiment directory.
proje_wd <- "~/Documents/GitHub/memory-for-error-dataset/materials/experiments/mfe_b"
setwd(proje_wd)

today <- Sys.Date()
today <- format(today, "%Y%m%d")

# Defining the input and output folders.
input_path <- paste(proje_wd, "data", sep ="/", collapse = NULL) # input data directory
output_path <- paste(proje_wd, "stat_output", sep ="/", collapse = NULL) # output directory
proc_fileName <- paste(today, "_mfeProj.csv", sep ="", collapse = NULL) # output filename

#identify data files
datafiles_list <- c() # an empty list that will be filled in the next "for" loop!
csvSelect <- list.files(input_path, pattern = ".csv") # listing only csv files
for (lisar1 in 1:length(csvSelect)){
  temp_for_file <- ifelse (str_detect(csvSelect[lisar1], "mfe_b", negate = FALSE), 1, 0)
  if (temp_for_file == 1){
    temp_list <- csvSelect[lisar1]
    datafiles_list <- c(datafiles_list, temp_list)
  }
}

# Creating the main empty dataframe that will be filled with the data from the loop below:
percent_mainDat <- setNames(data.frame(matrix(ncol = 32, nrow = 0)), c("id", "congAcc", "incongAcc", "congCorr_meanRT", "incongCorr_meanRT", "congCorr_logMeanRT", "incongCorr_logMeanRT",
                                                                       "flankEff_meanACC", "flankEff_meanRT", "flankEff_logMeanRT",
                                                                       "reported_errors", "committed_errors", "memoryBias_score",
                                                                       "num_incong_errors",
                                                                       "num_foilFaces_reported_definitely_old", "num_foilFaces_reported_probably_old",
                                                                       "num_foilFaces_reported_maybe_old", "num_foilFaces_reported_maybe_new", "num_foilFaces_reported_probably_new",
                                                                       "num_foilFaces_reported_definitely_new", "num_incong_corrFaces_reported_definitely_new", "num_incong_corrFaces_reported_definitely_old", "num_incong_corrFaces_reported_probably_new",
                                                                       "num_incong_corrFaces_reported_probably_old", "num_incong_corrFaces_reported_maybe_new", "num_incong_corrFaces_reported_maybe_old",
                                                                       "num_incong_errorFaces_reported_definitely_new", "num_incong_errorFaces_reported_definitely_old", "num_incong_errorFaces_reported_probably_new",
                                                                       "num_incong_errorFaces_reported_probably_old", "num_incong_errorFaces_reported_maybe_new", "num_incong_errorFaces_reported_maybe_old"))

outlier_mainDat <- setNames(data.frame(matrix(ncol = 14, nrow = 0)), c("id", "congAcc", "incongAcc", "congCorr_meanRT", "incongCorr_meanRT", "congCorr_logMeanRT", "incongCorr_logMeanRT",
                                                                       "flankEff_meanACC", "flankEff_meanRT", "flankEff_logMeanRT",
                                                                       "reported_errors", "committed_errors", "memoryBias_score", "num_incong_errors"))

# will loop over all participant datafiles.
for(i in 1:length(datafiles_list)){
  #for this participant, find the csv file
  psychopy_file <- paste(input_path,datafiles_list[i], sep = "/", collapse = NULL)

  #read in the data for this participant, establish id, and remove extraneous variables
  psychopyDat <- read.csv(file = psychopy_file, stringsAsFactors = FALSE, na.strings=c("", "NA"))
  id <- psychopyDat$id[1]
  psychopyDatTrim <- psychopyDat[c("id",
                                   "new", # The displayed face is new? This column stores the correct value of the task not the response from the subject
                                   "firstStim_sliderA1.response", # Which answer was selected as an answer in the surprise!
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
                                   "cb")] # This stores the number of trial in a block; For this study it starts from 0 to 31
  #                                                                 as we have 32 trials in each block.
  ###################################
  #### SECTION 1:
  if (psychopyDatTrim$cb[1] == "A"){
    #firstStim_sliderA1.response
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 1, 'definitely_new')
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 2, 'probably_new')
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 3, 'maybe_new')
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 4, 'maybe_old')
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 5, 'probably_old')
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 6, 'definitely_old')

  } else if (psychopyDatTrim$cb[1] == "B"){
    #firstStim_sliderA1.response
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 1, 'definitely_old')
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 2, 'probably_old')
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 3, 'maybe_old')
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 4, 'maybe_new')
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 5, 'probably_new')
    psychopyDatTrim$firstStim_sliderA1.response <- replace(psychopyDatTrim$firstStim_sliderA1.response, psychopyDatTrim$firstStim_sliderA1.response == 6, 'definitely_new')
  }

  #remove practice trials and any rows that do not reflect experiment data
  remove_first_row <- psychopyDatTrim[c(-1),]
  remove_prac_trials <- subset(remove_first_row, !complete.cases(remove_first_row$bigFace.started)) # removes practice trials
  # Calculate the overall accuracy in the main task
  accuracy <- mean(remove_prac_trials$accuracy, na.rm = TRUE)
  # Calculate the average accuracy in congruent trials
  congDat <- filter(remove_prac_trials, congruent ==1) # subset the data for congruent trials.
  congAcc <- mean(congDat$accuracy, na.rm = TRUE) # mean accuracy for congruent trials
  # Calculate the average accuracy in incongruent trials
  incongDat <- filter(remove_prac_trials, congruent ==0) # subset the data for incongruent trials.
  incongAcc <- mean(incongDat$accuracy, na.rm = TRUE) # mean accuracy for incongruent trials


  keep_rows_with_acc_vals <- subset(remove_prac_trials, complete.cases(remove_prac_trials$accuracy))
  errorDat <- filter(keep_rows_with_acc_vals, accuracy ==0) # subset error trials
  errorDat$task1_stim_keyResp.rt <- gsub("[", "", errorDat$task1_stim_keyResp.rt, fixed = TRUE) #removing brackets and converting to numeric
  errorDat$task1_stim_keyResp.rt <- gsub("]", "", errorDat$task1_stim_keyResp.rt, fixed = TRUE)
  errorDat$task1_stim_keyResp.rt <- gsub(",.*","",errorDat$task1_stim_keyResp.rt) # removing the RT for the second response within the same trial.
  errorDat$task1_stim_keyResp.rt <- as.numeric(errorDat$task1_stim_keyResp.rt) #
  errorDat <- subset(errorDat, complete.cases(errorDat$task1_stim_keyResp.rt))
  incong_errorDat <- filter(errorDat, congruent ==0) # subset incongruent error trials
  corrDat <- filter(keep_rows_with_acc_vals, accuracy ==1) # subset correct trials
  corrDat$task1_stim_keyResp.rt <- gsub("[", "", corrDat$task1_stim_keyResp.rt, fixed = TRUE)
  corrDat$task1_stim_keyResp.rt <- gsub("]", "", corrDat$task1_stim_keyResp.rt, fixed = TRUE)
  corrDat$task1_stim_keyResp.rt <-  gsub(",.*","",corrDat$task1_stim_keyResp.rt)
  corrDat$task1_stim_keyResp.rt <- as.numeric(corrDat$task1_stim_keyResp.rt) #
  corrDat <- subset(corrDat, complete.cases(corrDat$task1_stim_keyResp.rt))



  # subset the data for correct trials only, separately for congruent and incongruent trials, creating new data frames for each
  cong_corrDat <- corrDat[corrDat$congruent == 1,]
  incong_corrDat <- corrDat[corrDat$congruent == 0,]
  #for correct trials, compute mean RT (raw and log-corrected)
  congCorr_meanRT <- mean(cong_corrDat$task1_stim_keyResp.rt)
  incongCorr_meanRT <- mean(incong_corrDat$task1_stim_keyResp.rt)

  congCorr_logMeanRT <- mean(log((1+cong_corrDat$task1_stim_keyResp.rt)))
  incongCorr_logMeanRT <- mean(log((1+incong_corrDat$task1_stim_keyResp.rt)))

  # compute flanker-effect scores for accuracy, RT, log-RT
  flankEff_meanACC <- incongAcc - congAcc
  flankEff_meanRT <- incongCorr_meanRT - congCorr_meanRT
  flankEff_logMeanRT <- incongCorr_logMeanRT - congCorr_logMeanRT

  # number of errors made in the main task
  committed_errors <- 0
  for (khata in 1:nrow(keep_rows_with_acc_vals)){
    if (keep_rows_with_acc_vals$accuracy[khata] == 0){
      committed_errors <- committed_errors +1
    }
  }
  reported_errors <- subset(remove_prac_trials, complete.cases(remove_prac_trials$textbox_errorNum.text))
  reported_errors <- reported_errors$textbox_errorNum.text # number of reported errors by participants
  if (length(reported_errors) == 0){ # in case a participant does not answer the question, this code will prevent from future errors.
    reported_errors <- NA
    memoryBias_score <- NA
  } else {
    memoryBias_score <- ( reported_errors - committed_errors)/ abs(reported_errors) # percent bias score calculation
  }
  surpDat <- subset(remove_prac_trials, complete.cases(remove_prac_trials$new)) #contains all the data we need from the surprise task

  num_incong_errors <- nrow(incong_errorDat)
  # Participants with less than 8 incong errors are considered outliers. This may be updated according to the data mean and SD.
  outlier_num <- 8
  if (nrow(incong_errorDat) >= outlier_num){ #for when the participant has outlier_num or more than outlier_num incongruent errors
    #######################################
    ######## SECTION 2: Surprise Task
    # Let's keep only the surprise trials that have faces from error trials in the main task. Then, we will be able to easily use that smaller dataframe to calculate the number of OLD faces among error trials.
    # Loop over the faces from error trials.
    # to prevent errors when there is no incong_errors:
    if (nrow(incong_errorDat) != 0){
      num_incong_errorFaces_reported_definitely_old <- 0 # this is the number of error faces that they report as OLD and will be updated in the loop below:
      for (Jafa in 1:nrow(incong_errorDat)){
        temp_face <- incong_errorDat$straightFace[Jafa]
        temp_for_surp <- filter(surpDat, surpriseFaces == temp_face)
        identified_old_correctly <- ifelse (temp_for_surp$firstStim_sliderA1.response == 'definitely_old', 1, 0)
        if (identified_old_correctly == 1){
          num_incong_errorFaces_reported_definitely_old <- num_incong_errorFaces_reported_definitely_old + 1 # The number of error faces that they report as OLD
        }
      }
    } else {
      num_incong_errorFaces_reported_definitely_old <- 0
    }
    #####
    if (nrow(incong_errorDat) != 0){
      num_incong_errorFaces_reported_probably_old <- 0 # this is the number of error faces that they report as OLD and will be updated in the loop below:
      for (Jafa in 1:nrow(incong_errorDat)){
        temp_face <- incong_errorDat$straightFace[Jafa]
        temp_for_surp <- filter(surpDat, surpriseFaces == temp_face)
        identified_old_correctly <- ifelse (temp_for_surp$firstStim_sliderA1.response == 'probably_old', 1, 0)
        if (identified_old_correctly == 1){
          num_incong_errorFaces_reported_probably_old <- num_incong_errorFaces_reported_probably_old + 1 # The number of error faces that they report as OLD
        }
      }
    } else {
      num_incong_errorFaces_reported_probably_old <- 0
    }
    #####
    if (nrow(incong_errorDat) != 0){
      num_incong_errorFaces_reported_maybe_old <- 0 # this is the number of error faces that they report as OLD and will be updated in the loop below:
      for (Jafa in 1:nrow(incong_errorDat)){
        temp_face <- incong_errorDat$straightFace[Jafa]
        temp_for_surp <- filter(surpDat, surpriseFaces == temp_face)
        identified_old_correctly <- ifelse (temp_for_surp$firstStim_sliderA1.response == 'maybe_old', 1, 0)
        if (identified_old_correctly == 1){
          num_incong_errorFaces_reported_maybe_old <- num_incong_errorFaces_reported_maybe_old + 1 # The number of error faces that they report as OLD
        }
      }
    } else {
      num_incong_errorFaces_reported_maybe_old <- 0
    }
    #####
    if (nrow(incong_errorDat) != 0){
      num_incong_errorFaces_reported_maybe_new <- 0 # this is the number of error faces that they report as OLD and will be updated in the loop below:
      for (Jafa in 1:nrow(incong_errorDat)){
        temp_face <- incong_errorDat$straightFace[Jafa]
        temp_for_surp <- filter(surpDat, surpriseFaces == temp_face)
        identified_new_incorrectly <- ifelse (temp_for_surp$firstStim_sliderA1.response == 'maybe_new', 1, 0)
        if (identified_new_incorrectly == 1){
          num_incong_errorFaces_reported_maybe_new <- num_incong_errorFaces_reported_maybe_new + 1
        }
      }
    } else {
      num_incong_errorFaces_reported_maybe_new <- 0
    }
    #####
    if (nrow(incong_errorDat) != 0){
      num_incong_errorFaces_reported_probably_new <- 0 # this is the number of error faces that they report as OLD and will be updated in the loop below:
      for (Jafa in 1:nrow(incong_errorDat)){
        temp_face <- incong_errorDat$straightFace[Jafa]
        temp_for_surp <- filter(surpDat, surpriseFaces == temp_face)
        identified_new_incorrectly <- ifelse (temp_for_surp$firstStim_sliderA1.response == 'probably_new', 1, 0)
        if (identified_new_incorrectly == 1){
          num_incong_errorFaces_reported_probably_new <- num_incong_errorFaces_reported_probably_new + 1
        }
      }
    } else {
      num_incong_errorFaces_reported_probably_new <- 0
    }
    #####
    if (nrow(incong_errorDat) != 0){
      num_incong_errorFaces_reported_definitely_new <- 0 # this is the number of error faces that they report as OLD and will be updated in the loop below:
      for (Jafa in 1:nrow(incong_errorDat)){
        temp_face <- incong_errorDat$straightFace[Jafa]
        temp_for_surp <- filter(surpDat, surpriseFaces == temp_face)
        identified_new_incorrectly <- ifelse (temp_for_surp$firstStim_sliderA1.response == 'definitely_new', 1, 0)
        if (identified_new_incorrectly == 1){
          num_incong_errorFaces_reported_definitely_new <- num_incong_errorFaces_reported_definitely_new + 1
        }
      }
    } else {
      num_incong_errorFaces_reported_definitely_new <- 0
    }
    ########## Correct faces Old vs. New ################
    if (nrow(incong_corrDat) != 0){
      num_incong_corrFaces_reported_definitely_old <- 0 # this is the number of error faces that they report as OLD and will be updated in the loop below:
      for (Jafa in 1:nrow(incong_corrDat)){
        temp_face <- incong_corrDat$straightFace[Jafa]
        temp_for_surp <- filter(surpDat, surpriseFaces == temp_face)
        identified_old_correctly <- ifelse (temp_for_surp$firstStim_sliderA1.response == 'definitely_old', 1, 0)
        if (identified_old_correctly == 1){
          num_incong_corrFaces_reported_definitely_old <- num_incong_corrFaces_reported_definitely_old + 1 # The number of error faces that they report as OLD
        }
      }
    } else {
      num_incong_corrFaces_reported_definitely_old <- 0
    }
    #####
    if (nrow(incong_corrDat) != 0){
      num_incong_corrFaces_reported_probably_old <- 0 # this is the number of error faces that they report as OLD and will be updated in the loop below:
      for (Jafa in 1:nrow(incong_corrDat)){
        temp_face <- incong_corrDat$straightFace[Jafa]
        temp_for_surp <- filter(surpDat, surpriseFaces == temp_face)
        identified_old_correctly <- ifelse (temp_for_surp$firstStim_sliderA1.response == 'probably_old', 1, 0)
        if (identified_old_correctly == 1){
          num_incong_corrFaces_reported_probably_old <- num_incong_corrFaces_reported_probably_old + 1 # The number of error faces that they report as OLD
        }
      }
    } else {
      num_incong_corrFaces_reported_probably_old <- 0
    }
    #####
    if (nrow(incong_corrDat) != 0){
      num_incong_corrFaces_reported_maybe_old <- 0 # this is the number of error faces that they report as OLD and will be updated in the loop below:
      for (Jafa in 1:nrow(incong_corrDat)){
        temp_face <- incong_corrDat$straightFace[Jafa]
        temp_for_surp <- filter(surpDat, surpriseFaces == temp_face)
        identified_old_correctly <- ifelse (temp_for_surp$firstStim_sliderA1.response == 'maybe_old', 1, 0)
        if (identified_old_correctly == 1){
          num_incong_corrFaces_reported_maybe_old <- num_incong_corrFaces_reported_maybe_old + 1 # The number of error faces that they report as OLD
        }
      }
    } else {
      num_incong_corrFaces_reported_maybe_old <- 0
    }
    #####
    if (nrow(incong_corrDat) != 0){
      num_incong_corrFaces_reported_maybe_new <- 0 # this is the number of error faces that they report as OLD and will be updated in the loop below:
      for (Jafa in 1:nrow(incong_corrDat)){
        temp_face <- incong_corrDat$straightFace[Jafa]
        temp_for_surp <- filter(surpDat, surpriseFaces == temp_face)
        identified_new_incorrectly <- ifelse (temp_for_surp$firstStim_sliderA1.response == 'maybe_new', 1, 0)
        if (identified_new_incorrectly == 1){
          num_incong_corrFaces_reported_maybe_new <- num_incong_corrFaces_reported_maybe_new + 1
        }
      }
    } else {
      num_incong_corrFaces_reported_maybe_new <- 0
    }
    #####
    if (nrow(incong_corrDat) != 0){
      num_incong_corrFaces_reported_probably_new <- 0 # this is the number of error faces that they report as OLD and will be updated in the loop below:
      for (Jafa in 1:nrow(incong_corrDat)){
        temp_face <- incong_corrDat$straightFace[Jafa]
        temp_for_surp <- filter(surpDat, surpriseFaces == temp_face)
        identified_new_incorrectly <- ifelse (temp_for_surp$firstStim_sliderA1.response == 'probably_new', 1, 0)
        if (identified_new_incorrectly == 1){
          num_incong_corrFaces_reported_probably_new <- num_incong_corrFaces_reported_probably_new + 1
        }
      }
    } else {
      num_incong_corrFaces_reported_probably_new <- 0
    }
    #####
    if (nrow(incong_corrDat) != 0){
      num_incong_corrFaces_reported_definitely_new <- 0 # this is the number of error faces that they report as OLD and will be updated in the loop below:
      for (Jafa in 1:nrow(incong_corrDat)){
        temp_face <- incong_corrDat$straightFace[Jafa]
        temp_for_surp <- filter(surpDat, surpriseFaces == temp_face)
        identified_new_incorrectly <- ifelse (temp_for_surp$firstStim_sliderA1.response == 'definitely_new', 1, 0)
        if (identified_new_incorrectly == 1){
          num_incong_corrFaces_reported_definitely_new <- num_incong_corrFaces_reported_definitely_new + 1
        }
      }
    } else {
      num_incong_corrFaces_reported_definitely_new <- 0
    }
    #####################################################
    #####
    # Number of foil faces reported new? old?
    num_foilFaces_reported_definitely_new <- 0
    num_foilFaces_reported_probably_new <- 0
    num_foilFaces_reported_maybe_new <- 0
    num_foilFaces_reported_definitely_old <- 0
    num_foilFaces_reported_probably_old <- 0
    num_foilFaces_reported_maybe_old <- 0

    for (foil_num in 1:nrow(surpDat)){
      if (surpDat$new[foil_num] == 1){
        if (surpDat$firstStim_sliderA1.response[foil_num] == 'definitely_new'){
          num_foilFaces_reported_definitely_new <- num_foilFaces_reported_definitely_new + 1
        } else if (surpDat$firstStim_sliderA1.response[foil_num] == 'probably_new'){
          num_foilFaces_reported_probably_new <- num_foilFaces_reported_probably_new + 1
        } else if (surpDat$firstStim_sliderA1.response[foil_num] == 'maybe_new'){
          num_foilFaces_reported_maybe_new <- num_foilFaces_reported_maybe_new + 1
        } else if (surpDat$firstStim_sliderA1.response[foil_num] == 'maybe_old'){
          num_foilFaces_reported_maybe_old <- num_foilFaces_reported_maybe_old + 1
        } else if (surpDat$firstStim_sliderA1.response[foil_num] == 'probably_old'){
          num_foilFaces_reported_probably_old <- num_foilFaces_reported_probably_old + 1
        } else if (surpDat$firstStim_sliderA1.response[foil_num] == 'definitely_old'){
          num_foilFaces_reported_definitely_old <- num_foilFaces_reported_definitely_old + 1
        }
      }
    }
    ##### Plot for each participant #####
    participant_plot_error <- data.frame(name = c("num_incong_errorFaces_reported_definitely_new", "num_incong_errorFaces_reported_probably_new", "num_incong_errorFaces_reported_maybe_new",
                                "num_incong_errorFaces_reported_definitely_old", "num_incong_errorFaces_reported_probably_old", "num_incong_errorFaces_reported_maybe_old"), value = c(num_incong_errorFaces_reported_definitely_new, num_incong_errorFaces_reported_probably_new, num_incong_errorFaces_reported_maybe_new,
                                     num_incong_errorFaces_reported_definitely_old, num_incong_errorFaces_reported_probably_old, num_incong_errorFaces_reported_maybe_old))
    error_label <- paste("Participant plot for Error", as.character(i), collapse = ", ")
    print(ggplot(data.frame(participant_plot_error),aes(x= name, y=value))+geom_bar(stat="identity") + theme(axis.text.x = element_text(angle=90, vjust=.5, hjust=1)) + ggtitle(error_label))

    participant_plot_correct <- data.frame(name = c("num_incong_corrFaces_reported_definitely_new", "num_incong_corrFaces_reported_probably_new", "num_incong_corrFaces_reported_maybe_new",
                                  "num_incong_corrFaces_reported_definitely_old", "num_incong_corrFaces_reported_probably_old", "num_incong_corrFaces_reported_maybe_old"), value = c(num_incong_corrFaces_reported_definitely_new, num_incong_corrFaces_reported_probably_new, num_incong_corrFaces_reported_maybe_new,
                                       num_incong_corrFaces_reported_definitely_old, num_incong_corrFaces_reported_probably_old, num_incong_corrFaces_reported_maybe_old))
    correct_label <- paste("Participant plot for Correct", as.character(i), collapse = ", ")
    print(ggplot(data.frame(participant_plot_correct),aes(x= name, y=value))+geom_bar(stat="identity") + theme(axis.text.x = element_text(angle=90, vjust=.5, hjust=1)) + ggtitle(correct_label))

    ##########
    percent_mainDat[nrow(percent_mainDat) + 1,] <-c(id, congAcc, incongAcc, congCorr_meanRT, incongCorr_meanRT, congCorr_logMeanRT,
                                                    incongCorr_logMeanRT, flankEff_meanACC, flankEff_meanRT, flankEff_logMeanRT,
                                                    reported_errors, committed_errors, memoryBias_score, num_incong_errors,
                                                    num_foilFaces_reported_definitely_old, num_foilFaces_reported_probably_old,
                                                    num_foilFaces_reported_maybe_old, num_foilFaces_reported_maybe_new, num_foilFaces_reported_probably_new,
                                                    num_foilFaces_reported_definitely_new, num_incong_corrFaces_reported_definitely_new, num_incong_corrFaces_reported_definitely_old, num_incong_corrFaces_reported_probably_new,
                                                    num_incong_corrFaces_reported_probably_old, num_incong_corrFaces_reported_maybe_new, num_incong_corrFaces_reported_maybe_old,
                                                    num_incong_errorFaces_reported_definitely_new, num_incong_errorFaces_reported_definitely_old, num_incong_errorFaces_reported_probably_new,
                                                    num_incong_errorFaces_reported_probably_old, num_incong_errorFaces_reported_maybe_new, num_incong_errorFaces_reported_maybe_old)
    } else if (nrow(incong_errorDat) < outlier_num){
      outlier_mainDat[nrow(outlier_mainDat) + 1,] <-c(id, congAcc, incongAcc, congCorr_meanRT, incongCorr_meanRT, congCorr_logMeanRT, incongCorr_logMeanRT, flankEff_meanACC, flankEff_meanRT, flankEff_logMeanRT, reported_errors, committed_errors, memoryBias_score, num_incong_errors)
    }
  }




#write the extracted summary scores to disk
write.csv(percent_mainDat,paste(output_path,proc_fileName, sep = "/", collapse = NULL), row.names=FALSE)
write.csv(outlier_mainDat,paste(output_path,"outlier_data.csv", sep = "/", collapse = NULL), row.names=FALSE)
#### Plots


## Let's do some Bar plotting!
sample_size <- length(datafiles_list) # total number of participants. This will be needed to compute standard error.
# Convert mainDat with specified columns to long format. So, I can use ggplot, etc. easily.


longDat_error <- gather(percent_mainDat, column_name, value, num_incong_errorFaces_reported_definitely_new, num_incong_errorFaces_reported_probably_new, num_incong_errorFaces_reported_maybe_new,
                        num_incong_errorFaces_reported_definitely_old, num_incong_errorFaces_reported_probably_old, num_incong_errorFaces_reported_maybe_old)

longDat_correct <- gather(percent_mainDat, column_name, value, num_incong_corrFaces_reported_definitely_new, num_incong_corrFaces_reported_probably_new, num_incong_corrFaces_reported_maybe_new,
                        num_incong_corrFaces_reported_definitely_old, num_incong_corrFaces_reported_probably_old, num_incong_corrFaces_reported_maybe_old)

longDat_foil <- gather(percent_mainDat, column_name, value, num_foilFaces_reported_definitely_old, num_foilFaces_reported_probably_old,
                       num_foilFaces_reported_maybe_old, num_foilFaces_reported_maybe_new, num_foilFaces_reported_probably_new,
                       num_foilFaces_reported_definitely_new)



# error
for_plot_error <- longDat_error %>%
  group_by(column_name) %>%
  summarise(
    n=n(),
    mean=mean(as.numeric(value)),
    sd=sd(as.numeric(value))
  ) %>%
  mutate( se=sd/sqrt(n))
ggplot(for_plot_error) +
  geom_bar( aes(x= column_name, y=mean), stat="identity", fill="forestgreen", alpha=0.5) +
  geom_errorbar( aes(x=column_name, ymin=mean-se, ymax=mean+se), width=0.4, colour="orange", alpha=0.9, size=1.5) +
  theme(axis.text.x = element_text(angle=90, vjust=.5, hjust=1)) +
  ggtitle("Error")

# Correct
for_plot_correct <- longDat_correct %>%
  group_by(column_name) %>%
  summarise(
    n=n(),
    mean=mean(as.numeric(value)),
    sd=sd(as.numeric(value))
  ) %>%
  mutate( se=sd/sqrt(n))
ggplot(for_plot_correct) +
  geom_bar( aes(x= column_name, y=mean), stat="identity", fill="forestgreen", alpha=0.5) +
  geom_errorbar( aes(x=column_name, ymin=mean-se, ymax=mean+se), width=0.4, colour="orange", alpha=0.9, size=1.5) +
  theme(axis.text.x = element_text(angle=90, vjust=.5, hjust=1)) +
  ggtitle("Correct")

# foil
for_plot_foil <- longDat_foil %>%
  group_by(column_name) %>%
  summarise(
    n=n(),
    mean=mean(as.numeric(value)),
    sd=sd(as.numeric(value))
  ) %>%
  mutate( se=sd/sqrt(n))
ggplot(for_plot_foil) +
  geom_bar( aes(x= column_name, y=mean), stat="identity", fill="forestgreen", alpha=0.5) +
  geom_errorbar( aes(x=column_name, ymin=mean-se, ymax=mean+se), width=0.4, colour="orange", alpha=0.9, size=1.5) +
  theme(axis.text.x = element_text(angle=90, vjust=.5, hjust=1)) +
  ggtitle("Foil")
