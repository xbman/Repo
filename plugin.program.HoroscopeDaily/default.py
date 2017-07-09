import urllib2, re, xbmc, xbmcgui, xbmcaddon, xbmcplugin, os

#get actioncodes from keymap.xml
ACTION_PREVIOUS_MENU = 10
ACTION_SELECT_ITEM = 7

aname = 'plugin.program.HoroscopeDaily'
ooo = xbmcaddon.Addon(aname)

class MyClass(xbmcgui.Window):
    def __init__(self):
        self.image_dir = xbmc.translatePath(os.path.join(ooo.getAddonInfo('path'), "resources", "images"))
        self.addControl(xbmcgui.ControlImage(0, 0, 1280, 720, self.image_dir + '/astrology_0.jpg', aspectRatio=0))
        self.addControl(xbmcgui.ControlImage(20,555,90,90, self.image_dir + '/icon_aries.png'))
        self.addControl(xbmcgui.ControlImage(120,515,90,90, self.image_dir + '/icon_taurus.png'))
        self.addControl(xbmcgui.ControlImage(223,485,90,90, self.image_dir + '/icon_gemini.png'))
        self.addControl(xbmcgui.ControlImage(327,463,90,90, self.image_dir + '/icon_cancer.png'))
        self.addControl(xbmcgui.ControlImage(430,447,90,90, self.image_dir + '/icon_leo.png'))
        self.addControl(xbmcgui.ControlImage(535,439,90,90, self.image_dir + '/icon_virgo.png'))
        self.addControl(xbmcgui.ControlImage(640,438,90,90, self.image_dir + '/icon_libra.png'))
        self.addControl(xbmcgui.ControlImage(743,445,90,90, self.image_dir + '/icon_scorpio.png'))
        self.addControl(xbmcgui.ControlImage(845,460,90,90, self.image_dir + '/icon_sagittarius.png'))
        self.addControl(xbmcgui.ControlImage(950,482,90,90, self.image_dir + '/icon_capricorn.png'))
        self.addControl(xbmcgui.ControlImage(1055,512,90,90, self.image_dir + '/icon_aquarius.png'))
        self.addControl(xbmcgui.ControlImage(1162,552,90,90, self.image_dir + '/icon_pisces.png'))

        #### Button and text Colors: Focused Color / Text Color / bottom text color. / heading-date - line1 - line2
        # Color code examples: 0xFFCCFFFF = #CCFFFF
        fColor = "0xFFCCFFFF"; tColor = "0xFF003366"; btcolor = "0xFFCCFFFF"; headingcolor = "0xFFCCCC99"; L1color = "0xFFCCFFFF"; L2color = "0xFFCCFFFF";
        ### Font SiZeS. 1:top left/ 2:bottom / 3:top date / 4: horo line1 / 5:horo line2
        fsize1 = "font13"; fsize2 = "font13"; fsize3 = "font30"; fsize4 = "font20"; fsize5 = "font25";


        # Top left label: * Horocope Daily * ControlLabel
        self.strActionInfo = xbmcgui.ControlLabel(12, 20, 220, 200, '', fsize1, '0xFF993366')
        self.addControl(self.strActionInfo)
        self.strActionInfo.setLabel('* Horoscope Daily *')
        self.strActionInfo = xbmcgui.ControlLabel(95, 43, 220, 200, '', 'font1', '0xFF444444')
        self.addControl(self.strActionInfo)
        self.strActionInfo.setLabel('by: xbman.')

        # Bottom onclick message. ControlLabel
        self.strActionInfo = xbmcgui.ControlLabel(400, 610, 800, 400, '', 'fsize2', btcolor)
        self.addControl(self.strActionInfo)

        ### Add horoscope date from site... Your Daily Horoscope for...
        self.strActionInfoHeading = xbmcgui.ControlLabel(340, 50, 850, 100, '', fsize3, headingcolor)
        self.addControl(self.strActionInfoHeading)

        ### Add horoscope line 1 from site. ControlTextBox wraps text.. ControlLabel does not.
        self.strActionInfoHoros1 =  xbmcgui.ControlTextBox(20, 100, 1260, 100, 'fsize4', L1color)
        self.addControl(self.strActionInfoHoros1)

        ### Add horoscope line 2 from site. ControlTextBox wraps text.. ControlLabel does not.
        self.strActionInfoHoros2 = xbmcgui.ControlTextBox(20, 190, 1260, 200, 'fsize5', L2color)
        self.addControl(self.strActionInfoHoros2)

        ### Add Buttons.
        self.button0 = xbmcgui.ControlButton(25, 650, 180, 30, "[B]Aries[/B]",'','font50',textColor=tColor,focusedColor=fColor)
        self.addControl(self.button0)
        self.button1 = xbmcgui.ControlButton(115, 615, 180, 30, "[B]Taurus[/B]",'','font50',textColor=tColor,focusedColor=fColor)
        self.addControl(self.button1)
        self.button2 = xbmcgui.ControlButton(220, 578, 180, 30, "[B]Gemini[/B]",'','font50',textColor=tColor,focusedColor=fColor)
        self.addControl(self.button2)
        self.button3 = xbmcgui.ControlButton(320, 553, 180, 30, "[B]Cancer[/B]",'','font50',textColor=tColor,focusedColor=fColor)
        self.addControl(self.button3)
        self.button4 = xbmcgui.ControlButton(445, 533, 180, 30, "[B]Leo[/B]",'','font50',textColor=tColor,focusedColor=fColor)
        self.addControl(self.button4)
        self.button5 = xbmcgui.ControlButton(540, 523, 180, 30, "[B]Virgo[/B]",'','font50',textColor=tColor,focusedColor=fColor)
        self.addControl(self.button5)
        self.button6 = xbmcgui.ControlButton(643, 525, 180, 30, "[B]Libra[/B]",'','font50',textColor=tColor,focusedColor=fColor)
        self.addControl(self.button6)
        self.button7 = xbmcgui.ControlButton(735, 530, 180, 30, "[B]Scorpio[/B]",'','font50',textColor=tColor,focusedColor=fColor)
        self.addControl(self.button7)
        self.button8 = xbmcgui.ControlButton(815, 553, 180, 30, "[B]Sagittarius[/B]",'','font50',textColor=tColor,focusedColor=fColor)
        self.addControl(self.button8)
        self.button9 = xbmcgui.ControlButton(920, 575, 180, 30, "[B]Capricorn[/B]",'','font50',textColor=tColor,focusedColor=fColor)
        self.addControl(self.button9)
        self.button10 = xbmcgui.ControlButton(1033, 610, 180, 30, "[B]Aquarius[/B]",'','font50',textColor=tColor,focusedColor=fColor)
        self.addControl(self.button10)
        self.button11 = xbmcgui.ControlButton(1155, 647, 180, 30, "[B]Pisces[/B]",'','font50',textColor=tColor,focusedColor=fColor)
        self.addControl(self.button11)

        ## set focus on first button.
        self.setFocus(self.button0)

        ##### ADD MOVEMENT to move to each button.
        self.button0.controlRight(self.button1)
        self.button1.controlRight(self.button2)
        self.button2.controlRight(self.button3)
        self.button3.controlRight(self.button4)
        self.button4.controlRight(self.button5)
        self.button5.controlRight(self.button6)
        self.button6.controlRight(self.button7)
        self.button7.controlRight(self.button8)
        self.button8.controlRight(self.button9)
        self.button9.controlRight(self.button10)
        self.button10.controlRight(self.button11)
        self.button11.controlRight(self.button0)

        self.button0.controlLeft(self.button11)
        self.button1.controlLeft(self.button0)
        self.button2.controlLeft(self.button1)
        self.button3.controlLeft(self.button2)
        self.button4.controlLeft(self.button3)
        self.button5.controlLeft(self.button4)
        self.button6.controlLeft(self.button5)
        self.button7.controlLeft(self.button6)
        self.button8.controlLeft(self.button7)
        self.button9.controlLeft(self.button8)
        self.button10.controlLeft(self.button9)
        self.button11.controlLeft(self.button10)

    def GetScope(self, horos):
        BROWSER_HEADER = "Mozilla/5.0 (Windows NT 6.0; rv:52.0) Gecko/20100101 Firefox/52.0"
        BROWSER_REFERER = "https://www.horoscopedates.com/daily-horoscope/"
        url = "https://www.horoscopedates.com/daily-horoscope/" + horos + "/"
        req = urllib2.Request(url, headers={'Referer' : BROWSER_REFERER, 'User-Agent' : BROWSER_HEADER})
        page=urllib2.urlopen(req)
        data=page.read()
        header = re.compile('<h3>(.*?)\</h3>').findall(data)
        scope = re.compile('<p>(.*?)\</p>').findall(data)
        self.strActionInfoHeading.setLabel(str(header[0]))
        mod1 = str(scope[0])
        self.strActionInfoHoros1.setText(mod1)
        mod2 = str(scope[1])
        self.strActionInfoHoros2.setText(mod2)

    def onControl(self, control):
        if control == self.button0:
            ###self.message('Aries','Aries')
            self.strActionInfo.setLabel('ARIES: March 21 - April 19[CR][B]The Ram. A Fire sign, ruled by Mars...[/B]')
            horos = 'aries'; self.GetScope(horos);
        if control == self.button1:
            self.strActionInfo.setLabel('TAURUS: April 20 - May 20[CR][B]The Bull. An Earth sign, ruled by Venus...[/B]')
            horos = 'taurus'; self.GetScope(horos);
        if control == self.button2:
            self.strActionInfo.setLabel('GeMINI: May 21 - June 20[CR][B]The Twins. An Air sign, ruled by Mercury...[/B]')
            horos = 'gemini'; self.GetScope(horos);
        if control == self.button3:
            self.strActionInfo.setLabel('CANCER: June 21 - July 22[CR][B]The Crab. An Water sign, ruled by the Moon...[/B]')
            horos = 'cancer'; self.GetScope(horos);
        if control == self.button4:
            self.strActionInfo.setLabel('LEO: July 23 - August 22[CR][B]The Lion. A Fire sign, ruled by the Sun...[/B]')
            horos = 'leo'; self.GetScope(horos);
        if control == self.button5:
            self.strActionInfo.setLabel('VIRGO: August 23 - September 22[CR][B]The Maiden. An Earth sign, ruled by Mercury...[/B]')
            horos = 'virgo'; self.GetScope(horos);
        if control == self.button6:
            self.strActionInfo.setLabel('LIBRA: September 23 - October 22[CR][B]The Scales. An Air sign, ruled by Venus...[/B]')
            horos = 'libra'; self.GetScope(horos);
        if control == self.button7:
            self.strActionInfo.setLabel('SCORPIO: October 23 - November 21[CR][B]The Scorpion. A Water sign, ruled by Pluto...[/B]')
            horos = 'scorpio'; self.GetScope(horos);
        if control == self.button8:
            self.strActionInfo.setLabel('SAGITTARIUS: November 22 - December 21[CR][B]The Centaur. A Fire sign, ruled by Jupiter...[/B]')
            horos = 'sagittarius'; self.GetScope(horos);
        if control == self.button9:
            self.strActionInfo.setLabel('CAPRICORN: December 22 - January 19[CR][B]The Mountain Goat. An Earth sign, ruled by Saturn...[/B]')
            horos = 'capricorn'; self.GetScope(horos);
        if control == self.button10:
            self.strActionInfo.setLabel('AQUARIUS: January 20 -February 18[CR][B]The Man who Carries Water. An Air sign, ruled by Uranus...[/B]')
            horos = 'aquarius'; self.GetScope(horos);
        if control == self.button11:
            self.strActionInfo.setLabel('PISCES: February 19 - March 20[CR][B]The Fish. A Water sign, ruled by Neptune...[/B]')
            horos = 'pisces'; self.GetScope(horos);

    def message(self, title, message):
        dialog = xbmcgui.Dialog()
        dialog.ok(title, message)

def onAction(self, action):
    if action == ACTION_PREVIOUS_MENU:
        self.close()
    if action == ACTION_SELECT_ITEM:
        self.strActionInfo.reset()

mydisplay = MyClass()
mydisplay .doModal()
del mydisplay