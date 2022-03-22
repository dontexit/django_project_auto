import subprocess
import os
import platform

PLATFORM = platform.system()

if PLATFORM  == 'Windows':
    PLATFORM = True
    PREF = 'python'
    path = '_env/Scripts/python'
elif PLATFORM == 'Linux':
    PLATFORM = False
    PREF = 'python3'
    path = '_env/bin/python'

def create_env(proj):
    try:
        subprocess.run([PREF,'-m','venv',"%s_env" % proj], check=True)
    except Exception as e:
            print(e)
            quit()
    else:
        print("CREATED VENV '%s_env'" % proj)


def install_django(env=False):
        if env:
            cmd = [env,'-m','pip','install','django']
        else:
            cmd = ['pip','install','django']
        try:
            subprocess.run(cmd,check=True)
        except Exception as e:
                print(e)
                quit()
        else:
                print("Sucessfully Installed Django....")


def create_proj(proj,env=False):
    if env:
        cmd = [env,'-m','django',"startproject",proj]
    else:
        cmd = [PREF,'-m','django',"startproject",proj]
    print("Creating project '%s' in '%s'" % (proj, os.getcwd()))
    
    try:
        subprocess.run(cmd, check=True)
    except Exception as e:
        print(e)
        print("Creating django project %s  failed."% proj)
        print("EXITING................")
        quit()
    else:
        print("Created django project %s sucessfully."% proj)

def main():
    proj = input("Enter your projects name: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("project name set to '%s' \n"% proj)
    env = proj + path
    yn = input("Create a virtual env? (y/n)")
    while yn != 'y' and yn != 'n':
        yn = input("Create a virtual env? (y/n)")
    if yn == 'y':
        print("CREATING A VENV.....")
        create_env(proj)
        print("SWITCHING TO VENV.....")
        print("INSTALLING DJANGO.....")
        install_django(env)
        create_proj(proj,env)
    elif yn == 'n':
        print("INSTALLING DJANGO.....")
        install_django()
        create_proj(proj)        
if __name__ == '__main__':
    main()



