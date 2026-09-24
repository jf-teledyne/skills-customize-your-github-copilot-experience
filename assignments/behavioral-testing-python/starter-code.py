"""A small task-list module for practicing behavioral testing."""


def add_task(tasks, title, priority="normal"):
    """Add a task and return the new task."""
    if not title.strip():
        raise ValueError("Task title cannot be empty")

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "completed": False,
    }
    tasks.append(task)
    return task


def complete_task(tasks, task_id):
    """Mark a task as complete and report whether a task was changed."""
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return True
    return False


def list_tasks(tasks, completed=None):
    """Return all tasks or tasks matching a completion status."""
    if completed:
        return [task for task in tasks if task["completed"]]
    return list(tasks)
