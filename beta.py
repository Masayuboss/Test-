import tkinter as t

def show_output():
    number= int(number_input.get())

    output=""
    for i in range (21):
        output += str(number) + " * " + str(i)
        output += " = " + str(number ** i ) + "\n"

    output_label.configure(text=output)

window = t.Tk()
window.title("Beta")
window.minsize(width=400, height=400)

title_label = t.Label(master=window, text="ยกกำลัง")
title_label.pack()

number_input =t.Entry(master=window)
number_input.pack()

ok_button = t.Button(
    master=window,text="ได้แก่",
    command=show_output
)
ok_button.pack()

output_label= t.Label(master=window)
output_label.pack()


window.mainloop()
