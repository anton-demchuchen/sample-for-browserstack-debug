from selenium import webdriver


class WebDriver:
    @staticmethod
    def setup_driver(config):
        global web_driver
        if config['platform'] == 'desktop':

            if config["browser"] == "chrome":
                options = webdriver.ChromeOptions()
                options.add_argument("window-position=-1000,0")
                options.add_argument("--disable-extensions")
                options.add_argument("--disable-popup-blocking")  # Optional: Disable popups
                options.add_argument("--no-sandbox")
                options.add_argument("--guest")
                # options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
                options.set_capability('goog:loggingPrefs', {'browser': 'ALL', 'performance': 'ALL'})
                options.add_experimental_option("detach", True)
                prefs = {
                    'autofill.profile_enabled': False
                }
                options.add_experimental_option('prefs', prefs)
                if config["headless_mode"] is True:
                    options.add_argument("--headless")
                web_driver = webdriver.Chrome(options)
                web_driver.maximize_window()

            elif config["browser"] == "firefox":
                options = webdriver.FirefoxOptions()
                options.add_argument("window-position=-1000,0")
                if config["headless_mode"] is True:
                    options.headless = True
                web_driver = webdriver.Firefox(options)
                web_driver.maximize_window()


            elif config["browser"] == "edge":
                options = webdriver.EdgeOptions()
                options.use_chromium = True
                if config["headless_mode"] is True:
                    options.headless = True
                web_driver = webdriver.Edge(options)
                web_driver.maximize_window()

            elif config["browser"] == "safari":
                options = webdriver.SafariOptions()
                options.add_argument("window-position=-1000,0")
                if config["headless_mode"] is True:
                    options.headless = True
                web_driver = webdriver.Safari(options)
                web_driver.maximize_window()

        elif config['platform'] == 'mobile':

            if config["browser"] == "chrome":
                options = webdriver.ChromeOptions()
                options.add_argument("window-position=753,92")
                options.add_argument("--window-size=430,896")  # dimensions of the Iphone XR
                options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
                options.add_experimental_option("detach", True)
                prefs = {
                    'autofill.profile_enabled': False
                }
                options.add_experimental_option('prefs', prefs)
                options.add_argument('--disable-notifications')
                options.add_argument("--disable-infobars")
                options.add_argument("--disable-extensions")
                if config["headless_mode"] is True:
                    options.add_argument("--headless")
                web_driver = webdriver.Chrome(options)

            else:
                raise Exception(f'Browser "{config["browser"]}" is not supported in local mode')
        else:
            raise NameError(f'Invalid platform value "{config['platform']}" for web_driver.')
        return web_driver
