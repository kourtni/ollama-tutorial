from crewai import Agent, Task, Crew, Process

from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchRun
from langchain_community.llms import Ollama

search_tool = DuckDuckGoSearchRun()
ollama_llama3 = Ollama(model="llama3")
# ollama_openhermes = Ollama(model="openhermes")
# ollama_solar = Ollama(model="solar")

researcher = Agent(
    role='Researcher',
    goal=('Research methods to grow this channel Gao Dalie (高達烈) on youtube and get more '
          'subscribers'),
    backstory='You are an AI research assistant',
    tools=[search_tool],
    verbose=True,
    llm=ollama_llama3, # Ollama model passed here
    allow_delegation=False
)

writer = Agent(
    role='Writer',
    goal=('Write compelling and engaging reasons as to why someone should join Gao Dalie (高達烈) '
          'youtube channel'),
    backstory='You are an AI master mind capable of growing any youtube channel',
    verbose=True,
    llm=ollama_llama3, # Ollama model passed here
    allow_delegation=False
)

task1 = Task(description='Investigate Gao Dalie (高達烈) Youtube channel',
             expected_output='A list of videos that can be found on the channel and a brief',
             agent=researcher)
task2 = Task(description='Investigate sure fire ways to grow a channel',
             expected_output='A list of 10 videos related to growing a youtube channel and a brief',
             agent=researcher)
task3 = Task(description='Write a list of tasks Gao Dalie (高達烈) must do to grow his channel',
             expected_output='A list of 5 tasks that Gao Dalie (高達烈) must do to grow his channel',
             agent=writer)

crew = Crew(
    agents=[researcher, writer],
    tasks = [task1,task2,task3],
    verbose=2,
    process=Process.sequential
)

result = crew.kickoff()
print(result)
exit(0)
