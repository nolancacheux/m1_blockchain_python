# News sorting about cryptocurrencies

class News:
    
    # Constructor
    def __init__(self, header):
        self.header = header                              # News header

    def is_about_token(self, tokenName):
        return tokenName.lower() in self.header.lower()   # Take upper/lower case into account
        
class NewsBox:
    
    # Constructeur
    def __init__(self, coinName):
        self.coinName = coinName                          # Name of the cryptocurrency to watch
        self.savedNews = []                               # Box of news to deliver
        
    # Function that accumulates only the news about the desired cryptocurrency
    def deliver_news(self, news):
        if news.is_about_token(self.coinName):            # If the recevied news is about our cryptocurrency...
            self.savedNews.append(news)                   # We save it for later
            
    # Function that displays all the news in the box
    def consult(self):
        for news in self.savedNews:                       # For each news
            print(news.header)                            # We display the news