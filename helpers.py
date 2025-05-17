import os
import json
import streamlit as st
from settings import *
import assist
import requests
from rembg import remove
from PIL import Image


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


def get_cocktail_image_path(cocktail):
    """Given a Cocktail object, get the path to the image for that cocktail.
    Image file name is assumed to be the normal_name in lower snake_case"""
    file_name = f'{cocktail.get("normal_name", "").lower().replace(" ", "_")}.png'
    path = os.path.join(LOGO_FOLDER, file_name)
    return path


def get_valid_cocktails():
    cocktail_data = load_cocktails().get('cocktails', [])
    cocktails = []
    for cocktail in cocktail_data:
        if os.path.exists(get_cocktail_image_path(cocktail)):
            cocktails.append(cocktail)
    return cocktails


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


def generate_image(normal_name):
    safe_cname = get_safe_name(normal_name)
    filename = os.path.join(LOGO_FOLDER, f"{safe_cname}.png")

    if os.path.exists(filename):
        # If it already exists, skip generation
        return filename
    else:
        prompt = (
            f"A realistic illustration of a {normal_name} cocktail on a plain white background. "
            "The lighting and shading create depth and realism, making the drink appear fresh and inviting."
        )
        try:
            # 1) Generate the image URL
            image_url = assist.generate_image(prompt)

            # 2) Download + remove background in memory
            img_data = requests.get(image_url).content
            from io import BytesIO
            with Image.open(BytesIO(img_data)).convert("RGBA") as original_img:
                bg_removed = remove(original_img)
                bg_removed.save(filename, "PNG")

            return filename

        except Exception as e:
            pass