from selenium.webdriver.common.by import By

from pages.base import BasePage
from pages.config import TestData


class MainPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    MAIN_LOGO = (By.CSS_SELECTOR, "#stickyHeader div")
    CATALOG = (By.CSS_SELECTOR, "div[data-widget ='catalogMenu'] div button")
    ELECTRONICA_SUB = (By.XPATH, "//a[@class = 'a3p5 g5s4 g5s6 g5t' and @href='/category/elektronika-15500/']")
    HEAD_OF_PAGE_ELECTRONICA_SUB = (By.XPATH, "//h1[@class = 'b3a0' and contains (text(), 'Электроника')]")
    SEARCH_WHERE = (By.CSS_SELECTOR, "div[data-widget = 'searchBarDesktop'] form div span")
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder = 'Искать на Ozon']")
    SUBMIT_SEARCH = (By.XPATH, "//button[@class = 'aa2i']")
    ENTRANCE = (By.CSS_SELECTOR, "div[data-widget = 'profileMenuAnonymous']")
    POPUP_WINDOW_ENTRANCE = (By.XPATH, "//div[@class = 'ui-k6']")
    FAVORITES = (By.XPATH, "//a[@href = '/my/favorites']")
    HEAD_OF_PAGE_FAVORITES = (By.XPATH, "//div[@class = 'a4' and contains (text(), 'Товары и списки')]")
    CART = (By.XPATH, "//a[@href = '/cart']")
    ORDERS = (By.XPATH, "//a[@href = '/my/orderlist']")
    TOPFASHION = (By.XPATH, "//a[@href = '/highlight/top-fashion/' and @class = 'a4 q3c']")
    HEAD_OF_PAGE_TOP_FASHION = (By.XPATH, "//h1[@class = 'jx' and contains (text(), 'TOP Fashion')]")
    Premium = (By.XPATH, "//a[@href = '/highlight/premium/' and @class = 'a4 q3c']")
    OZON_TRAVEL = (By.XPATH, "//a[@href = 'https://www.ozon.ru/travel/hotels/?mwc_campaign=airplane_main_hotel' and @class = 'a4 q3c']")
    OZON_KART = (By.XPATH, "//a[@href = 'https://www.ozon.ru/highlight/keshbek-do-30-dlya-ozon-schet-i-premium-323369' and @class = 'a4 q3c']")
    LIVE = (By.XPATH, "//a[@href = '/live/' and @class = 'a3p5 g5e3']")
    ACTIONS = (By.XPATH, "//a[@href = '/highlight/globalpromo/' and @class = 'a4 q3c']")
    HEAD_OF_PAGE_ACTIONS = (By.XPATH, "//div[@class = 'a3p5' and contains (text(), 'Акции и спецпредложения')]")
    BRENDS = (By.XPATH, "//a[@href = '/brand/' and @class = 'a4 q3c']")
    HEAD_OF_PAGE_BRENDS = (By.XPATH, "//h1[@class = 'yj4 tsHeadXL' and contains (text(), 'Все бренды')]")
    SHOPS = (By.XPATH, "//a[@href = '/seller/' and @class = 'a3p5 g5e3']")
    HEAD_OF_PAGE_SHOPS = (By.XPATH, "//div[@class = 'g2f8' and contains (text(), 'Все магазины')]")
    ELECTRONICA_MAIN = (By.XPATH, "//a[@href = '/category/elektronika-15500/' and contains (text(), 'Электроника')]")
    HEAD_OF_PAGE_ELECTRONICA_MAIN = (By.XPATH, "//h1[@class = 'zj8' and contains (text(), 'Электроника')]")
    CLOTHES_AND_SHOES = (By.XPATH, "//a[@href = '/category/zhenskaya-odezhda-7501/' and contains (text(), 'Одежда и обувь')]")
    CHAPTER_OF_CLOTHES_AND_SHOES = (By.XPATH, "//div[@class = 'a4' and contains (text(), 'Женская одежда, обувь и аксессуары')]")
    KIDS_GOODS = (By.XPATH, "//a[@href = '/category/detskie-tovary-7000/' and contains (text(), 'Детские товары')]")
    HEAD_OF_PAGE_KIDS_GOODS = (By.XPATH, "//h1[@class = 'zj8' and contains (text(), 'Детские товары')]")
    HOUSE_AND_GARDEN = (By.XPATH, "//a[@href = '/category/dom-i-sad-14500/' and contains (text(), 'Дом и сад')]")
    HEAD_OF_PAGE_HOUSE_AND_GARDEN = (By.XPATH, "//h1[@class = 'zj8' and contains (text(), 'Дом и сад')]")
    BUTTON_SELECT_CITY = (By.XPATH, "//button[@type = 'button' and @class = 'ui-b2']")
    INPUT_FIELD_CITY = (By.XPATH, "//input[@class = 'ui-g ui-g2' and @type = 'text']")
    LIST_OF_SUITABLE_CITIES = (By.XPATH, "//ul[@class = 'a3i7']")
    LIMIT = (By.XPATH, "//a[@href = '/section/limit/' and contains (text(), 'Рассрочка']")
    HEAD_OF_PAGE_LIMIT = (By.XPATH, "//h1[@class = 'header__title' and contains (text(), 'Подключите оплату в рассрочку'")
    EXPRESS = (By.XPATH, "//a[@href = '/highlight/express/' and @class = 'a4 c9q marked-element']")
    HEAD_OF_PAGE_EXPRESS = (By.XPATH, "//h1[@class = 'zj8 marked-element' and contains (text(), 'Товары с экспресс-доставкой')]")
    CERTIFICATES = (By.XPATH, "//a[@href = '/context/detail/id/135382627/?perehod=menu' and @class = 'a4 c9q']")
    HEAD_OF_PAGE_CERTIFICATES = (By.XPATH, "//h1[@class = 'n7n marked-element' and contains (text(), 'Электронный подарочный сертификат Миллион подарков (3000) ozon'")