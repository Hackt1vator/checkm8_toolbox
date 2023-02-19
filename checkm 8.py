# import system functions
import os
import time
import re
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from subprocess import run
import subprocess
# load images in Tkinter python
from PIL import ImageTk, Image
# web
import webbrowser
# sounds
# from pygame import mixer

# Designed and developed by @ios_euphoria

# frame settings
root = tk.Tk()
frame = tk.Frame(root, width="500", height="250")
frame.pack(fill=BOTH,expand=True)
#tk.Entry(root).pack(fill='x')

# uses current directory to load the image file for the icon
root.iconphoto(False, tk.PhotoImage(file='Palera1n-icon.png'))

LAST_CONNECTED_UDID = ""
LAST_CONNECTED_IOS_VER = ""

def startcheckra1n():
    global LAST_CONNECTED_UDID, LAST_CONNECTED_IOS_VER

    root.iconphoto(False, tk.PhotoImage(file='checkra1nicon.png'))
    messagebox.showinfo("Enter DFU Mode",
                        "Get ready...\n\nFirst, press Ok button.\n\nThen, put the device into DFU mode. The jailbreak will automatically complete afterwards.")

    print("Loading jb script...")
    os.system("./checkra1n/checkra1n -c -V -E")
    print("Ran jb script.\n")
    # show message to jb
    messagebox.showinfo("Jailbreak Ran", "Jailbreak done!\n\nNow bypass")
    root.iconphoto(False, tk.PhotoImage(file='checkra1nicon.png'))

def showDFUMessage():
    messagebox.showinfo("Step 1","Put your iDevice into DFU mode.\n\nClick Ok once its ready in DFU mode to proceed.")
    
def startpalera1n():
    global LAST_CONNECTED_UDID, LAST_CONNECTED_IOS_VER

#iOSVER = str(LAST_CONNECTED_IOS_VER)
    global LAST_CONNECTED_UDID, LAST_CONNECTED_IOS_VER
    # step 1 technically
    print("Searching for connected device...")
    os.system("idevicepair unpair")
    os.system("idevicepair pair")
    os.system("./device/ideviceinfo > ./device/lastdevice.txt")

    time.sleep(2)

    f = open("./device/lastdevice.txt", "r")
    fileData = f.read()
    f.close()

    if ("ERROR:" in fileData):
        # no device was detected, so retry user!
        print("ERROR: No device found!")

        messagebox.showinfo("No device detected! 0x404", "Try disconnecting and reconnecting your device.")
    else:
        # we definitely have something connected...

        # find the UDID
        start = 'UniqueDeviceID: '
        end = 'UseRaptorCerts:'
        s = str(fileData)

        foundData = s[s.find(start) + len(start):s.rfind(end)]
        UDID = str(foundData)
        LAST_CONNECTED_UDID = str(UDID)

        # find the iOS
        # we definitely have something connected...
        start2 = 'ProductVersion: '
        end2 = 'ProductionSOC:'
        s2 = str(fileData)

        foundData2 = s2[s.find(start2) + len(start2):s2.rfind(end2)]
        deviceIOS = str(foundData2)
        LAST_CONNECTED_IOS_VER = str(deviceIOS)

        if (len(UDID) > 38):
            # stop automatic detection
            timerStatus = 0

            print("Found UDID: " + LAST_CONNECTED_UDID)
            messagebox.showinfo("iDevice is detected!", "Found iDevice on iOS " + LAST_CONNECTED_IOS_VER)
        #            cbeginExploit10["state"] = "normal"
        #            cbeginExploit2["state"] = "normal"

        # messagebox.showinfo("Ready to begin!","We are ready to start jailbreak!")

        # cbeginExploit10["state"] = "normal"

        else:
            print("Couldn't find your device")
            messagebox.showinfo("Somethings missing! 0x405", "Try disconnecting and reconnecting your device.")

    #check if theres a valid string to continue to reversing jb
    if(len(LAST_CONNECTED_IOS_VER) < 2):
        showinfo('jailbreak Failed', 'Give me a valid iOS version.')
    else:
        showinfo('Ready to Jailbreak...', 'Hi, iOS '+str(LAST_CONNECTED_IOS_VER)+'. \n\nWe will now attempt to jailbreak iOS '+str(LAST_CONNECTED_IOS_VER)+' Semi-Tethered.')
        print("Starting jailbreak...")
        os.system("idevicepair unpair")
        os.system("idevicepair pair")
        os.system(f"cd ./palera1n/ && ./palera1n.sh --tweaks --semi-tethered {LAST_CONNECTED_IOS_VER}")

        print("Device is jailbroken!\n")
        showinfo('jailbreak Success!', 'Device is now jailbroken!')


def removepalera1n():
    global LAST_CONNECTED_UDID, LAST_CONNECTED_IOS_VER

    # iOSVER = str(LAST_CONNECTED_IOS_VER)
    global LAST_CONNECTED_UDID, LAST_CONNECTED_IOS_VER
    # step 1 technically
    print("Searching for connected device...")
    os.system("idevicepair unpair")
    os.system("idevicepair pair")
    os.system("./device/ideviceinfo > ./device/lastdevice.txt")

    time.sleep(2)

    f = open("./device/lastdevice.txt", "r")
    fileData = f.read()
    f.close()

    if ("ERROR:" in fileData):
        # no device was detected, so retry user!
        print("ERROR: No device found!")

        messagebox.showinfo("No device detected! 0x404", "Try disconnecting and reconnecting your device.")
    else:
        # we definitely have something connected...

        # find the UDID
        start = 'UniqueDeviceID: '
        end = 'UseRaptorCerts:'
        s = str(fileData)

        foundData = s[s.find(start) + len(start):s.rfind(end)]
        UDID = str(foundData)
        LAST_CONNECTED_UDID = str(UDID)

        # find the iOS
        # we definitely have something connected...
        start2 = 'ProductVersion: '
        end2 = 'ProductionSOC:'
        s2 = str(fileData)

        foundData2 = s2[s.find(start2) + len(start2):s2.rfind(end2)]
        deviceIOS = str(foundData2)
        LAST_CONNECTED_IOS_VER = str(deviceIOS)

        if (len(UDID) > 38):
            # stop automatic detection
            timerStatus = 0

            print("Found UDID: " + LAST_CONNECTED_UDID)
            messagebox.showinfo("iDevice is detected!", "Found iDevice on iOS " + LAST_CONNECTED_IOS_VER)
        #            cbeginExploit10["state"] = "normal"
        #            cbeginExploit2["state"] = "normal"

        # messagebox.showinfo("Ready to begin!","We are ready to start jailbreak!")

        # cbeginExploit10["state"] = "normal"

        else:
            print("Couldn't find your device")
            messagebox.showinfo("Somethings missing! 0x405", "Try disconnecting and reconnecting your device.")
    
    #check if theres a valid string to continue to reversing jb
    if(len(LAST_CONNECTED_IOS_VER) < 2):
        showinfo('jailbreak Failed', 'Give me a valid iOS version.')
    else:
        showinfo('Ready to remove Jailbreak...', 'Hi, iOS '+str(LAST_CONNECTED_IOS_VER)+'. \n\nWe will now attempt to remove jailbreak on iOS '+str(LAST_CONNECTED_IOS_VER)+' Semi-Tethered.')
        print("Starting removing jailbreak...")
        os.system("idevicepair unpair")
        os.system("idevicepair pair")
        os.system(f"cd ./palera1n/ && ./palera1n.sh --restorerootfs --tweaks {LAST_CONNECTED_IOS_VER}")


def palera1nC():
    os.system("palera1n -cf")


def bootpalera1nC():
    os.system("palera1n -f")


def buildramdisk():
    global LAST_CONNECTED_UDID, LAST_CONNECTED_IOS_VER

    # iOSVER = str(LAST_CONNECTED_IOS_VER)
    global LAST_CONNECTED_UDID, LAST_CONNECTED_IOS_VER
    # step 1 technically
    print("Searching for connected device...")
    os.system("idevicepair unpair")
    os.system("idevicepair pair")
    os.system("./device/ideviceinfo > ./device/lastdevice.txt")

    time.sleep(2)

    f = open("./device/lastdevice.txt", "r")
    fileData = f.read()
    f.close()

    if ("ERROR:" in fileData):
        # no device was detected, so retry user!
        print("ERROR: No device found!")

        messagebox.showinfo("No device detected! 0x404", "Try disconnecting and reconnecting your device.")
    else:
        # we definitely have something connected...

        # find the UDID
        start = 'UniqueDeviceID: '
        end = 'UseRaptorCerts:'
        s = str(fileData)

        foundData = s[s.find(start) + len(start):s.rfind(end)]
        UDID = str(foundData)
        LAST_CONNECTED_UDID = str(UDID)

        # find the iOS
        # we definitely have something connected...
        start2 = 'ProductVersion: '
        end2 = 'ProductionSOC:'
        s2 = str(fileData)

        foundData2 = s2[s.find(start2) + len(start2):s2.rfind(end2)]
        deviceIOS = str(foundData2)
        LAST_CONNECTED_IOS_VER = str(deviceIOS)

        if (len(UDID) > 38):
            # stop automatic detection
            timerStatus = 0

            print("Found UDID: " + LAST_CONNECTED_UDID)
            messagebox.showinfo("iDevice is detected!", "Found iDevice on iOS " + LAST_CONNECTED_IOS_VER)
        #            cbeginExploit10["state"] = "normal"
        #            cbeginExploit2["state"] = "normal"

        # messagebox.showinfo("Ready to begin!","We are ready to start jailbreak!")

        # cbeginExploit10["state"] = "normal"

        else:
            print("Couldn't find your device")
            messagebox.showinfo("Somethings missing! 0x405", "Try disconnecting and reconnecting your device.")

    # check if theres a valid string to continue to reversing jb
    if (len(LAST_CONNECTED_IOS_VER) < 2):
        showinfo('jailbreak Failed', 'Give me a valid iOS version.')
    else:
        showinfo('Ready to Jailbreak...',
                 'Hi, iOS ' + str(LAST_CONNECTED_IOS_VER) + '. \n\nWe will now attempt to jailbreak iOS ' + str(
                     LAST_CONNECTED_IOS_VER) + ' Semi-Tethered.')
        print("Starting jailbreak...")
        os.system("idevicepair unpair")
        os.system("idevicepair pair")
        os.system(f"cd ./SSHRD_Script/ && ./sshrd.sh {LAST_CONNECTED_IOS_VER}")

        print("Device is jailbroken!\n")
        showinfo('jailbreak Success!', 'Device is now jailbroken!')



def bootramdisk():
    os.system(f"cd ./SSHRD_Script/ && ./sshrd.sh boot")

def ipass():
    os.system("./iPass15_universe_MacOS1.2/palera1n-macos-universal")





def enterRecMode():
    print("Kicking device into recovery mode...")
    os.system("./recovery/enterrecovery.sh")

def exitRecMode():
    print("Kicking device out recovery mode...")
    os.system("./recovery/exitrecovery.sh")

def callback(url):
   webbrowser.open_new_tab(url)

def quitProgram():
    print("Exiting...")
    os.system("exit")
    
def opentwitter():
    webbrowser.open('https://www.twitter.com/laurin2261', new=2)


root.title('checkm 8 toolbox - Made by @laurin2261')
frame.pack()

#set image and resize it
#img2 = Image.open("racoon.png")
#frame2 = PhotoImage(file=imagefilename, format="gif -index 2")
#NewIMGSize2 = img2.resize((120,120), Image.ANTIALIAS)
#new_image2 = ImageTk.PhotoImage(NewIMGSize2)
#label = Label(frame, image = new_image2)
#label.place(x=235, y=10)

#BIG title on program
mainText = Label(root, text="checkm8 toolbox",font=('Helveticabold', 24))
mainText.place(x=170, y=70)

#label
my_label2 = Label(frame,
                 text = "Designed to run on macos")
my_label2.place(x=170, y=130)

#label
my_label3 = Label(frame,
                 text = "ver 1.0")
my_label3.place(x=10, y=220)

cButton1 = tk.Button(frame,
                   text="start checkra1n",
                   command=startcheckra1n,
                   state="normal")
cButton1.place(x=50, y=160)

cButton2 = tk.Button(frame,
                   text="Run palera1n",
                   command=startpalera1n,
                   state="normal")
cButton2.place(x=180, y=160)
cButton3 = tk.Button(frame,
                   text="remove palera1n",
                   command=removepalera1n,
                   state="normal")
cButton3.place(x=295, y=160)
cButton4 = tk.Button(frame,
                   text="enter recovery",
                   command=enterRecMode,
                   state="normal")
cButton4.place(x=10, y=10)
cButton5 = tk.Button(frame,
                 text="exit recovery",
                 command=exitRecMode,
                 state="normal")
cButton5.place(x=380, y=10)
cButton6 = tk.Button(frame,
                   text="build ramdisk",
                   command=buildramdisk,
                   state="normal")
cButton6.place(x=200, y=10)
cButton7 = tk.Button(frame,
                   text="boot ramdisk",
                   command=bootramdisk,
                   state="normal")
cButton7.place(x=50, y=100)
cButton8 = tk.Button(frame,
                   text="palera1n C",
                   command=palera1nC,
                   state="normal")
cButton8.place(x=330, y=100)
cButton9 = tk.Button(frame,
                   text="boot palera1n C",
                   command=bootpalera1nC,
                   state="normal")
cButton9.place(x=10, y=60)
cButton10 = tk.Button(frame,
                   text="start ipass",
                   command=ipass,
                   state="normal")
cButton10.place(x=380, y=60)
#Create a Label to display the link
link = Label(root, text="Made this gui @laurin2261",font=('Helveticabold', 12), cursor="hand2")
link.place(x=165, y=220)
link.bind("<Button-1>", lambda e:
callback("https://twitter.com/laurin2261"))

cbeginExploit2 = tk.Button(frame,
                   text="Twitter",
                   command=opentwitter,
                   state="normal")
cbeginExploit2.place(x=380, y=210)

root.geometry("500x250")

root.resizable(False, False)

root.eval('tk::PlaceWindow . center')


root.mainloop()