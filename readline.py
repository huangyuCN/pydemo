file = raw_input()
p = 0
with open(file,'r+') as f:
    while True:
        line = f.readline()
        if line:
            print line