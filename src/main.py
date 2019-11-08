#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import wx
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import time
import random
import json
import win
import player
import var

g_main_win = None
g_tmpPlayerDict = None
g_totalNobody = 0

class knockoutMain(win.knockoutWin):

    def __init__(self, parent):
        win.knockoutWin.__init__(self, parent)
        self.m_bitmap_top16winner.SetBitmap(wx.Bitmap( u"../img/champion.PNG", wx.BITMAP_TYPE_ANY ))
        self.exeBinRoot = os.getcwd()
        self.exeTopRoot = os.path.dirname(self.exeBinRoot)
        exeMainFile = os.path.join(self.exeTopRoot, 'src', 'main.py')
        if not os.path.isfile(exeMainFile):
            self.exeTopRoot = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.playersFilename = os.path.join(self.exeTopRoot, 'bin', 'players.json')
        self._loadExistingPlayers()
        self._createRemainingPlayers()
        self._showRemainingPlayers()

    def _createRemainingPlayers(self):
        global g_tmpPlayerDict
        playerDict = var.getPlayer()
        g_tmpPlayerDict = playerDict.copy()

    def _loadExistingPlayers(self):
        if os.path.isfile(self.playersFilename):
            with open(self.playersFilename, 'r') as fileObj:
                playerDict = json.load(fileObj)
                var.setPlayer(playerDict)
                fileObj.close()

    def _showRemainingPlayers(self):
        global g_tmpPlayerDict
        self.m_textCtrl_playerList.Clear()
        for key in g_tmpPlayerDict:
            if (g_tmpPlayerDict[key] != None) and (g_tmpPlayerDict[key].find('nobody') == -1):
                self.m_textCtrl_playerList.write(g_tmpPlayerDict[key] + "\n")

    def callbackEditPlayer( self, event ):
        playerCfgFrame = player.playerCfg(None)
        playerCfgFrame.Show(True)

    def _showFirstRoundPlayer(self, playerId, playerLoc ):
        if playerLoc == 0:
            self.m_textCtrl_top16a1.Clear()
            self.m_textCtrl_top16a1.write(playerId)
        elif playerLoc == 1:
            self.m_textCtrl_top16a2.Clear()
            self.m_textCtrl_top16a2.write(playerId)
        elif playerLoc == 2:
            self.m_textCtrl_top16b1.Clear()
            self.m_textCtrl_top16b1.write(playerId)
        elif playerLoc == 3:
            self.m_textCtrl_top16b2.Clear()
            self.m_textCtrl_top16b2.write(playerId)
        elif playerLoc == 4:
            self.m_textCtrl_top16c1.Clear()
            self.m_textCtrl_top16c1.write(playerId)
        elif playerLoc == 5:
            self.m_textCtrl_top16c2.Clear()
            self.m_textCtrl_top16c2.write(playerId)
        elif playerLoc == 6:
            self.m_textCtrl_top16d1.Clear()
            self.m_textCtrl_top16d1.write(playerId)
        elif playerLoc == 7:
            self.m_textCtrl_top16d2.Clear()
            self.m_textCtrl_top16d2.write(playerId)
        elif playerLoc == 8:
            self.m_textCtrl_top16e1.Clear()
            self.m_textCtrl_top16e1.write(playerId)
        elif playerLoc == 9:
            self.m_textCtrl_top16e2.Clear()
            self.m_textCtrl_top16e2.write(playerId)
        elif playerLoc == 10:
            self.m_textCtrl_top16f1.Clear()
            self.m_textCtrl_top16f1.write(playerId)
        elif playerLoc == 11:
            self.m_textCtrl_top16f2.Clear()
            self.m_textCtrl_top16f2.write(playerId)
        elif playerLoc == 12:
            self.m_textCtrl_top16g1.Clear()
            self.m_textCtrl_top16g1.write(playerId)
        elif playerLoc == 13:
            self.m_textCtrl_top16g2.Clear()
            self.m_textCtrl_top16g2.write(playerId)
        elif playerLoc == 14:
            self.m_textCtrl_top16h1.Clear()
            self.m_textCtrl_top16h1.write(playerId)
        elif playerLoc == 15:
            self.m_textCtrl_top16h2.Clear()
            self.m_textCtrl_top16h2.write(playerId)
        else:
            pass

    def _clearFirstRoundPlayers(self):
        for i in range(16):
            self._showFirstRoundPlayer('', i)

    def _clearSecondRoundPlayers(self):
        self.m_textCtrl_top16a.Clear()
        self.m_textCtrl_top16a.write('')
        self.m_textCtrl_top16b.Clear()
        self.m_textCtrl_top16b.write('')
        self.m_textCtrl_top16c.Clear()
        self.m_textCtrl_top16c.write('')
        self.m_textCtrl_top16d.Clear()
        self.m_textCtrl_top16d.write('')
        self.m_textCtrl_top16e.Clear()
        self.m_textCtrl_top16e.write('')
        self.m_textCtrl_top16f.Clear()
        self.m_textCtrl_top16f.write('')
        self.m_textCtrl_top16g.Clear()
        self.m_textCtrl_top16g.write('')
        self.m_textCtrl_top16h.Clear()
        self.m_textCtrl_top16h.write('')

    def _showSecondRoundPlayers(self):
        player1Id = self.m_textCtrl_top16a1.GetLineText(0)
        player2Id = self.m_textCtrl_top16a2.GetLineText(0)
        if player1Id.find('nobody') != -1:
            self.m_textCtrl_top16a.write(player2Id)
        else:
            self.m_textCtrl_top16a.write('A Winner')
        player3Id = self.m_textCtrl_top16b1.GetLineText(0)
        player4Id = self.m_textCtrl_top16b2.GetLineText(0)
        if player3Id.find('nobody') != -1:
            self.m_textCtrl_top16b.write(player4Id)
        else:
            self.m_textCtrl_top16b.write('B Winner')
        player5Id = self.m_textCtrl_top16c1.GetLineText(0)
        player6Id = self.m_textCtrl_top16c2.GetLineText(0)
        if player5Id.find('nobody') != -1:
            self.m_textCtrl_top16c.write(player6Id)
        else:
            self.m_textCtrl_top16c.write('C Winner')
        player7Id = self.m_textCtrl_top16d1.GetLineText(0)
        player8Id = self.m_textCtrl_top16d2.GetLineText(0)
        if player7Id.find('nobody') != -1:
            self.m_textCtrl_top16d.write(player8Id)
        else:
            self.m_textCtrl_top16d.write('D Winner')
        player9Id = self.m_textCtrl_top16e1.GetLineText(0)
        player10Id = self.m_textCtrl_top16e2.GetLineText(0)
        if player9Id.find('nobody') != -1:
            self.m_textCtrl_top16e.write(player10Id)
        else:
            self.m_textCtrl_top16e.write('E Winner')
        player11Id = self.m_textCtrl_top16f1.GetLineText(0)
        player12Id = self.m_textCtrl_top16f2.GetLineText(0)
        if player11Id.find('nobody') != -1:
            self.m_textCtrl_top16f.write(player12Id)
        else:
            self.m_textCtrl_top16f.write('F Winner')
        player13Id = self.m_textCtrl_top16g1.GetLineText(0)
        player14Id = self.m_textCtrl_top16g2.GetLineText(0)
        if player13Id.find('nobody') != -1:
            self.m_textCtrl_top16g.write(player14Id)
        else:
            self.m_textCtrl_top16g.write('G Winner')
        player15Id = self.m_textCtrl_top16h1.GetLineText(0)
        player16Id = self.m_textCtrl_top16h2.GetLineText(0)
        if player15Id.find('nobody') != -1:
            self.m_textCtrl_top16h.write(player16Id)
        else:
            self.m_textCtrl_top16h.write('H Winner')

    def _clearOtherRoundPlayers(self):
        self.m_textCtrl_top16ab.Clear()
        self.m_textCtrl_top16ab.write('')
        self.m_textCtrl_top16cd.Clear()
        self.m_textCtrl_top16cd.write('')
        self.m_textCtrl_top16ef.Clear()
        self.m_textCtrl_top16ef.write('')
        self.m_textCtrl_top16gh.Clear()
        self.m_textCtrl_top16gh.write('')

    def _showOtherRoundPlayers(self):
        self.m_textCtrl_top16ab.write('AB')
        self.m_textCtrl_top16cd.write('CD')
        self.m_textCtrl_top16ef.write('EF')
        self.m_textCtrl_top16gh.write('GH')

    def _getTotalNobody(self):
        global g_tmpPlayerDict
        global g_totalNobody
        g_totalNobody = 0
        for key in g_tmpPlayerDict:
            if (g_tmpPlayerDict[key] != None) and (g_tmpPlayerDict[key].find('nobody') != -1):
                g_totalNobody += 1

    def _selectFirstRoundPlayer(self, playerLoc, wantNobody ):
        global g_totalNobody
        isPlayerFound = False
        while not isPlayerFound:
            idx = random.randint(1, 16)
            global g_tmpPlayerDict
            playerId = g_tmpPlayerDict['player'+str(idx)]
            if playerId != None:
                if wantNobody:
                    if g_totalNobody:
                        if playerId.find('nobody') != -1:
                            g_totalNobody -= 1
                        else:
                            continue
                else:
                    if playerId.find('nobody') != -1:
                        continue
                isPlayerFound = True
                self._showFirstRoundPlayer(playerId, playerLoc)
                g_tmpPlayerDict['player'+str(idx)] = None
                self._showRemainingPlayers()

    def callbackCreateKnockout( self, event ):
        global g_totalNobody
        self._clearFirstRoundPlayers()
        self._clearSecondRoundPlayers()
        self._clearOtherRoundPlayers()
        self._createRemainingPlayers()
        self._getTotalNobody()
        if g_totalNobody > 8:
            messageText = ('Less than 8 players')
            wx.MessageBox(messageText, "Error", wx.OK | wx.ICON_INFORMATION)
            return
        wantNobody = True
        nobodyIdxList = random.sample(list(range(0,8)), g_totalNobody)
        for i in range(16):
            wantNobody = False
            if (i % 2 == 0) and ((int(i / 2)) in nobodyIdxList):
                wantNobody = True
            self._selectFirstRoundPlayer(i, wantNobody)
            time.sleep(0.5)
        self._showSecondRoundPlayers()
        self._showOtherRoundPlayers()

    def callbackClearKnockout( self, event ):
        self._clearFirstRoundPlayers()
        self._clearSecondRoundPlayers()
        self._clearOtherRoundPlayers()
        self._createRemainingPlayers()
        self._showRemainingPlayers()

    def _saveExistingPlayers(self):
        playerDict = var.getPlayer()
        with open(self.playersFilename, 'w') as fileObj:
            json.dump(playerDict, fileObj, indent=1)
            fileObj.close()

    def callbackClose( self, event ):
        self._saveExistingPlayers()
        global g_main_win
        g_main_win.Show(False)

if __name__ == '__main__':
    app = wx.App()

    g_main_win = knockoutMain(None)
    g_main_win.SetTitle(u"Knockout v1.0")
    g_main_win.Show()

    app.MainLoop()

