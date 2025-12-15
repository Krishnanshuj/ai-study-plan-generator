# planner_engine.py

def allocate_days(total_days, subject_levels):
    """
    Allocate study weight based on weakness level
    """
    weights = {"Weak": 0.5, "Medium": 0.3, "Strong": 0.2}
    total_weight = sum(weights[v] for v in subject_levels.values())

    allocation = {}
    for subject, level in subject_levels.items():
        allocation[subject] = max(
            1, int((weights[level] / total_weight) * total_days)
        )

    return allocation


def generate_study_plan(
    total_days,
    allocation,
    syllabus,
    daily_questions,
    total_mocks
):
    """
    Generates EXACTLY total_days calendar days
    Includes:
    - Concept task
    - Practice task
    - Weekly revision
    - Mock tests
    - Rest day every 15 days
    """

    plan = []
    subjects = list(allocation.keys())
    subject_idx = 0

   
    mock_gap = max(1, total_days // max(1, total_mocks))
    mock_days = set(
        range(total_days - total_mocks * mock_gap + 1, total_days + 1, mock_gap)
    )

    topic_tracker = {}

    for day in range(1, total_days + 1):

       
        if day % 15 == 0:
            plan.append({
                "Day": day,
                "Subject": "Rest Day",
                "Major Topic": "Recovery",
                "Sub Topic": "Mental Reset",
                "Task": "Rest + Light Revision + Planning",
                "Task Type": "Rest",
                "Done": False
            })
            continue

      
        if day in mock_days:
            plan.append({
                "Day": day,
                "Subject": "All Subjects",
                "Major Topic": "Mock Test",
                "Sub Topic": "Full Length",
                "Task": "Mock Test + Analysis",
                "Task Type": "Mock",
                "Done": False
            })
            continue

       
        if day % 7 == 0:
            plan.append({
                "Day": day,
                "Subject": "All Subjects",
                "Major Topic": "Revision",
                "Sub Topic": "Weak Areas",
                "Task": "Weekly Revision",
                "Task Type": "Revision",
                "Done": False
            })
            continue

       
        subject = subjects[subject_idx % len(subjects)]
        subject_idx += 1

        subject_data = syllabus[subject]
        major_topics = list(subject_data.keys())

        if subject not in topic_tracker:
            topic_tracker[subject] = {"major": 0, "sub": 0}

        major_topic = major_topics[
            topic_tracker[subject]["major"] % len(major_topics)
        ]

        subtopics = subject_data[major_topic]
        sub_topic = subtopics[
            topic_tracker[subject]["sub"] % len(subtopics)
        ]

        topic_tracker[subject]["sub"] += 1
        if topic_tracker[subject]["sub"] % len(subtopics) == 0:
            topic_tracker[subject]["major"] += 1

       
        plan.append({
            "Day": day,
            "Subject": subject,
            "Major Topic": major_topic,
            "Sub Topic": sub_topic,
            "Task": "Concept Study",
            "Task Type": "Concept",
            "Done": False
        })

       
        plan.append({
            "Day": day,
            "Subject": subject,
            "Major Topic": major_topic,
            "Sub Topic": sub_topic,
            "Task": f"Practice {daily_questions} Questions",
            "Task Type": "Practice",
            "Done": False
        })

    return plan


def carry_forward_tasks(plan, day_number, incomplete_tasks):
    """
    Carry forward ONLY unfinished tasks to next day
    """
    for task in incomplete_tasks:
        new_task = task.copy()
        new_task["Day"] = day_number + 1
        new_task["Done"] = False
        plan.append(new_task)

    return plan
