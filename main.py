from gui import *
def main():
    window = Tk()
    window.title('VotingApp')
    window.geometry('300x360')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()