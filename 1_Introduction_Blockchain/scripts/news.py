# Cryptocurrency news sorting

class News:
    
    # Initialization
    def __init__(self, header):
        self.header = header                                # header of the news

    def is_about_token(self, token_name):
        return token_name.lower() in self.header.lower()   # Case insensitive check
        
class NewsBox:
    
    # Initialization
    def __init__(self, coin_name):
        self.coin_name = coin_name                        # Cryptocurrency name to monitor
        self.collected_news = []                          # Collection of relevant news
        
    # Method to gather news related to the specified cryptocurrency
    def deliver_news(self, news):
        if news.is_about_token(self.coin_name):           # If the news pertains to our cryptocurrency...
            self.collected_news.append(news)              # Save it for future reference
            
    # Method to display all collected news
    def consult(self):
        for news in self.collected_news:                  # For each piece of news
            print(news.header)                             # Display the header