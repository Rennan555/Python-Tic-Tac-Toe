import tkinter as tk
from tkinter import messagebox as mb
from src.table import Table

class Display:
    def __init__(self, table: Table):
        self.root = tk.Tk()
        self.root.title('Tic Tac Toe')
        
        self.table = table
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        # Buttons grid
        for row in range(3):
            for col in range(3):
                btn = tk.Button(
                    self.root,
                    text='',
                    width=10,
                    height=4,
                    command=lambda r=row, c=col: self.on_button_click(r, c)
                )
                self.buttons[row][col] = btn
                btn.grid(row=row, column=col, padx=5, pady=5)

        # Current player label 
        self.lbl = tk.Label(self.root, text=f'Player turn: {self.table.CURRENT_PLAYER}')
        self.lbl.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        self.root.mainloop()
        
    def on_button_click(self, row, col):
        self.table.play(row, col)
        self.lbl.config(text=f'Player turn: {self.table.CURRENT_PLAYER}')
        self.buttons[row][col].config(text=self.table.spaces[row][col])
        temp = self.table.check_victory_condition()
        print('table: ', self.table)
        print(f'victory condition: {temp}')
        print('playable condition: ', self.table.check_playable_condition())
        if temp is not None:
            mb.showinfo(title='Game Over', message=f'{temp}')
            self.root.destroy()
        self.root.update()

# Test cases
if __name__ == '__main__':
    table = Table()
    Display(table)
