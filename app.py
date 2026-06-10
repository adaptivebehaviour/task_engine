import random
import streamlit as st
from dataclasses import dataclass

st.set_page_config(layout="wide")

DEFAULT_MODEL = "random"

def _reset_session():
    """Clear all state and reinitialise for the newly selected model."""
    _m = st.session_state.get("mode", DEFAULT_MODEL)


# ── Session-state initialisation ───────────────────────────────────────────────
if "mode" not in st.session_state:
    st.session_state.mode = DEFAULT_MODEL

