from elementtree.SimpleXMLWriter import XMLWriter
from django.http import HttpResponse
from StringIO import StringIO

def get_fail_response(message="", status=1):
    result = StringIO()
    xml = XMLWriter(result, 'utf-8')
    xml.start("result", status=str(status), message = message)
    xml.end()
    return HttpResponse('<?xml version="1.0" encoding="UTF-8"?>' + result.getvalue())

def get_empty_success_response():
    result = StringIO()
    xml = XMLWriter(result, 'utf-8')
    xml.start("result", status="0")
    xml.end()
    return HttpResponse('<?xml version="1.0" encoding="UTF-8"?>' + result.getvalue())