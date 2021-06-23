import pandas as pd
import string
import pickle

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import f1_score,precision_score, recall_score, classification_report
from nltk.tokenize import word_tokenize


def average_numbers(train, test):
    all_questions = pd.concat([train, test])

    count_words = 0
    count_questions = 0
    count_characters = 0

    for question in all_questions['question']:
        question_without_punctuation = question.translate(str.maketrans("", "", string.punctuation))
        question_tokens = word_tokenize(question_without_punctuation)

        for word in question_tokens:
            count_characters = count_characters + len(word)

        count_words = count_words + len(question_tokens)
        count_questions = count_questions + 1

    average_tokens = count_words / count_questions
    average_characters = count_characters / count_questions

    return average_tokens, average_characters


def bag_of_words(train, test):
    
    vectorizer = CountVectorizer()
    vectorizer.fit(train.append(test).question)
    
    x_train = vectorizer.transform(train.question)
    y_train = train.predicate.values

    x_test = vectorizer.transform(test.question)
    y_test = test.predicate.values

    with open('vectorizerBoW', 'wb') as vectorizerB:
        pickle.dump(vectorizer, vectorizerB)

    return x_train, y_train, x_test, y_test

def tf_idf(train,test):

    vectorizer = TfidfVectorizer()
    vectorizer.fit(train.append(test).question)

    x_train = vectorizer.transform(train.question)
    y_train = train.predicate.values

    x_test = vectorizer.transform(test.question)
    y_test = test.predicate.values

    return x_train, y_train, x_test, y_test

def main():

    train = pd.read_csv("train.csv", sep=';')
    test = pd.read_csv("test.csv", sep=';')

    average_tokens, average_characters = average_numbers(train, test)

    print("Average tokens: {}, Average characters: {}".format(average_tokens, average_characters))
    
    print(train.groupby(['predicate']).sum())
    print(test.groupby(['predicate']).sum())

    #Bag of Words
    x_train_bow, y_train_bow, x_test_bow, y_test_bow = bag_of_words(train, test)

    classifier_bow = LogisticRegression()
    classifier_bow.fit(x_train_bow, y_train_bow)
    y_predict_bow = classifier_bow.predict(x_test_bow)

    f1_bow = f1_score(y_test_bow, y_predict_bow, average='weighted')
    print('F1 Score for BoW = {0}'.format(f1_bow))

    recall_bow = recall_score(y_test_bow, y_predict_bow, average='weighted')
    print('Recall Score for BoW = {0}'.format(recall_bow))

    precision_bow = precision_score(y_test_bow, y_predict_bow, average='weighted')
    print('Precision Score for BoW = {0}'.format(precision_bow))

    print(classification_report(y_test_bow, y_predict_bow))

    print('_______________________________________')

    #TF-IDF
    x_train_tf, y_train_tf, x_test_tf, y_test_tf = tf_idf(train, test)

    classifier_tf = LogisticRegression()
    classifier_tf.fit(x_train_tf, y_train_tf)
    y_predict_tf = classifier_tf.predict(x_test_tf)

    f1_tf = f1_score(y_test_tf, y_predict_tf, average='weighted')
    print('F1 Score for TF-IDF = {0}'.format(f1_tf))

    recall_tf = recall_score(y_test_tf, y_predict_tf, average='weighted')
    print('Recall Score for TF-IDF = {0}'.format(recall_tf))

    precision_tf = precision_score(y_test_tf, y_predict_tf, average='weighted')
    print('Precision Score for TF-IDF = {0}'.format(precision_tf))

    print(classification_report(y_test_tf, y_predict_tf))

    with open('question_classifier', 'wb') as model:
        pickle.dump(classifier_bow, model)

    

if __name__ == "__main__":
    main()