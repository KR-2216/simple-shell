import os
import subprocess

#Built-in cd
def shellcd(parts):
    if len(parts)<2:
        print("Usage: cd <directory>")
    else:
        try:
            os.chdir(parts[1])
        except FileNotFoundError:
            print("Directory not found: {parts[1]}")
        except Exception as e:
            print(f"Error: {e}")
#Built-in help
def shellhelp():
    print("\nBuilt-in commands:")
    print("  cd <directory>  - Change directory")
    print("  pwd             - Print working directory")
    print("  cls/clear       - Clear screen")
    print("  help            - Show this help message")
    print("  exit/quit       - Exit the shell")
    print("\nNOTE: You can also run any external program (e.g., notepad, python, dir)\n")
    
def main():
    print("---Simple Shell v0.1---")
    print("Type 'help' for more information\n")

    while True:
        #Input Prompt
        current_dir = os.getcwd()
        command = input(f"{current_dir}> ")
        
        #Empty command handling
        if not command.strip():
            continue
        
        #Split command and arguments
        parts = command.split()
        cmd_name = parts[0].lower()

        if cmd_name in ['exit', 'quit']:
            break
        elif cmd_name == 'cd':
            shellcd(parts)
        elif cmd_name == "pwd":
            print(os.getcwd())
            continue
        elif cmd_name in ['clear', 'cls']:
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif cmd_name == 'help':
            shellhelp()
            continue

        #Try to execute external command
        else:
            try:
                subprocess.run(command, shell=True)
            except Exception as e:
                print(f"Error: {e}")
main()
