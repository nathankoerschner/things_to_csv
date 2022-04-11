import things
import csv
#one page of tasks, one page of projects, one page of areas, one page of tasks
allTasks = things.tasks(status=None)

keys = ['uuid', 'type', 'title', 'status', 'start', 'area', 'area_title', 'project', 'project_title', 'heading', 'heading_title', 'notes', 'tags', 'start', 'start_date', 'deadline', 'checklist', 'stop_date', 'created', 'modified', 'index', 'today_index']
with open('todos.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(allTasks)