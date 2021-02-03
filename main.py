import tkinter as tk
from soduku import Solve, toHex

# better tkinter entry with max length and digit input mask
class NewEntry(tk.Entry):
    def __init__(self, master=None, max_len=5, **kwargs):
        self.var = tk.StringVar()
        self.max_len = max_len
        tk.Entry.__init__(self, master, textvariable=self.var,width=3, font=("default", 35), justify='center', **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)

    def check(self, *args):
        if len(self.get()) > self.max_len or self.get() not in [str(i) for i in range(0,10)]:
            self.var.set('') # reject change

# get the board from the entry list
def getBoard(entries):
    board = []
    for box in entries:
        if box.get() == '':
            board.append(0)
        else:
            board.append(box.get())
    return board

# clear all the entries text (changes them to '')
def clear(entries):
    for box in entries:
        box.insert(0,' ')
        box.config(fg=toHex((0,0,0)))

# solves the board and changes all the entries accordingly
def solveBoard(entries, window):
    board = Solve(board=getBoard(entries))
    for idx,box in enumerate(entries):
        if box.get() == '':
            box.insert(0,str(board[idx]))
            box.config(fg=toHex((60,116,183)))

  
#initialize the screen
window = tk.Tk()
window.title("Almog's Soduku Solver")
window.geometry('740x750')


#generate the board (entries)
TextBoxes = []
for row in range(9):
    for column in range(9):
        entry = NewEntry(window, max_len=1)
        entry.grid(column=column, row=row, ipady=10)
        TextBoxes.append(entry)
    
# initialize the solve button
solveBtn = tk.Button(window, text="Solve Board", command= lambda: solveBoard(entries=TextBoxes,window=window), height=3)
solveBtn.grid(column=4, row=9)

# initialize the clear button
clearBtn = tk.Button(window, text="Clear Board", command= lambda: clear(TextBoxes), height=3)
clearBtn.grid(column=5, row=9)

# tkinter window loop
window.mainloop()