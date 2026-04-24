"""
storage.py - File handling and JSON operations

This module handles all file operations for the Task API.
It provides functions to read and write tasks to a JSON file.
"""

import json
import os
from typing import List, Dict, Any, Optional


# File path for storing tasks
DATA_FILE = "tasks.json"


def read_tasks() -> List[Dict[str, Any]]:
    """
    Read all tasks from the JSON file.
    
    Returns:
        List of task dictionaries. Returns empty list if file doesn't exist.
    """
    # Check if file exists
    if not os.path.exists(DATA_FILE):
        return []
    
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            # Ensure we always return a list
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, IOError):
        # If there's any error reading the file, return empty list
        return []


def write_tasks(tasks: List[Dict[str, Any]]) -> bool:
    """
    Write all tasks to the JSON file.
    
    Args:
        tasks: List of task dictionaries to save.
    
    Returns:
        True if successful, False otherwise.
    """
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)
        return True
    except IOError:
        return False


def get_task_by_id(task_id: int) -> Optional[Dict[str, Any]]:
    """
    Find a specific task by its ID.
    
    Args:
        task_id: The ID of the task to find.
    
    Returns:
        Task dictionary if found, None otherwise.
    """
    tasks = read_tasks()
    for task in tasks:
        if task.get("id") == task_id:
            return task
    return None


def get_next_id() -> int:
    """
    Generate the next available task ID.
    
    Returns:
        The next available integer ID.
    """
    tasks = read_tasks()
    if not tasks:
        return 1
    
    # Find the maximum ID and add 1
    max_id = 0
    for task in tasks:
        task_id = task.get("id", 0)
        if task_id > max_id:
            max_id = task_id
    
    return max_id + 1