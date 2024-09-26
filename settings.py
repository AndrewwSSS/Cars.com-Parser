USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
             "AppleWebKit/537.36 (KHTML, like Gecko) " \
             "Chrome/112.0.0.0 Safari/537.36"\

PAGE_SIZE = 20

BASE_URL = f"https://www.cars.com/shopping/results/?&include_shippable=true&stock_type=all&maximum_distance=all&page_size={PAGE_SIZE}"
DETAIL_URL_PATTERN = "https://www.cars.com/vehicledetail/{listing_id}"

PROXIES = [
    "gtjikewl:lyeraqmvxaix@38.154.227.167:5868",
    "gtjikewl:lyeraqmvxaix@45.127.248.127:5128",
    "gtjikewl:lyeraqmvxaix@207.244.217.165:6712",
    "gtjikewl:lyeraqmvxaix@64.64.118.149:6732",
    "gtjikewl:lyeraqmvxaix@167.160.180.203:6754",
    "gtjikewl:lyeraqmvxaix@104.239.105.125:6655",
    "gtjikewl:lyeraqmvxaix@198.105.101.92:5721",
    "gtjikewl:lyeraqmvxaix@154.36.110.199:6853",
    "gtjikewl:lyeraqmvxaix@204.44.69.89:6342",
    "gtjikewl:lyeraqmvxaix@206.41.172.74:6634"
]

OUTPUT_FILEPATH = "cars.csv"



