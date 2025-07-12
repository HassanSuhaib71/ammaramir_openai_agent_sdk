import asyncio
from agents import Agent, Runner
from dotenv import load_dotenv
from agents.tool import function_tool
import os


load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')


@function_tool("get_weather")
def get_weather(location : str, temp : str = "C"):
    """
    Fetch the weather for a given location.
    """

    return f"The weather of {location} is 22 degree {temp}."


@function_tool("piaic_student")
def piaic_student(roll_no : int):
    """
    Find the piaic student on the basis of rollno.
    """
    data = {
        1 : "Qasim",
        2 : "Zia",
        3 : "Rehan",
    }

    return data.get(roll_no, "Not Found")


async def main():

    agent = Agent(
        name = "Helpful Assistant",
        instructions="You are helpful assistant.",
        tools=[get_weather,piaic_student]
    )

    result = await Runner.run(
        agent,
        input = "What is the wname of roll no 2"
    )

    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())