# progress_tracker.py

def update_day_progress(plan, day_number, task_status):
    """
    task_status = list of booleans for that day
    """

    current_day = plan[day_number - 1]
    carry_tasks = []

    for i, status in enumerate(task_status):
        current_day["Tasks"][i]["done"] = status
        if not status:
            carry_tasks.append(current_day["Tasks"][i]["task"])

   
    if carry_tasks and day_number < len(plan):
        next_day = plan[day_number]
        for task in carry_tasks:
            next_day["Tasks"].insert(
                0, {"task": f"Carry Forward: {task}", "done": False}
            )

    return plan
