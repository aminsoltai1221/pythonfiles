print([i if i%2==0 else ("-" if i%3==0 else " No") for i in range(11)])

l=[[1,2,3],[4,5,6]]
# print([[i for i in n] for n in l])
# print([n for n in [i for i in l]])
# print([n for n in [i for i in l]])
[[print(n) for n in p] for p in l]

# for n in l:
#     for i in n:
#         print(i)
      
