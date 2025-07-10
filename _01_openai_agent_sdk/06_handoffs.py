import asyncio 
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from dotenv import load_dotenv
import os


load_dotenv()

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


spanish_agent = Agent(
    name="spanish_agent",
    instructions="You translate user's message to Spanish.",
    handoff_description="An English to Spanish Translator.",
    model=model
)

french_agent = Agent(
    name = "french_agent",
    instructions="You translate user's message to French.",
    handoff_description="An English to French Translator.",
    model=model
)

german_agent = Agent(
    name = "german_agent",
    instructions="You translate user's message to German.",
    handoff_description="An English to German Translator.",
    model=model
)

urdu_agent = Agent(
    name="urdu_agent",
    instructions="You translte user's message to Urdu.",
    handoff_description="An English to Urdu Translator.",
    model=model,
)


triage_agent = Agent(
    name = "General Assistant",
    instructions= "You determine which agent to use based on the user's query.",
    handoffs=[spanish_agent, french_agent, german_agent, urdu_agent]
)


async def main():

    result = await Runner.run(
        triage_agent,
        input= "Translate into Urdu 'Hello How are You?'",
        run_config=run_config
    )
    print(result.final_output)


asyncio.run(main())