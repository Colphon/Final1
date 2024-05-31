from tkinter import *
import csv


class Gui:
    def __init__(self, window):
        self.window = window

        self.frame_one = Frame(self.window)
        self.input_name = Entry(self.frame_one, width=20)
        self.label_name = Label(self.frame_one, text='Name')
        self.label_name.pack(side='left')
        self.input_name.pack(side='left', padx = 5)
        self.frame_one.pack(anchor='w', padx = 10, pady = 10)

        self.frame_two = Frame(self.window)
        self.input_name2 = Entry(self.frame_two, width=20)
        self.label_name2 = Label(self.frame_two, text='Age')
        self.label_name2.pack(side='left', padx=5)
        self.input_name2.pack(side='left', padx=5)
        self.frame_two.pack(anchor='w', padx=10, pady=10)


        self.frame_three = Frame(self.window)
        self.stat_answer = IntVar()
        self.stat_answer.set(0)
        self.label_name3 = Label(self.frame_three, text='Status')
        self.student = Radiobutton(self.frame_three, text='Student', variable=self.stat_answer, value=1)
        self.staff = Radiobutton(self.frame_three, text='Staff', variable=self.stat_answer, value=2)
        self.both = Radiobutton(self.frame_three, text='Both', variable=self.stat_answer, value=3)
        self.label_name3.pack(side='left', pady=10)
        self.student.pack(side='left', pady=10)
        self.staff.pack(side='left', pady=10)
        self.both.pack(side='left', pady=10)
        self.frame_three.pack()

        self.frame_four = Frame(self.window)
        self.button_save = Button(self.frame_four, text='SAVE', command=self.submit)
        self.button_save.pack(side='bottom', pady = 10)
        self.label_name.pack()
        self.frame_four.pack()

        self.frame_five = Frame(self.window)
        self.label_display = Label(self.frame_five, text='Please fill out all values')
        self.label_display.pack(side='bottom')
        self.frame_five.pack()

        self.frame_six = Frame(self.window)
        self.label_display = Label(self.frame_six, text='WHY HELLO', font=('Impact',10,'bold'), fg='#527860')
        self.label_display.pack(side='bottom')
        self.frame_six.pack()

    def submit(self):
        name = self.input_name.get()
        if name == '':
            name = 'Anonymous'
        name = name.strip()
        try:
            age = self.input_name2.get()
            age = int(age)
            if age < 0:
                raise ValueError
            age = age * 10
            status = self.stat_answer.get()
            if status == 0:
                status = 'NA'
            elif status == 1:
                status = 'Student'
            elif status == 2:
                status = 'Staff'
            else:
                status = 'Both'
            with open('data.csv', 'a', newline='') as stuffout:
                contentout = csv.writer(stuffout)
                contentout.writerow([name, age, status])
            self.input_name.delete(0, END)
            self.input_name2.delete(0, END)
            self.label_display.config(text='')
            self.stat_answer.set(0)
            self.input_name.focus()
        except ValueError:
            self.label_display.config(text='Enter correct age value')


