#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import win
import var

class playerCfg(win.playerWin):

    def __init__(self, parent):
        win.playerWin.__init__(self, parent)

    def callbackAdd( self, event ):
        playerDict = var.getPlayer()
        playerId = self.m_textCtrl_playerId.GetLineText(0)
        if playerId != '':
            isNewPlayer = True
            isPlayerSpaceFull = True
            for key in playerDict:
                if playerDict[key] == playerId:
                    isNewPlayer = False
                    break
            if isNewPlayer:
                for key in playerDict:
                    if playerDict[key].find('nobody') != -1:
                        playerDict[key] = playerId
                        isPlayerSpaceFull = False
                        break
                if isPlayerSpaceFull:
                    messageText = ('The players are full')
                    wx.MessageBox(messageText, "Error", wx.OK | wx.ICON_INFORMATION)
                    return
            var.setPlayer(playerDict)
        self.Show(False)

    def callbackRemove( self, event ):
        playerDict = var.getPlayer()
        playerId = self.m_textCtrl_playerId.GetLineText(0)
        if playerId != '':
            for key in playerDict:
                if playerDict[key] == playerId:
                    playerDict[key] = u"nobody"
                    break
            var.setPlayer(playerDict)
        self.Show(False)
