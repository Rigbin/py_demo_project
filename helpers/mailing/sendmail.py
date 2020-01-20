from . import mailconf as conf
# from helpers.mailing import mailconf

def send():
    print(f"sending mail as {conf.SENDER}...")
