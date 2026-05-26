def allocate_tasks(members, tasks):
    """
    Allocates tasks to studio members.
    Demonstrates nested functions and error handling.
    """
    def check_eligibility(member):
        return member in ["Krish", "Alex", "Jordan"]

    allocation = {}
    
    try:
        if len(members) != len(tasks):
            raise ValueError("The number of members must match the number of tasks.")
        
        for i in range(len(members)):
            member = members[i]
            if not check_eligibility(member):
                print(f"Warning: {member} is a guest and cannot receive high-priority tasks.")
                continue
            allocation[member] = tasks[i]
            
    except Exception as e:
        print(f"Allocation Error: {e}")
        return None
        
    return allocation

# Main execution block
if __name__ == "__main__":
    studio_members = ["Krish", "Alex", "Sam"] # Sam is not eligible
    project_tasks = ["Level Design", "Core Engine", "UI Overhaul"]
    
    print("Starting Task Allocation...")
    result = allocate_tasks(studio_members, project_tasks)
    
    if result:
        print(f"Successful Allocations: {result}")
