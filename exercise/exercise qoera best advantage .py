import random

def cases_calc(a,b,c,A,B,C,X,Y,T,P):
    cases=[]
    for brown_number in range(P+1):
        for white_number in range(P+1):
            for magic_number in range(P+1):
                if magic_number <= T:
                    if (brown_number + white_number + magic_number) == P:
                        cases.append([brown_number, white_number, magic_number])
    results = []
    def best_calc(l):
        brown_number = l[0]
        white_number = l[1]
        magic_number = l[2]
        def magic_advantage(c,C,magic_number):
            magic_advan = (C - c) * magic_number
            return magic_advan
        def white_advantage(c,C,magic_number):
            white_advan = ((B - b) * white_number) - ((0 + (white_number-1) * Y) * (white_number)) / 2
            return white_advan
        def grown_advantage(c,C,magic_number):
            grown_advan = ((A - a) * brown_number) - ((0 + (brown_number-1) * X) * (brown_number)) / 2
            return grown_advan
        total_advan = (magic_advantage(c,C,magic_number) + grown_advantage(c,C,magic_number) 
                    + white_advantage(c,C,magic_number))
        return list([l, total_advan])
    for case in cases:
        results.append(best_calc(case))
    results.sort(key=lambda x:x[1])  
    print(*results[-1:])
cases_calc(1,1,1,20, 30, 40, 4, 6, 2, 10)