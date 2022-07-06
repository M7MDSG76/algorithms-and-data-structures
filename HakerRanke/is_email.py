
from typing import List



def is_sympol( index, char):
    sympols = ['!','@','#','$','%','^','&',
            '*','(',')','-','=','+',',','.',
            '/','`','~','[',']','{','}','\\',
            '|','?','/','<','>',':',';']
    if index == 0 and char in sympols:
        return True
    else:
        return False
    
    
def is_number(index, char):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    if index == 0 and char in numbers:
        return True
    else:
        return False
    
def is_email(email: str):
    """
    the email should contain atleast three parts:
    1- username:
        - doesn't start with with number or sympols.
        - string length is longer than 1 char.
        - can contain ("-_.")

    2- domain name:
        - start with '@'.
        - after '@' sympol one char atleast.
        
    
    3- top-level domain:
    """
    username = ''
    domain_name = ''
    top_level_domain = ''
    index_of_at = 0
    
    # split the entered email
    for i,char in enumerate(email):
        
        if is_sympol(i, char) or is_number(i, char):
            # email can't start with number or sympols.
            if char == '@':
                return 'write the username'
            return f'email shouldn\'t start with numbers or sympols!\n{char}'
         
        if char == '@':
            index_of_at = i
            username = str(email[:i])
        elif char == '.' and '.' not in email[i+1:]:
            if email[index_of_at+1:i]:
                domain_name = email[index_of_at+1:i]
            top_level_domain = email[i+1:]
            
    # check for the lengths
    if len(username) < 1:
        return 'there is no username'
    if len(domain_name) < 1:
        return 'write the domain name'
    if len(top_level_domain) < 2:
        return 'T-L domain should be longer than 1 char'
        
    print(f'Username: {username},\ndomain name: {domain_name},\ntop level domain: {top_level_domain}')


is_email('m7@example.com')