import os
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import FileSerializer, FileDelimeterSerializer, URLUploadSerializer
from .docx import getText
from .pdf import getPdfText
from .txt import get_txt_word
from .csv import readCSV
from .jsonReader import readJSON
from .xmlReader import xmlViewer
from .rtfReader import get_rtf_text
from .epubReader import readEpub
from .odtreader import readOdtFiles
from .sasReader import readSas
from . odsReader import odsFileReader
from .xlsReader import xlsFileReader
from .stataReader import readSTATA

from .uploadRequests import confirmFile
from .confirmFile import confirmFileType
from django.conf import settings



base_dir = settings.BASE_DIR

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        filedata = {}

        file_serializer = FileSerializer(data=request.FILES)
        if file_serializer.is_valid():
            file_serializer.save()
            file1_path = file_serializer['file1'].value
            file2_path = file_serializer['file2'].value


            # dataform = os.path.join(base_dir, filename[1:])

            file1 = file_serializer.validated_data['file1']
            file2 = file_serializer.validated_data['file2']
            #   file1path = file_to_string(filetosave.file.path)

            file1_extension = file1.name.split('.')[1].lower()
            file2_extension = file2.name.split('.')[1].lower()

            allowed_files = ['docx','html', 'pdf', 'txt', 'csv', 'json', 'xml', 'rtf', 'odt','xpt', 'ods', 'xls', 'dta', 'epub', 'css']

            if file1_extension in allowed_files and file2_extension in allowed_files:
                if file1_extension == 'docx' :
                    filedata['file1']=getText(file1)
                if file1_extension == 'pdf':
                    filedata['file1']= getPdfText(os.path.join(base_dir, file1_path[1:]))
                if file1_extension == 'txt' or file1_extension == 'html' or file1_extension == 'css':
                    filedata['file1'] = get_txt_word(os.path.join(base_dir, file1_path[1:]))
                if file1_extension == 'csv':
                    filedata['file1'] = readCSV(os.path.join(base_dir, file1_path[1:]))
                if file1_extension == 'json':
                    filedata['file1'] = readJSON(os.path.join(base_dir, file1_path[1:]))
                if file1_extension == 'xml':
                    filedata['file1'] = xmlViewer(os.path.join(base_dir, file1_path[1:]))
                if file1_extension == 'rtf':
                    filedata['file1'] = get_rtf_text(os.path.join(base_dir, file1_path[1:]))
                if file1_extension == 'epub':
                    filedata['file1'] = readEpub(os.path.join(base_dir, file1_path[1:]))
                if file1_extension == 'odt':
                    filedata['file1'] = readOdtFiles(os.path.join(base_dir, file1_path[1:]))
                
                if file1_extension == 'xpt':
                    filedata['file1'] = readSas(os.path.join(base_dir, file1_path[1:]))

                if file1_extension == 'ods':
                    filedata['file1'] = odsFileReader(os.path.join(base_dir, file1_path[1:]))

                if file1_extension == 'xls':
                    filedata['file1'] = xlsFileReader(os.path.join(base_dir, file1_path[1:]))

                if file1_extension == 'dta':
                    filedata['file1'] = readSTATA(os.path.join(base_dir, file1_path[1:]))

                if file1_extension == 'epub':
                    filedata['file1'] = readEpub(os.path.join(base_dir, file1_path[1:]))





                if file2_extension == 'docx' :
                    filedata['file2']= getText(file2)
                if file2_extension == 'pdf':
                    filedata['file2']= getPdfText(os.path.join(base_dir, file2_path[1:]))
                if file2_extension == 'txt' or file2_extension == 'html' or file2_extension == 'css':
                    filedata['file2'] = get_txt_word(os.path.join(base_dir, file2_path[1:]))
                if file2_extension == 'csv':
                    filedata['file2'] = readCSV((os.path.join(base_dir, file2_path[1:])))
                if file2_extension == 'json':
                    filedata['file2'] = readJSON(os.path.join(base_dir, file2_path[1:]))
                if file2_extension == 'xml':
                    filedata['file2'] = xmlViewer(os.path.join(base_dir, file2_path[1:]))
                if file2_extension == 'rtf':
                    filedata['file2'] = get_rtf_text(os.path.join(base_dir, file2_path[1:]))
                if file2_extension == 'epub':
                    filedata['file2'] = readEpub(os.path.join(base_dir, file2_path[1:]))
                if file2_extension == 'odt':
                    filedata['file2'] = readOdtFiles(os.path.join(base_dir, file2_path[1:]))
                if file2_extension == 'xpt':
                    filedata['file2'] = readSas(os.path.join(base_dir, file2_path[1:]))
                if file2_extension == 'ods':
                    filedata['file2'] = odsFileReader(os.path.join(base_dir, file2_path[1:]))
                if file2_extension == 'dta':
                    filedata['file2'] = readSTATA(os.path.join(base_dir, file2_path[1:]))

                    

                return Response(filedata)
            else:
                return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileDelimeterView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        filedata = {}

        file_serializer = FileDelimeterSerializer(data=request.FILES)
        if file_serializer.is_valid():
            file_serializer.save()
            file1_path = file_serializer['file1'].value


            file1 = file_serializer.validated_data['file1']

            #   file1path = file_to_string(filetosave.file.path)

            file1_extension = file1.name.split('.')[1].lower()


            allowed_files = ['docx','html', 'pdf', 'txt', 'csv', 'json', 'xml', 'rtf', 'odt','xpt', 'ods', 'xls', 'dta', 'epub', 'css']

            if file1_extension in allowed_files:
                if file1_extension == 'docx' :
                    filedata['file1']=getText(file1)
                if file1_extension == 'pdf':
                    filedata['file1']= getPdfText(os.path.join(base_dir, file1_path[1:]))
                if file1_extension == 'txt' or file1_extension == 'html' or file1_extension == 'css':
                    filedata['file1'] = get_txt_word(os.path.join(base_dir, file1_path[1:]))
                if file1_extension == 'csv':
                    filedata['file1'] = readCSV(os.path.join(base_dir, file1_path[1:]))
                if file1_extension == 'json':
                    filedata['file1'] = readJSON(os.path.join(base_dir, file1_path[1:]))
                if file1_extension == 'xml':
                    filedata['file1'] = xmlViewer(os.path.join(base_dir, file1_path[1:]))
                if file1_extension == 'rtf':
                    filedata['file1'] = get_rtf_text(os.path.join(base_dir, file1_path[1:]))
                if file1_extension == 'epub':
                    filedata['file1'] = readEpub(os.path.join(base_dir, file1_path[1:]))
                if file1_extension == 'odt':
                    filedata['file1'] = readOdtFiles(os.path.join(base_dir, file1_path[1:]))
                
                if file1_extension == 'xpt':
                    filedata['file1'] = readSas(os.path.join(base_dir, file1_path[1:]))

                if file1_extension == 'ods':
                    filedata['file1'] = odsFileReader(os.path.join(base_dir, file1_path[1:]))

                if file1_extension == 'xls':
                    filedata['file1'] = xlsFileReader(os.path.join(base_dir, file1_path[1:]))

                if file1_extension == 'dta':
                    filedata['file1'] = readSTATA(os.path.join(base_dir, file1_path[1:]))

                if file1_extension == 'epub':
                    filedata['file1'] = readEpub(os.path.join(base_dir, file1_path[1:]))
                return Response(filedata)
            else:
                return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class uploadViaUrl(APIView):
    def post(self, request, *args, **kwargs):
        filedata = {}
        url_serializer = URLUploadSerializer(data = request.POST)

        if url_serializer.is_valid():
            url1 = request.POST['url1']
            url2 = request.POST['url2']
            if confirmFileType(url1) and confirmFileType(url2):
                file1 = confirmFile(url1)
                file2 = confirmFile(url2)
                filedata['file1'] = file1
                filedata['file2'] = file2
                return Response(filedata)
            else:
                return Response('One of the Uploaded file type not allowed', status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(url_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class uploadSingleFileViaUrl(APIView):
    def post(self, request, *args, **kwargs):
        filedata = {}
        url_serializer = URLUploadSerializer(data = request.POST)

        if url_serializer.is_valid():
            url1 = request.POST['url1']
            if confirmFileType(url1):
                file1 = confirmFile(url1)
                filedata['file1'] = file1
                return Response(filedata)
            else:
                return Response('One of the Uploaded file type not allowed', status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(url_serializer.errors, status=status.HTTP_400_BAD_REQUEST)