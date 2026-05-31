class AIPromptManager:
    """Implementing the Singleton design pattern for central AI prompt management."""
    _instance = None

    def __new__(cls):
        """Overrides __new__ to ensure only one instance of the class exists."""
        if cls._instance is None:
            print("Creating unique AI Prompt Manager instance...")
            cls._instance = super(AIPromptManager, cls).__new__(cls)
            # Initialize attributes only once
            cls._instance.history = []
        return cls._instance

    def generate_prompt(self, task, style="professional"):
        """Generates and logs a prompt."""
        prompt = f"As an expert AI, please {task} in a {style} tone."
        self.history.append(prompt)
        return prompt

    def get_history(self):
        return self.history

# --- Testing the implementation ---
if __name__ == "__main__":
    # First access
    manager1 = AIPromptManager()
    print(manager1.generate_prompt("explain decorators", "simple"))
    
    # Second access (should return the SAME instance)
    manager2 = AIPromptManager()
    print(f"Is manager2 same as manager1? {manager1 is manager2}")
    
    manager2.generate_prompt("refactor this class", "technical")
    
    # Both see the same history
    print("\n--- Shared Prompt History ---")
    for idx, p in enumerate(manager1.get_history(), 1):
        print(f"{idx}. {p}")
