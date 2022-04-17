# -*- coding: UTF-8 -*-
# Author: Eureka <manchen_0528@outlook.com>


import os
import scriptHandler
import globalPluginHandler
import globalCommands
import globalVars
import speechDictHandler
import ui

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
		description=_("开关盲文到语音转译"), 
gesture=_("kb:NVDA+O"))
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
