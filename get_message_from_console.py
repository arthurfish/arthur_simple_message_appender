import sys

def get_message_from_console():
    message_content = ""
    if len(sys.argv) > 1:
        content = ""
        for sentence in sys.argv[1:]:
            content += sentence + " "
        message_content = content
    else:
        content = ""
        while True:
            try:
                line = input()
                content += line + "\n"
            except EOFError:
                break
        message_content = content
    return message_content