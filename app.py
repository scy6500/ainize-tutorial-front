import streamlit as st
import requests


def send_request(text, length):
    api_url = 'https://main-ainize-tutorial-server-scy6500.endpoint.ainize.ai/predict'
    files = {
        'base_text': (None, text),
        'length': (None, length),
    }
    response = requests.post(api_url, files=files)
    status_code = response.status_code

    return status_code, response


st.title("GPT-2 Pride And Prejudice Demo")
st.header("Generate Pride and Prejudice story using GPT-2 model")

length_slider = st.sidebar.slider("Length", 0, 300)

base_story = st.text_input("Type Base Story", "\"I love him. He's not proud. I was wrong. I was entirely wrong about him.\"")
if st.button("Submit"):
    if length_slider == 0:
        st.warning("Please define the length")
    else:
        status_code, response = send_request(base_story, length_slider)
        if status_code == 200:
            prediction = response.json()
            st.success(prediction["prediction"])
        else:
            st.error(str(status_code) + " Error")

st.markdown('''
<div style="display:flex">
        <a target="_blank" href="https://github.com/scy6500/ainize-tutorial-server">
            <img width=150px src="https://i.imgur.com/AOHw2Yc.png"/>
        </a>
        <a style="margin-left:5px" target="_blank" href="https://ainize.ai/scy6500/ainize-tutorial-server?branch=main">
            <img width=130px src="https://i.imgur.com/F3r8BHB.png"/>
        </a>
<div>
    ''',
    unsafe_allow_html=True
)
