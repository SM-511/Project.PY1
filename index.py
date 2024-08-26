print("************************************************************************************************************************************)")
print("")
print("**************************************************************** Project 1 *********************************************************)")
print("")
print("************************************************************************************************************************************)")
print(F"                                     ||| -------   THE    -------  QUIZ  ------  GAME    -------- |||                               ")

name=input("Name : ")   
Player_name=input("Enter your Player name : ")              
email=input("Email : ")
age=int(input("Age : "))
print()
print("=" *50)
print("Check your Details below: ")
print(f" Your Name         is   ->     { name}")
print(f" Your Player Name  is   ->     { Player_name }")
print(f" Your EmailID      is   ->     { email }")
print(f" Your Age          is   ->     { age }")
print("=" *50)

details=input("Enter 'yes' if checked: ")

print()
if(age>=18):
    print("YOU AREELIGIBLE, ENJOY THE QUIZ")
    print()
    print(f"================================================================================================================================")
    print(f"                                                                                                                                ")
    print(f"                                 ********** WELCOME TO THE QUIZ GAME {Player_name }**********                                   ")
    print(f"                                                                                                                                ")
    print(f"================================================================================================================================")
    
    print()
    print(f"                                          ====>    Terms and Conditions    <====                                               ")
    print("Read the Terms and conditions carefully and ACCEPT to proceed further in game ")
    print()
    print("1) Register with accurate personal details; false information leads to disqualification.")
    print("2) Adhere to the quiz rules; cheating or disrupting the game results in immediate disqualification.")
    print("3) You cannot leave the game in the middle.")
    print("4) You can only choose one option : option a) option b) option c) and option d). ")
    print("5) If you cannnot guess the correct answer at once then the score will not be calculated or remained same. ")
    print("6) If you cannot guess the correct answer at once then three chances will be given. ")
    print("7) If you cannot guess the correct answer in the given three chances then the game will be over.")

    guess=input("Enter 'yes' if Accept: " )
    if(guess=="yes" or guess=="Yes"):
        print("Let's get into it ")
        print()
        print(f"=======================================================================================================================")
        print(f"                                               BEST OF LUCK {Player_name}                                                ") 
        print(f"=======================================================================================================================")
        print()
        #---------------------------------------1st question---------------------------------
        print("___________________________________________________")
        print("HOW MANY ELEMEMTS ARE THEIR IN THE PERIODIC TABLE ?")
        print("___________________________________________________")
        print("a.116")
        print("b.118")
        print("c.119")
        print("d.111")
        
        print()
        
        correct_ans=input("Answer : ")
        score=0
        
        if(correct_ans == 'a'):
            score+=10
            print("Correct Answer! You've Scored a Point")
            print("=" *50)
        else:
            print("Try Again")
            print()
            chance=2
            while(chance > 0):
                correct_ans=input("Answer : ")
                print()
                
                if(correct_ans == 'a'):
                    break
                else:
                    print("Try Againn  !!")
                    chance-=1
                   
        print()
        print()            
       
       
       #----------------------------------2nd question----------------------------------------  
        print("____________________________________________")           
        print("WHO IS THE PRESENT CHIEF JUSTICE OF INDIA? ")
        print("___________________________________________")
        print("a. C.Y. CHANDRACHUD")
        print("b. SHAH RUKH KHAN")
        print("c. NARENDRA MODI")
        print("d. AMIT SHAH")
        print()
        correct_ans=input("Answer : ")
        
        if(correct_ans == 'a'):
            score+=10
            print("Correct Answer! You've Scored a Point")
            print("=" *50)
        else:
            print("Try again")
            chance=2
            while(chance > 0):
                correct_ans=input("Answer : ")
                print()
                if(correct_ans == 'b'):
                    print("Next Question")
                    break
                else:
                    print("Try Againn  !!")
                    chance-=1    
        print()
        print()
                    
        
        #---------------------------------------------3rd question--------------------------
        print("_____________________________________")
        print("WHICH ANIMAL BUILDS UP LARGEST EGGS ?")
        print("_____________________________________")
        print("a. ELEPHANT")
        print("b. OSTRICH")
        print("c. HEN")
        print("d. OWL")
        print()
        correct_ans=input("Answer : ")
        
        if(correct_ans == 'b'):
            score+=10
            print("Correct Answer! You've Scored a Point")
            print("=" *50)
        else:
            print("Try again")
            chance=2
            while(chance > 0):
                correct_ans=input("Answer : ")
                print()
                if(correct_ans == 'b'):
                    print("Next Question")
                    break
                else:
                    print("Try Againn  !!")
                    chance-=1
        print()
        print()            
                    
                    
        #----------------------------------4th question-------------------------------------
        print("___________________________________________________")
        print("WHICH IS THE MOST ABDONDENT GAS IN THE ATMOSPHERE ?")
        print("___________________________________________________")
        print("a. OXYGEN ")
        print("b. CARBON DYOXIDE")
        print("c. NITROGEN")
        print("d. METHANE")
        print()
        correct_ans=input("Answer : ")
        
        if(correct_ans == 'c'):
            score+=10
            print("Correct Answer! You've Scored a Point")
            print("=" *50)
          
        else:
            print("Try again")
            chance=2
            while(chance > 0):
                correct_ans=input("Answer : ")
                print()
                if(correct_ans == 'c'):
                    print("Next Question")
                    break
                else:
                    print("Try Againn  !!")
                    chance-=1
        print()
        print()            
                    
                    
                    
        #--------------------------------------5th question----------------------------------
        print("____________________________________________")
        print("WHICH IS THE MOST POPULATED COUNTRY IN ASIA?")
        print("____________________________________________")
        print("a. SRI LANKA")
        print("b. CHINA")
        print("c.INDIA ")
        print("d. PAKISTAN")
        print()
        correct_ans=input("Answer : ")
        
        if(correct_ans == 'b'):
            score+=10
            print("Correct Answer! You've Scored a Point")
            print("=" *50)
        else:
            print("Try again")
            chance=2
            while(chance > 0):
                correct_ans=input("Answer : ")
                print()
                if(correct_ans == 'b'):
                    print("Next Question")
                    break
                else:
                    print("Try Againn  !!")
                    chance-=1
        print()
        print()            
                    
                    
        #--------------------------------------6th question----------------------------------
        print("_____________________________")
        print("HOW MANY DAYS ARE IN A WEEK ?")
        print("_____________________________")
        print("a. 5")
        print("b. 6")
        print("c. 7")
        print("d. 8")
        print()
        correct_ans=input("Answer : ")
        
        if(correct_ans == 'c'):
            score+=10
            print("Correct Answer! You've Scored a Point")
            print("=" *50)
        else:
            print("Try again")
            chance=2
            while(chance > 0):
                correct_ans=input("Answer : ")
                print()
                if(correct_ans == 'c'):
                    print("Next Question")
                    break
                else:
                    print("Try Againn  !!")
                    chance-=1
        print()
        print()
        
        
        #------------------------------------------7th question-----------------------------------
        print("_________________________________________________")
        print("WHICH ANIMAL IN THE SOLAR SYSTEM IS THE HOTTEST ?")
        print("_________________________________________________")
        print("a. SUN")
        print("b. MOON")
        print("c. MERCURY")
        print("d. VENUS")
        print()
        correct_ans=input("Answer : ")
        
        if(correct_ans == 'd'):
            score+=10
            print("Correct Answer! You've Scored a Point")
            print("=" *50)
        else:
            print("Try again")
            chance=2
            while(chance > 0):
                correct_ans=input("Answer : ")
                print()
                if(correct_ans == 'd'):
                    print("Next Question")
                    break
                else:
                    print("Try Againn  !!")
                    chance-=1
        print()               
        # print("Your total Score is :" , score)            
        print()
        print()
    
   
    
    else:
        print("Exiting !")
        print("Please Accept the Terms and conditions to play.")
            
           
else:
    print("Sorry! You are not Eligible")

print()

print(f"-------------------------------------------------------------------------------------------------------------------------------------")
print(f"-------------------------------------------------------------------------------------------------------------------------------------")      
print(f"                                                       CERTIFICATE                                                                   ") 
print(f"                                                           of                                                                        ")   
print(f"                                                       APPRECIATION                                                                  ")  
print(f"                                               __________________________                                                            ")    
print(f"                       {Player_name} has successfully completed the QUIZ GAME, scoring {score} /70 points                            ")
print()
print(f"                                            HOPE YOU HAD FUN PLAYING  !!!!                                                           ")
print()
print(f"                                                jOIN US SOON !!!                                                                     ")
print()                                                 
print(f"                                                THANKYOU {name} :)                                                                   ")
print()
print(f"-------------------------------------------------------------------------------------------------------------------------------------")
print(f"-------------------------------------------------------------------------------------------------------------------------------------")    
    
    
    
    
    









