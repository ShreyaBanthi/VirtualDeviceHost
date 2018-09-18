import re
from VirtualFunctions.OutputGeneratorStrategy import OutputGeneratorStrategy


class RegexReplaceOutputGeneratorStrategy(OutputGeneratorStrategy):
    regex_string = ''
    compiled_regex = None
    replace_string = ''

    def __init__(self, regex_string, replace_string):
        # compile for performance reasons. According to docs, the most recent regex are cached automatically
        # but as we don't know how many are used later we have to be sure
        self.regex_string = regex_string
        self.compiled_regex = re.compile(regex_string, re.MULTILINE)
        self.replace_string = str(replace_string)

    def generate(self, source_message):
        updated_string = self.compiled_regex.sub(self.replace_string, source_message)
        return updated_string
