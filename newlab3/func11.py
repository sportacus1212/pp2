def is_palindrome(word):
    
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_word = ''.join(word.lower().split())

    # Check if the cleaned word is the same when reversed
    return cleaned_word == cleaned_word[::-1]

# Example usage:
user_input = input("Enter a word or phrase: ")
result = is_palindrome(user_input)

if result:
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")