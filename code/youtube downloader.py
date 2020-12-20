from pytube import YouTube, Playlist
# from pytube import Playlist
from bs4 import BeautifulSoup
import os
import subprocess
import re
import webbrowser
import drawlogo
os.system('cls')
# video


def resolution(s):
    F2 = str(s).split("res=")[1]
    F3 = str(F2).split(" fps=")[0]
    return F3


def frame(s):
    F2 = str(s).split("fps=")[1]
    F3 = str(F2).split(" vcodec=")[0]
    return F3


def midia(s):
    F2 = str(s).split("mime_type=")[1]
    F3 = str(F2).split(" res=")[0]
    return F3


# audio
def Audio_resolution(s):
    F2 = str(s).split("abr=")[1]
    F3 = str(F2).split(" acodec=")[0]
    return F3


def Audio_midia(s):
    F2 = str(s).split("mime_type=")[1]
    F3 = str(F2).split(" abr=")[0]
    return F3

# choice


def itagfuck(s):
    F2 = str(s).split("itag=")[1]
    F3 = str(F2).split(" mime_type=")[0]
    return F3


def subtitle(s):
    F2 = str(s).split(" code=")[1]
    F3 = str(F2).split(">")[0]
    return F3


def fucking_title():
    title = re.sub('[=+,#/\?:^$.@*\"※~&%ㆍ!』\‘|\》]', '', yt.title)
    return title


def fucking_title_out():
    title = re.sub(' ', '_', yt.title)
    return title


print(drawlogo.drawlogo())
inputvalue = input('press any key to continue')  # developing
if inputvalue == inputvalue:  # developing
    url = input("past the url:")
    os.system('cls')
    print(drawlogo.drawlogo())
    yt = YouTube(url)
    print('thumbnail_link          ' + yt.thumbnail_url)
    print("")
    print("Is the video name  <%s> ?" % yt.title)
    # webbrowser.open(yt.thumbnail_url) #optional for the thumbnail on the browser
    input("press any key to countinue")
    os.system('cls')
    print(drawlogo.drawlogo())
    stream = yt.streams.all()
    # print(stream)
    n = 0
    num = 0

    for i in range(len(str(stream).split(","))):
        n += 1
        if "audio" in str(stream).split(",")[i]:
            num = n
            break

    for i in range(num-1):
        fuck = str(stream).split(",")[int(i)]
        print("────────────────────────────────────────────────────────────────────────")
        print(str(i) + "  ───resolution:" + resolution(fuck) +
              ",  frame rate: " + frame(fuck) + ",  type " + midia(fuck))
    num2 = num
    for i in range(len(str(stream).split(",")) - num):
        # print(num)

        fuck = str(stream).split(",")[int(num)]
        print("────────────────────────────────────────────────────────────────────────")
        print(str(num) + "  ───resolution:" +
              str(Audio_resolution(fuck)) + ",  type " + str(Audio_midia(fuck)))
        if int(Audio_resolution(fuck)[1:-5]) >= 160:
            BA = num
        num += 1
    print('\n\n\n')
    choice = input("type the format  :")
    adress = input("past DIR to download  :")

    os.system('cls')
    print(drawlogo.drawlogo())

    if adress == "":
        adress = os.getcwd()
    if int(choice) < num2:
        # video
        target = str(stream).split(",")[int(choice)]
        itag = itagfuck(target)
        itag = itag[1:-1]
        stream = yt.streams.get_by_itag(itag)
        if "video/mp4" in Audio_midia(target)[1:-1]:
            video_format = ".mp4"
        else:
            video_format = ".webm"
        print('downloading.......................')
        stream.download(adress)

        os.rename(adress + '/' + fucking_title() + video_format, adress + '/' + "video" + video_format)
        # audio
        stream = yt.streams.all()
        target = str(stream).split(",")[BA]
        itag = itagfuck(target)
        itag = itag[1:-1]
        stream = yt.streams.get_by_itag(itag)
        if "audio/webm" in Audio_midia(target)[1:-1]:
            audio_format = ".webm"
        else:
            audio_format = ".mp3"
        stream.download(adress)

        print('download done')
        os.rename(adress + '/' + fucking_title() + audio_format,
                  adress + '/' + "audio" + audio_format)
        # mixing
        os.system('ffmpeg -i '+adress + '/'+'video'+video_format+' -i '+adress + '/'+'audio'+audio_format+' -c copy ' +adress + '/'+
                  fucking_title_out()+'.mp4')                                    # "Muxing Done
        print('Muxing Done')
        os.remove(adress + '/' + 'video'+video_format)
        os.remove(adress + '/' + 'audio'+audio_format)
        print("done")
        input()
    else:
        stream = yt.streams.all()
        target = str(stream).split(",")[BA]
        itag = itagfuck(target)
        itag = itag[1:-1]
        stream = yt.streams.get_by_itag(itag)
        stream.download(adress)
        os.rename(adress + '/' + fucking_title() + '.webm',
                  adress + '/' + fucking_title_out() + '.mp3')
        print('done')
    input()

# elif inputvalue=='2':
#     playlist_url = input("past playlist url : ")
#     p = Playlist(playlist_url)
#     for url in p.video_urls[:3]:
#         print(url)
#     input('press any key to download')
#     p = Playlist(playlist_url)
#     print(f'Downloading: {p.title}')
#     for video in p.videos:
#         video.streams.first().download()

    answer = input("want subtitle? [N/Y]")
    if answer == "Y" or answer == "y":
        os.system('cls')
        print(drawlogo.drawlogo())
        for i in range(len(yt.captions.all())):
            print(subtitle(yt.captions.all()[i]))
        code = input("write the Language code : ")
        if code == '':
            print('none selected')
            input()
        else:
            caption = yt.captions.get_by_language_code(code)
            sub_name = yt.title+'_'+code
            file1 = open( adress + '/' + '%s.srt' % sub_name, "a")
            # print(caption.generate_srt_captions())
            file1.write(caption.generate_srt_captions())
            print("done")
            input()

    os.system('cls')
   