import tkinter as tk
from tkinter import ttk


def main():
    root_window = tk.Tk()
    root_window.title = "Input Form"

    base_frame = ttk.Frame(root_window)
    base_frame.pack()

    input_label = tk.Label(
        base_frame,
        text="Hello, Tkinter",
        foreground="white",  # Set the text color to white
        background="black"  # Set the background color to black
    )
    input_label.pack()

    # standard_button = ttk.Button(base_frame)
    # standard_button["text"] = 'Get input'
    # standard_button["command"] = (lambda: get_input_value())
    # standard_button.pack()

    root_window.mainloop()


def get_input_value():
    print("You clicked button")


# ----------------------
# Calls  main  function.
# ----------------------
main()

