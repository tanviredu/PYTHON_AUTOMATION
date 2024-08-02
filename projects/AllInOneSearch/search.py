import webbrowser
import time

class Search:
    
    __slots__ = ("keyword")
    def __init__(self,keyword):
        self.keyword  = keyword\
            
    def search_google(self):
        BASE_LINK     = "https://www.google.com/search?q="
        SEARCH_PATERN = BASE_LINK + self.keyword
        #time.sleep(1)
        try:
            webbrowser.open_new_tab(SEARCH_PATERN)
        except:
            print("Error opening google")
        
    def search_bing(self):
        BASE_LINK     = "https://www.bing.com/search?q="
        SEARCH_PATERN = BASE_LINK + self.keyword
        #time.sleep(1)
        try:
            webbrowser.open_new_tab(SEARCH_PATERN)
        except:
            print("Error opening bing")
    
    def search_wikipedia(self):
        BASE_LINK     = "https://en.wikipedia.org/wiki/"
        SEARCH_PATERN = BASE_LINK + self.keyword
        #time.sleep(1)
        try:
            webbrowser.open_new_tab(SEARCH_PATERN)
        except:
            print("Error opening wiki")
    
    def search_ddg(self):
        BASE_LINK     = "https://duckduckgo.com/?t=h_&q="
        SEARCH_PATERN = BASE_LINK + self.keyword
        #time.sleep(1)
        try:
            webbrowser.open_new_tab(SEARCH_PATERN)
        except:
            print("Error opening duck duck go")
    

def main():
    print("Enter your keyword for search")
    keyword = input("==>")
    web = Search(keyword)
    web.search_google()
    web.search_bing()
    web.search_wikipedia()
    web.search_ddg()
    

if __name__ == "__main__":
    main()
    

