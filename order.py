# order.py
# Author: zymzs
# Date: 2019/4/30 21:23

def order(sentence):
    def listSentence(inputSentence):
        global endSign
        inputSentence = str(inputSentence)
        test = inputSentence.replace(" ", '')
        if test.isalpha() == True:
            endSign = '.'
        else:
            endWord = inputSentence[-1]
            if endWord in [".", ",", "!", "?"] :
                endSign = endWord   # 如果是标点，将标点储存到endSign内
                inputSentence = inputSentence.replace(endSign, "")    # 去除标点
        sentenceList = inputSentence.split(" ")     # 转换为列表形式
        return sentenceList

    def upsetList(sentenceList):
        import random
        random.shuffle(sentenceList)
        return sentenceList

    def outputList(list):
        sentenceOutput = ""
        for i in sentenceList:
            sentenceOutput = sentenceOutput + i + " "
        sentenceOutput = sentenceOutput.strip(" ")
        return sentenceOutput

    # sentence = input("请输入一段文字：")
    sentence = listSentence(sentence)
    sentenceList = upsetList(sentence)
    sentenceOutput = outputList(sentenceList)
    return sentenceOutput, endSign
