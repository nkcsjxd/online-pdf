import requests
from requests.auth import HTTPBasicAuth
import os

api_key = '2eda35bcd0252ddad721b002388ee3875069e612'
endpoint = "https://sandbox.zamzar.com/v1/jobs"

source_path = "./chm/"
target_format = "txt"
local_path = "./txt/"

for file_name in os.listdir(source_path):
        source_file = os.path.join(source_path, file_name)
        if os.path.isfile(source_file):
            print(file_name)
            file_content = {'source_file': open(source_file, 'rb')}
            data_content = {'target_format': target_format}
            
            res = requests.post(endpoint, data=data_content, files=file_content, auth=HTTPBasicAuth(api_key, ''))
            print(res.json())
            job_id = res.json()['id']
            endpoint = "https://sandbox.zamzar.com/v1/jobs/{}".format(job_id)
            response = requests.get(endpoint, auth=HTTPBasicAuth(api_key, ''))
            print(response.json())
            # response.json()['target_files']
            # file_id = res.json()['id']
            # print(file_id)
            # re_endpoint = "https://sandbox.zamzar.com/v1/files/{}/content".format(file_id)
            # response = requests.get(re_endpoint, stream=True, auth=HTTPBasicAuth(api_key, ''))
            # local_filename = local_path + file_name + 'txt'
            # try:
            #     with open(local_filename, 'wb') as f:
            #         for chunk in response.iter_content(chunk_size=1024):
            #             if chunk:
            #                 f.write(chunk)
            #                 f.flush()

            #         print("File downloaded")

            # except IOError:
            #     print("Error")