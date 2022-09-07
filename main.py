import tkinter as tk

# Create a Tkinter object
window = tk.Tk()
window.title("Disappearing Text Writing App")
window.minsize(500, 500)
counter = 0


# method to clear text from screen
def disappear_text():
    textbox.delete(1.0, tk.END)
    textbox.insert(tk.END, "")


# method containing condition to call the disappear function
def check_disappear():
    global counter, text
    if text == textbox.get(1.0, tk.END):
        if counter == 10:
            window.after(1000, disappear_text)
            counter = -1
        window.after(1000, check_disappear)
        counter += 1
    else:
        window.after(1000, check_disappear)
        text = textbox.get(1.0, tk.END)
        counter = 0


# Application UI
title = tk.Label(window, text="Welcome to the Disappearing Text Writing App.")
title.grid(row=0, column=1)

text = ""
textbox = tk.Text(height=40, width=100, yscrollcommand=True)
textbox.focus()
textbox.grid(row=3, column=1, padx=10, pady=10)

window.after(1000, check_disappear)
window.mainloop()
