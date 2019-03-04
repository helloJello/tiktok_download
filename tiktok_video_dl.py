#open the file sent
file = open('DownloadLink2.txt')
import urllib.request

#initialize counter
i = 0

#parse the download file
lines = file.readlines()

#loop and download
for each_line in lines:
    urllib.request.urlretrieve(each_line, "video_{i}.mp4".format(**locals()))
    i += 1