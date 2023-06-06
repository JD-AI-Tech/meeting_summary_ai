import os
import whisper

# https://analyzingalpha.com/openai-whisper-python-tutorial

def transcribe_audio_locally(audio_file):
    try:
        print("extract_audio() video_path: " + audio_file)
        full_file_path = os.path.splitext(audio_file)[0]
        print("full_file_path: " + full_file_path)

        model = whisper.load_model("base")
        print("Transcribing audio file, please wait!")
        result = model.transcribe(audio_file, fp16=False)
        print("about to write txt file!")
        text_file_name = full_file_path + ".txt"
        with open(text_file_name, "w") as f:
            f.write(result["text"])
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
    audio_file = 'C:/tmp/downloadedVideos/I Am Going Read Aloud.mp3'
    new_text_file = transcribe_audio_locally(audio_file)
    print("transcribe_audio() returned " + new_text_file)