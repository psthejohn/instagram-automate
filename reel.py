from pytube import YouTube, Search

def download_first_video(keyword):
    # Search for videos on YouTube
    search_results = Search(keyword)

    # Get the first video object in the search results
    first_video = search_results.results[0]

    # Print the first video object
    print("First Video Object:")
    print(first_video)

if __name__ == "__main__":
    # Specify the search keyword
    search_keyword = "sky"

    # Get the first video related to the search keyword
    download_first_video(search_keyword)
