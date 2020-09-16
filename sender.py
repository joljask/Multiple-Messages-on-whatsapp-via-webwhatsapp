import pyautogui as run
import keyboard
import time
from colorama import init, Fore

sizeWidth = str(run.size().width)
sizeHeight = str(run.size().height)
finalSize = sizeWidth + "x" + sizeHeight
init()
print(Fore.RED + "           _ - - _ ")
print("         /         \     ---------------     |\         |    |---\       ---------------     |----------     ")
print("        /            \   |                   |  \       |    |    \      |                   |         |   ")
print("        \                |                   |    \     |    |     \     |                   |         |  ")
print("          \              |                   |     \    |    |      \    |                   |----------        ")
print("            \            |---------------    |      \   |    |       /   |--------------     |\   ")
print("              \          |                   |       \  |    |      /    |                   |   \  ")
print("                \_       |                   |        \ |    |     /     |                   |      \ ")
print("       \_        /       ---------------     |         \|    |---/       |--------------     |        \ ")
print("         - _ _ -")
print("\033[36m" + "                                                                     Created By - JOLLY          ")
print('\033[31m' + "Size of screen is " + finalSize)
msg = input("Enter your message  :  ")
count = int(input("how many times do you want to send the message? "))
print("OPTIONAL  :   Do you want to go for advance setting to send message according to the time interval? (DEFAULT time interval is 1 sec.)")
adv = input("Y/N ?  : ")
timeInterval = 1
if adv.lower() == "y" or adv.lower() == "yes":
    print("Do you want send message in [SECONDS],[MINUTES],[HOUR]")
    print("Enter 'S' for SECONDS")
    print("Enter 'M' for MINUTES")
    print("Enter 'H' for HOURS")
    timeIntervalPreference = input("S/M/H ? ")


    if timeIntervalPreference.lower() == "s":
        timeInterval = int(input("Enter the value in seconds : "))
    if timeIntervalPreference.lower() == "m":
        timeInterval = int(input("Enter the value in minutes  : "))
        timeInterval = timeInterval * 60
    if timeIntervalPreference.lower() == "h":
        timeInterval = int(input("Enter the value in hour  : "))
        timeInterval = timeInterval * 3600

elif adv.lower() == "n" or adv.lower() == "no":
    print("You are proceeding with default settings.")
    print("Thank You")
else:
    print("Wrong Input")
print("Time Interval = " + str(timeInterval) + "seconds")
run.alert('Place the cursor in the position and hit "ENTER" key')


def getPosition():
    var = 1
    while var == 1:

        if keyboard.is_pressed('enter'):
            print("Enter")
            break
        print(run.position())
        cursorPositionX = run.position().x
        cursorPositionY = run.position().y
        return cursorPositionX, cursorPositionY
'''
    Typing cursor
'''

typingCursorPosition = getPosition()
i = 0
print("position" + str(typingCursorPosition))
while i < count:
    run.click(typingCursorPosition)
    print(run.write(msg))
    print("Message : " + msg)
    time.sleep(timeInterval)
    run.press('enter')
    print("Enter key executed.")
    print("")
    print("########################### MESSAGE SENT " + str(count) + " TIMES ###########################")
    i = i + 1