import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    while True:
        clear_screen()
        print("Microsoft Windows 98 [Version 4.10.1998]")
        print("(c)Copyright Microsoft Corp 1981-1999.")
        print()
        command = input("C:\\>")
        if command.lower() == "exit":
            break
        else:
            os.system(command)

if __name__ == "__main__":
    main()
