from xintesis import ServicePack
from flask_restplus import Resource, fields, reqparse
from projects.NLP.summary import get_summary

service_pack = ServicePack("Summarization method")


@service_pack.service
class Summary:

    @service_pack.post_expect
    def summary_expect():
        expect = dict()
        expect["opinions"] = fields.String(required=True, description='Opinions list')
        expect["n_ideas"] = fields.Integer(required=True, description='Desired n most important ideas')
        return expect

    @service_pack.post_method
    def summary_method(**kwargs):
        """ Get the most important ideas in a set of opinions
        \n JSON Example:
        \n\t {
        \n\t "opinions" :
        \n\t   [
        \n\t\t     {
        \n\t\t      "id": 1,
        \n\t\t      "text": "The cats are really cute animals"
        \n\t\t    },
        \n\t\t     {
        \n\t\t      "id": 2,
        \n\t\t     "text": "The cutest pets are cats. They are my favorite animal."
        \n\t\t    },
        \n\t\t     {
        \n\t\t      "id": 3,
        \n\t\t     "text": "I am a dog lover and hate cats. I will never have a cat as a pet."
        \n\t\t    }
        \n\t   ]
        \n\t }
        """
        my_input = kwargs['input']
        summary = get_summary(my_input['n_ideas'],my_input['opinions'])
        return True, summary
