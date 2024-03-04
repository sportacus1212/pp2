with open("test.txt", "r") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            f1.write(line)
