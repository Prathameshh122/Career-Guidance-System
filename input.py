def get_user_input():
    print("=" * 50)
    print("      AI Career Guidance System")
    print("=" * 50)

    name = input("Enter your name: ")
    age = input("Enter your age: ")
    qualification = input("Enter your qualification: ")
    skills = input("Enter your skills (comma separated): ")
    interests = input("Enter your interests (comma separated): ")

    return {
        "name": name,
        "age": age,
        "qualification": qualification,
        "skills": skills,
        "interests": interests
    }