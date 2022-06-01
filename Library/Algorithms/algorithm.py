class Algorithm(object):

    def __init__(self, execution_constructor, name):
        self.name = name
        self.execution_constructor = execution_constructor

    def run(self, instance, result):
        result.algorithm = self.name
        self.execution_constructor(instance, result)
        return result

