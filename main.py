import os
import streamlit as st
from audio_extractor import extract_audio
from audio_to_text import transcribe_audio_locally
from transcribe_to_text import transcribe_audio_api
from utils import read_text_file
from file_utility import create_directory
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ['OPENAI_API_KEY'] = st.secrets["apikey"]

data_directory = 'data'
create_directory(data_directory)
first_prompt = "Please provide a summary and bullet points for the following text: "

# set creativity level
title_template = PromptTemplate(
    input_variables = ['topic'],
    template ='Please provide a summary and bullet points for the following text {topic}'
)

llm = OpenAI(temperature=0.6)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)

st.title('🦜🔗 Meeting Notes Generator')
st.subheader("Please upload meeting video file to summarize (mp4)")

with st.sidebar:
    st.title('About')
    st.markdown('''
        This is a Proof Of Concept (POC). 
        The goal is to use AI to generate a Summary and Bullet points of the uploaded video.
        - OpenAI's Whisper transcribes audio to text.
        - OpanAI's GPT API generates Summary & bullet.
              
    ''')
    st.title('Technology')
    st.markdown('''
        Developed by Jorge Duenas using:
        - [OpenAI GPT-3.5 API](https://openai.com/product)
        - [OpenAI Whisper API](https://openai.com/research/whisper)
        - [Streamlit.io](https://streamlit.io/)
        - [LangChain](https://python.langchain.com/en/latest/index.html)
        - [Python](https://www.python.org/)
        - [Anaconda](https://www.anaconda.com/)   
        - [Pycharm IDE](https://www.jetbrains.com/pycharm/)   
    ''')

uploaded_file = st.file_uploader('', type=['mp4'])
# extract audio from uploaded video (mp4) file
if uploaded_file is not None:
    with open(os.path.join(data_directory, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    saved_file_name = data_directory + "/" + uploaded_file.name

    # extra audio from MP4
    st.write("Extracting audio from video file:  " + saved_file_name)
    new_audio_file = extract_audio(saved_file_name)

    # transcribing audio (mp3) into text file
    st.write("Transcribing audio to text using OpenAI's Whisper neural net ")
    # new_text_file = transcribe_audio_locally(new_audio_file)
    new_text_file = transcribe_audio_api(new_audio_file)

    # Read transcribed text for Openai prompt
    second_prompt = read_text_file(new_text_file)

    st.write("Making call to OpenAI GPT-3.5 API to generate summary and bullet points ")
    # submit to OpenAI for Summary and bullets
    response = title_chain.run(topic=second_prompt)

    with st.expander("Prompt submitted to OpenAI's GPT-3.5 API"):
        st.info(first_prompt)

    with st.expander("Transcribed text"):
        st.info(second_prompt)

    st.write(response)
