from dotenv import load_dotenv
load_dotenv()

from crewai import Crew, Process

from input import get_user_input

from agents import (
    create_skill_analyzer,
    create_career_recommender,
    create_learning_roadmap
)

from tasks import (
    create_skill_analysis_task,
    create_career_task,
    create_roadmap_task
)

# ------------------------
# Get User Input
# ------------------------

user_data = get_user_input()



skill_agent = create_skill_analyzer()
career_agent = create_career_recommender()
roadmap_agent = create_learning_roadmap()



skill_task = create_skill_analysis_task(skill_agent, user_data)
career_task = create_career_task(career_agent, user_data)
roadmap_task = create_roadmap_task(roadmap_agent)

career_crew = Crew(
    agents=[
        skill_agent,
        career_agent,
        roadmap_agent
    ],
    tasks=[
        skill_task,
        career_task,
        roadmap_task
    ],
    process=Process.sequential,
    verbose=True
)


result = career_crew.kickoff()

print("\n" + "="*60)
print("FINAL RESULT")
print("="*60)
print(result)
with open("career_report.txt", "w", encoding="utf-8") as f:
    f.write(str(result))

print("Report saved as career_report.txt")