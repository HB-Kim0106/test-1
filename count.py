import sys

d = {}
with open("059.fasta",'r') as handle:
    print(type(handle))
    for i in handle:
        print(type(i))
        if i.startswith(">"):
             continue
        i = i.strip()
        for j in i: 
            if j in d:   
                d[j] += 1
    
            else:
                d[j] = 1

print(d)
