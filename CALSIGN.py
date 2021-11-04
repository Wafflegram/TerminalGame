import sys

on_menu = False
on_vulture = False
null_fix = False
on_null = False

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
else:
    sys_lock()