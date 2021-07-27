from nodes1 import Node
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def enqueue(self,data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail =self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
        self.count +=1
    def dequeue(self):
        current = self.head
        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.prev = None
            self.count -=1
                
from random import randint           
            
class Track:
    def __init__(self, title=None):
        self.title = title
        self.length = randint(5, 10)
        
        

import time

class MediaPlayerQueue(Queue):
    def __init__(self):
        super(MediaPlayerQueue, self).__init__()
    def add_track(self, track):
        self.enqueue(track)
    def add_track(self, track):
        self.enqueue(track)
    def play(self):        
        while self.count > 0:
            current_track_node = self.dequeue()
            print("Now playing {}".format(current_track_node.data.title))
            time.sleep(current_track_node.data.length)            