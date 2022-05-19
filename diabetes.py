import re
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


global a


def browse():
    filename = filedialog.askopenfilename(filetypes=(("All Files", "*.*"), ("File", "*.py")))
    path.config(text=filename)

    a = filename
    global file
    file = a
    print(a)



def test():
    if Fname.get() == "":
        print("First Name Field is Empty!!")
        user = "First Name Field is Empty!!"
        Label(win, text=user, fg="blue", bg="yellow", font=("Calibri 10 bold")).place(x=12, y=720)
    elif Lname.get() == "":
        print("Last Name Field is empty")
        user = "Last Name Fiels is empty"
        Label(win, text=user, fg="blue", bg="yellow", font=("calibri 10 bold")).place(x=12, y=720)

    elif phone.get() == "":
        print("Phone No. Field is empty")
        user = "Phone No. Fiels is empty"
        Label(win, text=user, fg="blue", bg="yellow", font=("calibri 10 bold")).place(x=12, y=720)

    #elif gender.get() == "":
        #print("Gender Field is Empty!!")
        #user = "Gender Field is Empty!!"
        #Label(win, text=user, fg="blue", bg="yellow", font=("Calibri 10 bold")).place(x=12, y=720)

    elif glucose_conc.get() == "":
        print("Glucose Concentration Field is Empty!!")
        user = "Glucose Concentration Field is Empty!!"
        Label(win, text=user, fg="blue", bg="yellow", font=("Calibri 10 bold")).place(x=12, y=720)

    elif diastolic_bp.get() == "":
        print(" Diastolic_bp is Empty!!")
        user = "Diastolic Field is Empty!!"
        Label(win, text=user, fg="blue", bg="yellow", font=("Calibri 10 bold")).place(x=12, y=720)

    elif thickness.get() == "":
        print("Thickness Field is Empty!!")
        user = "Thickness Field is Empty!!"
        Label(win, text=user, fg="blue", bg="yellow", font=("Calibri 10 bold")).place(x=12, y=720)

    elif insulin.get() == "":
        print("Insulin Field is Empty!!")
        user = "Insulin Field is Empty!!"
        Label(win, text=user, fg="blue", bg="yellow", font=("Calibri 10 bold")).place(x=12, y=720)

    elif bmi.get() == "":
        print("BMI Field is Empty!!")
        user = "BMI Field is Empty!!"
        Label(win, text=user, fg="blue", bg="yellow", font=("Calibri 10 bold")).place(x=12, y=720)

    elif diab_pred.get() == "":
        print("diab_pred Field is Empty!!")
        user = "diab_pred Field is Empty!!"
        Label(win, text=user, fg="blue", bg="yellow", font=("Calibri 10 bold")).place(x=12, y=720)

    elif age.get() == "":
        print("Age Field is Empty!!")
        user = "Age Field is Empty!!"
        Label(win, text=user, fg="blue", bg="yellow", font=("Calibri 10 bold")).place(x=12, y=720)

    elif skin.get() == "":
        print("Skin Field is Empty!!")
        user = "Skin Field is Empty!!"
        Label(win, text=user, fg="blue", bg="yellow", font=("Calibri 10 bold")).place(x=12, y=720)
    import numpy as np
    import pandas as pd

    diabetes = pd.read_csv('/home/ms/Downloads/internship projects/Diabetes-Prediction-master/data/pima-data.csv')
    diabetes.head()
    diabetes.shape
    diabetes.isnull().sum()
    # the diabetes column in dataset is the dependent attribute and the rest are independent attributes
    # the dependent column is in char format and all others are in numeric format to we will have to encode it.
    diab_map = {True: 1, False: 0}
    diabetes['diabetes'] = diabetes['diabetes'].map(diab_map)
    diabetes.head()
    # now, we will split the data into training and test set
    from sklearn.model_selection import train_test_split
    features = ['num_preg', 'glucose_conc', 'diastolic_bp', 'thickness', 'insulin', 'bmi', 'diab_pred', 'age', 'skin']
    predictor = ['diabetes']
    x = diabetes[features].values
    y = diabetes[predictor].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=20)
    # check which independent features have observation as 0
    print("no of rows missing values glucose_conc:{0}".format(len(diabetes.loc[diabetes['glucose_conc'] == 0])))
    print("no of rows with missing values diastolic_bp:{0}".format(len(diabetes.loc[diabetes['diastolic_bp'] == 0])))
    print("no of rows with missing values thickness:{0}".format(len(diabetes.loc[diabetes['thickness'] == 0])))
    print("no of rows with missing values insulin:{0}".format(len(diabetes.loc[diabetes['insulin'] == 0])))
    print("no of rows with missing values bmi:{0}".format(len(diabetes.loc[diabetes['bmi'] == 0])))
    print("no of rows with missing values diab_pred:{0}".format(len(diabetes.loc[diabetes['diab_pred'] == 0])))
    print("no of rows with missing values age:{0}".format(len(diabetes.loc[diabetes['age'] == 0])))
    print("no of rows with missing values skin:{0}".format(len(diabetes.loc[diabetes['skin'] == 0])))

    from sklearn.impute import SimpleImputer
    fillValues = SimpleImputer(missing_values=0, strategy="mean")
    x_train = fillValues.fit_transform(x_train)
    x_test = fillValues.fit_transform(x_test)

    # Naive Bayes Algorithm
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import classification_report
    from sklearn.metrics import accuracy_score
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler
    from sklearn.naive_bayes import GaussianNB
    classifier = GaussianNB()
    classifier.fit(x_train, y_train)
    # predicting the test set results
    NBy_pred = classifier.predict(x_test)

    # making confusion matrix
    cm_NB = confusion_matrix(y_test, NBy_pred)
    cm_NB

    accuracy = ((104 + 38) / 192)
    accuracy

    print('confusion matrix: \n', confusion_matrix(y_test, NBy_pred))
    print('accuracy: \n', accuracy_score(y_test, NBy_pred))
    print('classication report: \n', classification_report(y_test, NBy_pred))
    print(result)


    #print("Testing")

    dimension = (40,40)
    result = NBy_pred.predict(x_test)

    #print(result)
    if result[1] == 1:
        print("Infected")
        person = Fname.get()
        user = person + 'is tested as Diabetes patient '
        a = user
        Label(win, text="", fg="red", bg="white",font=("Calibri 12 bold")).place(x=12, y=720)
        Label(win, text=user, fg="red", bg="white", font=("Calibri 12 bold")).place(x=12, y=720)

    else:
        print("Uninfected")
        person = Fname.get()
        user = person + ' is NOT Tested as Diabetic Patient'
        a = user
        Label(win, text=". ", fg="red", bg="white", font=("Calibri 12 bold")).place(x=12, y=720)
        Label(win, text=user, fg="blue", bg="yellow", font=("Calibri 12 bold")).place(x=12, y=720)
    print(result)

        # after testing save the records
        #save(a)

    def save(a):
        First = Fname.get()
        Last = Lname.get()
        #email = email.get()
        phoneNo = phone.get()
        gender = str(radio.get())
        save_name = First + ".txt"

        file = open(save_name, "a")
        file.write("\n\nFirst Name: " + First + "\n")
        file.write("Last Name: " + Last + "\n")
        file.write("Phone: " + phone + "\n")
        file.write("Email: " + email + "\n")

        file.write("Gender: " + gender + "\n")
        file.write("Report: " + a + "\n")
        file.close()
        report = First + "'s Health Detection have successfully done and Report is saved in " + First + ".txt"
        Label(win, text=report, fg="blue", bg="yellow", font=("Calibri 10 bold")).place(x=12, y=720)
        save(a)

def reset():
    Fname.set("")
    Lname.set("")
    email.set("")
    phone.set("")
    gender.set("")
    num_preg.set("")
    glucose_conc.set("")
    diastolic_bp.set("")
    thickness.set("")
    insulin.set("")
    bmi.set("")
    diab_pred.set("")
    age.set("")
    skin.set("")


win = Tk()
win.geometry("400x1200")
win.configure(background="cyan")
win.title("Diabetes Prediction")
# win.iconbitmap('download.png')

title = Label(win, text="Diabetes Prediction", bg="gray", width="300", height="2", fg="White",
              font=("Calibri 20 bold italic underline")).pack()

Fname = Label(win, text="First Name: ", bg="cyan", font=("verdana 12")).place(x=12, y=80)
gap = Label(win, text="", bg="cyan").pack()

Lname = Label(win, text="Last Name:", bg="cyan", font=("verdana 12")).place(x=12, y=120)
gap = Label(win, text="", bg="cyan").pack()

email = Label(win, text="Email ID:", bg="cyan", font=("verdana 12")).place(x=12, y=160)
gap = Label(win, text="", bg="cyan").pack()

phone = Label(win, text="Phone:", bg="cyan", font=("verdana 12")).place(x=12, y=200)
gap = Label(win, text="", bg="cyan").pack()

# city = Label(win, text = "City:", bg = "cyan", font = ("verdana 12")).place(x = 12, y = 300)
# gap = Label(win, text = "", bg = "cyan").pack()

gender = Label(win, text="Gender:", bg="cyan", font=("verdana 12")).place(x=12, y=240)
radio = StringVar()
Male = Radiobutton(win, text="Male", bg="cyan", variable=radio, value="Male", font=("Verdana 12")).place(x=12, y=280)
Female = Radiobutton(win, text="Female", bg="cyan", variable=radio, value="Female", font=("Verdana 12")).place(x=120,
                                                                                                               y=280)
gap = Label(win, text="", bg="cyan").pack()

num_preg = Label(win, text="No. of Preg: ", bg="cyan", font=("verdana 12")).place(x=12, y=320)
gap = Label(win, text="", bg="cyan").pack()

glucose_conc = Label(win, text="Glucose Conc: ", bg="cyan", font=("verdana 12")).place(x=12, y=360)
gap = Label(win, text="", bg="cyan").pack()

# diastolic_bp = Label(win, text = "DiasBP: ", bg = "cyan", font = ("verdana 12")).place(x = 12, y = 400)
# gap = Label(win, text = "", bg = "cyan").pack()

diastolic_bp = Label(win, text="DiasBP:", bg="cyan", font=("verdana 12")).place(x=12, y=400)
gap = Label(win, text="", bg="cyan").pack()

thickness = Label(win, text="Thickness: ", bg="cyan", font=("verdana 12")).place(x=12, y=440)
gap = Label(win, text="", bg="cyan").pack()

insulin = Label(win, text="insulin: ", bg="cyan", font=("verdana 12")).place(x=12, y=480)
gap = Label(win, text="", bg="cyan").pack()

bmi = Label(win, text="BMI: ", bg="cyan", font=("verdana 12")).place(x=12, y=520)
gap = Label(win, text="", bg="cyan").pack()

diab_pred = Label(win, text="Diabetes Pred: ", bg="cyan", font=("verdana 12")).place(x=12, y=560)
gap = Label(win, text="", bg="cyan").pack()

age = Label(win, text="Age: ", bg="cyan", font=("verdana 12")).place(x=12, y=600)
gap = Label(win, text="", bg="cyan").pack()

skin = Label(win, text="skin: ", bg="cyan", font=("verdana 12")).place(x=12, y=640)
gap = Label(win, text="", bg="cyan").pack()

Fname = StringVar()
Lname = StringVar()
email = StringVar()
phone = StringVar()
# city = StringVar()
gender = StringVar()
num_preg = StringVar()
glucose_conc = StringVar()
diastolic_bp = StringVar()
thickness = StringVar()
insulin = StringVar()
bmi = StringVar()
diab_pred = StringVar()
age = StringVar()
skin = StringVar()

entry_Fname = Entry(win, textvariable=Fname, width=30)
entry_Fname.place(x=120, y=80)

entry_Lname = Entry(win, textvariable=Lname, width=30)
entry_Lname.place(x=120, y=120)

entry_email = Entry(win, textvariable=email, width=25)
entry_email.place(x=120, y=160)

entry_phone = Entry(win, textvariable=phone, width=10)
entry_phone.place(x=120, y=200)

entry_num_preg = Entry(win, textvariable=num_preg, width=7)
entry_num_preg.place(x=160, y=320)

entry_glucose_conc = Entry(win, textvariable=glucose_conc, width=7)
entry_glucose_conc.place(x=160, y=360)

entry_diastolic_bp = Entry(win, textvariable=diastolic_bp, width=7)
entry_diastolic_bp.place(x=120, y=400)

entry_thickness = Entry(win, textvariable=thickness, width=7)
entry_thickness.place(x=120, y=440)

entry_insulin = Entry(win, textvariable=insulin, width=7)
entry_insulin.place(x=120, y=480)

entry_bmi = Entry(win, textvariable=bmi, width=7)
entry_bmi.place(x=120, y=520)

entry_diab_pred = Entry(win, textvariable=diab_pred, width=7)
entry_diab_pred.place(x=160, y=560)

entry_age = Entry(win, textvariable=age, width=7)
entry_age.place(x=120, y=600)

entry_skin = Entry(win, textvariable=skin, width=7)
entry_skin.place(x=120, y=640)
# entry_city = Entry(win, textvariable = city, width = 25)
# entry_phoneNo.place(x = 120, y = 300)

path = Label(win, bg="cyan", font=("Verdana 8"))
path.place(x=150, y=400)
upload = Button(win, text="Upload", width="8", height="1", activebackground="blue", bg="Pink", font=("Calibri 12 "),
                command=browse).place(x=120, y=680)

reset = Button(win, text="Reset", width="6", height="1", activebackground="red", bg="Pink", font=("Calibri 12 "),
               command=reset).place(x=20, y=680)
submit = Button(win, text="Test", width="12", height="1", activebackground="violet", bg="Pink", command=test,
                font=("Calibri 12 ")).place(x=240, y=680)

win.mainloop()
