from VirtualValues.ParsingStrategy import ParsingStrategy
import lxml.etree


class XmlParsingStrategy(ParsingStrategy):
    path = ''

    def __init__(self, path):
        self.path = path

    def parse(self, raw_payload):
        tree = lxml.etree.fromstring(raw_payload)
        root = tree.getroot()
        r = root.xpath(self.path)
        return r[0].tag
