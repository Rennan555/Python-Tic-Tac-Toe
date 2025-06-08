import tkinter as tk
from table import Table

class Display:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Grid 3x3 de Botões')

        for row in range(3):
            for col in range(3):
                btn = tk.Button(
                    self.root,
                    text='',
                    width=10,
                    height=4,
                    command=lambda r=row, c=col: self.on_button_click(r, c)
                )
                btn.grid(row=row, column=col, padx=5, pady=5)

        self.root.mainloop()
        
    def on_button_click(self, row, col):
        print(row, col)

# Test cases
if __name__ == '__main__':
    Display()
