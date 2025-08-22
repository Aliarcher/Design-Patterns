"""
    Adapter
    - a structural design pattern that allows objects with incompatible interface to collaborate
"""
import xmltodict #use for convert xml to json

class Application:
    def send_request():
        return "data.xml"
    
class Analytic:
    def recieve_request(self,json):
        return json    
#Adapter
class Adapter:
    def convert_xml_json(self,file):
        with open(file,'r') as myfile:
            obj = xmltodict.parse(myfile.read())
            return obj
#client
def client_adaptor():
    sender = Application().send_request()
    converted_data = Adapter().convert_xml_json(sender)
    receiver = Analytic().recieve_request(converted_data)
    print(receiver)