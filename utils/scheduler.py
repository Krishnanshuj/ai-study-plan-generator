

def apply_revision_and_tests(plan):
    for i, row in enumerate(plan):
        day_num = i + 1

        if day_num % 30 == 0:
            row["Task"] = "Full-Length Mock Test"
            row["Subject"] = "All Subjects"
            row["Major Topic"] = "Mock"
            row["Sub Topic"] = "Analysis"

        elif day_num % 14 == 0:
            row["Task"] = "Sectional Mock + Analysis"

        elif day_num % 7 == 0:
            row["Task"] = "Weekly Revision"
            row["Sub Topic"] = "Weak Areas Revision"

    return plan
