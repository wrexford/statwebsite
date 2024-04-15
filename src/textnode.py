class TextNode:
    def __init__(self, text, text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        #print(f"TextNode({self.text}, {self.text_type}, {self.url})")

    def compare(self, text2):
        if self.text == text2.text and self.text_type == text2.text_type and self.url == text2.url :
            return True
        else:
            pass

    def __rerp__(self):
         return str(f"TextNode({self.text},{self.text_type},{self.url})")
