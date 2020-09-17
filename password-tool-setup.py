# import tools, mostly file management tools for smooth installation process
import platform, sys, subprocess, shutil, os

# Setting pip up
class Pip:
    """This is the handler for quiet pip installs"""
    def ___init__(self):
        pass
    def install(self, package):
        """Use pip to install a package through a script quietly"""
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, "-q"])

    def uninstall(self, package):
        """Use pip to uninstall through as subprocess script quietly"""
        subprocess.check_call([sys.executable, "-m", "pip", "uninstall", package, "-q"])


# Intro Stuff
print("\n")
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
        print(f"Your Python Version is {python_version}")

        # Write the Python Version to the given file
        f = open("python_version.txt", "w")
        f.write(python_version)

    except:
        print("Oookay, so that didn't go well, skipping that ... ")
    finally:
        # Close the file and return the python version
        f.close()
        return python_version

print("\n")

# Turn it into an Integer for future processing
python_version = collect_info()
python_version = python_version.replace(".", "", 2)
python_version = int(python_version)


print("Now I Need To Do Some Checking ... ")
# Setting pip up
pip = Pip()
need_to_install = []

# Check If bs4 Beautiful Soup is installed
print("Checking bs4 BeautifulSoup exists ...")
try:
    from bs4 import BeautifulSoup
    print("Nice")
    print()
except ModuleNotFoundError:
    print("bs4 BeautifulSoup needs to be installed")
    need_to_install.append("bs4")

# Check If requests Needs to be Installed
print("Checking if requests exists ... ")
try:
    import requests
    print("Nice")
    print()
except ModuleNotFoundError:
    print("requests needs to be installed")
    need_to_install.append("requests")
    
# Check if PyQt5 needs to be installed
print("Checking if PyQt5 exists ... ")
try:
    import PyQt5
    print("Nice")
    print()
except ModuleNotFoundError:
    print("PyQt5 needs to be installed")
    need_to_install.append("PyQt5")

if len(need_to_install) > 0:
    print("Ok, So You Appear to Be Missing Stuff, So I am Going to Install it for You")
    comma = ","
    print(f"I Will Install {comma.join(need_to_install)}")

    for package in need_to_install:
        print(f"Installing {package}...")
        pip.install(package)
        print(f"{package} Installed")

print("Setting Up Desktop Files ...")
shutil.move(f"{os.getcwd()}/backend.py", "usr/share/Password-Tool/backend.py")
shutil.move(f"{os.getcwd()}/frontend.py", "usr/share/Password-Tool/frontend.py")
shutil.move(f"{os.getcwd()}/main.py", "usr/share/Password-Tool/frontend.py")
shutil.move(f"{os.getcwd()}/passwords.txt", "usr/share/Password-Tool/passwords.txt")
shutil.move(f"{os.getcwd()}/run_password_tool.sh", "usr/share/Password-Tool/run_password-Tool.sh")
#shutil.move(f"{os.getcwd()}/Password-Tool.svg", "/usr/share/applications")
#shutil.move(f"{os.getcwd()}/Password-Tool.desktop", "/usr/share/applications")
print("Well, So Long, and Enjoy My App ...")

