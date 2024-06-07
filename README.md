# Ollama Tutorial
This is my first attempt at working with LLMs to create Intelligent Digital Workers.

Eventually this project will implement the ideas discussed
[here](https://quickaitutorial.com/crewai-solor-hermes-langchain-ollama-super-ai-agent/)

For now, this simple example just connects to a running Ollama server and streams it's response
to a hard-coded question.

## Running the Ollama server
```
ollama serve
```

## If this is your first time, download a model
Ollama requires a model on your system. To install the llama3 model, for instance, run the
following command:
```
ollama run llama3
```

## Running the example code
```
python main.py
```

## Current state:
As of now, some functionality has been shown. But it is very slow (~3-4 minutes to see activity),
and on top of that there is an error that is also encountered

```
I encountered an error while trying to use the tool. This was the error: DuckDuckGoSearchRun._run()
got an unexpected keyword argument 'q'.
Tool duckduckgo_search accepts these inputs: A wrapper around DuckDuckGo Search. Useful for when
you need to answer questions about current events. Input should be a search query.
```
There is a [GitHub issue](https://github.com/joaomdmoura/crewAI/issues/706) tracking this same
error, but it doesn't appear to have been triaged as of yet.

One thing to note, is that depending on which model is selected for the `research_agent` role, it
might bypass the error after a few tries. This was seen when using the `solar` model.

## Future work:
Will look into trying other tools to replace DuckDuckGo search.
