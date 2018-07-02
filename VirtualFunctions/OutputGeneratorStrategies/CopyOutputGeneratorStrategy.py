from VirtualFunctions.OutputGeneratorStrategy import OutputGeneratorStrategy


# copy to different topic or different broker or both
class CopyOutputGeneratorStrategy(OutputGeneratorStrategy):
    def __init__(self):
        pass

    def generate(self, source_message):
        return source_message
