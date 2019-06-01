from order import order
import tkinter as tk

window = tk.Tk()
window.title("英语句子打乱工具")
window.geometry("300x170")

inputNotice = tk.Label(window, text="↓ Please Input ↓", font=('Times New Roman', 12))

e = tk.Entry(window, show=None)

text = tk.StringVar()

def ordering():
    t.delete(1.0, tk.END)
    inputText = e.get()
    orderedText = order(inputText)[0]+" ("+order(inputText)[1]+")"
    text.set(orderedText)
    t.insert('insert', text.get())

b = tk.Button(window, text="START", font=('Times New Roman', 12), width=12, height=1, command=ordering)

t = tk.Text(window, height = 5)

inputNotice.pack()  # 显示"↓ Please Input ↓"
e.pack()            # 显示输入框
b.pack()            # 显示按钮
t.pack()            # 显示文本框

window.mainloop()
