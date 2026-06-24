# Define weather conditions
the_weather_is_good = True
the_weather_is_bad = False
the_weather_is_sunny = True

def go_for_a_walk():
    print("Going for a walk!")

def go_to_a_theater():
    print("Going to a theater!")

def have_lunch():
    print("Having lunch!")

def stay_home():
    print("Staying home!")

def go_to_a_restaurant():
    print("Going to a restaurant!")

def wear_sunglasses():
    print("Wearing sunglasses!")

def eat_a_sandwich():
    print("Eating a sandwich!")

def go_to_the_theater():
    print("Going to the theater!")

def go_shopping():
    print("Going shopping!")

if the_weather_is_good:
    go_for_a_walk()
else:
    go_to_a_theater()
have_lunch()


if the_weather_is_bad:
    stay_home()     
else:
    go_to_a_restaurant()


if the_weather_is_sunny:
    wear_sunglasses()


def safiye():
    print("Safiye is going for a walk.")

alles_goed_gaat = True

if alles_goed_gaat:
    safiye()
else:
    print("Safiye is staying home.")
    

#Nested if-else statements so we can check multiple conditions

nice_restaurant_is_found = True  # Define the variable before using it

if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    tickets_are_available = True  # Define the variable before using it
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()    

def safiye_is_happy():
    print("Safiye is happy.")
def safiye_is_not_happy():
    print("Safiye is not happy.")    
alle_cursus_is_klaar= True # Define the variable before using it
the_werk_is_done = True

if alle_cursus_is_klaar:
    if the_werk_is_done :
        safiye_is_happy()
    else:
        safiye_is_not_happy()
else:
    safiye_is_not_happy()        

#The elif statement so we can check multiple conditions
# Define a function to check weather conditions
def check_weather_condition(weather_condition):
    if weather_condition == "sunny":
        print("It's sunny outside!")
    elif weather_condition == "rainy":
        print("It's rainy outside!")
    elif weather_condition == "cloudy":
        print("It's cloudy outside!")
    else:
        print("Weather condition is unknown.")

table_is_available = True  # Define the variable before using it
def go_for_lunch():
    print("Going for lunch!")
def play_chess_at_home():
    print("Playing chess at home!")

if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()

def today_is_monday():
    print("Today is monday.")   
def today_is_tuesday():
    print("Today is tuesday.")
def today_is_wednesday():
    print("Today is wednesday.")
def today_is_thursday():
    print("Today is thursday.")
def today_is_friday():
    print("Today is friday.")
def today_is_saturday():
    print("Today is saturday.")
def today_is_sunday():
    print("Today is sunday.")

# Check the day of the week and call the appropriate function
# Assuming the user inputs a number from 1 to 7 for the day of the week
the_day_of_the_week = int(input("Enter the day of the week (1-7): "))

if the_day_of_the_week==1:
    today_is_monday()
elif the_day_of_the_week==2:
    today_is_tuesday()
elif the_day_of_the_week==3:
    today_is_wednesday()
elif the_day_of_the_week==4:
    today_is_thursday()
elif the_day_of_the_week==5:
    today_is_friday()
elif the_day_of_the_week==6:
    today_is_saturday()
elif the_day_of_the_week==7:
    today_is_sunday()
