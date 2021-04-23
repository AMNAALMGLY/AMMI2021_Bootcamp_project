from utils import read_data
from utils import read_test
from model import RuleBasedModel



def main():
    #path="/Users/benjaminbenteke/Desktop/AMMI_bootCampProject/AMMI2021_Bootcamp_project/" #change the path in
    train_file = "train_data.txt"
    test_file = "test_data.txt"
    variables = ['ID', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'class']


    print ("========= Reading train dataset =========")

    	# TO DO:
    train=read_data(variables,train_file)
    
	# use the read data function you created to read the train data
    print ("======== Done reading =========.\n")

    print ("========= Reading test data =========")
    	# TO-DO 
    test=read_test(variables,test_file)

	# Read the test  data
    print ("========= Done reading =========.\n")

    print ("==== Training classifier =====")
	# TO-DO
    dt=RuleBasedModel(train,test)
    dt.classify()
	# Initialize the classifier you built in model.py and return the necessary values
    print ("======== Done training classifier ===========.\n")

    print ("========= Classifying test samples =======")
	# TO-DO 
	# use your classifier to do predictions on all the test samples
    print ("========== Done classifying =======")

    	# TO-DO
    # class_test=dt.
	# Evalutate your classifier with the Accuracy function you implemented and return the necessary outputs
    accu=dt.accuracy()
    numCorrect=(accu*len(test))/100
    total_samples=len(test)
    print("Model's Accuracy {}% model correctly predicted {} out of {}".format(accu,numCorrect,total_samples))
    #print(f"Model's Accuracy {round(accu)} %, model correctly predicted {numCorrect} out of {total_samples}")
    print('================================================================')
    print ("finished.\n")

if __name__== '__main__':
    main()

