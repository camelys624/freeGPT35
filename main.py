import g4f
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import insertData, findData


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
g4f.logging = True


@app.get('/v1/competion')
def spin_content(content):
    response = g4f.ChatCompletion.create(
        model=g4f.models.default,
        provider=None,
        messages=[
            {"role": "user", "content": """现在你是我的记账助手，你需要根据我的提示，将其转换为如下格式的纯json字符串，不要添加任何描述和其他的东西。
            {
                "date": Date,
                "item": Item,
                "cost": Number,
                "description": String
            }，其中 Item 的枚举值如下：
            {
                "0": "餐饮", 
                "1": "交通", 
                "2": "购物", 
                "3": "居家", 
                "4": "娱乐", 
                "5": "通讯", 
                "6": "医疗", 
                "7": "其他", 
            }，下面是我的提示：""" + content}
        ]
    )

    json_response = response.replace('```json', '').replace('```', '')
    result = insertData(json_response)
    
    return result

@app.get('/v1/getList')
def get_list(pageSize, pageNum):
    result = findData(pageSize=int(pageSize), pageNum=int(pageNum))
    return result
    