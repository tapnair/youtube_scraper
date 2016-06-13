__author__ = 'patrick'

import requests
import json

filename = 'videoNames.txt'
outputFile = open('outputFile.csv', 'w')

lines = [line.rstrip('\n') for line in open(filename)]

total = 0

totalLikes = 0

for line in lines:

    url = 'https://www.googleapis.com/youtube/v3/videos?part=statistics&id=' + line + '&key=AIzaSyDpSHCo3KsVg-FYOTBLABAXbwxHpuUntv4'
    r = requests.get(url)

    data = r.json()

    # print r.text



    count = data['items'][0]["statistics"]["viewCount"]

    likes = data['items'][0]["statistics"]["likeCount"]

    total += int(count)
    totalLikes += int(likes)

    print (line + ',' + str(count) + ',' + str(likes))


    outputFile.write(line + ',' + str(count) + ',' + str(likes) + '\n')

#
# print("Total Views = " + str(total))
#
# print("Total Likes = " + str(totalLikes))



