# main.py
# Author: zymzs
# Date: 2019/4/30 21:23

def listSentence(inputSentence):
    global endSign
    global endWord
    inputSentence = str(inputSentence)
    if inputSentence.isalpha() == True:
        pass
    else:
        endWord = inputSentence[-1]
        print(endWord)
        if endWord == "." or endWord == "," or endWord == "!" or endWord == "?":    # or 语句两边是不同的判断情境
            endSign = endWord   # 如果是标点，将标点储存到endSign内
            inputSentence = inputSentence.replace(endSign, "")    # 去除标点
    sentenceList = inputSentence.split(" ")
    return sentenceList

def upsetList(sentenceList):
    import random
    random.shuffle(sentenceList)
    return sentenceList

def outputList(list):
    sentenceOutput = ""
    for i in sentenceList:
        sentenceOutput = sentenceOutput + i + " "
    return sentenceOutput

sentence = input("请输入一段文字：")
sentenceList = listSentence(sentence)
sentenceList = upsetList(sentenceList)
sentenceOutput = outputList(sentenceList)
print(sentenceOutput)