import tkinter as tk
from tkinter import Label, Entry, Button, messagebox

def calculate_grade():
    try:
        ac = float(ac_entry.get())
        mt = float(mt_entry.get())
        final_grade = (ac * 0.1 + mt * 0.9) * 0.2
        result_label.config(text=f"Your Final Grade is: {final_grade:.1f}", fg="green", font=("Helvetica", 12, "bold"))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")

# Create the main window
window = tk.Tk()
window.title("Grade Calculator")
window.geometry("300x200")  # Set a fixed window size

# Create and place widgets with improved styling and centering
ac_label = Label(window, text="AC Grade:", anchor="e")
ac_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

ac_entry = Entry(window)
ac_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")

mt_label = Label(window, text="MT Grade:", anchor="e")
mt_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

mt_entry = Entry(window)
mt_entry.grid(row=1, column=1, padx=10, pady=10, sticky="e")

calculate_button = Button(window, text="Calculate", command=calculate_grade, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"))
calculate_button.grid(row=2, column=0, columnspan=2, pady=10, sticky="nsew")

result_label = Label(window, text="", font=("Helvetica", 12))
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Configure row and column weights to make the button expand
window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# Start the main event loop
window.mainloop()
