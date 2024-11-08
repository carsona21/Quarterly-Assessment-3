import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Bowl Project")
        self.root.geometry("500x400")

        # Database connection
        self.conn = sqlite3.connect('qa_database.db')
        self.cursor = self.conn.cursor()

        self.create_category_window()

    def create_category_window(self):
        # Clear any existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Category selection window
        label = tk.Label(self.root, text="Select a Category", font=("Arial", 14))
        label.pack(pady=10)

        self.category_var = tk.StringVar()
        categories = ["ACCT2110", "BMGT3510", "ECON4900", "FIN3210", "MKT3400"]
        self.category_combobox = ttk.Combobox(self.root, textvariable=self.category_var, values=categories, state='readonly')
        self.category_combobox.pack(pady=10)

        start_button = tk.Button(self.root, text="Start Quiz Now", command=self.start_quiz)
        start_button.pack(pady=20)

    def start_quiz(self):
        selected_category = self.category_var.get()
        if not selected_category:
            messagebox.showwarning("Warning", "Please select a category.")
            return

        # Fetch questions and answers for the selected category
        try:
            self.cursor.execute(f"SELECT question, answer FROM {selected_category} LIMIT 10")
            self.questions = self.cursor.fetchall()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
            return
        
        if not self.questions:
            messagebox.showinfo("No Questions", "No questions available for this category.")
            return

        self.current_question_index = 0
        self.correct_answers = 0
        self.create_quiz_window()

    def create_quiz_window(self):
        # Clear any existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        if self.current_question_index < len(self.questions):
            question, answer_data = self.questions[self.current_question_index]
            options = answer_data.split('\\n')  # Assuming the options are stored as newline-separated text in the database

            label = tk.Label(self.root, text=f"Question {self.current_question_index + 1}: {question}", wraplength=450)
            label.pack(pady=10)

            self.answer_var = tk.StringVar()
            for option in options:
                radio = tk.Radiobutton(self.root, text=option, variable=self.answer_var, value=option)
                radio.pack(anchor='w')

            submit_button = tk.Button(self.root, text="Submit Answer", command=self.submit_answer)
            submit_button.pack(pady=20)
        else:
            self.show_results()

    def submit_answer(self):
        user_answer = self.answer_var.get()
        correct_answer = self.questions[self.current_question_index][1].split('\\n')[-1].replace("Correct Answer: ", "").strip()
        
        if user_answer == correct_answer:
            self.correct_answers += 1

        self.current_question_index += 1
        self.create_quiz_window()

    def show_results(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        label = tk.Label(self.root, text=f"Quiz Completed! You got {self.correct_answers} out of {len(self.questions)} correct.", font=("Arial", 14))
        label.pack(pady=20)

        restart_button = tk.Button(self.root, text="Restart", command=self.create_category_window)
        restart_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
