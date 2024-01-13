import xml.etree.ElementTree as ET


class XMLParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.root = None
        self.data = []

    def parse_xml(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            xml_content = file.read()
        self.root = ET.fromstring(xml_content)

    def extract_information(self):
        if self.root is None:
            raise ValueError("XML not parsed. Call parse_xml() first.")
        # Iterate through each 'item' element and extract information
        for item in self.root.findall('.//item'):
            title = item.find('title').text
            link = item.find('link').text
            description = item.find('description').text

            # Extracting domains from categories
            domains = [category.text for category in item.findall('.//category[@domain]')]

            item_info = {
                'title':title,
                'link':link,
                'description':description,
                'domains':domains
            }
            self.data.append(item_info)

        return self.data


if __name__ == '__main__':
    xml_file_path = "news_xml_files/Health.xml"
    xml_parser = XMLParser(xml_file_path)
    xml_parser.parse_xml()
    result = xml_parser.extract_information()
    for res in result:
        print(res)
