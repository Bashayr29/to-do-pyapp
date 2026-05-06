import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        self.todos = []

        # Title
        title = tk.Label(root, text="To-Do List", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333")
        title.pack(pady=(20, 10))

        # Input frame
        input_frame = tk.Frame(root, bg="#f0f0f0")
        input_frame.pack(padx=20, fill="x")

        self.entry = tk.Entry(input_frame, font=("Helvetica", 13), relief="solid", bd=1)
        self.entry.pack(side="left", fill="x", expand=True, ipady=6, padx=(0, 8))
        self.entry.bind("<Return>", lambda e: self.add_todo())

        add_btn = tk.Button(
            input_frame, text="Add", font=("Helvetica", 12, "bold"),
            bg="#4CAF50", fg="white", relief="flat", cursor="hand2",
            padx=12, pady=4, command=self.add_todo
        )
        add_btn.pack(side="left")

        # Scrollable list frame
        list_outer = tk.Frame(root, bg="#f0f0f0")
        list_outer.pack(padx=20, pady=15, fill="both", expand=True)

        canvas = tk.Canvas(list_outer, bg="#f0f0f0", highlightthickness=0)
        scrollbar = tk.Scrollbar(list_outer, orient="vertical", command=canvas.yview)
        self.list_frame = tk.Frame(canvas, bg="#f0f0f0")

        self.list_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.list_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Bind mousewheel
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(-1 * (e.delta // 120), "units"))

    def add_todo(self):
        text = self.entry.get().strip()
        if not text:
            messagebox.showwarning("Empty input", "Please enter a to-do item.")
            return
        self.todos.append(text)
        self.entry.delete(0, tk.END)
        self.render_todos()

    def delete_todo(self, index):
        del self.todos[index]
        self.render_todos()

    def render_todos(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        for i, todo in enumerate(self.todos):
            row = tk.Frame(self.list_frame, bg="white", pady=4, padx=8, relief="solid", bd=1)
            row.pack(fill="x", pady=4)

            label = tk.Label(row, text=todo, font=("Helvetica", 12), bg="white", fg="#222", anchor="w", wraplength=290, justify="left")
            label.pack(side="left", fill="x", expand=True)

            del_btn = tk.Button(
                row, text="Delete", font=("Helvetica", 10),
                bg="#e53935", fg="white", relief="flat", cursor="hand2",
                padx=8, pady=2,
                command=lambda idx=i: self.delete_todo(idx)
            )
            del_btn.pack(side="right")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
