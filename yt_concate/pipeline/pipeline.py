from .steps.step import StepExcption

class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs):
        for step in self.steps:
            try:
                step.process(inputs)
            except Exception as e:
                print('Exception happened:', e)
                break
