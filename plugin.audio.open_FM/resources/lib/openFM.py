﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Imports
#

import os
import sys
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon

__addon__   = "plugin.audio.open_FM"
__settings__ = xbmcaddon.Addon(id='plugin.audio.open_FM')
names = __settings__.getLocalizedString

#
# Main class
#
class Main:
	def __init__( self ):
		
        #
        # Polecane
        #
		listitem = xbmcgui.ListItem( "Szczególnie Polecamy", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1] ), url = '%s?pol&po_co=%s' % ( sys.argv[ 0 ], "Szczególnie Polecamy" ), listitem=listitem, isFolder=True)		
        #
        # Impreza
        #
		listitem = xbmcgui.ListItem( "Impreza", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?impr&po_co=%s' % ( sys.argv[ 0 ], "Impreza" ), listitem=listitem, isFolder=True)
		#		
        # Pop
        #
		listitem = xbmcgui.ListItem( "Pop", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?pop&po_co=%s' % ( sys.argv[ 0 ], "Pop" ), listitem=listitem, isFolder=True)
        #
        # Hip-Hop/RnB
        #
		listitem = xbmcgui.ListItem( "Hip-Hop/RnB", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?hhrnb&po_co=%s' % ( sys.argv[ 0 ], "Hip-Hop/RnB" ), listitem=listitem, isFolder=True)
        #
        # Rock/Metal
        #
		listitem = xbmcgui.ListItem( "Rock/Metal", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?RM&po_co=%s' % ( sys.argv[ 0 ], "Rock/Metal" ), listitem=listitem, isFolder=True)
        #
        # Alternatywa
        #
		listitem = xbmcgui.ListItem( "Alternatywa", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?alt&po_co=%s' % ( sys.argv[ 0 ], "Alternatywa" ), listitem=listitem, isFolder=True)
        #
        # Reggae
        #
		listitem = xbmcgui.ListItem( "Reggae", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?reG&po_co=%s' % ( sys.argv[ 0 ], "Reggae" ), listitem=listitem, isFolder=True)
        #
        # Elektronika
        #
		listitem = xbmcgui.ListItem( "Elektronika", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?elek&po_co=%s' % ( sys.argv[ 0 ], "Elektronika" ), listitem=listitem, isFolder=True)
        #
        #  Jazz
        #
		listitem = xbmcgui.ListItem( "Jazz", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?jazz&po_co=%s' % ( sys.argv[ 0 ], "Jazz" ), listitem=listitem, isFolder=True)
        #
        #  Inne
        #
		listitem = xbmcgui.ListItem( "Inne", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?inne&po_co=%s' % ( sys.argv[ 0 ], "Inne" ), listitem=listitem, isFolder=True)

        # Disable sorting...
		xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_NONE )
		
        # End of list...
		xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )
