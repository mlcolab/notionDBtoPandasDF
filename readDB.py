import requests, json
import pandas as pd


class NotionDatabase(): 

    def __init__(self, token, database_id) -> None:
        self.token = token
        self.database_id = database_id
        self.headers = {
        "Authorization": "Bearer " + token,
        "Notion-Version": "2021-05-13"
        }

    def to_dataframe(self):
        read_url = f"https://api.notion.com/v1/databases/{self.database_id}/query"

        #gets data of database
        res = requests.request("POST", read_url, headers=self.headers)
        data = res.json()
        print('Status code for data request: ', res.status_code) # if status code is 200 everything is great

        df = pd.json_normalize(data, record_path=['results']) #converts json data into pandas dataframe

        return df

