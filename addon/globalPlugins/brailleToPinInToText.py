import globalPluginHandler

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def getPinInDict():
		brailleToPinIn={"⠁":1,
		"⠂":2,
		"⠄":3,
		"⠆":4,
		"⠃":"B",
		"⠏":"P",
		"⠍":"M",
		"⠋":"F",
		"⠙":"D",
		"⠞":"T",
		"⠝":"N",
		"⠇":"L",
		"⠛":"G",
		"⠅":"K",
		"⠓":"H",
		"⠌":"ZH",
		"⠟":"CH",
		"⠱":"SH",
		"⠚":"R",
		"⠵":"Z",
		"⠉":"C",
		"⠎":"S",
		"⠳":"iu",
		"⠫":"ia",
		"⠿":"ua",
		"⠢":"e",
		"⠗":"er",
		"⠻":"uan",
		"⠾":"ue",
		"⠬":"u",
		"⠥":"u",
		"⠊":"i",
		"⠕":"uo",
		"⠒":"un",
		"⠔":"a",
		"⠹":"iong",
		"⠲":"ong",
		"⠭":"iang",
		"⠶":"uang",
		"⠴":"en",
		"⠼":"eng",
		"⠦":"ang",
		"⠧":"an",
		"⠖":"ao",
		"⠪":"ai",
		"⠡":"ing",
		"⠮":"ei",
		"⠑":"ie",
		"⠜":"iao",
		"⠺":"ui",
		"⠷":"ou",
		"⠣":"in",
		"⠩":"ian",
		"⠸":"vn",
		"⠽":"uai",
		
		}
		return brailleToPinIn
	
	def getTextDict():
		pinInToText={
		"a":"啊",
		"a1":"阿",
		"a2":"嗄",
		"ai":"嗌",
		"ai1":"埃",
		"ai2":"皑",
		"ai3":"蔼",
		"ai4":"嗌",
		"an":"按",
		"an1":"鞍",
		"an3":"俺",
		"an4":"按",
		"ang":"昂",
		"ang1":"肮",
		"ang2":"昂",
		"ang4":"盎",
		"ao":"傲",
		"ao1":"凹",
		"ao2":"敖",
		"ao3":"拗",
		"ao4":"傲",
		"ba":"把",
		"ba1":"扒",
		"ba2":"拔",
		"ba3":"钯",
		"ba4":"耙",
		"bai":"柏",
		"bai1":"掰",
		"bai2":"白",
		"bai3":"柏",
		"bai4":"败",
		"ban":"扮",
		"ban1":"斑",
		"ban3":"板",
		"ban4":"扮",
		"bang":"邦",
		"bang1":"邦",
		"bang3":"膀",
		"bang4":"磅",
		"bao":"苞",
		"bao1":"苞",
		"bao2":"薄",
		"bao3":"堡",
		"bao4":"暴",
		"bei":"北",
		"bei1":"陂",
		"bei3":"北",
		"bei4":"孛",
		"ben":"苯",
		"ben1":"贲",
		"ben3":"苯",
		"ben4":"笨",
		"beng":"揼",
		"beng1":"崩",
		"beng2":"甭",
		"beng3":"琫",
		"beng4":"泵",
		"bi":"臂",
		"bi1":"逼",
		"bi2":"鼻",
		"bi3":"比",
		"bi4":"臂",
		"bian":"便",
		"bian1":"鞭",
		"bian3":"贬",
		"bian4":"便",
		"biao":"表",
		"biao1":"骠",
		"biao3":"表",
		"biao4":"鳔",
		"bie":"别",
		"bie1":"鳖",
		"bie2":"别",
		"bie3":"瘪",
		"bie4":"彆",
		"bin":"玢",
		"bin1":"玢",
		"bin4":"摈",
		"bing":"病",
		"bing1":"兵",
		"bing3":"柄",
		"bing4":"病",
		"bo":"拨",
		"bo1":"剥",
		"bo2":"伯",
		"bo3":"簸",
		"bo4":"檗",
		"bu":"埠",
		"bu1":"逋",
		"bu2":"醭",
		"bu3":"捕",
		"bu4":"埠",
		"ca":"嚓",
		"ca1":"嚓",
		"ca3":"礤",
		"cai":"菜",
		"cai1":"猜",
		"cai2":"裁",
		"cai3":"睬",
		"cai4":"菜",
		"can":"参",
		"can1":"参",
		"can2":"蚕",
		"can3":"惨",
		"can4":"灿",
		"cang":"藏",
		"cang1":"伧",
		"cang2":"藏",
		"cao":"操",
		"cao1":"操",
		"cao2":"槽",
		"cao3":"草",
		"cao4":"肏",
		"ce":"厕",
		"ce4":"厕",
		"cen":"岑",
		"cen1":"嵾",
		"cen2":"岑",
		"ceng":"曾",
		"ceng1":"噌",
		"ceng2":"曾",
		"ceng4":"蹭",
		"cha":"插",
		"cha1":"插",
		"cha2":"查",
		"cha3":"镲",
		"cha4":"差",
		"chai":"拆",
		"chai1":"拆",
		"chai2":"柴",
		"chai4":"瘥",
		"chan":"铲",
		"chan1":"搀",
		"chan2":"禅",
		"chan3":"铲",
		"chan4":"颤",
		"chang":"尝",
		"chang1":"昌",
		"chang2":"尝",
		"chang3":"场",
		"chang4":"畅",
		"chao":"吵",
		"chao1":"焯",
		"chao2":"朝",
		"chao3":"吵",
		"chao4":"耖",
		"che":"车",
		"che1":"车",
		"che3":"扯",
		"che4":"撤",
		"chen":"臣",
		"chen1":"郴",
		"chen2":"臣",
		"chen3":"碜",
		"chen4":"趁",
		"cheng":"澄",
		"cheng1":"称",
		"cheng2":"澄",
		"cheng3":"逞",
		"cheng4":"秤",
		"chi":"持",
		"chi1":"吃",
		"chi2":"持",
		"chi3":"尺",
		"chi4":"赤",
		"chong":"充",
		"chong1":"充",
		"chong2":"虫",
		"chong3":"宠",
		"chong4":"铳",
		"chou":"臭",
		"chou1":"抽",
		"chou2":"仇",
		"chou3":"瞅",
		"chou4":"臭",
		"chu":"处",
		"chu1":"初",
		"chu2":"橱",
		"chu3":"褚",
		"chu4":"处",
		"chua1":"欻",
		"chuai":"啜",
		"chuai1":"揣",
		"chuai4":"啜",
		"chuan":"串",
		"chuan1":"川",
		"chuan2":"传",
		"chuan3":"喘",
		"chuan4":"串",
		"chuang":"创",
		"chuang1":"疮",
		"chuang2":"幢",
		"chuang3":"闯",
		"chuang4":"创",
		"chui":"吹",
		"chui1":"吹",
		"chui2":"椎",
		"chun":"春",
		"chun1":"春",
		"chun2":"醇",
		"chun3":"蠢",
		"chuo":"戳",
		"chuo1":"戳",
		"chuo4":"绰",
		"ci":"此",
		"ci1":"呲",
		"ci2":"词",
		"ci3":"此",
		"ci4":"伺",
		"cong":"从",
		"cong1":"枞",
		"cong2":"从",
		"cou":"凑",
		"cou4":"凑",
		"cu":"粗",
		"cu1":"粗",
		"cu2":"徂",
		"cu4":"酢",
		"cuan":"蹿",
		"cuan1":"蹿",
		"cuan4":"篡",
		"cui":"摧",
		"cui1":"摧",
		"cui3":"璀",
		"cui4":"脆",
		"cun":"存",
		"cun1":"村",
		"cun2":"存",
		"cun3":"忖",
		"cun4":"寸",
		"cuo":"措",
		"cuo1":"撮",
		"cuo2":"嵯",
		"cuo3":"脞",
		"cuo4":"措",
		"d":"的",
		"da":"大",
		"da1":"嗒",
		"da2":"沓",
		"da3":"打",
		"da4":"大",
		"dai":"带",
		"dai1":"呔",
		"dai3":"歹",
		"dai4":"带",
		"dan":"弹",
		"dan1":"单",
		"dan3":"疸",
		"dan4":"弹",
		"dang":"铛",
		"dang1":"铛",
		"dang3":"挡",
		"dang4":"荡",
		"dao":"到",
		"dao1":"叨",
		"dao3":"捣",
		"dao4":"到",
		"de":"的",
		"de2":"得",
		"den4":"㩐",
		"deng":"蹬",
		"deng1":"蹬",
		"deng3":"等",
		"deng4":"瞪",
		"di":"地",
		"di1":"堤",
		"di2":"翟",
		"di3":"底",
		"di4":"地",
		"dian":"踮",
		"dian1":"颠",
		"dian3":"踮",
		"dian4":"佃",
		"diao":"调",
		"diao1":"碉",
		"diao3":"屌",
		"diao4":"调",
		"die":"碟",
		"die1":"跌",
		"die2":"碟",
		"die4":"哋",
		"ding":"定",
		"ding1":"丁",
		"ding3":"顶",
		"ding4":"定",
		"diu":"丢",
		"diu1":"丢",
		"dong":"侗",
		"dong1":"东",
		"dong3":"董",
		"dong4":"侗",
		"dou":"都",
		"dou1":"都",
		"dou3":"抖",
		"dou4":"斗",
		"du":"读",
		"du1":"督",
		"du2":"读",
		"du3":"堵",
		"du4":"度",
		"duan":"短",
		"duan1":"端",
		"duan3":"短",
		"duan4":"锻",
		"dui":"兑",
		"dui1":"堆",
		"dui4":"兑",
		"dun":"顿",
		"dun1":"蹲",
		"dun3":"盹",
		"dun4":"顿",
		"duo":"掇",
		"duo1":"掇",
		"duo2":"夺",
		"duo3":"垛",
		"duo4":"柁",
		"e":"噁",
		"e1":"屙",
		"e2":"蛾",
		"e3":"噁",
		"e4":"恶",
		"ei":"诶",
		"ei2":"诶",
		"en":"摁",
		"en1":"恩",
		"en4":"摁",
		"eng":"鞥",
		"eng1":"鞥",
		"er":"耳",
		"er2":"而",
		"er3":"耳",
		"er4":"佴",
		"fa":"法",
		"fa1":"发",
		"fa2":"罚",
		"fa3":"法",
		"fa4":"珐",
		"fan":"反",
		"fan1":"番",
		"fan2":"樊",
		"fan3":"反",
		"fan4":"范",
		"fang":"放",
		"fang1":"方",
		"fang2":"肪",
		"fang3":"仿",
		"fang4":"放",
		"fei":"菲",
		"fei1":"菲",
		"fei2":"肥",
		"fei3":"匪",
		"fei4":"芾",
		"fen":"芬",
		"fen1":"芬",
		"fen2":"坟",
		"fen3":"粉",
		"fen4":"奋",
		"feng":"逢",
		"feng1":"丰",
		"feng2":"逢",
		"feng3":"讽",
		"feng4":"缝",
		"fou":"否",
		"fou3":"否",
		"fu":"赴",
		"fu1":"夫",
		"fu2":"佛",
		"fu3":"甫",
		"fu4":"赴",
		"ga":"尬",
		"ga1":"伽",
		"ga2":"噶",
		"ga3":"尕",
		"ga4":"尬",
		"gai":"盖",
		"gai1":"该",
		"gai3":"改",
		"gai4":"盖",
		"gan":"干",
		"gan1":"甘",
		"gan3":"赶",
		"gan4":"干",
		"gang":"冈",
		"gang1":"冈",
		"gang3":"岗",
		"gang4":"戆",
		"gao":"告",
		"gao1":"篙",
		"gao3":"镐",
		"gao4":"告",
		"ge":"硌",
		"ge1":"胳",
		"ge2":"鬲",
		"ge3":"哿",
		"ge4":"硌",
		"gei":"给",
		"gei3":"给",
		"gen":"根",
		"gen1":"根",
		"gen2":"哏",
		"gen3":"艮",
		"gen4":"亘",
		"geng":"更",
		"geng1":"耕",
		"geng3":"埂",
		"geng4":"更",
		"gong":"工",
		"gong1":"工",
		"gong3":"巩",
		"gong4":"贡",
		"gou":"垢",
		"gou1":"钩",
		"gou3":"苟",
		"gou4":"垢",
		"gu":"嘏",
		"gu1":"辜",
		"gu2":"鶻",
		"gu3":"嘏",
		"gu4":"故",
		"gua":"挂",
		"gua1":"栝",
		"gua3":"剐",
		"gua4":"挂",
		"guai":"怪",
		"guai1":"乖",
		"guai3":"拐",
		"guai4":"怪",
		"guan":"棺",
		"guan1":"棺",
		"guan3":"莞",
		"guan4":"罐",
		"guang":"广",
		"guang1":"光",
		"guang3":"广",
		"guang4":"逛",
		"gui":"龟",
		"gui1":"龟",
		"gui3":"轨",
		"gui4":"炔",
		"gun":"辊",
		"gun3":"辊",
		"gun4":"棍",
		"guo":"过",
		"guo1":"锅",
		"guo2":"国",
		"guo3":"果",
		"guo4":"过",
		"ha":"哈",
		"ha1":"哈",
		"ha2":"蛤",
		"hai":"嚡",
		"hai":"还",
		"hai1":"嗨",
		"hai2":"还",
		"hai3":"海",
		"hai4":"氦",
		"han":"邯",
		"han1":"酣",
		"han2":"邯",
		"han3":"阚",
		"han4":"翰",
		"hang":"行",
		"hang1":"夯",
		"hang2":"行",
		"hang4":"沆",
		"hao":"郝",
		"hao1":"蒿",
		"hao2":"貉",
		"hao3":"郝",
		"hao4":"耗",
		"he":"和",
		"he1":"呵",
		"he2":"和",
		"he4":"赫",
		"hei1":"嘿",
		"hen":"恨",
		"hen2":"痕",
		"hen3":"很",
		"hen4":"恨",
		"heng":"横",
		"heng1":"哼",
		"heng2":"横",
		"hong":"虹",
		"hong1":"轰",
		"hong2":"虹",
		"hong3":"哄",
		"hong4":"讧",
		"hou":"厚",
		"hou1":"齁",
		"hou2":"喉",
		"hou3":"吼",
		"hou4":"厚",
		"hu":"护",
		"hu1":"呼",
		"hu2":"瑚",
		"hu3":"浒",
		"hu4":"护",
		"hua":"花",
		"hua1":"花",
		"hua2":"华",
		"hua4":"画",
		"huai":"坏",
		"huai2":"徊",
		"huai4":"坏",
		"huan":"郇",
		"huan1":"欢",
		"huan2":"郇",
		"huan3":"缓",
		"huan4":"换",
		"huang":"黄",
		"huang1":"荒",
		"huang2":"黄",
		"huang3":"晃",
		"huang4":"㨪",
		"hui":"蛔",
		"hui1":"珲",
		"hui2":"蛔",
		"hui3":"毁",
		"hui4":"会",
		"hun":"魂",
		"hun1":"荤",
		"hun2":"魂",
		"hun4":"混",
		"huo":"活",
		"huo1":"豁",
		"huo2":"活",
		"huo3":"伙",
		"huo4":"砉",
		"ji":"及",
		"ji1":"击",
		"ji2":"及",
		"ji3":"挤",
		"ji4":"偈",
		"jia":"夹",
		"jia1":"夹",
		"jia2":"袷",
		"jia3":"贾",
		"jia4":"稼",
		"jian":"荐",
		"jian1":"犍",
		"jian3":"剪",
		"jian4":"荐",
		"jiang":"僵",
		"jiang1":"僵",
		"jiang3":"蒋",
		"jiang4":"降",
		"jiao":"蕉",
		"jiao1":"蕉",
		"jiao3":"脚",
		"jiao4":"峤",
		"jie":"解",
		"jie1":"嗟",
		"jie2":"颉",
		"jie3":"解",
		"jie4":"戒",
		"jin":"今",
		"jin1":"矜",
		"jin3":"紧",
		"jin4":"进",
		"jing":"经",
		"jing1":"荆",
		"jing3":"颈",
		"jing4":"镜",
		"jiong":"炅",
		"jiong1":"冂",
		"jiong3":"炅",
		"jiu":"厩",
		"jiu1":"揪",
		"jiu3":"玖",
		"jiu4":"厩",
		"ju":"咀",
		"ju1":"居",
		"ju2":"桔",
		"ju3":"咀",
		"ju4":"句",
		"juan":"倦",
		"juan1":"捐",
		"juan3":"卷",
		"juan4":"倦",
		"jue":"嚼",
		"jue1":"撅",
		"jue2":"嚼",
		"jvn":"麇",
		"jvn1":"麇",
		"jvn4":"峻",
		"ka":"咖",
		"ka1":"咖",
		"ka3":"卡",
		"kai":"开",
		"kai1":"开",
		"kai3":"楷",
		"kai4":"忾",
		"kan":"看",
		"kan1":"刊",
		"kan3":"槛",
		"kan4":"看",
		"kang":"康",
		"kang1":"康",
		"kang2":"扛",
		"kang4":"抗",
		"kao":"靠",
		"kao1":"尻",
		"kao3":"考",
		"kao4":"靠",
		"ke":"克",
		"ke1":"苛",
		"ke2":"壳",
		"ke3":"坷",
		"ke4":"克",
		"ken":"肯",
		"ken3":"肯",
		"ken4":"裉",
		"keng":"吭",
		"keng1":"吭",
		"kong":"控",
		"kong1":"空",
		"kong3":"恐",
		"kong4":"控",
		"kou":"口",
		"kou1":"抠",
		"kou3":"口",
		"kou4":"扣",
		"ku":"苦",
		"ku1":"枯",
		"ku3":"苦",
		"ku4":"酷",
		"kua":"挎",
		"kua1":"姱",
		"kua3":"垮",
		"kua4":"挎",
		"kuai":"块",
		"kuai3":"蒯",
		"kuai4":"块",
		"kuan":"宽",
		"kuan1":"宽",
		"kuan3":"款",
		"kuang":"匡",
		"kuang1":"匡",
		"kuang2":"狂",
		"kuang3":"夼",
		"kuang4":"矿",
		"kui":"亏",
		"kui1":"亏",
		"kui2":"葵",
		"kui3":"跬",
		"kui4":"馈",
		"kun":"困",
		"kun1":"坤",
		"kun3":"捆",
		"kun4":"困",
		"kuo":"括",
		"kuo4":"括",
		"la":"啦",
		"la":"垃",
		"la1":"垃",
		"la2":"剌",
		"la3":"喇",
		"la4":"腊",
		"lai":"莱",
		"lai2":"莱",
		"lai4":"赖",
		"lan":"蓝",
		"lan2":"蓝",
		"lan3":"揽",
		"lan4":"烂",
		"lang":"琅",
		"lang1":"啷",
		"lang2":"琅",
		"lang3":"朗",
		"lang4":"莨",
		"lao":"老",
		"lao1":"捞",
		"lao2":"劳",
		"lao3":"老",
		"lao4":"酪",
		"le":"了",
		"le1":"肋",
		"le4":"乐",
		"lei":"累",
		"lei1":"勒",
		"lei2":"雷",
		"lei3":"蕾",
		"lei4":"累",
		"leng":"冷",
		"leng2":"棱",
		"leng3":"冷",
		"leng4":"愣",
		"li":"理",
		"li1":"哩",
		"li2":"厘",
		"li3":"理",
		"li4":"栎",
		"lia":"俩",
		"lia3":"俩",
		"lian":"联",
		"lian2":"联",
		"lian3":"敛",
		"lian4":"链",
		"liang":"两",
		"liang2":"粮",
		"liang3":"两",
		"liang4":"辆",
		"liao":"聊",
		"liao1":"撩",
		"liao2":"聊",
		"liao3":"蓼",
		"liao4":"撂",
		"lie":"列",
		"lie3":"咧",
		"lie4":"列",
		"lin":"琳",
		"lin1":"拎",
		"lin2":"琳",
		"lin3":"凛",
		"lin4":"赁",
		"ling":"玲",
		"ling2":"玲",
		"ling3":"岭",
		"ling4":"另",
		"liu":"琉",
		"liu1":"溜",
		"liu2":"琉",
		"liu3":"柳",
		"liu4":"六",
		"long":"泷",
		"long2":"泷",
		"long3":"垄",
		"long4":"徿",
		"lou":"偻",
		"lou2":"偻",
		"lou3":"搂",
		"lou4":"漏",
		"lu":"碌",
		"lu1":"撸",
		"lu2":"芦",
		"lu3":"掳",
		"lu4":"碌",
		"luan":"乱",
		"luan2":"峦",
		"luan3":"卵",
		"luan4":"乱",
		"lun":"论",
		"lun1":"抡",
		"lun2":"纶",
		"lun4":"论",
		"luo":"萝",
		"luo1":"啰",
		"luo2":"萝",
		"luo3":"裸",
		"luo4":"落",
		"lv":"率",
		"lv2":"驴",
		"lv3":"捋",
		"lv4":"率",
		"lve":"掠",
		"lve4":"掠",
		"m2":"呣",
		"ma":"玛",
		"ma1":"妈",
		"ma2":"麻",
		"ma3":"玛",
		"ma4":"骂",
		"mai":"脉",
		"mai2":"埋",
		"mai3":"买",
		"mai4":"脉",
		"man":"蔓",
		"man1":"颟",
		"man2":"瞒",
		"man3":"满",
		"man4":"蔓",
		"mang":"芒",
		"mang2":"芒",
		"mang3":"莽",
		"mao":"茅",
		"mao1":"猫",
		"mao2":"茅",
		"mao3":"铆",
		"mao4":"茂",
		"me":"么",
		"mei":"镁",
		"mei2":"没",
		"mei3":"镁",
		"mei4":"昧",
		"men":"门",
		"men2":"门",
		"men4":"闷",
		"meng":"梦",
		"meng2":"盟",
		"meng3":"锰",
		"meng4":"梦",
		"mi":"米",
		"mi1":"眯",
		"mi2":"祢",
		"mi3":"米",
		"mi4":"秘",
		"mian":"面",
		"mian2":"棉",
		"mian3":"渑",
		"mian4":"面",
		"miao":"苗",
		"miao1":"喵",
		"miao2":"苗",
		"miao3":"藐",
		"miao4":"庙",
		"mie":"蔑",
		"mie1":"乜",
		"mie4":"蔑",
		"min":"民",
		"min2":"民",
		"min3":"敏",
		"min3":"敏",
		"ming":"明",
		"ming2":"明",
		"ming3":"酩",
		"ming4":"命",
		"miu":"谬",
		"miu4":"谬",
		"mo":"末",
		"mo1":"摸",
		"mo2":"模",
		"mo3":"抹",
		"mo4":"末",
		"mou":"某",
		"mou1":"哞",
		"mou2":"缪",
		"mou3":"某",
		"mu":"墓",
		"mu2":"毪",
		"mu3":"拇",
		"mu4":"墓",
		"n":"嗯",
		"n2":"嗯",
		"na":"那",
		"na2":"拿",
		"na3":"哪",
		"na4":"那",
		"nai":"氖",
		"nai3":"氖",
		"nai4":"耐",
		"nan":"南",
		"nan1":"囡",
		"nan2":"南",
		"nan3":"腩",
		"nang":"囊",
		"nang1":"囔",
		"nang2":"囊",
		"nang3":"攮",
		"nao":"臑",
		"nao1":"孬",
		"nao2":"挠",
		"nao3":"脑",
		"nao4":"臑",
		"ne":"呢",
		"ne4":"讷",
		"nei":"内",
		"nei3":"馁",
		"nei4":"内",
		"nen":"恁",
		"nen4":"恁",
		"neng":"能",
		"neng2":"能",
		"ni":"拟",
		"ni1":"妮",
		"ni2":"霓",
		"ni3":"拟",
		"ni4":"匿",
		"nian":"年",
		"nian1":"蔫",
		"nian2":"年",
		"nian3":"碾",
		"nian4":"念",
		"niang":"酿",
		"niang2":"娘",
		"niang4":"酿",
		"niao":"鸟",
		"niao3":"鸟",
		"niao4":"尿",
		"nie":"聂",
		"nie1":"捏",
		"nie4":"聂",
		"nin":"您",
		"nin2":"您",
		"ning":"柠",
		"ning2":"柠",
		"ning4":"泞",
		"niu":"牛",
		"niu1":"妞",
		"niu2":"牛",
		"niu3":"扭",
		"nong":"弄",
		"nong2":"脓",
		"nong4":"弄",
		"nou":"耨",
		"nou4":"耨",
		"nu":"努",
		"nu2":"奴",
		"nu3":"努",
		"nu4":"怒",
		"nuan":"暖",
		"nuan3":"暖",
		"nuo":"挪",
		"nuo2":"挪",
		"nuo4":"喏",
		"nv":"女",
		"nv3":"女",
		"nv4":"恧",
		"nve4":"疟",
		"o":"哦",
		"o1":"喔",
		"o2":"哦",
		"ou":"藕",
		"ou1":"欧",
		"ou3":"藕",
		"ou4":"怄",
		"pa":"爬",
		"pa1":"啪",
		"pa2":"爬",
		"pa4":"帕",
		"pai":"排",
		"pai1":"拍",
		"pai2":"排",
		"pai4":"湃",
		"pan":"盘",
		"pan1":"攀",
		"pan2":"盘",
		"pan4":"盼",
		"pang":"庞",
		"pang1":"乓",
		"pang2":"庞",
		"pang3":"耪",
		"pang4":"胖",
		"pao":"跑",
		"pao1":"抛",
		"pao2":"刨",
		"pao3":"跑",
		"pao4":"炮",
		"pei":"培",
		"pei1":"呸",
		"pei2":"培",
		"pei4":"配",
		"pen":"盆",
		"pen1":"喷",
		"pen2":"盆",
		"peng":"碰",
		"peng1":"砰",
		"peng2":"彭",
		"peng3":"捧",
		"peng4":"碰",
		"pi":"坯",
		"pi1":"坯",
		"pi2":"埤",
		"pi3":"匹",
		"pi4":"辟",
		"pian":"片",
		"pian1":"篇",
		"pian2":"谝",
		"pian3":"諞",
		"pian4":"片",
		"piao":"票",
		"piao1":"飘",
		"piao2":"瓢",
		"piao3":"殍",
		"piao4":"票",
		"pie":"撇",
		"pie1":"撇",
		"pie3":"丿",
		"pin":"频",
		"pin1":"拼",
		"pin2":"频",
		"pin3":"品",
		"pin4":"聘",
		"ping":"屏",
		"ping1":"乒",
		"ping2":"屏",
		"po":"迫",
		"po1":"泼",
		"po2":"婆",
		"po3":"颇",
		"po4":"迫",
		"pou":"剖",
		"pou1":"剖",
		"pou2":"裒",
		"pu":"埔",
		"pu1":"扑",
		"pu2":"脯",
		"pu3":"埔",
		"pu4":"曝",
		"qi":"奇",
		"qi1":"期",
		"qi2":"奇",
		"qi3":"起",
		"qi4":"契",
		"qia":"掐",
		"qia1":"掐",
		"qia4":"恰",
		"qian":"前",
		"qian1":"牵",
		"qian2":"前",
		"qian3":"遣",
		"qian4":"欠",
		"qiang":"强",
		"qiang1":"枪",
		"qiang2":"强",
		"qiang3":"抢",
		"qiang4":"炝",
		"qiao":"桥",
		"qiao1":"缲",
		"qiao2":"桥",
		"qiao3":"巧",
		"qiao4":"鞘",
		"qie":"且",
		"qie3":"且",
		"qie4":"切",
		"qin":"溱",
		"qin1":"钦",
		"qin2":"溱",
		"qin3":"寝",
		"qin4":"沁",
		"qing":"擎",
		"qing1":"鲭",
		"qing2":"擎",
		"qing3":"顷",
		"qing4":"庆",
		"qiong":"琼",
		"qiong1":"芎",
		"qiong2":"琼",
		"qiu":"求",
		"qiu1":"秋",
		"qiu2":"求",
		"qiu3":"糗",
		"qu":"趣",
		"qu1":"区",
		"qu2":"瞿",
		"qu3":"取",
		"qu4":"趣",
		"quan":"鬈",
		"quan1":"圈",
		"quan2":"鬈",
		"quan3":"犬",
		"quan4":"券",
		"que":"雀",
		"que1":"缺",
		"que2":"瘸",
		"que4":"雀",
		"qvn":"裙",
		"qvn1":"逡",
		"qvn2":"裙",
		"ran":"然",
		"ran2":"然",
		"ran3":"冉",
		"rang":"让",
		"rang2":"瓤",
		"rang3":"壤",
		"rang4":"让",
		"rao":"绕",
		"rao2":"饶",
		"rao3":"扰",
		"rao4":"绕",
		"re":"热",
		"re3":"惹",
		"re4":"热",
		"ren":"壬",
		"ren2":"壬",
		"ren3":"忍",
		"ren4":"韧",
		"reng":"扔",
		"reng1":"扔",
		"reng2":"仍",
		"ri":"日",
		"ri4":"日",
		"rong":"戎",
		"rong1":"茸",
		"rong2":"戎",
		"rong3":"冗",
		"rou":"肉",
		"rou2":"揉",
		"rou4":"肉",
		"ru":"入",
		"ru2":"茹",
		"ru3":"辱",
		"ru4":"入",
		"ruan":"软",
		"ruan2":"堧",
		"ruan3":"软",
		"rui":"瑞",
		"rui2":"蕤",
		"rui3":"蕊",
		"rui4":"瑞",
		"run":"闰",
		"run4":"闰",
		"ruo":"若",
		"ruo2":"捼",
		"ruo4":"若",
		"sa":"挲",
		"sa1":"挲",
		"sa3":"洒",
		"sa4":"萨",
		"sai":"赛",
		"sai1":"塞",
		"sai4":"赛",
		"san":"三",
		"san1":"三",
		"san3":"伞",
		"san4":"散",
		"sang":"丧",
		"sang1":"桑",
		"sang3":"嗓",
		"sang4":"丧",
		"sao":"扫",
		"sao1":"搔",
		"sao3":"扫",
		"sao4":"埽",
		"se":"色",
		"se4":"色",
		"sen":"森",
		"sen1":"森",
		"seng":"僧",
		"seng1":"僧",
		"sha":"莎",
		"sha1":"莎",
		"sha2":"啥",
		"sha3":"傻",
		"sha4":"厦",
		"shai":"晒",
		"shai1":"酾",
		"shai4":"晒",
		"shan":"善",
		"shan1":"杉",
		"shan3":"闪",
		"shan4":"善",
		"shang":"上",
		"shang":"裳",
		"shang1":"墒",
		"shang3":"赏",
		"shang4":"上",
		"shao":"哨",
		"shao1":"梢",
		"shao2":"苕",
		"shao3":"少",
		"shao4":"哨",
		"she":"设",
		"she1":"奢",
		"she2":"蛇",
		"she3":"舍",
		"she4":"设",
		"shei":"谁",
		"shei2":"谁",
		"shen":"椹",
		"shen1":"砷",
		"shen2":"什",
		"shen3":"沈",
		"shen4":"椹",
		"sheng":"生",
		"sheng1":"声",
		"sheng2":"绳",
		"sheng3":"省",
		"sheng4":"盛",
		"shi":"是",
		"shi1":"师",
		"shi2":"石",
		"shi3":"史",
		"shi4":"是",
		"shou":"手",
		"shou1":"收",
		"shou3":"手",
		"shou4":"寿",
		"shu":"术",
		"shu1":"蔬",
		"shu2":"赎",
		"shu3":"薯",
		"shu4":"术",
		"shua":"刷",
		"shua1":"刷",
		"shua3":"耍",
		"shuai":"帅",
		"shuai1":"衰",
		"shuai3":"甩",
		"shuai4":"帅",
		"shuan":"栓",
		"shuan1":"栓",
		"shuan4":"涮",
		"shuang":"霜",
		"shuang1":"霜",
		"shuang3":"爽",
		"shui":"水",
		"shui":"氵",
		"shui2":"誰",
		"shui3":"水",
		"shui4":"睡",
		"shun":"瞬",
		"shun3":"吮",
		"shun4":"瞬",
		"shuo":"说",
		"shuo1":"说",
		"shuo4":"硕",
		"si":"肆",
		"si1":"斯",
		"si3":"死",
		"si4":"肆",
		"song":"颂",
		"song1":"忪",
		"song3":"耸",
		"song4":"颂",
		"sou":"搜",
		"sou1":"搜",
		"sou3":"擞",
		"sou4":"嗽",
		"su":"宿",
		"su1":"苏",
		"su2":"俗",
		"su4":"宿",
		"suan":"蒜",
		"suan1":"酸",
		"suan4":"蒜",
		"sui":"隋",
		"sui1":"虽",
		"sui2":"隋",
		"sui3":"髓",
		"sui4":"碎",
		"sun":"孙",
		"sun1":"孙",
		"sun3":"损",
		"suo":"嗦",
		"suo":"琐",
		"suo1":"缩",
		"suo3":"琐",
		"ta":"铊",
		"ta1":"铊",
		"ta2":"蹹",
		"ta3":"塔",
		"ta4":"挞",
		"tai":"苔",
		"tai1":"胎",
		"tai2":"苔",
		"tai4":"泰",
		"tan":"覃",
		"tan1":"坍",
		"tan2":"覃",
		"tan3":"坦",
		"tan4":"碳",
		"tang":"倘",
		"tang1":"汤",
		"tang2":"糖",
		"tang3":"倘",
		"tang4":"趟",
		"tao":"套",
		"tao1":"掏",
		"tao2":"萄",
		"tao3":"讨",
		"tao4":"套",
		"te":"忒",
		"te4":"忒",
		"teng":"藤",
		"teng2":"藤",
		"ti":"体",
		"ti1":"梯",
		"ti2":"提",
		"ti3":"体",
		"ti4":"裼",
		"tian":"天",
		"tian1":"天",
		"tian2":"填",
		"tian3":"舔",
		"tian4":"掭",
		"tiao":"眺",
		"tiao1":"挑",
		"tiao2":"条",
		"tiao3":"窕",
		"tiao4":"眺",
		"tie":"铁",
		"tie1":"贴",
		"tie3":"铁",
		"tie4":"餮",
		"ting":"廷",
		"ting1":"町",
		"ting2":"廷",
		"ting3":"挺",
		"tong":"通",
		"tong1":"通",
		"tong2":"僮",
		"tong3":"桶",
		"tong4":"痛",
		"tou":"投",
		"tou1":"偷",
		"tou2":"投",
		"tou3":"钭",
		"tou4":"透",
		"tu":"图",
		"tu1":"凸",
		"tu2":"图",
		"tu3":"土",
		"tu4":"兔",
		"tuan":"团",
		"tuan1":"湍",
		"tuan2":"团",
		"tuan3":"疃",
		"tuan4":"彖",
		"tui":"褪",
		"tui1":"推",
		"tui2":"颓",
		"tui3":"腿",
		"tui4":"褪",
		"tun":"屯",
		"tun1":"吞",
		"tun2":"屯",
		"tun3":"氽",
		"tuo":"拖",
		"tuo1":"拖",
		"tuo2":"驮",
		"tuo3":"椭",
		"tuo4":"拓",
		"wa":"哇",
		"wa1":"挖",
		"wa2":"娃",
		"wa3":"瓦",
		"wa4":"袜",
		"wai":"外",
		"wai1":"歪",
		"wai3":"崴",
		"wai4":"外",
		"wan":"万",
		"wan1":"豌",
		"wan2":"玩",
		"wan3":"碗",
		"wan4":"万",
		"wang":"王",
		"wang1":"汪",
		"wang2":"王",
		"wang3":"枉",
		"wang4":"旺",
		"wei":"蔚",
		"wei1":"威",
		"wei2":"圩",
		"wei3":"尾",
		"wei4":"蔚",
		"wen":"问",
		"wen1":"瘟",
		"wen2":"蚊",
		"wen3":"吻",
		"wen4":"问",
		"weng":"嗡",
		"weng1":"嗡",
		"weng3":"蓊",
		"weng4":"瓮",
		"wo":"我",
		"wo1":"涡",
		"wo3":"我",
		"wo4":"斡",
		"wu":"武",
		"wu1":"巫",
		"wu2":"无",
		"wu3":"武",
		"wu4":"坞",
		"xi":"昔",
		"xi1":"昔",
		"xi2":"檄",
		"xi3":"铣",
		"xi4":"戏",
		"xia":"吓",
		"xia1":"虾",
		"xia2":"匣",
		"xia4":"吓",
		"xian":"现",
		"xian1":"先",
		"xian2":"咸",
		"xian3":"显",
		"xian4":"现",
		"xiang":"巷",
		"xiang1":"相",
		"xiang2":"翔",
		"xiang3":"想",
		"xiang4":"巷",
		"xiao":"晓",
		"xiao1":"萧",
		"xiao2":"淆",
		"xiao3":"晓",
		"xiao4":"校",
		"xie":"楔",
		"xie1":"楔",
		"xie2":"挟",
		"xie3":"写",
		"xie4":"械",
		"xin":"新",
		"xin1":"薪",
		"xin2":"鐔",
		"xin4":"信",
		"xing":"幸",
		"xing1":"星",
		"xing2":"行",
		"xing3":"醒",
		"xing4":"幸",
		"xiong":"雄",
		"xiong1":"兄",
		"xiong2":"雄",
		"xiong4":"詗",
		"xiu":"休",
		"xiu1":"休",
		"xiu3":"朽",
		"xiu4":"嗅",
		"xu":"许",
		"xu1":"嘘",
		"xu2":"徐",
		"xu3":"许",
		"xu4":"蓄",
		"xuan":"选",
		"xuan1":"轩",
		"xuan2":"悬",
		"xuan3":"选",
		"xuan4":"眩",
		"xue":"学",
		"xue1":"削",
		"xue2":"学",
		"xue3":"雪",
		"xue4":"血",
		"xvn":"训",
		"xvn1":"勋",
		"xvn2":"寻",
		"xvn4":"训",
		"ya":"压",
		"ya1":"压",
		"ya2":"芽",
		"ya3":"雅",
		"ya4":"轧",
		"yan":"言",
		"yan1":"烟",
		"yan2":"言",
		"yan3":"奄",
		"yan4":"燕",
		"yang":"样",
		"yang1":"殃",
		"yang2":"杨",
		"yang3":"氧",
		"yang4":"样",
		"yao":"药",
		"yao1":"邀",
		"yao2":"姚",
		"yao3":"咬",
		"yao4":"药",
		"ye":"野",
		"ye1":"椰",
		"ye2":"耶",
		"ye3":"野",
		"ye4":"页",
		"yi":"一",
		"yi1":"一",
		"yi2":"颐",
		"yi3":"椅",
		"yi4":"佚",
		"yin":"茵",
		"yin1":"茵",
		"yin2":"吟",
		"yin3":"饮",
		"yin4":"印",
		"ying":"英",
		"ying1":"英",
		"ying2":"莹",
		"ying3":"影",
		"ying4":"硬",
		"yo":"哟",
		"yo1":"哟",
		"yong":"用",
		"yong1":"拥",
		"yong2":"喁",
		"yong3":"踊",
		"yong4":"用",
		"you":"酉",
		"you1":"幽",
		"you2":"尢",
		"you3":"酉",
		"you4":"右",
		"yu":"予",
		"yu1":"迂",
		"yu2":"俞",
		"yu3":"予",
		"yu4":"玉",
		"yuan":"苑",
		"yuan1":"鸳",
		"yuan2":"元",
		"yuan3":"远",
		"yuan4":"苑",
		"yue":"越",
		"yue1":"曰",
		"yue3":"噦",
		"yue4":"越",
		"yun":"筠",
		"yun1":"晕",
		"yun2":"筠",
		"yun3":"陨",
		"yun4":"熨",
		"za":"砸",
		"za1":"拶",
		"za2":"砸",
		"za3":"咋",
		"zai":"载",
		"zai1":"栽",
		"zai3":"仔",
		"zai4":"载",
		"zan":"咱",
		"zan1":"簪",
		"zan2":"咱",
		"zan3":"攒",
		"zan4":"暂",
		"zang":"赃",
		"zang1":"赃",
		"zang3":"驵",
		"zang4":"脏",
		"zao":"躁",
		"zao1":"遭",
		"zao2":"凿",
		"zao3":"藻",
		"zao4":"躁",
		"ze":"择",
		"ze2":"择",
		"ze4":"仄",
		"zei2":"贼",
		"zen":"怎",
		"zen3":"怎",
		"zen4":"谮",
		"zeng":"增",
		"zeng1":"增",
		"zeng4":"赠",
		"zhou":"舟",
		"zhou1":"周",
		"zhou2":"轴",
		"zhou3":"肘",
		"zhou4":"咒",
		"zha":"扎",
		"zha1":"扎",
		"zha2":"札",
		"zha3":"眨",
		"zha4":"栅",
		"zhai":"窄",
		"zhai1":"摘",
		"zhai2":"宅",
		"zhai3":"窄",
		"zhai4":"债",
		"zhan":"蘸",
		"zhan1":"粘",
		"zhan3":"盏",
		"zhan4":"蘸",
		"zhang":"长",
		"zhang1":"张",
		"zhang3":"长",
		"zhang4":"杖",
		"zhao":"爪",
		"zhao1":"啁",
		"zhao3":"爪",
		"zhao4":"赵",
		"zhe":"者",
		"zhe1":"遮",
		"zhe2":"折",
		"zhe3":"者",
		"zhe4":"蔗",
		"zhen":"珍",
		"zhen1":"珍",
		"zhen3":"枕",
		"zhen4":"震",
		"zheng":"正",
		"zheng1":"徵",
		"zheng3":"整",
		"zheng4":"正",
		"zhi":"吱",
		"zhi1":"吱",
		"zhi2":"殖",
		"zhi3":"址",
		"zhi4":"峙",
		"zhong":"中",
		"zhong1":"中",
		"zhong3":"种",
		"zhong4":"重",
		"zhou1":"舟",
		"zhou2":"轴",
		"zhou3":"肘",
		"zhou4":"咒",
		"zhu":"著",
		"zhu1":"珠",
		"zhu2":"逐",
		"zhu3":"煮",
		"zhu4":"著",
		"zhua":"抓",
		"zhua1":"抓",
		"zhuai":"拽",
		"zhuai1":"拽",
		"zhuai3":"跩",
		"zhuan":"赚",
		"zhuan1":"专",
		"zhuan3":"转",
		"zhuan4":"赚",
		"zhuang":"撞",
		"zhuang1":"桩",
		"zhuang4":"撞",
		"zhui":"隹",
		"zhui1":"隹",
		"zhui4":"赘",
		"zhun":"准",
		"zhun1":"谆",
		"zhun3":"准",
		"zhuo":"捉",
		"zhuo1":"捉",
		"zhuo2":"卓",
		"zi":"子",
		"zi1":"觜",
		"zi3":"紫",
		"zi4":"自",
		"zong":"总",
		"zong1":"鬃",
		"zong3":"总",
		"zong4":"纵",
		"zou":"走",
		"zou1":"邹",
		"zou3":"走",
		"zou4":"奏",
		"zu":"祖",
		"zu1":"租",
		"zu2":"足",
		"zu3":"祖",
		"zuan":"钻",
		"zuan1":"钻",
		"zuan3":"纂",
		"zuan4":"攥",
		"zui":"醉",
		"zui1":"朘",
		"zui3":"嘴",
		"zui4":"醉",
		"zun":"尊",
		"zun1":"尊",
		"zun3":"撙",
		"zuo":"做",
		"zuo1":"嘬",
		"zuo2":"琢",
		"zuo3":"左",
		"zuo4":"做",
		}
		return pinInToText
	
	def getSingleWord():
		singleWord={
		"iu":"yiu",
		"ia":"ya",
		"ua":"wa",
		"e":"e",
		"er":"er",
		"uan":"wuan",
		"ue":"yue",
		"u":"yu",
		"u":"wu",
		"i":"yi",
		"uo":"wo",
		"un":"wen",
		"a":"oa",
		"iong":"yong",
		"ong":"wong",
		"iang":"yang",
		"uang":"wang",
		"en":"en",
		"eng":"eng",
		"ang":"ang",
		"an":"an",
		"ao":"ao",
		"ai":"ai",
		"ing":"ying",
		"ei":"ei",
		"ie":"ye",
		"iao":"yao",
		"ui":"wei",
		"ou":"ou",
		"in":"yin",
		"ian":"yan",
		"vn":"yun",
		"ZH":"zhi",
		"CH":"chi",
		"SH":"shi",
		"R":"ri",
		"Z":"zi",
		"C":"ci",
		"D":"de",
		"S":"si"
		}
		return singleWord