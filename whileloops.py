def greetings():

    name = input("Enter Your Name : ")

    age = int(input("Enter Your Age : "))
    
    print(f"Your Name Is {name} And Your Age Is {age}.")

    if(age>18):
        print(f"Congrats {name} Your Age {age} Is Eligible For This System.")

    else:
        print(f"OOPS Your Age {age} Is Not Compatible For This System.")

greetings()