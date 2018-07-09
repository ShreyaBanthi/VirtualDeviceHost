from VirtualFunctions.OutputGeneratorStrategy import OutputGeneratorStrategy


import re


class JarvisLightStripOutputGeneratorStrategy(OutputGeneratorStrategy):
    regex_string = ''
    compiled_regex = None
    replace_string = ''

    def __init__(self, regex_string, matching_identifiers):
        # compile for performance reasons. According to docs, the most recent regex are cached automatically
        # but as we don't know how many are used later we have to be sure
        self.regex_string = regex_string
        self.compiled_regex = re.compile(regex_string, re.MULTILINE)

    def generate(self, source_message):
        # updated_string = self.compiled_regex.sub(source_message, self.replace_string)
        # updated_string = re.sub(self.regex_string, self.replace_string, source_message)
        updated_string = self.compiled_regex.sub(self.replace_string, source_message)
        return updated_string
