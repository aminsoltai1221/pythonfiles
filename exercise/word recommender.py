from listedwords import words_bank


def recommender(word):
    l = [ ]
    l2 = [ ]
    for words in words_bank:
        if words == word:
            l.append(words)
        if words.startswith(word):
            l.append(words)
        if abs(len(word) - len(words)) < 3:
            l2.append(words)
    for words in l2:
        word1 = set([i for i in word])
        word2 = set([i for i in words])
        if len(word1 - word2) < 2 and len(word2 - word1) <2:
            max_min = [words, word]
            max_min.sort(key=lambda x:len(x))
            min,max = max_min[0],max_min[1]
            m = 0
            for i in range(len(min)):
                if min[i] != max[i]:
                    m += 1
                if m > 2:
                    break
            else:    
                l.append(words)
    return l
print(recommender("can"))
            
            
         