def is_palindrome(inps):
    inps = inps.lower()
    revs = ""
    for i in range(len(inps) - 1, -1, -1):
        if inps[i].isalnum():
            revs += inps[i]
    return inps == revs

inps = input("Enter a string: ")

if is_palindrome(inps):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
