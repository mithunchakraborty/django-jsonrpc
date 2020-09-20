import os
import ssl
import json
import urllib.request
from django.conf import settings


def auth_check(hostname, certificate_str, key_str):
    """
    Идентифицирует клиента на hostname API c помощью сертификата и ключа.
    Делает jsonrpc запрос к методу auth.check.  
    Возвращает словарь ответа сервера на запрос к методу auth.check.
    """
    cert_path = _get_path_string_to_file(settings.API_CERTIFICATE, 'client03test.crt')
    key_path = _get_path_string_to_file(settings.API_KEY, 'client03test.key')
    
    payload = {
        "method": "auth.check",
        "jsonrpc": "2.0",
        "id": 1,
    }
    
    payload = json.dumps(payload)
    data = payload.encode('ascii')
    
    # Создание SSL контекста
    context = ssl.SSLContext()
    context.load_cert_chain(cert_path, key_path)


    req = urllib.request.Request(hostname)
    req.add_header('Content-Type', 'application/json')
    r = urllib.request.urlopen(req, data=data, context=context)
    
    return r.read().decode('utf-8')
    

def _get_path_string_to_file(source_string:str, filename):
    """
    Возвращает путь, созданного файла из строки.
    """
    path = os.path.join(settings.BASE_DIR, filename)
    
    with open(path, "w") as file:
        file.write(source_string)
        
    return path
    
