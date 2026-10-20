class Question:
    def __init__(self, question_text, answer):
        # look up private variables of classes, and decide whether these should accessible
        self.question_text = question_text
        self.answer = answer