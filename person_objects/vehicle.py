"""
Vehicle Object

Determines car position and probable destination

"""
from dependencies import *

class Vehicle():
    def __init__(self):
        self.id = uuid.uuid4()

    def __str__(self):
        return self.id

    def __repr__(self):
        return str(self.id)[:5]
