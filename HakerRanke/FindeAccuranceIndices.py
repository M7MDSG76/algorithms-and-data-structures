# Enter your code here. Read input from STDIN. Print output to STDOUT

S = input()
k = input()

def find_accurance_indices(S, k):
    indices = []
    S_letters = []
    k_letters = []
    x = [indices, S_letters, k_letters]
    for i, k_letter in enumerate(k):
        print(f'i: {i}, kl:{k_letter}\n')
        for j, S_letter in enumerate(S):
            print(f'i: {j}, Sl:{S_letter}\n')
            if k_letter == S_letter:
                print(f'find: {k_letter}')
                indices.append(j)
                S_letters.append(S_letter)
                k_letters.append(k_letter)
                S = S[j+1:]
                print(S)
                break
            
                
            
                
                
    
            
    output = (indices[0], indices[-1])            

    for i in x:
        print(i, end=',\n')   
find_accurance_indices(S,k)

    
# def find_accurance_indices(S, k):
    