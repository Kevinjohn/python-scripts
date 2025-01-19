import os

def get_folder_path():
    """
    Prompt the user for a folder path and validate it.
    Handles both Mac and Windows file path structures.
    Returns:
        str: A validated folder path.
    """
    while True:
        folder_path = input("Please enter the folder path: ").strip()
        folder_path = os.path.normpath(folder_path)  # Normalize path for OS compatibility

        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            print(f"Folder path verified: {folder_path}")
            return folder_path
        else:
            print("Invalid folder path. Please try again.")
