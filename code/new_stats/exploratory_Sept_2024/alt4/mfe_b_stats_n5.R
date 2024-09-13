# This script will run stats on mfe_b data.
# Author: Kianoosh Hosseini at NDCLab @FIU (https://Kianoosh.info; https://NDClab.com)
# Last Update: 2024-09-03 (YYYY-MM-DD)

library(tidyverse)
library(dplyr)
library(stringr)
library(psycho)
library(car)
library(lme4)
library(ggplot2)
library(emmeans)
library(report)
library(sjPlot)



#Working directory should be the Psychopy experiment directory.

proje_wd <- "/Users/kihossei/Documents/GitHub/memory-for-error-dataset"
setwd(proje_wd)

processed_file_input <- paste(proje_wd, "derivatives", "preprocessed", "psychopy", "stat_output", sep ="/", collapse = NULL) # input data directory
main_df <-  read.csv(file = paste(processed_file_input, "processed_data_mfe_b_Proj_n5.csv", sep ="/", collapse = NULL), stringsAsFactors = FALSE, na.strings=c("", "NA"))

#################### Adding ROC toolbox outputs to main_df

# Load ROC toolbox results from current trials
roc_current_trial_df <-  read.csv(file = '/Users/kihossei/Documents/GitHub/memory-for-error-dataset/derivatives/preprocessed/roc_dat/dpsd_n5/current_trial/dpsd_group_data_acc_bias_data.csv', stringsAsFactors = FALSE, na.strings=c("", "NA"))

# Keeping the columns that we need!
roc_current_trial_df <- roc_current_trial_df[c("subID", "all_auc", "all_c", "all_HR", "all_FAR", "all_HR_m_FAR")]
# AUC: Area under the curve
# C: Response Bias
# Reminder: correct FAR is the same as error FAR
for (rr in 1:nrow(main_df)){
  temp_id <- main_df$participant_id[rr]
  tempDat <- filter(roc_current_trial_df, subID == temp_id)
  if (nrow(tempDat) == 1){
    main_df$current_all_auc[rr] <- tempDat$all_auc
    main_df$current_all_c[rr] <- tempDat$all_c
    main_df$current_all_HR[rr] <- tempDat$all_HR
    main_df$current_all_FAR[rr] <- tempDat$all_FAR
    main_df$current_all_HR_m_FAR[rr] <- tempDat$all_HR_m_FAR
  } else if (nrow(tempDat) == 0){
    main_df$current_all_auc[rr] <- NA
    main_df$current_all_c[rr] <- NA
    main_df$current_all_HR[rr] <- NA
    main_df$current_all_FAR[rr] <- NA
    main_df$current_all_HR_m_FAR[rr] <- NA
  }
}


# Load the estimated R and F parameters using the DPSD model in ROC toolbox.
roc_current_trial_df2 <-  read.csv(file = '/Users/kihossei/Documents/GitHub/memory-for-error-dataset/derivatives/preprocessed/roc_dat/dpsd_n5/current_trial/dpsd_group_data_pars.csv', stringsAsFactors = FALSE, na.strings=c("", "NA"))

# Keeping the columns that we need!
roc_current_trial_df2 <- roc_current_trial_df2[c("subID", "all_Ro", "all_F")]
# Ro is recollection of ‘oldness’. F is familiarity.
for (rr in 1:nrow(main_df)){
  temp_id <- main_df$participant_id[rr]
  tempDat <- filter(roc_current_trial_df2, subID == temp_id)
  if (nrow(tempDat) == 1){
    main_df$current_all_Ro[rr] <- tempDat$all_Ro
    main_df$current_all_F[rr] <- tempDat$all_F
  } else if (nrow(tempDat) == 0){
    main_df$current_all_Ro[rr] <- NA
    main_df$current_all_F[rr] <- NA
  }
}


# Load ROC toolbox results from post trials
roc_post_trial_df <-  read.csv(file = '/Users/kihossei/Documents/GitHub/memory-for-error-dataset/derivatives/preprocessed/roc_dat/dpsd_n5/post_trial/dpsd_group_data_acc_bias_data.csv', stringsAsFactors = FALSE, na.strings=c("", "NA"))

# Keeping the columns that we need!
roc_post_trial_df <- roc_post_trial_df[c("subID", "all_auc", "all_c", "all_HR", "all_FAR", "all_HR_m_FAR")]

for (rr in 1:nrow(main_df)){
  temp_id <- main_df$participant_id[rr]
  tempDat <- filter(roc_post_trial_df, subID == temp_id)
  if (nrow(tempDat) == 1){
    main_df$post_all_auc[rr] <- tempDat$all_auc
    main_df$post_all_c[rr] <- tempDat$all_c
    main_df$post_all_HR[rr] <- tempDat$all_HR
    main_df$post_all_FAR[rr] <- tempDat$all_FAR
    main_df$post_all_HR_m_FAR[rr] <- tempDat$all_HR_m_FAR
  } else if (nrow(tempDat) == 0){
    main_df$post_all_auc[rr] <- NA
    main_df$post_all_c[rr] <- NA
    main_df$post_all_HR[rr] <- NA
    main_df$post_all_FAR[rr] <- NA
    main_df$post_all_HR_m_FAR[rr] <- NA
  }
}

# Load the estimated R and F parameters using the DPSD model in ROC toolbox.
roc_post_trial_df2 <-  read.csv(file = '/Users/kihossei/Documents/GitHub/memory-for-error-dataset/derivatives/preprocessed/roc_dat/dpsd_n5/post_trial/dpsd_group_data_pars.csv', stringsAsFactors = FALSE, na.strings=c("", "NA"))

# Keeping the columns that we need!
roc_post_trial_df2 <- roc_post_trial_df2[c("subID", "all_Ro", "all_F")]
# Ro is recollection of ‘oldness’. F is familiarity.
for (rr in 1:nrow(main_df)){
  temp_id <- main_df$participant_id[rr]
  tempDat <- filter(roc_post_trial_df2, subID == temp_id)
  if (nrow(tempDat) == 1){
    main_df$post_all_Ro[rr] <- tempDat$all_Ro
    main_df$post_all_F[rr] <- tempDat$all_F
  } else if (nrow(tempDat) == 0){
    main_df$post_all_Ro[rr] <- NA
    main_df$post_all_F[rr] <- NA
  }
}




# Check the values in every column in main_df and remove the outliers based on +- 3SD.
# Write a function that removes the outliers from an array
remove_outliers <- function(x) {
    mean_x <- mean(as.numeric(x), na.rm = TRUE)
    sd_x <- sd(as.numeric(x), na.rm = TRUE)
    for (xx in 1:length(x)){
      if (!is.na(x[xx])){
        if (x[xx] < (mean_x - 3*sd_x) | x[xx] > (mean_x + 3*sd_x)){
          x[xx] <- NA
        }
      }
    }
  return(x)
}
# apply this outlier removing function to all the columns in the dataframe except for participant ID column and the SA_group column.
df_new <- subset(main_df, select = -(SA_group)) # remving SA_group from the dataframe as it is not a numerical value that needs outliers to be removed.
new_main_df <- df_new
new_main_df[-c(1, ncol(new_main_df))] <- apply(df_new[-c(1, ncol(df_new))], 2, remove_outliers)

# adding the SA_group column back to the dataframe
new_main_df$SA_group <- main_df$SA_group
main_df <- new_main_df

# We have these subjects 51, 52, 27, 37, 41 and need to check to see if they are outliers in important measures or not. If they are, they will be excluded.
# [See tracker notes on why this is the case]
# Outlier subjects: 41,
# Non-outlier subjects: 27, 37, 52, 51
# Remove subject 41 from the dataset.
main_df <- main_df[main_df$participant_id != 200041, ]


roc_low_sa_df <- filter(main_df, SA_group == "low")
roc_high_sa_df <- filter(main_df, SA_group == 'high')



# Surprise memory task in mfe_c_face task
mean(main_df$overall_hitRate, na.rm = TRUE)
sd(main_df$overall_hitRate, na.rm = TRUE)

mean(main_df$current_all_HR, na.rm = TRUE)
sd(main_df$current_all_HR, na.rm = TRUE)
shapiro.test(main_df$current_all_HR) #

mean(main_df$post_all_HR, na.rm = TRUE)
sd(main_df$post_all_HR, na.rm = TRUE)
shapiro.test(main_df$post_all_HR) #

## To confirm incidental memory is above chance level
t.test(main_df$overall_hitRate, main_df$overall_false_alarm_rate, paired = TRUE, na.action = na.omit) # p-value < 2.2e-16; hitrate is larger.
##

### Regressions between Current difference scores of AUC, HR, and c AND behavioral measures of interest (not controlling for phq)
######## AUC
current_auc_reg_1 <- lm(current_all_auc ~ scaared_b_scrdSoc_s1_r1_e1, data = main_df)
summary(current_auc_reg_1)
ggplot(main_df, aes(x=scaared_b_scrdSoc_s1_r1_e1, y=current_all_auc)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED social anxiety score", y = "current_all_auc") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))



current_auc_reg_2 <- lm(current_all_auc ~ bfne_b_scrdTotal_s1_r1_e1, data = main_df)
summary(current_auc_reg_2) # sig

current_auc_reg_3 <- lm(current_all_auc ~ scaared_b_scrdTotal_s1_r1_e1, data = main_df)
summary(current_auc_reg_3) # non-sig
ggplot(main_df, aes(x=scaared_b_scrdTotal_s1_r1_e1, y=current_all_auc)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED total anxiety score", y = "current_all_auc") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))



current_auc_reg_4 <- lm(current_all_auc ~ stai5_scrdS_diff, data = main_df)
summary(current_auc_reg_4) # non-sig

current_auc_reg_5 <- lm(current_all_auc ~ stai5_scrdS_s1_r1_e1, data = main_df)
summary(current_auc_reg_5) # non-sig

current_auc_reg_6 <- lm(current_all_auc ~ stai5_scrdS_s1_r1_e2, data = main_df)
summary(current_auc_reg_6) # non-sig

current_auc_reg_7 <- lm(current_all_auc ~ epepq15_scrdTotal_s1_r1_e1, data = main_df)
summary(current_auc_reg_7) # non-sig

######## HR
current_HR_reg_1 <- lm(current_all_HR ~ scaared_b_scrdSoc_s1_r1_e1, data = main_df)
summary(current_HR_reg_1)
ggplot(main_df, aes(x=scaared_b_scrdSoc_s1_r1_e1, y=current_all_HR)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED social anxiety score", y = "current_all_HR") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))



current_HR_reg_2 <- lm(current_all_HR ~ bfne_b_scrdTotal_s1_r1_e1, data = main_df)
summary(current_HR_reg_2) # non-sig

current_HR_reg_3 <- lm(current_all_HR ~ scaared_b_scrdTotal_s1_r1_e1, data = main_df)
summary(current_HR_reg_3) # non-sig
ggplot(main_df, aes(x=scaared_b_scrdTotal_s1_r1_e1, y=current_all_HR)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED total anxiety score", y = "current_all_HR") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))


current_HR_reg_4 <- lm(current_all_HR ~ stai5_scrdS_diff, data = main_df)
summary(current_HR_reg_4) # non-sig

current_HR_reg_5 <- lm(current_all_HR ~ stai5_scrdS_s1_r1_e1, data = main_df)
summary(current_HR_reg_5) # non-sig

current_HR_reg_6 <- lm(current_all_HR ~ stai5_scrdS_s1_r1_e2, data = main_df)
summary(current_HR_reg_6) # non-sig

current_HR_reg_7 <- lm(current_all_HR ~ epepq15_scrdTotal_s1_r1_e1, data = main_df)
summary(current_HR_reg_7) # non-sig

######## c (response Bias)
current_c_reg_1 <- lm(current_all_c ~ scaared_b_scrdSoc_s1_r1_e1, data = main_df)
summary(current_c_reg_1)
ggplot(main_df, aes(x=scaared_b_scrdSoc_s1_r1_e1, y=current_all_c)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED social anxiety score", y = "current_all_c") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))


current_c_reg_2 <- lm(current_all_c ~ bfne_b_scrdTotal_s1_r1_e1, data = main_df)
summary(current_c_reg_2) # non-sig

current_c_reg_3 <- lm(current_all_c ~ scaared_b_scrdTotal_s1_r1_e1, data = main_df)
summary(current_c_reg_3) # non-sig
ggplot(main_df, aes(x=scaared_b_scrdTotal_s1_r1_e1, y=current_all_c)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED total anxiety score", y = "current_all_c") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))

current_c_reg_4 <- lm(current_all_c ~ stai5_scrdS_diff, data = main_df)
summary(current_c_reg_4) # non-sig

current_c_reg_5 <- lm(current_all_c ~ stai5_scrdS_s1_r1_e1, data = main_df)
summary(current_c_reg_5) # non-sig

current_c_reg_6 <- lm(current_all_c ~ stai5_scrdS_s1_r1_e2, data = main_df)
summary(current_c_reg_6) # non-sig

current_c_reg_7 <- lm(current_all_c ~ epepq15_scrdTotal_s1_r1_e1, data = main_df)
summary(current_c_reg_7) # non-sig

# Ro
current_Ro_reg_1 <- lm(current_all_Ro ~ scaared_b_scrdSoc_s1_r1_e1, data = main_df)
summary(current_Ro_reg_1) # sig, negative correlation
ggplot(main_df, aes(x=scaared_b_scrdSoc_s1_r1_e1, y=current_all_Ro)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED social anxiety score", y = "current_all_Ro") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))


current_Ro_reg_2 <- lm(current_all_Ro ~ bfne_b_scrdTotal_s1_r1_e1, data = main_df)
summary(current_Ro_reg_2)

current_Ro_reg_3 <- lm(current_all_Ro ~ scaared_b_scrdTotal_s1_r1_e1, data = main_df)
summary(current_Ro_reg_3) # sig, negative correlation
ggplot(main_df, aes(x=scaared_b_scrdTotal_s1_r1_e1, y=current_all_Ro)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED total anxiety score", y = "current_all_Ro") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))

current_Ro_reg_4 <- lm(current_all_Ro ~ stai5_scrdS_diff, data = main_df)
summary(current_Ro_reg_4)

current_Ro_reg_5 <- lm(current_all_Ro ~ stai5_scrdS_s1_r1_e1, data = main_df)
summary(current_Ro_reg_5)

current_Ro_reg_6 <- lm(current_all_Ro ~ stai5_scrdS_s1_r1_e2, data = main_df)
summary(current_Ro_reg_6)

current_Ro_reg_7 <- lm(current_all_Ro ~ epepq15_scrdTotal_s1_r1_e1, data = main_df)
summary(current_Ro_reg_7)


# F

current_F_reg_1 <- lm(current_all_F ~ scaared_b_scrdSoc_s1_r1_e1, data = main_df)
summary(current_F_reg_1)
ggplot(main_df, aes(x=scaared_b_scrdSoc_s1_r1_e1, y=current_all_F)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED social anxiety score", y = "current_all_F") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))

current_F_reg_2 <- lm(current_all_F ~ bfne_b_scrdTotal_s1_r1_e1, data = main_df)
summary(current_F_reg_2) # sig, negative correlation

current_F_reg_3 <- lm(current_all_F ~ scaared_b_scrdTotal_s1_r1_e1, data = main_df)
summary(current_F_reg_3)
ggplot(main_df, aes(x=scaared_b_scrdTotal_s1_r1_e1, y=current_all_F)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED total anxiety score", y = "current_all_F") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))


current_F_reg_4 <- lm(current_all_F ~ stai5_scrdS_diff, data = main_df)
summary(current_F_reg_4)

current_F_reg_5 <- lm(current_all_F ~ stai5_scrdS_s1_r1_e1, data = main_df)
summary(current_F_reg_5)

current_F_reg_6 <- lm(current_all_F ~ stai5_scrdS_s1_r1_e2, data = main_df)
summary(current_F_reg_6)

current_F_reg_7 <- lm(current_all_F ~ epepq15_scrdTotal_s1_r1_e1, data = main_df)
summary(current_F_reg_7)




### Regressions between Current difference scores of AUC, HR, and c AND behavioral measures of interest (controlling for phq)
######## AUC
current_auc_reg_1 <- lm(current_all_auc ~ scaared_b_scrdSoc_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_auc_reg_1) # non-sig

plot_model(current_auc_reg_1, type = "eff", terms = c("scaared_b_scrdSoc_s1_r1_e1","phq8_scrdTotal_s1_r1_e1"))


current_auc_reg_2 <- lm(current_diff_auc ~ bfne_b_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_auc_reg_2) # main effect of bfne is sig

current_auc_reg_3 <- lm(current_all_auc ~ scaared_b_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_auc_reg_3) # main effect of scaared total is close to sig

current_auc_reg_4 <- lm(current_diff_auc ~ stai5_scrdS_diff + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_auc_reg_4) # non-sig

current_auc_reg_5 <- lm(current_diff_auc ~ stai5_scrdS_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_auc_reg_5) # non-sig

current_auc_reg_6 <- lm(current_diff_auc ~ stai5_scrdS_s1_r1_e2 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_auc_reg_6) # non-sig

current_auc_reg_7 <- lm(current_diff_auc ~ epepq15_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_auc_reg_7) # non-sig

######## HR
current_HR_reg_1 <- lm(current_diff_HR ~ scaared_b_scrdSoc_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_HR_reg_1) # non-sig


plot_model(current_HR_reg_1, type = "eff", terms = c("scaared_b_scrdSoc_s1_r1_e1","phq8_scrdTotal_s1_r1_e1"))


current_HR_reg_2 <- lm(current_diff_HR ~ bfne_b_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_HR_reg_2) # non-sig

current_HR_reg_3 <- lm(current_diff_HR ~ scaared_b_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_HR_reg_3) # non-sig

current_HR_reg_4 <- lm(current_diff_HR ~ stai5_scrdS_diff + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_HR_reg_4) # non-sig

current_HR_reg_5 <- lm(current_diff_HR ~ stai5_scrdS_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_HR_reg_5) # non-sig

current_HR_reg_6 <- lm(current_diff_HR ~ stai5_scrdS_s1_r1_e2 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_HR_reg_6) # non-sig

current_HR_reg_7 <- lm(current_diff_HR ~ epepq15_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_HR_reg_7) # non-sig

######## c (response Bias)
current_c_reg_1 <- lm(current_diff_c ~ scaared_b_scrdSoc_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1 , data = main_df)
summary(current_c_reg_1) # non-sig

plot_model(current_c_reg_1, type = "eff", terms = c("scaared_b_scrdSoc_s1_r1_e1","phq8_scrdTotal_s1_r1_e1"))

current_c_reg_2 <- lm(current_diff_c ~ bfne_b_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1 , data = main_df)
summary(current_c_reg_2) # non-sig

current_c_reg_3 <- lm(current_diff_c ~ scaared_b_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_c_reg_3) # non-sig

current_c_reg_4 <- lm(current_diff_c ~ stai5_scrdS_diff + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_c_reg_4) # non-sig

current_c_reg_5 <- lm(current_diff_c ~ stai5_scrdS_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_c_reg_5) # non-sig

current_c_reg_6 <- lm(current_diff_c ~ stai5_scrdS_s1_r1_e2 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_c_reg_6) # non-sig

current_c_reg_7 <- lm(current_diff_c ~ epepq15_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_c_reg_7) # non-sig



#### How pepq interacts with scaared social to predict diff AUC, HR, and c (not controlling for phq)
### Current
# AUC
current_pep_auc_reg <- lm(current_diff_auc ~ epepq15_scrdTotal_s1_r1_e1*scaared_b_scrdSoc_s1_r1_e1 , data = main_df)
summary(current_pep_auc_reg) # non-sig
# plot
plot_model(current_pep_auc_reg, type = "eff", terms = c("scaared_b_scrdSoc_s1_r1_e1","epepq15_scrdTotal_s1_r1_e1"))

# HR
current_pep_HR_reg <- lm(current_diff_HR ~ epepq15_scrdTotal_s1_r1_e1*scaared_b_scrdSoc_s1_r1_e1 , data = main_df)
summary(current_pep_HR_reg) # close to sig for main effect of scaared social and epepq
# plot
plot_model(current_pep_HR_reg, type = "eff", terms = c("epepq15_scrdTotal_s1_r1_e1","scaared_b_scrdSoc_s1_r1_e1"))
plot_model(current_pep_HR_reg, type = "eff", terms = c("scaared_b_scrdSoc_s1_r1_e1","epepq15_scrdTotal_s1_r1_e1"))
# c
current_pep_c_reg <- lm(current_diff_c ~ epepq15_scrdTotal_s1_r1_e1*scaared_b_scrdSoc_s1_r1_e1 , data = main_df)
summary(current_pep_c_reg) # close to sig for epepq

plot_model(current_pep_c_reg, type = "eff", terms = c("scaared_b_scrdSoc_s1_r1_e1","epepq15_scrdTotal_s1_r1_e1"))

#### How pepq interacts with scaared social to predict diff AUC, HR, and c (controlling for phq)
### Current
# AUC
current_pep_auc_reg <- lm(current_diff_auc ~ epepq15_scrdTotal_s1_r1_e1*scaared_b_scrdSoc_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_pep_auc_reg) # non-sig
plot_model(current_pep_auc_reg, type = "eff", terms = c("scaared_b_scrdSoc_s1_r1_e1","epepq15_scrdTotal_s1_r1_e1", "phq8_scrdTotal_s1_r1_e1"))

# HR
current_pep_HR_reg <- lm(current_diff_HR ~ epepq15_scrdTotal_s1_r1_e1*scaared_b_scrdSoc_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_pep_HR_reg) # close to sig epepq
plot_model(current_pep_HR_reg, type = "eff", terms = c("scaared_b_scrdSoc_s1_r1_e1","epepq15_scrdTotal_s1_r1_e1", "phq8_scrdTotal_s1_r1_e1"))

# c
current_pep_c_reg <- lm(current_diff_c ~ epepq15_scrdTotal_s1_r1_e1*scaared_b_scrdSoc_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_pep_c_reg) # close to sig epepq
plot_model(current_pep_c_reg, type = "eff", terms = c("scaared_b_scrdSoc_s1_r1_e1","epepq15_scrdTotal_s1_r1_e1", "phq8_scrdTotal_s1_r1_e1"))



############################################### POST

######## AUC
post_auc_reg_1 <- lm(post_all_auc ~ scaared_b_scrdSoc_s1_r1_e1, data = main_df)
summary(post_auc_reg_1) # non-sig
ggplot(main_df, aes(x=scaared_b_scrdSoc_s1_r1_e1, y=post_all_auc)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED social anxiety score", y = "post_all_auc") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))



post_auc_reg_2 <- lm(post_all_auc ~ bfne_b_scrdTotal_s1_r1_e1, data = main_df)
summary(post_auc_reg_2) # non-sig

post_auc_reg_3 <- lm(post_all_auc ~ scaared_b_scrdTotal_s1_r1_e1, data = main_df)
summary(post_auc_reg_3) # non-sig

post_auc_reg_4 <- lm(post_all_auc ~ stai5_scrdS_diff, data = main_df)
summary(post_auc_reg_4) # non-sig

post_auc_reg_5 <- lm(post_all_auc ~ stai5_scrdS_s1_r1_e1, data = main_df)
summary(post_auc_reg_5) # non-sig

post_auc_reg_6 <- lm(post_all_auc ~ stai5_scrdS_s1_r1_e2, data = main_df)
summary(post_auc_reg_6) # non-sig

post_auc_reg_7 <- lm(post_all_auc ~ epepq15_scrdTotal_s1_r1_e1, data = main_df)
summary(post_auc_reg_7) # non-sig

######## HR
post_HR_reg_1 <- lm(post_all_HR ~ scaared_b_scrdSoc_s1_r1_e1, data = main_df)
summary(post_HR_reg_1) # non-sig
ggplot(main_df, aes(x=scaared_b_scrdSoc_s1_r1_e1, y=post_all_HR)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED social anxiety score", y = "post_all_HR") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))


post_HR_reg_2 <- lm(post_all_HR ~ bfne_b_scrdTotal_s1_r1_e1, data = main_df)
summary(post_HR_reg_2) # non-sig

post_HR_reg_3 <- lm(post_all_HR ~ scaared_b_scrdTotal_s1_r1_e1, data = main_df)
summary(post_HR_reg_3) # non-sig

post_HR_reg_4 <- lm(post_all_HR ~ stai5_scrdS_diff, data = main_df)
summary(post_HR_reg_4) # non-sig

post_HR_reg_5 <- lm(post_all_HR ~ stai5_scrdS_s1_r1_e1, data = main_df)
summary(post_HR_reg_5) # non-sig

post_HR_reg_6 <- lm(post_all_HR ~ stai5_scrdS_s1_r1_e2, data = main_df)
summary(post_HR_reg_6) # non-sig

post_HR_reg_7 <- lm(post_all_HR ~ epepq15_scrdTotal_s1_r1_e1, data = main_df)
summary(post_HR_reg_7) # non-sig

######## c (response Bias)
post_c_reg_1 <- lm(post_all_c ~ scaared_b_scrdSoc_s1_r1_e1, data = main_df)
summary(post_c_reg_1) # non-sig
ggplot(main_df, aes(x=scaared_b_scrdSoc_s1_r1_e1, y=post_all_c)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED social anxiety score", y = "post_all_c") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))


post_c_reg_2 <- lm(post_all_c ~ bfne_b_scrdTotal_s1_r1_e1, data = main_df)
summary(post_c_reg_2) # non-sig

post_c_reg_3 <- lm(post_all_c ~ scaared_b_scrdTotal_s1_r1_e1, data = main_df)
summary(post_c_reg_3) # non-sig

post_c_reg_4 <- lm(post_all_c ~ stai5_scrdS_diff, data = main_df)
summary(post_c_reg_4) # non-sig

post_c_reg_5 <- lm(post_all_c ~ stai5_scrdS_s1_r1_e1, data = main_df)
summary(post_c_reg_5) # non-sig

post_c_reg_6 <- lm(post_all_c ~ stai5_scrdS_s1_r1_e2, data = main_df)
summary(post_c_reg_6) # non-sig

post_c_reg_7 <- lm(post_all_c ~ epepq15_scrdTotal_s1_r1_e1, data = main_df)
summary(post_c_reg_7) # non-sig

# Ro
post_Ro_reg_1 <- lm(post_all_Ro ~ scaared_b_scrdSoc_s1_r1_e1, data = main_df)
summary(post_Ro_reg_1)
ggplot(main_df, aes(x=scaared_b_scrdSoc_s1_r1_e1, y=post_all_Ro)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED social anxiety score", y = "post_all_Ro") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))

post_Ro_reg_2 <- lm(post_all_Ro ~ bfne_b_scrdTotal_s1_r1_e1, data = main_df)
summary(post_Ro_reg_2)

post_Ro_reg_3 <- lm(post_all_Ro ~ scaared_b_scrdTotal_s1_r1_e1, data = main_df)
summary(post_Ro_reg_3) # sig, negative correlation

post_Ro_reg_4 <- lm(post_all_Ro ~ stai5_scrdS_diff, data = main_df)
summary(post_Ro_reg_4)

post_Ro_reg_5 <- lm(post_all_Ro ~ stai5_scrdS_s1_r1_e1, data = main_df)
summary(post_Ro_reg_5)

post_Ro_reg_6 <- lm(post_all_Ro ~ stai5_scrdS_s1_r1_e2, data = main_df)
summary(post_Ro_reg_6)

post_Ro_reg_7 <- lm(post_all_Ro ~ epepq15_scrdTotal_s1_r1_e1, data = main_df)
summary(post_Ro_reg_7)


# F

post_F_reg_1 <- lm(post_all_F ~ scaared_b_scrdSoc_s1_r1_e1, data = main_df)
summary(post_F_reg_1)
ggplot(main_df, aes(x=scaared_b_scrdSoc_s1_r1_e1, y=post_all_F)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED social anxiety score", y = "post_all_F") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))


post_F_reg_2 <- lm(post_all_F ~ bfne_b_scrdTotal_s1_r1_e1, data = main_df)
summary(post_F_reg_2) # sig, negative correlation

post_F_reg_3 <- lm(post_all_F ~ scaared_b_scrdTotal_s1_r1_e1, data = main_df)
summary(post_F_reg_3)

post_F_reg_4 <- lm(post_all_F ~ stai5_scrdS_diff, data = main_df)
summary(post_F_reg_4)

post_F_reg_5 <- lm(post_all_F ~ stai5_scrdS_s1_r1_e1, data = main_df)
summary(post_F_reg_5)

post_F_reg_6 <- lm(post_all_F ~ stai5_scrdS_s1_r1_e2, data = main_df)
summary(post_F_reg_6)

post_F_reg_7 <- lm(post_all_F ~ epepq15_scrdTotal_s1_r1_e1, data = main_df)
summary(post_F_reg_7)


### Regressions between post difference scores of AUC, HR, and c AND behavioral measures of interest (controlling for phq)
######## AUC
post_auc_reg_1 <- lm(post_diff_auc ~ scaared_b_scrdSoc_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_auc_reg_1) # non-sig

post_auc_reg_2 <- lm(post_diff_auc ~ bfne_b_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_auc_reg_2) # non-sig

post_auc_reg_3 <- lm(post_diff_auc ~ scaared_b_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_auc_reg_3) # non-sig

post_auc_reg_4 <- lm(post_diff_auc ~ stai5_scrdS_diff + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_auc_reg_4) # non-sig

post_auc_reg_5 <- lm(post_diff_auc ~ stai5_scrdS_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_auc_reg_5) # non-sig

post_auc_reg_6 <- lm(post_diff_auc ~ stai5_scrdS_s1_r1_e2 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_auc_reg_6) # non-sig

post_auc_reg_7 <- lm(post_diff_auc ~ epepq15_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_auc_reg_7) # non-sig

######## HR
post_HR_reg_1 <- lm(post_diff_HR ~ scaared_b_scrdSoc_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_HR_reg_1) # non-sig

post_HR_reg_2 <- lm(post_diff_HR ~ bfne_b_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_HR_reg_2) # non-sig

post_HR_reg_3 <- lm(post_diff_HR ~ scaared_b_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_HR_reg_3) # non-sig

post_HR_reg_4 <- lm(post_diff_HR ~ stai5_scrdS_diff + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_HR_reg_4) # non-sig

post_HR_reg_5 <- lm(post_diff_HR ~ stai5_scrdS_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_HR_reg_5) # non-sig

post_HR_reg_6 <- lm(post_diff_HR ~ stai5_scrdS_s1_r1_e2 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_HR_reg_6) # non-sig

post_HR_reg_7 <- lm(post_diff_HR ~ epepq15_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_HR_reg_7) # non-sig

######## c (response Bias)
post_c_reg_1 <- lm(post_diff_c ~ scaared_b_scrdSoc_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_c_reg_1) # non-sig

post_c_reg_2 <- lm(post_diff_c ~ bfne_b_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_c_reg_2) # non-sig

post_c_reg_3 <- lm(post_diff_c ~ scaared_b_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_c_reg_3) # non-sig

post_c_reg_4 <- lm(post_diff_c ~ stai5_scrdS_diff + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_c_reg_4) # non-sig

post_c_reg_5 <- lm(post_diff_c ~ stai5_scrdS_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_c_reg_5) # non-sig

post_c_reg_6 <- lm(post_diff_c ~ stai5_scrdS_s1_r1_e2 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_c_reg_6) # non-sig

post_c_reg_7 <- lm(post_diff_c ~ epepq15_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_c_reg_7) # non-sig



#### How pepq interacts with scaared social to predict diff AUC, HR, and c (not controlling for phq)
### post
# AUC
post_pep_auc_reg <- lm(post_diff_auc ~ epepq15_scrdTotal_s1_r1_e1*scaared_b_scrdSoc_s1_r1_e1 , data = main_df)
summary(post_pep_auc_reg) # non-sig (interaction close to sig)
# plot
plot_model(post_pep_auc_reg, type = "eff", terms = c("scaared_b_scrdSoc_s1_r1_e1","epepq15_scrdTotal_s1_r1_e1"))

# HR
post_pep_HR_reg <- lm(post_diff_HR ~ epepq15_scrdTotal_s1_r1_e1*scaared_b_scrdSoc_s1_r1_e1 , data = main_df)
summary(post_pep_HR_reg)
# plot
plot_model(post_pep_HR_reg, type = "eff", terms = c("epepq15_scrdTotal_s1_r1_e1","scaared_b_scrdSoc_s1_r1_e1"))
plot_model(post_pep_HR_reg, type = "eff", terms = c("scaared_b_scrdSoc_s1_r1_e1","epepq15_scrdTotal_s1_r1_e1"))
# c
post_pep_c_reg <- lm(post_diff_c ~ epepq15_scrdTotal_s1_r1_e1*scaared_b_scrdSoc_s1_r1_e1 , data = main_df)
summary(post_pep_c_reg)
plot_model(post_pep_c_reg, type = "eff", terms = c("scaared_b_scrdSoc_s1_r1_e1","epepq15_scrdTotal_s1_r1_e1"))


#### How pepq interacts with scaared social to predict diff AUC, HR, and c (controlling for phq)
### post
# AUC
post_pep_auc_reg <- lm(post_diff_auc ~ epepq15_scrdTotal_s1_r1_e1*scaared_b_scrdSoc_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_pep_auc_reg) # non-sig
plot_model(post_pep_auc_reg, type = "eff", terms = c("scaared_b_scrdSoc_s1_r1_e1","epepq15_scrdTotal_s1_r1_e1"))

# HR
post_pep_HR_reg <- lm(post_diff_HR ~ epepq15_scrdTotal_s1_r1_e1*scaared_b_scrdSoc_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_pep_HR_reg) # non-sig
# c
post_pep_c_reg <- lm(post_diff_c ~ epepq15_scrdTotal_s1_r1_e1*scaared_b_scrdSoc_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_pep_c_reg) # non-sig


# Neural responses to errors correlations with social anxiety SCAARED
lm_for_cor_fit_line <- lm(theta_power_mfc_difference_score ~ scaared_b_scrdSoc_s1_r1_e1, main_df)
summary(lm_for_cor_fit_line)
ggplot(main_df, aes(x=scaared_b_scrdSoc_s1_r1_e1, y=theta_power_mfc_difference_score)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED social anxiety score", y = "Error Vs. Correct within MFC Power") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))


lm_for_cor_fit_line <- lm(theta_itps_mfc_difference_score ~ scaared_b_scrdSoc_s1_r1_e1, main_df)
summary(lm_for_cor_fit_line)
ggplot(main_df, aes(x=scaared_b_scrdSoc_s1_r1_e1, y=theta_itps_mfc_difference_score)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED social anxiety score", y = "Error Vs. Correct within MFC ITPS") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))


lm_for_cor_fit_line <- lm(theta_wpli_lat_occipital_difference_score ~ scaared_b_scrdSoc_s1_r1_e1, main_df)
summary(lm_for_cor_fit_line)
ggplot(main_df, aes(x=scaared_b_scrdSoc_s1_r1_e1, y=theta_wpli_lat_occipital_difference_score)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED social anxiety score", y = "Error Vs. Correct Between MFC-Visual Sensory cortex wPLI") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))







# Save the dataset
#write the extracted and computed summary scores to disk
write.csv(main_df, paste(output_path, 'main_df_all.csv', sep = "/", collapse = NULL), row.names=FALSE)
##################
