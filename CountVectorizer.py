from collections import defaultdict
from itertools import chain


class CountVectorizer:
    """Преобразует список текстовых документов
     в матрицу подсчета вхождений слов в каждый документ."""
    def __init__(self):
        self.features = []

    def fit_transform(self, corpus: list):
        lower_split_corpus = [list(map(lambda x: x.lower(),
                                       text.split())) for text in corpus]
        self.features = list(set(chain.from_iterable(lower_split_corpus)))

        word_to_index = defaultdict()

        for index, word in enumerate(self.features):
            word_to_index[word] = index

        matrix = []

        for text in lower_split_corpus:
            str_in_matrix = [0] * len(self.features)
            for word in text:
                str_in_matrix[word_to_index[word]] += 1
            matrix.append(str_in_matrix)

        return matrix

    def get_feature_names(self):
        return self.features


corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]

vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print(count_matrix)
print(vectorizer.__doc__)

