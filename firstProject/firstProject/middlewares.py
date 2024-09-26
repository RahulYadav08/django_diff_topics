from django.http import HttpResponse

class CustomMiddleware():
    '''
    custom middleware should implement two mandatory methods __init__ and __call__.
    Whereas process_view -- called before request submitted to views and
    process_exception -- called when there is exception
    process_template_response -- after template just before goes response to client
    are optional.
    '''

    def __init__(self, get_response):
        print("Middlewares innitiated")
        self.get_response = get_response

    def __call__(self,request):

        #before reaching view
        

        #calling next middleware or view
        response = self.get_response(request)

        #before reaching to client
        # print("Response", response)
        response_content = response.content.decode('utf-8')
        response.content = (response_content + " Middleware customized message").encode('utf-8')

        return response

    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     pass

    # def process_exception(self, request, exception):
    #     pass

    # def process_template_response(self, request, response):
        # pass