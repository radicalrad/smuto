﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import xbmc
import xbmcgui
import xbmcplugin
import urllib
import xbmcaddon

__addon__   = "plugin.audio.open_FM"
__settings__ = xbmcaddon.Addon(id='plugin.audio.open_FM')
ICO_DIR = xbmc.translatePath( os.path.join( __settings__.getAddonInfo('path'), 'resources', 'ico' ) )

class Main:
	def __init__( self ) :
		self.getNames()
	def getNames(self):
		stos=[
			("Bieganie",'http://gr-relay-12.gaduradio.pl/116',os.path.join(ICO_DIR,'bieganie.png')),
			("Fitness",'http://gr-relay-12.gaduradio.pl/65',os.path.join(ICO_DIR,'fitness.png')),
			("Trening",'http://gr-relay-12.gaduradio.pl/101',os.path.join(ICO_DIR,'trening.png'))
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			li.setProperty('mimetype', 'application/octet-stream')
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)
