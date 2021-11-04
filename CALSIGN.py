import sys

on_menu = False
on_vulture = False
null_fix = False
on_null = False

class FileCorruption(Exception):
    pass

def sys_start():
    print("(**%PROTOCAL01011010%**)")
    print("[0][1][EXEC START][1][0]")
    print("")
    print("")
    print("EMTECH EST 1984")
    print("")
    print("<|||||||||||||>")
    print("_______________")
    print("")
    print("CALSIGN OS V3.4")
    print("_____________________________________________")

def sys_lock():
  print("Incorrect user key")
  print("System locked for 12 Days")
  print("Shutting Down System........")
  print("________________________")
  sys.exit()

sys_start()

user_key = input("Please enter user key: ")

if user_key == "Telebeetle22":
    print("Access granted")
    on_menu = True
else:
    sys_lock()

apps_list = ["Vulture Console", "null", "Unknown", "Notepad"]

while on_menu == True:
    print("Available Apps: " + str(apps_list))
    app_chosen = input("Choose an app: ")

    if app_chosen == "Vulture Console":
        print("Opening VULTURE")
    elif app_chosen == "null":
        if null_fix == True:
            pass
        else:
            print("_________________________________________________________SYSTEM SHUTDOWN_________________________________________________________")
            print("")
            print("##################################################0x00000012 TRAP_CAUSE_UNKNOWN##################################################")
            print("_________________________________________________________________________________________________________________________________")
            print("")
            raise FileCorruption
    elif app_chosen == "Notepad":
        print("Notepad was unable to open. STOP CODE: ERROR_OPEN_FAILED")
    else:
        print("App is either unavailable or you spelled it wrong. Case sensitive")
