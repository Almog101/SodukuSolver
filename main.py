import pygame as pg
from algo import Solve

pg.init()
screen = pg.display.set_mode((800, 870))
COLOR_INACTIVE = pg.Color(79, 79, 79)
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 100)
SOLVE = Solve()

class InputBox:
    def __init__(self, x, y, w, h):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = ''
        self.txt_surface = FONT.render(' ', True, (0,0,0))
        self.active = False

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+25, self.rect.y+10))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)


    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if event.unicode in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        self.text = event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, COLOR_INACTIVE)


class Button:
    def __init__(self, x, y, w, h, text, Boxes):
        self.rect = pg.Rect(x, y, w, h)
        self.color = pg.Color(64, 64, 64)
        self.text = text
        self.txt_surface = FONT.render(self.text, True, self.color)
        self.active = False
        self.boxes = Boxes

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+25, self.rect.y+10))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)

    def clear_board(self):
        for box in self.boxes:
            box.txt_surface = FONT.render('', True, COLOR_INACTIVE)

    def get_board(self):
        board = []
        for box in self.boxes:
            text = box.text
            if text == '' or text == text == ' ' or text == '0':
                board.append('0')
            else:
                board.append(text)
        return board


    def solve_board(self, board):
        board = [int(x) for x in board]
        solved_board = board.copy()

        index = 0
        while index < 81:

            if board[index] == 0:
                digitBeforeChange = solved_board[index]

                for x in range(solved_board[index] + 1, 10):
                    if SOLVE.CheckTile(index, x, solved_board):
                        solved_board[index] = x
                        break

                if solved_board[index] != 0 and digitBeforeChange != solved_board[index]:
                    index += 1

                else:
                    solved_board[index] = 0
                    index -= 1
                    while board[index] != 0:
                        index -= 1
            else:
                index += 1

        return solved_board


    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            if self.active:


                if self.text == 'Clear':
                    self.clear_board()
                    print('clear')

                elif self.text == 'Solve':
                    print('solve')
                    for idx, digit in enumerate(self.solve_board(self.get_board())):
                        box = self.boxes[idx]
                        if box.text == 0 or box.text == "" or box.text == " ":
                            box.txt_surface = FONT.render(str(digit), True, COLOR_ACTIVE)





def main():
    clock = pg.time.Clock()
    pg.display.set_caption('Soduku Solver')

    programIcon = pg.image.load('icon.jpg')
    pg.display.set_icon(programIcon)

    space = 80
    input_boxes = []

    for row in range(9):
        for column in range(9):
            input_boxes.append(InputBox(column*space+40, row*space+40, space, space))


    solve_btn = Button(140, 770, 230, 80, 'Solve', input_boxes)
    clear_btn = Button(440, 770, 230, 80, 'Clear', input_boxes)


    done = False

    while not done:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)
            solve_btn.handle_event(event)
            clear_btn.handle_event(event)

        screen.fill((214, 214, 214))

        for box in input_boxes:
            box.draw(screen)

        solve_btn.draw(screen)
        clear_btn.draw(screen)

        for i in range(1,3):
            pg.draw.rect(screen, (0, 0, 0), [40+ i*3*80, 40, 5, 80*9])
        for i in range(1,3):
            pg.draw.rect(screen, (0, 0, 0), [40, 40+ i*3*80, 80*9, 5])


        pg.display.flip()
        clock.tick(30)



if __name__ == '__main__':
    main()
    pg.quit()