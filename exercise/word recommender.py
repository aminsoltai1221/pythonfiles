

<<<<<<< HEAD
=======
with open("exercise/listofwords.txt") as wf:
    result = wf.readlines()
    for i in result:
        words_list.append(i[:-1])
    
with open("listedwords", "w") as lw:
    lw.write(str(words_list))
    
print(words_list) 
>>>>>>> origin/main


def recommender(word):
    l = [ ]
    l2 = [ ]
    for words in words_list:
        if words == word:
            l.append(words)
        if words.startswith(word):
            l.append(words)
        if abs(len(word) - len(words)) < 3:
            l2.append(words)
    for words in l2:
        word1 = set([i for i in word])
            
        
    return l
print(recommender("can"))
            
            
         