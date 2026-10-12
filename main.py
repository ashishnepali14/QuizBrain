from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

Question_Bank = []
for question in question_data:
    question_text = question["question"]
    answer = question["correct_answer"]
    new_question = Question(question_text, answer)
    Question_Bank.append(new_question)

quiz = QuizBrain(Question_Bank)

while quiz.question_number < len(Question_Bank):
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(Question_Bank)}")


   


