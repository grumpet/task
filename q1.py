
from pprint import pprint

def get_albums():
    list = []
    with open('Pink_Floyd_DB.txt', 'r') as file:
        for line in file:
            if line.startswith('#'):
                line = line.strip("#")
                line = line.strip("::")
                list.append(line.split("::")[0])
    return list
     
def get_songs_from_album(album):
    albums_list = get_albums()
    songs_list = []
    if album not in albums_list:
        return "Album not found"
    else:
        with open('Pink_Floyd_DB.txt', 'r') as file:
            processing_songs = False
            for line in file:
                if line.startswith('#'):
                    line = line.strip("#")
                    line = line.strip("::")
                    if album in line:
                        processing_songs = True
                    else:
                        processing_songs = False
                elif processing_songs and line.startswith('*'):
                    line = line.strip('*')
                    line = line.split('::')
                    songs_list.append(line[0])
    return songs_list


def get_song_length(song):
    with open('Pink_Floyd_DB.txt', 'r') as file:
        for line in file:
            if line.startswith('*'):
                line = line.strip('*')
                line = line.split('::')
                if song in line[0]:
                    return line[2]
    return "Song not found"

def get_song_lyrics(song):
    with open('Pink_Floyd_DB.txt', 'r') as file:
        processing_lyrics = False
        lyrics = ""
        for line in file:
            if line.startswith('*'):
                line = line.strip('*')
                line = line.split('::')
                if song in line[0]:
                    processing_lyrics = True
                else:
                    processing_lyrics = False
            elif processing_lyrics:
                lyrics+=line
        return lyrics

def what_album_is_song_on(song):
    with open('Pink_Floyd_DB.txt', 'r') as file:
        album = "album not found"
        for line in file:
            if line.startswith('#'):
                line = line.strip("#")
                line = line.split("::")
                album = line[0]
            elif line.startswith('*'):
                line = line.strip('*')
                line = line.split('::')
                if song in line[0]:
                    return album
    return album

print(what_album_is_song_on("Lucir Sam"))