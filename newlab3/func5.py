from itertools import permutations

def Solve(word):
    print('All permutations:')
    list_of_perm=permutations(word)
    for perm in list(list_of_perm):
        print(''.join(perm))
        
word=str(input('Enter a word for permutation:\n'))
cn=Solve(word)