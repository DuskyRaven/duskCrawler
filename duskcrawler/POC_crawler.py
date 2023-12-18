from concurrent.futures import ThreadPoolExecutor, as_completed
from queue import Queue
from lxml.etree import HTML
from requests import get
# Global variables
visited_pages = set()
visited_articles = set()
pages_queue = Queue()
articles_queue = Queue()
def process_page(page_url: str):
    print(page_url)
    # global visited_pages, visited_articles, pages_queue, articles_queue
    try:
        response = get(page_url)
        tree = HTML(response.text)
        for page_link in tree.xpath(
            "//a[contains(@class, 'horo-card border-rad-4 px-1 pt-15 pb-2 text-center')]/@href"
        ):
            full_page_url = page_link
            if full_page_url not in visited_pages:
                pages_queue.put(full_page_url)
                visited_pages.add(full_page_url)
        # for article_link in tree.xpath("//a[contains(@class, 'horo-card border-rad-4 px-1 pt-15 pb-2 text-center')]/@href"):
        #     article_url = article_link
        #     if article_url not in visited_articles:
        #         visited_articles.add(article_url)
        #         articles_queue.put(article_url)
            print(full_page_url)
    except Exception as e:
        print("Error retrieving url:", e)
print("Example data: ")
process_page("https://www.astrology.com/horoscope/daily.html")
