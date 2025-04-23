import streamlit as st
import random
import string

st.title("🔐 Password Generator")

length = st.slider("Select password length", min_value=4, max_value=32, value=12)
use_uppercase = st.checkbox("Include Uppercase Letters", value=True)
use_lowercase = st.checkbox("Include Lowercase Letters", value=True)
use_digits = st.checkbox("Include Numbers", value=True)
use_symbols = st.checkbox("Include Symbols", value=True)

if st.button("Generate Password"):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if characters:
        password = ''.join(random.choice(characters) for _ in range(length))
        st.success("Generated Password:")
        st.code(password)
    else:
        st.error("Please select at least one character type.")

# Check out the output:
# https://passwordgeneratorpythonproject-wyowzurdsh8u2tuy2fxl3c.streamlit.app/
