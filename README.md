Utility to make creating commits easier.
Uses an autogen agent to create a commit message based on the changes made to the repository.

Contains tools to:
 - Find the changes made to the repository (git diff)
 - Create a commit message based on the changes made
 - Create a commit with the message

## Installation

1. Make sure you have Python 3.6+ and pip installed on your system.

2. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

3. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# OR
.\venv\Scripts\activate  # On Windows
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. You're ready to use the tool! Remember to activate the virtual environment whenever you want to use it.

To deactivate the virtual environment when you're done:
```bash
deactivate
```
