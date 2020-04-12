from mongoengine import disconnect
from selenium import webdriver
from app import create_app


def before_all(context):
    print("Executing before all")
    disconnect(alias='default')
    context.app = create_app('testing')
    context.client = context.app.test_client(use_cookies=True)
    options = webdriver.ChromeOptions()
    # prefs = {'profile.default_content_setting_values': {'cookies': 2,
    #                                                     'plugins': 2, 'popups': 2, 'geolocation': 2,
    #                                                     'notifications': 2, 'auto_select_certificate': 2,
    #                                                     'fullscreen': 2,
    #                                                     'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
    #                                                     'media_stream_mic': 2, 'media_stream_camera': 2,
    #                                                     'protocol_handlers': 2,
    #                                                     'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
    #                                                     'push_messaging': 2, 'ssl_cert_decisions': 2,
    #                                                     'metro_switch_to_desktop': 2,
    #                                                     'protected_media_identifier': 2, 'app_banner': 2,
    #                                                     'site_engagement': 2,
    #                                                     'durable_storage': 2}}

    # 'javascript': 2,'images': 2,
    # options.add_experimental_option('prefs', prefs)
    # options.add_argument("start-maximized")
    # options.add_argument("disable-infobars")
    # options.add_argument("--disable-extensions")
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # context.browser = webdriver.Chrome(chrome_options=options, executable_path='dependencies/chromedriver')
    # context.browser = webdriver.Chrome('dependencies/chromedriver')
    # 'dependencies/geckodriver_2'
    context.browser = webdriver.Firefox()
    context.browser.maximize_window()
    context.browser.implicitly_wait(20)


def before_feature(context, feature):
    print("Before feature\n")


# Scenario level objects are popped off context when scenario exits
def before_scenario(context, scenario):
    print("Before scenario\n")


def after_scenario(context, scenario):
    print("After scenario\n")


def after_feature(context, feature):
    print("\nAfter feature")


def after_all(context):
    print("Executing after all")





