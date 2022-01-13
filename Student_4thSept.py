from tkinter import *
from tkinter import ttk


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Classroom Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Classroom Management System", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), bg="yellow", fg="red")
        title.pack(side=TOP, fill=X)

        # Manage Frame
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Manage_Frame.place(x=20, y=100, width=450, height=600)

        m_title = Label(Manage_Frame, text="Manage Students",
                        font=("times new roman", 30, "bold"), bg="crimson", fg="white")
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = Label(Manage_Frame, text="Roll No",
                         font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_roll = Entry(Manage_Frame, font=(
            "times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(Manage_Frame, text="Name",
                         font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Manage_Frame, font=(
            "times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(Manage_Frame, text="Email",
                          font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_email = Entry(Manage_Frame, font=(
            "times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender",
                           font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(
            Manage_Frame, font=("times new roman", 13, "bold"), state='readonly')
        combo_gender['values'] = ("male", "female", "other")
        combo_gender.grid(row=4, column=1, padx=20, pady=10)

        lbl_contact = Label(Manage_Frame, text="Contact",
                            font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_contact = Entry(Manage_Frame, font=(
            "times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_dob = Label(Manage_Frame, text="D.O.B",
                        font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_dob = Entry(Manage_Frame, font=(
            "times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(Manage_Frame, text="Address",
                            font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_Address = Text(Manage_Frame, width=25, height=4, font=("", 10))
        txt_Address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        # Button Frame

        Button_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="crimson")
        Button_Frame.place(x=15, y=520, width=420)

        AddBtn = Button(Button_Frame, text="Add", width=10).grid(
            row=0, column=0, padx=10, pady=10)

        UpdateBtn = Button(Button_Frame, text="Update", width=10).grid(
            row=0, column=1, padx=10, pady=10)

        DeleteBtn = Button(Button_Frame, text="Delete", width=10).grid(
            row=0, column=2, padx=10, pady=10)

        ClearBtn = Button(Button_Frame, text="Clear", width=10).grid(
            row=0, column=3, padx=10, pady=10)

        # Manage Detail Frame
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=800, height=600)


root = Tk()
ob = Student(root)
root.mainloop()
