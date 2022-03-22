
class browser:
  def __init__(self):
    import requests
    import base64
    import json
    self.json = json
    self.base64 = base64
    self.requests = requests
    self.cookies = {}
    self.headers = {}
    self.auth = ""
    self.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43"

  def get(self, url, responseType = ''):
    return self.post(url, {}, responseType)

  def post(self, url, post, responseType = ''):
    self.headers = {}
    requests = self.requests
    if ".onion" in url:
        requests = requests.session()
        requests.proxies = {'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'}
    headers = {}
    headers["User-Agent"] = self.UserAgent
    cookies = {}
    if self.auth:
        headers["Authorization"] = "Basic " + self.base64.b64encode(this.auth.encode('ascii')).decode('ascii')
        cookies["phpbb3_thbm8_u"] = "274163"
        cookies["phpbb3_thbm8_k"] = ""
        cookies["phpbb3_thbm8_sid"] = "fdd788b78b0fa23fda95f2d6f44e8a65"
        cookies["style_cookie"] = "printonly"
    else:
        for key, value in self.cookies.copy().items():
            if key != 'expires' and key != 'path' and key != 'domain':
                cookies[key] = value
    if len(post):
        requests = requests.post(url, post, headers=headers, cookies=cookies)
    else:
        requests = requests.get(url, headers=headers, cookies=cookies)
    headers = {}
    headers["code"] = headers["status_code"] = requests.status_code
    setcookie = ""
    for r in requests.history:
        for key, value in r.cookies.get_dict().copy().items():
            setcookie+=" "+key+"="+value+";"
    for key, value in requests.headers.copy().items():
        if key.lower() == 'set-cookie':
            if 'HttpOnly' in value:
                if 'ttp:' in url:
                    setcookie+=" "+value.replace('HttpOnly', '')
            else:
                setcookie+=" "+value
                
        else:
            self.headers[key] = value
    if setcookie:
        self.parse(setcookie);
    return requests.text

  def clean(self):
    self.cookies = {}

  def setUserAgent(self, UserAgent):
    self.UserAgent = UserAgent

  def parse(self, a):
    for data in a.split(';'):
        data = data.split('=')
        if (len(data)>1):
            self.cookies[data[0].strip()] = data[1].split(';')[0].strip()

  def auth(self, url, value):
    self.auth = value
    content = self.get(url)
    self.auth = ""
    return content
    
test = browser()
content = test.post("https://blablaland.fun/login", {'login': '', 'password': ''})
content = test.get("https://blablaland.fun")