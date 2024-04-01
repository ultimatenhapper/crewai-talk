from textwrap import dedent
from crewai import Task

class MeetingPrepTasks():
    def research_task(self, agent, meeting_participants, meeting_context):
        return Task(
            description=dedent(f"""\
                Conduct comprehensive research of each of the individuals and companies involved
                in the upcoming meeting. Gather information on recent news, achievements, profesional background, and any relevant
                business activities 
                
                Participants: {meeting_participants} 
                Meeting Context: {meeting_context}"""),
            expected_output=dedent(f"""\
                A detailed report summarizing key findings about each participant
                and company, highlighting  information that could be relevant for the meeting"""),
            agent=agent,
            async_execution=True
        )
    
    def industry_analysis_task(self, agent, meeting_participants, meeting_context):
        return Task(
            description=dedent(f"""\
                Analyze the current industry trends, challenges, and opportunities
                relevant to the meeting´s context. Consider market reports, recent 
                developments, and expert opinions to provide a comprehensive
                overview of the industry landscape.
                
                Participants: {meeting_participants} 
                Meeting Context: {meeting_context}"""),
            expected_output=dedent(f"""\
                A detailed report summarizing key findings about each participant
                and company, highlighting  information that could be relevant for the meeting"""),
            agent=agent,
            async_execution=True
        )
    def meeting_strategy_task(self, agent, meeting_context, meeting_objective):
        return Task(
            description=dedent(f"""\
                Develop strategic talking points, questions, and discussion angles
                for the meeting based on the research and industry analysis conducted
                
                Meeting Objective: {meeting_objective} 
                Meeting Context: {meeting_context}"""),
            expected_output=dedent(f"""\
                Complete report with a list of key talking points, strategic questions to ask
                to help achieve the meetings objective during the meeting"""),
            agent=agent,
        )
    
    def summary_and_briefing_task(self, agent, meeting_context, meeting_objective):
        return Task(
            description=dedent(f"""\
                Compile all the research findings, industry analysis, and strategic
                talking points into a concise, comprehensive briefing document for 
                the meeting.
                Ensure the briefing is easy to digest and equips the meeting 
                participants with all neccesary information and strategies.
                
                Meeting Objective: {meeting_objective} 
                Meeting Context: {meeting_context}"""),
            expected_output=dedent(f"""\
                A well-structured briefing document that includes sections for participants bios,
                industry overview, talking points, and strategic recommendations"""),
            agent=agent,
            async_execution=True
        )