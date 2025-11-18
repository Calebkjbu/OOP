import tkinter as tk
from tkinter import messagebox

class Queue:
    def __init__(self):
        self.elements = []

    def enqueue(self, item):
        self.elements.append(item)

    def dequeue(self):
        if not self.elements:
            return None
        return self.elements.pop(0)

    def displayQueue(self):
        return " <- ".join(self.elements) if self.elements else "Queue is empty"

class Stack:
    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        if not self.elements:
            return None
        return self.elements.pop()

    def displayStack(self):
        return " -> ".join(self.elements) if self.elements else "Stack is empty"

class App:
    def __init__(self, root):
        self.root = root
        root.title("Queue and Stack GUI")
        root.geometry("500x400")

        self.queue = Queue()
        self.stack = Stack()

        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)

        tk.Label(root, text="Queue Operations", font=("Arial", 14)).pack()
        tk.Button(root, text="Enqueue", command=self.enqueue).pack(pady=3)
        tk.Button(root, text="Dequeue", command=self.dequeue).pack(pady=3)

        self.queue_label = tk.Label(root, text="Queue: ")
        self.queue_label.pack(pady=5)

        tk.Label(root, text="Stack Operations", font=("Arial", 14)).pack(pady=10)
        tk.Button(root, text="Push", command=self.push).pack(pady=3)
        tk.Button(root, text="Pop", command=self.pop_stack).pack(pady=3)

        self.stack_label = tk.Label(root, text="Stack: ")
        self.stack_label.pack(pady=5)

    def enqueue(self):
        item = self.entry.get().strip()
        if not item:
            messagebox.showwarning("Warning", "Please enter a value")
            return
        self.queue.enqueue(item)
        self.update_queue_display()

    def dequeue(self):
        removed = self.queue.dequeue()
        if removed is None:
            messagebox.showinfo("Info", "Queue is empty")
        else:
            messagebox.showinfo("Dequeued", f"Removed: {removed}")
        self.update_queue_display()

    def update_queue_display(self):
        self.queue_label.config(text=f"Queue: {self.queue.displayQueue()}")

    def push(self):
        item = self.entry.get().strip()
        if not item:
            messagebox.showwarning("Warning", "Please enter a value")
            return
        self.stack.push(item)
        self.update_stack_display()

    def pop_stack(self):
        removed = self.stack.pop()
        if removed is None:
            messagebox.showinfo("Info", "Stack is empty")
        else:
            messagebox.showinfo("Popped", f"Removed: {removed}")
        self.update_stack_display()

    def update_stack_display(self):
        self.stack_label.config(text=f"Stack: {self.stack.displayStack()}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()