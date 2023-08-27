from colorama import init, Fore
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style

# Initialize colorama for color support
init(autoreset=True)

# Define a custom style for the prompt_toolkit session
style = Style.from_dict({
    "prompt": "bold",
    "input": "fg:#00aa00",
    "output": "fg:#0000aa",
    "error": "fg:#aa0000",
})

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Not Done"
        return f"{self.description} (Due: {self.due_date}) - {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

    def mark_task_completed(self, task_idx):
        if 0 <= task_idx < len(self.tasks):
            self.tasks[task_idx].mark_as_completed()

class ToDoListApp:
    def __init__(self):
        self.todo_list = ToDoList()
        self.session = PromptSession(style=style)
    
    def add_task(self):
        description = self.session.prompt("Enter task description: ")
        due_date = self.session.prompt("Enter due date: ")
        new_task = Task(description, due_date)
        self.todo_list.add_task(new_task)
        print(Fore.GREEN + "Task added!" + Fore.RESET)
    
    def mark_task(self):
        self.show_tasks()
        try:
            task_idx = int(self.session.prompt("Enter task number to mark as completed: ")) - 1
            self.todo_list.mark_task_completed(task_idx)
            print(Fore.GREEN + "Task marked as completed." + Fore.RESET)
        except (ValueError, IndexError):
            print(Fore.RED + "Invalid task index." + Fore.RESET)
    
    def show_tasks(self):
        print(Fore.CYAN + "\n--- Tasks ---" + Fore.RESET)
        self.todo_list.show_tasks()

    def run(self):
        while True:
            print(Fore.YELLOW + "\n--- To-Do List Application ---" + Fore.RESET)
            print("1. Add Task")
            print("2. Show Tasks")
            print("3. Mark Task as Completed")
            print("4. Quit")

            try:
                choice = self.session.prompt("Enter your choice: ")
                if choice == "1":
                    self.add_task()
                elif choice == "2":
                    self.show_tasks()
                elif choice == "3":
                    self.mark_task()
                elif choice == "4":
                    print("Quitting the application.")
                    break
                else:
                    print(Fore.RED + "Invalid choice. Please select a valid option." + Fore.RESET)
            except KeyboardInterrupt:
                print(Fore.YELLOW + "\nExiting the application." + Fore.RESET)
                break

if __name__ == "__main__":
    app = ToDoListApp()
    app.run()
