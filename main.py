from random import randint
import pywhatkit
from sys import exit
import os
import datetime

# Generate random number ffrom 0-99
rand_num = randint(0, 99)

count = 10
# phone_number= input("Enter your phone number: ")

def recurr_func(guesses=[], num=[]):
    # Declare count as global
    global count

    while(count > 0): 
        if not guesses: #if no previous guesses are in the list
            user_guess = int(input("Guess first number.\nRange(0 to 99)\n"))
            compare_size(rand_num, user_guess)        
            compare_nums(user_guess, rand_num,count)
            count -=1 
            print("You have", count , " more chances to go")
            guesses.append(user_guess)    
            num.append(rand_num)
            recurr_func(guesses,num) 

        else:
            user_guess = int(input("Try again.\nRange(0,99)\n "))

            if user_guess in guesses:
                print("Please guess another number.")
                compare_size(rand_num, user_guess)
                count-=1
                print("You have", count , " more chances to go")
                recurr_func(guesses, num) 

            else:
                compare_nums(user_guess,num[0], count)
                guesses.append(user_guess)
                count-=1
                print("You have", count ," to go")
                recurr_func(guesses, num) 
        

def compare_nums(your_guess, my_num, count):
    if (your_guess == my_num):
        send_msg(count)
        print(type(datetime.datetime.now().min))
        print("Final", count)
        exit()

    else:
        return


def compare_size(rand,guess):
    if(rand > guess):
        print("Value is less by: ", rand - guess)

    elif(rand<guess):
        print("Value more by: ", guess - rand)

    else:
        return


def get_phone_number():
    phone_number = input("Enter your phone number: ")

    if(len(phone_number) != 13):
        return input("Please enter a valid phone number: ")

    if(phone_number[:4] != "+254"):
        return input("Country code begins with +254: ")

    return phone_number


# Send whatsapp message *** sendwhatmsg(number,"message", hr, min)
def send_msg(score):
    # hour = datetime.datetime.now().min
    # minute = datetime.datetime.now().min
    message = "You scored", score
    pywhatkit.sendwhatmsg(get_phone_number() , message , 18, 32)


recurr_func()
