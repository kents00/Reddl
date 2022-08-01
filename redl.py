import os
from RedDownloader import RedDownloader

download_path = "download"

def get_video_subreddit(subreddit):
    
    get_shortby = int(input("Please select a shortby:\n[1] Top \n[2] New \n[3] Hot \n"))
    if get_shortby == 1:
        get_shortby = "top"
    elif get_shortby == 2:
        get_shortby = "new"
    elif get_shortby == 3:
        get_shortby = "hot"
    else:
        print("Invalid shortby")
    NumberOfPosts = int(input("Please enter the number of posts to download: "))
    RedDownloader.DownloadVideosBySubreddit(subreddit, quality=720, NumberOfPosts=NumberOfPosts , SortBy = get_shortby,destination=os.path.join(download_path, 'RedditVideos'))
    print("Subreddit videos downloaded successfully!")

def get_images_subreddit(subreddit):
    
    get_shortby = int(input("Please select a shortby:\n[1] Top \n[2] New \n[3] Hot \n"))
    if get_shortby == 1:
        get_shortby = "top"
    elif get_shortby == 2:
        get_shortby = "new"
    elif get_shortby == 3:
        get_shortby = "hot"
    else:
        print("Invalid shortby")
    NumberOfPosts = int(input("Please enter the number of posts to download: "))
    RedDownloader.DownloadImagesBySubreddit(subreddit, quality=720, NumberOfPosts=NumberOfPosts , SortBy = get_shortby,destination=os.path.join(download_path, 'RedditVideos'))
    print("Subreddit Images downloaded successfully!")

def get_stuff_subreddit(subreddit):
    NumberOfPosts = int(input("Please enter the number of posts to download: "))
    get_shortby = int(input("Please select a shortby:\n[1] Top \n[2] New \n[3] Hot \n"))
    if get_shortby == 1:
        get_shortby = "top"
    elif get_shortby == 2:
        get_shortby = "new"
    elif get_shortby == 3:
        get_shortby = "hot"
    else:
        print("Invalid shortby")
    RedDownloader.DownloadBySubreddit(subreddit, quality=720, NumberOfPosts=NumberOfPosts, SortBy = get_shortby,flair = None ,destination=os.path.join(download_path, 'RedditVideos'))
    print("Subreddit downloaded successfully!")

def main():
    print("""
    888888ba   88888888b 888888ba  888888ba  dP        
    88    `8b  88        88    `8b 88    `8b 88        
   a88aaaa8P' a88aaaa    88     88 88     88 88        
    88   `8b.  88        88     88 88     88 88        
    88     88  88        88    .8P 88    .8P 88        
    dP     dP  88888888P 8888888P  8888888P  88888888P
    """)
    get_vid = int(input("Please select a format:\n[1] Video \n[2] Download Random Stuff at Subreddit\n"))

    try:
        if get_vid == 1:
            url = input("Please enter the URL of the video: ")
            RedDownloader.Download(url, quality=1080, destination=os.path.join(download_path, 'RedditVideos'), audio=True)
            print("Video downloaded successfully!")
        elif get_vid == 2:
            select_type = int(input("Please select a format:\n[1] Video \n[2] Image \n[3] Random Stuff \n"))
            if select_type == 1:
                subreddit = input("Please enter the subreddit: ")
                get_video_subreddit(subreddit)
            elif select_type == 2:
                subreddit = input("Please enter the subreddit: ")
                get_images_subreddit(subreddit)
            elif select_type == 3:
                subreddit = input("Please enter the subreddit: ")
                get_stuff_subreddit(subreddit)
            else:
                print("Invalid format")
    except ConnectionError:
        print("Connection Error")

if __name__ == "__main__":
    main()