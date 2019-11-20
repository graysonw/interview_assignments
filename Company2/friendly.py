import requests
from tenacity import retry
import config

session = requests.Session()


@retry(**config.friendly_retry_settings)
def get_pages():
    first_page = session.get(config.friendly["url"]).json()
    
    # Use a generator here so we can do lazy loading.
    yield first_page
    num_pages = first_page['total_pages']

    for page in range(2, num_pages + 1):
        next_page = session.get(config.friendly["url"], params={'page': page}).json()
        yield next_page
