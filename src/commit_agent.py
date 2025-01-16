"""
AI-powered Git commit analysis module.

This module uses OpenAI's GPT model through the autogen library to analyze Git diffs,
suggest files for commit, and generate appropriate conventional commit messages.
It handles the interaction with the AI model and parsing of its responses.
"""

import os
import autogen
from typing import List, Tuple
from git_utils import get_diff

# Get API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Configure the agent
config_list = [
    {
        "model": "gpt-4o",
        "api_key": api_key  # Should be configured via environment variable
    }
]

# Create assistant agent without Docker
assistant = autogen.AssistantAgent(
    name="git_assistant",
    llm_config={
        "config_list": config_list,
    },
    system_message="""You are a helpful assistant that analyzes git diffs and suggests:
    1. Which files should be included in the commit
    2. An appropriate commit message following conventional commit format

    Focus on creating clear, concise commit messages that explain the purpose of the changes."""
)

# Create user proxy agent
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=0,
    is_termination_msg=lambda x: x.get(
        "content", "").rstrip().endswith("TERMINATE"),
    code_execution_config=False,
)


def analyze_changes(seed_text: str = None) -> Tuple[List[str], str, float]:
    """
    Analyze git diff and return suggested files and commit message
    Args:
        seed_text: Optional text to guide commit message generation
    Returns:
        Tuple containing (list of files to commit, suggested commit message, operation cost)
    """
    diff_output = get_diff()

    # Initialize the conversation
    chat_result = user_proxy.initiate_chat(
        assistant,
        message=f"""Please analyze this git diff and suggest:
        1. Which files should be included in the commit
        2. A clear commit message following conventional commit format
        3. For larger commits, include details about the changes made as bullet points

        Git diff:
        {diff_output}
        
        {"Consider this seed text for the commit message: " + seed_text if seed_text else ""}

        Format your response as:
        FILES:
        - file1
        - file2

        MESSAGE:
        type(scope): description

        Additional details as bullet points (if needed)

        TERMINATE"""
    )

    # Extract response
    last_message = assistant.last_message()
    if not last_message:
        return [], "No changes to commit"

    print(f"Last message: {last_message}")

    content = last_message.get("content", "")

    # Parse response
    files_section = ""
    message_section = ""

    if "FILES:" in content and "MESSAGE:" in content:
        sections = content.split("MESSAGE:")
        files_section = sections[0].split("FILES:")[1].strip()
        message_section = sections[1].strip()

    # Extract files
    files = [f.strip("- ").strip()
             for f in files_section.split("\n") if f.strip()]
    # Print detected files
    print(f"Detected files: {files}")

    # Extract message
    # message = message_section.split("\n")[0].strip()
    message = message_section
    # Remove any lines with "TERMINATE"
    message = "\n".join(
        [line for line in message.split("\n") if "TERMINATE" not in line])

    # Print detected message
    print(f"Detected message: {message}")

    # Get cost from the last conversation
    cost = chat_result.cost['usage_including_cached_inference']['total_cost']
    return files, message, cost
