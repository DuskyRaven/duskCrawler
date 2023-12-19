from lxml.etree import HTML
from requests import get
import textwrap
import csv
# pd data set
dataset = []

# Crawling
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
            print("")
            print(f"Article link: {full_page_url}")
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
            for title1 in tree1.xpath(
                "//h4[contains(@class, 'header-container mb-1 mb-md-15')]/text()"
            ):
                tt1 = title1.__str__().strip()
                tt2 = tree1.xpath("//h4[contains(text(), 'Daily Food Horoscope')]/text()").__str__().strip("['\\n ").strip(" \\n']").strip()
                tt3 = tree1.xpath("//h4[contains(text(), 'Daily Home Horoscope')]/text()").__str__().strip("['\\n ").strip(" \\n']").strip()
                tt4 = tree1.xpath("//h4[contains(text(), 'Daily Dog Horoscope')]/text()").__str__().strip("['\\n ").strip(" \\n']").strip()
                tt5 = tree1.xpath("//h4[contains(text(), 'Daily Teen Horoscope')]/text()").__str__().strip("['\\n ").strip(" \\n']").strip()
                tt6 = tree1.xpath("//h4[contains(text(), 'Daily Cat Horoscope')]/text()").__str__().strip("['\\n ").strip(" \\n']").strip()
                tt7 = tree1.xpath("//h4[contains(text(), 'Daily Bonus Horoscope')]/text()").__str__().strip("['\\n ").strip(" \\n']").strip()
                if tt1 == tt2:
                    par1 = tree1.xpath("//div[contains(@id, 'content-food')]/text()")
                    par1 = par1.__str__().strip('["\\n ').strip(' \\n"]').strip("['\\n ").strip(" \\n']").strip()
                    print("\033[1m" + title1 + "\033[0m")
                    print(textwrap.fill(par1))
                elif tt1 == tt3:
                    par2 = tree1.xpath("//div[contains(@id, 'content-home')]/text()")
                    par2 = par2.__str__().strip('["\\n ').strip(' \\n"]').strip("['\\n ").strip(" \\n']").strip()
                    print("\033[1m" + title1 + "\033[0m")
                    print(textwrap.fill(par2))
                elif tt1 == tt4:
                    par3 = tree1.xpath("//div[contains(@id, 'content-dog')]/text()")
                    par3 = par3.__str__().strip('["\\n ').strip(' \\n"]').strip("['\\n ").strip(" \\n']").strip()
                    print("\033[1m" + title1 + "\033[0m")
                    print(textwrap.fill(par3))
                elif tt1 == tt5:
                    par4 = tree1.xpath("//div[contains(@id, 'content-teen')]/text()")
                    par4 = par4.__str__().strip('["\\n ').strip(' \\n"]').strip("['\\n ").strip(" \\n']").strip()
                    print("\033[1m" + title1 + "\033[0m")
                    print(textwrap.fill(par4))
                elif tt1 == tt6:
                    par5 = tree1.xpath("//div[contains(@id, 'content-cat')]/text()")
                    par5 = par5.__str__().strip('["\\n ').strip(' \\n"]').strip("['\\n ").strip(" \\n']").strip()
                    print("\033[1m" + title1 + "\033[0m")
                    print(textwrap.fill(par5))
                elif tt1 == tt7:
                    par6 = tree1.xpath("//div[contains(@id, 'content-bonus')]/text()")
                    par6 = par6.__str__().strip('["\\n ').strip(' \\n"]').strip("['\\n ").strip(" \\n']").strip()
                    print("\033[1m" + title1 + "\033[0m")
                    print(textwrap.fill(par6))
                else:
                    print("error")
    except Exception as e:
        print("Error retrieving url:", e)

print("Example data: ")
process_page("https://www.astrology.com/horoscope/daily.html")
# Testing inputs from user
while True:
    prompt1 = input("Would you like for the data to be saved on your computer?").lower()
    if prompt1 == "yes":
        print("Hooray")
        break
    elif prompt1 == "no":
        print("T_T")
        break
    else:
        print("whaa?")
        print("Answer must be a 'yes' or a 'no' ")