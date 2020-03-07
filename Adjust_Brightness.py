import sys, time

setup = input("Enter brightness level, d=150, n=80:   ")

while setup!='d' and setup!='n':
    print("Incorrect input. Enter d or n")
    setup = input("Enter brightness level, d=150, n=80:   ")
    time.sleep(0.2)

def set_brightness(run):
    if run=='d':
        brightness = 150
        with open("/sys/class/backlight/intel_backlight/brightness","w") as bright:
             bright.write(str(brightness))
             bright.close()
             
    elif run=='n':
        brightness = 80
        with open("/sys/class/backlight/intel_backlight/brightness","w") as bright:
             bright.write(str(brightness))
             bright.close()
    
set_brightness(setup)

sys.exit()
