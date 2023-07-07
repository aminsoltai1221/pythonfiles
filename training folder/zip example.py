names = ["Amin", "hadi", "hasan", "ali"]
scores = [1, 3, 6, 7]
results = zip([1, 2, 3, 4], names, scores)
for i, j, k in results:
    print(f"{i}: name = {j} ===>  score = {k}")
