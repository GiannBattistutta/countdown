"""
service.py - Business logic

This module contains the business logic for task operations.
It acts as an intermediary between routes and storage layers.
"""

import time
from typing import List, Dict, Any, Optional, Tuple

import storage


def get_all_tasks() -> List[Dict[str, Any]]:
    """
    Get all tasks from storage.
    
    Returns:
        List of all tasks.
    """
    return storage.read_tasks()


def get_task_by_id(task_id: int) -> Optional[Dict[str, Any]]:
    """
    Get a single task by its ID.
    
    Args:
        task_id: The ID of the task to retrieve.
    
    Returns:
        Task dictionary if found, None otherwise.
    """
    return storage.get_task_by_id(task_id)


def create_task(title: str, description: str) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    """
    Create a new task.
    
    Args:
        title: The title of the task.
        description: The description of the task.
    
    Returns:
        Tuple of (task, error_message). Task is None if error occurred.
    """
    # Validate input
    if not title or not title.strip():
        return None, "Title is required"
    
    if not description or not description.strip():
        return None, "Description is required"
    
    # Create task dictionary
    task = {
        "id": storage.get_next_id(),
        "title": title.strip(),
        "description": description.strip(),
        "completed": False,
        "created_at": int(time.time())
    }
    
    # Read existing tasks
    tasks = storage.read_tasks()
    
    # Add new task
    tasks.append(task)
    
    # Save to file
    if storage.write_tasks(tasks):
        return task, None
    
    return None, "Failed to save task"


def update_task(task_id: int, title: str, description: str) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    """
    Update an existing task.
    
    Args:
        task_id: The ID of the task to update.
        title: New title for the task.
        description: New description for the task.
    
    Returns:
        Tuple of (task, error_message). Task is None if error occurred.
    """
    # Validate input
    if not title or not title.strip():
        return None, "Title is required"
    
    if not description or not description.strip():
        return None, "Description is required"
    
    # Read all tasks
    tasks = storage.read_tasks()
    
    # Find and update the task
    for i, task in enumerate(tasks):
        if task.get("id") == task_id:
            tasks[i]["title"] = title.strip()
            tasks[i]["description"] = description.strip()
            
            # Save to file
            if storage.write_tasks(tasks):
                return tasks[i], None
            
            return None, "Failed to save task"
    
    return None, "Task not found"


def delete_task(task_id: int) -> Tuple[bool, Optional[str]]:
    """
    Delete a task by its ID.
    
    Args:
        task_id: The ID of the task to delete.
    
    Returns:
        Tuple of (success, error_message).
    """
    # Read all tasks
    tasks = storage.read_tasks()
    
    # Find and remove the task
    for i, task in enumerate(tasks):
        if task.get("id") == task_id:
            tasks.pop(i)
            
            # Save to file
            if storage.write_tasks(tasks):
                return True, None
            
            return False, "Failed to save task"
    
    return False, "Task not found"


def complete_task(task_id: int) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    """
    Mark a task as completed.
    
    Args:
        task_id: The ID of the task to mark as completed.
    
    Returns:
        Tuple of (task, error_message). Task is None if error occurred.
    """
    # Read all tasks
    tasks = storage.read_tasks()
    
    # Find and update the task
    for i, task in enumerate(tasks):
        if task.get("id") == task_id:
            tasks[i]["completed"] = True
            
            # Save to file
            if storage.write_tasks(tasks):
                return tasks[i], None
            
            return None, "Failed to save task"
    
    return None, "Task not found"