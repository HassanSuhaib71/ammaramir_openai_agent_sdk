from agents import Agent, FileSearchTool, Runner, WebSearchTool
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

agent = Agent(
    name = "Hassan Personal Assistant",
    tools=(
        WebSearchTool(),
        FileSearchTool(
            max_num_results=3,
            vector_store_ids=["vs_687774ea99688191987443e658f108c1"],
        )
    )
)

result = Runner.run_sync(
    agent,
    "what the ai skills are with hassan suhaib"
)

print(result.final_output)