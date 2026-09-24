
stud_lists = []

class Student:

    def __init__(self ,id ,name ,mark):
        self.id = id
        self.name = name
        self.mark =mark

    def display(self):

        print(f'{self.id} {self.name} {self.mark}')
        # print({"id":self.id ,"name":self.name ,"mark":self.mark})


def add_student():

    try:

        stud_id = int(input("enter a id: "))
        name = input("enter a name : ")
        mark = int(input("enter a mark : "))

        found = False

        if stud_id >= 0 and (mark >= 0 and mark <= 100):

            student = Student(stud_id, name, mark)

            for my_id in stud_lists:

                if my_id.id == stud_id:

                    found = True

                    print("only unique ID's no student added")

                    break

            if found is False:

                stud_lists.append(student)

        else:
            print("no added to list")

    except ValueError:
        print("give correct value")


def update_student():

    try:

        stud_id = int(input("enter a student id : "))
        stud_mark = int(input("enter a student mark : "))

        found = False

        if stud_id >= 0 and (stud_mark >= 0 and stud_mark <= 100):

            for student in stud_lists:

                if student.id == stud_id:

                    found = True

                    student.mark = stud_mark

                    break

            if found is False:
                print("no student found")
        else:
            print(" no updated marks")

    except ValueError:
        print("give correct value")

def view_student():
    for student in stud_lists:
        student.display()

while True:

    user_actions = input("add student ,update mark , view student ,exit: ")

    if user_actions =="add student":

        add_student()

    elif user_actions =="update mark":
        update_student()

    elif user_actions == "view student":

        view_student()

    elif user_actions == "exit":

        break








