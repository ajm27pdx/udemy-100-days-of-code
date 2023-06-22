from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text="question", fill=THEME_COLOR,
                                                     font=('Arial', 20, 'italic'), width=275)

        true_image = PhotoImage(file='images/true.png')
        false_image = PhotoImage(file='images/false.png')
        self.true_btn = Button(image=true_image, highlightthickness=0, command=self.ans_true)
        self.false_btn = Button(image=false_image, highlightthickness=0, command=self.ans_false)

        self.score_lbl = Label(text='Score: 0', bg=THEME_COLOR, fg='white')

        self.score_lbl.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.true_btn.grid(row=2, column=0)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def ans_true(self):
        correct_ans = self.quiz.check_answer(True)
        self.display_feedback(correct_ans)

    def ans_false(self):
        correct_ans = self.quiz.check_answer(False)
        self.display_feedback(correct_ans)

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end.")
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')

    def display_feedback(self, correct_ans: bool):
        self.score_lbl.config(text=f'Score: {self.quiz.score}')
        if correct_ans:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)
