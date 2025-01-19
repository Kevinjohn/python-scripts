import os
import subprocess
from colorama import init, Fore, Style
from _include_get_folder_path import get_folder_path
from _include_process_folders import run_function_on_all_subfolders

init(autoreset=True)


def convert_video_to_mp3(folder_path):
    """Convert all video files in a folder to MP3 format."""
    try:
        video_extensions = ('.mp4', '.mov', '.avi', '.mkv')
        video_files = [file for file in os.listdir(folder_path) if file.lower().endswith(video_extensions)]
        total_files = len(video_files)

        if total_files == 0:
            print(f"{Fore.YELLOW}No video files found in the folder: {folder_path}{Style.RESET_ALL}")
            return

        print(f"{Fore.YELLOW}Starting to process {total_files} video file(s) in {folder_path}...{Style.RESET_ALL}")

        for index, video_file in enumerate(video_files, start=1):
            input_path = os.path.join(folder_path, video_file)
            output_path = os.path.join(folder_path, os.path.splitext(video_file)[0] + ".mp3")

            print(f"[{index}/{total_files}] Starting processing of: {video_file} {Style.RESET_ALL}")                            


            try:
                # Get the audio streams
                print(f"{Fore.CYAN}* Checking audio streams in video file {Style.RESET_ALL}")
                probe_result = subprocess.run(
                    ["ffmpeg", "-i", input_path],
                    stderr=subprocess.PIPE, 
                    stdout=subprocess.DEVNULL, 
                    text=True
                )
                # print(f"{Fore.CYAN} probe_result.stderr = {probe_result.stderr} {Style.RESET_ALL}")


                # Select the first audio stream
                if "Stream #0:1" in probe_result.stderr:
                    print(f"{Fore.CYAN}* * Using Stream #0:1  {Style.RESET_ALL}")
                    audio_stream = "0:1"
                elif "Stream #0:2" in probe_result.stderr:
                    print(f"{Fore.CYAN}* * Using Stream #0:1  {Style.RESET_ALL}")
                    audio_stream = "0:2"
                else:
                    print(f"{Fore.RED}ERROR. No valid audio stream found for {video_file}. Skipping... {Style.RESET_ALL}")
                    continue

                # Convert video to MP3
                print(f"{Fore.CYAN}* Starting FFmpeg conversion {Style.RESET_ALL}")                
                subprocess.run(
                    ["ffmpeg", "-i", input_path, "-q:a", "0", "-map", audio_stream, output_path],
                    stderr=subprocess.PIPE, 
                    stdout=subprocess.DEVNULL,                     
                    check=True
                )
                print(f"{Fore.GREEN}* Output created: {os.path.basename(output_path)}{Style.RESET_ALL}")

            except Exception as e:
                #print(f"{Fore.RED}Error converting {video_file}: {error}{Style.RESET_ALL}")
                #print(f"{Fore.WHITE}FFmpeg Output: {error.stderr.decode('utf-8')}{Style.RESET_ALL}")
                print(f"{Fore.RED}Error converting {video_file}: {e}{Style.RESET_ALL}")
                print(f"{Fore.WHITE}FFmpeg Output: {str(e)}{Style.RESET_ALL}")

                print("\n\n")                


        print(f"{Fore.GREEN}Video-to-MP3 conversion completed successfully.{Style.RESET_ALL}")
    except Exception as error:
        print(f"{Fore.RED}Error: {error}{Style.RESET_ALL}")

folder_to_process = get_folder_path()
run_function_on_all_subfolders(folder_to_process, convert_video_to_mp3)
