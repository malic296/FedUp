import datetime
from .inews_fetcher import INewsFetcher
import feedparser
from urllib.parse import urlparse


class NewsFetcher(INewsFetcher):
    def fetch_news_rss(self) -> list:
        """ 
        Fetch news articles from various RSS feeds.
        Returns a list of news items with details such as title, description, link, publication date, author, language, and category.
        """
        
        howOld = datetime.timedelta(minutes=10)  # how old news can be to be fetched
        debug = False # Enable debug output, for debuging is recommended to set howOld to a higher value like hours=1

        if debug: print("Debugging is enabled")

        url_list = ["https://servis.idnes.cz/rss.aspx?c=zpravodaj",
                    "https://www.denik.cz/rss/zpravy.html", 
                    "https://feeds.bbci.co.uk/news/world/rss.xml",
                    "https://www.seznamzpravy.cz/rss", 
                    "https://ct24.ceskatelevize.cz/rss", 
                    "https://www.aktualne.cz/rss/",
                    "https://servis.lidovky.cz/rss.aspx",
                    "https://servis.lidovky.cz/rss.aspx?r=ln_lidovky",
                    "https://servis.lidovky.cz/rss.aspx?c=ln_nazory",
                    "https://servis.lidovky.cz/rss.aspx?c=ln_relax",
                    "https://servis.lidovky.cz/rss.aspx?c=ln_orientace",
                    "https://servis.lidovky.cz/rss.aspx?r=ln_serialy",
                    "https://www.parlamentnilisty.cz/export/rss.aspx", 
                    "https://feeds.bbci.co.uk/news/world/rss.xml", 
                    "https://feeds.bbci.co.uk/news/rss.xml",
                    "https://ir.thomsonreuters.com/rss/news-releases.xml?items=15",
                    "https://ir.thomsonreuters.com/rss/events.xml?items=15",
                    "https://ir.thomsonreuters.com/rss/sec-filings.xml?items=15", 
                    "https://www.theguardian.com/world/rss", 
                    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml", 
                    "http://rss.cnn.com/rss/edition.rss",
                    "https://www.aljazeera.com/xml/rss/all.xml", 
                    "http://feeds.washingtonpost.com/rss/world",
                    "https://www.economist.com/international/rss.xml", 
                    "https://www.spiegel.de/international/index.rss",
                    "https://www.lemonde.fr/rss/une.xml"]
        
        

        result = []  # result list for news items

        for url in url_list:
            feed = feedparser.parse(url)
            language = feed.feed.get("language") or "unknown"  # default language of feed

            credit = self.parseUrl(feed.feed.get("link")) # credit source parsed from feed link
            if credit == "unknown": credit = self.parseUrl(url)  or "unknown" # if not found in feed, parse from url
            

            if debug: 
                print(f"\n\n\nFeed language: {language}\nFeed credit: {credit}\n")
                counter = 0

            for entry in feed.entries:

                if debug: 
                    counter += 1
                    if counter >= 2: break  

                if not hasattr(entry, 'published_parsed'): continue # skip entries without published date

                published = datetime.datetime(*entry.published_parsed[:6]) #parsing published date and packing it into formated string
                if published < datetime.datetime.now() - howOld: continue # skip old news

                # get attributes with defaults
                summary = getattr(entry, "summary", "") or entry.get("summary", "")
                title = getattr(entry, "title", "No Title")
                link = getattr(entry, "link", "")
                
                if summary == "" or title == "No Title" or link == "":
                    if debug: print(f"Skipping entry due to missing fields: title='{title}', link='{link}', summary length={len(summary)}")
                    continue  # skip entries with missing essential fields

                # append news item to result list
                result.append({
                    "title": title,
                    "description": summary,
                    "link": link,
                    "publicationDate": published.strftime("%Y-%m-%dT%H:%M:%S"),
                    "author": credit,
                    "language": language,
                    "category": ""
                })

                if debug: print(result[counter-1])
        
        return result
                    


    #Helper method to parse credit source from url
    def parseUrl(self, raw_link: str) -> str:
        """
         Helper method to parse credit source from url
        """

        if raw_link:
            # ensure urlparse sees a scheme when missing (e.g. "www.example.com/path")
            tmp = raw_link if "://" in raw_link else "http://" + raw_link
            parsed = urlparse(tmp)
            # remove possible userinfo and port
            netloc = parsed.netloc.split("@")[-1].split(":")[0]
            credit = netloc or "unknown"
        else: credit = "unknown"
        return credit
        