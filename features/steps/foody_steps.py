from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from entity.foody import Foody
import time
from main import crawl_by_name


@given('Login by username and password.')
def login_foody(context):
    print("HERE: " + "https://id.foody.vn/account/login")
    # context.browser = webdriver.Chrome('dependencies/chromedriver')
    context.browser.get("https://id.foody.vn/account/login")

    username_input = context.browser.find_element_by_id("Email")
    username_input.send_keys("phuongvuong98@gmail.com")
    pass_input = context.browser.find_element_by_id("Password")
    pass_input.send_keys("Vuong0935986100")

    submit_button = context.browser.find_element_by_id("bt_submit")
    submit_button.click()


@when(u'Click into foody icon with {category}')
def click_foody(context, category):
    context.browser.get("https://www.foody.vn/ho-chi-minh/food/" + category)


@when(u'Search into Ho Chi Minh with {category}')
def search_ho_chi_minh(context, category):
    context.browser.get("https://www.foody.vn/ho-chi-minh/food/" + category)


    context.browser.find_element_by_class_name("fd-btn-login-new").click()

    store = []
    sum_str = context.browser.find_element_by_class_name('number-msg').text
    sum = sum_str[:sum_str.find('kết quả')].strip().replace(",", "").replace(".", "")

    print(sum)
    print(int(int(sum) / 12) + 1)
    queue_check_heigh = []

    SCROLL_PAUSE_TIME = 1

    # Get scroll height
    last_height = context.browser.execute_script("return document.body.scrollHeight")

    while True:
        time.sleep(1)
        # Scroll down to bottom
        context.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)


        # Calculate new scroll height and compare with last scroll height
        new_height = context.browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    context.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    element = context.browser.find_element_by_id("catfish-banner")
    context.browser.execute_script("arguments[0].setAttribute('style','display:none;')", element)

    while True:
        print("Prepare click ")
        try:
            context.browser.find_element_by_partial_link_text('Xem tiếp').click()
        except:
            pass
        while True:
            # Scroll down to bottom
            context.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)


            # Calculate new scroll height and compare with last scroll height
            new_height = context.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        height = context.browser.execute_script("return document.documentElement.scrollHeight")
        queue_check_heigh.append(height)
        new_height = height - 1500
        print('Height:', height)
        context.browser.execute_script("window.scrollTo(0, " + str(new_height) + ");")

        print("Check height:", int(int(height)/10000))
        if int(int(height)/10000) % 2 == 0:
            items = context.browser.find_elements_by_class_name('filter-result-item')

            for i in range(0, len(items) - 6):
                try:
                    if items[i].find_element_by_tag_name('h2'):
                        print(items[i].find_element_by_tag_name('h2').text)

                        name = items[i].find_element_by_tag_name('h2').text
                        link = items[i].find_element_by_tag_name('a').get_attribute('href')
                        address = items[i].find_element_by_class_name('address').text
                        address = address[:-1] if address[len(address) - 1] == ',' else address
                        system = "0"

                        # if store is system -> save system = 1
                        if address.find("chi nhánh") != -1:
                            system = "1"

                        str_store = name + '|' + link + '|' + address + '|' + system

                        store.append(str_store)
                except:
                    continue

            obj_store = set(store)

            print(obj_store)
            print(len(obj_store))

            for item in obj_store:
                name = item.split("|")[0]
                link_foody = item.split("|")[1]
                address = item.split("|")[2]
                system = item.split("|")[3]

                if len(Foody.objects(name__exact=name, category__exact=category)) == 0:
                    print(name)
                    Foody(name=name, link_foody=link_foody, category=category, address=address, system=system).save()

        if queue_check_heigh.count(height) == 3:
            break

        try:
            check = context.browser.find_element_by_partial_link_text('Xem tiếp')
        except NoSuchElementException:
            print("End game")
            break

        time.sleep(1)

    items = context.browser.find_elements_by_class_name('filter-result-item')

    for i in range(0, len(items) - 6):
        try:
            if items[i].find_element_by_tag_name('h2'):
                print(items[i].find_element_by_tag_name('h2').text)

                name = items[i].find_element_by_tag_name('h2').text
                link = items[i].find_element_by_tag_name('a').get_attribute('href')
                address = items[i].find_element_by_class_name('address').text
                address = address[:-1] if address[len(address) - 1] == ',' else address
                system = "0"

                # if store is system -> save system = 1
                if address.find("chi nhánh") != -1:
                    system = "1"

                str_store = name + '|' + link + '|' + address + '|' + system

                store.append(str_store)
        except:
            continue

    obj_store = set(store)

    print(obj_store)
    print(len(obj_store))

    for item in obj_store:
        name = item.split("|")[0]
        link_foody = item.split("|")[1]
        address = item.split("|")[2]
        system = item.split("|")[3]

        if len(Foody.objects(name__exact=name, category__exact=category)) == 0:
            print(name)
            Foody(name=name, link_foody=link_foody, category=category, address=address, system=system).save()


@when(u'Handle each system store with {category}')
def handle_system_store(context, category):
    store = []
    for item in Foody.objects:
        if item.system == "1" and item.category == category:

            print(item.name)
            context.browser.get(item.link_foody)
            items = context.browser.find_elements_by_class_name('ldc-item')

            for i in range(0, len(items)):
                try:
                    if items[i].find_element_by_tag_name('h2'):
                        print(items[i].find_element_by_tag_name('h2').text)

                        name = items[i].find_element_by_tag_name('h2').text
                        link = items[i].find_element_by_tag_name('a').get_attribute('href')
                        address = items[i].find_element_by_class_name('ldc-item-h-address').text
                        address = address[:-1] if address[len(address) - 1] == ',' else address
                        system = "0"

                        str_store = name + '|' + link + '|' + address + '|' + system

                        store.append(str_store)

                except:
                    continue

            obj_store = set(store)
            print(obj_store)
            print(len(obj_store))

            for y in obj_store:
                name = y.split("|")[0]
                link_foody = y.split("|")[1]
                address = y.split("|")[2]
                system = y.split("|")[3]

                if len(Foody.objects(name__exact=name, category__exact=category)) == 0:
                    print(name)
                    Foody(name=name, link_foody=link_foody, category=category, address=address, system=system).save()
    Foody.objects(system="1", category=category).delete()


@when(u'Handle price each store with {category}')
def handle_price(context, category):
    print(len(Foody.objects))
    for item in Foody.objects:
        if item.system == "0" and item.category == category:
            if item.price is None:
                print(item.name)
                context.browser.get(item.link_foody)
                try:
                    price = context.browser.find_element_by_class_name('res-common-minmaxprice').text

                    print(price)
                    Foody.objects(id__exact=item.id).update(set__price=price)
                except:
                    price = context.browser.find_element_by_class_name('res-common-minmaxprice').text

                    print(price)
                    Foody.objects(id__exact=item.id).update(set__price=price)


@when(u'Open google maps')
def open_gg(context):
    context.browser.get("https://www.google.com/maps")


@when(u'Save link with {category}')
def save_link_gg(context, category):
    test_input = context.browser.find_element_by_class_name("tactile-searchbox-input")
    test_input.send_keys(Foody.objects[0].name)
    test_btn = context.browser.find_element_by_class_name("searchbox-searchbutton")
    test_btn.click()
    time.sleep(3)

    for item in Foody.objects:

        if not item.link_gg and item.category == category:

            # search by name + address
            print(item.name.split("-")[0])

            search_input = context.browser.find_element_by_class_name("tactile-searchbox-input")
            search_input.clear()
            search_input.send_keys(item.name.split("-")[0] + " " + item.address)

            search_btn = context.browser.find_element_by_class_name("searchbox-searchbutton")
            search_btn.click()

            time.sleep(3)

            print(context.browser.current_url)
            link_gg = "no_n_a" if context.browser.current_url.find("/maps/place/") == -1 else context.browser.current_url

            print(Foody.objects(link_gg__exact=link_gg, category__exact=category))

            # search by name
            if link_gg == "no_n_a":
                search_input = context.browser.find_element_by_class_name("tactile-searchbox-input")
                search_input.clear()
                search_input.send_keys(item.name.split("-")[0] + "TP Ho Chi Minh")

                search_btn = context.browser.find_element_by_class_name("searchbox-searchbutton")
                search_btn.click()

                time.sleep(3)

            print(context.browser.current_url)
            link_gg = "no_n" if context.browser.current_url.find(
                "/maps/place/") == -1 else context.browser.current_url

            if Foody.objects(link_gg__exact=link_gg, category__exact=category):
                link_gg = "dup"


            location = {"lat": 0, "long": 0}
            # handle link_gg into lat and long
            if link_gg.find("https://www.google.com/maps/place/") != -1:
                print("Link_gg:", link_gg)
                idx_1 = link_gg.find("/@")
                idx_2 = link_gg.find("z/")

                sub_link = link_gg[idx_1:idx_2]
                print("Sub:", sub_link)
                lat = sub_link.split(",")[0][2:]
                long = sub_link.split(",")[1]
                location = {"lat": lat, "long": long}



            Foody.objects(id__exact=item.id).update(set__link_gg=link_gg, set__location=location)
