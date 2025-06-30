import src.mood as mood

"""
Function meant to display mood history... coming soon
"""

"""
1.Open data/mood_log.txt (using files)
2. Read and print each mood entry (using files)
3. else -> message "No page available, try logging in a mood first" (conditionals)
"""

def view_history():
    with open("data/mood_log.txt", "r") as file:
        mood_entries = file.readlines() # read all lines in mood file
        if mood_entries:
            print("\n--- Mood History ---")
            for entry in mood_entries:
                print(entry.strip()) #display the mood log
        else:
            print("\nNo mood history available. Please log your mood first.")


if __name__ == "__main__":
    view_history()

