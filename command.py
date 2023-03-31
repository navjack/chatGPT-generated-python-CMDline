import os
import shutil
from datetime import datetime

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

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

def execute_copy(args):
    if len(args) != 2:
        print("Invalid number of arguments for COPY command")
        return
    src, dst = args
    try:
        shutil.copy(src, dst)
        print(f"Copied {src} to {dst}")
    except Exception as e:
        print(f"Error copying file: {e}")

def execute_command(command):
    parts = command.split()
    cmd = parts[0]
    args = parts[1:]
    if cmd.lower() == "dir":
        execute_dir()
    elif cmd.lower() == "copy":
        execute_copy(args)
    else:
        os.system(command)

def main():
    clear_screen()
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
