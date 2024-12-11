def append_to_notion(message_content: str, notion_api_key: str):
    # 获取API密钥
    page_id = "159cba75-4c10-8035-aae7-ea5c582aed69"

    import requests
    # 头信息
    headers = {
        'Authorization': f'Bearer {notion_api_key}',
        'Content-Type': 'application/json',
        'Notion-Version': '2022-06-28',
    }
    # 数据负载
    data = {
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": str(message_content),
                            }
                        }
                    ]
                }
            }
        ]
    }
    # 发送PATCH请求
    response = requests.patch(
        f'https://api.notion.com/v1/blocks/{page_id}/children',
        headers=headers,
        json=data
    )
    # 响应处理
    if response.status_code == 200:
        print("Notion Done.")
    else:
        print("Error:", response.status_code, response.text)