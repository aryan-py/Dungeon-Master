import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Snowflake configuration
SNOWFLAKE_CONFIG = {
    "account": os.getenv("aryan-py"),
    "user": os.getenv("ARYANPY"),
    "password": os.getenv("Suchitra1"),
    "warehouse": os.getenv("cortex_search_tutorial_wh"),
    "database": os.getenv("cortex_search_tutorial_db"),
    "schema": os.getenv("cortex_search_tutorial_db.public.fomc")
}

# Model configuration
MODELS = [
    os.getenv("MODEL_NAME", "mistral-large2")
]

# Game configuration
DND_DICE = [4, 6, 8, 10, 12, 20]

# UI Configuration
DICE_ICONS = {
    4: "🔻",   # Tetrahedron
    6: "⬦",    # Cube
    8: "💎",   # Octahedron
    10: "🔟",  # Decahedron
    12: "⬙",   # Dodecahedron
    20: "🎲"   # Icosahedron
}

CHAT_ICONS = {
    "assistant": "🧙‍♂️",  # Wizard for the AI GM
    "user": "⚔️"      # Sword for the player
}
