library(haven)
library(tidyverse)
install.packages("questionr")
library(questionr)
setwd("/Users/kihossei/OneDrive - Florida International University/Courses/QM3/session_4")
Multclass4 <- read_sav("Multclass4.sav")

model1 <- glm(binge ~ sex, family = "binomial", data = Multclass4)
summary(model1)
confint(model1)

model2 <- glm(binge ~ rapi.mean, family = "binomial", data = Multclass4)
summary(model2)
confint(model2)

model3 <- glm(binge ~ sex + rapi.mean, family = "binomial", data = Multclass4)
summary(model3)
confint(model3)

model4 <- glm(binge ~ 1, family = "binomial", data = Multclass4)
summary(model4)
# answers based on model3
#4.1



# 4.1.1
datA <- data.frame(sex = 0, rapi.mean = 0)
datB <- data.frame(sex = 0, rapi.mean = 2)
datC <- data.frame(sex = 1, rapi.mean = 0)
datD <- data.frame(sex = 1, rapi.mean = 2)

# to calculate the predicted probability
predict(model3, datA, type = "response")
predict(model3, datB, type = "response")
predict(model3, datC, type = "response")
predict(model3, datD, type = "response")

# 4.1.2

odds.ratio(model3)