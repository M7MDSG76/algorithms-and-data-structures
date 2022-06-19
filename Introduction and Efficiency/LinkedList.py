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
        step = 0
        
        if current:
            while step <= position:
                if step == position:
                    return current.value
                elif current.next:
                    current = current.next 
                elif current.next is None:
                    return f'the position is not found'
                
                step += 1
                    
        else:
            return 'There is no elements in this linked list!'
    
    def           
                
            
      
      
            
e1 = Element(1)
e2 = Element(2)
e3 = Element(42)
e4 = Element(22)

ll = LinkedList()

ll.append(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)

print(ll.get_position(3))

            
        
        
        