from VirtualValues.ParsingStrategy import ParsingStrategy


class RawParsingStrategy(ParsingStrategy):

    def parse(self, raw_payload):
        # raw data is expected, so don't do any processing
        return raw_payload
