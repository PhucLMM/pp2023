
# create a student class 
class student:
    
     # function creates and adds new student to dictionary s
    def add_student( self, ID, name, DOB):
        s[ID]={"name":name, "DOB": DOB}
    # add student but from user    
    def add_student_from_user(self):
        s[input("ID:")]= {"name":input("student name: "), "DOB":input("DOB: ")}
       
    # show students  
    def display(self):
        print (s)
        
#create course class
class course:
    # function creates and add new course to a dictionary c
    def add_course( self, ID, name):
        c[ID]={"name":name}
    # add course but from user
    def add_course_from_user(self):
        c[input("ID: ")]={"name":input("course name: ")}
        
    #function adds marks to right course
    def add_mark(self,course_ID,student_name,mark):
        c[course_ID].update({student_name : mark})
    # add mark but from user    
    def add_mark_from_user(self):
        m={input("student_name: "): int(input("mark: "))}
        c[input("course ID: ")].update(m)
    
    # show courses
    def display(self):
        print(c)
  
# create a dictionary holds students 
s={}
# create a dictionary holds courses
c={}
# create student object
stu= student()

# create and fill inside dict s with new students
stu.add_student("1","Tran","1/2/3")
stu.add_student("2","Nguyen","2/2/2")
print("add new student")
stu.add_student_from_user()
# create course object
cou=course()
# create and fill inside dict c with new courses
cou.add_course("ict_1","programming")
cou.add_course("ict_2","data structure")
print("add new course")
cou.add_course_from_user()
# add mark to course
cou.add_mark("ict_1","thai",20)
print("add student's mark")
cou.add_mark_from_user()
# show students and courses
stu.display()
cou.display()