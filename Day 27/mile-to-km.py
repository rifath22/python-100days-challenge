import tkinter

window = tkinter.Tk()
window.title("Mile to KM Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)
# Label
label_1 = tkinter.Label(text="is equal to", font=("Arial", 24, "bold"))
label_1.grid(row=2,column=1)

label_2 = tkinter.Label(text="miles", font=("Arial", 24, "bold"))
label_2.grid(row=1,column=3)

label_3 = tkinter.Label(text="km", font=("Arial", 24, "bold"))
label_3.grid(row=2,column=3)

label_4 = tkinter.Label(text="", font=("Arial", 24, "bold"))
label_4.grid(row=2,column=2)
#Button
def button_clicked():
    print("Button Clicked")
    # my_label["text"] = "Button Clicked"
    miles_in_text = miles.get()
    miles_to_km = round(float(miles_in_text) * 1.6, 2)
    print(f"miles_in_text: {miles_in_text}")
    print(f"miles_to_km: {miles_to_km}")
    label_4.config(text=str(miles_to_km))

button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(row=3,column=2)

#Entry
miles = tkinter.Entry()
miles.grid(row=1,column=2)

# km = tkinter.Entry()
# km.grid(row=2,column=2)

window.mainloop()