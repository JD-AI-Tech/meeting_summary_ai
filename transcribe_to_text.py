import openai
import os
import streamlit as st

def transcribe_audio_api(audio_file_path):
    try:
        os.environ['OPENAI_API_KEY'] = st.secrets["apikey"]

        print("extract_audio() audio_file_path: " + audio_file_path)
        full_file_path = os.path.splitext(audio_file_path)[0]
        print("full_file_path: " + full_file_path)

        os.environ['OPENAI_API_KEY'] = st.secrets["apikey"]
        openai.api_key = os.environ['OPENAI_API_KEY']
        audio_file = open(audio_file_path, "rb")
        result = openai.Audio.transcribe(model="whisper-1", file=audio_file, response_format="text")
        print("about to write txt file!")
        text_file_name = full_file_path + ".txt"
        with open(text_file_name, "w") as f:
            f.write(result)
        print("Transcription saved successfully!")
        return text_file_name
    except (OSError, IOError) as e:
        print("Error: An error occurred while accessing the video file.")
        print(e)
    except Exception as e:
        print("Error: An error occurred during transcription.")
        print(e)

if __name__ == "__main__":
    # usage:
    audio_file_path = 'C:/tmp/downloadedVideos/I Am Going Read Aloud.mp3'
    new_text_file = transcribe_audio_api(audio_file_path)
    print("transcribe_audio_api() returned " + new_text_file)
