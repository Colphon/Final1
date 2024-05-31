from tkinter import *
import csv


class Gui:
    def __init__(self, window):
        self.window = window

        self.frame_one = Frame(self.window)
        self.label_display = Label(self.frame_one, text='OFFICIAL BALLOT', font=('Roboto Condensed', 10, 'bold'))
        self.label_display.pack()
        self.frame_one.pack(pady=5)

        self.lineframe = Frame(self.window, highlightbackground='gray', highlightthickness=0.5)
        self.lineframe.pack()

        self.frame_two = Frame(self.lineframe)
        self.input_name = Entry(self.frame_two, width=20)
        self.label_name = Label(self.frame_two, text='ID')
        self.label_name.pack(side='left', padx=5)
        self.input_name.pack(side='left', padx=5)
        self.frame_two.pack(padx=70, pady=20)

        self.lineframe2 = Frame(self.window, highlightbackground='gray', highlightthickness=0.5)
        self.lineframe2.pack()

        self.frame_three = Frame(self.lineframe2)
        self.label_name2 = Label(self.frame_three, text='Governor', font=('Segoe UI', 9, 'bold'))
        self.label_name3 = Label(self.frame_three, text='(Vote for only one)', font=('Segoe UI', 7))
        self.label_name2.pack(pady=(10,0))
        self.label_name3.pack()
        self.frame_three.pack(side='top')

        self.frame_four = Frame(self.lineframe2)
        self.stat_answer = IntVar()
        self.stat_answer.set(0)
        self.Bianca = Radiobutton(self.frame_four, text='  Bianca T. Sparrow - D', variable=self.stat_answer, value=1)
        self.Edward = Radiobutton(self.frame_four, text='  Edward M. Green - R', variable=self.stat_answer, value=2)
        self.Felicia = Radiobutton(self.frame_four, text='  Felicia F. Soot - L', variable=self.stat_answer, value=3)
        self.Write_in = Radiobutton(self.frame_four, variable=self.stat_answer, value=4, command=self.enable)
        self.Write_entry = Entry(self.frame_four, state='disabled')
        self.Write_label = Label(self.lineframe2, text='Write-in', font=('Segoe UI', 5))
        self.Bianca.pack(anchor='w', pady=5)
        self.Edward.pack(anchor='w', pady=5)
        self.Felicia.pack(anchor='w', pady=5)
        self.Write_in.pack(side='left', pady=5)
        self.Write_entry.pack(side='left', pady=5)
        self.Write_label.pack(side='bottom', padx=(0,210), pady=(0,10))
        self.frame_four.pack(padx=(0, 146), pady=(10,0))

        self.frame_five = Frame(self.window)
        self.button_save = Button(self.frame_five, text='SUBMIT', command=self.submit)
        self.button_save.pack(side='bottom', pady = 30)
        self.frame_five.pack()

        self.frame_six = Frame(self.window)
        self.label_display1 = Label(self.frame_six, text='Please insert ID and fill out candidate choice', fg='#ECA516')
        self.label_display1.pack(side='bottom', pady=(0,30))
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

    def enable(self):
        pass


