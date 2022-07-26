from copy import deepcopy


class Result(object):

    def __init__(self):
        self.algorithm_name = None
        self.tool_name = None

        self.command_results = []
        self.not_supported = False
        self.timed_out = False
        self.threw_error = False
        self.qva_error = None
        self.error_text = None

        self.measurements = {}

        self.index = None

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for key, v in self.__dict__.items():
            if key == "self.command_results":
                setattr(result, key, [])
            else:
                setattr(result, key, deepcopy(v, memo))
        return result