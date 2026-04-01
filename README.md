[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/abuzarmahmood/auto-commit/main.svg)](https://results.pre-commit.ci/latest/github/abuzarmahmood/auto-commit/main)

# Auto-Commit 🤖

A smart utility that makes creating Git commits easier by automatically analyzing your changes and suggesting meaningful commit messages. Powered by OpenAI's GPT models through the AutoGen framework.

## ✨ Features

- 📝 Automatically analyzes repository changes using `git diff`
- 💡 Generates contextual commit messages based on the changes
- ✅ Interactive confirmation before creating commits
- 🔄 Handles staging files and commit creation
- 🚀 Optional auto-confirmation and auto-pushing
- $$ Outputs cost of the API call for transparency

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- Git
- OpenAI API key (or compatible API key for other providers)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/abuzarmahmood/auto-commit.git
cd auto-commit
```

2. Create and activate a virtual environment:
```bash
python -m venv venv

# On Linux/Mac:
source venv/bin/activate

# On Windows:
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the application by creating a `config.json` file in the repository root:
```json
{
  "model": "gpt-4",
  "api_key_env_var": "OPENAI_API_KEY"
}
```

Available configuration options:
- `model`: The AI model to use (e.g., "gpt-4", "gpt-4o", "gpt-3.5-turbo")
- `api_key_env_var`: Name of the environment variable containing your API key

5. Set up your API key as an environment variable:
```bash
# On Linux/Mac:
export OPENAI_API_KEY='your-api-key-here'

# Or add the following line to your shell profile (e.g. .bashrc, .zshrc):
export OPENAI_API_KEY='your-api-key-here'

# On Windows:
set OPENAI_API_KEY=your-api-key-here
```

Note: The environment variable name should match the `api_key_env_var` value in your `config.json`.

6. Set up the bash function for easier access:
```bash
# Source the bash function file:
source src/autocommit.sh

# Add this line to your shell profile (e.g. .bashrc, .zshrc) to make it permanent:
source /path/to/repository/src/autocommit.sh
```

## 🎯 Usage

1. Make your changes to the repository files
2. Run the commit assistant:
```bash
python src/main.py [options]
```
3. Review the suggested files and commit message
4. Confirm to create the commit

### Command Line Options

- `-d, --directory`: Path to git repository (defaults to current directory)
- `-y, --yes`: Automatically confirm commit without prompting
- `-p, --push`: Automatically push changes after commit
- `-m, --message`: Seed text to guide commit message generation

Examples:
```bash
# Interactive mode (default)
python src/main.py

# Auto-commit without prompts
python src/main.py -y

# Auto-commit and push
python src/main.py -y -p

# Specify working directory
python src/main.py -d /path/to/repo

# Provide seed text for commit message
python src/main.py -m "Update user authentication"
```

## 🎬 Example Workflow

Here's a typical workflow using auto-commit:

```bash
# Make some changes to your code
echo "print('hello world')" > hello.py

# Stage your changes
git add hello.py

# Run auto-commit
python src/main.py

# You'll see output like this:
Suggested files to commit:
- hello.py

Suggested commit message:
feat: Add hello world script

Add a simple Python script that prints "hello world"

Proceed with commit? [y/N] y
Commit created successfully!

Push changes to remote? [y/N] y
Changes pushed successfully!

Operation cost: $0.0023
```

## ⚙️ Configuration

The `config.json` file allows you to customize the behavior of auto-commit:

```json
{
  "model": "gpt-4",
  "api_key_env_var": "OPENAI_API_KEY"
}
```

### Configuration Options

- **model**: Specify which AI model to use for generating commit messages
  - Examples: `"gpt-4"`, `"gpt-4o"`, `"gpt-3.5-turbo"`
  - Default: `"gpt-4o"` if not specified

- **api_key_env_var**: Name of the environment variable containing your API key
  - This allows you to use different API providers or multiple API keys
  - Default: `"OPENAI_API_KEY"` if not specified
  - Example: Set to `"ANTHROPIC_API_KEY"` if using Claude models

### Using Different Models or Providers

To switch models, simply update the `config.json` file:

```json
{
  "model": "gpt-3.5-turbo",
  "api_key_env_var": "OPENAI_API_KEY"
}
```

For different API providers (if supported by AutoGen), update both fields:

```json
{
  "model": "claude-3-opus",
  "api_key_env_var": "ANTHROPIC_API_KEY"
}
```

## 💡 Tips

- The tool works best when changes are focused and related
- You can always review and modify the suggested commit message
- Make sure your API key environment variable is properly set before running
- Adjust the model in `config.json` to balance between cost and quality

## 🛠️ Development

Want to contribute? Great! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
