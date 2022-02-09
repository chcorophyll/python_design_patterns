"""
references:
https://github.com/youngsterxyf/mpdp-code
https://sourcemaking.com/design_patterns/creational_patterns
"""
import xml.etree.ElementTree as etree
import json


class JSONConnector(object):

    def __init__(self, file_path):
        self.data = dict()
        with open(file_path, mode="r", encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def parse_data(self):
        return self.data


class XMLConnector(object):

    def __init__(self, file_path):
        self.tree = etree.parse(file_path)

    @property
    def parse_data(self):
        return self.tree


def connection_factory(file_path):
    if file_path.endswith("json"):
        connector = JSONConnector
    elif file_path.endswith("xml"):
        connector = XMLConnector
    else:
        raise ValueError("Cannot connect to {}".format(file_path))
    return connector(file_path)


def connect_to(file_path):
    factory = None
    try:
        factory = connection_factory(file_path)
    except ValueError as e:
        print(e)
    return factory


def main():
    sqlite_factory = connect_to("./data/person.sq3")
    print("*********************")
    xml_factory = connect_to("./data/person.xml")
    xml_data = xml_factory.parse_data
    liars = xml_data.findall(".//{}[{}='{}']".format("person", "lastName", "Liar"))
    print("found: {} persons".format(len(liars)))
    for liar in liars:
        print("first name: {}".format(liar.find("firstName").text))
        print("last name: {}".format(liar.find("lastName").text))
        [print("phone number ({})".format(p.attrib["type"]), p.text)
         for p in liar.find("phoneNumbers")]
    print("*********************")
    json_factory = connect_to("./data/donut.json")
    json_data = json_factory.parse_data
    print("found: {} donuts".format(len(json_data)))
    for donut in json_data:
        print("name: {}".format(donut["name"]))
        print("price: ${}".format(donut["ppu"]))
        [print("topping: {} {}".format(t["id"], t["type"])) for t in donut["topping"]]


if __name__ == "__main__":
    main()