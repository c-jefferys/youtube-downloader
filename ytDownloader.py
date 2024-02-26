from pytube import YouTube
from sys import argv, exit
from os import path

link = argv[1]  # link is entered when program is executed in terminal
yt = YouTube(link)  # object for video info and available streams

print('Title: ' + yt.title)
print(f'Creator: {yt.author}')
print(f'Length: {round(yt.length/60)} minutes')

check = input('Correct Video? ').lower()

if check != 'yes': exit()  # exit program if video result was unexpected

video_type = input('video or audio? ').lower()  # video = video & audio, no = only audio

# gets the proper download type
if video_type == 'video':
    print('Downloading...')
    stream = yt.streams.get_highest_resolution()  # gets highest available video quality
elif video_type == 'audio':
    print('Downloading...')
    stream = yt.streams.get_audio_only()
else:
    print('Invalid download type!')
    exit()  # invalid input for video type

stream.download(path.expanduser('~/Downloads'))
print('Downloaded!')
