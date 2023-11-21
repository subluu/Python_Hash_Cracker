#Initializing Imports
import time
import hashlib

#Global Variables
count = 0
shout = 0
hashAlgos = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
preferences = ['Your Own Wordlist', 'Default Wordlists']
choices = ['1', '2', '3', '4', '5', '6']

#Printing the Intro
print('\n[!] Welcome, to the Hash Cracker. [!]\n')
time.sleep(.05)

#Listing Wordlist Choices
for pref in preferences:
    time.sleep(.05)
    shout += 1
    print(str(shout) + ". " + pref)

#Recieving User Input
preferance = input("\n[+] What preferance would you like to use? ")
print('\n')

if preferance == "1":
    for algo in hashAlgos:
        time.sleep(.05)
        count += 1
        print(str(count) + ". " + algo)
    response = input("\n[+] What hashing algorithm would you like to use? ")
    if response == "1":
        wordlist = input(r"[+] Please input the absolute path of the wordlist you would like to use.. ")
        hashfile = input(r"[+] Please input the absolute path of the hashfile you would like to use.. ")
        print("\n")
        with open(wordlist, 'r', errors="ignore") as words, open(hashfile, 'r', errors="ignore") as hashes:
            parse_lines = hashes.read().splitlines()
            for passwd in words:
                for l in parse_lines:
                    if hashlib.md5(passwd.strip().encode()).hexdigest() == l:
                        print(f"[!]Password Found: {passwd}")
    elif response == "2":
        wordlist = input(r"Please input the absolute path of the wordlist you would like to use.. ")
        hashfile = input(r"Please input the absolute path of the hashfile you would like to use.. ")
        print("\n")
        with open(wordlist, 'r', errors="ignore") as words, open(hashfile, 'r', errors="ignore") as hashes:
            parse_lines = hashes.read().splitlines()
            for passwd in words:
                for l in parse_lines:
                    if hashlib.sha1(passwd.strip().encode()).hexdigest() == l:
                        print(f"[!]Password Found: {passwd}")
    elif response == "3":
        wordlist = input(r"Please input the absolute path of the wordlist you would like to use.. ")
        hashfile = input(r"Please input the absolute path of the hashfile you would like to use.. ")
        print("\n")
        with open(wordlist, 'r', errors="ignore") as words, open(hashfile, 'r', errors="ignore") as hashes:
            parse_lines = hashes.read().splitlines()
            for passwd in words:
                for l in parse_lines:
                    if hashlib.sha224(passwd.strip().encode()).hexdigest() == l:
                        print(f"[!]Password Found: {passwd}")
    elif response == "4":
        wordlist = input(r"Please input the absolute path of the wordlist you would like to use.. ")
        hashfile = input(r"Please input the absolute path of the hashfile you would like to use.. ")
        print("\n")
        with open(wordlist, 'r', errors="ignore") as words, open(hashfile, 'r', errors="ignore") as hashes:
            parse_lines = hashes.read().splitlines()
            for passwd in words:
                for l in parse_lines:
                    if hashlib.sha256(passwd.strip().encode()).hexdigest() == l:
                        print(f"[!]Password Found: {passwd}")
    elif response == "5":
        wordlist = input(r"Please input the absolute path of the wordlist you would like to use.. ")
        hashfile = input(r"Please input the absolute path of the hashfile you would like to use.. ")
        print("\n")
        with open(wordlist, 'r', errors="ignore") as words, open(hashfile, 'r', errors="ignore") as hashes:
            parse_lines = hashes.read().splitlines()
            for passwd in words:
                for l in parse_lines:
                    if hashlib.sha3_384(passwd.strip().encode()).hexdigest() == l:
                        print(f"[!]Password Found: {passwd}")
    elif response == "6":
        wordlist = input(r"Please input the absolute path of the wordlist you would like to use.. ")
        hashfile = input(r"Please input the absolute path of the hashfile you would like to use.. ")
        print("\n")
        with open(wordlist, 'r', errors="ignore") as words, open(hashfile, 'r', errors="ignore") as hashes:
            parse_lines = hashes.read().splitlines()
            for passwd in words:
                for l in parse_lines:
                    if hashlib.sha512(passwd.strip().encode()).hexdigest() == l:
                        print(f"[!]Password Found: {passwd}")