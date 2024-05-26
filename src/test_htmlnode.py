import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="p", value="This is a text node", props="{\"href\": \"https://www.google.com\", \"target\": \"_blank\"}")
        node2 = HTMLNode(tag="p", value="This is a text node", props="{\"href\": \"https://www.google.com\", \"target\": \"_blank\"}")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
