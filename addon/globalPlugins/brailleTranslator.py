import globalPluginHandler
from scriptHandler import script
import ui
import api
from .Pinyin2Hanzi import DefaultHmmParams
from .Pinyin2Hanzi import viterbi
from . import brailleToPinInToText
from .Pinyin2Hanzi import simplify_pinyin as s 

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
			temp=brailleToPinInToText.GlobalPlugin.getPinInDict().get(braille[i])
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
						word=brailleToPinInToText.GlobalPlugin.getSingleWord().get(pinIn[j])
						pinInList.append(word)
						word=""
					elif pinIn[j+1] is None or type(pinIn[j+1])==int:
						word=brailleToPinInToText.GlobalPlugin.getSingleWord().get(pinIn[j])
						pinInList.append(word)
						word=""
					elif pinIn[j-1] is None or j==0:
						if pinIn[j+1].islower():
							word=pinIn[j]
						else:
							word=brailleToPinInToText.GlobalPlugin.getSingleWord().get(pinIn[j])
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
				pl.append(s(p[0:-1].lower()))
			else:
				pl.append(s(p.lower()))
		print("pl",pl)
		result = viterbi(hmm_params=hmmparams, observations=pl, path_num = 1)
		for i in result:
			resultText="".join(i.path)
	else:
		pinInToTextDict=brailleToPinInToText.GlobalPlugin.getTextDict()
		resultText=""
		for k in range(0,len(pinInList)):
			temp=pinInToTextDict.get(pinInList[k].lower()) if pinInList[k] !=None else None
			if temp is not None: resultText=resultText+str(temp)
		print("result:",resultText)
	api.copyToClip(resultText)


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	@script(
		description=_("Announces the window class name of the current focus object"),
		gesture="kb:NVDA+x"
	)
	def script_announceWindowClassName(self, gesture):
		focusObj = api.getFocusObject()
		value = focusObj.value
		ui.message("hello")
		brailleToText(value)