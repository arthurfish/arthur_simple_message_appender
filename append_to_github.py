def append_to_github(message_content: str, github_access_token: str):
    import requests
    import datetime
    import time
    import base64
    owner = "arthurfish"
    repo = "PermanentMessage"
    filename = str(time.time_ns())

    commiter_name = "Arthur Schwarzer"
    commiter_email = "arthurfish8051@gmail.com"
    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{filename}'
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {github_access_token}',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    data = {
        "message": f"commit_at: {datetime.datetime.now()}",
        "committer": {
            "name": commiter_name,
            "email": commiter_email,
        },
        "content": base64.b64encode(message_content.encode()).decode()
    }
    response = requests.put(url, headers=headers, json=data)
    if str(response.status_code)[0] != "2":
        print(f"Error sending message. Code:{response.status_code}Response JSON: " + str(response.json()))
    else:
        print("Github Done.")