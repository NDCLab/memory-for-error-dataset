# Author: Kianoosh Hosseini at NDCLab @FIU (https://Kianoosh.info; https://NDClab.com)
# Last Update: 2023-09-25 (YYYY-MM-DD)

# This script will load the outputs of mfe_b_measure_computations_n1 script.
# To see how this script organize dataframe in order to be able to use the output csv file in the ROC toolbox, see ROC toolbox manual in logseq.


# Working directory should be the Psychopy experiment directory.

proje_wd <- "/Users/kihossei/Documents/GitHub/memory-for-error-dataset"
setwd(proje_wd)

output_path <- paste(proje_wd, "derivatives", "preprocessed", "organized_csvDat_for_roc_toolbox", sep ="/", collapse = NULL) # output directory
output_for_current_trial_fileName <- "longDat_current_trial_n1_with_headers.csv" # output filename
output_for_post_trial_fileName <- "longDat_post_trial_n1_with_headers.csv" # output filename
processed_file_input <- paste(proje_wd, "derivatives", "preprocessed", "psychopy", "stat_output", sep ="/", collapse = NULL) # input data directory

main_df <-  read.csv(file = paste(processed_file_input, "processed_data_mfe_b_Proj_n1.csv", sep ="/", collapse = NULL), stringsAsFactors = FALSE, na.strings=c("", "NA"))

# Create a dataframe that has 6 columns: Subject ID, Group ID, Condition Label, item type, Rating bin (Confidence rating), Response Frequency.
# The order of columns should exactly stay as listed above. The order matters.
# The column headers should not be included in the output CSV file.
# Each participant of this study, will have 24 rows in the output CSV file.

########################################################################################################################
                                             ##### Current trial #####
########################################################################################################################
# In this section of script, I extract and make the csv using data from current flanker trials.

# Create an empty dataframe with 6 columns.
# At the end, I will delete column headers.
roc_long_dat_current_trial <- setNames(data.frame(matrix(ncol = 6, nrow = 0)), c("subject_id", "group_id", "cond_label",
                                                                    "item_label", "rating_bin", "response_freq"))
for (subject in 1:nrow(main_df)){
  subject_id <- main_df$participant_id[subject]
  group_id <- main_df$SA_group[subject]
  for (i in 1:2){ # for condition label (error or correct)
    if (i == 1){
      cond_label <- "error"
      for (ii in 1:2){ # for item labels (target or lure)
        if (ii == 1){
          item_label <- "target" # this toolbox recognizes only the words target and lure. So, I will use olds as target and new as lure.
          for (iii in 1:6){ # for rating bin
            if (iii == 1){ # definitely old
              rating_bin <- 6
              response_freq <- main_df$num_errorFaces_reported_def_old[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 2){ # probably old
              rating_bin <- 5
              response_freq <- main_df$num_errorFaces_reported_prob_old[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 3){ # maybe old
              rating_bin <- 4
              response_freq <- main_df$num_errorFaces_reported_may_old[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 4){ # maybe new
              rating_bin <- 3
              response_freq <- main_df$num_errorFaces_reported_may_new[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 5){ # probably new
              rating_bin <- 2
              response_freq <- main_df$num_errorFaces_reported_prob_new[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 6){ # definitely new
              rating_bin <- 1
              response_freq <- main_df$num_errorFaces_reported_def_new[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            }
          }
        } else if (ii == 2){
          item_label <- "lure"
          for (iii in 1:6){ # for rating bin
            if (iii == 1){
              rating_bin <- 6
              response_freq <- main_df$num_foil_faces_reported_def_old[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 2){
              rating_bin <- 5
              response_freq <- main_df$num_foil_faces_reported_prob_old[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 3){
              rating_bin <- 4
              response_freq <- main_df$num_foil_faces_reported_may_old[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 4){
              rating_bin <- 3
              response_freq <- main_df$num_foil_faces_reported_may_new[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 5){
              rating_bin <- 2
              response_freq <- main_df$num_foil_faces_reported_prob_new[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 6){
              rating_bin <- 1
              response_freq <- main_df$num_foil_faces_reported_def_new[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            }
          }
        }
      }
    } else if (i == 2){
      cond_label <- "correct"
      for (ii in 1:2){ # for item labels
        if (ii == 1){
          item_label <- "target" # this toolbox recognizes only the words target and lure. So, I will use olds as target and new as lure.
          for (iii in 1:6){ #for rating bin
            if (iii == 1){
              rating_bin <- 6
              response_freq <- main_df$num_correctFaces_reported_def_old[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 2){
              rating_bin <- 5
              response_freq <- main_df$num_correctFaces_reported_prob_old[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 3){
              rating_bin <- 4
              response_freq <- main_df$num_correctFaces_reported_may_old[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 4){
              rating_bin <- 3
              response_freq <- main_df$num_correctFaces_reported_may_new[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 5){
              rating_bin <- 2
              response_freq <- main_df$num_correctFaces_reported_prob_new[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 6){
              rating_bin <- 1
              response_freq <- main_df$num_correctFaces_reported_def_new[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            }
          }
        } else if (ii == 2){
          item_label <- "lure"
          for (iii in 1:6){ #for rating bin
            if (iii == 1){
              rating_bin <- 6
              response_freq <- main_df$num_foil_faces_reported_def_old[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 2){
              rating_bin <- 5
              response_freq <- main_df$num_foil_faces_reported_prob_old[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 3){
              rating_bin <- 4
              response_freq <- main_df$num_foil_faces_reported_may_old[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 4){
              rating_bin <- 3
              response_freq <- main_df$num_foil_faces_reported_may_new[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 5){
              rating_bin <- 2
              response_freq <- main_df$num_foil_faces_reported_prob_new[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 6){
              rating_bin <- 1
              response_freq <- main_df$num_foil_faces_reported_def_new[subject]
              roc_long_dat_current_trial[nrow(roc_long_dat_current_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            }
          }
        }
      }
    }
  }
}

####################
# Save the dataset
# write the long dataframe that has column headers
write.csv(roc_long_dat_current_trial, paste(output_path, output_for_current_trial_fileName, sep = "/", collapse = NULL), row.names=FALSE)
##################
# Export to CSV without header
# I remove columns headers manually in the MS Excel.

########################################################################################################################
                                           ##### Post trial #####
########################################################################################################################
# In this section of script, I extract and make the csv using data from post flanker trials.

# Create an empty dataframe with 6 columns.
# After saving, I will delete column headers manually.
roc_long_dat_post_trial <- setNames(data.frame(matrix(ncol = 6, nrow = 0)), c("subject_id", "group_id", "cond_label",
                                                                                 "item_label", "rating_bin", "response_freq"))
for (subject in 1:nrow(main_df)){
  subject_id <- main_df$participant_id[subject]
  group_id <- main_df$SA_group[subject]
  for (i in 1:2){ # for condition label
    if (i == 1){
      cond_label <- "error"
      for (ii in 1:2){ # for item labels
        if (ii == 1){
          item_label <- "target" # this toolbox recognizes only the words target and lure. So, I will use olds as target and new as lure.
          for (iii in 1:6){ #for rating bin
            if (iii == 1){
              rating_bin <- 6
              response_freq <- main_df$num_post_errorFaces_reported_def_old[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 2){
              rating_bin <- 5
              response_freq <- main_df$num_post_errorFaces_reported_prob_old[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 3){
              rating_bin <- 4
              response_freq <- main_df$num_post_errorFaces_reported_may_old[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 4){
              rating_bin <- 3
              response_freq <- main_df$num_post_errorFaces_reported_may_new[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 5){
              rating_bin <- 2
              response_freq <- main_df$num_post_errorFaces_reported_prob_new[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 6){
              rating_bin <- 1
              response_freq <- main_df$num_post_errorFaces_reported_def_new[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            }
          }
        } else if (ii == 2){
          item_label <- "lure"
          for (iii in 1:6){ #for rating bin
            if (iii == 1){
              rating_bin <- 6
              response_freq <- main_df$num_foil_faces_reported_def_old[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 2){
              rating_bin <- 5
              response_freq <- main_df$num_foil_faces_reported_prob_old[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 3){
              rating_bin <- 4
              response_freq <- main_df$num_foil_faces_reported_may_old[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 4){
              rating_bin <- 3
              response_freq <- main_df$num_foil_faces_reported_may_new[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 5){
              rating_bin <- 2
              response_freq <- main_df$num_foil_faces_reported_prob_new[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 6){
              rating_bin <- 1
              response_freq <- main_df$num_foil_faces_reported_def_new[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            }
          }
        }
      }
    } else if (i == 2){
      cond_label <- "correct"
      for (ii in 1:2){ # for item labels
        if (ii == 1){
          item_label <- "target" # this toolbox recognizes only the words target and lure. So, I will use olds as target and new as lure.
          for (iii in 1:6){ #for rating bin
            if (iii == 1){
              rating_bin <- 6
              response_freq <- main_df$num_post_correctFaces_reported_def_old[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 2){
              rating_bin <- 5
              response_freq <- main_df$num_post_correctFaces_reported_prob_old[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 3){
              rating_bin <- 4
              response_freq <- main_df$num_post_correctFaces_reported_may_old[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 4){
              rating_bin <- 3
              response_freq <- main_df$num_post_correctFaces_reported_may_new[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 5){
              rating_bin <- 2
              response_freq <- main_df$num_post_correctFaces_reported_prob_new[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 6){
              rating_bin <- 1
              response_freq <- main_df$num_post_correctFaces_reported_def_new[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            }
          }
        } else if (ii == 2){
          item_label <- "lure"
          for (iii in 1:6){ #for rating bin
            if (iii == 1){
              rating_bin <- 6
              response_freq <- main_df$num_foil_faces_reported_def_old[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 2){
              rating_bin <- 5
              response_freq <- main_df$num_foil_faces_reported_prob_old[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 3){
              rating_bin <- 4
              response_freq <- main_df$num_foil_faces_reported_may_old[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 4){
              rating_bin <- 3
              response_freq <- main_df$num_foil_faces_reported_may_new[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 5){
              rating_bin <- 2
              response_freq <- main_df$num_foil_faces_reported_prob_new[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            } else if (iii == 6){
              rating_bin <- 1
              response_freq <- main_df$num_foil_faces_reported_def_new[subject]
              roc_long_dat_post_trial[nrow(roc_long_dat_post_trial) + 1,] <-c(subject_id, group_id, cond_label, item_label, rating_bin, response_freq)
            }
          }
        }
      }
    }
  }
}

####################
# Save the dataset
# write the long dataframe that has column headers
write.csv(roc_long_dat_post_trial, paste(output_path, output_for_post_trial_fileName, sep = "/", collapse = NULL), row.names=FALSE)
##################

# I remove columns headers manually in the MS Excel.
### Kianoosh has checked up to this point and no error.