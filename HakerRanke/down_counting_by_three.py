from typing import List

def countdown(num: int) -> List[int]:
    
    counting_num = num
    list = []
    
    if num<=3:
        list.append(0)
        return list
    else:
        while counting_num > 3:
            counting_num -= 3
            if (counting_num % 2) == 0:
                list.append(counting_num)
            
        
        list.sort()   
        return list
    
