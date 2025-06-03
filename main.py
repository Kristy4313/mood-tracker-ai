from mood import get_mood
from history import view_history

def main_menu():
    while True:
        print("\nWelcome to Mood Tracker AI") # menu first line

        print("\nPlease select an option:\n")
        print("1 - Enter today's mood\n")
        print("2 - View mood history\n")
        print("3 - Exit\n")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            get_mood()
        elif choice == "2":
            view_history()
        elif choice == "3":
            print("\nGoodbye!, comeback soon...\n")
            print("------------------------------\n")
            break
        else:
            print("Sorry, that's an invalid choice. Please try again.")

        
        
if __name__ == "__main__":
    main_menu()
        


