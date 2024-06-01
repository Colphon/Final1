from tkinter import *
import logic



class Gui:
    def __init__(self, window: Tk) -> None:
        '''
        Method that sets up the Gui elements of the window.
        :param window: The window created in main.py using the tkinter module. Will hold Gui elements.
        '''
        self.window = window

        self.frame_one = Frame(self.window)
        self.label_display = Label(self.frame_one, text='OFFICIAL BALLOT', font=('Roboto Condensed', 10, 'bold'))
        self.label_display.pack()
        self.frame_one.pack(pady=5)

        self.lineframe = Frame(self.window, highlightbackground='gray', highlightthickness=0.5)
        self.lineframe.pack()

        self.frame_two = Frame(self.lineframe)
        self.input_ID = Entry(self.frame_two, width=20)
        self.label_name = Label(self.frame_two, text='ID')
        self.label_name.pack(side='left', padx=5)
        self.input_ID.pack(side='left', padx=5)
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
        self.answer = IntVar()
        self.answer.set(0)
        self.Bianca = Radiobutton(self.frame_four, text='  Bianca T. Sparrow - D', variable=self.answer, value=1, command=self.enable)
        self.Edward = Radiobutton(self.frame_four, text='  Edward M. Green - R', variable=self.answer, value=2, command=self.enable)
        self.Felicia = Radiobutton(self.frame_four, text='  Felicia F. Soot - L', variable=self.answer, value=3, command=self.enable)
        self.Write_button = Radiobutton(self.frame_four, variable=self.answer, value=4, command=self.enable)
        self.Write_entry = Entry(self.frame_four, state='disabled')
        self.Write_label = Label(self.lineframe2, text='Write-in', font=('Segoe UI', 5))
        self.Bianca.pack(anchor='w', pady=5)
        self.Edward.pack(anchor='w', pady=5)
        self.Felicia.pack(anchor='w', pady=5)
        self.Write_button.pack(side='left', pady=5)
        self.Write_entry.pack(side='left', pady=5)
        self.Write_label.pack(side='bottom', padx=(0,210), pady=(0,10))
        self.frame_four.pack(padx=(0, 146), pady=(10,0))

        self.frame_five = Frame(self.window)
        self.button_submit = Button(self.frame_five, text='SUBMIT', command=self.submit)
        self.button_submit.pack(side='bottom', pady = 20)
        self.frame_five.pack()

        self.frame_six = Frame(self.window)
        self.label_display2 = Label(self.frame_six, text='Please insert ID and fill out candidate choice', fg='#ECA516')
        self.label_display2.pack(side='bottom', pady=(0,30))
        self.frame_six.pack()


    def submit(self) -> None:
        '''
        Method that calls the checkID and checkvote functions from the logic module to examine the voter id and candidate for issues.
        Afterward, the method calls the submitvote function from the logic module to write the voter id and vote to data.csv.
        Finally, the label at the bottom changes to 'Vote Submitted' and the radiobuttons and entry fields are cleared.
        When one of the functions from the logic module raises an error, label_display2 is configured to display what the voter did wrong.
        '''
        ID = self.input_ID.get()
        vote = self.answer.get()
        candidate=''
        if vote == 4:
            candidate = self.Write_entry.get()
        try:
            checkedID = logic.checkID(ID)
            checkedvote = logic.checkvote(vote, candidate)
            logic.submitvote(checkedID, checkedvote)
            self.label_display2.config(text='Vote Submitted', fg='green')
            self.input_ID.delete(0, END)
            self.Write_entry.delete(0, END)
            self.answer.set(0)
            self.input_ID.focus()

        except TypeError:
            self.label_display2.config(text='Enter seven character alphanumeric ID', fg='red')
        except NameError:
            self.label_display2.config(text='ID has already voted', fg='red')
        except ValueError:
            self.label_display2.config(text='No candidate has been picked', fg='red')
        except SyntaxError:
            self.label_display2.config(text='Please include the first and last name of the candidate', fg='red')

    def enable(self) -> None:
        '''
        Enables the write-in entry field if the write-in option is selected. Otherwise, the field is disabled.
        '''
        if self.answer.get() == 4:
            self.Write_entry.config(state='normal')
        else:
            self.Write_entry.config(state='disabled')
