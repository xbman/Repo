import util, urllib2 , os , xbmcaddon , urllib , xbmcgui , xbmcplugin , random ,re


mysettings = xbmcaddon.Addon(id = 'plugin.video.Vlive')
getSetting = xbmcaddon.Addon().getSetting
setSetting = xbmcaddon.Addon().setSetting
enable_custom_params = mysettings.getSetting('enable_custom_params')
TIME_OUT = mysettings.getSetting('timeout_')
##################################################
MainSite = mysettings.getSetting('browser_site')
BROWSER_HEADER = mysettings.getSetting('browser_header')
KEY_URL = mysettings.getSetting('key_url')
PLAY_PARAMS = mysettings.getSetting('play_params')
DOMAIN_TAG = mysettings.getSetting('domain_tag')
mysettings.setSetting(id='scrolldown', value='Customization')

######## Set Default parameter values for updates.#######
if enable_custom_params == "false":
    MainSite = mysettings.setSetting(id='browser_site', value='https://vaughnlive.tv')
    BROWSER_HEADER = mysettings.setSetting(id='browser_header', value='Mozilla/5.0 (Windows NT 6.0; rv:52.0) Gecko/20100101 Firefox/52.0')
    KEY_URL = mysettings.setSetting(id='key_url', value='http://{site}{path}{domainTag}_{channelname}?{version}_{ms}-{ms}-{random}')
    PLAY_PARAMS = mysettings.setSetting(id='play_params', value='rtmp://{ip}:{port}/live?{mvnkey} app=live?{mvnkey} swfUrl={SWFURL} pageUrl={MainSite}/{channelname} playpath={domainTag}_{channelname} timeout={timeout}')
    DOMAIN_TAG = mysettings.setSetting(id='domain_tag', value='live')
    mysettings.setSetting(id='scrolldown', value='_Hello_')
    ##############################################

    MainSite = mysettings.getSetting('browser_site')
    BROWSER_HEADER = mysettings.getSetting('browser_header')
    KEY_URL = mysettings.getSetting('key_url')
    PLAY_PARAMS = mysettings.getSetting('play_params')
    DOMAIN_TAG = mysettings.getSetting('domain_tag')
##################################################
thumbmode = int(mysettings.getSetting('thumb_type'))
backmode = int(mysettings.getSetting('back_type'))
profile = mysettings.getAddonInfo('profile')
home = mysettings.getAddonInfo('path')
fanart = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
nothumb = xbmc.translatePath(os.path.join(home, 'nophoto.jpg'))
logos = xbmc.translatePath(os.path.join(home, 'icon.png')) # subfolder for logos
homemenu = xbmc.translatePath(os.path.join(home, 'resources', 'playlists'))

enable_All = mysettings.getSetting('enable_All')
enable_Misc = mysettings.getSetting('enable_Misc')
enable_People = mysettings.getSetting('enable_enable_People')
enable_Nature = mysettings.getSetting('enable_Nature')
enable_Creative = mysettings.getSetting('enable_Creative')
enable_MusicCafe = mysettings.getSetting('enable_MusicCafe')
enable_NewsandTech = mysettings.getSetting('enable_NewsandTech')
enable_Lifestyles = mysettings.getSetting('enable_Lifestyles')
enable_Espanol = mysettings.getSetting('enable_Espanol')
enable_settings = mysettings.getSetting('enable_settings')
enable_custom_view = mysettings.getSetting('enable_custom_view')
menu_view = mysettings.getSetting('menu_view')
thumb_view = mysettings.getSetting('thumb_view')
back_view = mysettings.getSetting('back_view')
#xbmc.executebuiltin("Container.SetViewMode(50)")

ClearImages = 'ClearImages'
NextPage = 'NextPage'
PageOne = 'PageOne'

all = 'all'
misc = 'misc'
people = 'people'
nature = 'nature'
creative = 'creative'
musiccafe = 'musiccafe'
newsandtech = 'newsandtech'
lifestyles = 'lifestyles'
espanol = 'espanol'
GetVidInfo = 'GetVidInfo'


Categories = 'Categories'
Settings = 'Settings'
#xbmcplugin.setContent(int(sys.argv[1]), 'movies')


def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if mysettings.getSetting('enable_custom_view') == 'true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % mysettings.getSetting(viewType) )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_UNSORTED )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_LABEL )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_GENRE )


def get_params():
	param = []
	paramstring = sys.argv[2]
	if len(paramstring)>= 2:
		params = sys.argv[2]
		cleanedparams = params.replace('?', '')
		if (params[len(params)-1] == '/'):
			params = params[0:len(params)-2]
		pairsofparams = cleanedparams.split('&')
		param = {}
		for i in range(len(pairsofparams)):
			splitparams = {}
			splitparams = pairsofparams[i].split('=')
			if (len(splitparams)) == 2:
				param[splitparams[0]] = splitparams[1]
	return param


def playVideo(params):
        videoLink = params['video']
        url = params['url']
        #mode = params['Type']
        #ip = params['ip']
        #port = params['port']
        #channelname = params['channelname']
        #key = params['key']
        util.playMedia(params['title'], params['image'], videoLink, 'Video')




def main():
    if getSetting("enable_All") == 'true':
        util.add_dir('All', all, 0, 0, 0, 0, 2, icon, fanart)
    if getSetting("enable_Misc") == 'true':
        util.add_dir('Misc', misc, 0, 0, 0, 0, 2, icon, fanart)
    if getSetting("enable_People") == 'true':
        util.add_dir('People', people, 0, 0, 0, 0, 2, icon, fanart)
    if getSetting("enable_Nature") == 'true':
        util.add_dir('Nature', nature, 0, 0, 0, 0, 2, icon, fanart)
    if getSetting("enable_Creative") == 'true':
        util.add_dir('Creative', creative, 0, 0, 0, 0, 2, icon, fanart)
    if getSetting("enable_MusicCafe") == 'true':
        util.add_dir('Music Cafe', musiccafe, 0, 0, 0, 0, 2, icon, fanart)
    if getSetting("enable_NewsandTech") == 'true':
        util.add_dir('News and Tech', newsandtech, 0, 0, 0, 0, 2, icon, fanart)
    if getSetting("enable_Lifestyles") == 'true':
        util.add_dir('Lifestyles', lifestyles, 0, 0, 0, 0, 2, icon, fanart)
    if getSetting("enable_Espanol") == 'true':
        util.add_dir('Espanol', espanol, 0, 0, 0, 0, 2, icon, fanart)
    if getSetting("enable_settings") == 'true':
        util.add_dir3('[COLOR slategray]Settings[/COLOR]', Settings, 0, 0, None, 0, 3, icon, fanart)
    setView('movies', 'menu_view')

def start(url,mode,ip,port,channelname,key,iconimage):
    if 'all' in url:
        ### VlistPage is the page the channels are listed on vaughnlive.
        VlistPage = MainSite + '/browse/all'
        GetChannelName(VlistPage,url,mode,iconimage)
    elif 'misc' in url:
        VlistPage = MainSite + '/browse/misc'
        GetChannelName(VlistPage,url,mode,iconimage)
    elif 'people' in url:
        VlistPage = MainSite + '/browse/people'
        GetChannelName(VlistPage,url,mode,iconimage)
    elif 'nature' in url:
        VlistPage = MainSite + '/browse/nature'
        GetChannelName(VlistPage,url,mode,iconimage)
    elif 'creative' in url:
        VlistPage = MainSite + '/browse/creative'
        GetChannelName(VlistPage,url,mode,iconimage)
    elif 'musiccafe' in url:
        VlistPage = MainSite + '/browse/music_cafe'
        GetChannelName(VlistPage,url,mode,iconimage)
    elif 'newsandtech' in url:
        VlistPage = MainSite + '/browse/news_tech'
        GetChannelName(VlistPage,url,mode,iconimage)
    elif 'lifestyles' in url:
        VlistPage = MainSite + '/browse/lifestyles'
        GetChannelName(VlistPage,url,mode,iconimage)
    elif 'espanol' in url:
        VlistPage = MainSite + '/browse/espanol'
        GetChannelName(VlistPage,url,mode,iconimage)
    elif 'GetVidInfo' in url:
        GetVID(ip,port,channelname,key,iconimage)

### Get the channel names and live images from the vl section page.
def GetChannelName(VlistPage,url,mode,iconimage):
    req = urllib2.Request(VlistPage, headers={'User-Agent' : BROWSER_HEADER })
    page = urllib2.urlopen(req)
    if page and page.getcode() == 200:
        data = page.read()
        datos = util.extractAll(data, '<div class="browseThumb">', '</div>')
        for stuff in datos:
            channelname = util.extract(stuff, '<a href="/', '" target="_top">')
            if thumbmode == 0:
                channelthumb = "http://" + util.extract(stuff, 'target="_top"><img src="//', '" class"browseThumb"')
                iconimage = channelthumb
            if thumbmode == 1:
                channelthumb = "https://cdn.vaughnsoft.com/vaughnsoft/vaughn/img_profiles/" + channelname + "_320.jpg"
                iconimage = channelthumb
            if backmode == 0:
                backthumb = "http://" + util.extract(stuff, 'target="_top"><img src="//', '" class"browseThumb"')
                fanart = backthumb
            if backmode == 1:
                backthumb = "https://cdn.vaughnsoft.com/vaughnsoft/vaughn/img_profiles/" + channelname + "_320.jpg"
                fanart = backthumb
            util.add_dir2(channelname, GetVidInfo, 0, 0, channelname, 0, 4, channelthumb, backthumb)
    setView('movies', 'thumb_view')


def GetVID(ip,port,channelname,key,iconimage):
    ### GET SWF URL from channel page.
    url = MainSite + "/embed/video/" + channelname
    req = urllib2.Request(url, headers={'User-Agent' : BROWSER_HEADER})
    swfplayer_re = re.compile(r'swfobject.embedSWF\("(/\d+/swf/[0-9A-Za-z]+\.swf)"')
    page=urllib2.urlopen(req)
    data=page.read()
    match = re.compile('swfobject.embedSWF\("(.+?)"').findall(data)
    #print str(match[0])
    #print str(match[1])
    #print str(match[2])
    SWFURL = MainSite + str(match[2])

    ### Get the data directly from the .swf file.
    ### GET SWF Data- mvnVersion(0.1.1.793) - DomainPath(mvn.vaughnsoft.net) - MvnURL ending path(/video/edge/)
    reqSWF = urllib2.Request(SWFURL, headers={'User-Agent' : BROWSER_HEADER})
    openpage=urllib2.urlopen(reqSWF)
    getswfdata=openpage.read()
    swfdata = util.swfdecompress(getswfdata).decode("latin1")
    player_version_m = re.search(r"0\.\d+\.\d+\.\d+", swfdata)
    info_url_domain_m = re.search(r"\w+\.vaughnsoft\.net", swfdata)
    info_url_path_m = re.search(r"/video/edge/[a-zA-Z0-9_]+-", swfdata)
    player_version = player_version_m and player_version_m.group(0)
    info_url_domain = info_url_domain_m and info_url_domain_m.group(0)
    info_url_path = info_url_path_m and info_url_path_m.group(0)
    #print player_version
    #print info_url_domain
    #print info_url_path

    ### Create mvnKey URL formating and then get the key.
    if player_version and info_url_domain and info_url_path:
        paramsz = {"channelname": channelname,
        "domainTag": DOMAIN_TAG,
        "version": player_version,
        "ms": random.randint(0, 999),
        "random": random.random(),
        "site": info_url_domain,
        "path": info_url_path}
        info_url = KEY_URL.format(**paramsz)
        #print info_url

        #### GET Server ip and port and send video link to xbmc to play.
        geturl = info_url
        requrl = urllib2.Request(geturl, headers={'User-Agent' : BROWSER_HEADER})
        response=urllib2.urlopen(requrl)
        if response and response.getcode() == 200:
            content = response.read()
            content = content.replace(';NA','')
            content = content.replace(';','')
            keyip = content.split(':')
            mvnkey = keyip[2].replace('mvnkey-','')
            Pparams = {"ip": keyip[0],
            "port": keyip[1],
            "mvnkey": mvnkey,
            "SWFURL": SWFURL,
            "MainSite": MainSite,
            "channelname": channelname,
            "domainTag": DOMAIN_TAG,
            "timeout": TIME_OUT}
            Playparams = PLAY_PARAMS.format(**Pparams)
            #xbmc.Player().play(Playparams)
            li = xbmcgui.ListItem(label=channelname, iconImage=iconimage, thumbnailImage=iconimage, path=Playparams)
            li.setInfo(type="Video", infoLabels={ "Title": 'Channel: [COLOR=skyblue][B]' +  channelname + '[/B][/COLOR]', "plot": 'You are watching Channel: ' + '[COLOR=skyblue][B]' + channelname + '[/B][/COLOR]' })
            xbmc.Player().play(item=Playparams, listitem=li)


def settings():
    xbmcaddon.Addon().openSettings()

def test():
    params = get_params()
    url = None
    name = None
    mode = None
    iconimage = None
    channelthumb = None
    ip = '0'
    port = '0'
    key = '0'
    channelname = 'None'
    try:
        url = urllib.unquote_plus(params["url"])
    except:
        pass
    try:
        name = urllib.unquote_plus(params["name"])
    except:
        pass
    try:
        ip = str(params["ip"])
    except:
        pass
    try:
        port = str(params["port"])
    except:
        pass
    try:
        channelname = str(params["channelname"])
    except:
        pass
    try:
        key = str(params["key"])
    except:
        pass
    try:
        mode = int(params["mode"])
    except:
        pass
    try:
        iconimage = urllib.unquote_plus(params["iconimage"])
    except:
        pass
    try:
        channelthumb = urllib.unquote_plus(params["channelthumb"])
    except:
        pass
    if mode == None or url == None or len(url) < 1:
        main()
    elif mode == 2:
        start(url,mode,ip,port,channelname,key,iconimage)
    elif mode == 3:
        settings()
    elif mode == 4:
        GetVID(ip,port,channelname,key,iconimage)



parameters = util.parseParameters()
if 'play' in parameters:
    params = get_params()
    #mode = params['mode']
    #url = params['url']
    #totalusers = params['Num']
    #url = None
    #mode = None
    try:
	    url = urllib.unquote_plus(params["url"])
    except:
	    pass
    try:
	    mode = int(params["mode"])
    except:
	    pass
    playVideo(parameters)
else:
    test()



xbmcplugin.endOfDirectory(int(sys.argv[1]))