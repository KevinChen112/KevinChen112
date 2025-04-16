进口要求

url1 ='https://helmet.real2tech.net/api/label/PC/labelInfo/page？' pageSize=20&pageNo=1 '
有效负载={"标签类型":"","苹果":" 806EC9 ","项目Id ":"1867092082510057474"}
标题={'授权': 无记名eyjhbgcioijsuzi 1 nij 9 . eyjzdwiioijhzg 1 pbiisinvzzxjzci 6 ijeeilcjuyw 1 lijoiywrtaw 4 ilcjpzci 6 Inc 2 bndquoxvuiiwizgvwyxj 0 swqioiixmdailcjehaioje 3 nd qd 5 MDN 9 . yweet 7d 8 hoabazbwex 5 qi2 ldjmydl 4 jqkm 0j odex 82 pnupceavaeibkwo 6 dpk MH 7 ds,'内容类型':应用/JSON；charset=UTF-8 ',饼干:hm _ lvt _ 1 DFA 88d 0 c 8571 eef 2d 383070 CB 3 e 5 ca 1 = 1744815323；hm account = 8ed 526 F9 a 34 a 420 b；D2 admin-1 . 5 . 9-is refresh = false；D2 admin-1 . 5 . 9-uuid = 1；D2 admin-1 . 5 . 9-token = eyjhbgcioijsuzi 1 nij 9 . eyjzdwioijzg 1 pbiisisinvzzxjzci 6 ije ilcjuyw 1 lijoiywrtaw 4 ilcjpzci 6 Inc 2 bndquoxvuiiwizzg vwyxj 0 swqioiiximdailcjlehaioje 3 ndq 5 MDN 9 . yweet 7d 8 hoabazbwex 5 qi 2 ldjmydl 4 jqkm0 j 1 odex 82 pnupceavaeid2admin-1 . 5 . 9-expire date = 2025-04-17% 2022:55:03;D2 admin-1 . 5 . 9-refresh token = w 6 NWP 9 un；D2 admin-1 . 5 . 9-tenantId = null；D2 admin-1 . 5 . 9-projectId = 1867092082510057474；D2 admin-1 . 5 . 9-is change = false；D2 admin-1 . 5 . 9-can return = true；hm _ lpvt _ 1 DFA 88 d0c 8571 eef 2d 383070 CB 3 e5ca 1 = 1744815345 '}
极好的 post _请求(url、有效负载、标题):
响应=请求。邮政(url，json =有效负载，headers =标题)
    如果回应。状态代码 == 200:
数据=响应。json()  # 如果响应是JSON格式
        打印(数据)
    其他:
        打印(f "请求失败,状态码：{回应。状态代码}")

url2 =https://helmet . real 2 tech . net/API/passage/project organ/getOrganTree？projectId=1867092082510057474 '
响应=请求。得到(url2，标题=标题)
如果回应。状态代码 == 200:
数据=响应。json()  # 如果响应是JSON格式
    打印(数据)
其他:
    打印(f "请求失败,状态码：{回应。状态代码}")
    打印('123454353464564562153153123153214')
