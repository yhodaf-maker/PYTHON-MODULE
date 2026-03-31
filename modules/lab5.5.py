import tkinter as tk

# יצירת חלון
root = tk.Tk()

# כותרת החלון
root.title("My First GUI")

# גודל החלון
root.geometry("300x200")

# תווית ראשית
label = tk.Label(root, text="Hello Yehuda 👋", font=("Arial", 16))
label.pack(pady=10)

# תווית בפינה ימנית למעלה
upper_right = tk.Label(root, text="Upper Right")
upper_right.pack(anchor="ne")

# שדה קלט   
entry = tk.Entry(root)
entry.pack()

# פונקציה לכפתור
def clicked():
   text = entry.get()
   label.config(text=f"hello {text}!")
   print("clicked")

# כפתור
button = tk.Button(root, text="Click me",bg="lightblue", command=clicked)
button.pack()

# הפעלת החלון
root.mainloop()