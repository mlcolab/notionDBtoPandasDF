import requests, json
import pandas as pd

#first the user has to enter the integration token
token = str(input('Enter secret token: '))

#then the user has to enter the database id
databaseId = str(input('Enter database id: '))


headers = {
    "Authorization": "Bearer " + token,
    "Notion-Version": "2021-05-13"
}

#reads data and transformes it into an dataframe
def readDatabase(databaseId, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}"

    #gets general info about the database --> like title etc.
    db_info = requests.request("GET", readUrl, headers=headers)
    info = db_info.json()
    print('Status code for info request: ', db_info.status_code) # if status code is 200 everything is great

    title = info['title'][0]['plain_text'] # save title for filename later


    #gets data of database
    res = requests.request("POST", readUrl+'/query', headers=headers)
    data = res.json()
    print('Status code for data request: ', res.status_code) # if status code is 200 everything is great

    df = pd.json_normalize(data, record_path=['results']) #converts json data into pandas dataframe
    #print(df)

    file_name = title+'_'+databaseId+'.feather' # creates filename out of tilte and database id
    df.to_feather(file_name) # saves file as .feather
    

readDatabase(databaseId, headers)