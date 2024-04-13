import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="left")

#Button
def button_clicked():
    print("Button Clicked")
    # my_label["text"] = "Button Clicked"
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

#Entry
input = tkinter.Entry()
input.pack()

window.mainloop()