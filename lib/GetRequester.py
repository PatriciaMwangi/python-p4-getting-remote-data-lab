import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response=requests.get(self.url)
        return response.content
        

    def load_json(self,response):
        try:
            jsons=json.loads(response)
            return jsons
        except json.JSONDecodeError as e:
            print(f'Failed to decode: {e}')
            return None
    
cls=GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
get=cls.get_response_body()
getting=cls.load_json(get)

#print(get)
#print(getting[1])
        