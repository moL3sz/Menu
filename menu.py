import msvcrt
import os
def loginPage():
    print("loginPage")
    pass
def aboutPage():
    print("about Page")
    pass
def exitPage():
    print("exitPage")
    pass
options = [
    "Login",
    "About",
    "Exit"
    ]
funcitons = {0:loginPage,1:aboutPage,2:exitPage}
def printMenu(current_opt_id):
    current_arrow = "=>"
    for i,opt in enumerate(options):
        if i == abs(current_opt_id) % len(options):
            print(f"{current_arrow} {opt}")
        else:
            print(f"{opt}")
def main():
    os.system("cls")
    current_opt_id = 0
    printMenu(current_opt_id)
    while True:
        key = msvcrt.getch()
        os.system("cls")
        if key == b"P":
            current_opt_id += 1
        elif key == b"H":
            current_opt_id -=1
        elif key == b"\r":
            funcitons[abs(current_opt_id) % len(options)]()
            break
        printMenu(current_opt_id)
if __name__ == "__main__":
    main()