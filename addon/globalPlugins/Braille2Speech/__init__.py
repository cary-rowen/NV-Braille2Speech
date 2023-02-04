# -*- coding: UTF-8 -*-
# Author: Eureka <manchen_0528@outlook.com>


import os
import scriptHandler
import globalPluginHandler
import globalCommands
import globalVars
import speechDictHandler
import ui
import api
from . import brailleTranslator

dictFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "brailleDic.dic")
speechDict = speechDictHandler.SpeechDict()
transBRL = False

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = globalCommands.SCRCAT_BRAILLE

	def __init__(self):
		super().__init__()
		global speechDict, dictFile
		speechDict.load(dictFile)

	def terminate(self):
		transOff()
		global speechDict
		speechDict = None


	@scriptHandler.script(
	description=_("盲文转汉字"),
	gesture="kb:NVDA+Alt+T"
	)
	def script_TransBraille(self, gesture):
		from controlTypes.role import Role
		focusObj = api.getFocusObject()
		if focusObj.role != Role.EDITABLETEXT: return
		try:
			value = focusObj.value
		except:
			pass
		else:
			if value:
				result = brailleTranslator.brailleToText(value)
				if scriptHandler.getLastScriptRepeatCount() > 0:
					api.copyToClip(result, notify=True)
				else:
					ui.message(result)
			else: ui.message("没有可转换的 Unicode 盲文")

	@scriptHandler.script(
		description=_("开关盲文到语音转译"), 
gesture=_("kb:NVDA+Alt+V"))
	def script_toggle(self, gesture):
		if not globalVars.speechDictionaryProcessing:
			return
		if transBRL:
			transOff()
			ui.message(_("off"))
		else:
			transOn()
			ui.message(_("on"))

def transOn():
	global transBRL
	speechDictHandler.dictionaries["temp"].extend(speechDict)
	transBRL = True

def transOff():
	global transBRL
	for entry in speechDict:
		if entry in speechDictHandler.dictionaries["temp"]:
			speechDictHandler.dictionaries["temp"].remove(entry)
	transBRL = False
