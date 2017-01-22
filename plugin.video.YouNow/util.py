import sys, urllib , os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin

########################################################
younowtags = 'https://api.younow.com/php/api/younow/queue/locale=en/numberOfRecords=50/startFrom='  # /tags=sumtag


def playMedia(title, thumbnail, link, mediaType='Video') :
    """Plays a video

    Arguments:
    title: the title to be displayed
    thumbnail: the thumnail to be used as an icon and thumbnail
    link: the link to the media to be played
    mediaType: the type of media to play, defaults to Video. Known values are Video, Pictures, Music and Programs
    """
    li = xbmcgui.ListItem(label=title, iconImage=thumbnail, thumbnailImage=thumbnail, path=link)
    li.setInfo(type=mediaType, infoLabels={ "Title": title })
    xbmc.Player().play(item=link, listitem=li)

def parseParameters(inputString=sys.argv[2]):
    """Parses a parameter string starting at the first ? found in inputString
    
    Argument:
    inputString: the string to be parsed, sys.argv[2] by default
    
    Returns a dictionary with parameter names as keys and parameter values as values
    """
    parameters = {}
    p1 = inputString.find('?')
    if p1 >= 0:
        splitParameters = inputString[p1 + 1:].split('&')
        for nameValuePair in splitParameters:
            if (len(nameValuePair) > 0):
                pair = nameValuePair.split('=')
                key = pair[0]
                value = urllib.unquote(urllib.unquote_plus(pair[1])).decode('utf-8')
                parameters[key] = value
    return parameters

def notify(addonId, message, timeShown=5000):
    """Displays a notification to the user
    
    Parameters:
    addonId: the current addon id
    message: the message to be shown
    timeShown: the length of time for which the notification will be shown, in milliseconds, 5 seconds by default
    """
    addon = xbmcaddon.Addon(addonId)
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)' % (addon.getAddonInfo('name'), message, timeShown, addon.getAddonInfo('icon')))

mysettings = xbmcaddon.Addon(id = 'plugin.video.YouNow')
home = mysettings.getAddonInfo('path')
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
iconimage = xbmc.translatePath(os.path.join(home, 'icon.png'))
fanart = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))

def notifyClear(header=None, msg='', duration=5000):
    if header is None: header = 'YouNow'
    builtin = "XBMC.Notification(%s,%s, %s, %s)" % (header, msg, duration, icon)
    xbmc.executebuiltin(builtin)

def showError(addonId, errorMessage):
    """
    Shows an error to the user and logs it
    
    Parameters:
    addonId: the current addon id
    message: the message to be shown
    """
    notify(addonId, errorMessage)
    xbmc.log(errorMessage, xbmc.LOGERROR)

def extractAll(text, startText, endText):
    """
    Extract all occurences of a string within text that start with startText and end with endText
    
    Parameters:
    text: the text to be parsed
    startText: the starting tokem
    endText: the ending token
    
    Returns an array containing all occurences found, with tabs and newlines removed and leading whitespace removed
    """
    result = []
    start = 0
    pos = text.find(startText, start)
    while pos != -1:
        start = pos + startText.__len__()
        end = text.find(endText, start)
        result.append(text[start:end].replace('\n', '').replace('\t', '').lstrip())
        pos = text.find(startText, end)
    return result

def extract(text, startText, endText):
    """
    Extract the first occurence of a string within text that start with startText and end with endText
    
    Parameters:
    text: the text to be parsed
    startText: the starting tokem
    endText: the ending token
    
    Returns the string found between startText and endText, or None if the startText or endText is not found
    """
    start = text.find(startText, 0)
    if start != -1:
        start = start + startText.__len__()
        end = text.find(endText, start + 1)
        if end != -1:
            return text[start:end]
    return None
    
def makeLink(params, baseUrl=sys.argv[0]):
    """
    Build a link with the specified base URL and parameters

    Parameters:
    params: the params to be added to the URL
    BaseURL: the base URL, sys.argv[0] by default
    """
    return baseUrl + '?' +urllib.urlencode(dict([k.encode('utf-8'),unicode(v).encode('utf-8')] for k,v in params.items()))

def addMenuItem(caption, link, icon=None, thumbnail=None, folder=False):
    """
    Add a menu item to the xbmc GUI

    Parameters:
    caption: the caption for the menu item
    icon: the icon for the menu item, displayed if the thumbnail is not accessible
    thumbail: the thumbnail for the menu item
    link: the link for the menu item
    folder: True if the menu item is a folder, false if it is a terminal menu item

    Returns True if the item is successfully added, False otherwise
    """
    listItem = xbmcgui.ListItem(unicode(caption), iconImage=icon, thumbnailImage=thumbnail)
    listItem.setInfo(type="Video", infoLabels={ "Title": caption })
    #ListItem.addStreamInfo(type="Video", infoLabels={ "Title": caption })
    #return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=link, listitem=listItem, isFolder=folder)
    #return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=link, listitem=listItem, isFolder=False)
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=link, listitem=listItem, isFolder=False)
    # False plays right. but gives unsupported protocol(plugin) Warning. WTF really.
    # Nevermind fixed that crap in menu2 below.. haha.. in ur face unsupported protocol(plugin)

def addMenuItem2(caption, link, icon=None, thumbnail=None, folder=False):
    """
    Add a menu item to the xbmc GUI

    Parameters:
    caption: the caption for the menu item
    icon: the icon for the menu item, displayed if the thumbnail is not accessible
    thumbail: the thumbnail for the menu item
    link: the link for the menu item
    folder: True if the menu item is a folder, false if it is a terminal menu item
    Returns True if the item is successfully added, False otherwise
    """

    video_streaminfo = {'codec': 'h264','aspect': 1.33,'width': 480,'height': 480,}

    #video_streaminfo = {'codec': 'h264'}
    listItem = xbmcgui.ListItem(unicode(caption), iconImage=icon, thumbnailImage=thumbnail)
    listItem.setInfo(type="Video", infoLabels={ "Title": caption })
    listItem.addStreamInfo('video', video_streaminfo)
    fanart = icon
    listItem.setArt({'fanart': fanart})
    #listItem.setArt({'poster': iconimage})
    #listItem.setArt({'thumb': 'thumbnail.jpg', 'poster': 'poster.jpg' 'fanart': 'fanart.jpg'})
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=link, listitem=listItem, isFolder=False)


def endListing():
    """
    Signals the end of the menu listing
    """
    xbmcplugin.endOfDirectory(int(sys.argv[1]))