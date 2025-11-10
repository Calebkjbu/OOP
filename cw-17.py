import tkinter as tk
from tkinter import ttk


# Your existing Queue class
class Queue:
    def __init__(self):
        self.element = []

    def enqueue(self, nn):
        self.element.append(nn)

    def dequeue(self):
        if not self.is_empty():
            return self.element.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.element) == 0

    def display(self):
        return ", ".join(map(str, self.element))


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("cw-17")
        self.geometry("450x300")

        # Initialize queue storage and counter
        self.queues = {"Queue 1": Queue()}
        self.queue_counter = 1

        # Variable to hold the name of the currently selected queue
        self.active_queue_name = tk.StringVar(value="Queue 1")

        # --- Widgets ---

        # Frame for controls and status
        self.control_frame = tk.Frame(self)
        self.control_frame.pack(pady=10)

        # Frame for radio buttons (for dynamic widget management)
        self.radio_button_frame = tk.Frame(self.control_frame)
        self.radio_button_frame.pack(side=tk.LEFT, padx=5)

        tk.Label(self.radio_button_frame, text="Select Queue:").pack(anchor="w")

        # Populate initial radio buttons
        self.update_radio_buttons()

        # Button to create a new queue
        self.create_queue_button = tk.Button(self.control_frame, text="Create New Queue", command=self.create_new_queue)
        self.create_queue_button.pack(side=tk.LEFT, padx=5)

        # Input and Enqueue button
        self.input_frame = tk.Frame(self)
        self.input_frame.pack(pady=5)
        self.input_box = tk.Entry(self.input_frame, width=30)
        self.input_box.pack(side=tk.LEFT, padx=(0, 5))
        self.enqueue_button = tk.Button(self.input_frame, text="Enqueue", command=self.enqueue_item)
        self.enqueue_button.pack(side=tk.LEFT)

        # Dequeue button
        self.dequeue_button = tk.Button(self, text="Dequeue", command=self.dequeue_item)
        self.dequeue_button.pack(pady=5)

        # Status Label to display queue contents
        self.status_label = tk.Label(self, text="", wraplength=400)
        self.status_label.pack(pady=10)


        self.update_status_label()



    def create_new_queue(self):
        self.queue_counter += 1
        new_name = f"Queue {self.queue_counter}"
        self.queues[new_name] = Queue()
        self.active_queue_name.set(new_name)  # Select the new queue
        self.update_radio_buttons()
        self.update_status_label()
        print(f"New queue '{new_name}' created.")

    def update_radio_buttons(self):

        for widget in self.radio_button_frame.winfo_children():
            if isinstance(widget, tk.Radiobutton):
                widget.destroy()

        # Create and pack new radio buttons
        for name in self.queues.keys():
            tk.Radiobutton(
                self.radio_button_frame,
                text=name,
                variable=self.active_queue_name,
                value=name,
                command=self.update_status_label
            ).pack(anchor="w")

    def get_active_queue(self):
        """Returns the currently active queue object."""
        return self.queues[self.active_queue_name.get()]

    def enqueue_item(self):
        item = self.input_box.get()
        if item:
            self.get_active_queue().enqueue(item)
            self.update_status_label()
            self.input_box.delete(0, tk.END)
        else:
            print("Please enter an item to enqueue.")

    def dequeue_item(self):
        dequeued_item = self.get_active_queue().dequeue()
        queue_name = self.active_queue_name.get()
        if dequeued_item is not None:
            print(f"Dequeued from {queue_name}: {dequeued_item}")
        else:
            print(f"Queue '{queue_name}' is empty, cannot dequeue.")
        self.update_status_label()

    def update_status_label(self):
        active_queue = self.get_active_queue()
        queue_name = self.active_queue_name.get()
        if not active_queue.is_empty():
            self.status_label.config(text=f"Current Queue: {queue_name}\nContents: {active_queue.display()}")
        else:
            self.status_label.config(text=f"Current Queue: {queue_name}\nContents: Queue is empty.")



if __name__ == "__main__":
    app = App()
    app.mainloop()