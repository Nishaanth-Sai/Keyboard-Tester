# Logged MVP 2 - Ayman Zubair and Nishaanth Sai Vinodh Kumar
# Program description: The second version of Logged.
# 1/10/2025

from keyboard_tester import KeyboardTester
from virtual_keyboard import VirtualKeyboard
import tkinter as tk
import threading

class LoggedMVP:
    def __init__(self):
        self.keyboard_thread = None

    def launch_virtual_keyboard(self):
        root = tk.Tk()
        root.withdraw()  # This hides the main root window
        keyboard = VirtualKeyboard()
        keyboard.run()

    def run(self):
        # Makes another thread so both windows can be open at once
        self.keyboard_thread = threading.Thread(target=self.launch_virtual_keyboard, daemon=True)
        self.keyboard_thread.start()

        # Run the keyboard tester exercises
        tester = KeyboardTester()
        tester.run()

if __name__ == "__main__":
    app = LoggedMVP()
    app.run()
