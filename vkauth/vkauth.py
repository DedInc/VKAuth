import psutil
import browser_cookie_3x as bc
from requests import Session
from urllib.parse import unquote

user_scope = 'https://oauth.vk.com/authorize?client_id=6287487&scope=501202911&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token'
group_scope = 'https://oauth.vk.com/authorize?client_id=7497650&scope=134623237&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&group_ids='

browser_procs = {
  bc.chrome: 'chrome.exe',
  bc.yandex: 'browser.exe',
  bc.firefox: 'firefox.exe',
  bc.edge: 'msedge.exe',
  bc.opera: 'launcher.exe',
  bc.opera_gx: 'launcher.exe'
}

class VKAuth:
    
    def __init__(self):
        self.session = self.get_session()
        
    def kill_proc(self, proc):
        for process in psutil.process_iter(['name']):
            if process.info['name'] == proc:
                try:
                    process.kill()
                except:
                    pass
                    
    def scan_cookies(self, cookies):
        remixsid = remixnsid = p = None
        for cookie in cookies:
            domain = cookie.domain
            name = cookie.name
            if domain == '.vk.com' or domain == 'vk.com':
                if name == 'remixnsid':
                    remixnsid = cookie.value
                elif name == 'remixsid':
                    remixsid = cookie.value
            elif domain == '.login.vk.com':
                if name == 'p':
                    p = cookie.value
        if remixsid and remixnsid and p:            
            return remixsid, remixnsid, p
        return None
            
    def get_auth_cookies(self, after_check=False):

        for browser in browser_procs:
            try:
              cookies = self.scan_cookies(browser())
              if cookies:
                return cookies 
            except PermissionError as e:
                if after_check:
                    self.kill_proc(browser_procs[browser])
                    cookies = self.scan_cookies(browser())
                    if cookies:
                        return cookies
            except Exception as e:
                pass
        if not after_check:
            return self.get_auth_cookies(True)
        return None
    
    def get_session(self):
        cookies = self.get_auth_cookies()
        if cookies:
            self.session = Session()
            self.session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
            })
            self.session.cookies.update({
                'remixsid': cookies[0],
                'remixnsid': cookies[1],
                'p': cookies[2]
            })
        else:
            raise Exception('Auth Error!')
        return self.session
    
    def get_token(self, group_id=None):
        url = user_scope if not group_id else group_scope + f'{group_id}'
        r = self.session.get(url)
        
        grant_link = r.text.split('+addr')[0].split('"')[-2]
        r = self.session.get(grant_link)
        
        token = 'vk1' + unquote(unquote(r.url).split('_url=')[1]).split('=vk1')[1].split('&')[0]
        return token