import tkinter as tk



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
        self.geometry("400x200")

        self.my_queue = Queue()


        self.input_frame = tk.Frame(self)
        self.input_frame.pack(pady=10)

        self.input_box = tk.Entry(self.input_frame, width=30)
        self.input_box.pack(side=tk.LEFT, padx=(0, 5))

        self.enqueue_button = tk.Button(self.input_frame, text="Enqueue", command=self.enqueue_item)
        self.enqueue_button.pack(side=tk.LEFT)


        self.dequeue_button = tk.Button(self, text="Dequeue", command=self.dequeue_item)
        self.dequeue_button.pack(pady=5)


        self.status_label = tk.Label(self, text="Queue is empty.")
        self.status_label.pack(pady=10)



    def enqueue_item(self):
        item = self.input_box.get()
        if item:
            self.my_queue.enqueue(item)
            self.update_status_label()
            self.input_box.delete(0, tk.END)
        else:
            print("Please enter an item to enqueue.")

    def dequeue_item(self):
        dequeued_item = self.my_queue.dequeue()
        if dequeued_item is not None:
            print(f"Dequeued: {dequeued_item}")
        else:
            print("Queue is empty, cannot dequeue.")
        self.update_status_label()

    def update_status_label(self):
        if not self.my_queue.is_empty():
            self.status_label.config(text=f"Queue: {self.my_queue.display()}")
        else:
            self.status_label.config(text="Queue is empty.")



if __name__ == "__main__":
    app = App()
    app.mainloop()
