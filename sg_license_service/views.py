# -*- coding: utf-8 -*-



from django.http import HttpResponse, HttpResponseForbidden
from django.conf import settings
from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials, Error #NEED PyOpenSSL and PyCrypto
from StringIO import StringIO
from elementtree.SimpleXMLWriter import XMLWriter

import os
import xmlbuilder
import httplib2

def license(request):
    package = request.GET.get("package", "")
    sku = request.GET.get("sku", "")
    service = request.GET.get("service", "")
    token = request.GET.get("token", "")
    key = request.GET.get("key", "")

    key_content = get_key(key)

    if (len(key_content) == 0):
        return xmlbuilder.get_fail_response("Wrong key name", 2)

    credentials = SignedJwtAssertionCredentials(
      service,
      key_content,
      scope='https://www.googleapis.com/auth/androidpublisher')

    try:
        http = httplib2.Http()
        http = credentials.authorize(http)
        service = build("androidpublisher", "v1.1", http=http)
        result = service.inapppurchases().get(packageName=package, productId=sku, token=token).execute(http=http)
    except Error, ex:
        return xmlbuilder.get_fail_response(str(ex), 1)
    
    print result
    xml_result = StringIO()
    xml = XMLWriter(xml_result, 'utf-8')
    xml.start("result", status="0", consumptionState=str(result["consumptionState"]), purchaseState=str(result["purchaseState"]), purchaseTime=str(result["purchaseTime"]))
    xml.end()
    return HttpResponse('<?xml version="1.0" encoding="UTF-8"?>' + xml_result.getvalue())


def get_key(key_name):
    try:
        with open(os.path.join(settings.KEY_STORE, key_name + '.p12'), 'rb') as f:
            return f.read()
    except IOError:
        return ""
