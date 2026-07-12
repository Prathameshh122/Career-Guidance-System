import os
from dotenv import load_dotenv
from crewai import Agent, LLM

load_dotenv()

llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2,
    max_tokens=300,  
)

def create_skill_analyzer():
    return Agent(
        role="Skill Analyzer",
        goal="Analyze the student's skills and identify strengths and weaknesses.",
        backstory=(
            "You are an experienced career counselor who evaluates students' "
            "technical and soft skills."
        ),
        llm=llm,
        verbose=True
    )


def create_career_recommender():
    return Agent(
        role="Career Recommendation Expert",
        goal="Recommend the best career paths based on the student's profile.",
        backstory=(
            "You have guided thousands of students in choosing careers based "
            "on their skills and interests."
        ),
        llm=llm,
        verbose=True
    )


def create_learning_roadmap():
    return Agent(
        role="Learning Roadmap Planner",
        goal="Create a personalized learning roadmap for the student.",
        backstory=(
            "You design structured learning plans including courses, projects, "
            "and milestones."
        ),
        llm=llm,
        verbose=True
    )