import unittest
from seleniumrequests import Firefox


class DefaultVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_homepage(self):
        # Test Sample project homepage
        self.browser.get('http://localhost:5000/default_proj')
        # Default title test
        self.assertIn('Default', self.browser.title)

    def test_post(self):
        res = self.browser.request('POST', 'http://localhost:5000/default_proj/default_proj/DemoProj',
                                   json={"text": "string"})
        self.assertEqual({'success': True, 'data': {'text': 'string'}, 'message': ''}, res.json())


if __name__ == '__main__':
    unittest.main(warnings='ignore')
