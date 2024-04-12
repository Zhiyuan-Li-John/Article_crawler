import requests
import feedparser
import datetime
import os

def format_date(days=0):
    return (datetime.datetime.now() - datetime.timedelta(days=days)).strftime('%Y%m%d')

def is_related_by_keyword(title, summary, keywords):
        text = title.lower() + " " + summary.lower()
        return any(keyword.lower() in text for keyword in keywords)
class arxiv_reader():
    """
    feedparser Version
    """
    def __init__(self) -> None:
        self.articles = []
        self.match_articles = []
        self.today_date = format_date()
        self.yesterday_date = format_date(1)
        self.url = f'http://export.arxiv.org/api/query?search_query=submittedDate:[{self.yesterday_date}+TO+{self.today_date}]&sortBy=submittedDate&sortOrder=descending&max_results=1000'
        super().__init__()

    def get_your_interest(self, interests):
        """
        interest is a list. e.g. interests = ["image captioning", "visual question answering"]
        """
        self.interests = interests
        
    def read_articles(self):
        """
        The article information is stored in a dictionary. The form looks like {"title": title, "summary": summary, "link": link}
        """
        # Parse the feed using feedparser
        response = requests.get(self.url)
        feed = feedparser.parse(response.content)

        #Store article title and summary into a dictionary, store article into a articles list
        for entry in feed.entries:
            article = {}
            article["title"] = entry.title
            article["link"] = entry.link
            article["summary"] = entry.summary
            self.articles.append(article)
        
    
    def print_out(self):
        """
        Print out the article information stored in the list
        """
        for entry in self.articles:
            print("Title:", entry["title"])
            print("Summary:", entry["summary"])
            print("Link:", entry["link"])
            print("\n")

    def find_match(self):
        folder_path = "record/" + str(datetime.datetime.now().strftime('%Y%m%d'))
        os.makedirs(folder_path, exist_ok=True)
        text_path = os.path.join(folder_path, '%s.txt' %(str(datetime.datetime.now().strftime('%Y%m%d'))))
        self
        for entry in self.articles:
            title = entry["title"]
            summary = entry["summary"]
            link = entry["link"]
            if is_related_by_keyword(title, summary, self.interests):
                with open(text_path, "a") as file:
                    file.write("Tittle: " + title + "\n")
                    file.write("Summary: "+ summary + "\n")
                    file.write("Link:" + link + "\n")
                    file.write("\n")
                self.match_articles.append(entry)
    
    def print_out_matching(self):
        """
        Print out the article information stored in the list
        """
        for entry in self.match_articles:
            print("Title:", entry["title"])
            print("Summary:", entry["summary"])
            print("Link:", entry["link"])
            print("\n")

        





            



   

    

        
            

        






