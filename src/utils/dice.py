import random
import streamlit as st

def roll_dice(sides):
    """Roll a die with the specified number of sides and update the session state."""
    result = random.randint(1, sides)
    st.session_state.last_roll = {"dice": f"d{sides}", "result": result}
    return result

def get_roll_outcome(result, dice):
    """Get the dramatic outcome of a dice roll."""
    if result == 20 and dice == "d20":
        return "⭐ CRITICAL SUCCESS! ⭐"
    elif result == 1 and dice == "d20":
        return "💥 CRITICAL FAILURE! 💥"
    elif result >= (int(dice[1:]) * 0.75):
        return "✨ Excellent Roll!"
    elif result <= (int(dice[1:]) * 0.25):
        return "😰 Poor Roll..."
    else:
        return "🎯 Decent Roll"
