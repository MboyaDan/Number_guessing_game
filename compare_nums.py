def compare_nums(your_guess, my_num):
    if (your_guess == my_num):
        return True
    else:
        return False

        
def is_greater_than(rand, guess):
    if(rand > guess):
        return True
    else:
        return False


def decrement(count):
    count -= 1
    return count


# phone_number = input("Enter your phone number: ")
def get_phone_number(phone_number):
    if(len(phone_number) != 13):
        return input("Please enter a valid phone number: ")

    if(phone_number[:4] != "+254"):
        return input("Country code begins with +254: ")

    return phone_number