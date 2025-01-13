# Auto-Commit 🤖

A smart utility that makes creating Git commits easier by automatically analyzing your changes and suggesting meaningful commit messages. Powered by OpenAI's GPT models through the AutoGen framework.

## ✨ Features

- 📝 Automatically analyzes repository changes using `git diff`
- 💡 Generates contextual commit messages based on the changes
- ✅ Interactive confirmation before creating commits
- 🔄 Handles staging files and commit creation

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- Git
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
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

4. Set up your OpenAI API key:
```bash
# On Linux/Mac:
export OPENAI_API_KEY='your-api-key-here'

# Or add the following line to your shell profile (e.g. .bashrc, .zshrc):
export OPENAI_API_KEY='your-api-key-here'

# On Windows:
set OPENAI_API_KEY=your-api-key-here
```

## 🎯 Usage

1. Make your changes to the repository files
2. Run the commit assistant:
```bash
python src/main.py
```
3. Review the suggested files and commit message
4. Confirm to create the commit

## 💡 Tips

- The tool works best when changes are focused and related
- You can always review and modify the suggested commit message
- Make sure your OpenAI API key is properly set before running

## 🛠️ Development

Want to contribute? Great! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
