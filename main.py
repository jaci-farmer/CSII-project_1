from gui import *

def main():
    """
    Method setting size of window and running the application
    :return:
    """
    window = Tk()
    window.title("Student Registration")
    window.geometry("400x300")
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
