from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

Question_Bank = [] # this feels like something that could also be in the quizbrain class. There's no reason you can't include this as part of its  __init__ method
for question in question_data:
    # consider what you'd do if these fields were non-existent. Should the program die? Catch and move on?
    question_text = question["question"]
    answer = question["correct_answer"]
    new_question = Question(question_text, answer)
    Question_Bank.append(new_question)

quiz = QuizBrain(Question_Bank)
# usability suggestion: Add a print statement that informs the user that they have to type True/False in full (or handle variants like  't','f')
while quiz.question_number < len(Question_Bank): 
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(Question_Bank)}")


""" 
This is a very clean way of doing this - defining the data outside of the class and feeding it in.
Looks to me like you've got the general idea of classes down here.

Some general suggestions: 
- I would look at doing typing in your function definitions as that makes it even easier to understand
- You could add a randomisation of the question order (there are simple shuffle methods in python)
- I note that you have question types and possible answers in your data. As a way of extending what you've done here
you could make it so that these elements are part of the Question class, and determine what is displayed. This would involve
making the print and input parts the responsibility of the Question model, rather then in the QuizBrain (something like question.askQuestion())
- &quot; is printing literally in my display, might be better served with ' quote marks
"""


