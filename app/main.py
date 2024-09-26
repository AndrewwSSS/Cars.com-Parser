import json
import random

from selenium.common import TimeoutException
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import settings
from models import Car


def get_seleniumwire_options() -> dict:
    proxy = random.choice(settings.PROXIES)
    return {
        "proxy": {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}",
            "no_proxy": "localhost,127.0.0.1"
        }
    }


def change_driver_proxy(driver: webdriver.Chrome) -> None:
    new_proxy = random.choice(settings.PROXIES)
    driver.proxy = {
        "http": f"http://{new_proxy}",
        "https": f"https://{new_proxy}",
        "no_proxy": "localhost,127.0.0.1"
    }


def get_chrome_options(user_agent: str, load_strategy: str = "eager") -> Options:
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(f"user-agent={user_agent}")
    chrome_options.page_load_strategy = load_strategy
    return chrome_options


def interceptor(request):
    request.headers["User-Agent"] = settings.USER_AGENT
    request.headers["Accept-Language"] = "en-US,en;q=0.9"
    request.headers["Referer"] = "https://www.google.com/"


def get_pages_number(driver: webdriver.Chrome) -> int:
    test = (
        driver.find_elements(
            By.CSS_SELECTOR,
            "spark-pagination ul li"
        )[-1].text
    )
    return int(test)


def scrape_contact_information(cars: [Car]) -> None:
    detailed_driver = webdriver.Chrome(
        options=get_chrome_options(settings.USER_AGENT),
        seleniumwire_options=get_seleniumwire_options()
    )

    for car in cars:
        detailed_driver.get(
            settings.DETAIL_URL_PATTERN.format(listing_id=car.listing_id)
        )

        try:
            element = detailed_driver.find_element(
                By.ID,
                "CarsWeb.ListingController.show"
            )
            json_data = json.loads(element.get_attribute("innerHTML"))
            car.contact = json_data["callSourceDniMetadata"]["seller"]["phoneNumber"]
        except TimeoutException:
            ...

    detailed_driver.quit()


def get_cars() -> [Car]:
    driver = webdriver.Chrome(
        options=get_chrome_options(settings.USER_AGENT),
        seleniumwire_options=get_seleniumwire_options(),
    )

    driver.request_interceptor = interceptor
    current_page = 1
    pages_count = None
    cars = []
    unique_cars = set()

    while True:
        driver.get(settings.BASE_URL + f"&page={current_page}")

        if not pages_count:
            pages_count = get_pages_number(driver)

        json_data = driver.find_element(
            By.ID, "search-live-content"
        ).get_attribute("data-site-activity")

        new_cars = []
        for car_json in json.loads(json_data)["vehicleArray"]:
            identifier = car_json["canonical_mmty"]
            if identifier in unique_cars:
                continue
            new_cars.append(
                Car(
                    car_json["make"],
                    car_json["model"],
                    int(car_json["year"]),
                    int(car_json["price"]) if car_json["price"] else None,
                    car_json["listing_id"],
                )
            )
            unique_cars.add(identifier)

        scrape_contact_information(new_cars)
        cars.extend(new_cars)

        if current_page == pages_count:
            return cars
        current_page += 1


def main():
    cars = get_cars()
    Car.write_to_csv(cars, settings.OUTPUT_FILEPATH)


if __name__ == "__main__":
    main()
