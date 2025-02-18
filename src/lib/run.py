"""
run.py

This module provides functionality to run an agent asynchronously, print debug information, 
and save the agent's history to a file.
"""

from src.lib.utils import print_agent_brain, print_extracted_content


async def run_agent(agent):
    """
    Asynchronously runs the agent, prints debug information, and saves the agent's history.

    Args:
        agent (object): The agent object to be run and whose history will be processed and saved.

    Returns:
        final_result (object): The final result of the agent's run.

    The function performs the following steps:
    1. Runs the agent with a maximum of 50 steps.
    2. Prints a separator line.
    3. Prints the action results from the agent's history.
    4. Prints the model thoughts from the agent's history.
    """

    result = await agent.run(max_steps=50)

    print("-" * 80)
    print("\n=== Action Results ===")
    print_extracted_content(result.action_results())
    print("\n=== Model Thoughts ===")
    print_agent_brain(result.model_thoughts())

    return result.final_result()
