import subprocess

def run_pyrcc5():
    try:
        # Run the pyrcc5 command
        subprocess.run(['pyrcc5', 'MyQRC.qrc', '-o', 'data/MyQRC_rc.py'], check=True)
        print("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")

if __name__ == "__main__":
    run_pyrcc5()
