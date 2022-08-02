import os
from RedDownloader import RedDownloader

# Class Objects
# Our object consist of:
# Identity : Urls, subreddits( NumberofPost, Sortby)
# State : Getting urls and subreddits names
# Behaviors : Downloading Images, Videos.

"""
Note: Downlaoding videos may sometimes getting some temporary (mp3/mp4) files while downloading 
according to the issue: #15 Unable to fetch posts Expecting value: line 1 column 1 (char 0) 

please check the folders the delete those temporary files
Support this Library: https://github.com/JackhammerYT/RedDownloader
"""
class Download:
  def __init__(self, url=None, subreddit=None, NumberOfPost=None, SortBy=None):
    self.url = url
    self.subreddit = subreddit
    self.NumberOfPost = NumberOfPost
    self.SortBy = SortBy
    self.NumberOfPost = 1

    # Built-in Functions
    self.download_path = "download"
    self.destination = os.path.join(self.download_path, "Reddit Videos")
    self.flair = None
    self.quality = 1080

  def get_single_video(self):
    RedDownloader.Download(self.url,self.quality,self.destination)
    return "Download Complete"

  def get_subreddit(self):
    RedDownloader.DownloadBySubreddit(self.subreddit, self.quality, self.flair, self.NumberOfPost, self.SortBy, self.destination)
    return "Download Complete"

  def get_video_subreddit(self):
    RedDownloader.DownloadVideosBySubreddit(self.subreddit, self.quality, self.NumberOfPost, self.SortBy, self.destination)
    return "Download Complete"
  
  def get_images_subreddit(self):
    RedDownloader.DownloadImagesBySubreddit(self.subreddit, self.quality, self.NumberOfPost, self.SortBy, self.destination)
    return "Download Complete"
  
def main():
    print("""
    888888ba   88888888b 888888ba  888888ba  88        
    88    `8b  88        88    `8b 88    `8b 88        
    88aaaa8P'  88aaaa    88     88 88     88 88        
    88   `8b.  88        88     88 88     88 88        
    88     88  88        88    .8P 88    .8P 88        
    dP     dP  88888888P 8888888P  8888888P  88888888P
    """)
    get_vid = int(input("Please select a format:\n[1] Video \n[2] Download Random Stuff at Subreddit\n"))

    try:
        if get_vid == 1:
            url = input("Please enter the URL of the video: ")
            Download(url).get_single_video()
        elif get_vid == 2:
            select_type = int(input("Please select a format:\n[1] Video \n[2] Image \n[3] Random Stuff \n"))
            if select_type == 1:
                subreddit = input("Please enter the subreddit: ")
                Download(subreddit).get_video_subreddit()
            elif select_type == 2:
                subreddit = input("Please enter the subreddit: ")
                Download(subreddit).get_images_subreddit()
            elif select_type == 3:
                subreddit = input("Please enter the subreddit: ")
                Download(subreddit).get_subreddit()
            else:
                print("Invalid format")
    except ConnectionError:
        print("Connection Error")

if __name__ == "__main__":
  main()
