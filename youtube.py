from pytube import YouTube, Playlist
from pytube.cli import on_progress


def Download_vid(link):
    if 'list' in link:
        pl = Playlist(link)
        for video in pl.videos:
            print(f'Start Download playlist {pl.title} \n {video.title}')
            video.streams.get_highest_resolution().download(
                f'D:/Video_youtube/Python/{pl.owner}/{pl.title}_{pl.length}vid/')
            print('dan')
    else:
        yt1 = YouTube(link)
        yt = yt1.streams.get_highest_resolution()
        file_size = yt.filesize_approx
        try:
            print(f'Start Download video: \n {yt1.title}')
            output_path = f'D:/Video_youtube/Python/{yt1.author}/'
            yt.download(output_path)
        except:
            print("An error has occurred")


    print("Download is completed successfully")
    # print(float((yt1.length)/60))
    print(f'{file_size}')


link = 'https://www.youtube.com/watch?v=1SWGdyVwN3E'


Download_vid(link)

