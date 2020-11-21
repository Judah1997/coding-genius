


from tkinter import *
import tkinter as tk
import numbers
import time

window = tk.Tk()
window.title('jay calculator')
window.geometry('220x320')

icon = tk.PhotoImage(file='C:/Users/Tafadzwa/Pictures/Pictures/Riding.png')
def button_click(item):
    global operator
    operator = operator + str(item)
    input_text.set(operator)

def btn_clear():
    global operator
    operator = ''
    input_text.set(operator)

def But_equal():
    global operator
    result = str(eval(operator))
    input_text.set(result)


operator = ''
input_text = StringVar()

input_frame = tk.Frame(window, bg='powder blue')
input_frame.pack(side=TOP, fill=BOTH, expand=True)

txt = tk.Entry(input_frame, width=20, bg='black', borderwidth=5, textvariable=input_text, fg='white', font=('Cambria', 13))
txt.pack(fill=BOTH, expand=True)
def first_message():
    msg = 'done by tafadzwa'
    txt._displayof(msg)
    time.sleep(1)


first_message()
input_frame1 = tk.Frame(window, bg='red')
input_frame1.pack(side=TOP, fill=BOTH, expand=True)
# buttons from 9-7 in the top row
button7 = tk.Button(input_frame1, text='7', font=('Cambria', 15), command=lambda: button_click(7))
button7.pack(side=LEFT, fill=BOTH, expand=True)
button8 = tk.Button(input_frame1, text='8', font=('Cambria', 15), command=lambda: button_click(8))
button8.pack(side=LEFT, fill=BOTH, expand=True)

multiply_button = tk.Button(input_frame1, text='x', font=('Cambria', 15), command=lambda: button_click('*'))
multiply_button.pack(side=RIGHT, fill=BOTH, expand=True)
button9 = tk.Button(input_frame1, text='9', font=('Cambria', 15), command=lambda: button_click(9))
button9.pack(side=RIGHT, fill=BOTH, expand=True)

# 2nd row buttons
input_frame2 = tk.Frame(window, bg='red')
input_frame2.pack(side=TOP, fill=BOTH, expand=True)
button4 = tk.Button(input_frame2, text='4', font=('Cambria', 15), command=lambda: button_click(4))
button4.pack(side=LEFT, fill=BOTH, expand=True)
button5 = tk.Button(input_frame2, text='5', font=('Cambria', 15), command=lambda: button_click(5))
button5.pack(side=LEFT, fill=BOTH, expand=True)

summation_button = tk.Button(input_frame2, text='+', font=('Cambria', 15), command=lambda: button_click('+'))
summation_button.pack(side=RIGHT, fill=BOTH, expand=True)
button6 = tk.Button(input_frame2, text='6', font=('Cambria', 15), command=lambda: button_click(6))
button6.pack(side=RIGHT, fill=BOTH, expand=True)

# 3rd row buttons
input_frame3 = tk.Frame(window, bg='red')
input_frame3.pack(side=TOP, fill=BOTH, expand=True)
button1 = tk.Button(input_frame3, text='1', font=('Cambria', 15), command=lambda: button_click(1))
button1.pack(side=LEFT, fill=BOTH, expand=True)
button2 = tk.Button(input_frame3, text='2', font=('Cambria', 15), command=lambda: button_click(2))
button2.pack(side=LEFT, fill=BOTH, expand=True)

subtract_button = tk.Button(input_frame3, text=' -', font=('Cambria', 15), command=lambda: button_click('-'))
subtract_button.pack(side=RIGHT, fill=BOTH, expand=True)
button3 = tk.Button(input_frame3, text='3', font=('Cambria', 15), command=lambda: button_click(3))
button3.pack(side=RIGHT, fill=BOTH, expand=True)

#4rd row
input_frame4 = tk.Frame(window, bg='red')
input_frame4.pack(side=TOP, fill=BOTH, expand=True)
button_dot = tk.Button(input_frame4, text='.', font=('Cambria', 15), command=lambda: button_click('.'))
button_dot.pack(side=LEFT, fill=BOTH, expand=True)
division_button = tk.Button(input_frame4, text='/', font=('Cambria', 15), command=lambda: button_click('/'))
division_button.pack(side=RIGHT, fill=BOTH, expand=True)
button0 = tk.Button(input_frame4, text=' 0', font=('Cambria', 15), command=lambda: button_click(0))
button0.pack(side=RIGHT, fill=BOTH, expand=True)

# final row for equal sign
input_frame5 = tk.Frame(window, bg='red')
input_frame5.pack(side=TOP, fill=BOTH, expand=True)
button_dot = tk.Button(input_frame5, text='=', font=('Cambria', 15), command=lambda: But_equal())
button_dot.pack(side=LEFT, fill=BOTH, expand=True)
button_clear = tk.Button(input_frame5, text='C', font=('Cambria', 15), command=lambda: btn_clear())
button_clear.pack(side=LEFT, fill=BOTH, expand=True)


window.mainloop()