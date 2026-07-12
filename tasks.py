from crewai import Task


def create_skill_analysis_task(agent, user_data):
    return Task(
        description=f"""
        Analyze the following student profile:

        Name: {user_data['name']}
        Qualification: {user_data['qualification']}
        Skills: {user_data['skills']}
        Interests: {user_data['interests']}

        Identify:
        - Strengths
        - Weaknesses
        - Skills to improve
        """,
        expected_output="""
        A detailed skill analysis with strengths,
        weaknesses and improvement suggestions.
        """,
        agent=agent
    )


def create_career_task(agent, user_data):
    return Task(
        description=f"""
        Based on this profile:

        Skills: {user_data['skills']}
        Interests: {user_data['interests']}

        Recommend the top 2 careers.

        Explain why each career suits the student.
        """,
        expected_output="""
        A ranked list of career recommendations
        with explanations.
        """,
        agent=agent
    )


def create_roadmap_task(agent):
    return Task(
        description="""
        Create a learning roadmap for the
        recommended career.

        Include:
        - Skills to learn
        - Online resources
        - Projects
        - Timeline
        """,
        expected_output="""
        A complete step-by-step learning roadmap in 200 words.
        """,
        agent=agent
    )