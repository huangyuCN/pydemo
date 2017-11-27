file = raw_input()
with open(file) as f:
    for line in f.readlines():
        print(line.strip())