from sklearn.svm import LinearSVC
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report
from  sklearn.metrics  import accuracy_score

vectoriser = TfidfVectorizer()

class model:
    def vector_fit(x_train):
        vectoriser.fit(x_train)
        print('\n\nNo. of feature_words: ', len(vectoriser.get_feature_names_out()))
    
    def vector_transform(x):
        return vectoriser.transform(x)

    def model_Evaluate(model, x_test, y_test):

        y_pred = model.predict(x_test)

        print("\n\nClassification report: ")
        print(classification_report(y_test, y_pred))

        cf_matrix = confusion_matrix(y_test, y_pred)
        print("\n\nConfusion Matrix:")
        print(cf_matrix)
        print("\n\nPrediction Accuracy:")
        print(accuracy_score(y_test, y_pred))

    def train_lr(x_train, y_train):
        LRmodel = LogisticRegression(C = 3, max_iter = 1000, n_jobs=-1)
        LRmodel.fit(x_train, y_train) 
        return LRmodel