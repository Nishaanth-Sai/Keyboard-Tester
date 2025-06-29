# Keyboard-Tester

A Python-based virtual keyboard testing tool that allows users to verify the functionality of their physical keyboard in real-time.
Features: 
   - Real-Time Key Detection: Press a key on your physical keyboard, and see it light up on the on-screen virtual keyboard.
   - Graphical Interface: Built using Tkinter, providing a user-friendly visual layout of a full QWERTY keyboard.
   - Modular Design: Code is organized across multiple files with clean, reusable functions for maintainability and scalability.
   - Event Logging (via logged_mvp2.py): Captures and records key events for tracking or debugging purposes.


Technologies Used:
  - Python 3
  - Tkinter (GUI)
  - pynput (keyboard input capture)
  - Modular architecture for separation of logic and UI

How It Works: 
    1. Launch the main script.
    2. A virtual keyboard GUI appears.
    3. Press any key on your physical keyboard.
    4. The corresponding virtual key is highlighted.
    5. Optionally, key events can be logged for analysis.

File Overview:
    - keyboard_tester.py: Main script to initialize and run the application.
    - virtual_keyboard.py: Handles the drawing and layout of the on-screen keyboard.
    - logged_mvp2.py: Optional module to log key press events.
