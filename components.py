import streamlit as st


class Selectbox:
    """A selectbox that initialises its own session-state key.

    Args:
        label:     Label shown above the selectbox.
        options:   Sequence of selectable options.
        key:       Session-state key for the selected value.
        default:   Initial value; defaults to the first option if omitted.
        on_change: Called whenever the selection changes.
    """

    def __init__(self, label, options, key, default=None, on_change=None):
        self.label = label
        self.options = list(options)
        self.key = key
        self.default = default if default is not None else self.options[0]
        self.on_change = on_change
        self._init_state()

    def _init_state(self):
        if self.key not in st.session_state:
            st.session_state[self.key] = self.default

    def render(self):
        st.selectbox(
            self.label,
            options=self.options,
            key=self.key,
            on_change=self.on_change,
        )

    @property
    def value(self):
        """Currently selected value."""
        return st.session_state.get(self.key, self.default)


class Checkbox:
    """A checkbox that initialises its own session-state key.

    Args:
        label:     Label shown next to the checkbox.
        key:       Session-state key for the checked state.
        default:   Initial value; defaults to False.
        on_change: Called whenever the checkbox state changes.
    """

    def __init__(self, label, key, default=False, on_change=None):
        self.label = label
        self.key = key
        self.default = default
        self.on_change = on_change
        self._init_state()

    def _init_state(self):
        if self.key not in st.session_state:
            st.session_state[self.key] = self.default

    def render(self):
        st.checkbox(
            self.label,
            key=self.key,
            on_change=self.on_change,
        )

    @property
    def value(self):
        """Current checked state."""
        return st.session_state.get(self.key, self.default)
