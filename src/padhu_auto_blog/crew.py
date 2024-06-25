from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
#from langchain_anthropic import ChatAnthropic
#from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from datetime import datetime
import subprocess

@CrewBase
class PadhuAutoBlogCrew:
    """PadhuAutoBlog crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    llm = ChatOpenAI(model="gpt-3.5-turbo")

    @agent
    def researcher(self) -> Agent:
        agent = Agent(
            config=self.agents_config['researcher'],
            verbose=True,
            llm=self.llm
        )
        
        return agent

    @agent
    def reporting_analyst(self) -> Agent:
        agent = Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True,
            llm=self.llm
        )
        
        return agent

    @agent
    def designer(self) -> Agent:
        agent = Agent(
            config=self.agents_config['designer'],
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

        return agent

    
    @task
    def research_task(self) -> Task:
        task = Task(
            config=self.tasks_config['research_task'],
            agent=self.researcher(),
            output_file=f"logs/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_research_task.md"
        )
        print(f"Initialized research task: {task}")
        return task

    @task
    def reporting_task(self) -> Task:
        task = Task(
            config=self.tasks_config['reporting_task'],
            agent=self.reporting_analyst(),
            output_file=f"logs/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_reporting_task.md"
        )
        
        return task
    
    @task
    def designing_task(self) -> Task:
        task = Task(
            config=self.tasks_config['designing_task'],
            agent=self.designer(),
            output_file=f"logs/blog_post.html"
        )
        
        return task

    #@task
    #def blog_posting_task(self) -> Task:
    #    """This task is to run after all the other tasks are completed"""
    #    def posting_function():
    #        result = subprocess.run(['python', 'src/padhu_auto_blog/blog_post.py'], capture_output=True, text=True)
    #        if result.returncode == 0:
    #            print("Blog post script executed successfully.")
    #        else:
    #            print(f"Blog post script failed with return code {result.returncode}.")
    #            print(result.stderr)

    #   task = Task(
    #        name="Run Blog post Script",
    #        task_function=posting_function,
    #        agent=self.designer(),  # Assigning the dummy agent
    #        output_file=f"logs/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_blog_posting_task.log",
    #        description="This task runs the standalone blog post script.",
    #        expected_output="Message indicating the successful execution or failure of the blog post script."
    #    )
    #    print(f"Initialized blog posting task: {task}")
    #    return task

    @crew
    def crew(self) -> Crew:
        """Creates the PadhuAutoBlog crew"""
        crew = Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks,
            process=Process.sequential,
            verbose=2
           
        )
        
        return crew


