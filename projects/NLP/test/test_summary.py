import unittest
import json
from projects.NLP.summary import get_summary


class SummaryTest(unittest.TestCase):

    def test_summarization_method(self):
        op_str = """[
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
        """
        op_dict = json.loads(op_str)
        summary = get_summary(1, op_dict)
        self.assertIn("The cats are really cute animals", summary)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
