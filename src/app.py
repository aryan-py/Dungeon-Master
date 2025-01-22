import streamlit as st
from snowflake.core import Root
from snowflake.cortex import Complete
from snowflake.snowpark.context import get_active_session
import snowflake.connector
from config import SNOWFLAKE_CONFIG, MODELS, DND_DICE, DICE_ICONS, CHAT_ICONS
from utils.dice import roll_dice, get_roll_outcome
from utils.prompts import create_gm_prompt, create_history_summary_prompt

# Initialize Snowflake connection
def init_snowflake():
    """Initialize Snowflake connection and return session."""
    try:
        session = snowflake.connector.connect(
            **SNOWFLAKE_CONFIG
        )
        return get_active_session()
    except Exception as e:
        st.error(f"Failed to connect to Snowflake: {str(e)}")
        return None

def init_messages():
    """Initialize the session state for chat messages."""
    if st.session_state.clear_conversation or "messages" not in st.session_state:
        st.session_state.messages = []

def init_service_metadata(session):
    """Initialize the session state for cortex search service metadata."""
    if "service_metadata" not in st.session_state:
        try:
            services = session.sql("SHOW CORTEX SEARCH SERVICES;").collect()
            service_metadata = []
            if services:
                for s in services:
                    svc_name = s["name"]
                    svc_search_col = session.sql(
                        f"DESC CORTEX SEARCH SERVICE {svc_name};"
                    ).collect()[0]["search_column"]
                    service_metadata.append(
                        {"name": svc_name, "search_column": svc_search_col}
                    )
            st.session_state.service_metadata = service_metadata
        except Exception as e:
            st.error(f"Failed to initialize service metadata: {str(e)}")
            st.session_state.service_metadata = []

def init_config_options():
    """Initialize the configuration options in the Streamlit sidebar."""
    # Your existing init_config_options code here

def query_cortex_search_service(session, query, columns=[], filter={}):
    """Query the selected cortex search service."""
    # Your existing query_cortex_search_service code here

def get_chat_history():
    """Get chat history from session state."""
    # Your existing get_chat_history code here

def complete(model, prompt):
    """Complete the prompt using the specified model."""
    return Complete(model, prompt).replace("$", "\$")

def make_chat_history_summary(chat_history, question):
    """Make a summary of chat history."""
    prompt = create_history_summary_prompt(chat_history, question)
    summary = complete(st.session_state.model_name, prompt)
    
    if st.session_state.debug:
        st.sidebar.text_area("Chat history summary", summary.replace("$", "\$"), height=150)
    
    return summary

def create_prompt(user_question):
    """Create the main prompt for the AI."""
    # Your existing create_prompt code here

def main():
    """Main application function."""
    st.set_page_config(
        page_title="D&D AI Game Master",
        page_icon="🐉",
        layout="wide"
    )
    
    st.title("🐉 The Realm of Digital Dragons")
    st.markdown("*Where AI meets Fantasy in an Epic Adventure*")

    # Initialize Snowflake session
    session = init_snowflake()
    if not session:
        st.error("Failed to initialize Snowflake session. Please check your credentials.")
        return

    root = Root(session)
    
    init_service_metadata(session)
    init_config_options()
    init_messages()

    # Your existing main function code here

if __name__ == "__main__":
    main()
