import os
import subprocess
from colorama import Fore, Style
from _include_process_folders import process_folders
from _include_get_folder_path import get_folder_path

def convert_video_to_mp3(folder_path):
    """Convert all video files in a folder to MP3 format."""
    try:
        video_extensions = ('.mp4', '.mov', '.avi', '.mkv')
        video_files = [file for file in os.listdir(folder_path) if file.lower().endswith(video_extensions)]
        total_files = len(video_files)

        if total_files == 0:
            print(f"{Fore.YELLOW}No video files found in the folder: {folder_path}{Style.RESET_ALL}")
            return

        print(f"{Fore.GREEN}Starting to process {total_files} video file(s) in {folder_path}...{Style.RESET_ALL}")

        for index, video_file in enumerate(video_files, start=1):
            input_path = os.path.join(folder_path, video_file)
            output_path = os.path.join(folder_path, os.path.splitext(video_file)[0] + ".mp3")

            try:
                subprocess.run(
                    ["ffmpeg", "-i", input_path, "-q:a", "0", "-map", "a", output_path],
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                print(f"{Fore.CYAN}[{index}/{total_files}] Converted: {video_file} -> {os.path.basename(output_path)}{Style.RESET_ALL}")
            except subprocess.CalledProcessError as error:
                print(f"{Fore.RED}Error converting {video_file}: {error}{Style.RESET_ALL}")

        print(f"{Fore.GREEN}Video-to-MP3 conversion completed successfully.{Style.RESET_ALL}")
    except Exception as error:
        print(f"{Fore.RED}Error: {error}{Style.RESET_ALL}")

folder_to_process = get_folder_path()
process_folders(folder_to_process, convert_video_to_mp3)
