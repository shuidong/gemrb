# -*-python-*-
# GemRB - Infinity Engine Emulator
# Copyright (C) 2003 The GemRB Project
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
# $Header: /data/gemrb/cvs2svn/gemrb/gemrb/gemrb/GUIScripts/pst/GUIMA.py,v 1.9 2004/08/27 13:36:33 avenger_teambg Exp $


# GUIMA.py - scripts to control map windows from GUIMA and GUIWMAP winpacks

###################################################

import GemRB
from GUIDefines import *

#from GUICommonWindows import OpenCommonWindows, CloseCommonWindows
#import GUICommonWindows

MapWindow = None
WorldMapWindow = None

###################################################
def OpenMapWindow ():
	global MapWindow

	GemRB.HideGUI()

	if MapWindow:
		if WorldMapWindow: OpenWorldMapWindow ()
		
		GemRB.UnloadWindow (MapWindow)
		MapWindow = None
		GemRB.SetVar ("OtherWindow", -1)
		
		GemRB.UnhideGUI ()
		return

	GemRB.LoadWindowPack ("GUIMA")
	MapWindow = Window = GemRB.LoadWindow (3)
	GemRB.SetVar ("OtherWindow", MapWindow)

	# World Map
	Button = GemRB.GetControl (Window, 0)
	GemRB.SetText (Window, Button, 20429)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenWorldMapWindow")

	# Add Note
	Button = GemRB.GetControl (Window, 1)
	GemRB.SetText (Window, Button, 4182)

	# Map Control
	#Button = GemRB.GetControl (Window, 3)
	#GemRB.SetControlPos (Window, Button, 65535, 0)
	GemRB.CreateMapControl (Window, 3, 24, 23, 480, 360)
	Map = GemRB.GetControl (Window, 3)

	Text = GemRB.GetControl (Window, 4)
	GemRB.SetText (Window, Text, "Note text ...")

	MapTable = GemRB.LoadTable( "MAPNAME" )
	MapName = GemRB.GetTableValue(MapTable, GemRB.GetCurrentArea (), 'STRING')
	GemRB.UnloadTable( MapTable )
	
	Label = GemRB.GetControl (Window, 0x10000005)
	GemRB.SetText (Window, Label, MapName)
	#GemRB.SetLabelTextColor (Window, Label, 255, 0, 0)
	# 2 - map name?
	# 3 - map bitmap?
	# 4 - ???
		       
	# Done
	Button = GemRB.GetControl (Window, 5)
	GemRB.SetText (Window, Button, 1403)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenMapWindow")

	GemRB.UnhideGUI ()

def OpenWorldMapWindow ():
	global WorldMapWindow, Travel

	Travel = 1 #allow travel or not, this should be set somehow
	GemRB.HideGUI()

	if WorldMapWindow:
		GemRB.UnloadWindow (WorldMapWindow)
		WorldMapWindow = None
		GemRB.SetVar ("OtherWindow", MapWindow)

		GemRB.UnhideGUI ()
		return

	GemRB.LoadWindowPack ("GUIWMAP")
	WorldMapWindow = Window = GemRB.LoadWindow (0)
	GemRB.SetVar ("OtherWindow", WorldMapWindow)

	#Button = GemRB.GetControl (Window, 4)
	#GemRB.SetControlSize (Window, Button, 0, 0)
	GemRB.CreateWorldMapControl (Window, 4, 0, 62, 640, 418, Travel)
	Map = GemRB.GetControl (Window, 4)
	
	# Done
	Button = GemRB.GetControl (Window, 0)
	GemRB.SetText (Window, Button, 1403)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenWorldMapWindow")

	#GemRB.SetVisible (WorldMapWindow, 1)
	GemRB.UnhideGUI ()



###################################################
# End of file GUIMA.py
