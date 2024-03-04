import os

def list_directories(path):
    return [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]

def list_files(path):
    return [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]

def list_all(path):
    return os.listdir(path)

path = input("Enter the path: ")

print("Directories:")
print(list_directories(path))

print("\nFiles:")
print(list_files(path))

print("\nAll directories and files:")
print(list_all(path))
