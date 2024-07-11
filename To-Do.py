import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        
        self.root = root
        self.root.title("To-Do List Applicaiton")
        self.root.geometry("400x400")
        
        #Applying Theme
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        #Main Frame
        self.frame = ttk.Frame(root)
        self.frame.pack(pady = 10)
        
        #Listbox to display tasks
        self.listbox = tk.Listbox(self.frame, width = 50, height = 10, bd = 0)
        self.listbox.pack(side = tk.LEFT, fill = tk.BOTH)
        
        #Scrollbar
        self.scrollbar = ttk.Scrollbar(self.frame)
        self.scrollbar.pack(side = tk.RIGHT, fill = tk.BOTH)
        
        self.listbox.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.listbox.yview)
        
        #Box to create new tasks
        self.task_entry = ttk.Entry(root, width = 50)
        self.task_entry.pack(pady = 20)
        
        #Button Frame
        self.button_frame = ttk.Frame(root)
        self.button_frame.pack(pady = 20)
        
        self.add_button = ttk.Button(self.button_frame, text = "Add Task", command = self.add_task)
        self.add_button.pack(side = tk.LEFT, padx = 10)
        
        self.delete_button = ttk.Button(self.button_frame, text = "Delete Task", command = self.delete_task)
        self.add_button.pack(side = tk.LEFT, padx = 10)
        
        self.clear_button = ttk.Button(self.button_frame, text = "Clear Task", command = self.clear_tasks)
        self.clear_button.pack(side = tk.LEFT, padx = 10)
        
        
    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task")
    
    
    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_task_index)
        except:
            messagebox.showwarning("Warning", "You must select a task to delete")
    
    
    def clear_tasks(self):
        self.listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()