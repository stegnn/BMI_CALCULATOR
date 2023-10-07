from tkinter import *

def is_numeric(value): # girilen değerin numara mı yoksa metin mi olduğunu kontrol eden fonksiyon
    try:
        float(value)
        return True
    except ValueError:
        return False
def calculator(): #ve bu fonksiyonun içine entegre ettim
    if not is_numeric(kilo.get()) or not is_numeric(boy.get()):
        label3.config(text="Incorrect entry. Please enter digital values.")
        return

    girdi1 = int(kilo.get())
    girdi2 = int(boy.get())
    bmi = girdi1 / ((girdi2/100) ** 2)
    label3.config(text=f"Your BMI is {bmi:.2f}.")
    if (bmi >= 10) and (bmi <= 18.15):
         label3.config(text=f"Your BMI is {bmi:.2f}. You are weak")
    elif (bmi >= 18.15) and (bmi <= 25):
        label3.config(text=f"Your BMI is {bmi:.2f}. You are normal weight")
    elif (bmi >= 25) and (bmi <= 30):
        label3.config(text=f"Your BMI is {bmi:.2f}. You are overweight")
    elif (bmi >= 30) and (bmi <= 40):
        label3.config(text=f"Your BMI is {bmi:.2f}. You are shiko, carefully")
    else:
        label3.config(text=f"Your BMI is {bmi:.2f}. You are too overweight")




ana_ekran = Tk()
ana_ekran.title("BMI Calculator")
ana_ekran.minsize(width=500, height=500)

label1 = Label(ana_ekran, text="Enter Your Weight (kg)", pady=20)
label1.pack()

kilo = Entry(ana_ekran)
kilo.pack()

label2 = Label(ana_ekran, text="Enter your Height (cm)", pady=20)
label2.pack()

boy = Entry(ana_ekran)
boy.pack()

Button(ana_ekran, text="Calculate", padx=10, command=calculator).pack()

label3 = Label(ana_ekran, font=("Calibri", 12))
label3.pack(pady=20)

label4 = Label(ana_ekran,text=" " , font=("calibri", 12))
label4.pack(pady=20)


ana_ekran.mainloop()