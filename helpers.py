import os
import json
import streamlit as st
from settings import *


def load_saved_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except Exception as e:
            st.error(f"Error loading configuration: {e}")
    return {}


def save_config(data):
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        st.error(f"Error saving configuration: {e}")


def load_cocktails():
    if os.path.exists(COCKTAILS_FILE):
        try:
            with open(COCKTAILS_FILE, "r") as f:
                return json.load(f)
        except Exception as e:
            st.error(f"Error loading cocktails: {e}")
    return {}


def save_cocktails(data, append=True):
    """Save the given list of cocktails to the cocktails file."""
    try:
        cocktails = load_cocktails()
        with open(COCKTAILS_FILE, "w") as f:
            if append:
                cocktails['cocktails'] += data['cocktails']
            else:
                cocktails = data
            json.dump(cocktails, f, indent=2)
    except Exception as e:
        st.error(f"Error saving cocktails: {e}")


def get_safe_name(name):
    """Convert a cocktail name to a safe filename-friendly string."""
    return name.lower().replace(" ", "_")