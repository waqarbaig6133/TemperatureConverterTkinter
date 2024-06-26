import tkinter as tk

root = tk.Tk()
root.geometry("400x400")  
root.resizable(False, False)
white_frame = tk.Frame(root, bd=0, highlightthickness=0, background="white")
blue_frame = tk.Frame(root, bd=0, highlightthickness=0, background="blue")

white_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1.0)
blue_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1.0)

def update_label(*args):
    try:
        value = entry_var.get()
        if value == '':
            value = '0'
        value2 = float(value)
        print(value2)
        if choices1.get() == 'Celcius':
            if value2 >= 100.0:
                blue_frame.config(background='red')
                label.config(background='red')
                title2.config(background='red')
                lis2.config(background='red')
            else:
                blue_frame.config(background='blue')
                label.config(background='blue')
                title2.config(background='blue')
                lis2.config(background='blue')
        elif choices1.get() == 'Fahrenheit':
            if value2 >= 212.0:
                blue_frame.config(background='red')
                label.config(background='red')
                title2.config(background='red')
                lis2.config(background='red')
            else:
                blue_frame.config(background='blue')
                label.config(background='blue')
                title2.config(background='blue')
                lis2.config(background='blue')
        elif choices1.get() == 'Kelvin':
            if value2 >= 373.15:
                blue_frame.config(background='red')
                label.config(background='red')
                title2.config(background='red')
                lis2.config(background='red')
            else:
                blue_frame.config(background='blue')
                label.config(background='blue')
                title2.config(background='blue')
                lis2.config(background='blue')

        if choices1.get() == 'Fahrenheit' and choices2.get() == 'Celcius':
            label_var.set(str((value2 - 32) * (5/9)))
        elif choices1.get() == 'Celcius' and choices2.get() == 'Fahrenheit':
            label_var.set(str((value2 * (9/5)) + 32))
        elif choices1.get() == 'Kelvin' and choices2.get() == 'Celcius':
            label_var.set(str(value2 - 273.15))
        elif choices1.get() == 'Celcius' and choices2.get() == 'Kelvin':
            label_var.set(str(value2 + 273.15))
        elif choices1.get() == 'Fahrenheit' and choices2.get() == 'Kelvin':
            label_var.set(str(((value2 - 32) * (5/9)) + 273.15))
        else:
            label_var.set(str(((value2 - 32) * (5/9)) + 273.15))

    except ValueError:
        label_var.set("Enter")

title1 = tk.Label(root, text="Temperature", font=("calibri BOLD", 26), fg='blue', bg='white')
title1.place(x=0, y=0)

title2 = tk.Label(root, text="Converter", font=("calibri BOLD", 26), fg='white', bg='blue')
title2.place(x=225, y=0)

entry_var = tk.StringVar()
entry_var.trace("w", update_label)

enttemp = tk.Entry(root, font=("calibri 30 bold"), width=9, bg='white', borderwidth=0, fg='blue', textvariable=entry_var)
enttemp.place(x=2, y=180)
enttemp.focus_set()

label_var = tk.StringVar()

label = tk.Entry(root, font=("calibri 30 bold"), width=9, bg='blue', borderwidth=0, fg='white', textvariable=label_var)
label.place(x=201, y=180)

def check_options(*args):
    choices = ['Fahrenheit', 'Celcius', 'Kelvin']
    if choices1.get() == choices2.get():
        choices.remove(choices1.get())
        choices2.set(choices[0])
    elif choices2.get() == choices1.get():
        choices.remove(choices2.get())
        choices1.set(choices[0])

choices1 = tk.StringVar()
choices2 = tk.StringVar()

choices1.set('Fahrenheit')
choices2.set('Celcius')

choices1.trace("w", check_options)
choices2.trace("w", check_options)

lis1 = tk.OptionMenu(root, choices1, 'Fahrenheit', 'Celcius', 'Kelvin')
lis1.place(x=35, y=45)
lis1.configure(bg='white', fg='blue', font=("calibri 15 bold"), highlightthickness=0, borderwidth=0, relief='flat')

lis2 = tk.OptionMenu(root, choices2, 'Fahrenheit', 'Celcius', 'Kelvin')
lis2.place(x=250, y=45)
lis2.configure(bg='blue', fg='white', font=("calibri 15 bold"), highlightthickness=0, borderwidth=0, relief='flat')



root.mainloop()
