from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from .ultis import parse_query, process_browser_log_entry

class Browser:
    def __init__(self, url, show_br = False):
        self.driver = None
        self.url = url
        self.show_br = show_br

    def launch_borwser(self):
        caps = DesiredCapabilities.CHROME
        caps['goog:loggingPrefs'] = {'performance': 'ALL'}
        options = webdriver.ChromeOptions()
        if self.show_br == False:
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--ignore-certificate-errors')
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=caps, options=options)
        self.driver.get(self.url)

    def get_defaut_params(self):
        netLog = self.driver.get_log('performance')
        events = [process_browser_log_entry(entry) for entry in netLog]
        events = [event for event in events if 'Network.responseReceived' in event['method']]
        url = 'https://www.tiktok.com/api/share/settings/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=1&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/102.0.5005.63 Safari/537.36&channel=tiktok_web&cookie_enabled=true&device_id=7106332458585245185&device_platform=webapp_pc&focus_state=true&from_page=user&history_len=2&is_fullscreen=false&is_page_visible=true&mode=1&os=windows&priority_region=&referer=&region=VN&screen_height=600&screen_width=800&tz_name=Asia/Bangkok&webcast_language=en'
        for item in events:
            if "response" in item["params"]:
                if "url" in item["params"]["response"]:
                    if '/api/share/settings' in item["params"]["response"]["url"]:
                        url = item["params"]["response"]["url"]
                        break
        return parse_query(url)

    def first_data(self):
        data = self.driver.execute_script('return window.SIGI_STATE;')
        # print(data)
        return data

    def fetch_browser(self, url, params = ''):
        js = '''\
            fetch("%s", {
            "headers": { \
                "accept": "*/*",
        ''' % url
        if params != '':
            js += ''' \
            "x-tt-params": "%s",
            ''' % params
        js += ''' \
            },
            "referrer": "https://www.tiktok.com/",
            "referrerPolicy": "strict-origin-when-cross-origin",
            "body": null,
            "method": "GET",
            "mode": "cors",
            "credentials": "include"
            }).then(response => response.json())
            .then(data =>a = data);
        '''
        # print(js)
        self.driver.execute_script(js)
        import time 
        time.sleep(4)
        
        return self.driver.execute_script("return a;")

    def get_tt_params_script(self, url):
        js = _get_tt_params_script()
        self.driver.execute_script(js)
        import time 
        time.sleep(4)
        tt = self.driver.execute_script("""return window.genXTTParams("""
                + json.dumps(dict(parse_qsl(urlparse(url).query)))
                + """);
            
                }""")
        return tt

    def get_page_source(self):
        return self.driver.page_source

    def get_cookies(self):
        return self.driver.get_cookies()

    def close_browser(self):
        self.driver.close()
        self.driver.quit()

    
