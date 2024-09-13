# This script will run stats on mfe_b data.
# Author: Kianoosh Hosseini at NDCLab @FIU (https://Kianoosh.info; https://NDClab.com)
# Last Update: 2024-09-02 (YYYY-MM-DD)

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
main_df <-  read.csv(file = paste(processed_file_input, "processed_data_mfe_b_Proj_n3.csv", sep ="/", collapse = NULL), stringsAsFactors = FALSE, na.strings=c("", "NA"))


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

## To confirm incidental memory is above chance level
t.test(main_df$overall_hitRate, main_df$overall_false_alarm_rate, paired = TRUE, na.action = na.omit) # p-value < 2.2e-16; hitrate is larger.
##

### Current trial t-tests

t.test(main_df$current_correct_HR, main_df$current_error_HR, paired = TRUE, na.action = na.omit) #


### Post trial t-tests

t.test(main_df$post_correct_HR, main_df$post_error_HR, paired = TRUE, na.action = na.omit) # nonsig,


# the same t-tests in low sa group

t.test(roc_low_sa_df$current_correct_HR, roc_low_sa_df$current_error_HR, paired = TRUE, na.action = na.omit) # sig, correct is larger

# the same t-tests in high sa group

t.test(roc_high_sa_df$current_correct_HR, roc_high_sa_df$current_error_HR, paired = TRUE, na.action = na.omit) # sig, correct is larger

### Regressions between Current difference scores of AUC, HR, and c AND behavioral measures of interest (not controlling for phq)

######## HR
current_HR_reg_1 <- lm(current_HR_diff ~ scaared_b_scrdSoc_s1_r1_e1, data = main_df)
summary(current_HR_reg_1) # non-sig
ggplot(main_df, aes(x=scaared_b_scrdSoc_s1_r1_e1, y=current_HR_diff)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED social anxiety score", y = "current_HR_diff") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))


current_HR_reg_2 <- lm(current_HR_diff ~ bfne_b_scrdTotal_s1_r1_e1, data = main_df)
summary(current_HR_reg_2) # sig (negative)
ggplot(main_df, aes(x=bfne_b_scrdTotal_s1_r1_e1, y=current_HR_diff)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "BFNE total score", y = "current_HR_diff") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))

ggplot(main_df, aes(x=bfne_b_scrdTotal_s1_r1_e1, y=current_error_HR)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "BFNE total score", y = "current_error_HR") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))

ggplot(main_df, aes(x=bfne_b_scrdTotal_s1_r1_e1, y=current_correct_HR)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "BFNE total score", y = "current_correct_HR") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))


current_HR_reg_3 <- lm(current_HR_diff ~ scaared_b_scrdTotal_s1_r1_e1, data = main_df)
summary(current_HR_reg_3) # non-sig
ggplot(main_df, aes(x=scaared_b_scrdTotal_s1_r1_e1, y=current_HR_diff)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED total score", y = "current_HR_diff") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))

ggplot(main_df, aes(x=scaared_b_scrdTotal_s1_r1_e1, y=current_error_HR)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED total score", y = "current_error_HR") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))

ggplot(main_df, aes(x=scaared_b_scrdTotal_s1_r1_e1, y=current_correct_HR)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED total score", y = "current_correct_HR") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))

current_HR_reg_4 <- lm(current_HR_diff ~ stai5_scrdS_diff, data = main_df)
summary(current_HR_reg_4) # non-sig

current_HR_reg_5 <- lm(current_HR_diff ~ stai5_scrdS_s1_r1_e1, data = main_df)
summary(current_HR_reg_5) # non-sig

current_HR_reg_6 <- lm(current_HR_diff ~ stai5_scrdS_s1_r1_e2, data = main_df)
summary(current_HR_reg_6) # non-sig

current_HR_reg_7 <- lm(current_HR_diff ~ epepq15_scrdTotal_s1_r1_e1, data = main_df)
summary(current_HR_reg_7) # sig
ggplot(main_df, aes(x=epepq15_scrdTotal_s1_r1_e1, y=current_HR_diff)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "epepq15_scrdTotal_s1_r1_e1", y = "current_HR_diff") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))

ggplot(main_df, aes(x=epepq15_scrdTotal_s1_r1_e1, y=current_error_HR)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "epepq15_scrdTotal_s1_r1_e1", y = "current_error_HR") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))

ggplot(main_df, aes(x=epepq15_scrdTotal_s1_r1_e1, y=current_correct_HR)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "epepq15_scrdTotal_s1_r1_e1", y = "current_correct_HR") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))


### Regressions between Current difference scores of AUC, HR, and c AND behavioral measures of interest (controlling for phq)

######## HR
current_HR_reg_1 <- lm(current_HR_diff ~ scaared_b_scrdSoc_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_HR_reg_1) # non-sig
plot_model(current_HR_reg_1, type = "eff", terms = c("scaared_b_scrdSoc_s1_r1_e1","phq8_scrdTotal_s1_r1_e1"))

current_HR_reg_2 <- lm(current_HR_diff ~ bfne_b_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_HR_reg_2) # sig (negative)

current_HR_reg_3 <- lm(current_HR_diff ~ scaared_b_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_HR_reg_3) # non-sig

current_HR_reg_4 <- lm(current_HR_diff ~ stai5_scrdS_diff + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_HR_reg_4) # non-sig

current_HR_reg_5 <- lm(current_HR_diff ~ stai5_scrdS_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_HR_reg_5) # non-sig

current_HR_reg_6 <- lm(current_HR_diff ~ stai5_scrdS_s1_r1_e2 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_HR_reg_6) # non-sig

current_HR_reg_7 <- lm(current_HR_diff ~ epepq15_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_HR_reg_7) # non-sig


#### How pepq interacts with scaared social to predict diff AUC, HR, and c (not controlling for phq)
### Current

# HR
current_pep_HR_reg <- lm(current_HR_diff ~ epepq15_scrdTotal_s1_r1_e1*scaared_b_scrdSoc_s1_r1_e1 , data = main_df)
summary(current_pep_HR_reg) # close to sig for main effect of scaared social and epepq (gone after 60%)
# plot
plot_model(current_pep_HR_reg, type = "eff", terms = c("epepq15_scrdTotal_s1_r1_e1","scaared_b_scrdSoc_s1_r1_e1"))
plot_model(current_pep_HR_reg, type = "eff", terms = c("scaared_b_scrdSoc_s1_r1_e1","epepq15_scrdTotal_s1_r1_e1"))

#### How pepq interacts with scaared social to predict diff AUC, HR, and c (controlling for phq)
### Current

# HR
current_pep_HR_reg <- lm(current_HR_diff ~ epepq15_scrdTotal_s1_r1_e1*scaared_b_scrdSoc_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(current_pep_HR_reg) # close to sig epepq


############################################### POST
######## HR
post_HR_reg_1 <- lm(post_HR_diff ~ scaared_b_scrdSoc_s1_r1_e1, data = main_df)
summary(post_HR_reg_1) # non-sig
ggplot(main_df, aes(x=scaared_b_scrdSoc_s1_r1_e1, y=post_HR_diff)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED social anxiety score", y = "post_HR_diff") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))

post_HR_reg_2 <- lm(post_HR_diff ~ bfne_b_scrdTotal_s1_r1_e1, data = main_df)
summary(post_HR_reg_2) # non-sig
ggplot(main_df, aes(x=bfne_b_scrdTotal_s1_r1_e1, y=post_HR_diff)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "BFNE total score", y = "post_HR_diff") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))

ggplot(main_df, aes(x=bfne_b_scrdTotal_s1_r1_e1, y=post_error_HR)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED total score", y = "post_error_HR") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))

ggplot(main_df, aes(x=bfne_b_scrdTotal_s1_r1_e1, y=post_correct_HR)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "BFNE total score", y = "post_correct_HR") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))

post_HR_reg_3 <- lm(post_HR_diff ~ scaared_b_scrdTotal_s1_r1_e1, data = main_df)
summary(post_HR_reg_3) # non-sig
ggplot(main_df, aes(x=scaared_b_scrdTotal_s1_r1_e1, y=post_HR_diff)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED total anxiety score", y = "post_HR_diff") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))
ggplot(main_df, aes(x=scaared_b_scrdTotal_s1_r1_e1, y=post_error_HR)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED total anxiety score", y = "post_error_HR") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))

ggplot(main_df, aes(x=scaared_b_scrdTotal_s1_r1_e1, y=post_correct_HR)) + geom_point(size = 4) + geom_smooth(method="lm") +
  labs(x = "SCAARED total anxiety score", y = "post_correct_HR") +
  theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                     panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) + theme(axis.text = element_text(size = 15)) + theme(text = element_text(size = 18))



post_HR_reg_4 <- lm(post_HR_diff ~ stai5_scrdS_diff, data = main_df)
summary(post_HR_reg_4) # non-sig

post_HR_reg_5 <- lm(post_HR_diff ~ stai5_scrdS_s1_r1_e1, data = main_df)
summary(post_HR_reg_5) # non-sig

post_HR_reg_6 <- lm(post_HR_diff ~ stai5_scrdS_s1_r1_e2, data = main_df)
summary(post_HR_reg_6) # non-sig

post_HR_reg_7 <- lm(post_HR_diff ~ epepq15_scrdTotal_s1_r1_e1, data = main_df)
summary(post_HR_reg_7) # non-sig

### Regressions between post difference scores of AUC, HR, and c AND behavioral measures of interest (controlling for phq)

######## HR
post_HR_reg_1 <- lm(post_HR_diff ~ scaared_b_scrdSoc_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_HR_reg_1) # non-sig
plot_model(post_HR_reg_1, type = "eff", terms = c("scaared_b_scrdSoc_s1_r1_e1","phq8_scrdTotal_s1_r1_e1"))


post_HR_reg_2 <- lm(post_HR_diff ~ bfne_b_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_HR_reg_2) # non-sig

post_HR_reg_3 <- lm(post_HR_diff ~ scaared_b_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_HR_reg_3) # non-sig

post_HR_reg_4 <- lm(post_HR_diff ~ stai5_scrdS_diff + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_HR_reg_4) # non-sig

post_HR_reg_5 <- lm(post_HR_diff ~ stai5_scrdS_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_HR_reg_5) # non-sig

post_HR_reg_6 <- lm(post_HR_diff ~ stai5_scrdS_s1_r1_e2 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_HR_reg_6) # non-sig

post_HR_reg_7 <- lm(post_HR_diff ~ epepq15_scrdTotal_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_HR_reg_7) # non-sig


#### How pepq interacts with scaared social to predict diff AUC, HR, and c (not controlling for phq)
### post

# HR
post_pep_HR_reg <- lm(post_HR_diff ~ epepq15_scrdTotal_s1_r1_e1*scaared_b_scrdSoc_s1_r1_e1 , data = main_df)
summary(post_pep_HR_reg)
# plot
plot_model(post_pep_HR_reg, type = "eff", terms = c("epepq15_scrdTotal_s1_r1_e1","scaared_b_scrdSoc_s1_r1_e1"))
plot_model(post_pep_HR_reg, type = "eff", terms = c("scaared_b_scrdSoc_s1_r1_e1","epepq15_scrdTotal_s1_r1_e1"))


#### How pepq interacts with scaared social to predict diff AUC, HR, and c (controlling for phq)
### post

# HR
post_pep_HR_reg <- lm(post_HR_diff ~ epepq15_scrdTotal_s1_r1_e1*scaared_b_scrdSoc_s1_r1_e1 + phq8_scrdTotal_s1_r1_e1, data = main_df)
summary(post_pep_HR_reg) # non-sig
plot_model(post_pep_HR_reg, type = "eff", terms = c("scaared_b_scrdSoc_s1_r1_e1","epepq15_scrdTotal_s1_r1_e1", "phq8_scrdTotal_s1_r1_e1"))







# Save the dataset
#write the extracted and computed summary scores to disk
write.csv(main_df, paste(output_path, 'main_df_all.csv', sep = "/", collapse = NULL), row.names=FALSE)
##################
