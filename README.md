# Things to CSV

A Python3 tool to export your Things 3 database to a CSV, using the [Things Python API](https://github.com/thingsapi/things.py).

### Notes

- Each of the Things database entities (Tasks, Projects, Areas, Tags) are exported separately, hence separate files for each.

- If a task or project has not been modified since it's completion (e.g., by adding extra notes post-hoc), then one may take the `modified` property of `completed` tasks and projects as the completion date and time.

## Getting Your Data

Assuming you have downloaded the files and are in the `things_to_csv` directory, to get all of your Things data in a single CSV, run `python3 things_to_csv.py True True`.
The first Boolean parameter represents the inclusion of completed tasks, and the second canceled tasks.

If you would only like to include incomplete tasks and projects, simply run `python3 things_to_csv.py`

#### Get Your Tasks

Run `python3 tasks_to_csv` to get all incomplete tasks as a CSV in this directory.

If you'd like to include completed and canceled tasks, run this program passing the optional parameters:
`python3 tasks_to_csv.py True True`
(where the first parameter represents the inclusion of completed tasks, and the second canceled tasks.)

#### Get Your Projects (very similar to tasks)

Run `python3 projects_to_csv` to get all incomplete projects as a CSV in this directory.

If you'd like to include completed and canceled projects, run this program passing the optional parameters:
`python3 projects_to_csv.py True True`
(where the first parameter represents the inclusion of completed projects, and the second canceled projects.)

### Get Your Tags or Areas

Run `python3 tags_to_csv` or `python3 tags_to_csv`.

_The outputs of these scripts will include extraneous columns, used for inter-operability with the CSV outputs of the other scripts._
