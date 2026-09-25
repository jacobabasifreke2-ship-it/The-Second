prompt = "---Welcome to Trivia Questions---"
prompt += f"\nAnswer the questions correctly and win a price"
prompt += f"\nPlease enter end to terminate the program"
prompt += f"\nEnter Start to begin "

# que1 = ""
# que2 = ""
# que3 = ""

us_ch1 = "Paris"                                                            #the part that
us_ch2 = "Madrid"                                                            #lets the questionee
us_ch3 = "Canada"
us_ch4 = "London"
us_ch5 = "New York"                                                              #change the answers


#develop a function to take answers

answers = []

program = True
answ1 = True
answ2 = True
answ3 = True
answ4 = True
answ5 = True

while program == True:
    
    launch = input(prompt)

    if launch.lower() == "start" or "Start":
      
        while answ1 == True:
            que1 = input("What city is known as the city of lights? ")                                #to change question one

            if que1 != "" or " ":            
                confirm = input("Is that your final answer ")

                if confirm == "yes":
                    print("---Next Question---")
                    break
                    answ1 = False
                elif confirm == "no":
                    continue
                    answ1 = True
                else:
                    print("Please enter a valid answer")
                    continue
                    answ1 = True
            else:
                print("Please enter an answer")
                answ = True

        while answ2 == True:  
            que2 = input("What is the capital of Spain? ")                            #to change question two
        
            if que2 != "" or " ":            
                confirm = input("Is that your final answer ")  

                if confirm == "yes":
                    print("---Next Question---")
                    break
                    answ2 = False
                elif confirm == "no":
                    continue
                    answ2 = True
                else:
                    print("Please enter a valid answer")
                    continue
                    answ2 = True
            else:
                print("Please enter an answer")
                answ2 = True
        
        while answ3 == True:
            que3 = input("Which country is considered the second largest in the world by area? ")               #to change question three
            
            if que3 != "" or " ":            
                confirm = input("Is that your final answer ")

                if confirm == "yes":
                    print("---Next Question---")
                    break
                    answ3 = False
                elif confirm == "no":
                    continue
                    answ3 = True
                else:
                        print("Please enter a valid answer")
                        continue
                        answ3 = True
            else:
                print("Please enter an answer")
                answ = True
            
        while answ4 == True:
                que4 = input("Where is the famous Big Ben building located? ")               #to change question four
            
                if que4 != "" or " ":            
                    confirm = input("Is that your final answer ")

                    if confirm == "yes":
                        print("---Next Question---")
                        break
                        answ4 = False
                    elif confirm == "no":
                        continue
                        answ4 = True
                    else:
                        print("Please enter a valid answer")
                        continue
                        answ4 = True
                else:
                    print("Please enter an answer")
                    answ = True

        while answ5 == True:
            que5 = input("In which city is the empire state building located? ")                                 #to change question five
        
            if que5 != "" or " ":            
                confirm = input("Is that your final answer ")

                if confirm == "yes":
                    # print("---Next Question---")
                    break
                    answ5 = False
                elif confirm == "no":
                    continue
                    answ5 = True
                else:
                    print("Please enter a valid answer")
                    continue
                    answ5 = True
            else:
                print("Please enter an answer")
                answ = True
            

            
        answers = (que1,que2,que3,que4,que5)                                  #the part that involves storing the user answers in a string
        c_answers = (us_ch1,us_ch2,us_ch3,us_ch4,us_ch5)                          #the part that stores the questionees choice of answers
        score = 0

        print(f"\nThese are the the answers you inputed and the correct answer:")
        for answer in answers :
            print(f"Question -:- you inputed {answer}\n")             #the part that displays the answers inputed by the user

        if que1 == us_ch1:
            print("You got question one correct✔️")
        else:
            print(f"You lost question 1❌ \nThe correct answer is {us_ch1}")
        
        if que2 == us_ch2:
            print("You got question two correct✔️")
        else:
            print(f"You lost question 2❌ \nThe correct answer is {us_ch2}")

        if que3 == us_ch3:
            print("You got question three correct✔️")
        else:
            print(f"You lost question 3❌ \nThe correct answer is {us_ch3}")
        
        if que4 == us_ch4:
            print("You got question three correct✔️")
        else:
            print(f"You lost question 4❌ \nThe correct answer is {us_ch4}")
        
        if que5 == us_ch5:
            print("You got question three correct✔️")
        else:
            print(f"You lost question 5❌ \nThe correct answer is {us_ch5}")

        
        for entries in range(len(answers)):

            if c_answers[entries] == answers[entries]:
                score += 20

        print(f"Your total score is = {score}")
        print("Thank you for trying")
        
        restart = ("Enter yes if you Would like to try again")
        restart += (f"\nEnter any other value to exit")

        restart = input(restart)

        if restart == "yes":
            program = True
        else:
            print("Thank you for parcitipating")
            program = False

    elif launch == "end":
        print("Thank you for parcitipating")
        program = False
    else:
        print("Enter a valid option")
        program = True