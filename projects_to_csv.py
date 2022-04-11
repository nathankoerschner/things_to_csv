import things
import csv
import sys
from datetime import datetime

includeCompleted = sys.argv[1] if len(sys.argv) > 1 else False
includeCanceled = sys.argv[2] if len(sys.argv) > 2 else False


def getProjects(includeCompleted, includeCanceled):
    completed = []
    canceled = []

    if includeCompleted:
        completed = things.projects(status="completed", include_items=True)
    if includeCanceled:
        canceled = things.projects(status="canceled", include_items=True)

    projects = things.projects(include_items=True)
    projects = projects + completed + canceled

    return projects


usersProjects = getProjects(includeCompleted, includeCanceled)

# format string for output
completed = "_completed" if includeCompleted else ""
canceled = "_canceled" if includeCanceled else ""
now = datetime.now()


filename = f"things_projects_{now.year}-{now.month}-{now.day}_{now.hour}-{now.minute}_incomplete{completed}{canceled}.csv"


keys = [
    "uuid",
    "type",
    "title",
    "shortcut",
    "status",
    "start",
    "area",
    "area_title",
    "project",
    "project_title",
    "heading",
    "heading_title",
    "notes",
    "items",
    "tags",
    "start",
    "start_date",
    "deadline",
    "checklist",
    "stop_date",
    "created",
    "modified",
    "index",
    "today_index",
]

with open(filename, "w", encoding="utf-8-sig", newline="") as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(usersProjects)
