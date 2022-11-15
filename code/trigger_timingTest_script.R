

#######  www.ndclab.com   ###########
# By: Kianoosh Hosseini at NDCLab@FIU  
# This script reads text files that include triggers sent to the recorder laptop.
# This script is changed for different timing tests.
# These files have ".vmrk" extension.
# install.packages("pracma")
library(stringr)
library(pracma)
library(dplyr)

#setwd("~/Users/kihossei/Desktop") #set working directory to where your text file (the one that you have triggers and their times) is located.
path <- ("/Users/kihossei/OneDrive - Florida International University/time_test")

mrkTxt <- readLines(paste(path, "/resp_time_buttonBox_01.vmrk", sep = "")) # load the .vmrk file into the workspace.
myDat <- setNames(data.frame(matrix(nrow = length(mrkTxt), ncol = 1)), c("colA")) # creates an empty data frame with a single column and row # = length(mrkTxt)

# This for loop creates a dataframe from the loaded text file. 
for (i in 1:length(mrkTxt)) {
  myDat[i, 1] <- mrkTxt[i]
  
}

# Keep rows that have the string "Stimulus"
newDat <- myDat %>%
  filter(
    str_detect(colA, "Stimulus")
  )
# Let's delete all the strings to "Stimulus,"
for (i in 1:nrow(newDat)) {
  newDat$colB[i] <- gsub(".*Stimulus,", "", newDat$colA[i]) 
}

# Let's delete all the strings after the ms of the sent marker!
for (i in 1:nrow(newDat)) {
  newDat$colC[i] <- gsub(",1,0*.", "", newDat$colB[i]) 
}

newDat <- subset(newDat, select = -c(colA, colB)) # removing the colA and colB columns.
proc_fileName <- "timing_output.csv"
write.csv(newDat,paste(path,proc_fileName, sep = "/", collapse = NULL), row.names=FALSE)
newDat <- read.csv(paste(path,proc_fileName, sep = "/", collapse = NULL))

timeVal <- setNames(data.frame(matrix(ncol = 1)), c("timeDiff")) # creating an empty data frame that will be filled with time difference values!
dVal <- setNames(data.frame(matrix(ncol = 1)), c("timeDiff"))
# If you wana perform the flanker timing test for stimulus presentation run the code below!
for (i in 1:nrow(newDat)) {
  if (str_detect(newDat$colC[i], "S128")) {
    secondVal <- str2num(gsub(".*S128,", "", newDat$colC[i]))
    firstVal <- str2num(gsub(".*,", "", newDat$colC[i-2]))
    diffVal <- secondVal - firstVal
    dVal[1,] <- diffVal
    timeVal <- rbind(timeVal, dVal)
  } else {
    next
  }
}
# If you wana perform the Surprise timing test for stimulus presentation run the code below!
for (i in 1:nrow(newDat)) {
  if (str_detect(newDat$colC[i], "S128")) {
    secondVal <- str2num(gsub(".*S128,", "", newDat$colC[i]))
    firstVal <- str2num(gsub(".*,", "", newDat$colC[i-1]))
    diffVal <- secondVal - firstVal
    dVal[1,] <- diffVal
    timeVal <- rbind(timeVal, dVal)
  } else {
    next
  }
}
timeVal <- na.omit(timeVal, na.action = "omit")
mean(timeVal$timeDiff)
sd(timeVal$timeDiff)

# If you wana perform the Surprise timing test for response run the code below!
for (i in 1:nrow(newDat)) {
  if (str_detect(newDat$colC[i], "S128")) {
    firstVal <- str2num(gsub(".*S128,", "", newDat$colC[i]))
    secondVal <- str2num(gsub(".*,", "", newDat$colC[i+1]))
    diffVal <- secondVal - firstVal
    dVal[1,] <- diffVal
    timeVal <- rbind(timeVal, dVal)
  } else {
    next
  }
}
timeVal <- na.omit(timeVal, na.action = "omit")
mean(timeVal$timeDiff)
sd(timeVal$timeDiff)

######## Below is the timing test results for the Flanker task of the memory for error task######
# stimulus presentation for mfe_b study
# mean(test$value)
# [1] 21.11765
#  sd(test$value)
# [1] 1.857051

test <- na.omit(test, na.action = "omit")
mean(test$value)
sd(test$value)
######## Below is the timing test results for the Surprise task of the memory for error task######
# stimulus presentation for mfe_b study
# mean(test$value)
# [1] 20.15278
# sd(test$value)
# [1] 1.969197







