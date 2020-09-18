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


def collect_info():
    """This is used to collect and validate info from the user about their python versioon"""
    try:
        # Collect The Python Version
        python_version = platform.python_version()

        # Write the Python Version to the given file
        f = open("python_version.txt", "w")
        f.write(python_version)

    except:
        pass
    finally:
        # Close the file and return the python version
        f.close()
        return python_version


# Turn it into an Integer for future processing
python_version = collect_info()
python_version = python_version.replace(".", "", 2)
python_version = int(python_version)


# Setting pip up
pip = Pip()
need_to_install = []

# Check If bs4 Beautiful Soup is installed
try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    need_to_install.append("bs4")

# Check If requests Needs to be Installed
try:
    import requests
except ModuleNotFoundError:
    need_to_install.append("requests")
    
# Check if PyQt5 needs to be installed
try:
    import PyQt5
except ModuleNotFoundError:
    need_to_install.append("PyQt5")

if len(need_to_install) > 0:
    for package in need_to_install:
        pip.install(package)


