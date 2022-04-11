# Things to CSV

A Python3 tool to export your Things 3 database to a CSV, using the [Things Python API](https://github.com/thingsapi/things.py).

Note that each of the Things entities (Tasks, Projects, Areas, Tags) are exported separately, hence separate files for each.

Assuming you have downloaded the files and are in the `things_to_csv` directory:

## Tasks_To_CSV

run `python3 tasks_to_csv` to get all incomplete tasks as a CSV in this directory.

If you'd like to include completed and canceled tasks, run this program passing the optional parameters:
`python3 tasks_to_csv.py True True`
(where the first parameter represents the inclusion of completed tasks, and the second canceled tasks.)
