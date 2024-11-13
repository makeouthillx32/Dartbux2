import os
import subprocess
import sys

def main():
    # Ask the user how many Punch Cards they want to generate
    num_punchcards = int(input("How many Punch Cards do you want to generate? "))

    # Ensure we are in the correct directory
    os.chdir("C:\\Users\\Kiosk\\OneDrive\\Documents\\Punsh_card_maker")

    # Generate individual Punch Cards
    result = subprocess.run([sys.executable, "generate_individual_punchcard.py", str(num_punchcards)])
    if result.returncode != 0:
        print("Error generating individual Punch Cards.")
        return

    # Create composite images for printing
    result = subprocess.run([sys.executable, "create_composit_image.py"])
    if result.returncode != 0:
        print("Error creating composite images.")
        return

if __name__ == "__main__":
    main()
