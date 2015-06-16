fileURL <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv"
download.file(fileURL,destfile="C:/Users/Win/Desktop/Coursera/Data Science Course/R Data/American Community Survey.csv")

pdfURA <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FPUMSDataDict06.pdf"
download.file(fileURL,destfile="C:/Users/Win/Desktop/Coursera/Data Science Course/R Data/American Community Survey Meta.pdf")

setwd("C:/Users/Win/Desktop/Coursera/Data Science Course/R Data/")
getwd()

ACSdata <- read.csv("American Community Survey.csv")
ACSmeta <- read.table("American Community Survey Meta.pdf",header = TRUE,sep=",")

# How many properties are worth $1,000,000 or more?
library(data.table)
length(which(ACSdata$VAL==24 & ACSdata$TEN==2))
