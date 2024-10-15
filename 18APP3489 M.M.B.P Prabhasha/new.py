from tkinter import *
from tkinter import ttk
import sqlite3

c = sqlite3.connect("student.db")
print("Database created")
curses = c.cursor()
curses.execute("CREATE TABLE IF NOT EXISTS student(Id VARCHAR(10), Name VARCHAR(20), Age INTEGER, DOB VARCHAR(15), Department VARCHAR(20), Year VARCHAR(10))")
c.commit()
c.close()
print("Table Created")


class Student:
    def __init__(self, main):
        self.main = main
        self.T_Frame = Frame(self.main, height=50, width=1200, background="blue")
        self.T_Frame.pack()
        self.Title = Label(self.T_Frame, text="Student Management System", font="arial 20 bold", width=1200,
                           bg="OliveDrab4")
        self.Title.pack()

        self.Frame_1 = Frame(self.main, height=600, width=450, bd=2, relief=GROOVE, bg="OliveDrab2")
        self.Frame_1.pack(side=LEFT)

# add labels for frame_1
        self.Frame_1.pack_propagate(0)
        Label(self.Frame_1,text="Student Details",background='White', font="arial 14 bold").pack()

        self.Id = Label(self.Frame_1, text="Id",background='White',font='arial 12 bold')
        self.Id.place(x=20, y=60)
        self.Id_Entry = Entry(self.Frame_1,width=40)
        self.Id_Entry.place(x=150, y=60)

        self.Name = Label(self.Frame_1, text="Name",background='White',font='arial 12 bold')
        self.Name.place(x=20, y=120)
        self.Name_Entry = Entry(self.Frame_1,width=40)
        self.Name_Entry.place(x=150, y=120)

        self.Age = Label(self.Frame_1, text="Age",background='White',font='arial 12 bold')
        self.Age.place(x=20, y=180)
        self.Age_Entry = Entry(self.Frame_1,width=40)
        self.Age_Entry.place(x=150, y=180)

        self.DOB = Label(self.Frame_1, text="DOB",background='White',font='arial 12 bold')
        self.DOB.place(x=20, y=240)
        self.DOB_Entry = Entry(self.Frame_1,width=40)
        self.DOB_Entry.place(x=150, y=240)

        self.Department = Label(self.Frame_1, text="Department",background='White',font='arial 12 bold')
        self.Department.place(x=20, y=300)
        self.Department_Entry = Entry(self.Frame_1,width=40)
        self.Department_Entry.place(x=150, y=300)

        self.Year = Label(self.Frame_1, text="Academic Year",background='White',font='arial 12 bold')
        self.Year.place(x=20, y=360)
        self.Year_Entry = Entry(self.Frame_1,width=40)
        self.Year_Entry.place(x=150, y=360)

# adding Button for Frame_1

        self.Button_Frame = Frame(self.Frame_1, height=250,width=250, relief=GROOVE,bd=2, background="DarkOliveGreen3")
        self.Button_Frame.place(x=80, y=400)

        self.Add = Button(self.Button_Frame, text='Add', width=25,font="arial 12 bold", command=self.Add)
        self.Add.pack()

        self.Delete = Button(self.Button_Frame, text='Delete', width=25, font="arial 12 bold", command=self.Delete)
        self.Delete.pack()

        self.Update = Button(self.Button_Frame, text='Update',width=25, font="arial 12 bold", command=self.Update)
        self.Update.pack()

        self.Clear = Button(self.Button_Frame, text='Clear', width=25, font="arial 12 bold", command=self.Clear)
        self.Clear.pack()



        self.Frame_2 = Frame(self.main, height=600, width=750, bd=2, relief=GROOVE, bg="OliveDrab2")
        self.Frame_2.pack(side=RIGHT)

# crete tables Frame_2

        self.tree = ttk.Treeview(self.Frame_2, columns=('c1', 'c2', 'c3', 'c4', 'c5', 'c6'), show='headings', height=25)
        self.tree.pack()

        self.tree.column("#1", anchor=CENTER, width=50)
        self.tree.heading("#1", text='Id')

        self.tree.column("#2", anchor=CENTER, width=150)
        self.tree.heading("#2", text='Name')

        self.tree.column("#3", anchor=CENTER, width=100)
        self.tree.heading("#3", text='Age')

        self.tree.column("#4", anchor=CENTER, width=100)
        self.tree.heading("#4", text='DOB')

        self.tree.column("#5", anchor=CENTER, width=200)
        self.tree.heading("#5", text='Department')

        self.tree.column("#6", anchor=CENTER, width=150)
        self.tree.heading("#6", text='Academic_Year')

 # add sample data

        self.tree.insert("", index=0, values=("18APP", "Bishan",25, "2000-12-12","PST", "3rd"))

# set buttons commands
    def Add(self):
        Id = self.Id_Entry.get()
        Name = self.Name_Entry.get()
        Age = self.Age_Entry.get()
        DOB = self.DOB_Entry.get()
        Department = self.Department_Entry.get()
        Year = self.Year_Entry.get()


        c= sqlite3.connect("student.db")
        curses = c.cursor()
        curses.execute("INSERT INTO student(Id, Name, Age, DOB, Department, Year) VALUES(?,?,?,?,?,?)",(Id,Name,Age,DOB,Department,Year))
        c.commit()
        c.close()
        print("Value Inserted")

        self.tree.insert("", index=0, values=(Id,Name, Age, DOB, Department,Year))


    def Delete(self):
        #item = self.tree.selection()
        #self.tree.delete(item)
        #def Delete(self):
        selected_items = self.tree.selection()

        if selected_items:
          for item in selected_items:
            #self.tree.delete(item)

            selected_items = self.tree.item(item)['values'][0]

            c = sqlite3.connect("student.db")
            cursor = c.cursor()
            cursor.execute("DELETE FROM student WHERE Id=?", (selected_items,))
            c.commit()
            c.close()
            self.tree.delete(item)
          print("Value Deleted")
        else:
          print("No item selected for deletion.")



    def Update(self):
        Id = self.Id_Entry.get()
        Name = self.Name_Entry.get()
        Age = self.Age_Entry.get()
        DOB = self.DOB_Entry.get()
        Department = self.Department_Entry.get()
        Year = self.Year_Entry.get()

        selected_items = self.tree.selection()

        if selected_items:
           item = selected_items[0]
           c= sqlite3.connect("student.db")
           cursor = c.cursor()
           cursor.execute("UPDATE student SET Name=?, Age=?, DOB=?, Department=?,Year=? WHERE Id=?",(Name,Age,DOB,Department,Year,Id))
           c.commit()
           c.close()
           print("Raw value updated")
           self.tree.item(item, values=(Id, Name, Age, DOB, Department, Year))
        else:
           print("No item selected for update.")


    def Clear(self):
        self.Id_Entry.delete(0,END)
        self.Name_Entry.delete(0,END)
        self.Age_Entry.delete(0,END)
        self.DOB_Entry.delete(0,END)
        self.Department_Entry.delete(0,END)
        self.Year_Entry.delete(0,END)







main = Tk()
main.title("Student Management System")
main.resizable(False, False)
main.geometry("1200x600")

# Create an instance of the Student class
student_instance = Student(main)

main.mainloop()
