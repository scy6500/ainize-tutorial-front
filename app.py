import streamlit as st
import requests


def send_request(text, length):
    files = {
        'base_text': (None, text),
        'length': (None, length),
    }
    response = requests.post('https://main-ainize-tutorial-server-scy6500.endpoint.ainize.ai/predict', files=files)
    status_code = response.status_code

    return status_code, response


st.title("GPT-2 Pride And Prejudice Demo")
st.header("Generate Pride and Prejudice story using GPT-2 model")

length_slider = st.sidebar.slider("Length", 0, 300)

base_story = st.text_input("Type Base Story", "Mr. Darcy was nice and danced only once with Elizabeth.")
if st.button("Submit"):
    text = base_story.title()
    status_code, response = send_request(text, length_slider)
    if status_code == 200:
        prediction = response.json()
        st.success(prediction["prediction"])
    else:
        st.error(str(status_code) + " Error")

