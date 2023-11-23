# Import necessary libraries
import time
import hashlib
import os

# Function to prompt the user to choose a hashing algorithm
def choose_algorithm():
    print("\nChoose a hashing algorithm:")
    for count, algo in enumerate(hashAlgos, 1):
        print(f"{count}. {algo}")
    response = input("\n[+] What hashing algorithm would you like to use? ")
    return int(response) if response.isdigit() and 1 <= int(response) <= len(hashAlgos) else None

# Function to crack the password hash
def crack_password(algorithm_index):
    if algorithm_index is not None:
        # Input wordlist and hashfile names from the user
        wordlist = input("[+] Please input the wordlist you would like to use: ")
        hashfile = input("[+] Please input the hashfile you would like to use: ")
        print("\n")
        # Select the appropriate hashing function based on the user's choice
        hash_function = hash_functions[algorithm_index - 1]
        
        # Open and read the wordlist and hashfile to compare hashes
        with open(wordlist, 'r', errors="ignore") as words, open(hashfile, 'r', errors="ignore") as hashes:
            parse_lines = hashes.read().splitlines()
            for passwd in words:
                for l in parse_lines:
                    # Compare the hash of each word in the wordlist with hashes in the hashfile
                    if hash_function(passwd.strip().encode()).hexdigest() == l:
                        print(f"[!] Password Found: {passwd}")

def encrypt_files(algorithm_index):
    if algorithm_index is not None:
        desktop = os.path.expanduser(r"~/Desktop")
        encfile = input("[+] Please input the word file you would like to encrypt: ")
        filename = input("[+] Please name your encrypted file. ")
        print('\n')
        hash_function = hash_functions[algorithm_index - 1]
        with open(encfile, 'r', errors="ignore") as words, open(desktop + r'/' + filename + r'.txt', 'a') as finalfile:
            parse_lines = words.read().splitlines()
            for l in parse_lines:
                print(l)
                    

# List of available hashing algorithms
hashAlgos = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
# Corresponding hash functions
hash_functions = [
    hashlib.md5,
    hashlib.sha1,
    hashlib.sha224,
    hashlib.sha256,
    hashlib.sha384,
    hashlib.sha512
]

# Welcome message
print('\n[!] Welcome to the Hash Manager. [!]\n')
time.sleep(0.05)

# Default preference value
preference = 1

# Display the choice for wordlist
print("""1. Decrypt
2. Encrypt""")

# Loop for user interaction
while preference == 1:
    preference_input = input("\n[+] What preference would you like to use? ")

    if preference_input == "1":
        # Allow user to choose an algorithm and crack the password hash
        algorithm_choice = choose_algorithm()
        crack_password(algorithm_choice)
    elif preference_input == "2":
        algorithm_choice = choose_algorithm()
        encrypt_files(algorithm_choice)
        # Ask if the user wants to continue cracking hashes
        choice = input("\nWould you like to decrypt anymore hashes? (y/n): ")
        if choice.lower() != 'y':
            break
    else:
        # If the user enters an invalid preference, exit the loop
        print("Invalid preference. Exiting.")
        break
