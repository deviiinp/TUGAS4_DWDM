#Getting started with Naive Bayes
#Install the package
#install.packages(“e1071”)
#Loading the library
library(e1071)
?naiveBayes
data("Flags")
Flags_df=as.data.frame(Flags)
repeating_sequence=rep.int(seq_len(nrow(Flags_df)), Flags_df$Freq) #This will repeat each combination equal to the frequency of each combination
#Create the dataset by row repetition created
Flags_dataset=Flags_df[repeating_sequence,]
#We no longer need the frequency, drop the feature
Flags_dataset$Freq=NULL
 
#Fitting the Naive Bayes model
Naive_Bayes_Model=naiveBayes(Indonesia ~., data=Flags_dataset)
#What does the model say? Print the model summary
Naive_Bayes_Model
 
#Prediction on the dataset
NB_Predictions=predict(Naive_Bayes_Model,Flags_dataset)
#Confusion matrix to check accuracy
table(NB_Predictions,Flags_dataset$Indonesia)
 
#Getting started with Naive Bayes in mlr
#Install the package
#install.packages(“mlr”)
#Loading the library
library(mlr)
 
#Create a classification task for learning on Titanic Dataset and specify the target feature
task = makeClassifTask(data = Flags_dataset, target = "Indonesia")
 
#Initialize the Naive Bayes classifier
selected_model = makeLearner("classif.naiveBayes")
 
NB_mlr = flags(selected_model, task)
 
#Read the model learned  
NB_mlr$learner.model
 
#Predict on the dataset without passing the target feature
predictions_mlr = as.data.frame(predict(NB_mlr, newdata = Flags_dataset[,1:3]))
 
##Confusion matrix to check accuracy 
table(predictions_mlr[,1],Flags_dataset$Indonesia)<span style="font-family: 'Noto Serif', serif"><span>

