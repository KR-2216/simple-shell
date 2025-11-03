import os
import subprocess

def main():
    while True:
        #Input Prompt
        current_dir = os.getcwd()
        command = input(f"{current_dir}> ")
        
        #Check for exit
        if command.lower() in ['exit', 'quit']:
            break
        
        #Try to execute the command
        try:
            subprocess.run(command, shell=True)
        except Exception as e:
            print(f"Error: {e}")
main()