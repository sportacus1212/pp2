import os

def analyze_path(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return True, filename, directory
    else:
        return False, None, None

path = input("Enter the path: ")

exists, filename, directory = analyze_path(path)

if exists:
    print(f"Path exists.")
    print(f"Filename: {filename}")
    print(f"Directory: {directory}")
else:
    print("Path does not exist.")
