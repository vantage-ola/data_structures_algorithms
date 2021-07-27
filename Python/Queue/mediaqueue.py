from random import randint
import stackqueue
from stackqueue import Queue
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
                