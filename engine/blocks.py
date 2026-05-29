from engine.block import Block
from engine.position import Position
#class for the diffrent blocks
class LBlock(Block):
    def __init__(self):
        #id = colour
        super().__init__(id = 1) #goes to block att tells the id aka the color its 1 aka green
        # 3x3 grid where the postions of the cells that make up the shape
        # in in diffrent rotations states
        self.cells = {
            0:[Position(0,2),Position(1,0),Position(1,1),Position(1,2)],
            1:[Position(0,1),Position(1,1),Position(2,1),Position(2,2)],
            2:[Position(1,0),Position(1,1),Position(1,2),Position(2,0)],
            3:[Position(0,0),Position(0,1),Position(1,1),Position(2,1)],
        }
        self.move(0,3)

class JBlock(Block):
    def __init__(self):
        super().__init__(id = 2)
        # 3x3 grid where the postions of the cells that make up the shape
        # in in diffrent rotations states
        self.cells = {
            0:[Position(0,0),Position(1,0),Position(1,1),Position(1,2)],
            1:[Position(0,1),Position(0,2),Position(1,1),Position(2,1)],
            2:[Position(1,0),Position(1,1),Position(1,2),Position(2,2)],
            3:[Position(0,1),Position(1,1),Position(2,0),Position(2,1)],
        }
        self.move(0,3)

class IBlock(Block):
    def __init__(self):
        super().__init__(id = 3)
        # 3x3 grid where the postions of the cells that make up the shape
        # in in diffrent rotations states
        self.cells = {
            0:[Position(1,0),Position(1,1),Position(1,2),Position(1,3)],
            1:[Position(0,2),Position(1,2),Position(2,2),Position(3,2)],
            2:[Position(2,0),Position(2,1),Position(2,2),Position(2,3)],
            3:[Position(0,1),Position(1,1),Position(2,1),Position(3,1)],
        }
        self.move(-1,3)
    
class OBlock(Block):
    def __init__(self):
        super().__init__(id = 4)
        # 3x3 grid where the postions of the cells that make up the shape
        # in in diffrent rotations states
        self.cells = {
            0:[Position(0,0),Position(0,1),Position(1,0),Position(1,1)]
        }
        self.move(0,4)

class SBlock(Block):
    def __init__(self):
        super().__init__(id = 5)
        # 3x3 grid where the postions of the cells that make up the shape
        # in in diffrent rotations states
        self.cells = {
            0:[Position(0,1),Position(0,2),Position(1,0),Position(1,1)],
            1:[Position(0,1),Position(1,1),Position(1,2),Position(2,2)],
            2:[Position(1,1),Position(1,2),Position(2,0),Position(2,1)],
            3:[Position(0,0),Position(1,0),Position(1,1),Position(2,1)],
        }
        self.move(0,3)

class TBlock(Block):
    def __init__(self):
        super().__init__(id = 6)
        # 3x3 grid where the postions of the cells that make up the shape
        # in in diffrent rotations states
        self.cells = {
            0:[Position(0,1),Position(1,0),Position(1,1),Position(1,2)],
            1:[Position(0,1),Position(1,1),Position(1,2),Position(2,1)],
            2:[Position(1,0),Position(1,1),Position(1,2),Position(2,1)],
            3:[Position(0,1),Position(1,0),Position(1,1),Position(2,1)],
        }
        self.move(0,3)
    
class ZBlock(Block):
    def __init__(self):
        super().__init__(id = 7)
        # 3x3 grid where the postions of the cells that make up the shape
        # in in diffrent rotations states
        self.cells = {
            0:[Position(0,0),Position(0,1),Position(1,1),Position(1,2)],
            1:[Position(0,2),Position(1,1),Position(1,2),Position(2,1)],
            2:[Position(1,0),Position(1,1),Position(2,1),Position(2,2)],
            3:[Position(0,1),Position(1,0),Position(1,1),Position(2,0)],
        }
        self.move(0,3)