from concurrent.futures import ThreadPoolExecutor, as_completed
from queue import Queue
from lxml.etree import HTML
from requests import get
import textwrap
# Global variables
visited_pages = set()
visited_articles = set()
pages_queue = Queue()
articles_queue = Queue()
def process_page(page_url: str):
    print(f"Start page: {page_url}")
    # global visited_pages, visited_articles, pages_queue, articles_queue
    try:
        response = get(page_url)
        tree = HTML(response.text)
        for page_link in tree.xpath(
            "//a[contains(@class, 'horo-card border-rad-4 px-1 pt-15 pb-2 text-center')]/@href"
        ):
            full_page_url = page_link
            print(full_page_url)
            response1 = get(page_link)
            tree1 = HTML(response1.text)
            for date in tree1.xpath(
                "//span[contains(@id, 'content-date')]/text()"
            ):
                print(str("\033[1m" + date + "\033[0m"))
            print("")
            for text in tree1.xpath(
                "//span[contains(@style, 'font-weight: 400')]/text()"
            ):
                print(textwrap.fill(text))
            print("")
            if full_page_url not in visited_pages:
                pages_queue.put(full_page_url)
                visited_pages.add(full_page_url)
    except Exception as e:
        print("Error retrieving url:", e)
print("Example data: ")
process_page("https://www.astrology.com/horoscope/daily.html")
