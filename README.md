# PadhuAutoBlog Crew

Welcome to my PadhuAutoBlog project. This project creates a blogpost based on input topic and uses openAI, Anthropic, Llama3 or any other LLM and various internet search and custom tools to develop a blog post. In addition, the prepared blog post is posted as a blog post in my personal website. This project's template is based on a flexible framework designed to help setting up a multi-agent AI system with ease provided by crewAI (www.crewai.com). 

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:
```bash
poetry lock
```
```bash
poetry install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/padhu_auto_blog/config/agents.yaml` to define your agents
- Modify `src/padhu_auto_blog/config/tasks.yaml` to define your tasks
- Modify `src/padhu_auto_blog/crew.py` to add your own logic, tools and specific args
- Modify `src/padhu_auto_blog/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
poetry run padhu_auto_blog
```

This command initializes the padhu_auto_blog Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folser

## Understanding Your Crew

The padhu_auto_blog Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the PadhuAutoBlog Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Joing our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat wtih our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
