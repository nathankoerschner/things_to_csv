import things
import csv
from datetime import datetime

usersTags = things.tags()

# format string for output
now = datetime.now()
filename = f"things_tags_{now.year}-{now.month}-{now.day}_{now.hour}-{now.minute}.csv"


keys = [
    "uuid",
    "type",
    "title",
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
    "shortcut",
    "index",
    "today_index",
]

with open(filename, "w", encoding="utf-8-sig", newline="") as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(usersTags)
