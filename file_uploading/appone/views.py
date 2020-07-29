import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

class FileHandleView(APIView):

    parser_classes = [MultiPartParser]

    def put(self,request):
        file_obj = request.data['file']
        data = file_obj.read()
        try:
            os.mkdir('file_uploading')
        except Exception as e:
            print("Exception while creating a directory",e)

        file_path = 'file_uploading/' + 'temp_' + file_obj.name

        with open(file_path,'wb') as file:
            file.write(data)
        return Response("Success")
