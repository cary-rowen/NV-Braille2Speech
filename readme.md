

## 软件介绍

本软件结合电子化盲文与人工智能技术，实现了电子盲文系统，系统中包括盲文输入法、文本转义、语音转义以及汉字转译成盲文等模块，目的是为解放视障者的双耳，提供一个在无干扰状态下输入盲文，并可在盲文、语音、汉字之间自由转换的，保证可写可读的应用软件。

## 软件安装

视障者主要使用键盘，借助屏幕阅读器——Screen Reader（可以将屏幕上的文字信息转化为语音的软件）来操作计算机。所以本系统作为 NVDA 屏幕阅读器扩展插件的形式在 GPL2.0 开原协议下分发，保证了与屏幕阅读器的良好兼容。
NVDA(NonVisual Desktop Access) 由澳大利亚的非盈利性组织 NV Access 发起，是一款完全开源且免费的屏幕阅读器，已被翻译成包括中文在内的 55 种语言，成为了多达 175 个国家视障用户使用个人电脑不可或缺的基础设施。

如需安装并使用本软件，可遵循以下步骤进行安装部署：
1. 从官方网站下载并安装 NVDA 屏幕阅读器： https://www.nvaccess.org/
2. 从 Github Release 页面下载本软件： https://github.com/cary-rowen/NV-Braille2Speech/releases
3. 下载后您将得到一个 .nvda-addon 的文件，此为本软件的安装包，点击后 NVDA 会询问您是否确认安装本软件，只需点击“是”按钮，即可完成本软件的安装部署。

## 输入盲文

1. 按 NVDA键 + 数字 0 这组快捷键开启盲文输入。此快捷键可以从 NVDA 设置中的“按键与手势”对话框的盲文类别下更改。
2. 通过在 PC 键盘上同时按下一组按键来输入盲文，就如同在实体盲文键盘上输入一样。
	* 如用双手输入文本，请使用 QWERTY 键盘布局的以下按键，或其他键盘布局相应位置的按键：
		* f、d 和 s分别代表 1、2 和 3 点。
		* j、k 和 l分别代表 4、5 和 6 点。
		* 使用 a 和分号（;）分别代表 7 和 8 点。
		* 您也可用上一行中的相应按键，即 q、w、e、r、u、i、o 和 p。
	* 如用单手输入，则可以同时或依次按下相应的键来输入盲文，输入完一个盲文单元后，请按 g 或 h 键以确认输入。如果在输入过程中出错，可以在确认输入之前，按t或y清除点位。
	  QWERTY 键盘布局中使用的按键如下：
		* 左手： f、 d、 s、 r、 e、 w、 a、 q 分别代表 1、 2、 3、 4、 5、 6、 7 、 8 点。
		* 右手： j、 k、 l、 u、 i、 o、 分号（;）、 p 分别代表 1、 2、 3、 4、 5、 6、 7、 8 点。
3. 您可以照常使用大多数其他按键，包括空格键、退格键、回车键和其他功能键。请注意不要按下 alt + shift，因为更改键盘布局可能会影响输入的点位。
4. 按下空格键加盲文点的组合即可移动系统光标（或读出当前行），就像您使用点显器一样。例如，空格 + 1 点模拟上光标，空格 + 4、 5、 6   点模拟Ctrl + end，空格 + 1、 4 点读出当前行，等等。
5. 按 NVDA + 0 关闭盲文输入。


## 读出盲文

如需将输入的盲文转换为语音，用户只需按下 NVDA + O 这组按键即可开启或关闭语音转译模式。
在语音转译模式下，本系统能够对用户输入的 Unicode 盲文进行时时转译，例如：

（1） 若用户输入： “⠌⠲⠛⠕⠂” 在开启语音模式的情况下会直接以  TTS 朗读为“中国”。
（2） 若用户输入： “⠌⠲⠛⠕⠂” 在关闭语音模式的情况下会朗读实际盲文点位，即：“3-4点；2-5-6点；1-2-4-5点；1-3-5点；2点，”

## 翻译盲文成汉字

如需将输入的盲文转换为汉字，用户只需按下 NVDA + X 这组按键即可将已输入的 Unicode 盲文转换为汉字。

对于转换后的结果，可以选择使用语音直接读出，或者复制到剪贴板便于粘贴。

比如： 若用户输入： “⠌⠲⠛⠕⠂” 后按下 NVDA + X 会听到 TTS 朗读“中国”，同时将“中国”这两个字复制到 Windows 系统剪贴板。
