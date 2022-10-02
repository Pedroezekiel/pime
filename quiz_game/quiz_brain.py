from quiz_game import data


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def nest_question(self):
        question = data.question_data[self.question_number]["text"]
        print(f"Q.1: {question} (True/False)")


QuizBrain("wws").nest_question()
