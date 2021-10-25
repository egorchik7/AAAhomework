class CountVectorizer:
    '''Делает терм-документную матрицу и опорные слова в тексте'''
    
    
    def __init__(self):
        '''Конструктор'''
        pass
        
        
    def fit_transform(self, corpus) -> list:
        '''Делает терм-документную матрицу в формате списка'''
        result = []
        corpus_lower = lower_words(corpus)
        unique_set = unique_words(corpus_lower)
        for elem in corpus_lower:
            count_set = []
            for uniq in unique_set:
                count_set.append(elem.split(' ').count(uniq))
            result.append(count_set)
        return result
        
    
    def get_feature_names(self, corpus) -> list:
        '''Делает список опорных слов в тексте'''
        result = []
        corpus_lower = lower_words(corpus)
        result = unique_words(corpus_lower)
        return result
        
       
corpus = ['Crock Pot Pasta Never boil pasta again','Pasta Pomodoro Fresh ingredients Parmesan to taste',
          'Pasta Boloneze parmesan cut again', 'Pasta Rizottotototo boil again']
          
          
def unique_words(datalist) -> list:
    '''Делает список уникальных(без повторений) слов в тексте'''
    result = []
    words = []
    for elem in datalist:
        for word in elem.split(' '):
            words.append(word)
    [result.append(x) for x in words if x not in result]
    return result
    
def lower_words(datalist) -> list:
    '''Все слова строчными буквами'''
    result = []
    [result.append(x.lower()) for x in datalist]
    return result


def main():
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    feature_names = vectorizer.get_feature_names(corpus)
    print(feature_names)
    print(count_matrix)
if  __name__ == '__main__':
    main()
    
