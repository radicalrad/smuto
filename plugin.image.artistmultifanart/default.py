﻿# -*- coding: utf-8 -*-
import xbmcaddon

import urllib, simplejson
import xbmc, xbmcgui, xbmcplugin


class multiImagesSession:

    def addLink(self,name,url):
        liz=xbmcgui.ListItem(name, iconImage="DefaultImage.png")
        return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)

    def LIBRARY_FANARTS(self):
        retval = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "AudioLibrary.GetArtists", "params": {"properties": ["fanart"] }, "id": 1}')
        result = simplejson.loads(retval)
        images = result['result']['artists']
        for img in images:
            title = img.get('label','')
            if not self.addLink(title,img.get('fanart','')): break
        return True

    def SEARCH_FANARTS(self,query):
        url = 'http://pipes.yahoo.com/pipes/pipe.run?_id=c2fa95340901afd0957744024c8a3372&mbid='+query+'&_render=json'
        search_results = urllib.urlopen(url)
        json = simplejson.loads(search_results.read())
        search_results.close()
        images = json['value']['items']
        for img in images:
            title = img.get('title','')
            if not self.addLink(title,img.get('link','')): break
        return True


## XBMC Plugin stuff starts here --------------------------------------------------------            
def get_params():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
        params=sys.argv[2]
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
            params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=splitparams[1]
                            
    return param

def get_mbid_artist(artist):
    artist_url = 'http://search.musicbrainz.org/ws/2/artist/?&fmt=json&query=artist:"'+artist+'"'
    search_results = urllib.urlopen(artist_url)
    json = simplejson.loads(search_results.read())
    search_results.close()
    if json['artist-list']['count'] == 0:
        return None
    else:
        mbid = json['artist-list']['artist'][0]['id']
        return mbid

def get_mbid(artist, song):
    artist=urllib.quote_plus(artist)
    song=urllib.quote_plus(song)
    recording_url = 'http://search.musicbrainz.org/ws/2/recording/?&fmt=json&query=artist:"'+artist+'"%20AND%20recording:"'+song+'"'
    search_results = urllib.urlopen(recording_url)
    json = simplejson.loads(search_results.read())
    search_results.close()
    if json['recording-list']['count'] == 0:
        return get_mbid_artist(artist)
    else:
        recordings = json['recording-list']['recording']
        for recording in recordings:
            mbid = recording['artist-credit']['name-credit'][0]['artist']['id']
        return mbid

def artist_mbid():
    artist=xbmc.Player().getMusicInfoTag().getArtist()
    song=xbmc.Player().getMusicInfoTag().getTitle()
    if len(artist) > 0 and len(song) > 0:
        multiartist=artist.split(' / ')
        if (len(multiartist)) >= 2:
            artist=multiartist[0]
        return get_mbid(artist, song)
    if len(artist) == 0 and len(song) > 0:
        artistsong=song.split(' - ')
        if (len(artistsong))==2:
            artist=artistsong[0]
            song=artistsong[1]
            return get_mbid(artist, song)
    else:
        return None
### Do plugin stuff --------------------------------------------------------------------------
def doPlugin():
    params=get_params()

    mode=None
    name=None

    if xbmc.Player().isPlayingAudio()==False:
        url=None 
    else:
        url=artist_mbid()
    try:
            url=urllib.unquote_plus(params["url"])
    except:
            pass
    try:
            name=urllib.unquote_plus(params["name"])
    except:
            pass
    try:
            mode=int(params["mode"])
    except:
            pass

    print "Mode: "+str(mode)
    print "URL: "+str(url)
    print "Name: "+str(name)


    update_dir = True
    success = True
    cache = True

    mis = multiImagesSession()
    
#    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TRACKNUM)
    
    if mode==None and url==None or len(url)<1:
        mis.LIBRARY_FANARTS()
    else:
        mis.SEARCH_FANARTS(query=url)

    xbmcplugin.endOfDirectory(int(sys.argv[1]),succeeded=success,updateListing=update_dir,cacheToDisc=cache)

doPlugin()