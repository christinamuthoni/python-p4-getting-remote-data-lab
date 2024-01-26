import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        #url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

        response = requests.get(self.url)
        print(response.content)
        return response.content 

    def load_json(self):
        response_content = self.get_response_body()

        if response_content is not None:
            try:
                # Use json.loads to parse the JSON content
                json_data = json.loads(response_content)
                return json_data
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                return None
        else:
            return None




