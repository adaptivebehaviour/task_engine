import random
import streamlit as st
from dataclasses import dataclass

from components import Checkbox, Selectbox

st.set_page_config(layout="wide")

DEFAULT_MODEL = "random"
MODELS = ["random"]


def _reset_session():
    """Clear all state and reinitialise for the newly selected model."""


def _on_default_toggle():
    if st.session_state.default_checkbox:
        st.session_state.default_model = model_select.value
    else:
        st.session_state.default_model = DEFAULT_MODEL


# ── Layout CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
header[data-testid="stHeader"] { display: none; }

html, body { height: 100%; overflow: hidden; }

section[data-testid="stMain"] {
    height: 100vh;
    overflow: hidden;
}

.block-container {
    height: 100vh;
    padding: 0 !important;
    max-width: 100% !important;
    display: flex;
    flex-direction: column;
}

.block-container > div[data-testid="stVerticalBlock"] {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
}

.block-container > div[data-testid="stVerticalBlock"]
    > div[data-testid="stVerticalBlock"]:first-child {
    flex: 0 0 20%;
    overflow: auto;
    padding: 0.75rem 1rem;
    box-sizing: border-box;
    border-bottom: 1px solid rgba(49, 51, 63, 0.2);
}

.block-container > div[data-testid="stVerticalBlock"]
    > div[data-testid="stVerticalBlock"]:last-child {
    flex: 1;
    overflow: auto;
    padding: 0.75rem 1rem;
    box-sizing: border-box;
}
</style>
""", unsafe_allow_html=True)


# ── Components ─────────────────────────────────────────────────────────────────
model_select = Selectbox(
    label="Model",
    options=MODELS,
    key="mode",
    default=DEFAULT_MODEL,
    on_change=_reset_session,
)

default_cb = Checkbox(
    label="Default",
    key="default_checkbox",
    on_change=_on_default_toggle,
)


# ── Session-state initialisation ───────────────────────────────────────────────
if "default_model" not in st.session_state:
    st.session_state.default_model = DEFAULT_MODEL

# Checkbox state is always derived: checked iff the selected model is the default.
st.session_state.default_checkbox = (
    model_select.value == st.session_state.default_model
)


# ── Areas ──────────────────────────────────────────────────────────────────────
controls = st.container()
model_area = st.container()

with controls:
    col_model, col_check, _ = st.columns([1, 1, 8], vertical_alignment="bottom")
    with col_model:
        model_select.render()
    with col_check:
        default_cb.render()

with model_area:
    st.caption("MODEL")
