# Ubuntu_Brightness_Fix
Alternative Intel backlight editor if all else fails!

These two scripts were written to automate screen brightness adjustment below the min-value setting on Ubuntu 18.04.
There are many other methods to do this but the ones I have found were unsuccessful for my case. 
Therefore this is yet another alternative for those who may also be struggling with similar issues.

Adjust_Brightness.py writes an interger value to the Intel Brightness file. It has one user input command with two options 
'd' for daytime or 'n' for nightime. These input commands will adjust the screen brightness accordingly and the script is 
easily adaptable to your tastes by changing the input interger values.

Run_Br_Change.py runs the sudo command for the Adjust_Brightness executable and has been set to enter 'd' input for any time 
before 19:00 and 'n' for after. Assuming you are not total night owls turning on your workstations after midnight! 
However these are also easily adjustable.   

The setup is rather tideous, however I will try explain each step as thouroughly as possible.

Step 1: Convert the python scripts into executables with pyinstaller. If you do not have pyinstaller, pip install it.
        Create a non-windowed one-file executable. Eg: pyinstaller -F -w --hidden-import=pkg_resources.py2_warn test.py
        Remember to make sure you open a terminal in the working directory when using the example command.
        
Step 2: Copy the Adjust_Brightness executable from the dist folder to your home{preferable} or choice directory. Create 
        folder for Run_Br_Change, at home{preferable} directory and copy Run_Br_Change executable to this folder.
        
Step 3: Change the Adjust_Brightness executable owernership to root with "sudo chown root:root /path/to/application",
        and set only root capabilities to read and write executable with "sudo chmod 700 /path/to/application". These
        two commands are done due the fact that this executable needs sudo capabilities to edit the Intel Backlight file
        and to make sure the the executable is not vernerable itself it can now only be controlled by root/sudo.
        
Step 4: Give Adjust_Brightness executable sudo capabilites. Run sudo visudo and edit the file by inserting
        "your_username ALL= (root) NOPASSWD: /home/your_username/Adjust_Brightness" underneath "#includedir /etc/sudoers.d". 
        Make sure that the path is the correct path to the executable and press ctrl-x to quit and say yes to commit change.
        
Step 5: In this final step, open the application Startup Application and add the Run_Br_Change executable to it. This will 
        allow it to run on startup and change the screen brightness.
        
I hope this helps those who have been struggling.
Thank your for your patronage, Severian-desu-ga.
        
    

        
