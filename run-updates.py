#!/usr/bin/env python3

'''This is a simple house keeping script that does a couple of things:

1) runs apt-get update
2) runs apt-get upgrade
3) runs apt-get dist-upgrade
4) runs apt-get clean
5) runs apt-get autoclean
6) runs apt-get remove
7) runs apt-get autoremove
8) runs updatedb

does any of this need to be jumbled into a script?  Absolutely not. But how else am I going to practice python?
'''

# importing time becuase I like to sleep
# importing os so i can enter cmds
# importing sys so i can do an early exit
import time, os, sys

#clear the screen, to start fresh
os.system('clear')



#Fancy artwork, because I like it
print(' _   _           _       _   _               _   __      _ _ ')
print('| | | |         | |     | | (_)             | | / /     | (_)')
print('| | | |_ __   __| | __ _| |_ _ _ __   __ _  | |/ /  __ _| |_ ')
print('| | | |  _ \ / _  |/ _  | __| |  _ \ / _  | |    \ / _  | | |')
print('| |_| | |_) | (_| | (_| | |_| | | | | (_| | | |\  \ (_| | | |')
print(' \___/|  __/ \__ _|\__ _|\__|_|_| |_|\__  | \_| \_/\__ _|_|_|')
print('      | |                             __/ |                  ')
print('      |_|                            |___/                   ')


#a quick moment to sleep
time.sleep(1)
print("")
print("")
print("Initializing updates...")

#now to run the first part, the update commands
os.system("apt-get update")
os.system("apt-get upgrade")
os.system("apt-get dist-upgrade")

#a quick moment to sleep, just to let things settle down
time.sleep(3)
print("")
print("")
print("Initializing clean-up...")


#now to run the second part, the clean-up commands
os.system("apt-get clean")
os.system("apt-get autoclean")
os.system("apt-get remove")
os.system("apt-get autoremove")


#another quick moment to sleep
time.sleep(3)
print("")
print("")
print("Initializing database update...")


#now runs updatedb to update the database
os.system("updatedb")


#more unnecessary sleep
time.sleep(3)
print("")
print("")


#Ok, now the option to reboot the system or just simply close out of the script
while True:
    print("Would you like to reboot the system?  If so, enter Yes.  Otherwise enter No end updates.")
    answer = input()
    if answer.lower() == 'yes':
        time.sleep(1)
        print("Rebooting...")
        os.system("shutdown -r now")

    elif answer.lower() == 'no':
        time.sleep(1)
        print("Exiting...")
        sys.exit()

    else:
        print("Please enter Yes or No to continue...")
        print("")
        print("")
        time.sleep(3)
        continue