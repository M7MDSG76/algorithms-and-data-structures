

def is_palindrom(string: str, low: int, high: int):
    # print(f'low:{low}, high:{high}')
    while low <= high:
        # print(f'string[low]: {string[low]}, string[high] {string[high]}')
        if string[low] != string[high]:
            return False
        low += 1
        high -= 1
    return True    


def all_pal_part_util(all_part: list, current_part: list, start: int, string_len: int, string: str):
    
    if start >= string_len:
        
        temp = current_part.copy()
        all_part.append(temp)
        return
    # print(f'start:{start}, string_len:{string_len}')
    for i in range(start, string_len):
        # print(f'i: {i},string[i]: {string[i]} ')
        if is_palindrom(string, start, i):
            
            current_part.append(string[start:i+1])
            
            all_pal_part_util(all_part, current_part, i+1, string_len, string)
            
            current_part.pop()
            

def all_pallindrom_partitioning(string:str):
    
    all_part = []
    current_part = []
    string_len = len(string)
    
    all_pal_part_util(all_part, current_part, 0, string_len, string)
    print()
    for i in range(len(all_part)):
        for j in range(len(all_part[i])):
            for k in range(len(all_part[i][j])):
                if len(all_part[i][j]) >= 1:
                    print(all_part[i][j], end=' ')  
            else:
                print(end=' ')
        print()
    print(f'\nallparts: {all_part}')
string = input('Enter any string:\n') 
all_pallindrom_partitioning(string)      