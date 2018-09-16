from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class M1(MiddlewareMixin):
    # 必须传入request对象
    def process_request(self, request):
        print("M1 process_request")

    # 必须传入request和response对象，必须返回response对象.
    def process_response(self, request, response):
        print("M1 process_response")
        response.setdefault("Access-Control-Allow-Origin", "*") # 为所有响应设置响应头.
        return response


class M2(MiddlewareMixin):
    def process_request(self, request):
        print("M2 process_request")

    def process_response(self, request, response):
        print("M2 process_response")
        return response
