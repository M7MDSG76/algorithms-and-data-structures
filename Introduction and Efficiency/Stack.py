"""
This file for Stack list
To-Do List:
    - create stack class [Done].
    - give it a push function [Done].
    - give it a pop function [Done].
"""

class Element():
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList():
    def __init__(self, head=None):
        self.head = head
         
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        current = self.head
        step = 1
        
        if current:
            while step <= position:
                if step == position:
                    return current.value
                elif current.next:
                    current = current.next 
                elif current.next is None:
                    return None
                
                step += 1
                    
        else:
            return None
    
    def get_length(self):
        length = 0
        current = self.head
        
        while current:
            if current.next:
                current = current.next
                length += 1
            elif current.next == None:
                length += 1
                return length
    
    def print_out(self):
        if self.head:
            current = self.head
            print('Nodes:\n', end=' ')
            while current:
                print(current.value, end=', ')
                current = current.next
            print('\n')
            return
        else:
            print('The List is empty.')
    
    def insert(self, element, position):
        current = self.head
        step = 1
        pos = position -1 
        
        if self.head:
             while step <= position:  
                
                if step == pos:
                    element.next = current.next
                    current.next = element
                    break
                
                elif current.next:
                    current = current.next 
                    
                elif current.next is None:
                    return f'the position is not found'
                
                step += 1
                    
        else:
            return 'There is no elements in this linked list!'
                    
    def delete(self, value):
        """
        Delete the first node with the given value.
        """
        def target_is_head_and_next(current):
            if step == 0 and current.value == value and current.next:
                return True
            else: 
                return False
        
        def target_is_head_and_no_next(current):
            if step == 0 and current.value == value:
                return True
            else: 
                return False
        
        def target_is_next(current):
            if current.next and current.next.value == value:
                return True
            else:
                return False
        
        def target_is_last_node(self, step, current, value):
            len = self.get_length()
            if step == len and current.value == value:
                return True
            else:
                return False
            
            
        current = self.head
        step = 0
        
        while current:
            print(f'[0]passed!!!')
            if target_is_head_and_next(current):
                print(f'[1]passed!!!')
                
                self.head = current.next
                current = None
                break
            
            elif target_is_head_and_no_next(current):
                print(f'[2]passed!!!')
                
                self.head = None
                break
            
            elif target_is_next(current):
                print(f'[3]passed!!!')
                current.next = current.next.next
                print(f'\n\ncurrent is:{current.value}')
                break
            
            elif target_is_last_node(self, step, current, value):
                print(f'[4]passed!!!')
                current = None
                break
            
            # if node is not target move to next node.
            else:
                print(f'[5]passed!!!')
                current = current.next
                step += 1 
              
    def insert_first(self, new_element):
        """
        Insert new element to the begining of the list.  
        """
        current = self.head
        if self.head:
            new_element.next = current
            self.head = new_element
            return self.head
        
        else:
            self.head = new_element
            
               
    def delete_first(self):
        if self.head:
            try:
                deleted = self.head
                self.head = deleted.next
                return deleted
            except:
                return None
                
                
            
            

class Stack():
    def __init__(self, top = None):
        self.__ll = LinkedList(top)
            
    def push(self, new_element):
        
        return self.__ll.insert_first(new_element)
        
    def pop(self):
    
        return self.__ll.delete_first()
        
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print (stack.pop().value)
print (stack.pop().value)
print (stack.pop().value)
print (stack.pop())
stack.push(e4)
print (stack.pop().value)