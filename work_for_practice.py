import datetime

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.spVoice")
    speak.speak(str)

year = input("Enter the age\n   OR    \nEnter the birth year\n")
loen=len(year)
current_year = datetime.datetime.now().strftime("%Y")
try:
    if loen ==4:
        print("you have entered the year of birth :",year)
        speak("you have entered the year of birth ")
        speak(year)
        yyears = int(current_year) - int(year)
        print(f"\n\nyou are {yyears} year old")
        print(f"you are {yyears} year old")
        print(f"you are {yyears} year old\n\n")
        speak(f"you are {yyears} year old {yyears} year old {yyears} year old")

        print("Thank for using this program")
        speak("Thank for using this program")
        print("If you want to know your age in any particular year")
        speak("If you want to know your age in any particular year")
        xx=input("Press '1': To know age in year\n\n")
        if xx == '1':

            k='c'
            while (k is not "q"):
                inp_agesss = input("Enter the year in which you want to check your age(ex-2200,2022,2300,2045,1999)\n\n")
                if int(inp_agesss) < int(current_year):
                    new_age = yyears - (int(current_year) - int(inp_agesss))
                    print(f"you will be of {new_age} in {inp_agesss}")
                    speak(f"you will be of {new_age} in {inp_agesss}")
                    k = input("For checking more year \nPress 'c' to continue\nPress 'q' to quit\n\n")

                elif int(inp_agesss) > int(current_year):
                    so_so = int(inp_agesss) - int(current_year) + yyears
                    print(f"you will be of {so_so} year in {inp_agesss}")
                    speak(f"you will be of {so_so} year in {inp_agesss}")
                    if so_so > 100:
                        print("You can be oldest person in india as age :\n\n",so_so)
                        speak("You can be oldest person in india as age :\n\n",so_so)
                    elif so_so < 100:
                        print("your age is:",so_so)
                        speak("your age is:",so_so)
                        k = input("For checking more year \nPress 'c' to continue\nPress 'q' to quit\n\n")



        else:
            print("Okk no Problem")
            speak("Okk no Problem")

    elif loen == 2:
        print("you have entered you age:",year)
        speak("you have entered you age")
        speak(year)
        birth_year = int(current_year) -  int(year)
        print(f"\n\nyour birth year is {birth_year}\n\n")

        print("Thank for using this program")
        speak("Thank for using this program")
        print("If you want to know your age in any particular year")
        speak("If you want to know your age in any particular year")
        xx = input("Press '1': To know age in year\n\n\n")
        if xx == '1':

            k = 'c'
            while (k is not "q"):
                inp_agesss = input("Enter the year in which you want to check your age(ex-2200,2022,2300,2045,1999)\n\n")
                if int(inp_agesss) < int(current_year):
                    new_age = int(year) - (int(current_year) - int(inp_agesss))
                    print(f"you will be of {new_age} in {inp_agesss}")
                    k = input("For checking more year \nPress 'c' to continue\nPress 'q' to quit\n\n")

                elif int(inp_agesss) > int(current_year):
                    so_so = (int(inp_agesss) - int(current_year)) + int(year)
                    print(f"you will be of {so_so} year in {inp_agesss}")
                    if so_so > 100:
                        print("You can be oldest person in india as age :\n\n", so_so)
                    elif so_so < 100:
                        print("your age is:", so_so)
                        k = input("For checking more year \nPress 'c' to 'continue'\nPress 'q' to 'quit'\n\n")


except ArithmeticError:
    print("You have put some wrong input")

else:
    print("great you are at end")

finally:
    print("this is just formailty")