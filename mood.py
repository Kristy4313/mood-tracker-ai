"""
Fuction meant to ask for mood and log it in
"""

def get_mood():
    mood = input("\nHow are you feeling today? ")
    print(f"Your mood [{mood}], has been recored (not yet saved)")

if __name__ == "__main__":
    get_mood()