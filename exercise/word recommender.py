words_list = ["assert", "can", "candy"]


with open("words.txt", "r") as wf:
    result = wf.readlines()
    for i in result:
        words_list.append(i)
    
print(words_list) 


# def recommender(word):
#     l = [ ]
#     l2 = [ ]
#     for words in words_list:
#         if words == word:
#             l.append(words)
#         if words.startswith(word):
#             l.append(words)
#         if abs(len(word) - len(words)) < 3:
#             l2.append(words)
#     for words in l2:
#         word1 = set([i for i in word])
            
        
#     return l
# print(recommender("can"))
            
            
         