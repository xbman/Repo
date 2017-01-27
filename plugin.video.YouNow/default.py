import util, urllib2 , os , xbmcaddon , urllib , xbmcgui , xbmcplugin , sqlite3


mysettings = xbmcaddon.Addon(id = 'plugin.video.YouNow')
getSetting = xbmcaddon.Addon().getSetting
langmode = int(mysettings.getSetting('lang_type'))
if langmode == 0:
    TheLang = 'en'
elif langmode == 1:
    TheLang = 'es'
elif langmode == 2:
    TheLang = 'me'
elif langmode == 3:
    TheLang = 'de'
elif langmode == 4:
    TheLang = 'fr'
elif langmode == 5:
    TheLang = 'pt'
elif langmode == 6:
    TheLang = 'tr'
elif langmode == 7:
    TheLang = 'ww'
younow = 'https://api.younow.com/php/api/younow/trendingUsers/locale=' + TheLang + '/numberOfRecords=50/startFrom='
#younow = 'https://api.younow.com/php/api/younow/trendingUsers/locale=en/numberOfRecords=50/startFrom='
younowtags = 'https://api.younow.com/php/api/younow/queue/locale=en/numberOfRecords=50/startFrom='  # /tags=sumtag

profile = mysettings.getAddonInfo('profile')
home = mysettings.getAddonInfo('path')
fanart = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
nexticon = xbmc.translatePath(os.path.join(home, 'next.png'))
refreshicon = xbmc.translatePath(os.path.join(home, 'clear.png'))
logos = xbmc.translatePath(os.path.join(home, 'icon.png')) # subfolder for logos
homemenu = xbmc.translatePath(os.path.join(home, 'resources', 'playlists'))

enable_clear_images = mysettings.getSetting('enable_clear_images')
enable_trending_users = mysettings.getSetting('enable_trending_users')
enable_trending_tags = mysettings.getSetting('enable_trending_tags')
enable_settings = mysettings.getSetting('enable_settings')

ClearImages = 'ClearImages'
Cleared = 'Cleared'
PageOne = 'PageOne'
Fifty = 'Fifty'
Page2 = 'Page2'
Page3 = 'Page3'
Page4 = 'Page4'
Page5 = 'Page5'
Page6 = 'Page6'
Page7 = 'Page7'
Page8 = 'Page8'
Page9 = 'Page9'
Page10 = 'Page10'
Page11 = 'Page11'
Page12 = 'Page12'
Page13 = 'Page13'
Page14 = 'Page14'
Page15 = 'Page15'
Page16 = 'Page16'
Page17 = 'Page17'
Page18 = 'Page18'
Page19 = 'Page19'
PageT0 = 'PageT0'
PageT1 = 'PageT1'
PageT2 = 'PageT2'
Categories = 'Categories'
Girls1 = 'Girls1'
Girls2 = 'Girls2'
Girls3 = 'Girls3'
Girls4 = 'Girls4'
Girls5 = 'Girls5'
Guys1 = 'Guys1'
Guys2 = 'Guys2'
Guys3 = 'Guys3'
Guys4 = 'Guys4'
Guys5 = 'Guys5'
Bored1 = 'Bored1'
Bored2 = 'Bored2'
Bored3 = 'Bored3'
Bored4 = 'Bored4'
Dance1 = 'Dance1'
Dance2 = 'Dance2'
Youtuber1 = 'Youtuber1'
Singing1 = 'Singing1'
Musicians1 = 'Musicians1'
Cooking1 = 'Cooking1'
Gaming1 = 'Gaming1'
Truthordare1 = 'Truthordare1'
Talk1 = 'Talk1'
humor1 = 'humor1'
lgbt1 = 'lgbt1'
ask_questions1 = 'ask_questions'
bestof1 = 'bestof1'
alternative1 = 'alternative1'
dj1 = 'dj1'
sleepingsquad1 = 'sleepingsquad1'
advice1 = 'advice1'
chill1 = 'chill1'
art1 = 'art1'
TagSearch = 'TagSearch'
UserSearch = 'UserSearch'
Results = 'Results'
Settings = 'Settings'

xbmcplugin.setContent(int(sys.argv[1]), 'movies')

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
        url = params['Page']
        mode = params['Type']
        util.playMedia(params['title'], params['image'], videoLink, 'Video')
        #start(url,mode) #Enable this if set folder to True in Util.

def add_dir(name, url, mode, iconimage, fanart):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage = "DefaultFolder.png", thumbnailImage = iconimage)
    fanart = fanart
    liz.setArt({'fanart': fanart})
    ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
    return ok

def add_dir2(name, url, mode, iconimage, fanart):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage = "DefaultFolder.png", thumbnailImage = iconimage)
    fanart = fanart
    liz.setArt({'fanart': fanart})
    ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = False)
    return ok

def Cat():
    if mysettings.getSetting("auto_clear") == "true":
        clean_database(False)
    add_dir('Trending Tags [COLOR yellow][B] Guys[/B][/COLOR]', Guys1, 2, icon, fanart)
    add_dir('Trending Tags [COLOR yellow][B] Girls[/B][/COLOR]', Girls1, 2, icon, fanart)
    add_dir('Trending Tags [COLOR yellow][B] Bored[/B][/COLOR]', Bored1, 2, icon, fanart)
    add_dir('Trending Tags [COLOR yellow][B] Dance[/B][/COLOR]', Dance1, 2, icon, fanart)
    add_dir('Trending Tags [COLOR yellow][B] Singing[/B][/COLOR]', Singing1, 2, icon, fanart)
    add_dir('Trending Tags [COLOR yellow][B] Musicians[/B][/COLOR]', Musicians1, 2, icon, fanart)
    add_dir('Trending Tags [COLOR yellow][B] Youtuber[/B][/COLOR]', Youtuber1, 2, icon, fanart)
    add_dir('Trending Tags [COLOR yellow][B] Cooking[/B][/COLOR]', Cooking1, 2, icon, fanart)
    add_dir('Trending Tags [COLOR yellow][B] Gaming[/B][/COLOR]', Gaming1, 2, icon, fanart)
    add_dir('Trending Tags [COLOR yellow][B] Talk[/B][/COLOR]', Talk1, 2, icon, fanart)
    add_dir('Trending Tags [COLOR yellow][B] Truthordare[/B][/COLOR]', Truthordare1, 2, icon, fanart)
    add_dir('Trending Tags [COLOR yellow][B] Humor[/B][/COLOR]', humor1, 2, icon, fanart)
    add_dir('Trending Tags [COLOR yellow][B] Lgbt[/B][/COLOR]', lgbt1, 2, icon, fanart)
    add_dir('Trending Tags [COLOR yellow][B] Ask_questions[/B][/COLOR]', ask_questions1, 2, icon, fanart)
    add_dir('Trending Tags [COLOR yellow][B] Bestof[/B][/COLOR]', bestof1, 2, icon, fanart)
    add_dir('Trending Tags [COLOR yellow][B] Alternative[/B][/COLOR]', alternative1, 2, icon, fanart)
    add_dir('Trending Tags [COLOR yellow][B] Dj[/B][/COLOR]', dj1, 2, icon, fanart)
    add_dir('Trending Tags [COLOR yellow][B] Sleepingsquad[/B][/COLOR]', sleepingsquad1, 2, icon, fanart)
    add_dir('Trending Tags [COLOR yellow][B] Advice[/B][/COLOR]', advice1, 2, icon, fanart)
    add_dir('Trending Tags [COLOR yellow][B] Chill[/B][/COLOR]', chill1, 2, icon, fanart)
    add_dir('Trending Tags [COLOR yellow][B] Art[/B][/COLOR]', art1, 2, icon, fanart)
    #xbmc.executebuiltin("Container.SetViewMode(50)")

def main():
    if getSetting("enable_clear_images") == 'true':
        add_dir2('[COLOR red][B]Clear Younow Images[/B][/COLOR]', ClearImages, 2, refreshicon, fanart)
    if getSetting("enable_trending_users") == 'true':
        add_dir('[B]Trending[B] [COLOR yellow][B] Users[/B][/COLOR]', PageOne, 2, icon, fanart)
    if getSetting("enable_trending_tags") == 'true':
        add_dir('[B]Trending[B] [COLOR yellow][B] Tags[/B][/COLOR]', Categories, 2, icon, fanart)
    if getSetting("enable_settings") == 'true':
        add_dir2('[COLOR slategray]Settings[/COLOR]', Settings, 3, icon, fanart)

def start(url,mode):
    total = 49
    #print total
    if 'PageOne' in url:
        if mysettings.getSetting("auto_clear") == "true":
            clean_database(False)
        TheUrl = younow + '0'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P1 [COLOR yellow] [B]Next Page[/B][/COLOR]', Page2, 2, nexticon, fanart)
    elif 'Page2' in url:
        TheUrl = younow + '50'
        buildMenu(TheUrl,url,mode)
        if total == 49:
            add_dir('P2 [COLOR yellow] [B]Next Page[/B][/COLOR]', Page3, 2, nexticon, fanart)
    elif 'Page3' in url:
        TheUrl = younow + '100'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P3 [COLOR yellow] [B]Next Page[/B][/COLOR]', Page4, 2, nexticon, fanart)
    elif 'Page4' in url:
        TheUrl = younow + '150'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P4 [COLOR yellow] [B]Next Page[/B][/COLOR]', Page5, 2, nexticon, fanart)
    elif 'Page5' in url:
        TheUrl = younow + '200'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P5 [COLOR yellow] [B]Next Page[/B][/COLOR]', Page6, 2, nexticon, fanart)
    elif 'Page6' in url:
        TheUrl = younow + '250'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P6 [COLOR yellow] [B]Next Page[/B][/COLOR]', Page7, 2, nexticon, fanart)
    elif 'Page7' in url:
        TheUrl = younow + '300'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P7 [COLOR yellow] [B]Next Page[/B][/COLOR]', Page8, 2, nexticon, fanart)
    elif 'Page8' in url:
        TheUrl = younow + '350'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P8 [COLOR yellow] [B]Next Page[/B][/COLOR]', Page9, 2, nexticon, fanart)
    elif 'Page9' in url:
        TheUrl = younow + '400'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P9 [COLOR yellow] [B]Next Page[/B][/COLOR]', Page10, 2, nexticon, fanart)
    elif 'Page10' in url:
        TheUrl = younow + '450'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P10 [COLOR yellow] [B]Next Page[/B][/COLOR]', Page11, 2, nexticon, fanart)
    elif 'Page11' in url:
        TheUrl = younow + '500'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P11 [COLOR yellow] [B]Next Page[/B][/COLOR]', Page12, 2, nexticon, fanart)
    elif 'Page12' in url:
        TheUrl = younow + '550'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P12 [COLOR yellow] [B]Next Page[/B][/COLOR]', Page13, 2, nexticon, fanart)
    elif 'Page13' in url:
        TheUrl = younow + '600'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P13 [COLOR yellow] [B]Next Page[/B][/COLOR]', Page14, 2, nexticon, fanart)
    elif 'Page14' in url:
        TheUrl = younow + '650'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P14 [COLOR yellow] [B]Next Page[/B][/COLOR]', Page15, 2, nexticon, fanart)
    elif 'Page15' in url:
        TheUrl = younow + '700'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P15 [COLOR yellow] [B]Next Page[/B][/COLOR]', Page16, 2, nexticon, fanart)
    elif 'Page16' in url:
        TheUrl = younow + '750'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P16 [COLOR yellow] [B]Next Page[/B][/COLOR]', Page17, 2, nexticon, fanart)
    elif 'Page17' in url:
        TheUrl = younow + '800'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P17 [COLOR yellow] [B]Next Page[/B][/COLOR]', Page18, 2, nexticon, fanart)
    elif 'Page18' in url:
        TheUrl = younow + '850'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P18 [COLOR yellow] [B]Next Page[/B][/COLOR]', Page19, 2, nexticon, fanart)
    elif 'Page19' in url:
        TheUrl = younow + '900'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P19 [COLOR yellow] [B]Next Page[/B][/COLOR]', PageT0, 2, nexticon, fanart)
    elif 'PageT0' in url:
        TheUrl = younow + '1000'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P20 [COLOR yellow] [B]Next Page[/B][/COLOR]', PageT1, 2, nexticon, fanart)
    elif 'PageT1' in url:
        TheUrl = younow + '1050'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P21 [COLOR yellow] [B]Next Page[/B][/COLOR]', PageT2, 2, nexticon, fanart)
    elif 'PageT2' in url:
        TheUrl = younow + '1100'
        buildMenu(TheUrl,url,mode)
        #if total >= 49:
        #    add_dir('P22 [COLOR yellow] [B]Next Page[/B][/COLOR]', PageT3, 2, nexticon, fanart)
    elif 'Categories' in url:
        Cat()
    elif 'Girls1' in url:
        TheUrl = younowtags + '0' + '/' + 'tag=' + 'girls'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P1 [COLOR yellow] [B]Next Page[/B][/COLOR]', Girls2, 2, nexticon, fanart)
    elif 'Girls2' in url:
        TheUrl = younowtags + '50' + '/' + 'tag=' + 'girls'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P2 [COLOR yellow] [B]Next Page[/B][/COLOR]', Girls3, 2, nexticon, fanart)
    elif 'Girls3' in url:
        TheUrl = younowtags + '100' + '/' + 'tag=' + 'girls'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P3 [COLOR yellow] [B]Next Page[/B][/COLOR]', Girls4, 2, nexticon, fanart)
    elif 'Girls4' in url:
        TheUrl = younowtags + '150' + '/' + 'tag=' + 'girls'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P4 [COLOR yellow] [B]Next Page[/B][/COLOR]', Girls5, 2, nexticon, fanart)
    elif 'Girls5' in url:
        TheUrl = younowtags + '200' + '/' + 'tag=' + 'girls'
        buildMenu(TheUrl,url,mode)
        #if total >= 49:
            #add_dir('P3 [COLOR yellow] [B]Next Page[/B][/COLOR]', Girls6, 2, nexticon, fanart)
    elif 'Guys1' in url:
        TheUrl = younowtags + '0' + '/' + 'tag=' + 'guys'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P1 [COLOR yellow] [B]Next Page[/B][/COLOR]', Guys2, 2, nexticon, fanart)
    elif 'Guys2' in url:
        TheUrl = younowtags + '50' + '/' + 'tag=' + 'guys'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P2 [COLOR yellow] [B]Next Page[/B][/COLOR]', Guys3, 2, nexticon, fanart)
    elif 'Guys3' in url:
        TheUrl = younowtags + '100' + '/' + 'tag=' + 'guys'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P3 [COLOR yellow] [B]Next Page[/B][/COLOR]', Guys4, 2, nexticon, fanart)
    elif 'Guys4' in url:
        TheUrl = younowtags + '150' + '/' + 'tag=' + 'guys'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P4 [COLOR yellow] [B]Next Page[/B][/COLOR]', Guys5, 2, nexticon, fanart)
    elif 'Guys5' in url:
        TheUrl = younowtags + '200' + '/' + 'tag=' + 'guys'
        buildMenu(TheUrl,url,mode)
        #if total >= 49:
        #    add_dir('P5 [COLOR yellow] [B]Next Page[/B][/COLOR]', Guys6, 2, nexticon, fanart)
    elif 'Bored1' in url:
        TheUrl = younowtags + '0' + '/' + 'tag=' + 'bored'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P1 [COLOR yellow] [B]Next Page[/B][/COLOR]', Bored2, 2, nexticon, fanart)
    elif 'Bored2' in url:
        TheUrl = younowtags + '50' + '/' + 'tag=' + 'bored'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P2 [COLOR yellow] [B]Next Page[/B][/COLOR]', Bored3, 2, nexticon, fanart)
    elif 'Bored3' in url:
        TheUrl = younowtags + '100' + '/' + 'tag=' + 'bored'
        buildMenu(TheUrl,url,mode)
        #if total >= 49:
        #    add_dir('P3 [COLOR yellow] [B]Next Page[/B][/COLOR]', Bored4, 2, nexticon, fanart)
    elif 'Dance1' in url:
        TheUrl = younowtags + '0' + '/' + 'tag=' + 'dance'
        buildMenu(TheUrl,url,mode)
        if total >= 49:
            add_dir('P1 [COLOR yellow] [B]Next Page[/B][/COLOR]', Dance2, 2, nexticon, fanart)
    elif 'Dance2' in url:
        TheUrl = younowtags + '50' + '/' + 'tag=' + 'dance'
        buildMenu(TheUrl,url,mode)
    elif 'Youtuber1' in url:
        TheUrl = younowtags + '0' + '/' + 'tag=' + 'youtuber'
        buildMenu(TheUrl,url,mode)
    elif 'Singing1' in url:
        TheUrl = younowtags + '0' + '/' + 'tag=' + 'singing'
        buildMenu(TheUrl,url,mode)
    elif 'Musicians1' in url:
        TheUrl = younowtags + '0' + '/' + 'tag=' + 'musicians'
        buildMenu(TheUrl,url,mode)
    elif 'Cooking1' in url:
        TheUrl = younowtags + '0' + '/' + 'tag=' + 'cooking'
        buildMenu(TheUrl,url,mode)
    elif 'Gaming1' in url:
        TheUrl = younowtags + '0' + '/' + 'tag=' + 'gaming'
        buildMenu(TheUrl,url,mode)
    elif 'Truthordare1' in url:
        TheUrl = younowtags + '0' + '/' + 'tag=' + 'truthordare'
        buildMenu(TheUrl,url,mode,)
    elif 'Talk1' in url:
        TheUrl = younowtags + '0' + '/' + 'tag=' + 'talk'
        buildMenu(TheUrl,url,mode)
    elif 'humor1' in url:
        TheUrl = younowtags + '0' + '/' + 'tag=' + 'humor'
        buildMenu(TheUrl,url,mode)
    elif 'lgbt1' in url:
        TheUrl = younowtags + '0' + '/' + 'tag=' + 'lgbt'
        buildMenu(TheUrl,url,mode)
    elif 'ask_questions1' in url:
        TheUrl = younowtags + '0' + '/' + 'tag=' + 'ask_questions'
        buildMenu(TheUrl,url,mode)
    elif 'bestof1' in url:
        TheUrl = younowtags + '0' + '/' + 'tag=' + 'bestof'
        buildMenu(TheUrl,url,mode)
    elif 'alternative1' in url:
        TheUrl = younowtags + '0' + '/' + 'tag=' + 'alternative'
        buildMenu(TheUrl,url,mode)
    elif 'dj1' in url:
        TheUrl = younowtags + '0' + '/' + 'tag=' + 'dj'
        buildMenu(TheUrl,url,mode)
    elif 'sleepingsquad1' in url:
        TheUrl = younowtags + '0' + '/' + 'tag=' + 'sleepingsquad'
        buildMenu(TheUrl,url,mode)
    elif 'advice1' in url:
        TheUrl = younowtags + '0' + '/' + 'tag=' + 'advice'
        buildMenu(TheUrl,url,mode)
    elif 'chill1' in url:
        TheUrl = younowtags + '0' + '/' + 'tag=' + 'chill'
        buildMenu(TheUrl,url,mode)
    elif 'art1' in url:
        TheUrl = younowtags + '0' + '/' + 'tag=' + 'art'
        buildMenu(TheUrl,url,mode)
    elif 'Results' in url:
        #TheUrl = younowtags + '0' + '/' + 'tag=' + searchText
        buildMenu(TheUrl,url,mode)
    elif 'ClearImages' in url:
        clean_database(showdialog=True)

def clean_database(showdialog=True):
    conn = sqlite3.connect(xbmc.translatePath("special://database/Textures13.db"))
    try:
        with conn:
            list = conn.execute("SELECT id, cachedurl FROM texture WHERE url LIKE '%%%s%%';" % ".younow.com")
            for row in list:
                conn.execute("DELETE FROM sizes WHERE idtexture LIKE '%s';" % row[0])
                try: os.remove(xbmc.translatePath("special://thumbnails/" + row[1]))
                except: pass
            conn.execute("DELETE FROM texture WHERE url LIKE '%%%s%%';" % ".younow.com")
            if showdialog:
                util.notifyClear('Finished','YouNow images cleared.')
    except:
        pass

def buildMenu(TheUrl,url,mode):
    params = get_params()
    total = 0
    response = urllib2.urlopen(TheUrl)
    if response and response.getcode() == 200:
        content = response.read()
        videos = util.extractAll(content, 'broadcastId', 'tags')
        for video in videos:
            total = total + 1
            params = {'play':1}
            params['video'] = 'rtmp://pullstream.younow.8686c.com/live/Stream-' + util.extract(video, '":"', '","username"')
            params['image'] = 'https://ynassets.younow.com/broadcastdynamic/live/' + util.extract(video, '":"', '","username"') + '/' + util.extract(video, '":"', '","username"') + '.jpg'
            params['title'] = util.extract(video, '","username":"', '\"')
            params['Page'] = url
            params['Type'] = mode
            params['Num'] = total
            link = util.makeLink(params)
            util.addMenuItem2(params['title'], link, params['image'], params['image'], False)
        #util.endListing()
    else:
        util.showError(ADDON_ID, 'Could not open URL %s to create menu' % (url))

def settings():
    xbmcaddon.Addon().openSettings()

def test():
    params = get_params()
    url = None
    name = None
    mode = None
    iconimage = None
    try:
        url = urllib.unquote_plus(params["url"])
    except:
        pass
    try:
        name = urllib.unquote_plus(params["name"])
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
    if mode == None or url == None or len(url) < 1:
        main()
    elif mode == 1:
        search()
    elif mode == 2:
        start(url,mode)
    elif mode == 3:
        settings()


parameters = util.parseParameters()
if 'play' in parameters:
    params = get_params()
    mode = params['Type']
    url = params['Page']
    total = params['Num']
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