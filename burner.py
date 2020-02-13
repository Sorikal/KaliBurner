#### This tool will help you burn kali linux onto a USB or DVD

import os
import sys
import time
import os.path
import hashlib


### The verify feature will only be available with the Kali-64bit-Installer because I'm lazy

def verify():

    asktoverify = input("Would you like to verify your image? (Y/n) ")
    if "Y" in asktoverify :

        hasher = hashlib.sha256()
        with open(imagename, 'rb') as afile:
            buf = afile.read()
            hasher.update(buf)
        imagehash = hasher.hexdigest()
        print("The image's hash is: " + imagehash)
        time.sleep(2)
        os.system("clear")
        if imageverifiedhash in imagehash :
            print("Your image is correct and isn't modified, continuing script.")
            time.sleep(1)
            os.system("clear")
        else:
            print("Your image is either corrupted or modified, please delete the corrupted/modified\nand restart the script.")
            time.sleep(2)
            exit()


def countdown():
    print("The image will be burned into the device in 10 seconds, Ctrl+C to cancel...")
    time.sleep(1)
    os.system("clear")
    print("The image will be burned into the device in 9 seconds, Ctrl+C to cancel...")
    time.sleep(1)
    os.system("clear")
    print("The image will be burned into the device in 8 seconds, Ctrl+C to cancel...")
    time.sleep(1)
    os.system("clear")
    print("The image will be burned into the device in 7 seconds, Ctrl+C to cancel...")
    time.sleep(1)
    os.system("clear")
    print("The image will be burned into the device in 6 seconds, Ctrl+C to cancel...")
    time.sleep(1)
    os.system("clear")
    print("The image will be burned into the device in 5 seconds, Ctrl+C to cancel...")
    time.sleep(1)
    os.system("clear")
    print("The image will be burned into the device in 4 seconds, Ctrl+C to cancel...")
    time.sleep(1)
    os.system("clear")
    print("The image will be burned into the device in 3 seconds, Ctrl+C to cancel...")
    time.sleep(1)
    os.system("clear")
    print("The image will be burned into the device in 2 seconds, Ctrl+C to cancel...")
    time.sleep(1)
    os.system("clear")
    print("The image will be burned into the device in 1 seconds, Ctrl+C to cancel...")
    os.system("clear")
    print("This process might take some time, please be patient.")

# Dependency stuff 

os.system("clear")

print("Checking for dependencies...")
time.sleep(1)

os.system("clear")

dep = os.path.isfile("dependencies.txt") 

if dep is True:
    print("Dependencies installed, continuing script.")
    time.sleep(2)
    os.system("clear")

else:
    rundependenciesscript = input("The tool will try to automatically install dependencies, continue? (Y/N): ")
    if "Y" in rundependenciesscript :
        os.system("sudo apt-get install figlet wget fdisk git -y")
        file = open("dependencies.txt","w")
        file.write("dependencies installed")
        file.close()
    else:
        print("Stopping script...")
        time.sleep(1)
        exit()

os.system("clear")

os.system("figlet Kali-Burner")
print("")
print("")
print("")
print("")
print("")

arch = input("What architecture is your installation target's CPU?\n\t64bit (1)\n\t32bit (2)\nSelect: ")

if int(arch) == 1:
    arch = "64"
if int(arch) == 2:
    arch = "32"

time.sleep(3)

os.system("clear")

os.system("figlet Kali-Burner")
print("")
print("")
print("")
print("")
print("")

image = input("What image would you like to download?\n\tLive (1)\n\tInstaller (2)\n\tNetinstall (3)\n Select: ")

os.system("clear")

os.system("sudo fdisk -l")
time.sleep(2)

device = input("Enter the name of the device you want to burn the image onto (eg. /dev/sdb): ")

time.sleep(2)
os.system("clear")

if int(image) == 2 and "64" in arch :
    imageverifiedhash = "e399fa5f4aa087218701aff513cc4cfda332e1fbd0d7c895df57c24cd5510be3"
    isimagepresent = os.path.isfile("kali-linux-2020.1-installer-amd64.iso")
    if isimagepresent is False :
        os.system("wget https://cdimage.kali.org/kali-2020.1/kali-linux-2020.1-installer-amd64.iso")
        verify()
    else:
        print("The image is already downloaded, continuing script.")
    time.sleep(1)
    os.system("clear")
        
    imagename = "kali-linux-2020.1-installer-amd64.iso"
    time.sleep(3)
    verify()
    time.sleep(2)
    os.system("clear")
    sure = input("Are you sure you want to burn the image onto the device (This can cause permanent damage to the device) [Y/N]: ")
    if "Y" in sure :
        countdown()
        os.system("sudo dd if=" + imagename + " " + "of=" + device)
        time.sleep(3)
        print("Image has been burned succesfully.")
        exit()

    else:
        exit()
        


if int(image) == 2 and "32" in arch :
    imageverifiedhash = "8b2bf7b6369fb120e42080f2ba57bc8cd7522a4abda1c2715c2b809b7157ae93"
    isimagepresent = os.path.isfile("kali-linux-2020.1-installer-i386.iso")
    if isimagepresent is False :
        os.system("wget https://cdimage.kali.org/kali-2020.1/kali-linux-2020.1-installer-i386.iso")
    else:
        print("The image is already downloaded, continuing script.")
    imagename = "kali-linux-2020.1-installer-i386.iso"
    time.sleep(3)
    sure = input("Are you sure you want to burn the image onto the device (This can cause permanent damage to the device) [Y/N]: ")
    if "Y" in sure :
        countdown()
        os.system("sudo dd if=" + imagename + " " + "of=" + device)
        time.sleep(3)
        print("Image has been burned succesfully.")
        exit()

    else:
        exit()

    
    
if int(image) == 1 and "64" in arch :
    imageverifiedhash = "acf455e6f9ab0720df0abed15799223c2445882b44dfcc3f2216f9464db79152"
    isimagepresent = os.path.isfile("kali-linux-2020.1-live-amd64.iso")
    if isimagepresent is False :
        os.system("wget https://cdimage.kali.org/kali-2020.1/kali-linux-2020.1-live-amd64.iso")
    else:
        print("The image is already downloaded, continuing script.")
    imagename = "kali-linux-2020.1-live-amd64.iso"
    time.sleep(3)
    sure = input("Are you sure you want to burn the image onto the device (This can cause permanent damage to the device) [Y/N]: ")
    if "Y" in sure :
        countdown()
        os.system("sudo dd if=" + imagename + " " + "of=" + device)
        time.sleep(3)
        print("Image has been burned succesfully.")
        exit()

    else:
        exit()

if int(image) == 1 and "32" in arch :
    imageverifiedhash = "401e2398d2931a4b910597e8bdf334bb85e40ef02d4878816f3050179c089fef"
    isimagepresent = os.path.isfile("kali-linux-2020.1-live-i386.iso")
    if isimagepresent is False :
        os.system("wget https://cdimage.kali.org/kali-2020.1/kali-linux-2020.1-live-i386.iso")
    else:
        print("The image is already downloaded, continuing script.")
    imagename = "kali-linux-2020.1-live-i386.iso"
    time.sleep(3)
    sure = input("Are you sure you want to burn the image onto the device (This can cause permanent damage to the device) [Y/N]: ")
    if "Y" in sure :
        countdown()
        os.system("sudo dd if=" + imagename + " " + "of=" + device)
        time.sleep(3)
        print("Image has been burned succesfully.")
        exit()

    else:
        exit()


if int(image) == 3 and "64" in arch :
    imageverifiedhash = "c9ebf2f7d95cd9349daa3441a25fdfd5e0dab522d03a298dbfe046859c3668db"
    isimagepresent = os.path.isfile("kali-linux-2020.1-installer-netinst-amd64.iso")
    if isimagepresent is False :
        os.system("wget https://cdimage.kali.org/kali-2020.1/kali-linux-2020.1-installer-netinst-amd64.iso")
    else:
        print("The image is already downloaded, continuing script.")
    imagename = "kali-linux-2020.1-installer-netinst-amd64.iso"
    time.sleep(3)
    sure = input("Are you sure you want to burn the image onto the device (This can cause permanent damage to the device) [Y/N]: ")
    if "Y" in sure :
        countdown()
        os.system("sudo dd if=" + imagename + " " + "of=" + device)
        time.sleep(3)
        print("Image has been burned succesfully.")
        exit()

    else:
        exit()

if int(image) == 3 and "32" in arch :
    imageverifiedhash = "fab46fd96194bc1172ab7b3882bf4cabf383b261c3192fbf8b8c78e29ab3e08d"
    isimagepresent = os.path.isfile("kali-linux-2020.1-installer-netinst-i386.iso")
    if isimagepresent is False :
        os.system("https://cdimage.kali.org/kali-2020.1/kali-linux-2020.1-installer-netinst-i386.iso")
    else:
        print("The image is already downloaded, continuing script.")
    imagename = "kali-linux-2020.1-installer-netinst-i386.iso"
    time.sleep(3)
    sure = input("Are you sure you want to burn the image onto the device (This can cause permanent damage to the device) [Y/N]: ")
    if "Y" in sure :
        countdown()
        os.system("sudo dd if=" + imagename + " " + "of=" + device)
        time.sleep(3)
        print("Image has been burned succesfully.")
        exit()

    else:
        exit()





