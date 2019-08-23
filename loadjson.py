#this program will print out all of teh text data from our
#twitter JSON file

import json

#open the json file
tweetFile = open("./p.json", "r")

#get data from the opened file
tweetData = json.load(tweetFile)

#close the file because we already have the data stored
tweetFile.close()

print("Tweet id: ", tweetData[0]["id"])

print("Tweet text: ", tweetData[0]["text"])
     print("Tweet id ")
