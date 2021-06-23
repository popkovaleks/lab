import requests
import json
import string
import random


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


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

def tokenize_question(question):
    tokens = word_tokenize(question)
    return(tokens)

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



def main():

    with open('question2.json') as questions_json:
        questions_list = json.load(questions_json)

    output = []

    for question in questions_list:
        response = {}

        response['id'] = question['id']
        response['question'] = question['question']
        question_not_tokenized = lemmatize_and_remove_stopwords(remove_punctiation(question['question']))
        response['question_preprocessed'] = tokenize_question(question_not_tokenized)
        response['named_entities'] = get_links(get_response(response['question'], 0.5))
        response['named_entities_preprocessed'] = get_links(get_response(question_not_tokenized, 0.5))
        #print(response)
        output.append(response)

    with open('question_2_out.json', 'w') as output_file:
        json.dump(output, output_file, indent=4)

    random_numbers = []

    while len(random_numbers) < 5:
        number = random.randint(0, len(output) - 1)

        if not (response in random_numbers):
            random_numbers.append(number)
            resp = output[number]
            print("Question ID: {}".format(resp['id']))
            print(resp['question'])
            print("------------------------------")


if __name__ == "__main__":
    main()