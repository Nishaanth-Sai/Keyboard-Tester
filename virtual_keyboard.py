# Class for creating the keyboard 

import tkinter as tk

class VirtualKeyboard:
    def __init__(self):
        self.root = tk.Toplevel()  # Created as a new window
        self.root.title("Virtual Keyboard")

        
        self.root.geometry("500x250")
        self.root.resizable(True, True)  # You can resize the window if needed

        # Defining the keyboard layout
        self.layout = [
            ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace'],
            ['Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
            ['Caps Lock', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'Enter'],
            ['Shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'Shift'],
            ['Ctrl', 'Win', 'Alt', 'Space', 'Alt', 'Win', 'Menu', 'Ctrl']
        ]

        
        row_index = 0
        for row in self.layout:
            row_frame = tk.Frame(self.root)
            row_frame.grid(row=row_index, column=0, sticky="w")

            col_index = 0
            for key in row:
                # Determining button width based on key
                width = 3
                if key in ['Backspace', 'Enter', 'Shift', 'Caps Lock']:
                    width = 7
                elif key == 'Space':
                    width = 15
                elif key in ['Tab', 'Ctrl', 'Alt', 'Win']:
                    width = 5

                
                btn = tk.Button(row_frame, text=key, width=width, height=2, relief='raised', bg='white')
                btn.grid(row=0, column=col_index, padx=1, pady=1)
                col_index += 1

            row_index += 1

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # This will hide the main root window
    keyboard = VirtualKeyboard()
    keyboard.run()
