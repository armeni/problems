from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
import numpy as np
import csv


class Parser:
    def __init__(self, categories, file, train):
        self.target_names = categories
        self.data = []
        self.filenames = []
        self.train = train
        file_train = list(csv.reader(open(file, 'rt', encoding="utf8"), delimiter='\t'))
        if train:
            self.target = []
            for line in file_train:
                self.data.append(line[2])
                self.filenames.append(line[1])
                self.target.append(self.target_names.index(line[0]))
        else:
            for line in file_train:
                self.data.append(line[1])
                self.filenames.append(line[0])


categories = ['science', 'style', 'culture', 'life', 'economics', 'business', 'travel', 'forces', 'media', 'sport']
docs_train = Parser(categories, 'news_train.txt', True)
docs_test = Parser(categories, 'news_test.txt', False)

text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-5, random_state=50))])

text_clf = text_clf.fit(docs_train.data, docs_train.target)

print(np.mean(text_clf.predict(docs_train.data) == docs_train.target))

output = open("news_output.txt", 'w')
for i in text_clf.predict(docs_test.data):
    output.write("%s\n" % docs_test.target_names[i])