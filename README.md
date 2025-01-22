# D&D AI Game Master 🐉

An interactive Dungeons & Dragons game master powered by AI, built with Streamlit and Snowflake.

## Project Structure
```
dnd-ai-gm/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   └── utils/
│       ├── __init__.py
│       ├── dice.py
│       └── prompts.py
```

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/dnd-ai-gm.git
cd dnd-ai-gm
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your environment variables:
```bash
cp .env.example .env
# Edit .env with your Snowflake credentials
```

5. Run the app:
```bash
streamlit run src/app.py
```

## Requirements
- Python 3.8+
- Streamlit
- Snowflake account and credentials
- Access to Cortex services

## Features
- Interactive D&D gameplay
- AI-powered Game Master
- Dice rolling system
- Character management
- Rich narrative generation

## Contributing
Feel free to open issues or submit pull requests with improvements!
