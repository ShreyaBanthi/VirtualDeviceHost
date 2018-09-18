from VirtualFunctions.OutputGeneratorStrategy import OutputGeneratorStrategy


class CopyOutputGeneratorStrategy(OutputGeneratorStrategy):
    """copy message to different topic or different broker or both"""

    def generate(self, source_message):
        # don't have to change anything from source message, so just return it
        return source_message
