from VirtualFunctions.OutputGeneratorStrategy import OutputGeneratorStrategy


class StringReplaceOutputGeneratorStrategy(OutputGeneratorStrategy):
    from_list = []
    to_list = []

    def __init__(self, from_list, to_list):
        self.from_list = from_list
        self.to_list = to_list

    def generate(self, source_message):
        updated_string = source_message
        for i in len(self.from_list):
            updated_string = updated_string.replace(str(self.from_list[i]), str(self.to_list[i]))
        return updated_string
