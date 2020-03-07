import sys, os, datetime, getpass

currentDT = datetime.datetime.now()
user = username = getpass.getuser()

if currentDT.hour > 18:

    command = r"yes n | sudo '/home/" + str(username) + "/adjust_brightness' && exit"

else:

    command = r"yes d | sudo '/home/" + str(username) + "/adjust_brightness' && exit"

os.system("gnome-terminal -e 'bash -c \""+command+";bash\"'")


sys.exit()
