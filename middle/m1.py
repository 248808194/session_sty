from  django.utils.deprecation import MiddlewareMixin
from  django.shortcuts import HttpResponse

class Row1(MiddlewareMixin):
    def process_request(self,request):
        print('request_ROW1')


    def process_view(self,request,view_func,view_func_args,view_func_kwargs):
        print('process_view_ROW1')


    def process_response(self,request,response):
        print('response_ROW1')
        return  response




class Row2(MiddlewareMixin):
    def process_request(self, request):
        print('request_ROW2')

    def process_view(self,request,view_func,view_func_args,view_func_kwargs):
        print('process_view_ROW2')


    def process_response(self, request, response):
        print('response_ROW2')
        return response
        # return  HttpResponse('GO')


class Row3(MiddlewareMixin):
    def process_request(self, request):
        print('request_ROW3')

    def process_view(self,request,view_func,view_func_args,view_func_kwargs):
        print('process_view_ROW3')


    def process_response(self, request, response):
        print('response_ROW3')
        return response

    def process_exception(self,request,exception):
        print(exception)
        return HttpResponse('页面错了')