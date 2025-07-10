import asyncio 
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from dotenv import load_dotenv, find_dotenv
from agents.tool import function_tool
import os
from agents import enable_verbose_stdout_logging
enable_verbose_stdout_logging()

load_dotenv(find_dotenv())


gemini_api_key = os.getenv('GEMINI_API_KEY')


provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model='gemini-2.0-flash',
    openai_client=provider,
)

run_config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True,
)



@function_tool("get weather")
def get_weather(location: str , unit: str = "C"):
    """
    Fetch the weather for a given location.
    """
    return f"The weather of {location} is 22 degree {unit}"




async def main():

    agent = Agent(
        name = "Agent",
        instructions="You are a helpful assistant, Please provide a clear answer without extra info. You will provide weather in ferenhite.",
        tools = [get_weather],
    )


    result = await Runner.run(
        agent,
        input = "What is the weather in Karachi.",
        run_config=run_config,
    )

    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())