import pickle
import os

class BotState:
    """Class to represent the state of an automated bot for serialization."""
    def __init__(self, bot_id, status, last_task):
        self.bot_id = bot_id
        self.status = status
        self.last_task = last_task
        self.tasks_completed = 0

    def complete_task(self):
        self.tasks_completed += 1
        print(f"Bot {self.bot_id} completed task: {self.last_task}")

    def __repr__(self):
        return f"BotState(ID={self.bot_id}, Status={self.status}, Completed={self.tasks_completed})"

# --- Testing the implementation ---
if __name__ == "__main__":
    file_path = "bot_memory.pkl"
    
    # 1. Create a bot and simulate activity
    my_bot = BotState("AI-9000", "Active", "Data Extraction")
    my_bot.complete_task()
    my_bot.complete_task()
    
    # 2. Serialize (Pickle) the object to a file
    print("\nSerializing bot state...")
    with open(file_path, "wb") as file:
        pickle.dump(my_bot, file)
    
    # 3. Modify the original object to show difference
    my_bot.status = "Offline"
    print(f"Original bot now: {my_bot}")
    
    # 4. Deserialize (Unpickle) the object back
    print("\nDeserializing bot state from file...")
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            restored_bot = pickle.load(file)
        print(f"Restored bot state: {restored_bot}")
        
        # Cleanup
        os.remove(file_path)
    else:
        print("Save file not found.")
