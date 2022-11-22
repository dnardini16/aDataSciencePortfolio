import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

x_label = 10

## title of window
window.title("BMI App with tkinter")

## size of window
window.geometry("450x300")

## intro label
tk.Label(text="Welcome to BMI App with Tkinter", 
                font=("Helvetica",15)
                ).place(x=x_label,y=10)

## dev notes
tk.Label(text="Developed by Davide Nardini", 
                font=("Helvetica",8)
                ).place(x=x_label,y=50)

## w label
tk.Label(text="Weigth (kg)", 
                font=("Helvetica",10)
                ).place(x=x_label,y=100)

## h label
tk.Label(text="Heigth (cm)", 
                font=("Helvetica",10)
                ).place(x=x_label+100,y=100)

## slider for both weight and height
weight_slider = tk.Scale(from_=0, to=200)
weight_slider.place(x=x_label,y=150)
height_slider = tk.Scale(from_=0, to=200)
height_slider.place(x=x_label+100,y=150)

## function to calculate bmi
def get_bmi():
    global text
    try:
        height = height_slider.get()
        weight = weight_slider.get()
        h = height / 100
        bmi = round(weight/(h*h),1)
        text = f"BMI = {bmi}"
    except:
        text = 'No Data'
    tk.Label(window,text=text).place(x=x_label+250,y=220)
        
## button to calculate bmi
btn = tk.Button(window,text="GET BMI",command=get_bmi)
btn.place(x=x_label+250,y=150)

window.mainloop()