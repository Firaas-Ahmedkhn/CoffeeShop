import pyttsx3 

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 60,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 70,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 90,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


profit = 0    # initially machine has no money


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def check_resources(order_ingredients):
    '''Returns True if order can be made, False if ingredients are insufficient.'''
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            speak("Sorry, it is not available.")
            print("Sorry, it is not available.")
            return False
    return True        


def process_coins():
    '''Returns the total calculated from coins inserted.'''
    speak("Please insert coins.")
    print("Please insert coins.")
    total = int(input("How many 20rs coins?: ")) * 20
    total += int(input("How many 10rs coins?: ")) * 10
    total += int(input("How many 5rs coins?: "))  * 5
    total += int(input("How many 1rs coins?: "))  * 1

    return total



def transaction(money_recieved, drink_cost):
    '''Return True when payment is successful, False if money is insufficient. '''
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)  # using round function to a given precision in decimal digits
        speak(f"Here is Rupees {change} in change.")
        print(f"Here is Rs.{change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        speak("Sorry, that's not enough money. Money refunded. Thank you")
        print("Sorry, that's not enough money. Money refunded. Thank you.")   
        return False 



def make_coffee(drink_name, order_ingredients):
    '''Detuct the required ingredients from the resources.'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    speak(f"Here is your {drink_name}. Thank you. Visit again." )
    print(f"Here is your {drink_name}. Thank you. Visit again.")    



speak("Hi, Welcome to the coffee shop.")
print("Hi, Welcome to the coffee shop.")

is_on = True

while is_on: 
    speak("What would you like to have?")
    choice = input("What would you like to have? (Latte / Espresso / Cappuccino): ")
    if choice == "off":
        is_on = False 
        print("Machine is not working currently.")

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: Rs.{profit}")

    else:
        drink = MENU[choice]        # getting ingredients for coffee
        
        print(drink)
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

