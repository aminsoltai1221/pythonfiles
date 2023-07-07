users = ["amin", "amirabbas", "amirhossain", "amirreza"]
def common_prefix(user_list):
    short, common, i, end = min(user_list, key=lambda x: len(x)), "", 1, 1
    while end:
        for name in users:
            word = short[0:i]
            if not name.startswith(word):
                end = 0
                break
        i = i+1
    common = short[0:i-2]
    print(common)
common_prefix(users)
