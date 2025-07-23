from pydantic import BaseModel
from agents import (
    Agent,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    OutputGuardrailTripwireTriggered,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    input_guardrail,
    output_guardrail,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    RunConfig
)
from dotenv import load_dotenv
import os
import asyncio


load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")


class MathHomeWorkOutput(BaseModel):
    is_math_homework : bool
    reasoning : str
    awnser : str

guardrail_agent = Agent(
    name = "Guardrail Check",
    instructions="Check if the user is asking you to do their math homework.",
    output_type=MathHomeWorkOutput
)

# result = Runner.run_sync(guardrail_agent, "Who is the founder of Pakistan.")
# print(result.final_output)

@input_guardrail
async def math_guardrail(
    ctx : RunContextWrapper[None], agent : Agent, input : str | list[TResponseInputItem]
) -> GuardrailFunctionOutput :
    result = await Runner.run(guardrail_agent, input, context=ctx.context)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_math_homework
    )

agent = Agent(
    name="Customer Support Agent",
    instructions="You are Math support agent. You help student with their questions.",
    input_guardrails=[math_guardrail],
)

try:
    result = Runner.run_sync(agent, "factoriel of 7")
    print("Guardrail didnot trip - this is unexpected")
    print(result.final_output)
except InputGuardrailTripwireTriggered:
    print("Math homework guardrail tripped.")