import sys
from pytube import YouTube
from sys import argv # for taking command line arguements
from threading import Thread as td

# link_offset = argv[0]# takes the name of the file as the first arguement so we take the second one instead
# def progress_function(self,stream, chunk,file_handle, bytes_remaining):

# #     size = stream.filesize
# #     p = 0
# #     while p <= 100:
# #         progress = p
# #         print (str(p)+'%')
# #         p = percent(bytes_remaining, size)
        
# # def percent(self, tem, total):
# #         perc = (float(tem) / float(total)) * float(100)
# #         return perc
#     global filesize
#     current = ((filesize - bytes_remaining)/filesize)
#     percent = ('{0:.1f}').format(current*100)
#     progress = int(50*current)
#     status = '█' * progress + '-' * (50 - progress)
#     sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
#     sys.stdout.flush()
        

link = argv[1]# takes the link from the command line
yt_ = YouTube(link)#creates a YouTube object make use_oauth = True if you want to download any vids

print("Title: ",yt_.title)#prints the title of the video
print("Views: ",yt_.views)#prints the number of views
# td1 = td(target=Youtube_download)
    # td1.start()
def download():
    """function download is the download logic for the object yt_ 
    you send the link here in this code block 
    no return type
    """
    try :
        Youtube_download = yt_.streams.get_highest_resolution()#gets the highest resolution stream
        Youtube_download.download('./download_output')#downloads the video to the specified folder
        
    except Exception:
        print("something went wrong")
        
    else:
        print(f"Downloaded the file {yt_.title}") #this block runs if no except block runs

    finally:
        pass
    

def main():
    download()
    

main()

if __name__ == "__main__":
    print(download.__doc__)
