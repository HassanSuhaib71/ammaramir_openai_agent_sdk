import asyncio
import os
from agents import Agent, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel, Runner
from dotenv import load_dotenv

load_dotenv()



openai_api_key = os.getenv("OPENAI_API_KEY")


async def main():

    agent = Agent(
        name="agent",
        instructions="You are a helpful assistant.",
    )

    result = Runner.run_streamed(
        agent,
        input="Who is the founder of Pakistan.",

    )

    async for event in result.stream_events():
        if event.type == "raw_response_event" and hasattr(event.data, 'delta'):
            token = event.data.delta
            print(token)


asyncio.run(main())