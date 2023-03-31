import os

def execute_command(command):
    if command.lower() == "dir":
        os.system("ls")
    else:
        os.system(command)

def main():
    print("Microsoft Windows 98 [Version 4.10.1998]")
    print("(c)Copyright Microsoft Corp 1981-1999.")
    print()
    while True:
        command = input("C:\\>")
        if command.lower() == "exit":
            break
        else:
            execute_command(command)

if __name__ == "__main__":
    main()
