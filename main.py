import tkinter

def calculating():
    h = entry_height.get()
    w = entry_weight.get()

    if entry_height.get() == "" or entry_weight.get() == "":
        result_label.config(text="Enter both weight and height!")
    else:
        try:
            int_h = int(h)
            try:
                int_w = int(w)
                bmi = int_w/((int_h / 100) ** 2)
                if 0 < bmi < 18.5 and int_h > 0 and int_w > 0:
                    bmi_new = format(bmi, ".2f")
                    result_label.config(text=f"Your BMI is {bmi_new}. You are under weight")
                    result_label.pack()

                elif 18.5 <= bmi <25 and int_h > 0 and int_w > 0:
                    bmi_new = format(bmi, ".2f")
                    result_label.config(text=f"Your BMI is {bmi_new}. You are normal weight")
                    result_label.pack()

                elif 25 <= bmi <30 and int_h > 0 and int_w > 0:
                    bmi_new = format(bmi, ".2f")
                    result_label.config(text=f"Your BMI is {bmi_new}. You are over weight")
                    result_label.pack()

                elif 30 <= bmi <35 and int_h > 0 and int_w > 0:
                    bmi_new = format(bmi, ".2f")
                    result_label.config(text=f"Your BMI is {bmi_new}. You are Obesity Class I")
                    result_label.pack()

                elif 35 <= bmi <40 and int_h > 0 and int_w > 0:
                    bmi_new = format(bmi, ".2f")
                    result_label.config(text=f"Your BMI is {bmi_new}. You are Obesity Class II")
                    result_label.pack()

                elif 40 <= bmi and int_h > 0 and int_w > 0:
                    bmi_new = format(bmi, ".2f")
                    result_label.config(text=f"Your BMI is {bmi_new}. You are Obesity Class III")
                    result_label.pack()

                elif bmi < 0 or int_h < 0 or int_w < 0:
                    result_label.config(text="Entered values can not be negative!")
                    result_label.pack()
                else:
                    result_label.config(text="Calculating is failed. Please try again!")
                    result_label.pack()
            except:
                result_label.config(text="Invalid weight!")
        except:
            result_label.config(text="Invalid height!")




window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(height=300,width=250)

label_weight = tkinter.Label(window,text="Enter Your Weight (kg)")
label_weight.config(pady=10)
label_weight.pack()

entry_weight = tkinter.Entry(window,width=10)
entry_weight.pack()

label_height = tkinter.Label(window,text="Enter Your Height (cm)")
label_height.config(pady=10)
label_height.pack()

entry_height = tkinter.Entry(window,width=10)
entry_height.pack(pady=10)

calculate_button = tkinter.Button(window,text="Calculate",command=calculating)
calculate_button.pack(pady=10)

result_label = tkinter.Label(window,text="")
result_label.pack()

window.mainloop()
