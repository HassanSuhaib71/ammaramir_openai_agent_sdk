from __future__ import annotations

import asyncio

from agents import Agent, Runner, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
from dotenv import load_dotenv
import os

load_dotenv()

MODEL = "gemini/gemini-2.0-flash"
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')


def main(model: str, api_key: str):
    agent = Agent(
        name = "Assistant",
        instructions="You are helpful assistant.",
        model = LitellmModel(model=model, api_key=api_key),
    )

    result = Runner.run_sync(
        agent,
        "hi",
    )

    print(result.final_output)


main(model=MODEL, api_key=GEMINI_API_KEY)