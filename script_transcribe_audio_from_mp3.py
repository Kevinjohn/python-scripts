import os
import whisper
from colorama import Fore, Style
from _include_get_folder_path import get_folder_path
from _include_process_folders import run_function_on_all_subfolders


def transcribe_audio_files(folder_path):
    """Transcribe all MP3 files in a folder and save transcripts as text files."""
    try:
        audio_files = [file for file in os.listdir(folder_path) if file.lower().endswith('.mp3')]
        total_files = len(audio_files)

        if total_files == 0:
            print(f"{Fore.YELLOW}No MP3 files found in the folder: {folder_path}{Style.RESET_ALL}")
            return

        print(f"{Fore.GREEN}Starting to process {total_files} audio file(s) in {folder_path}...{Style.RESET_ALL}")

        model = whisper.load_model("base")

        for index, audio_file in enumerate(audio_files, start=1):
            input_path = os.path.join(folder_path, audio_file)
            output_path = os.path.join(folder_path, os.path.splitext(audio_file)[0] + ".txt")

            try:
                print(f"{Fore.CYAN}[{index}/{total_files}] Transcribing: {audio_file}{Style.RESET_ALL}")
                result = model.transcribe(input_path)
                with open(output_path, 'w', encoding='utf-8') as transcript_file:
                    transcript_file.write(result['text'])
                print(f"{Fore.GREEN}Saved transcript: {os.path.basename(output_path)}{Style.RESET_ALL}")
            except Exception as error:
                print(f"{Fore.RED}Error transcribing {audio_file}: {error}{Style.RESET_ALL}")

        print(f"{Fore.GREEN}Audio transcription completed successfully.{Style.RESET_ALL}")
    except Exception as error:
        print(f"{Fore.RED}Error: {error}{Style.RESET_ALL}")

folder_to_process = get_folder_path()
run_function_on_all_subfolders(folder_to_process, transcribe_audio_files)
