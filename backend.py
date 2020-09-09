"""
This is where all the code for managing the password is held
"""
# Import Stuff
import random, requests
from bs4 import BeautifulSoup


def make_password():
    """Generates a Password"""
    # Set the Alphanumeric and extra characters
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 'm', "n", 'o', "p", "q", "r", "s", "t", "u", "v", "w", "x", 'y', "z"]
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
    chars = ["~", '`', "!", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", r"\"", "'", '"', "?", "/", ">", "<", ",","."]

    # Set a Password Length
    passwd_length = random.randint(11, 20) + 1

    # Set a Sequence (randomly generated)
    seq = random.sample(alphabet, len(nums)) + random.sample(nums, len(nums)) + random.sample(chars, len(chars)) + random.sample([letter.upper() for letter in alphabet], len(alphabet))
    passwd = ""

    # Generate the Password by adding a (random) character to the password
    for i in range(1, passwd_length):
        passwd = passwd + str(random.choice(seq))
        i += 1

    # Return the generated sequence
    return passwd


def update_unsafe_passwords_list():
    """Updates the List of Unsafe Passowords by Scraping A Website"""
    try:
        # Empty the unsafe_passwords.passwd file
        f = open("unsafe_passwords.passwd", "w")
        f.truncate()
        f.close()

        # Open it again
        f = open("unsafe_passwords.passwd", "a")

        # Get the Website containing the password information
        response = requests.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")

        # Filter the content
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table", attrs={"class": "wikitable"})
        common_passwords = []

        # Search through the filtered content and get the list
        for row in table.findAll("td", {"align":"left"}):
            if row.text in common_passwords:
                pass
            else:
                common_passwords.append(row.text.strip())

        # Add the list to the unsafe_passwords.text file
        for bad_password in common_passwords:
            if bad_password in f.read():
                pass
            else:
                f.write(f"{bad_password}\n")

    except: # In case it does not work, empty the file
        f.truncate()
        f.close()

    finally: # Close the file
        f.close()


def check_password_strength(password):
    """Checks the Strength of a given password"""
    update_unsafe_passwords_list()

    f = open("unsafe_passwords.passwd", "r")

    safe = True
    unsafe_levels = 0
    # First Check if the unsafe_passwords.passwd file is empty
    data = f.read()
    # If the Thing is empty
    if data == None or "":
        pass
    else:
        """
        Check if the password is in the list of unsafe passwords
        """
        for bad_password in data: # Loop through the data
            if password == bad_password: # If the password is in the list of bad passwords
                safe = False # The password is not safe
                unsafe_levels += 1
                break # End that check


        """
        Check the length of the if password < 10 then it is unsafe
        """
        if len(password) < 10:
            safe = False
            unsafe_levels += 1

        """
        Check if the password contains one or more of:
        A Capital letter
        A Small Letter
        A Number
        A Special Character
         """
        # Set up the necessary variables
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 'm', "n", 'o', "p", "q", "r", "s", "t", "u", "v", "w", "x", 'y', "z"]
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
        chars = ["~", '`', "!", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", r"\"", "'", '"', "?", "/", ">", "<", ",","."]
        uppercase = [letter.upper() for letter in alphabet]

        # Loop through each Alphanumeric character and check if they are in the pasword
        for letter in alphabet:
            if letter in password:
                alphabet = True
                break
        for letter in uppercase:
            if letter in password:
                uppercase = True
                break
        for num in nums:
            if str(num) in password:
                nums = True
                break
        for char in chars:
            if char in password:
                chars = True
                break

        # If all of the necessary variables are equal to true then the password passes
        if uppercase and alphabet and nums and chars == True:
            pass
        else:
            safe = False
            # Just Calculating Some Metrics For the Unsafe Levels
            if not alphabet == True:
                unsafe_levels += 1
            if not uppercase == True:
                unsafe_levels += 1
            if not nums == True:
                unsafe_levels += 1
            if not chars == True:
                unsafe_levels += 1


        """
        Check if the Password is reverse of the list of unsafe passwords
        """
       # Create the Reverse
        rev = password[::-1]
        for bad_password in data: # Loop through the data
            if rev == bad_password: # If the password is in the list of bad passwords
                safe = False
                unsafe_levels +=1
                break # End that check

    return (safe, unsafe_levels)

    
def make_passphrase(phrase):

    """This Turns a phrase Into a Passphrase"""

    # Capitalize the Beginning of the Phrase
    ender = phrase[1:len(phrase)]
    phrase = phrase[0].upper() + ender

    # Then Combine the Stuff into one sequence
    for character in phrase:
        if character == " ":
            phrase = phrase.replace(" ", random.choice(["_", "-"]), 1)

    # Then add a random sequence of numbers at the end
    phrase = phrase + random.choice(["-", ""])
    sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    for num in range(1, random.randrange(1, 5)):
        phrase = phrase + str(random.choice(sequence))
        num += 1
    return phrase

def encrypt(key):
    """Encrypt a String Value using In-House Encryption"""
    key_length = len(key)
    key = list(key)
    for index in range(0, 201):
        try:
            key[index] = ord(key[index])
        except IndexError:
            if index == key_length:
                key.append("end")
            else:
                key.append(random.randrange(1, 10000))
    return key

def decrypt(key):
    """Decrypt the In-House Encrypted Key"""
    tmp = []
    for index in range(0, 201):
        try:
            tmp.append(chr(key[index]))
        except TypeError:
            key = tmp
            break
    tmp = ""
    for char in key:
        tmp += char
    key = tmp
    return key

def write(fname, text):
    """Writes the text to a filename"""
    f = open("fname", 'a')
    f.write(repr(text) + "\n")
    f.close()

def get_file_content(filename):
    """Return's The Content of the file, each line is contained as an item in a list"""
    f = open(filename, "r")
    content = [""]
    index = 0
    for char in f.readlines():
        if char.endswith("\n"):
            content[index] += char.replace("\n", "")
            content.append("")
            index += 1
        else:
            content[index] += char
    return content

