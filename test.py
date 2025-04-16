import pandas as pd
import logging
import requests
url1 = 'https://helmet.real2tech.net/api/label/PC/labelInfo/page?pageSize=20&pageNo=1'
payload1 = {"labelType":"","mac":"806EC9","projectId":"1867092082510057474"}
headers1 = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJJZCI6IjEiLCJuYW1lIjoiYWRtaW4iLCJpZCI6Inc2bndQOXVuIiwiZGVwYXJ0SWQiOiIxMDAiLCJleHAiOjE3NDQ5MDE3MDN9.YwoETE7D8hOAbazBwEx5Qi2LDJMydl4jqkm0J1ODexX82PnuPCeAvAEIoybKWo6DpkmH7dsE1eYHmbGeioRJeCilBEaFiieY--3demjWXK9Tf7MmKLPVS2ignJs4nDU8cN9a2kWUbG7I6MAB7axVrNQhfXktJAwBkGe5gmJAIAM','Content-Type':'application/json;charset=UTF-8','Cookie':'Hm_lvt_1dfa88d0c8571eef2d383070cb3e5ca1=1744815323; HMACCOUNT=8ED526F9A34A420B; d2admin-1.5.9-isRefresh=false; d2admin-1.5.9-uuid=1; d2admin-1.5.9-token=eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJJZCI6IjEiLCJuYW1lIjoiYWRtaW4iLCJpZCI6Inc2bndQOXVuIiwiZGVwYXJ0SWQiOiIxMDAiLCJleHAiOjE3NDQ5MDE3MDN9.YwoETE7D8hOAbazBwEx5Qi2LDJMydl4jqkm0J1ODexX82PnuPCeAvAEIoybKWo6DpkmH7dsE1eYHmbGeioRJeCilBEaFiieY--3demjWXK9Tf7MmKLPVS2ignJs4nDU8cN9a2kWUbG7I6MAB7axVrNQhfXktJAwBkGe5gmJAIAM; d2admin-1.5.9-expireDate=2025-04-17%2022:55:03; d2admin-1.5.9-refreshToken=w6nwP9un; d2admin-1.5.9-tenantId=null; d2admin-1.5.9-projectId=1867092082510057474; d2admin-1.5.9-isChange=false; d2admin-1.5.9-canReturn=true; Hm_lpvt_1dfa88d0c8571eef2d383070cb3e5ca1=1744815345'}
# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def post_request(url,payload,headers):
    logging.info("正在发送请求url：",url,"请求体是：",payload,"请求头是：",headers)
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()  # 如果响应是 JSON 格式
        print(data)
    else:
        print(f"请求失败，状态码: {response.status_code}")


def read_excel_columns(file_path, sheet_name):
    """
    读取 Excel 文件的列名并打印。

    :param file_path: Excel 文件路径
    :param sheet_name: 表单名称
    """
    try:
        # 检查文件路径是否为空
        if not file_path.strip():
            raise ValueError("文件路径不能为空")

        # 读取 Excel 文件
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        for row in df.itertuples(index=True, name='Pandas'):
            print(f"Row {row.Index + 2}:")
            print(f"{row.url}, {row.请求方式}, {row.请求体},  {row.请求头}")
            url=row.url
            payload=row.请求体
            headers=row.请求头
            return url,payload,headers
        # 打印字段信息
        logging.info("文件字段信息（列名）:")
        logging.info(df.columns.tolist())
    except FileNotFoundError:
        logging.error(f"文件未找到，请检查路径: {file_path}")
    except ValueError as ve:
        logging.error(f"值错误: {ve}")
    except Exception as e:
        logging.error(f"发生未知错误: {e}")


# 示例调用
if __name__ == "__main__":
    file_path = input("请输入文件路径: ").strip()
    sheet_name = input("请输入表单名称: ").strip()
    a=read_excel_columns(file_path, sheet_name)
    print("url是:",a[0])
    print("请求体是:",a[1])
    print("请求体头:",a[2])
    post_request(url1,payload1,headers1)
    url2,payload2,headers2=a[0], a[1], a[2]
    post_request(url2, payload2, headers2)

1111