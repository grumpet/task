# funtions for Pink Floyd database
import tkinter as tk
from tkinter import simpledialog 

def get_albums():
    list = []
    with open('Pink_Floyd_DB.txt', 'r') as file:
        for line in file:
            if line.startswith('#'):
                line = line.strip("#")
                line = line.strip("::")
                list.append(line.split("::")[0])
    output_label.config(text="\n".join(list))
    return list
     
def get_songs_from_album():
    album = simpledialog.askstring("Input", "Enter album name")
    album = album.lower()
    albums_list = [album.lower() for album in get_albums()]
    songs_list = []
    if album not in albums_list:
        return output_label.config(text="Album not found")
    else:
        with open('Pink_Floyd_DB.txt', 'r') as file:
            processing_songs = False
            for line in file:
                if line.startswith('#'):
                    line = line.strip("#")
                    line = line.strip("::")
                    line = line.split("::")
                    line_album = line[0].lower()
                    if line_album == album:
                        processing_songs = True
                    else:
                        processing_songs = False
                elif processing_songs and line.startswith('*'):
                    line = line.strip('*')
                    line = line.split('::')
                    songs_list.append(line[0])
    if len(songs_list) == 0:
        output_label.config(text="No songs found")
        return "No songs found"
    else:
        output_label.config(text="\n".join(songs_list))
    return songs_list


def get_song_length():
    song = simpledialog.askstring("Input", "Enter song name")
    song = song.lower()
    with open('Pink_Floyd_DB.txt', 'r') as file:
        for line in file:
            if line.startswith('*'):
                line = line.strip('*')
                line = line.split('::')
                if song in line[0].lower():
                    output_label.config(text=line[2])
                    return line[2]
    output_label.config(text="Song not found")
    return "Song not found"

def get_song_lyrics():
    song = simpledialog.askstring("Input", "Enter song name")
    with open('Pink_Floyd_DB.txt', 'r') as file:
        processing_lyrics = False
        lyrics = ""
        for line in file:
            if line.startswith('*'):
                line = line.strip('*')
                line = line.split('::')
                if song.lower() in line[0].lower():
                    processing_lyrics = True
                else:
                    processing_lyrics = False
            elif processing_lyrics:
                lyrics+=line
        if lyrics == "":
            output_label.config(text="Song not found")
            return "Song not found"
        else:
            output_label.config(text=lyrics)
            return lyrics

def what_album_is_song_on():
    song = simpledialog.askstring("Input", "Enter song name")
    with open('Pink_Floyd_DB.txt', 'r') as file:
        for line in file:
            if line.startswith('#'):
                line = line.strip("#")
                line = line.split("::")
                album = line[0]
            elif line.startswith('*'):
                line = line.strip('*')
                line = line.split('::')
                if song in line[0]:
                    output_label.config(text=album)
                    return album
                
    output_label.config(text="album not found")
    return "album not found"

def get_song_by_word():
    word = simpledialog.askstring("Input", "Enter word")
    word = word.lower()
    with open('Pink_Floyd_DB.txt', 'r') as file:
        songs_list = []
        for line in file:
            if line.startswith('*'):
                line = line.lower()
                line = line.strip('*')
                line = line.split('::')
                if word in line[0]:
                    songs_list.append(line[0])
        if len(songs_list) == 0:
            output_label.config(text="No songs found")
            return "No songs found"
        else:
            output_label.config(text="\n".join(songs_list))
            return songs_list


def get_song_name_by_word_in_lyrics():
    word = simpledialog.askstring("Input", "Enter word")
    word = word.lower()
    with open('Pink_Floyd_DB.txt', 'r') as file:
        songs_list = []
        for line in file:
            if line.startswith('*'):
                line = line.strip('*')
                line = line.split('::')
                song_name = line[0]
            if '*' not in line and '#' not in line:
                if word in line and song_name not in songs_list:
                    songs_list.append(song_name)
    if len(songs_list) == 0:
        output_label.config(text="No songs found")
        return "No songs found"
    else:
        output_label.config(text="\n".join(songs_list))
        return songs_list

# GUI

root = tk.Tk()
button1 = tk.Button(root, text="Get Albums", command=get_albums)
button2 = tk.Button(root, text="Get Songs from Album", command=get_songs_from_album)
button3 = tk.Button(root, text="Get Song Length", command=get_song_length)
button4 = tk.Button(root, text="Get Song Lyrics", command=get_song_lyrics)
button5 = tk.Button(root, text="What album is song on", command=what_album_is_song_on)
button6 = tk.Button(root, text="Get Song by Word", command=get_song_by_word)
button7 = tk.Button(root, text="Get Song Name by Word in Lyrics", command=get_song_name_by_word_in_lyrics)


output_label = tk.Label(root, text="", bg="yellow", fg="black")


button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()

output_label.pack()
root.mainloop()