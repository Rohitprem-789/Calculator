import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="#171616")

expression = ""

def press(num):
    global expression
    expression += str(num)
    label_result.config(text=expression)

def clear():
    global expression
    expression = ""
    label_result.config(text="")

def equal():
    global expression
    try:
        result = str(eval(expression))
        label_result.config(text=result)
        expression = result
    except:
        label_result.config(text="Error")
        expression = ""

label_result = tk.Label(root, width=25, height=2, text="", font=("arial", 30))
label_result.pack()

# Row 1
tk.Button(root, text="C", command=clear, width=5, height=1, font=("arial",30,"bold"), fg="#fff", bg="#3697f5").place(x=10,y=100)
tk.Button(root, text="/", command=lambda: press("/"), width=5, height=1, font=("arial",30,"bold"), fg="#fff", bg="#2a2d36").place(x=150,y=100)
tk.Button(root, text="%", command=lambda: press("%"), width=5, height=1, font=("arial",30,"bold"), fg="#fff", bg="#2a2d36").place(x=290,y=100)
tk.Button(root, text="*", command=lambda: press("*"), width=5, height=1, font=("arial",30,"bold"), fg="#fff", bg="#2a2d36").place(x=430,y=100)

# Row 2
tk.Button(root, text="7", command=lambda: press("7"), width=5, height=1, font=("arial",30,"bold"), fg="#fff", bg="#3697f5").place(x=10,y=200)
tk.Button(root, text="8", command=lambda: press("8"), width=5, height=1, font=("arial",30,"bold"), fg="#fff", bg="#2a2d36").place(x=150,y=200)
tk.Button(root, text="9", command=lambda: press("9"), width=5, height=1, font=("arial",30,"bold"), fg="#fff", bg="#2a2d36").place(x=290,y=200)
tk.Button(root, text="-", command=lambda: press("-"), width=5, height=1, font=("arial",30,"bold"), fg="#fff", bg="#2a2d36").place(x=430,y=200)

# Row 3
tk.Button(root, text="6", command=lambda: press("6"), width=5, height=1, font=("arial",30,"bold"), fg="#fff", bg="#3697f5").place(x=10,y=300)
tk.Button(root, text="5", command=lambda: press("5"), width=5, height=1, font=("arial",30,"bold"), fg="#fff", bg="#2a2d36").place(x=150,y=300)
tk.Button(root, text="4", command=lambda: press("4"), width=5, height=1, font=("arial",30,"bold"), fg="#fff", bg="#2a2d36").place(x=290,y=300)
tk.Button(root, text="+", command=lambda: press("+"), width=5, height=1, font=("arial",30,"bold"), fg="#fff", bg="#2a2d36").place(x=430,y=300)

# Row 4
tk.Button(root, text="3", command=lambda: press("3"), width=5, height=1, font=("arial",30,"bold"), fg="#fff", bg="#3697f5").place(x=10,y=400)
tk.Button(root, text="2", command=lambda: press("2"), width=5, height=1, font=("arial",30,"bold"), fg="#fff", bg="#2a2d36").place(x=150,y=400)
tk.Button(root, text="1", command=lambda: press("1"), width=5, height=1, font=("arial",30,"bold"), fg="#fff", bg="#2a2d36").place(x=290,y=400)
tk.Button(root, text="=", command=equal, width=5, height=1, font=("arial",30,"bold"), fg="#fff", bg="#f54242").place(x=430,y=400)

# Row 5
tk.Button(root, text="0", command=lambda: press("0"), width=11, height=1, font=("arial",30,"bold"), fg="#fff", bg="#2a2d36").place(x=10,y=500)

root.mainloop()
