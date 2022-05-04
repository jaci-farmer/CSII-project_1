from tkinter import *
import csv

class GUI:
    def __init__(self, window):

        self.window = window

        self.frame_top = Frame(self.window)
        self.label_name = Label(self.frame_top, text='Name')
        self.entry_name = Entry(self.frame_top)
        self.label_name.pack(padx=0, side='left')
        self.entry_name.pack(padx=5, side='left')
        self.frame_top.pack(anchor='w', pady=10)

        self.frame_middle = Frame(self.window)
        self.label_age = Label(self.frame_middle, text='Age')
        self.entry_age = Entry(self.frame_middle)
        self.label_age.pack(padx=5, side='left')
        self.entry_age.pack(padx=5, side='left')
        self.frame_middle.pack(anchor='w', pady=10)

        self.frame_bottom = Frame(self.window)
        self.label_status = Label(self.frame_bottom, text='Status')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_student = Radiobutton(self.frame_bottom, text = "Student", variable=self.radio_1, value=1)
        self.radio_staff = Radiobutton(self.frame_bottom, text="Staff", variable=self.radio_1, value=2)
        self.radio_both = Radiobutton(self.frame_bottom, text="Both", variable=self.radio_1, value=3)
        self.label_status.pack(padx=5, side='left')
        self.radio_student.pack(padx=5, side='left')
        self.radio_staff.pack(padx=5, side='left')
        self.radio_both.pack(padx=5, side='left')
        self.frame_bottom.pack(anchor='w', pady=10)

        self.frame_last = Frame(self.window)
        self.button_save = Button(self.frame_last, text = "SAVE", command=self.clicked)
        self.button_save.pack()
        self.frame_last.pack()


    def clicked(self):

        name = self.entry_name.get()
        age = int(self.entry_age.get())
        if type(age) != int:
            raise TypeError("Not a number")
        if age < 0:
            raise ValueError("Negative")
        age = age * 2
        status = self.radio_1.get()
        if status == 1:
            status = "student"
        if status == 2:
            status = "staff"
        if status == 3:
            status = "both"


        info = [name, age, status]

        with open("records.csv", 'a', newline= "") as csvfile:
            content = csv.writer(csvfile)

            content.writerow(info)

        self.entry_name.delete(0, END)
        self.entry_age.delete(0, END)
        self.radio_1.set(0)




