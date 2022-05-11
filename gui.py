from tkinter import *
import csv

options = ['Freshman', 'Sophomore', 'Junior', 'Senior']

class GUI:
    """
    Class to represent to GUI application.
    """
    def __init__(self, window) -> None:
        """
        Method to set up the format of the application.
        :param window:
        """
        self.window = window

        # creating the Name label
        self.frame_top = Frame(self.window)
        self.label_name = Label(self.frame_top, text='Name')
        self.entry_name = Entry(self.frame_top)
        self.label_name.pack(padx=0, side='left')
        self.entry_name.pack(padx=5, side='left')
        self.frame_top.pack(anchor='w', pady=10)
        # creating the Age label
        self.frame_middle = Frame(self.window)
        self.label_age = Label(self.frame_middle, text='Age')
        self.entry_age = Entry(self.frame_middle)
        self.label_age.pack(padx=5, side='left')
        self.entry_age.pack(padx=5, side='left')
        self.frame_middle.pack(anchor='w', pady=10)
        # creating the status buttons
        self.frame_bottom = Frame(self.window)
        self.label_gender = Label(self.frame_bottom, text='Gender')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_male = Radiobutton(self.frame_bottom, text = "Male", variable=self.radio_1, value=1)
        self.radio_female = Radiobutton(self.frame_bottom, text="Female", variable=self.radio_1, value=2)
        self.radio_other = Radiobutton(self.frame_bottom, text="Other", variable=self.radio_1, value=3)
        self.label_gender.pack(padx=5, side='left')
        self.radio_male.pack(padx=5, side='left')
        self.radio_female.pack(padx=5, side='left')
        self.radio_other.pack(padx=5, side='left')
        self.frame_bottom.pack(anchor='w', pady=10)
        # creating drop down menu
        self.frame_final = Frame(self.window)
        self.label_grade = Label(self.frame_final, text='Grade')
        self.grade = StringVar(self.window)
        self.grade.set(options[0])  # default value
        self.w = OptionMenu(self.frame_final, self.grade, *options)
        self.w.pack()
        self.frame_final.pack(anchor='w', pady=20)

        # creating the submit button
        self.frame_last = Frame(self.window)
        self.button_submit = Button(self.frame_last, text = "SUBMIT", command=self.clicked)
        self.button_submit.pack()
        self.frame_last.pack()

    def name(self) -> str:
        name = self.entry_name.get()
        if type(name) != str:
            raise ValueError("Not a string")
        return name

    def age(self) -> int:
        age = int(self.entry_age.get())
        if type(age) != int:
            raise TypeError("Not a number")
        if age < 0:
            raise ValueError("Negative")
        return age

    def gender(self) -> str:
        gender = self.radio_1.get()
        if gender == 1:
            gender = "Male"
        if gender == 2:
            gender = "Female"
        if gender == 3:
            gender = "Other"
        return gender

    def get_grade(self) -> str:
        grade = self.grade.get()
        if grade == 0:
            grade = 'Freshman'
        if grade == 1:
            grade = 'Sophomore'
        if grade == 2:
            grade = 'Junior'
        if grade == 3:
            grade = 'Senior'
        return grade


    def clicked(self) -> None:
        """
        Method to save info to csv file when save is clicked
        :return:
        """
        info = [self.name(), self.age(), self.gender(), self.get_grade()]
        # saving info entered to csv file
        with open("records.csv", 'a', newline= "") as csvfile:
            content = csv.writer(csvfile)

            content.writerow(info)

        # resetting the application
        self.entry_name.delete(0, END)
        self.entry_age.delete(0, END)
        self.radio_1.set(0)
        self.grade.set("Freshman")