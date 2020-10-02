"""
This is where all the code for managing the password is held
"""
# Import Stuff
import random, requests
from bs4 import BeautifulSoup


class AppTools:
    def __init__(self):
        """The Tools and Variables Needed for the app to function"""
        self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 'm', "n", 'o', "p", "q", "r", "s", "t", "u", "v", "w", "x", 'y', "z"]
        self.nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.chars = ["~", '`', "!", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", r"\"", "'", '"', "?", "/", ">", "<", ",","."]
        self.uppercase = [letter.upper() for letter in self.alphabet]

    def make_password(self):
        """Generates a Password"""

        # Set a Password Length
        passwd_length = random.randint(11, 20) + 1

        # Set a Sequence (randomly generated)
        seq = random.sample(self.alphabet, len(self.alphabet)) + random.sample(self.nums, len(self.nums)) + random.sample(self.chars, len(self.chars)) + random.sample(self.uppercase, len(self.uppercase))
        passwd = ""

        # Generate the Password by adding a (random) character to the password
        for i in range(1, passwd_length):
            passwd = passwd + str(random.choice(seq))
            i += 1

        # Return the generated sequence
        return passwd

    def update_unsafe_passwords_list(self):
        """Updates the List of Unsafe Passowords by Scraping A Website"""
        try:
            # Empty the unsafe_passwords.txt file
            f = open("unsafe_passwords.txt", "w")
            f.truncate()
            f.close()

            # Open it again
            f = open("unsafe_passwords.txt", "a")

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

    def check_password_strength(self, password):
        """Checks the Strength of a given password"""
        self.update_unsafe_passwords_list()

        f = open("unsafe_passwords.txt", "r")

        safe = True
        unsafe_levels = 0
        # First Check if the unsafe_passwords.txt file is empty
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
            contains_alphabet = False
            contains_nums = False
            contains_chars = False
            contains_uppercase = False

            # Loop through each Alphanumeric character and check if they are in the pasword
            for letter in self.alphabet:
                if letter in password:
                    contains_alphabet = True
                    break
            for letter in self.uppercase:
                if letter in password:
                    contains_uppercase = True
                    break
            for num in self.nums:
                if str(num) in password:
                    contains_nums = True
                    break
            for char in self.chars:
                if char in password:
                    contains_chars = True
                    break

            # If all of the necessary variables are equal to true then the password passes
            if contains_uppercase and contains_alphabet and contains_nums and contains_chars == True:
                pass
            else:
                safe = False
                # Just Calculating Some Metrics For the Unsafe Levels
                if contains_alphabet == False:
                    unsafe_levels += 1
                if contains_uppercase == False:
                    unsafe_levels += 1
                if contains_nums == False:
                    unsafe_levels += 1
                if contains_chars == False:
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
    
    def make_passphrase(self, phrase):

        """This Turns a phrase Into a Passphrase"""

        # Capitalize the Beginning of the Phrase
        if len(phrase) == 0 or None:
            return "Empty"
        
        ender = phrase[1:len(phrase)]
        phrase = phrase[0].upper() + ender

        # Then Combine the Stuff into one sequence
        for character in phrase:
            if character == " ":
                phrase = phrase.replace(" ", random.choice(["_", "-"]), 1)

        # Then add a random sequence of numbers at the end
        phrase = phrase + random.choice(["-", ""])

        for num in range(1, random.randrange(1, 5)):
            phrase = phrase + str(random.choice(self.nums))
            num += 1
        return phrase

    
    def encrypt(self, key):
        """Encrypts a String Value using In-House Encryption"""
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

    def decrypt(self, key):
        """Decrypts the In-House Encrypted Key"""
        tmp = []
        for index in range(0, 201):
            try:
                tmp.append(chr(key[index]))
            except TypeError:
                key = tmp
                break
        tmp = ""
        for char in key:
            tmp += char.replace("'", "")
        key = tmp
        return key

    def write(self, fname, text):
        """Writes the text to a filename"""
        f = open(fname, 'a')
        f.write(f"{self.encrypt(repr(text))}\n")
        f.close()

    def get_file_content(self, filename):
        """Returns The Content of the file, each line is contained as an item in a list"""
        try:
            f = open(filename, "r")
        except FileNotFoundError:
            # Error Handling
            f = open(filename, "w")
            f.close()
            f = open(filename, "r")
        content = [""]
        val = None
        for index, char in enumerate(f.readlines()):
            if char.endswith("\n"):
                content[index] += char.replace("\n", "")
                content.append("")
            else:
                content[index] += self.decrypt(char)
        if len(content) == 0 or None or content == [""]:
            val = False
        else:
            val = []
            for key in content:
                if key != "":
                    key = self.decrypt(eval(key))
                    val.append(key)
                else:
                    pass
        if type(val) == list:
            val.reverse()
        return val


