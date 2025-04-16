import requests

url1 = 'https://helmet.real2tech.net/api/label/PC/labelInfo/page?pageSize=20&pageNo=1'
payload = {"labelType":"","mac":"806EC9","projectId":"1867092082510057474"}
headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJJZCI6IjEiLCJuYW1lIjoiYWRtaW4iLCJpZCI6Inc2bndQOXVuIiwiZGVwYXJ0SWQiOiIxMDAiLCJleHAiOjE3NDQ5MDE3MDN9.YwoETE7D8hOAbazBwEx5Qi2LDJMydl4jqkm0J1ODexX82PnuPCeAvAEIoybKWo6DpkmH7dsE1eYHmbGeioRJeCilBEaFiieY--3demjWXK9Tf7MmKLPVS2ignJs4nDU8cN9a2kWUbG7I6MAB7axVrNQhfXktJAwBkGe5gmJAIAM','Content-Type':'application/json;charset=UTF-8','Cookie':'Hm_lvt_1dfa88d0c8571eef2d383070cb3e5ca1=1744815323; HMACCOUNT=8ED526F9A34A420B; d2admin-1.5.9-isRefresh=false; d2admin-1.5.9-uuid=1; d2admin-1.5.9-token=eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJJZCI6IjEiLCJuYW1lIjoiYWRtaW4iLCJpZCI6Inc2bndQOXVuIiwiZGVwYXJ0SWQiOiIxMDAiLCJleHAiOjE3NDQ5MDE3MDN9.YwoETE7D8hOAbazBwEx5Qi2LDJMydl4jqkm0J1ODexX82PnuPCeAvAEIoybKWo6DpkmH7dsE1eYHmbGeioRJeCilBEaFiieY--3demjWXK9Tf7MmKLPVS2ignJs4nDU8cN9a2kWUbG7I6MAB7axVrNQhfXktJAwBkGe5gmJAIAM; d2admin-1.5.9-expireDate=2025-04-17%2022:55:03; d2admin-1.5.9-refreshToken=w6nwP9un; d2admin-1.5.9-tenantId=null; d2admin-1.5.9-projectId=1867092082510057474; d2admin-1.5.9-isChange=false; d2admin-1.5.9-canReturn=true; Hm_lpvt_1dfa88d0c8571eef2d383070cb3e5ca1=1744815345'}
def post_request(url,payload,headers):
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()  # 如果响应是 JSON 格式
        print(data)
    else:
        print(f"请求失败，状态码: {response.status_code}")

# url2 = 'https://helmet.real2tech.net/api/passage/projectOrgan/getOrganTree?projectId=1867092082510057474'
# response = requests.get(url2, headers=headers)
# if response.status_code == 200:
#     data = response.json()  # 如果响应是 JSON 格式
#     print(data)
# else:
#     print(f"请求失败，状态码: {response.status_code}")