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
)
from dotenv import load_dotenv
import os


load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

class Country(BaseModel):
    is_country_pakistan : bool
    reasoning : str
    answer : str

guardrail_agent = Agent(
    name = "Guardrail Agent",
    instructions="You allowed to give information about Pakistan only. Do not give answer to anyother country or aspect.",
    output_type=Country,
)

# result = Runner.run_sync(guardrail_agent, "Who is the founder of India.")
# print(result.final_output)

@output_guardrail
async def country_allowed(
    ctx : RunContextWrapper[None], agent : Agent, output
) -> GuardrailFunctionOutput : 
    result = await Runner.run(guardrail_agent, output, context=ctx.context)

    return GuardrailFunctionOutput(
        output_info = result.final_output,
        tripwire_triggered=result.final_output.is_country_pakistan is False,
    )

agent = Agent(
    name = "Assistant",
    instructions="You are provide information about Pakistan only.",
    output_guardrails=[country_allowed]
)

try:
    result = Runner.run_sync(agent, "Who is the founder of Pakistan.")
    print(result.final_output)
    print("Guardrail not tripp unexpected")
except GuardrailFunctionOutput:
    print("Guardrail tripped")