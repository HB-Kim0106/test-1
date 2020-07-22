import sys

n = int(sys.argv[1])  #int로 받아야 한다.

l1 = ["A", "T", "C", "G"]
l2 = ["A", "T", "C", "G"]

def mer(l1, l2, n):

    if n == 1:
        return l2
        
    l_d = []
    for i in l1:
        for j in l2:
            l_d.append(i+j)
    return mer(l1,l_d, n-1)  # mer함수 돌려서 나오는 값이기에 위치는 mer 다음!
       
result = mer(l1, l2, n)
print(result)
     
