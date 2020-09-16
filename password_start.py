import platform, os, sys, subprocess
from bs4 import BeautifulSoup


class Pip:
    """This is the handler for quiet pip installs"""
    def install(package):
        """Use pip to install a package through a script quietly"""
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, "-q"])

    def uninstall(package):
        """Use pip to uninstall through as subprocess script quietly"""
        subprocess.check_call([sys.executable, "-m", "pip", "uninstall", package, "-q"])


# Intro Stuff
print("xxxXXXX   Welcome to the Password-Tool Setup   XXXXxxx")
print("First I need to collect a bunch of info from your computer")


def collect_info():
    """This is used to collect and validate info from the user about their python versioon"""
    try:
        # Collect The Python Version
        print("Collecting Python Version ...")
        python_version = platform.python_version()
        print("Collected.")

        # Report My Findings to the Owner for confirmation
        query = f"Is Your Python Version Python {python_version}? (y/n):  "
        query = input(query)

        if query == "y":
            # Move on To the Next Phase
            print("Ok, Moving On ...")
            return python_version

        elif query == "n": # If I am Wrong (I doubt that, but It happens)

            query = input("Ok, What Is Your Python Version?  ")
            if int(query.replace(".", "")) < 300: # If the input is python2.x.x 
                # Warn user about the lack of support and testing
                print("Whoa There, You are using python2.x.x.")
                print("Well, I didn't add support for python2.x.x")

                query == input("Do you still want to go on? (y/n)")
                if query == "y":
                    print("Ok, If it glitches, Don't come crying")
                    print("Moving on ...")
                    python_version = query
        
                elif query == "n":
                    print("I respect your decision")
                    quit()

                else:
                   print("I take that as a yes")
                   print("Moving on ...")
                   python_version = query
        else:
            print("I see what You Tried to do, Sneak, if only it worked")
            print("Now we are going to do it all over again ... ")
            print("Mwahahahahahaha ...")
            collect_info()

    except:
        print("Oookay, so that didn't go well, skipping that ... ")
    finally:
        return python_version

print("\n\n")

# Turn it into an Integer for future processing
python_version = collect_info()
python_version = python_version.replace(".", "", 2)
python_version = int(python_version)



print("Now I Need To Do Some Checking ... ")
need_to_install = []

# Check If bs4 Beautiful Soup is installed
print("Checking bs4 BeautifulSoup exists ...")
try:
    from bs4 import BeautifulSoup
    print("Nice")
except ModuleNotFoundError:
    print("bs4 BeautifulSoup needs to be installed")
    need_to_install.append("bs4")

# Check If requests Needs to be Installed
print("Checking if requests exists ... ")
try:
    import requests
    print("Nice")
except ModuleNotFoundError:
    print("requests needs to be installed")
    need_to_install.append("requests")
except:
    print("Whoa There, It appears that your requests module is broken")
    print("I will try uninstalling requests ...")
    pip_uninstall("requests")
    print("I will install it later")
    
# Check if PyQt5 needs to be installed
print("Checking if PyQt5 exists ... ")
try:
    import small
    print("Nice")
except ModuleNotFoundError:
    print("PyQt5 needs to be installed")
    need_to_install.append("PyQt5")

if len(need_to_install) > 0:
    print("Ok, So You Appear to Be Missing Stuff, So I am Going to Install it for You")
    comma = ","
    print(f"I Will Install {comma.join(need_to_install)}")

    if python_version < 380:
        pass
    for package in need_to_install:
        print(f"Installing {package}...")
        pip_install(package)
        print(f"Package Installed")


print("Well, So Long, and Enjoy My App ...")