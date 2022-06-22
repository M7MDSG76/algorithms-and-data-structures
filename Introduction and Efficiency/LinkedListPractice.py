"""
To-Do List:
    1 - append function [Done].
    2 - get_position functions [Done].
    3 - delete function [Done]. 
    4 - Test all functionalties [Done].
"""


from calendar import isleap
from turtle import pos


class Element():
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def get_length(self):
        """
        Get the length of the linked list by iteration over the list.
        """
        current = self.head
        len = 0
        while current:
            if current.next:
                current = current.next
                len += 1
            elif current.next == None:
                len += 1
                return len
        return len
           
    def append(self, new_element):
        """
        add new_element to the end of the list.\n
        list => |11|22|33|44|\n
        
        Example:\n
        e4 = Element(55)\n
        list.append(e4)\n\n
        list => |11|22|33|44|55|

        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            if current.next == None:
                current.next = new_element
                return 'element appended'
        else:
            self.head = new_element
            return 'element appended as head'
        
    def get_position(self,position):
        """
        Get value of the given position\n
        positions(as an index) => |0|1|2|3| \n
        elements => |11|22|33|44|\n
        
        Example:\n
        get_position(1) # return 22
        """
        current = self.head
        step = 0
        while step <= position:
            if step == position:
                return current.value
            
            elif current.next:
                current = current.next
                step += 1
            else:
                return None
    
    def delete(self, value):
        """
        Delete the first element with the given value.
        
        Linked List => |0|1|2|3|
        
        value = 2
        
        new Linked List after deletion => |0|1|3|
        """
        def is_head_and_next(current):
            """
            Check is True function 
            The element is the head and there is a next element,\n so we have to assign it as head.
            """
            if current == self.head and current.next and current.value == value:
                return True
            else:
                False

        
        def is_head_no_next(current):
            """
            Check is True function
            The element is the head and there is no other elements in the list.
            """
            if current == self.head and current.next == None and current.value == value:
                return True
            else:
                return False

        
        def is_next(current):
            """
            Check is True function
            The element is in the meddile of the list, means that there is an element before and after.
            """

            if current.next and current.next.value == value:
                return True
            else:
                False

            
        def is_last(step, current):
            """
            Check is True function
            The element is the last element in the list
            """
            len = self.get_length()
            if current != self.head and current.next == None and step == len-1 and value == current.value:
                return True
            else:
                return False

                    
        current = self.head
        step = 0
        len = self.get_length()
        
        while current and step <= len:

            if is_head_no_next(current):
                self.head = None   
                current = None
                print(f'1 - Element No{step} deleted')
                break 
            
            elif is_head_and_next(current):
                
                self.head = current.next
                current = None
                
                print(f'2 - Element No{step} deleted')
                break 
            
            elif is_next(current):
                current.next = current.next.next
                
                print(f'3 - Element No{step} deleted')
                break 
            
            elif is_last(step, current):
    
                current = None
                print(f'4 - Element No{step} deleted')
                break 
            else:
    
                current = current.next
                step += 1
        print('element does not exist')
        return False
                
    def print_out(self):
        if self.head:
            current = self.head
            print('Nodes:\n', end=' ')
            while current:
                print(current.value, end=', ')
                current = current.next
            print('\n')
            return             
        


    
    
    
e1 = Element(1)
e2 = Element(2)
e3 = Element(33)

ll = LinkedList()

ll.append(e1)
ll.append(e2)
ll.append(e3)


ll.print_out()

ll.delete(2)

ll.print_out()
    



    
        