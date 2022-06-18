class Algorithm(object):

    def __init__(self, tool, execution_constructor, name):
        self.tool = tool
        self.execution_constructor = execution_constructor
        self.name = name

    def run(self, instance, result):
        result.algorithm_name = self.name
        result.tool_name = self.tool.name()
        self.execution_constructor(instance, result)
        return result

