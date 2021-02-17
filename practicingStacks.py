class Stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)
        #return self.list

    def pop(self):
        if self.is_empty():
            self.list.remove(self.list[-1])
        #return self.list


    def top(self):
        return self.list[-1]


    def is_empty(self):
        return not self.list

item = ['h', 'e', 'y']
s = Stack()
a = s.push(item)
b = s.pop()
#c = s.top()
print(s.push(item))
print(a, b)
