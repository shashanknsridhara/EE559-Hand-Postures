#Feature Selection and Dimenstionality Reduction
import utils

def PrincipalComponentAnalysis(TrainPreProcessedData, TestPreProcessedData, pca_components):
    #Thanks to sklearn's decomposition class for PCA function
    pca = utils.PCA(n_components=pca_components)
    PCATrain = pca.fit_transform(TrainPreProcessedData)
    PCATest = pca.transform(TestPreProcessedData)
    return PCATrain, PCATest


def LinearDiscriminantAnalysis(TrainPreProcessedData, trainLabels, TestPreProcessedData, testLabels, num_components):
    #Unlike PCA Fischer Linear Discriminant takes train labels to calculated the discriminant subspace
    #Thanks to sklearn's discriminant_analysis class for LinearDiscriminantAnalysis function
    linear_DA = utils.LDA(n_components = num_components)
    LDATrain = linear_DA.fit_transform(TrainPreProcessedData, trainLabels)
    LDATest = linear_DA.transform(TestPreProcessedData)
    return LDATrain, LDATest


def FeatureSelection(TrainPreProcessedData, trainLabels, TestPreProcessedData, testLabels, num_components):
    #Thanks to sklearn's feature_selection class for SelectKBest function
    kbest = utils.SelectKBest(k=num_components)
    BestTrainFeatures = kbest.fit_transform(TrainPreProcessedData, trainLabels)
    BestTestFeatures = kbest.transform(TestPreProcessedData)
    return BestTrainFeatures, BestTestFeatures
