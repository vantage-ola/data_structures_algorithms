class Queue:
    def __init__(self):
        self.inbound_stack=[]
        self.outbound_stack= []
    def enqueue(self,data):
        self.inbound_stack.append(data)
    def dequeue(self,data):
        if not self.outbound_stack:
            while self.bound_stack:
                self.outbound_stack.append(
                    self.inbound_stack.pop())
        return self.outbound_stack.pop()