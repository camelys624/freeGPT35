import g4f
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
g4f.logging = True


@app.get('/')
def spin_content(content):
    print(content)
    response = g4f.ChatCompletion.create(
        model=g4f.models.default,
        provider=None,
        messages=[
            {"role": "user", "content": """现在你是我的记账助手，你需要根据我的提示，将其转换为此格式 ```json
                {
                    "date": Date,
                    "item": String,
                    "cost": Number,
                    "description": String
                }
    ```的纯json字符串，不要添加任何描述和其他的东西。下面是我的提示：""" + content}
        ]
    )

    return response