question_prompts = [
  "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
  "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
  "What color are strawberries\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

class Question:
  def __init__(self, prompt, answer):
    self.prompt = prompt
    self.answer = answer

  # self is referring to the Question instance
  def is_correct_answer(self, answer):
    return self.answer == answer


questions = [
  Question(question_prompts[0], "a"),
  Question(question_prompts[1], "c"),
  Question(question_prompts[2], "b")
]

def run_test(questions: questions):
  score = 0
  for question in questions:
    if question.is_correct_answer(input(question.prompt)):
      score += 1
  return score

print("Your score is:", str(run_test(questions)) + "/" + str(len(questions)))
