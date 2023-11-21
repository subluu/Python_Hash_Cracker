#Initializing Imports
import time
import hashlib
import os

#Global Variables
count = 0
hashAlgos = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
preferences = ['Your Own Wordlist', 'Default Wordlists']
choices = ['1', '2', '3', '4', '5', '6']


#Printing the Intro
print('\nWelcome, to the Hash Cracker.\n')
time.sleep(.05)

#Listing Wordlist Choices
for pref in preferences:
    time.sleep(.05)
    shout += 1
    print(str(shout) + ". " + pref)

#Recieving User Input
preferance = input("\nWhat preferance would you like to use? " )
print('\n')

if preferance == "1":
    for algo in hashAlgos:
        time.sleep(.05)
        count += 1
        print(str(count) + ". " + algo)
    response = input("\nWhat hashing algorithm would you like to use? ")
    if response not in choices or preferance not in choices:
        raise ValueError("Please choose a supported number from the choice list.")
    wordlist = input("Please input the absolute path of the wordlist you would like to use.. ")
    print(wordlist)


if preferance == "2":
    for algo in hashAlgos:
        time.sleep(.05)
        count += 1
        print(str(count) + ". " + algo)
    response = input("\nWhat hashing algorithm would you like to use? ")
    print('\n')
    if response not in choices or preferance not in choices:
        raise ValueError("Please choose a supported number from the choice list.")

