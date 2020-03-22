import time
from sense_hat import SenseHat

BLOCK_COLOR = (116, 248, 252)
BG_COLOR = (5, 41, 61)

GRID_SIZE = 8

class Stack():

    def draw_line(self, row, width, offset = 0):
        pixels = [BG_COLOR for column in range(GRID_SIZE)]
        for column in range(width):
            column_index = offset + column
            if column_index < 0 or column_index >= GRID_SIZE:
                continue
            pixels[column_index] = BLOCK_COLOR

        for column, pixel in enumerate(pixels):
            self.sense.set_pixel(row, column, pixel)

    def play(self):
        '''
        Play a new game
        '''
        direction = 1
        offset = -2
        while self.active:
            self.draw_line(0, 3, offset)
            if offset == GRID_SIZE - 1:
                direction = -1
            elif offset == -2:
                direction = 1
            offset = offset + direction
            time.sleep(0.2)

    def __init__(self):
        self.sense = SenseHat()
        self.sense.set_rotation(180)
        self.active_row = 0
        self.active = True
        # reset the board
        board = [BG_COLOR for x in range(GRID_SIZE * GRID_SIZE)]
        self.sense.set_pixels(board)

def main():
    Stack().play()

if __name__ == '__main__':
    main()
