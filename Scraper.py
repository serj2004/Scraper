class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        res = []
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                res.append(url)
        return res


news = "https://yandex.ru"

res = Scraper(news).scrape()

with open('C:\\Users\Сергей\Desktop\файлы 10мб\File_113.txt', "w") as f:
    for l in res:
        f.write(f"{l}\n")
