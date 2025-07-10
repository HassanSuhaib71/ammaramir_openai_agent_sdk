import asyncio 
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from dotenv import load_dotenv, find_dotenv
import os


load_dotenv()

openrouter_api_key = os.getenv('OPENROUTER_API_KEY')


provider = AsyncOpenAI(
    api_key=openrouter_api_key,
    base_url="https://openrouter.ai/api/v1",
)

model = OpenAIChatCompletionsModel(
    model="google/gemini-2.0-flash-exp:free",
    openai_client=provider,
)

run_config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)


query_agent = Agent(
    name = "query_agent",
    instructions="You are a helpful assistant."
)


async def main():

    result =await Runner.run(
        query_agent,
        input="hi",
        run_config=run_config,
        
    )
    print(result.final_output)


asyncio.run(main())