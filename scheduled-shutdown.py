from os import system
from sys import exit
from subprocess import call


call(["shutdown", "/a"])
system('cls')

print()
print(' --- App: Scheduled Shutdown')
print(' # Do you want to continue?')
print()
user_choice = input(' $ [y/n] > ').lower()
if user_choice == 'y':
    system('cls')

    print()
    print(' --- GitHub Repository: https://github.com/Henrique-Coder/scheduled-shutdown')
    print(' # How soon will the computer shut down?')
    print(' Examples: 1m, 60s')
    print()
    timer = input(' $ Timer: ').lower()

    letter = timer[-1]
    number = int(timer[0:-1])

    if letter == 's':
        seconds = number
    elif letter == 'm':
        seconds = number * 60
    else:
        exit()

    call(["shutdown", "/s", "/t", str(seconds)])
    exit()

else:
    exit()
