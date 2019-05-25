from order import order
import tkinter as tk

window = tk.Tk()
window.title("英语句子打乱工具")
window.geometry("300x125")

inputNotice = tk.Label(window, text="↓Please Input↓", font=('Arial', 12))
inputNotice.pack()

e = tk.Entry(window, show=None)
e.pack()

text = tk.StringVar()
def ordering():
    inputText = e.get()
    orderedText = order(inputText)[0]
    text.set(orderedText)
    t.insert('insert', text.get())

b = tk.Button(window, text="START", font=('Arial', 12), width=12, height=1, command=ordering)
b.pack()

t = tk.Text(window, height = 2)
t.pack()

window.mainloop()