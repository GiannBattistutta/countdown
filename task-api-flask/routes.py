"""
routes.py - API routes

This module defines all the API endpoints for the Task API.
Each function handles a specific HTTP request.
"""

from typing import Any

from flask import Blueprint, jsonify, request

import service


# Create a Blueprint for all task-related routes
# This helps organize routes into modular groups
tasks_bp = Blueprint("tasks", __name__)


def create_response(data: Any, status_code: int = 200, error: str = None) -> tuple:
    """
    Create a standardized JSON response.
    
    Args:
        data: The data to include in the response.
        status_code: HTTP status code.
        error: Optional error message.
    
    Returns:
        Tuple of (response_dict, status_code).
    """
    if error:
        return {"error": error}, status_code
    
    return data, status_code


@tasks_bp.route("/tasks", methods=["GET"])
def get_all_tasks():
    """
    GET /tasks
    Get all tasks from the database.
    
    Returns:
        JSON response with all tasks.
    """
    tasks = service.get_all_tasks()
    return jsonify(tasks), 200


@tasks_bp.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    """
    GET /tasks/<id>
    Get a single task by its ID.
    
    Args:
        task_id: The ID of the task to retrieve.
    
    Returns:
        JSON response with the task or error message.
    """
    task = service.get_task_by_id(task_id)
    
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    
    return jsonify(task), 200


@tasks_bp.route("/tasks", methods=["POST"])
def create_task():
    """
    POST /tasks
    Create a new task.
    
    Request body should contain:
        - title: string (required)
        - description: string (required)
    
    Returns:
        JSON response with the created task or error message.
    """
    # Get JSON data from request
    data = request.get_json()
    
    if data is None:
        return jsonify({"error": "Request body must be JSON"}), 400
    
    # Extract fields
    title = data.get("title")
    description = data.get("description")
    
    # Create task through service layer
    task, error = service.create_task(title, description)
    
    if error:
        return jsonify({"error": error}), 400
    
    return jsonify(task), 201


@tasks_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    """
    PUT /tasks/<id>
    Update an existing task.
    
    Request body should contain:
        - title: string (required)
        - description: string (required)
    
    Args:
        task_id: The ID of the task to update.
    
    Returns:
        JSON response with the updated task or error message.
    """
    # Get JSON data from request
    data = request.get_json()
    
    if data is None:
        return jsonify({"error": "Request body must be JSON"}), 400
    
    # Extract fields
    title = data.get("title")
    description = data.get("description")
    
    # Update task through service layer
    task, error = service.update_task(task_id, title, description)
    
    if error:
        # Check if it's a "not found" error
        if "not found" in error.lower():
            return jsonify({"error": error}), 404
        return jsonify({"error": error}), 400
    
    return jsonify(task), 200


@tasks_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """
    DELETE /tasks/<id>
    Delete a task by its ID.
    
    Args:
        task_id: The ID of the task to delete.
    
    Returns:
        JSON response confirming deletion or error message.
    """
    success, error = service.delete_task(task_id)
    
    if error:
        # Check if it's a "not found" error
        if "not found" in error.lower():
            return jsonify({"error": error}), 404
        return jsonify({"error": error}), 400
    
    return jsonify({"message": "Task deleted successfully"}), 200


@tasks_bp.route("/tasks/<int:task_id>/complete", methods=["PATCH"])
def complete_task(task_id):
    """
    PATCH /tasks/<id>/complete
    Mark a task as completed.
    
    Args:
        task_id: The ID of the task to mark as completed.
    
    Returns:
        JSON response with the updated task or error message.
    """
    task, error = service.complete_task(task_id)
    
    if error:
        # Check if it's a "not found" error
        if "not found" in error.lower():
            return jsonify({"error": error}), 404
        return jsonify({"error": error}), 400
    
    return jsonify(task), 200