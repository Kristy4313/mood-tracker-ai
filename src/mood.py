import os
from datetime import datetime
"""
Fuction meant to ask for mood and log it in
"""

def get_mood():
    mood = input("\nHow are you feeling today? ")
    save_mood(mood) # saving mood 
    print("\n -----------------------------------------------------")


"""
Function for saving the mood and loging it in the moods_log.txt file
"""

def save_mood(mood):
    now = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

    # Ensure the data folder exists and add mood log there
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    log_path = os.path.join(data_dir, "mood_log.txt")

    with open(log_path, "a") as file:
        file.write(f"{now} - {mood}\n")
        
    print(f"\nYour mood '{mood}' was saved successfully!")

if __name__ == "__main__":
    get_mood()