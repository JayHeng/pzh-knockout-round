#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

g_playerDict = {'player1':u"nobody",
                'player2':u"nobody",
                'player3':u"nobody",
                'player4':u"nobody",
                'player5':u"nobody",
                'player6':u"nobody",
                'player7':u"nobody",
                'player8':u"nobody",
                'player9':u"nobody",
                'player10':u"nobody",
                'player11':u"nobody",
                'player12':u"nobody",
                'player13':u"nobody",
                'player14':u"nobody",
                'player15':u"nobody",
                'player16':u"nobody",
                 }

def getPlayer():
    global g_playerDict
    return g_playerDict

def setPlayer( *args ):
    global g_playerDict
    g_playerDict = args[0]
