student=[]
course =[]


def add_student(s, ID, name, DOB) :
    info={}
    info["id"]= ID
    info["name"]= name
    info["DOB"]= DOB
    
    s.append(info)
    
def add_student_from_user(s) :
    info={}
    info["id"]= input("id: ")
    info["name"]= input("name: ")
    info["DOB"]= input("DOB: ")
    
    s.append(info)
    
def add_course(c, ID, name) :
    info= {}
    info["id"]= ID
    info["name"]= name
    
    c.append(info)
    
def add_course_from_user(c) :
    info= {}
    info["id"]= input("id: ")
    info["name"]= input("name: ")
    
    c.append(info)
    
def add_mark(c, ID, student, mark) :
    for i in c:
        if i["id"]== ID: 
            i[student]= int(mark)
        
def add_mark_from_user(c, ID) :
    for i in c:
        if i["id"]== ID: 
            i[input("student: ")]= int(input("mark:"))
            
add_student(student, "0", "Nguyen", "30/3/2003")
add_student(student, "1", "Pham", "19/7/2003")
add_student(student, "2", "Tran", "26/4/2003")

add_course(course, "PP", "python programming")
add_course(course, "AS", "algebraic structure")
add_course(course, "CA", "computer architecture")

add_mark(course, "CA","Tran" ,8)

print("add student:")
add_student_from_user(student)
print("add course: ")
add_course_from_user(course)
print("add mark:  ")
add_mark_from_user(course, "CA")

print(course)
print(student)
