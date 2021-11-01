import math
from typing import List


def unique_words(datalist) -> list:
    result = []
    words = []
    for elem in datalist:
        for word in elem.split(' '):
            words.append(word)
    [result.append(x) for x in words if x not in result]
    return result


def lower_words(datalist) -> list:
    result = []
    [result.append(x.lower()) for x in datalist]
    return result


class CountVectorizer:
    corpus = ['Crock Pot Pasta Never boil pasta again', 'Pasta Pomodoro Fresh ingredients Parmesan to taste']

    def fit_transform(self, corpus) -> list:
        result1 = []
        corpus_lower = lower_words(corpus)
        unique_set = unique_words(corpus_lower)
        for elem in corpus_lower:
            count_set1 = []
            for uniq in unique_set:
                count_set1.append(elem.split(' ').count(uniq))
            result1.append(count_set1)
        return result1

    def get_feature_names(self) -> list:
        result = []
        corpus_lower = lower_words(self.corpus)
        result = unique_words(corpus_lower)
        return result


class TfidfTransformer:

    def idf_transform(self, count_matrix) -> List[float]:
        total_documents = len(count_matrix)
        idf_vector = []
        for ind, _ in enumerate(count_matrix[0]):
            documents_with_feature = 0
            for document_counts in count_matrix:
                if document_counts[ind] > 0:
                    documents_with_feature += 1
            idf_vector.append(math.log((total_documents + 1) / (documents_with_feature + 1)) + 1)
        return idf_vector

    def tf_transform(self, matrix: List[List[int]]) -> List[List[float]]:
        answer = []
        for index, row in enumerate(matrix):
            answer.append([])
            total_cnt = sum(row)
            for element in row:
                answer[index].append(element / total_cnt)
        return answer

    def fit_transform(self, count_matrix: List[List[int]]) -> List[List[float]]:
        tf = self.tf_transform(count_matrix)
        idf = self.idf_transform(count_matrix)
        tfidf = []
        for row, _ in enumerate(count_matrix):
            document_tfidf = []
            for col, _ in enumerate(count_matrix[0]):
                document_tfidf.append(tf[row][col] * idf[col])
            tfidf.append(document_tfidf)
        return tfidf


class TfidfVectorizer(CountVectorizer):

    def __init__(self):
        super().__init__()
        self._tfidf_transformer = TfidfTransformer()

    def fit_transform(self, corpus) -> list:
        count_matrix = super().fit_transform(corpus)
        tfidf_matrix = self._tfidf_transformer.fit_transform(count_matrix)
        return tfidf_matrix


def main():
    corpus = ['Crock Pot Pasta Never boil pasta again', 'Pasta Pomodoro Fresh ingredients Parmesan to taste']
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)


if __name__ == '__main__':
    main()

