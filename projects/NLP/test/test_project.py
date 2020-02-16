import unittest
from seleniumrequests import Firefox


class DefaultVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_homepage(self):
        # Test Sample project homepage
        self.browser.get('http://localhost:5000/NLP')
        # Default title test
        self.assertIn('Summary Project', self.browser.title)

    def test_post(self):
        test_json = {"opinions":
            [

                {

                    "id": 1,

                    "text": "The cats are really cute animals"

                },

                {

                    "id": 2,

                    "text": "The cutest pets are cats. They are my favorite animal."

                },

                {

                    "id": 3,

                    "text": "I am a dog lover and hate cats. I will never have a cat as a pet."

                }

            ]
            ,
            "n_ideas": 1
        }
        res = self.browser.request('POST', 'http://localhost:5000/NLP/NLP/Summary',
                                   json=test_json)

        self.assertEqual({'success': True, 'data': 'The cats are really cute animals.', 'message': ''}, res.json())


if __name__ == '__main__':
    unittest.main(warnings='ignore')
