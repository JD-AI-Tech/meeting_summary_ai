import os

def delete_processed_files(directory):
    print(f"Removing processed files from: {directory}")
    try:
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(file_name)[1]
                if file_extension.lower() in ['.txt', '.mp4', '.mp3']:
                    os.remove(file_path)
                    print(f"Deleted file: {file_name}")
    except FileNotFoundError:
        print("Directory not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    #  usage:
    directory_path = "./data"  # Replace with the actual directory path
    delete_processed_files(directory_path)
