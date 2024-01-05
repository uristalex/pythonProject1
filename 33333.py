from pytube import Playlist, YouTube
from pytube.cli import on_progress
from pathlib import Path
from os.path import join


def get_yt_playlist(playlist=None):
    """
    Get the list of youtube urls. Playlist can be used to download playlist as well,
    but there is no on_progress_callback hence I cannot get the progress bar for each videos.
    :param playlist:
        This is the url of the youtube playlist.
    :return:
        list of playlist urls.
    """
    pl = Playlist(playlist)
    return [l for l in pl]


def download_vid(url=None, path=None):
    """
    This function downloads the video from each playlist url,
    the path is specified with the path keyword.
    :param url:
        youtube url
    :param path:
        path to save the video in your computer
    :return:
        None
    """
    # on_progress is a progress bar in the pytube3 module.
    # the progress bar is shown in sys.stdout.
    yt = YouTube(url, on_progress_callback=on_progress)
    stream = yt.streams.first()
    # video title
    print(stream.title)
    # download and save to the computer path.
    stream.download(path)


if __name__ == "__main__":
    """
    This is an example using a youtube playlist.
    I tried threading, but youtube will reset the connection.
    So for this example is download one video after video finished, 
    which is very slow.
    """
    playlist = "https://www.youtube.com/playlist?list=PLA0M1Bcd0w8wfmtElObQrBbZjY6XeA06U"
    collect_list = get_yt_playlist(playlist)
    path = join(str(Path.home()), "Downloads")
    for pl in collect_list:
        download_vid(url=pl, path=path)