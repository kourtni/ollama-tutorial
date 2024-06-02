# Ollama Tutorial
This is my first attempt at working with LLMs to create Intelligent Digital Workers.

Eventually this project will implement the ideas discussed [here](https://quickaitutorial.com/crewai-solor-hermes-langchain-ollama-super-ai-agent/)

For now, this simple example just connects to a running Ollama server and streams it's response
to a hard-coded question.

## Running the Ollama server
```
ollama serve
```

## If this is your first time, download a model
Ollama requires a model on your system. To pull down the llama3 model, run the following command.
```
ollama run llama3
```

## Running the example code
```
python main.py
```
