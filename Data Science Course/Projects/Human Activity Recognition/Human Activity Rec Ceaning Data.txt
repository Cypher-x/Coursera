#Human Activity Recognition Using Smartphones 
#Getting and cleaning the data
#unzip the file to the desktop first!
#file location:
#H:/5 Personal Projects/Coursera/
#   Data Science Course/R Data/UCI HAR Dataset Small 6_20_15.zip

dir <- "C:/Users/Win/Desktop/UCI HAR Dataset"
test_dir <- "C:/Users/Win/Desktop/UCI HAR Dataset/test"
train_dir <- "C:/Users/Win/Desktop/UCI HAR Dataset/train"
library(plyr)

#=======Features
#Loading in features
setwd(dir)
features_col <- read.table("features.txt")
features_col$V1 = NULL
features_row <- t(features_col)
rm(features_col)

#==========Test Data
#Loading in test
setwd(test_dir)
x_test <- read.table("X_test.txt")
y_test <- read.table("y_test.txt")
subject_test <- read.table("subject_test.txt")

#-----Label data with Descriptive variable names
colnames(x_test) <- features_row
colnames(y_test) <- "activitiesNUMERIC"
colnames(subject_test) <- "subject_ID"

#-----Recode activities to descriptive activity names
activities_recode <-
  data.frame("activities" = c(ifelse(y_test$activitiesNUMERIC == 1, 
       "WALKING",
       ifelse(y_test$activitiesNUMERIC == 2, 
              "WALKING_UPSTAIRS", 
              ifelse(y_test$activitiesNUMERIC == 3,
                     "WALKING_DOWNSTAIRS",
                     ifelse(y_test$activitiesNUMERIC == 4,
                            "SITTING",
                            ifelse(y_test$activitiesNUMERIC == 5,
                                   "STANDING",
                                   ifelse(y_test$activitiesNUMERIC == 6,
                                          "LAYING",NA))))))))


#-----Extract only measurements: mean and stdev
InName_mean_stdev <- grepl("mean|std()|Mean",colnames(x_test))
xtest_subset <- x_test[,InName_mean_stdev]
rm(x_test)

#Bind the columns
bind_test <- data.frame(subject_test, 
                        y_test, 
                        activities_recode,
                        xtest_subset)

#Remove excess data
rm(activities_recode);rm(subject_test); rm(xtest_subset); rm(y_test)

#==========Train Data
#Loading in train
setwd(train_dir)
x_train <- read.table("X_train.txt")
y_train <- read.table("y_train.txt")
subject_train <- read.table("subject_train.txt")

#-----Label data with Descriptive variable names
colnames(x_train) <- features_row
colnames(y_train) <- "activitiesNUMERIC"
colnames(subject_train) <- "subject_ID"

#-----Recode activities to descriptive activity names
activities_recode <-
  data.frame("activities" = c(ifelse(y_train$activitiesNUMERIC == 1, 
                                     "WALKING",
                                     ifelse(y_train$activitiesNUMERIC == 2, 
                                            "WALKING_UPSTAIRS", 
                                            ifelse(y_train$activitiesNUMERIC == 3,
                                                   "WALKING_DOWNSTAIRS",
                                                   ifelse(y_train$activitiesNUMERIC == 4,
                                                          "SITTING",
                                                          ifelse(y_train$activitiesNUMERIC == 5,
                                                                 "STANDING",
                                                                 ifelse(y_train$activitiesNUMERIC == 6,
                                                                        "LAYING",NA))))))))

#-----Extract only measurements: mean and stdev
InName_mean_stdev <- grepl("mean|std()|Mean",colnames(x_train))
xtrain_subset <- x_train[,InName_mean_stdev]
rm(x_train)

#Bind the columns
bind_train <- data.frame(subject_train, 
                        y_train, 
                        activities_recode,
                        xtrain_subset)

#Remove excess data
rm(activities_recode);rm(subject_train); rm(xtrain_subset); rm(y_train)

#======Merge train and test data sets
HAR_data <- rbind(bind_test,bind_train)
rm(bind_test);rm(bind_train);rm(features_row)

#======Tidy Data of Avg of each var 
#       for every subject-activity combo===
HAR_avgs_data <- 
  aggregate(HAR_data, by=list(
    subject_ID = HAR_data$subject_ID, 
    activitiesNUMERIC = HAR_data$activitiesNUMERIC,
      activities = HAR_data$activities),mean)
HAR_avgs_data[,6] = NULL
HAR_avgs_data[,5] = NULL
HAR_avgs_data[,4] = NULL

setwd(dir)
write.table(HAR_avgs_data, "HAR_avgs_data.txt", 
            row.name=FALSE)
  