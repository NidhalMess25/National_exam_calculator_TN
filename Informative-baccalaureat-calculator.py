# First : Asking about scores in Exams!

print("Hello Friend,Now you can calculate your Result with Me!!") 

mysection = ["informative","sport","lettre","science","economy","technical","mathematics"]
print(mysection)
section = input("What's your section?,choose from list please.") 
if section == "informative" :
    Philosophy = float(input("How much do you get in philosophy?"))
    Arabic = float(input("How do you get in Arabic?"))
    English = float(input("How do you get in English?"))
    Mathematics = float(input("How do you get in Mathematics?"))
    French = float(input("How do you get in French?"))
    Physics = float(input("How do you get in physics"))
    Algorithms_programming = float(input("How do you get in Algorithms and programming (Written Test)?"))
    Algorithms_programming_ap = float(input("How do you get in Algorithms and programming (Application Test)?")) 
    database = float(input("How do you get in databases?"))
    Information_technology_Test = float(input("How do you get in Information technology and application communication Test?"))
    sport = float(input("How do you get in sport?"))
    Optional = float(input("How do you get in Optional test?"))

    # Second : Printing Result!

    Result = (Philosophy + Arabic + English + Mathematics * 3 + French + Physics * 2 + (((Algorithms_programming + Algorithms_programming_ap)/2) * 3) + database * 1.5 + Information_technology_Test * 1.5 + sport + Optional) / 17

    print("Your Result is" , Result , "!")

    # Finally : Check if the student has passed the test succefully!

    if Result >= 10  and Result < 13:
        print("Congratulations!!!You passed the test with a good Mark!")
    elif Result >= 13 :     
        print("Congratulations!!!You passed the test with an Excillent Mark!,you win an award!!!")
    else :
        print("Sorry, you did not get the required mark!")
else :
    print("Sorry,this is for Informative, you can go to another link!")

