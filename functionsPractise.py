
def identity(name, age, gender,number):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Gender : {gender}")
    print(f"Phone number : {number}")

# identity("Kartal",21,"Male", 34342545)



# key, value= name, age
studentInfo= {"Ahmet": 21,"Kartal":22, "Elon": "50"}
def my_student_info(x):
    '''
    it gives the informations of students that exists in studentInfo dataBase
    '''
    for key,value in x.items():
        print(f"{key} is {value} years old")

#my_student_info(studentInfo)



def addition(*numbers):
    '''
    it helpes us to addition the its parametres
     '''
    total=0
    for i in numbers:
        total=i+total
    print(total)

#addition(1,4,5,6,55,54)




def triangleArea(base_length, high):
    '''
      This function is calculating area of a 2D triangle
    '''
    area= (base_length * high)/2
    print(f"Area: {area}")

# triangleArea(8,4)



