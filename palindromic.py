sequence = input("input: ")

i_palindromic = 0


d_DNA = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

if len(sequence)%2 == 0:
    for i in range(len(sequence)):
        if sequence[i] == d_DNA[sequence[-(i+1)]]:
            i_palindromic += 0
              
        else:
            i_palindromic += 1
    
    if i_palindromic == 0:
        print("{0} is palindromic".format(sequence))
    
    else:
        print("{0} is not palindromic".format(sequence))
    
else:
    print("{0} is not palindromic".format(sequence))
