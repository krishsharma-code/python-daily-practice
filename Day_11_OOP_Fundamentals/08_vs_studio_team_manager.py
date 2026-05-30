# Day 11: VS Studio Team Manager
# Concept: Define a Developer class to manage team members and roles.

class Developer:
    def __init__(self, name, role, skill):
        self.name = name
        self.role = role
        self.skill = skill

    def __str__(self):
        return f"Developer: {self.name} | Role: {self.role} | Skill: {self.skill}"

class TeamManager:
    def __init__(self, project_name):
        self.project_name = project_name
        self.team = []

    def add_member(self, developer):
        if len(self.team) < 7:
            self.team.append(developer)
            print(f"Added {developer.name} to {self.project_name} team.")
        else:
            print("Team is full! Max 7 members allowed.")

    def show_team(self):
        print(f"\n--- {self.project_name} Team Roster ---")
        for dev in self.team:
            print(dev)

# Initializing Team Manager
vs_studio_team = TeamManager("VS Studio Plugin")

# Defining 7 developers with specific roles
developers = [
    Developer("Krish", "Lead Architect", "Python/C++"),
    Developer("Alice", "Game Logic", "Mathematics"),
    Developer("Bob", "GUI Specialist", "Tkinter/PyQt"),
    Developer("Charlie", "Database Lead", "SQL/PostgreSQL"),
    Developer("David", "Testing Lead", "PyTest"),
    Developer("Eve", "UI/UX Designer", "CSS/Assets"),
    Developer("Frank", "Network Engineer", "Sockets/API")
]

# Adding members to the team
for dev in developers:
    vs_studio_team.add_member(dev)

vs_studio_team.show_team()
