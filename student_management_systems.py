"""
1. Add student
2. View students
3. Search student
4. Calculate average marks
5. Show passed students
6. Exit

"""

student_lists = []

def add_student():

    try:
        stu_id = int(input("enter student id : "))
        name = input("enter a student name : ")
        mark = int(input("enter a student mark: "))

        # print({"id":id ,"name":name ,"mark":mark} )

        if stu_id >0 and (mark >=0 and mark <=100):
           student_lists.append({"id": stu_id, "name": name, "mark": mark})
        else:
            print("no student added give only positive integers")

    except ValueError:
        print("only gives related data type values")


def view_student():

    for key in student_lists:

        for keys ,value in key.items():
            print(keys, ":" ,value)

    print(student_lists)


def search_student():

    try:

        student_id = int(input("enter a id for student : "))

        found = False

        for stu_list in student_lists:

            if student_id == stu_list["id"]:
                found = True
                print(stu_list)
                break
        if found is False:
            print("no student found")

    except ValueError:
        print("only gives number in ID")

def calculate_marks():

    sum = 0

    count = 0

    for num in student_lists:


        sum = sum + num["mark"]

        count = count + 1

    print(sum)

    print(count)

    try:
        average = sum / count

        print(average)

    except ZeroDivisionError:
        print("there is no items in a list")


def show_pass_student():

    pass_stu = False

    for marks in student_lists:

        if marks["mark"]>=50:

            pass_stu = True

            print(f'this students are passed {marks}')


    if pass_stu is False:
        print("no students is passed in exams")


def delete_student():

    student_id = int(input("enter a student ID for delete : "))

    found = False

    for student_list in student_lists:

        if student_id == student_list["id"]:

            found = True
            student_lists.remove(student_list)


    if found is False:
            print("no student found")


def update_stud_marks():

    try:

        my_id = int(input("enter a student id : "))
        my_mark = int(input("enter a new student marks : "))

        if my_id >0 and (my_mark >=0 and my_mark<= 100):

            found = False

            for my_list in student_lists:

                if my_id == my_list["id"]:
                    found = True

                    my_list.update({"mark": my_mark})
                    break

            if found is False:
                print("no student found ")

            # print(student_lists)
        else:
            print("no values updated give positive numbers ")

    except ValueError:

        print("give the correct value")


def show_grade():

    try:
        stu_id = int(input("enter a student id : "))

        found = False

        for stu_list in student_lists:

            if stu_id == stu_list["id"]:

                found = True

                if stu_list["mark"] >= 90 and stu_list["mark"] <= 100:

                    print(f'{stu_list.get("name")}\n{stu_list.get("mark")}\ngrade : A')

                elif stu_list["mark"] >= 80 and stu_list["mark"] <= 90:

                    print(f'{stu_list.get("name")}\n{stu_list.get("mark")}\n grade : B')


                elif stu_list["mark"] >= 70 and stu_list["mark"] <= 80:

                    print(f'{stu_list.get("name")}\n{stu_list.get("mark")}\n grade : C')


                elif stu_list["mark"] >= 60 and stu_list["mark"] <= 70:

                    print(f'{stu_list.get("name")}\n{stu_list.get("mark")}\n grade : D')


                elif stu_list["mark"] >= 50 and stu_list["mark"] <= 60:

                    print(f'{stu_list.get("name")}\n{stu_list.get("mark")}\n grade : E')


                elif stu_list["mark"] <= 50:

                    print(f'{stu_list.get("name")}\n{stu_list.get("mark")}\n grade : F')

        if found is False:
            print("no student found")

    except:
        print("give correctly")



while True:

    users_options = input("add student ,view student , search student , calculate marks ,show passed students, delete student ,"
                          " update marks ,show grade,exit : ")

    if users_options == "add student":
        add_student()
        continue
    elif users_options == "view student":
        if student_lists == []:
            print("no students found")
        else:
            view_student()
            continue

    elif users_options == "search student":
        if student_lists == []:
            print("no students found in a list")
        else:
            search_student()

    elif users_options == "calculate marks":

        calculate_marks()

    elif users_options =="show passed students":

        show_pass_student()

    elif users_options == "delete student":

        delete_student()

    elif users_options == "update marks":

        update_stud_marks()

    elif users_options == "show grade":

        show_grade()

    elif users_options == "exit":
        break

    else:
        print("wrong options")









 # if stu_id >=0:
 #            if mark >0 and mark<=100:
 #
 #                student_lists.append({"id": stu_id, "name": name, "mark": mark})
 #            else:
 #                print("give correct mark")
 #
 #        else:
 #            print("give perfect numbers")
