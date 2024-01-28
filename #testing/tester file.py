import tkinter as tk
import time

def print_vapo(text_widget):
    for _ in range(10):
        text_widget.insert(tk.END, "\tVAPO🙅 VAPO🙅\n")
        text_widget.see(tk.END)  # Scroll to the end
        text_widget.update()
        time.sleep(0.5)  # Adjust the delay as needed

def on_yes_button_click(text_widget):
    print_vapo(text_widget)

def on_no_button_click(text_widget):
    text_widget.insert(tk.END, "\tTipo assimmmmm!\n")
    text_widget.see(tk.END)  # Scroll to the end
    text_widget.update()

def main():
    # Create the main window
    window = tk.Tk()
    window.title("Is malu drunky?")
    window.geometry("400x300")  # Set the window size

    # Set background color
    window.configure(bg='#880808')

    # Display the message
    label = tk.Label(window, text="Is malu drunky?", font=('Arial', 16), bg='#880808', fg='#ffffff')
    label.pack(pady=10)

    # Create a Text widget with a white background
    text_widget = tk.Text(window, height=8, width=30, bg='#ffffff', font=('Arial', 12))
    text_widget.pack(pady=10)

    # Create a frame to center the buttons
    button_frame = tk.Frame(window, bg='#880808')
    button_frame.pack()

    # Style for the buttons
    button_style = {'bg': '#4caf50', 'fg': '#ffffff', 'font': ('Arial', 12), 'bd': 0, 'relief': tk.FLAT}

    # Create Yes button with rounded corners
    yes_button = tk.Button(button_frame, text="Yesssss!", command=lambda: on_yes_button_click(text_widget), **button_style)
    yes_button.pack(side=tk.LEFT, padx=10)

    # Create No button with rounded corners
    no_button = tk.Button(button_frame, text="NO!", command=lambda: on_no_button_click(text_widget), **button_style)
    no_button.pack(side=tk.RIGHT, padx=10)

    # Start the main loop
    window.mainloop()

if __name__ == "__main__":
    main()
