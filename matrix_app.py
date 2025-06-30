import tkinter as tk
from tkinter import messagebox, simpledialog
from matrix_utils import multiply_matrices, multiply_matrix_by_number

class MatrixApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Calculator (4x4)")
        self.entries_a = []
        self.entries_b = []
        self.result_labels = []

        self.create_matrix_input("Matrix A", 0, self.entries_a)
        self.create_matrix_input("Matrix B", 5, self.entries_b)
        self.create_result_output("Result", 10)

        # Кнопки размещены ниже результата (row=15)
        tk.Button(root, text="A × B", command=self.calculate_product).grid(row=15, column=1, columnspan=4, pady=10)
        tk.Button(root, text="A × число", command=self.multiply_by_number).grid(row=15, column=6, columnspan=4, pady=10)

    def create_matrix_input(self, label, column_start, storage):
        tk.Label(self.root, text=label).grid(row=0, column=column_start, columnspan=4)
        for i in range(4):
            row_entries = []
            for j in range(4):
                e = tk.Entry(self.root, width=5)
                e.grid(row=i+1, column=column_start + j)
                e.insert(0, "0")
                row_entries.append(e)
            storage.append(row_entries)

    def create_result_output(self, label, column_start):
        tk.Label(self.root, text=label).grid(row=6, column=column_start, columnspan=4)
        for i in range(4):
            row_labels = []
            for j in range(4):
                l = tk.Label(self.root, text="0", width=5, relief=tk.SUNKEN, bg="white")
                l.grid(row=i+7, column=column_start + j)
                row_labels.append(l)
            self.result_labels.append(row_labels)

    def read_matrix(self, entries):
        return [[float(entries[i][j].get()) for j in range(4)] for i in range(4)]

    def calculate_product(self):
        try:
            a = self.read_matrix(self.entries_a)
            b = self.read_matrix(self.entries_b)
            result = multiply_matrices(a, b)
            self.display_result(result)
        except ValueError:
            messagebox.showerror("Ошибка", "Некорректный ввод!")

    def multiply_by_number(self):
        try:
            number = float(simpledialog.askstring("Введите число", "На что умножить Matrix A?"))
            a = self.read_matrix(self.entries_a)
            result = multiply_matrix_by_number(a, number)
            self.display_result(result)
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def display_result(self, result):
        for i in range(4):
            for j in range(4):
                self.result_labels[i][j].config(text=str(result[i][j]))

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixApp(root)
    root.mainloop()