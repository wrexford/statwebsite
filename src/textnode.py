class TextNode:
    def __init__(self, text, text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        #print(f"TextNode({self.text}, {self.text_type}, {self.url})")

    def __eq__(self, text2):
        return (
            self.text_type == text2.text_type
            and self.text == text2.text
            and self.url == text2.url
        )

    def __rerp__(self):
         return str(f"TextNode({self.text},{self.text_type},{self.url})")
