from VirtualValues.ParsingStrategy import ParsingStrategy


class RawParsingStrategy(ParsingStrategy):

    def parse(self, raw_payload):
        return raw_payload
