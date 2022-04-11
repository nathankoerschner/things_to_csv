import things
import csv
#want one page of tasks, one page of projects, one page of areas, one page of tasks
#want a toggle for including completed, removed, and canceled tasks
allTasks = things.tasks(status=None)

keys = ['uuid', 'type', 'title', 'status', 'start', 'area', 'area_title', 'project', 'project_title', 'heading', 'heading_title', 'notes', 'tags', 'start', 'start_date', 'deadline', 'checklist', 'stop_date', 'created', 'modified', 'index', 'today_index']
with open('todos.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(allTasks)


def getTasks(includeCompleted = False, includeCanceled = False, **kwargs):
    completed = []
    canceled = []

    if includeCompleted:
        completed = things.tasks(status = 'completed', include_items=True)
    if includeCanceled:
        canceled = things.tasks(status = 'canceled', include_items=True)

    tasks = things.tasks(include_items=True)

    tasks = tasks + completed + canceled

    return tasks
