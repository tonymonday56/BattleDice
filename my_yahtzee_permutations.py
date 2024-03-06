# my_yahtzee_permutations.py
import itertools
count = 1
for v in itertools.permutations(range(1,7), 6): # 1,2,3,4,5,6
    print(v)
    print(count)
    count = count + 1
    

