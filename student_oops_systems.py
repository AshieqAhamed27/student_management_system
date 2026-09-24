
class Student:

    def __init__(self ,id,name ,mark):

        self.id = id
        self.name = name
        self.mark = mark


    def display(self):

        print(f'{self.id} {self.name} {self.mark}')

# student= Student(1,"ashieq" ,50)



class StudentManagement:

    def __init__(self):

        self.student_list = []


    def add_student(self):

        try:
            my_id = int(input("enter a number for ID: "))
            name = input("enter a name: ")
            mark = int(input("enter a mark for student : "))

            found  =  False

            for student in self.student_list:

                if my_id == student.id:

                    found = True

                    print("already student exists with same id so can't add a student")

                    break

            if found is False:
                student = Student(my_id, name, mark)

                self.student_list.append(student)

                student.display()

        except ValueError:
            print("!!! give correct value")

    def view_student(self):

        for student in self.student_list:

            student.display()

    def update_mark(self):

        try:

            my_id = int(input("enter a id : "))

            new_mark = int(input("enter a new mark: "))

            found = False

            for student in self.student_list:

                if student.id == my_id:
                    found = True

                    student.mark = new_mark

                    break

            if found is False:
                print("no  updated ")

        except ValueError:
            print("give correct error")

    def search_student(self):

        my_id = int(input("enter a number : "))

        found = False

        for student in self.student_list:

            if student.id == my_id:

                found = True

                print(student.id ,student.name ,student.mark)

        if found is False:

            print("no student found ")


    def calculate_mark(self):

        total = 0

        count = 0

        for student in self.student_list:

            total = student.mark + sum

            count = count + 1

        print(total)

        try:

            average = sum/count

            print(average)
        except ZeroDivisionError:
            print("list has no items")


    def delete_student(self):

        my_id = int(input("enter a ID : "))

        found = False

        for student in self.student_list:

            if my_id == student.id:

                self.student_list.remove(student)

                break

        if found is False:

            print("no student found")

management = StudentManagement()

while True:

    user_actions = input("add student ,view student,update student ,search student ,calculate mark,delete student,exit: ")

    if user_actions =="add student":

        management.add_student()

    elif user_actions == "view student":

        management.view_student()

    elif user_actions =="update student":

        management.update_mark()

    elif user_actions =="search student":

        management.search_student()

    elif user_actions == "calculate mark":

        management.calculate_mark()

    elif user_actions == "delete student":

        management.delete_student()

    elif user_actions == "exit":

        break











