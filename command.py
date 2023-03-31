import os
from datetime import datetime

def format_file_size(size):
    if size < 1024:
        return f"{size} bytes"
    elif size < 1024 * 1024:
        return f"{size / 1024:.1f} KB"
    else:
        return f"{size / (1024 * 1024):.1f} MB"

def format_dir_entry(entry):
    if entry.is_file():
        size = format_file_size(entry.stat().st_size)
        mtime = datetime.fromtimestamp(entry.stat().st_mtime).strftime(
            "%m/%d/%Y %I:%M %p"
        )
        return f"{entry.name:<25} {size:>10} {mtime}"
    else:
        return f"{entry.name:<25}    <DIR>"

def execute_dir():
    entries = sorted(os.scandir(), key=lambda e: (e.is_file(), e.name))
    for entry in entries:
        print(format_dir_entry(entry))

def execute_command(command):
    if command.lower() == "dir":
        execute_dir()
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
