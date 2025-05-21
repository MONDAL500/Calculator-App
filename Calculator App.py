import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("Colorful Calculator")
root.geometry("400x500")
root.config(bg="#212121")  # Dark background for the main window-------------------------

# Define fonts and colors
button_font = font.Font(family="Helvetica", size=18, weight="bold")
display_font = font.Font(family="Helvetica", size=24)
button_bg_color = "#424242"  # Soft gray for regular buttons
button_text_color = "#FFFFFF"  # White for text on buttons
button_hover_color = "#666666"  # Button hover color
accent_button_bg = "#FF4081"  # Pink accent color for "=" and "C" buttons
operator_button_bg = "#00E5FF"  # Cyan for operator buttons
number_button_bg = "#76FF03"  # Green for number buttons
display_bg_color = "#263238"  # Darker gray for display background
display_text_color = "#FFFFFF"  # White text color for display

# Display frame for showing numbers and results--------------------------------------------------------
display_frame = tk.Frame(root, bg=display_bg_color)
display_frame.pack(expand=True, fill="both")

display_text = tk.StringVar()
display_label = tk.Label(display_frame, textvariable=display_text, font=display_font, bg=display_bg_color, fg=display_text_color, anchor="e", padx=10)
display_label.pack(expand=True, fill="both")

# Calculator logic-------------------------------------------------------------------------------------
expression = ""

def add_to_expression(value):
    global expression
    expression += str(value)
    display_text.set(expression)

def evaluate_expression():
    global expression
    try:
        result = str(eval(expression))
        display_text.set(result)
        expression = result
    except Exception as e:
        display_text.set("Error")
        expression = ""

def clear_expression():
    global expression
    expression = ""
    display_text.set("")

# Button frame for calculator buttons
button_frame = tk.Frame(root, bg="#212121")
button_frame.pack(expand=True, fill="both")

# Buttons layout-----------------------------------------------------------------------------------------------
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Add buttons to frame---------------------------------------------------------------------------------------------------
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(button_frame, text=text, font=button_font, bg=accent_button_bg, fg=button_text_color,
                           command=evaluate_expression)
    elif text == 'C':
        button = tk.Button(button_frame, text=text, font=button_font, bg=accent_button_bg, fg=button_text_color,
                           command=clear_expression)
    elif text in ('/', '*', '-', '+'):
        button = tk.Button(button_frame, text=text, font=button_font, bg=operator_button_bg, fg=button_text_color,
                           command=lambda value=text: add_to_expression(value))
    else:
        button = tk.Button(button_frame, text=text, font=button_font, bg=number_button_bg, fg=button_text_color,
                           command=lambda value=text: add_to_expression(value))
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Configure grid weights for resizing-----------------------------------------------------------------------
for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)

# Add hover effect for buttons---------------------------------------------------------------------------------
def on_enter(event):
    event.widget.config(bg=button_hover_color)

def on_leave(event):
    if event.widget.cget("text") in ('C', '=', '+', '-', '*', '/'):
        event.widget.config(bg=accent_button_bg)
    elif event.widget.cget("text") in ('/', '*', '-', '+'):
        event.widget.config(bg=operator_button_bg)
    else:
        event.widget.config(bg=number_button_bg)

# Bind hover effects to all buttons--------------------------------------------------------------------------------
for button in button_frame.winfo_children():
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

root.mainloop()
