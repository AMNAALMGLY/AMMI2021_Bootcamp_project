import numpy as np
class RuleBasedModel:
    def __init__(self,df_train,df_test):
        self.df_train=df_train
        self.df_test=df_test
    def classify(self):
        predict_class=[]
        for i in range(len(self.df_train)):
            if float(self.df_train[i]['f1'])<0.3 or float(self.df_train[i]['f3'])<0.5:
                predict_class.insert(i,2)
            else:
                predict_class.insert(i,1)
        return np.array(predict_class)
    
    def predict(self,idx):
        if float(self.df_test[idx]['f1'])< 0.3 or float(self.df_test[idx]['f1'])<0.5:
            return 2
        else:
            return 1
    def accuracy(self):
        summ=0
        for i in range(len(self.df_test)):
            summ+= (self.predict(i)==self.df_test[i]['class'])
        a=float(summ)/float(len(self.df_test))*100
        return a
