import os

def process_folders(base_folder, process_function):
    """
    Process files in a folder and optionally in its subfolders.

    Args:
        base_folder (str): The path to the base folder to process.
        process_function (callable): The function to process files in a folder.
    """
    try:
        include_subfolders = input("Do you want the script to be run on all sub-folders? (y/n): ").strip().lower()
        
        if include_subfolders == "y":
            print(f"Processing {base_folder} and all its subfolders...")
            for root, _, _ in os.walk(base_folder):
                print(f"Processing folder: {root}")
                process_function(root)
        elif include_subfolders == "n":
            print(f"Processing only the base folder: {base_folder}")
            process_function(base_folder)
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    except Exception as error:
        print(f"Error in processing folders: {error}")
