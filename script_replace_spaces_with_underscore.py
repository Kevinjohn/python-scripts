import os
from colorama import init, Fore, Style
from _include_get_folder_path import get_folder_path
from _include_process_folders import run_function_on_all_subfolders

init(autoreset=True)

def replace_spaces_with_underscores(folder_path):
    """Replace spaces in filenames with underscores in the given folder."""
    try:
        file_list = os.listdir(folder_path)
        total_files = len(file_list)

        if total_files == 0:
            print(f"{Fore.YELLOW}No files found in the folder: {folder_path}{Style.RESET_ALL}")
            return

        print(f"{Fore.GREEN}Starting to process {total_files} file(s) in {folder_path}...{Style.RESET_ALL}")

        for index, file_name in enumerate(file_list, start=1):
            original_path = os.path.join(folder_path, file_name)
            if os.path.isfile(original_path):
                new_name = file_name.replace(" ", "_")
                new_path = os.path.join(folder_path, new_name)
                os.rename(original_path, new_path)
                print(f"{Fore.CYAN}[{index}/{total_files}] Renamed: {file_name} -> {new_name}{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}[{index}/{total_files}] Skipped (not a file): {file_name}{Style.RESET_ALL}")

        print(f"{Fore.GREEN}File renaming completed successfully.{Style.RESET_ALL}")
    except Exception as error:
        print(f"{Fore.RED}Error: {error}{Style.RESET_ALL}")

folder_to_process = get_folder_path()
run_function_on_all_subfolders(folder_to_process, replace_spaces_with_underscores)
