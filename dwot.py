'''
    输入一个句子，通过dwot()函数将句子转换为list.
    使用方法：dwot(你要转换的句子)
    自动去除标点，标点保存在endSign内
'''
def dwot(sentence):
    sentence = str(sentence)
    if sentence.isalpha() == True:
        pass
    else:
        endWord = sentence[-1]
        print(endWord)
        if endWord == "." or endWord == "," or endWord == "!" or endWord == "?":    # or 语句两边是不同的判断情境
            endSign = endWord   # 如果是标点，将标点储存到endSign内
            sentence = sentence.replace(endSign, "")    # 去除标点
    sentenceList = sentence.split(" ")
    global endSign
    global endWord
    return sentenceList
