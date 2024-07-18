def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * (n-1)

n = int(input("Enter A Number : "))

print(f"Factorial Of Your Number Is : {factorial(n)}")

def marks():
    dict1 = {"Maths":120 ,
             "Islamiat":22,
             "Physics": 40}
    print(dict1)

marks()

def birds():
    list1 = ["Piegon", "Crow", "Eagle", "Sparrow"]
    print(list1)

birds()

def greetings():

    name = int(input("Enter Your Name : "))

    age = int(input("Enter Your Age : "))
    
    print(f"Your Name Is {name} And Your Age Is {age}.")

    if(age<18):
        print(f"Congrats {name} Your Age {age} Is Eligible For This System.")

    else:
        print(f"OOPS Your Age {age} Is Not Compatible For This System.")


def avg():

   a = int(input("Enter Your Number : "))

   b = int(input("Enter Your Number : "))

   c = int(input("Enter Your Number : "))

   average = (a+b+c)/3

   print(average)
