"""
utils.py

This module provides utility functions for printing and formatting model thoughts,
action results, and structured JSON results.
"""

import json


def print_agent_brain(model_thoughts):
    """
    Prints the details of each model thought in the provided list.

    Args:
        model_thoughts (list): A list of objects containing the model's thoughts.

    Returns:
        None
    """

    if not model_thoughts:
        print("No model thoughts available.")
        return

    for i, thought in enumerate(model_thoughts, start=1):
        print(f"\nAgent Brain #{i}:\n")
        print(f"Page Summary:\n{thought.page_summary}\n")
        print(f"Evaluation of Previous Goal:\n{thought.evaluation_previous_goal}\n")
        print(f"Memory:\n{thought.memory}\n")
        print(f"Next Goal:\n{thought.next_goal}\n")
        print("-" * 80)


def print_extracted_content(action_results):
    """
    Prints the extracted content from each action result in the provided list.

    Args:
        action_results (list): A list of objects containing action results.

    Returns:
        None
    """

    if not action_results:
        print("No action results available.")
        return

    for i, result in enumerate(action_results, start=1):
        print(f"\nAction Result #{i}:\n")
        print(f"Extracted Content:\n{result.extracted_content}\n")
        print("-" * 80)


def print_structured_result(result):
    """
    Pretty prints the structured result if it is compressed JSON.

    Args:
        result (str or dict): The JSON result to be printed.

    Returns:
        None
    """

    print("\n=== Structured Result ===\n")

    try:
        # Try to parse and pretty-print the JSON result
        parsed_result = json.loads(result) if isinstance(result, str) else result
        print(json.dumps(parsed_result, indent=4, ensure_ascii=False))
    except (json.JSONDecodeError, TypeError):
        # If it's not valid JSON, print it as-is
        print(result)

    print("\n", "-" * 80)
