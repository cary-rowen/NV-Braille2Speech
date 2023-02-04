import json
from .Pinyin2Hanzi import DefaultHmmParams
from .Pinyin2Hanzi import viterbi
from .Pinyin2Hanzi import simplify_pinyin
from os.path import join, dirname


def loadDict(dictFile):
	with open(join(dirname(__file__), dictFile),'r', encoding='UTF-8') as f:
		dict = json.load(f)
	return dict

PinInDict = loadDict("brailleToPinIn.json")
TextDict = loadDict("pinInToText.json")
SingleWord = loadDict("singleWord.json")

def brailleToText(braille):
	conflictVowels=["⠸","⠩","⠣","⠜","⠑","⠡","⠭","⠹","⠊","⠬","⠾","⠫","⠳"]
	conflictInitials=["⠛","⠓","⠅"]
	pinIn=list()
	temp=""
	for i in range(0,len(braille)):
		if braille[i] in conflictInitials and braille[i+1] in conflictVowels:
			if braille[i]=="⠛": temp="J"
			elif braille[i]=="⠓": temp="X"
			else: temp="Q"
		else:
			temp=PinInDict.get(braille[i])
		pinIn.append(temp)
	pinInList=list()
	print("pinIn",pinIn)
	word=""
	for j in range(0,len(pinIn)):
		if pinIn[j] is None:
			pinInList.append(word)
			word=""
		elif type(pinIn[j]) ==int:
			word=word +str(pinIn[j])
			pinInList.append(word)
			word=""
		elif pinIn[j].isalpha():
			if word.isupper() and pinIn[j].islower():
				word=word +pinIn[j]
				if j==len(pinIn)-1:
					pinInList.append(word)
			else:
				if word!="":
					pinInList.append(word)
				try:
					if len(pinIn) <=1 or j==len(pinIn)-1:
						word=SingleWord.get(pinIn[j])
						pinInList.append(word)
						word=""
					elif pinIn[j+1] is None or type(pinIn[j+1])==int:
						word=SingleWord.get(pinIn[j])
						pinInList.append(word)
						word=""
					elif pinIn[j-1] is None or j==0:
						if pinIn[j+1].islower():
							word=pinIn[j]
						else:
							word=SingleWord.get(pinIn[j])
							pinInList.append(word)
							word=""
					else:
						word=pinIn[j]
				except IndexError:
					word=pinIn[j]
					print("此处有误")
				if j==len(pinIn)-1:
					pinInList.append(word)
		else:
			pinInList.append(pinIn[j])
	print("pinInList",pinInList)
	if len(pinInList)>1:
		hmmparams = DefaultHmmParams()
		pl=[]
		for p in pinInList:
			if p=="" or p in "1234": continue	
			if p[0] in "JQX" and "vn" in p:
				pl.append(p[0].lower()+"un")
				continue
			if p[-1] in "1234":
				pl.append(simplify_pinyin(p[0:-1].lower()))
			else:
				pl.append(simplify_pinyin(p.lower()))
		print("pl",pl)
		result = viterbi(hmm_params=hmmparams, observations=pl, path_num = 1)
		for i in result:
			resultText="".join(i.path)
	else:
		resultText=""
		for k in range(0,len(pinInList)):
			temp=TextDict.get(pinInList[k].lower()) if pinInList[k] !=None else None
			if temp is not None: resultText=resultText+str(temp)
	return resultText

