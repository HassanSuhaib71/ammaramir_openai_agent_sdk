from pydantic import BaseModel
import asyncio
from dataclasses import dataclass
from agents import Agent, Runner, RunContextWrapper, function_tool
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

@dataclass
class UserInfo:
    name : str
    uid : int
    age : int
    location : str = "Pakistan"


@function_tool
async def fetch_user_age(wrapper : RunContextWrapper[UserInfo]) -> str:
    '''Return the age of the user.'''
    # print("[-> Tool]", wrapper, "\n\n")
    return f"User {wrapper.context.name} is {wrapper.context.age} year old."

@function_tool
async def fetch_user_location(wrapper : RunContextWrapper[UserInfo]) -> str:
    '''Return the currentlocation of user.'''
    # print("[->Tool Current Location]", wrapper, "\n\n")
    return f"User {wrapper.context.name} is current at {wrapper.context.location}"


async def main():
    user_info = UserInfo(uid=1, name="hassan", age=20)

    agent = Agent[UserInfo](
        name = "Assistant",
        tools=[fetch_user_age,fetch_user_location],
        
    )

    result = await Runner.run(
        agent,
        "What is the name and the age od the user and where the user is located",
        context = user_info
    )
    print(result.final_output)

asyncio.run(main())