import werkzeug
from flask_restplus import fields, reqparse
from xintesis import ServicePack

service_pack = ServicePack("My demo component general description.")


@service_pack.service
class DemoPack:
    @service_pack.get_expect    
    def val_def():
        """
        GET expect always use a RequestParser and not defined param location = 'form' . 
        If not expect defined by default use the integer fields 'elements' and 'page',
        """
        
        expect = reqparse.RequestParser()
        expect.add_argument('get_data',
                            required=True,
                            help='Some input data')
        return expect

    @service_pack.get_method
    def some_method(project, input, obj_dict):
        """My GET example DOC"""
        # result = demo_method_to_service(project)
        result = "CHANGE"
        # some code
        print(project.uri_list)
        # print(obj_dict)
        return True, result

    @service_pack.post_expect
    def expect_def():
        """
        POST expect may use a RequestParser or JSON imput in pyaload field formated as dict, see also PUT expect example
        """
        post_data = reqparse.RequestParser()
        post_data.add_argument('some_file',
                                type=werkzeug.datastructures.FileStorage,
                                location='files',
                                required=True,
                                help='Some file')
        post_data.add_argument('some_data',
                                required=False,
                                location='form',
                                help='Some optional data')
        return post_data
        
    @service_pack.post_method
    def some_method2(**kwargs):
        """My POST example DOC"""
        project = kwargs['project']
        my_input = kwargs['input']
        obj_dict = kwargs['obj_dict']
        
        # some code
        data = input['some_data']
        print(data)
        
        file = input['some_file']
        save_file_dir = "downloads" 
        if not project.model_exist(save_file_dir):
            project.model_mkdir(save_file_dir)
        
        # saving file    
        if my_input['img_file'].filename not in project.model_lsdir():
            # internally use secure filename 
            project.model_save_file(save_file_dir, file) 
        
        # returning a file, the only case to return 3 params 
        return True, project.model_lsdir()[-1], "file"
        
    @service_pack.put_expect
    def expect_put():
        """
        PUT expect may use a RequestParser or JSON imput in pyaload field formated as dict, see also POST expect example 
        """
        expect = dict()
        expect["text"] = fields.String(required=True, description='A test parameter')
        return expect
        
    @service_pack.put_method
    def some_method3(**kwargs):
        project = kwargs['project']
        my_input = kwargs['input']
        obj_dict = kwargs['obj_dict']
        
        print(my_input)
        
        # not success operation return 
        return False, "My Bad!!!"
        
    @service_pack.delete_method
    def some_method4(**kwargs):
        project = kwargs['project']
        my_input = kwargs['input']
        obj_dict = kwargs['obj_dict']
        # if not expect defined kwargs['input']['id_list'] is a list of strings  
        dict_out = {}
        dict_out['numbers'] = [1,2,3]
        dict_out['text'] = "first numbers"
        # auto format dict to JSON
        return True, my_input

