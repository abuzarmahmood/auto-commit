import autogen
from typing import List
from .git_utils import get_diff

# Configure the agent
config_list = [
    {
        "model": "gpt-4",
        "api_key": "your-api-key-here"  # Should be configured via environment variable
    }
]

# Create assistant agent
assistant = autogen.AssistantAgent(
    name="git_assistant",
    llm_config={"config_list": config_list},
    system_message="""You are a helpful assistant that analyzes git diffs and suggests:
    1. Which files should be included in the commit
    2. An appropriate commit message following conventional commit format
    
    Focus on creating clear, concise commit messages that explain the purpose of the changes."""
)

# Create user proxy agent
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=1,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
)

def analyze_changes() -> Tuple[List[str], str]:
    """
    Analyze git diff and return suggested files and commit message
    Returns:
        Tuple containing (list of files to commit, suggested commit message)
    """
    diff_output = get_diff()
    
    # Initialize the conversation
    user_proxy.initiate_chat(
        assistant,
        message=f"""Please analyze this git diff and suggest:
        1. Which files should be included in the commit
        2. A clear commit message following conventional commit format
        
        Git diff:
        {diff_output}
        
        Format your response as:
        FILES:
        - file1
        - file2
        
        MESSAGE:
        type(scope): description
        
        TERMINATE"""
    )
    
    # Extract response
    last_message = assistant.last_message()
    if not last_message:
        return [], "No changes to commit"
        
    content = last_message.get("content", "")
    
    # Parse response
    files_section = ""
    message_section = ""
    
    if "FILES:" in content and "MESSAGE:" in content:
        sections = content.split("MESSAGE:")
        files_section = sections[0].split("FILES:")[1].strip()
        message_section = sections[1].strip()
    
    # Extract files
    files = [f.strip("- ").strip() for f in files_section.split("\n") if f.strip()]
    
    # Extract message
    message = message_section.split("\n")[0].strip()
    
    return files, message
