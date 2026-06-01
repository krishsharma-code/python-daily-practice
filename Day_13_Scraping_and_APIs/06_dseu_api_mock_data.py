import json
import random

# Day 13: Web Scraping and APIs
# Concept 06: Data Generation and Serialization (JSON Export)

def generate_mock_student_data(count=5):
    """Generates mock student data for DSEU and saves to JSON."""
    
    names = ["Aarav", "Vivaan", "Aditya", "Ishan", "Vihaan", "Arjun", "Sai", "Aaryan", "Ananya", "Diya"]
    courses = ["Computer Science", "Mechanical Engineering", "Civil Engineering", "Data Analytics", "UI/UX Design"]
    campuses = ["Okhla-I", "Okhla-II", "Pusa-I", "Dwarka", "Rohini"]
    
    students = []
    
    for i in range(1, count + 1):
        student = {
            "student_id": f"DSEU2026{i:03d}",
            "name": random.choice(names),
            "course": random.choice(courses),
            "campus": random.choice(campuses),
            "gpa": round(random.uniform(7.0, 9.8), 2),
            "is_active": True
        }
        students.append(student)
        
    # File handling: Writing to a JSON file
    filename = "dseu_students.json"
    
    try:
        with open(filename, 'w') as f:
            # indent=4 makes the JSON file human-readable
            json.dump(students, f, indent=4)
        print(f"Successfully generated {count} mock student records in '{filename}'.")
        
    except IOError as e:
        print(f"Failed to write to file: {e}")

if __name__ == "__main__":
    generate_mock_student_data(10)
