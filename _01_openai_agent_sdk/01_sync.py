from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')


provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client=provider
)

run_config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)


agent = Agent(
    name="Assistant",
    instructions="You are a helpful Assistant."
)


result = Runner.run_sync(
    agent,
    input = "Who is the founder of Pakistan.",
    run_config=run_config
)

print(result.final_output)