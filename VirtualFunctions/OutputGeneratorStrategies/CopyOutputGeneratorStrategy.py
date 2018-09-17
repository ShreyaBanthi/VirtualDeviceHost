from VirtualFunctions.OutputGeneratorStrategy import OutputGeneratorStrategy


class CopyOutputGeneratorStrategy(OutputGeneratorStrategy):
    """copy to different topic or different broker or both"""

    def generate(self, source_message):
        return source_message
