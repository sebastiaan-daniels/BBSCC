import datetime

class log():
    def __init__(self,message) -> None:
        with open("data\\log.txt", "a") as log:
            now = datetime.datetime.now()
            now_str = now.strftime("%Y-%m-%d %H:%M:%S")
            log.write(f"{now_str} - {message}\n")

