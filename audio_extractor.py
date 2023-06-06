import os
from moviepy.editor import VideoFileClip
from pydub.exceptions import PydubException

def extract_audio(video_path):
    try:
        print("extract_audio() video_path .." + video_path)
        full_file_path = os.path.splitext(video_path)[0]
        print("full_file_path: " + full_file_path)

        video_clip = VideoFileClip(video_path)
        audio = video_clip.audio

        audio_file_name = full_file_path + ".mp3"
        audio.write_audiofile(audio_file_name)
        print("Closing files.")
        audio.close()
        video_clip.close()
        print("Audio extraction successful!")
        return  audio_file_name
    except (OSError, IOError) as e:
        print("Error: An error occurred while accessing the video file.")
        print(e)
    except PydubException as e:
        print("Error: An error occurred during audio extraction.")
        print(e)
    except Exception as e:
        print("Error: An error occurred !!")
        print(e)

if __name__ == "__main__":
    # usage:
    video_file = 'C:/tmp/downloadedVideos/I Am Going Read Aloud.mp4'
    audio_file_name = extract_audio(video_file)
    print("audio_extract() returned audio_file_name : " + audio_file_name)