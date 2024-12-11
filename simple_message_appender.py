#!/bin/python3
from threading import Thread

from append_to_github import append_to_github
from append_to_notion import append_to_notion
from get_message_from_console import get_message_from_console
from secret import *


def arthur_simple_message_appender(message: str):
    Thread(target=append_to_github, args=[message, github_access_token]).start()
    Thread(target=append_to_notion, args=[message, notion_api_key]).start()


if __name__ == "__main__":
    arthur_simple_message_appender(get_message_from_console())
