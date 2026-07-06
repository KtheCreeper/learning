import fire
import json
import datetime

class tools:
    def add(self, taskName, taskDesc):
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
        with open("ids.txt", "r") as IDs:
            currentID = int(IDs.read())
        taskName, taskDesc = str(taskName), str(taskDesc)
        currentID += 1
        tasks[currentID] = {"name": taskName, "description": taskDesc, "status": "todo", "createdAt": datetime.datetime.now(), "updatedAt": datetime.datetime.now()}
        with open("tasks.json", "w") as f:
            json.dump(tasks, f, default=str)
        with open("ids.txt", "w") as IDs:
            IDs.write(str(currentID))
        print(f"Task '{taskName}' added. ( ID: {currentID} )")

    def update(self, ID, taskName, taskDesc):
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
        taskName, taskDesc = str(taskName), str(taskDesc)
        tasks[str(ID)] = {"name": taskName, "description": taskDesc,  "status": tasks[str(ID)]["status"], "createdAt": tasks[str(ID)]["createdAt"],"updatedAt": datetime.datetime.now()}
        with open("tasks.json", "w") as f:
            json.dump(tasks, f, default=str)
        print(f"Task '{taskName}' updated.")

    def delete(self, ID):
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
        del tasks[str(ID)]
        with open("tasks.json", "w") as f:
            json.dump(tasks, f, default=str)
        print("Task deleted.")

    def mark(self, status, ID):
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
        status = str(status)
        if status not in ("done", "in-progress"): return
        tasks[str(ID)]["status"] = status
        with open("tasks.json", "w") as f:
            json.dump(tasks, f, default=str)
        print(f"Task '{tasks[str(ID)]["name"]}' marked as {status}.")

    def list(self, type="all"):
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
        tasksFound = False
        type = str(type)
        for task in tasks:
            if type == "all":
                print(f"'{tasks[task]["name"]}' (ID: {task}): '{tasks[task]["status"]}'")
                tasksFound = True
            elif tasks[task]["status"] == type:
                print(f"'{tasks[task]["name"]}' (ID: {task})")
                tasksFound = True
        if not tasksFound:
            print("(No tasks found)")



if __name__ == "__main__":
    fire.Fire(tools())