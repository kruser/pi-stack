import time
from sense_hat import SenseHat

BLOCK_COLOR = (116, 248, 252)
BG_COLOR = (5, 41, 61)

GRID_SIZE = 8

INITIAL_SPEED = 0.1 # ms

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

    def stop(self, event):
        if event.action != 'pressed':
            return

        print('stop button pressed')

        self.current_speed = self.current_speed * 0.90
        self.active_row = self.active_row + 1

        if self.active_row < 3:
            self.bar_width = 3
        elif self.active_row < 8:
            self.bar_width = 2
        else:
            self.bar_width = 1

    def play(self):
        '''
        Play a new game
        '''
        direction = 1
        offset = -2
        while self.active:
            self.draw_line(self.active_row, self.bar_width, offset)
            if offset == GRID_SIZE - 1:
                direction = -1
            elif offset == -2:
                direction = 1
            offset = offset + direction
            time.sleep(self.current_speed)

    def __init__(self):
        self.sense = SenseHat()
        self.sense.stick.direction_middle = self.stop
        self.sense.set_rotation(180)
        self.active_row = 0
        self.bar_width = 3
        self.active = True
        self.current_speed = INITIAL_SPEED
        # reset the board
        board = [BG_COLOR for x in range(GRID_SIZE * GRID_SIZE)]
        self.sense.set_pixels(board)

def main():
    Stack().play()

if __name__ == '__main__':
    main()
