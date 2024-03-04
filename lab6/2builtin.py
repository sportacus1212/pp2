def count_upper_lower_case_letters(input_string):
    uc = 0
    lc = 0
    for char in input_string:
        if char.isupper():
            uc += 1
        elif char.islower():
            lc += 1
    return uc, lc

input_string = input("Enter a string: ")

uc, lc = count_upper_lower_case_letters(input_string)

print(f"Number of uppercase letters: {uc}")
print(f"Number of lowercase letters: {lc}")
