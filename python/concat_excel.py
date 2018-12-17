fout=open("output.csv","a")
# first file:
for line in open("excel0" + ".csv"):
    fout.write(line)
# now the rest:    
for num in range(1,10):
    f = open("excel" +str(num)+".csv")
    f.__next__() # skip the header
    for line in f:
        if line[-1] != '\n': line += '\n'
        fout.write(line)
    f.close() # not really needed
fout.close()


# Concat csv files together with has the same label of columns
# Files are limited to filename of increasing numbers