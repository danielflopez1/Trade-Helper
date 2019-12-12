import pickle
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize

class VoteClassifier(ClassifierI):
    def __init__(self):
        self.classifier_names = ["originalnaivebayes5k.pickle",     #after saving the classifier models with SentimentAnalysis.py
                            "MNB_classifier5k.pickle",              #set the multiple models to check each other
                            "BernoulliNB_classifier5k.pickle",
                            "LinearSVC_classifier5k.pickle",
                            "LogisticRegression_classifier5k.pickle",
                            "SGDC_classifier5k.pickle"]
        self.classifiers = []
        self.set_wordfeatures()

    def set_wordfeatures(self):
        word_features5k_f = open("word_features5k.pickle", "rb")    #set the word features that might distinguish easily documents in positive and negative values
        self.word_features = pickle.load(word_features5k_f)
        word_features5k_f.close()

    def set_classifiers(self,classifier_names = []):                #open the classifiers and add them or use the default ones
        if(classifier_names != []):
            for classifier_name in classifier_names:
                open_file = open(classifier_name, "rb")
                self.classifiers.append(pickle.load(open_file))
                open_file.close()
        else:
            for classifier_name in self.classifier_names:
                open_file = open(classifier_name, "rb")
                self.classifiers.append(pickle.load(open_file))
                open_file.close()

    def classify_vote(self, features):          #the classifiers vote on how they see the text and the votes will be appended
        votes = []
        for x in range(len(self.classifiers)):
            c = self.classifiers[x]
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):         # The classifiers will have a vote and given their confidentce it will be measured
        votes = []
        for x in range(len(self.classifiers)):
            c = self.classifiers[x]
            v = c.classify(features)
            votes.append(v)
        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf

    def find_features(self,document):
        words = word_tokenize(document)
        features = {}
        for w in self.word_features:
            features[w] = (w in words)
        return features


    def get_sentiment(self,text):   #finally give the text and get the sentiment value ('neg' or 'pos' and the confidence value from 0 to 1
        self.set_classifiers()
        feats = self.find_features(text)
        return self.classify_vote(feats), self.confidence(feats)





if __name__ == '__main__':
    #example
    vc = VoteClassifier()
    print(vc.get_sentiment('the grass is green '))






