from hashlib import md5
import datetime

def shortener(url, username):
    url = "{}{}".format(url, username, datetime.datetime.now().strftime("%f"))
    url = bytes(url, encoding = "ascii")
    m = md5()
    m.update(url)
    return m.hexdigest()

