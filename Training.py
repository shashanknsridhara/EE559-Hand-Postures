#This file will contain different functions for different training methods.
#We can write one common function for for finding error rate and accuracy.
import utils

def SupportVectorMachine(Train, TrainLabels, Test, TestLabels, d, c):
    svmPred = utils.SVC(gamma='auto',kernel='rbf')
    svmPred.fit(Train, TrainLabels)
    accuracy_train= svmPred.score(Train, TrainLabels)
    predictions = svmPred.predict(Test)
    accuracy = utils.metrics.accuracy_score(TestLabels, predictions)
    fscore = utils.f1_score(TestLabels, predictions, average='micro')
    print("SVM - Train Accuracy: ", accuracy_train)
    print("SVM with RBF:  Test Accuracy - ",  accuracy, '  F1-Score-  ', fscore)    


def NaiveBayes(Train, TrainLabels, Test, TestLabels):
    naive_bayes = utils.GaussianNB()
    predictions = naive_bayes.fit(Train, TrainLabels).predict(Test)
    accuracy = utils.metrics.accuracy_score(TestLabels, predictions)
    fscore = utils.f1_score(TestLabels, predictions, average='micro')
    print("Naive Bayes Classifier: Test Accuracy - ",  accuracy, '  F1-Score-  ', fscore)


def RandomForestClassifierWithXGBoost(Train, TrainLabels, Test, TestLabels):
    RFModel = utils.RandomForestClassifier(n_estimators = 80, max_depth=100, random_state = 0)
    RFModel.fit(Train, TrainLabels)
    predictions = RFModel.predict(Test)
    predictions = RFModel.predict(Test)
    accuracy_train= RFModel.score(Train, TrainLabels)
    accuracy = utils.metrics.accuracy_score(TestLabels, predictions)
    fscore = utils.f1_score(TestLabels, predictions, average='micro')
    print("Random Forest - Train Accuracy: ", accuracy_train)
    print("Random Forest:  Test Accuracy - ",  accuracy, '  F1-Score-  ', fscore)    

def KNearestNeighbors(Train, TrainLabels, Test, TestLabels):
    K_vals = range(1,26)
    accuracy = {}
    accuracy_list =[]
    for i in K_vals:
        K_neighbor = utils.KNeighborsClassifier(n_neighbors =i)
        K_neighbor.fit(Train, TrainLabels)
        predictions = K_neighbor.predict(Test)
        accuracy[i] = utils.metrics.accuracy_score(TestLabels, predictions)
        accuracy_list.append(utils.metrics.accuracy_score(TestLabels, predictions))

    #Accuracy with auto values
    K_neighbor_new = utils.KNeighborsClassifier(algorithm='auto')
    K_neighbor_new.fit(Train, TrainLabels)
    predictions_new = K_neighbor.predict(Test)

    accuracy_train= K_neighbor_new.score(Train, TrainLabels)
    accuracy = utils.metrics.accuracy_score(TestLabels, predictions_new)
    fscore = utils.f1_score(TestLabels, predictions, average='micro')
    print("K-nearest Neighbor - Train Accuracy: ", accuracy_train)
    print("K-nearest Neighbor:  Test Accuracy - ",  accuracy, '  F1-Score-  ', fscore)  
    
    #Plot the Test Accuracy vs K values
    utils.plt.plot(K_vals, accuracy_list)
    utils.plt.xlabel('Value of K for K-Nearest Neighbor')
    utils.plt.ylabel('Testing Accuracy')
    utils.plt.title('KNN Accuracy vs K value with Standardization and PCA (3-Components)')
    utils.plt.savefig("KNN_accuracyVSK's.png")
