def write_list(lst, file_path):
    with open(file_path, 'w') as f:
        for item in lst:
            f.write(str(item) + '\n')

my_list = [1, 2, 3, 4, 5]
file_path = 'output.txt'
write_list(my_list, file_path)
print(f"List has been written to {file_path}")
