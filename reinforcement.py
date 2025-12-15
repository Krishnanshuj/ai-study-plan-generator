
def update_plan(plan, subject, performance, rewards, daily_hours):

    if not isinstance(rewards, list):
        rewards = []

    try:
        daily_hours = float(daily_hours)
    except:
        daily_hours = 6.0

    
    reward = 1 if performance == "good" else -1
    rewards.append(reward)

    negative_ratio = rewards.count(-1) / len(rewards)
    fatigue_score = (daily_hours / 12.0) + negative_ratio
    burnout = fatigue_score > 0.7

    
    for row in plan:
        if row["Subject"] == subject and row["Task"] == "Concept + Practice":
            if performance == "bad":
                row["Task"] = "Revision + Extra Practice"
            else:
                row["Task"] = "Practice + Test"

   
    if burnout:
        for row in plan:
            if row["Task"] == "Concept + Practice":
                row["Task"] = "Light Revision / Concept Video"

    return plan, rewards, burnout
