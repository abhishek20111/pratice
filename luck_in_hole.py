import random
import asyncio
import datetime

total_attent = 10
point_player1 = 0
point_player2 = 0
player1_att = 0
player2_att = 0

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)

class game_luck:
    print("First player turn\n")
    # speak("First player turn\n")
    print("This is Guessing game you have to Guess the no")
    # speak("This is Guessing game you have to Guess the no\n")

    def select_random_value():
        dic = []
        for i in range(0,100):
            s = dic.append(i)
            value = random.choice(dic)
        return value


    async def game_begin1():
        while total_attent >= player1_att:
            # speak("Guess the no")
            ss = int(input("Guess the no"))

            if ss > value1:
                player1_att +=1
                # speak("Guess Wrong  Please Guess larger")
                print(f"Guess Wrong\nPlease Guess larger than {value1}")
                print(f"Number of chance left {total_attent - player1_att}")
                await asyncio.sleep(1)

            elif ss < value1:
                player1_att +=1
                # speak("Guess Wrong    Please Guess Smaller")
                print(f"Guess Wrong\nPlease Guess Smaller than {value1}")
                print(f"Number of chance left {total_attent - player1_att}")
                await asyncio.sleep(1)

            elif ss == value1:
                player1_att +=1
                # speak("You entered correct no    Party chia")
                print("You won\nCorrect no you guess")
                print(f"Number of chance left {total_attent - player1_att}")
                await asyncio.sleep(1)

    async def game_begin2():
        while total_attent >= player2_att:
            # speak("Guess the no")
            ss = int(input("Guess the no"))

            if ss > value2:
                player2_att +=1
                # speak("Guess Wrong  Please Guess larger")
                print(f"Guess Wrong\nPlease Guess larger than {value1}")
                print(f"Number of chance left {total_attent - player2_att}")
                await asyncio.sleep(1)

            elif ss < value2:
                player2_att +=1
                # speak("Guess Wrong    Please Guess Smaller")
                print(f"Guess Wrong\nPlease Guess Smaller than {value1}")
                print(f"Number of chance left {total_attent - player2_att}")
                await asyncio.sleep(1)

            elif ss == value2:
                player2_att +=1
                # speak("You entered correct no    Party chia")
                print("You won\nCorrect no you guess")
                print(f"Number of chance left {total_attent - player2_att}")
                await asyncio.sleep(1)



a1= input("Enter your name")
a1 = game_luck()
value1 = a1.select_random_value()


a2 = input("Enter your 2 player name")
a2 = game_luck()
value2 = a2.select_random_value()

async def main()
    task1 = asyncio.create_task(game_luck(ga))