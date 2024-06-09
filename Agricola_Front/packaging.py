import subprocess

def run_pyrcc5():
    try:
        # Run the pyrcc5 command
        subprocess.run(['pyinstaller', 'main.spec'], check=True)
        print("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")

if __name__ == "__main__":
    run_pyrcc5()
