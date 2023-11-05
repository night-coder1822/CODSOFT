import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
        update_status()

def complete_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.itemconfig(selected_task, {'bg': 'light gray'})
        task_list.itemconfig(selected_task, {'strike': 1})
        update_status()
    except IndexError:
        pass

def delete_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.delete(selected_task)
        update_status()
    except IndexError:
        pass

def update_status():
    total_tasks = task_list.size()
    completed_tasks = len([i for i in range(total_tasks) if '1' in task_list.itemcget(i, 'strike')])
    status_label.config(text=f"Total Tasks: {total_tasks}, Completed: {completed_tasks}")

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)
entry.bind("<Return>", lambda event=None: add_task())

task_list = tk.Listbox(root, width=30)
task_list.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
complete_button = tk.Button(root, text="Complete Task", command=complete_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
add_button.pack()
complete_button.pack()
delete_button.pack()

status_label = tk.Label(root, text="", pady=10)
status_label.pack()

root.mainloop()
