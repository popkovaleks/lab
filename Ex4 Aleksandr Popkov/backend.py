from flask import Flask, request, jsonify
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer

import requests
import string
import pickle
import json
import os

APP = Flask(__name__)


def remove_punctiation(question):
    """Removing punctuation
    """

    question_without_punctuation = question.translate(str.maketrans("", "", string.punctuation))
    return question_without_punctuation

def lemmatize_and_remove_stopwords(question):
    """Lemmatization and removing stop words
    """
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(question)

    question_without_stopwords = []

    for word in tokens:
        if word not in stop_words:
            word = lemmatizer.lemmatize(word)
            question_without_stopwords.append(word)

    return " ".join(question_without_stopwords)


def get_response(question, confidence = 0.5):
    
    parameters = {'text': question, 'confidence': confidence}

    response = requests.get(url='http://webengineering.ins.hs-anhalt.de:43720/rest/annotate',
                          params=parameters,
                          headers={'accept': 'application/json'},
                          verify=False)

    return response.json()

def get_links(data):

    dictionary = {}

    try:
        data_resources = data['Resources']

        for i in data_resources:
            dictionary[i['@URI']] = i['@surfaceForm']
    
    finally:
        return dictionary


@APP.route('/health', methods=['GET'])
def health():
    """Function for checking server status
    """

    response = {"status" : "OK"}
    return jsonify(response)

@APP.route('/question', methods=['POST'])
def question():

    
    print('--------')
    question_text = request.get_json()
    print(question_text)
    print(question_text['question'])

    response = {}

    response['answer_text'] = 'This is your question: "{}"'.format(question_text['question'])
    question_preprocessed = lemmatize_and_remove_stopwords(remove_punctiation(question_text['question']))
    response['named_entities'] = get_links(get_response(question_preprocessed, 0.5))

    print(response)
    
    with open('vectorizerBoW', 'rb') as vectorizerB:
        vectorizer = pickle.load(vectorizerB)

    with open('question_classifier', 'rb') as trained_model:
        model = pickle.load(trained_model)

    text = vectorizer.transform([question_text['question']]).toarray()
    relation = model.predict(text)
    print(relation)
    
    response['relation'] = relation.tolist()

    print('__________________________________________________________________________')
    data_list = []
    if (os.path.isfile('output.json') == True):
        with open('output.json', 'r') as output_file:
            loaded_file = json.load(output_file)
            if isinstance(loaded_file, dict):
                data_list.append(loaded_file)
            else:
                data_list = loaded_file
        data_list.append(response)
        print(data_list)
        with open('output.json', 'w') as output_file:
            json.dump(data_list, output_file, indent=4)
            
    else:
        data_list.append(response)
        with open('output.json', 'w') as output_file:
            json.dump(response, output_file, indent=4)

    


    return jsonify(response)
    
def main():
    APP.run(host='0.0.0.0', debug=True)

if __name__ == "__main__":
    main()