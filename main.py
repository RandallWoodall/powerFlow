# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Randall Woodall, Andres Acosta, Sarbajit Basu
# February 2020
# main.py
# Control center for the power flow program as described by Dr. Ranade.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from admittance import Admittance
from gauss import Gauss

import sys
import numpy as np
import wx
import pandas as pd

# Globals
admittance = None
powerFlow = None


def loadAdmittance(fName):
    frm.SetStatusText('Building admittance matrix...')
    return Admittance(open(fName, 'r+').readlines())


def Quit(e):
    frm.Close()


def Load(e):
    global admittance
    with wx.FileDialog(frm, 'Open Line Information') as fileDialog:
        if fileDialog.ShowModal() == wx.ID_CANCEL:
            return
        fname = fileDialog.GetPath()

    admittance = loadAdmittance(fname)
    wx.StaticText(frm, 1, 'Y = ' + np.array2string(admittance.admittance))#  +
                  #'\n\nZ = ' + np.array2string(np.linalg.inv(admittance.admittance)))
    frm.SetStatusText('')

def Run(e):
    global powerFlow
    if admittance == None:
        return
    # Else
    frm.SetStatusText('Running Gauss-Seidel Power Flow')
    # Takes admittance matrix and known values at each bus
    with wx.FileDialog(frm, 'PQVd Information') as fileDialog:
        if fileDialog.ShowModal() == wx.ID_CANCEL:
            return
        fname = fileDialog.GetPath()
    pqvd = pd.read_csv(fname, header=None)
    powerFlow = Gauss(admittance.admittance, pqvd[0].values, pqvd[1].values, pqvd[2].values, pqvd[3].values)
    powerFlow.solve()
    frm.SetStatusText('')


if __name__ == '__main__':
    app = wx.App()
    frm = wx.Frame(None, title='Power Flow Program', size=(1200, 800))
    frm.SetBackgroundColour(wx.Colour(wx.WHITE))
    frm.Show()
    frm.CreateStatusBar()
    menubar = wx.MenuBar()
    fileMenu = wx.Menu()
    menubar.Append(fileMenu, '&File')
    load_admittance_button = fileMenu.Append(wx.ID_FILE, 'Load Lines', 'Load Lines into Admittance')
    gauss_run_button = fileMenu.Append(wx.ID_FILE1, 'Run Gauss', 'Runs Gauss Power Flow on Admittance Matrix')
    exit_button = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit Application')
    frm.Bind(wx.EVT_MENU, Quit, exit_button)
    frm.Bind(wx.EVT_MENU, Load, load_admittance_button)
    frm.Bind(wx.EVT_MENU, Run, gauss_run_button)
    frm.SetMenuBar(menubar)

    frm.SetStatusText('')

    np.set_printoptions(linewidth=5000)

    app.MainLoop()
