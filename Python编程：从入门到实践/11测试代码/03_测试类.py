class AnonymousSurvey:
    """收集匿名调查问卷的答案"""
def __init__(self, question):
    self.question = question
    self.responses = []
def show_question(self):
    """显⽰调查问卷"""
    print(self.question)
def store_response(self, new_response):
    """存储单份调查答卷"""
    self.responses.append(new_response)
def show_results(self):
    """显⽰收集到的所有答卷"""
    print("Survey results:")
    for response in self.responses:
        print(f"- {response}")

