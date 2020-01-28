from xintesis import ServicePack
from flask_restplus import Resource, fields, reqparse

service_pack = ServicePack("Summarization method")


@service_pack.service
class Summary:

    @service_pack.post_expect
    def summary_expect():
        expect = dict()
        expect["text"] = fields.String(required=True, description='A test parameter')
        return expect

    @service_pack.post_method
    def summary_method(**kwargs):
        """ Complex help
        \n This method do nothing but show a JSON as doc
        \n JSON:
        \n\t {
        \n\t "features" :
        \n\t   [
        \n\t\t     {"name": "temperature", "val": 32},
        \n\t\t     {"name": "weight", "val": 55},
        \n\t   ]
        \n\t }
        """
        return True, kwargs['input']
