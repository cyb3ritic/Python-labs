'''
Your task is to create a Stack class and extend it's behavior in such a way so that the class is able to count all the elements that are pushed and popped.

Follow the hints:
- Introduce a property designed to count push and pop operations and name it in a way which guarantees it is hidden;
- Initialize it to zero inside the constructor;
- Provide a method which returns the value currently assigned to the counter

'''

# Writing the python code

class Stack:
    
    def __init__(self):
        __stk = []
        
    def push(self, value):
        self.__stk.append(value)
        
    def pop(self, value):
        if len(self.__stk) > 0:  
            val = self.__stk[-1]
            del self.__stk[-1]
            return val
        else:
            print("The stack is empty.")
            
            
class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.count_push = 0
        self.count_pop = 0
    
    def count_push(self, val):
        self.Stack.push(val)
        self.count_push += 1
        return self.count_push
    
    def pop(self):
        Stack.pop()
        self.count_pop += 1
        return self.count_pop
    
    
test = Stack()
myStack = CountingStack(test)
for i in range(5):
    total_pushes = myStack.push(i)
print(total_pushes)
    
    

