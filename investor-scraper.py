import json
import scrapy
from scrapy.crawler import CrawlerProcess


amplify_urls = []

class AmplifySpider(scrapy.Spider):
    name = "amplify"
    start_urls = [
        "https://www.amplifypartners.com/portfolio",
    ]
    results = []

    def parse(self, response):
        for company in response.css("div.w-dyn-item"):
            if company.css("div.status-div > div::text").get() is None:
                continue

            if company.css("div.status-div > div::text").get() in ['IPO', 'Acquired']:
                continue

            url = company.css("div.website__link-wr > a::attr('href')").get()
            self.results.append(url)

    def close(self, ):
        global amplify_urls
        amplify_urls = self.results

def main():
    process = CrawlerProcess(
        settings={
            "LOG_ENABLED": False,
        }
    )

    process.crawl(AmplifySpider)
    process.start()

    results = {}
    results["amplifypartners.com"] = amplify_urls
    results = json.dumps(results, indent=2)
    with open("results.json", "w") as outfile:
        outfile.write(results)
    print(results)


if __name__=="__main__":
    main()
