words = ["hello", "hell", "heat", "hello world"]
def common_prefix(words):
    common = ""
    for i in range(len(min(words, key=lambda x: len(x)))):
        if len(set(name[i] for name in words)) != 1:
            break
        common += words[0][i]
    print()

common_prefix(words)