"""
This file for LinkedList practice reasonses.

ToDo list:
    - make linked list [].
    - add functions to get position of an element, insert new element, and delete elements [].
"""


from inspect import currentframe


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
            
    # def get_position(self, value):
    #     current = self.head
    #     if self.head:
            
    #         if current.value == value:
    #             return f'current value {current.value}, value is{value}'
            
    #         while current.value != value:
    #             if current.value == value:
    #                 return f'current value {current.value}, value is{value}'
                
    #             elif current.next.value == value:
    #                 return f'current value {current.value}, value is{value}'
                
    #             elif current.next == None:
    #                 break
                
    #             else:
    #                 current = current.next
    
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
                
                
                
          
        

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print (ll.head.next.next.value)
# Should also print 3
print (ll.get_position(3))

# Test insert
ll.insert(e4,3)
# Should print 4 now
print (ll.get_position(3))

# Test delete
ll.delete(1)
# Should print 2 now
print (ll.get_position(1))
# Should print 4 now
print (ll.get_position(2))
# Should print 3 now
print (ll.get_position(3))
        
        
        