import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)
# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(row=0,column=0)

#Button
def button_clicked():
    print("Button Clicked")
    # my_label["text"] = "Button Clicked"
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(row=1,column=1)
second_button = tkinter.Button(text="New Button", command=button_clicked)
second_button.grid(row=0,column=2)
#Entry
input = tkinter.Entry()
input.grid(row=2,column=3)

window.mainloop()