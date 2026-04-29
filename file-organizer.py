#!/usr/bin/env python3
"""
File Organizer - A simple command-line tool to organize files by category.
"""

import os
import shutil
from pathlib import Path

# Define file categories and their extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
}


def get_folder_path():
    """
    Ask the user for a folder path and validate if it exists.
    Returns the folder path as a string.
    """
    while True:
        folder_path = input("\nEnter the folder path to organize: ").strip()
        
        # Check if the path exists
        if not os.path.exists(folder_path):
            print(f"❌ Error: The folder '{folder_path}' does not exist.")
            continue
        
        # Check if the path is a directory
        if not os.path.isdir(folder_path):
            print(f"❌ Error: '{folder_path}' is not a directory.")
            continue
        
        return folder_path


def get_category(file_extension):
    """
    Determine the category of a file based on its extension.
    Returns the category name or 'Others' if unknown.
    """
    # Convert extension to lowercase for comparison
    file_extension = file_extension.lower()
    
    # Check each category
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension in extensions:
            return category
    
    # Return 'Others' for unknown extensions
    return "Others"


def create_category_folders(folder_path):
    """
    Create category folders inside the specified folder.
    """
    # Add 'Others' to the categories
    categories = list(FILE_CATEGORIES.keys()) + ["Others"]
    
    for category in categories:
        category_folder = os.path.join(folder_path, category)
        
        # Create the folder if it doesn't exist
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
            print(f"✓ Created folder: {category}")


def organize_files(folder_path):
    """
    Move files from the folder into their category folders.
    Returns a dictionary with the count of moved files per category.
    """
    # Dictionary to count moved files
    moved_files = {
        "Images": 0,
        "Documents": 0,
        "Videos": 0,
        "Audio": 0,
        "Archives": 0,
        "Others": 0,
    }
    
    # List all items in the folder
    items = os.listdir(folder_path)
    
    for item in items:
        item_path = os.path.join(folder_path, item)
        
        # Skip if it's a directory (we only move files)
        if os.path.isdir(item_path):
            continue
        
        # Get the file extension
        file_extension = os.path.splitext(item)[1]
        
        # Get the category for this file
        category = get_category(file_extension)
        
        # Create the destination folder path
        destination_folder = os.path.join(folder_path, category)
        destination_path = os.path.join(destination_folder, item)
        
        # Move the file
        try:
            shutil.move(item_path, destination_path)
            moved_files[category] += 1
            print(f"  → Moved: {item} → {category}/")
        except Exception as error:
            print(f"❌ Error moving {item}: {error}")
    
    return moved_files


def print_summary(moved_files):
    """
    Print a summary of how many files were moved to each category.
    """
    print("\n" + "=" * 50)
    print("📊 ORGANIZATION SUMMARY")
    print("=" * 50)
    
    total_files = 0
    for category, count in moved_files.items():
        if count > 0:
            print(f"  {category}: {count} file(s)")
            total_files += count
    
    print("-" * 50)
    print(f"  Total files moved: {total_files}")
    print("=" * 50)
    print("✓ File organization complete!\n")


def main():
    """
    Main function that runs the file organizer.
    """
    print("\n" + "=" * 50)
    print("📁 FILE ORGANIZER")
    print("=" * 50)
    print("This tool will organize files in a folder by category.")
    print("=" * 50)
    
    # Get the folder path from the user
    folder_path = get_folder_path()
    
    print(f"\n✓ Selected folder: {folder_path}")
    print("\nCreating category folders...")
    
    # Create category folders
    create_category_folders(folder_path)
    
    print("\nOrganizing files...")
    
    # Organize the files
    moved_files = organize_files(folder_path)
    
    # Print the summary
    print_summary(moved_files)


# Entry point of the script
if __name__ == "__main__":
    main()
