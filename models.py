from sklearn.linear_model import RidgeClassifier
from sklearn.linear_model import Perceptron
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
import basic_model
import  pickle
import os


def save_model(model,model_name):
    model_file = os.path.join(os.getcwd(),model_name+'.pkl')
    with open(model_file, 'wb') as f:
        pickle.dump(model, f)
if __name__=="__main__":
    X_train, y_train, X_test, y_test=basic_model.load_data()
    clf = RidgeClassifier(tol=1e-2, solver="sag")
    basic_model.benchmark(clf, X_train, y_train, X_test, y_test)

    clf1 = Perceptron(max_iter=50,random_state=42)
    basic_model.benchmark(clf1, X_train, y_train, X_test, y_test)

    clf2 = PassiveAggressiveClassifier(max_iter=50)
    basic_model.benchmark(clf2, X_train, y_train, X_test, y_test)

    clf3 = KNeighborsClassifier(n_neighbors=50)
    basic_model.benchmark(clf3, X_train, y_train, X_test, y_test)

    clf4 = RandomForestClassifier(n_estimators=100)
    basic_model.benchmark(clf4, X_train, y_train, X_test, y_test)

    clf5 = BernoulliNB(alpha=.01)
    basic_model.benchmark(clf5, X_train, y_train, X_test, y_test)

    clf6 = MultinomialNB(alpha=.01)
    basic_model.benchmark(clf6, X_train, y_train, X_test, y_test)

    eclf = VotingClassifier(estimators=[('rc', clf),('pc', clf1),  ('pac', clf2), ('knn', clf3),('rfc',clf4),('bnb',clf5),('mnb',clf6)], voting='hard')
    vectorizer,clf_descr,score, train_time, test_time = basic_model.benchmark(eclf, X_train, y_train, X_test, y_test)

    save_model(eclf, 'ensembel_model')
    save_model(vectorizer, 'count_vector')


