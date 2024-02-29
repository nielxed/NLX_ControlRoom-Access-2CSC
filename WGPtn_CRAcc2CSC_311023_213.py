# NLX Swrd: CRAcc2CSC (codename(as beta): Lothlorien)
# (Last beta)Version: Gil-Galad
import flet as nlxFT
# Vrfr never used so it is comented out 09012024_1
import Cgpt_VerAccPrmk_031223_cl as VrfrPrmk
# import Cgpt_ENG101_71123_cl_Alt1 as CSCRldr
import Cgpt_ENGPrmk_04122023_cl as CSCRldr_Prmk
import Cgpt_CamDict_271123_cl as CamIncrement
import Cgpt_VerAcc2AllPrmk_10012024 as FSSClass
# import Cgpt_ClsOfAssts_16012024 as assetClass
import NLXShield_CamDB_29124 as CamDB
import time
import datetime
import logging
"""
The software loads Flutter libraries over Flet in main window design.
Purpoce/Description/Functions
Build version are mentioned in a snack-bar form. Done
A status bar is inorporated to comment the users actions and direct with information and tips. Done
The user is placed in a panel form design with the sites separated with page selection. Done
The pages contain asset funtions in Elevated Button format. Done
Match site names to ExacqVision configured sites. Done
Function tooltips offer more information to help with the identification of the asset. Done
Asset search engine. Pending
To enable actions on these assets valid credential will have to be provided through interractive
modal. Done
Credential encryption. Pending
2FA access to TACACs.net through Google Authenticator App. Pending
Enabled functions shut inline power for the asset for 5 seconds and and then re-feed. Done
If an asset is cycled for a third time the asset is disabled and the user is notified to 
open a ticket for further support. Done - Untested
Before action, a notification modal should worn user which asset will be power cycled (by description)
and the user will have to confirm this action. Done
The software dimentions are constricted as much as possible to fit in most screen sizes. Done
On-screen session logger for performed actions. Done
Export recorded actions to text file. Done
"""

# Main Flet software for CR actions described in footer refference.
"""
This main soft is of type NLXSword
"""

class Data:
    def __init__(self) -> None:
        self.select = ""

currentCam = Data()

class RLDCams:
    def __init__(self) -> None:
        self.select = ""

RLDCamsCollector = RLDCams()
counter_manager = CamIncrement.CamCounterManager()

# Global definistions START
MSG1 = "Invalid username and/or password!"
MSG2 = "Please log in before you can perform actions."
userNameCR = ""                                                                                                             # Initialize a username string glb
userNameCPT = nlxFT.TextField(label="Username", width=250, border_color="white")                                            # Password text-field defined off-definition glb
global passWordCR
passWordCR = ""                                                                                                             # Initialize a password string glb
passWordCPT = nlxFT.TextField(label="Password", width=250, border_color="white", password=True, can_reveal_password=True)   # Password text-field defined off-definition glb and set to hidden
CRStatus = nlxFT.Text(value="notInit")
status = nlxFT.Text(value="System ready.", size= 15, color="white")
userComment = nlxFT.Text(value="Please Login To Perform Actions", style=nlxFT.TextThemeStyle.TITLE_SMALL, weight=nlxFT.FontWeight.BOLD, color="white")
emptMessage = "No cameras have been rebooted yet"
# Global definistions END

# Declare text-files
current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y%m%d_%H%M%S")
session_loggfile = f"CamRldLog_{formatted_datetime}.txt"

# Global setters START
def setChecker_Out():
    global inMain_loginChecker
    inMain_loginChecker = 0

def setChecker_In():
    global inMain_loginChecker
    inMain_loginChecker = 1

# User defined username
def setUserName_Global(USR):
    global inGlobal_User
    inGlobal_User = USR

# User defined password
def setPassWord_Global(PSW):
    global inGlobal_PassWord
    inGlobal_PassWord = PSW

# IP Address for the CSC asset the running instance will be connecting on
def setHost4Cam_Global(HST):
    global inGlobal_Host
    inGlobal_Host = HST

# The switchport interface of the asset that the current instance will be reloading
def setInt4Cam_Global(INT):
    global inGlobal_Interface
    inGlobal_Interface = INT

# The description (in script string) for the camera the current instance is targeting  
def setDesc4Cam_Global(DESC):
    global inGlobal_CamDescription
    inGlobal_CamDescription = DESC

def sureVAR_Global(SR):
    global rbtCSCInt
    rbtCSCInt = 0

def RLDCamsStory(RLDCamAdd2Story):
    global reloadedCamsStory
    reloadedCamsStory = RLDCamAdd2Story

def RLDCamsAtLeast1(AL1):
    global DefaultOrStory
    DefaultOrStory = AL1

# The global variable that increases reload actions for the dictionary class "Cgpt_CamDict_"
def setKeyInrmt(KEY):
    global KeyReloaded
    KeyReloaded = KEY

# Post implemented from SBarTstFletExe_01.py - in root
# --------------------
toSearch_VAR = ""
searchList_RES = []

def toSearch_Global(SRC): # Value in inGlobal_Search
    global inGlobal_Search
    inGlobal_Search = SRC

def searchCount_VAR(count_VAR): # Value in searchCount
    global searchCount
    searchCount = count_VAR

def shortListNavi_VAR(navi_VAR): # Value in naviCount
    global naviCount
    naviCount = navi_VAR

def globalList_VAR(composed):
    global searchList_RES
    searchList_RES = composed

def moreOrLess_VAR(moreLess):
    global moreOrLess
    moreOrLess = moreLess
moreOrLess_VAR(0)

textLst = []
for astTemp in CamDB.assetLst:
    textLst.append(nlxFT.Text(astTemp.label, style=nlxFT.TextThemeStyle.BODY_MEDIUM))

globalList_VAR("text")

def countRes():
    searchCount_VAR(0)
    print(f"(Line 188) Character to search: {inGlobal_Search}")
    for i in CamDB.assetLst:
        if inGlobal_Search in i.label:
            print(f"(Line 191) Label: {i.label}")
            searchCount_VAR(searchCount + 1)
    print(f"(Line 193) Assets matched: {searchCount}")
# --------------------

RLDCamsAtLeast1(0)
RLDCamsStory("Actions completed in current session:")

def Pozer():
    time.sleep(0.5)
# Global setters END

# Global definitions START
def reset_Creds():
    userNameCPT.value = ""
    passWordCPT.value = ""
# Global definitions END

# Main page definition START
def main(page: nlxFT.Page):
    # Page initializers
    page.bgcolor = "#fdfdfd"
    page.padding = 10
    # page.window_height = 1200
    page.window_height = 960
    page.window_width = 1200
    page.window_maximizable = False
    page.window_maximized = False
    page.window_resizable = False
    page.window_center()
    # page.title = "CR Site Camera Reload"
    page.title = "WG Control Room Camera Reload"

    # Post implemented from SBarTstFletExe_01.py - in root
    # --------------------
    # Search initializers
    page.bgcolor = "#fdfdfd"
    page.window_height = 940
    page.window_width = 1200
    page.window_maximizable = False
    page.window_maximized = False
    page.window_resizable = False
    page.window_center()

    # Search button list
    Brdr = nlxFT.Divider(color=nlxFT.colors.AMBER, opacity=0)
    btnList = [nlxFT.Divider(color=nlxFT.colors.AMBER)]
    pointerList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
    print(Brdr)
    for i in range(1, 12):
        btnList.append(Brdr)
        print(f"(Line 153) Devider {i} appended in list")
    print(f"(Line 154) Elements in list btnList: {len(btnList)}")
    print(f"(Line 155) Button list element 0 type: {type(btnList[0])}")
    for j in btnList:
        print("Count")

    def reIniSearchList():
        for i in range(0, 12):
            btnList[i] = Brdr

    # Search definitions
    # def reIniSearchList():
    #     for i in range(0, 11):
    #         btnList[i] = Brdr

    # inMain initializers
    setChecker_Out()
    setDesc4Cam_Global("")
    Pozer()
    time.sleep(0.2)

    def open_nskBar_version(e):
        # The "show_close_icon" operator seems to be buggy and causes some issues for the snack bar post-compilation. Removed for test.
        page.snack_bar = nlxFT.SnackBar(nlxFT.Text(f"Version: 2.3.1(67) Compiled: 154539022024"), duration=4500)
        page.snack_bar.open = True
        page.update()

    def app_Header_Brand():
        return nlxFT.Container(
            content=nlxFT.IconButton(
                nlxFT.icons.CAMERA_INDOOR_ROUNDED,
                icon_color="white",
                on_click=open_nskBar_version
            )
        )

    def app_Header_Avatar():
        return nlxFT.Container(
            content=nlxFT.IconButton(nlxFT.icons.PERSON_2_ROUNDED, on_click=open_dlg_UserLogin, icon_color="white")
        )

    def login_dlg_UserLogin(e):
        page.banner.open = False
        userNameCR = userNameCPT.value
        # passWordCR = passWordCPT.value
        host = "192.168.77.13"
        port = 22  # or the port you use for SSH
        timeout = 10  # you can adjust the timeout value if necessary
        close_dlg_UserLogin_onLogin(e)
        status.value = "Login in progress... Please Wait!"
        page.update()
        time.sleep(3)

        ssh_verifier = VrfrPrmk.CiscoSSHTester(host, userNameCPT.value, passWordCPT.value, port, timeout)
        if ssh_verifier.test_connectivity():
            status.value = f"User {userNameCR} logged in successfully!"
            userComment.value = f"Welcome {userNameCR}"
            page.update()
            setUserName_Global(userNameCPT.value)
            setPassWord_Global(passWordCPT.value)
            setChecker_In()
            reset_Creds()
        else:
            show_banner_click(e)
            reset_Creds()
            # reset_BaseCreds()
            status.value = "Unable to login. Please try again!"
            page.update()

        userNameCPT.value = ""
        passWordCPT.value = ""

    # userNameCPT = nlxFT.TextField(label="Username", width=250, border_color="white", on_submit=login_dlg_UserLogin)
    userNameCPT = nlxFT.TextField(label="Username", width=250, border_color="white", 
                                  on_submit=login_dlg_UserLogin, capitalization=nlxFT.TextCapitalization.CHARACTERS,
                                  helper_text="Text Auto-Capitalized")
    passWordCPT = nlxFT.TextField(label="Password", width=250, border_color="white", password=True, can_reveal_password=True, on_submit=login_dlg_UserLogin, 
                                  helper_text=" ")

    # HQ 1st Floor Server Room  key definitions
    def rbt_CSC_HQ(e):
        pass

    def rbt_CSC_11101(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF46")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/1")
            setKeyInrmt("rbt_CSC_11101")
            open_dlg_modal_VER(e)

    def rbt_CSC_11103(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.66")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/3")
            setKeyInrmt("rbt_CSC_11103")
            open_dlg_modal_VER(e)

    def rbt_CSC_11104(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.61")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/4")
            setKeyInrmt("rbt_CSC_11104")
            open_dlg_modal_VER(e)

    def rbt_CSC_11105(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF59")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/5")
            setKeyInrmt("rbt_CSC_11105")
            open_dlg_modal_VER(e)

    def rbt_CSC_11106(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.51")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/6")
            setKeyInrmt("rbt_CSC_11106")
            open_dlg_modal_VER(e)

    def rbt_CSC_11108(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.42")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/8")
            setKeyInrmt("rbt_CSC_11108")
            open_dlg_modal_VER(e)

    def rbt_CSC_11109(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF63")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/9")
            setKeyInrmt("rbt_CSC_11109")
            open_dlg_modal_VER(e)

    def rbt_CSC_111011(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF49")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/11")
            setKeyInrmt("rbt_CSC_111011")
            open_dlg_modal_VER(e)

    def rbt_CSC_111012(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.68")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/12")
            setKeyInrmt("rbt_CSC_111012")
            open_dlg_modal_VER(e)

    def rbt_CSC_111013(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.54")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/13")
            setKeyInrmt("rbt_CSC_111013")
            open_dlg_modal_VER(e)

    def rbt_CSC_111015(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF48")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/15")
            setKeyInrmt("rbt_CSC_111015")
            open_dlg_modal_VER(e)

    def rbt_CSC_111017(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF62")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/17")
            setKeyInrmt("rbt_CSC_111017")
            open_dlg_modal_VER(e)

    def rbt_CSC_111019(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF47")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/19")
            setKeyInrmt("rbt_CSC_111019")
            open_dlg_modal_VER(e)

    def rbt_CSC_111025(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.57")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/25")
            setKeyInrmt("rbt_CSC_111025")
            open_dlg_modal_VER(e)

    def rbt_CSC_111028(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.19")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/28")
            setKeyInrmt("rbt_CSC_111028")
            open_dlg_modal_VER(e)

    def rbt_CSC_111029(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.9")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/29")
            setKeyInrmt("rbt_CSC_111029")
            open_dlg_modal_VER(e)

    def rbt_CSC_111031(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.15")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/31")
            setKeyInrmt("rbt_CSC_111031")
            open_dlg_modal_VER(e)

    def rbt_CSC_111033(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.10")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/33")
            setKeyInrmt("rbt_CSC_111033")
            open_dlg_modal_VER(e)

    def rbt_CSC_111034(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.6")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/34")
            setKeyInrmt("rbt_CSC_111034")
            open_dlg_modal_VER(e)

    def rbt_CSC_111035(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.1")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/35")
            setKeyInrmt("rbt_CSC_111035")
            open_dlg_modal_VER(e)

    def rbt_CSC_111036(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.2")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/36")
            setKeyInrmt("rbt_CSC_111036")
            open_dlg_modal_VER(e)

    def rbt_CSC_111037(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.11")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/37")
            setKeyInrmt("rbt_CSC_111037")
            open_dlg_modal_VER(e)

    def rbt_CSC_111040(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.13")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/40")
            setKeyInrmt("rbt_CSC_111040")
            open_dlg_modal_VER(e)

    def rbt_CSC_111042(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.17")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/42")
            setKeyInrmt("rbt_CSC_111042")
            open_dlg_modal_VER(e)

    def rbt_CSC_111043(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.4")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/43")
            setKeyInrmt("rbt_CSC_111043")
            open_dlg_modal_VER(e)

    def rbt_CSC_111044(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.18")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/44")
            setKeyInrmt("rbt_CSC_111044")
            open_dlg_modal_VER(e)

    def rbt_CSC_111045(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.14")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/45")
            setKeyInrmt("rbt_CSC_111045")
            open_dlg_modal_VER(e)

    def rbt_CSC_111046(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.21")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/46")
            setKeyInrmt("rbt_CSC_111046")
            open_dlg_modal_VER(e)

    def rbt_CSC_111048(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.20")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi1/0/48")
            setKeyInrmt("rbt_CSC_111048")
            open_dlg_modal_VER(e)

    def rbt_CSC_11202(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.28")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/2")
            setKeyInrmt("rbt_CSC_11202")
            open_dlg_modal_VER(e)

    def rbt_CSC_11203(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF65")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/3")
            setKeyInrmt("rbt_CSC_11203")
            open_dlg_modal_VER(e)

    def rbt_CSC_11204(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.59")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/4")
            setKeyInrmt("rbt_CSC_11204")
            open_dlg_modal_VER(e)

    # QA - Added
    def rbt_CSC_11205(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF64")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/5")
            setKeyInrmt("rbt_CSC_11205")
            open_dlg_modal_VER(e)

    def rbt_CSC_11206(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.25")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/6")
            setKeyInrmt("rbt_CSC_11206")
            open_dlg_modal_VER(e)

    def rbt_CSC_11208(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF58")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/8")
            setKeyInrmt("rbt_CSC_11208")
            open_dlg_modal_VER(e)

    def rbt_CSC_11209(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.38")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/9")
            setKeyInrmt("rbt_CSC_11209")
            open_dlg_modal_VER(e)

    def rbt_CSC_112010(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.37")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/10")
            setKeyInrmt("rbt_CSC_112010")
            open_dlg_modal_VER(e)

    def rbt_CSC_112011(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.40")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/11")
            setKeyInrmt("rbt_CSC_112011")
            open_dlg_modal_VER(e)

    def rbt_CSC_112013(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF61")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/13")
            setKeyInrmt("rbt_CSC_112013")
            open_dlg_modal_VER(e)

    def rbt_CSC_112014(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.55")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/14")
            setKeyInrmt("rbt_CSC_112014")
            open_dlg_modal_VER(e)

    def rbt_CSC_112016(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.26")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/16")
            setKeyInrmt("rbt_CSC_112016")
            open_dlg_modal_VER(e)

    def rbt_CSC_112017(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.58")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/17")
            setKeyInrmt("rbt_CSC_112017")
            open_dlg_modal_VER(e)

    def rbt_CSC_112020(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.32")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/20")
            setKeyInrmt("rbt_CSC_112020")
            open_dlg_modal_VER(e)

    def rbt_CSC_112021(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF60")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/21")
            setKeyInrmt("rbt_CSC_112021")
            open_dlg_modal_VER(e)

    def rbt_CSC_112022(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.52")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/22")
            setKeyInrmt("rbt_CSC_112022")
            open_dlg_modal_VER(e)

    def rbt_CSC_112023(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.56")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/23")
            setKeyInrmt("rbt_CSC_112023")
            open_dlg_modal_VER(e)

    def rbt_CSC_112024(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.35")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/24")
            setKeyInrmt("rbt_CSC_112024")
            open_dlg_modal_VER(e)

    def rbt_CSC_112025(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.60")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/25")
            setKeyInrmt("rbt_CSC_112025")
            open_dlg_modal_VER(e)

    def rbt_CSC_112026(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.24")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/26")
            setKeyInrmt("rbt_CSC_112026")
            open_dlg_modal_VER(e)

    def rbt_CSC_112027(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.34")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/27")
            setKeyInrmt("rbt_CSC_112027")
            open_dlg_modal_VER(e)

    def rbt_CSC_112028(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.16")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/28")
            setKeyInrmt("rbt_CSC_112028")
            open_dlg_modal_VER(e)

    def rbt_CSC_112029(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.53")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/29")
            setKeyInrmt("rbt_CSC_112029")
            open_dlg_modal_VER(e)

    def rbt_CSC_112030(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.43")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/30")
            setKeyInrmt("rbt_CSC_112030")
            open_dlg_modal_VER(e)

    def rbt_CSC_112031(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.12")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/31")
            setKeyInrmt("rbt_CSC_112031")
            open_dlg_modal_VER(e)

    def rbt_CSC_112032(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.22")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/32")
            setKeyInrmt("rbt_CSC_112032")
            open_dlg_modal_VER(e)

    def rbt_CSC_112033(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.67")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/33")
            setKeyInrmt("rbt_CSC_112033")
            open_dlg_modal_VER(e)

    def rbt_CSC_112034(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.30")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/34")
            setKeyInrmt("rbt_CSC_112034")
            open_dlg_modal_VER(e)

    def rbt_CSC_112035(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.3")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/35")
            setKeyInrmt("rbt_CSC_112035")
            open_dlg_modal_VER(e)

    def rbt_CSC_112036(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.5")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/36")
            setKeyInrmt("rbt_CSC_112036")
            open_dlg_modal_VER(e)

    def rbt_CSC_112038(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.41")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/38")
            setKeyInrmt("rbt_CSC_112038")
            open_dlg_modal_VER(e)

    def rbt_CSC_112040(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.48")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/40")
            setKeyInrmt("rbt_CSC_112040")
            open_dlg_modal_VER(e)

    def rbt_CSC_112042(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.49")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi2/0/42")
            setKeyInrmt("rbt_CSC_112042")
            open_dlg_modal_VER(e)

    def rbt_CSC_113011(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.23")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi3/0/11")
            setKeyInrmt("rbt_CSC_113011")
            open_dlg_modal_VER(e)

    def rbt_CSC_113013(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.39")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi3/0/13")
            setKeyInrmt("rbt_CSC_113013")
            open_dlg_modal_VER(e)

    def rbt_CSC_113015(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.62")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi3/0/15")
            setKeyInrmt("rbt_CSC_113015")
            open_dlg_modal_VER(e)

    def rbt_CSC_113017(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.31")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi3/0/17")
            setKeyInrmt("rbt_CSC_113017")
            open_dlg_modal_VER(e)

    def rbt_CSC_113019(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.36")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi3/0/19")
            setKeyInrmt("rbt_CSC_113019")
            open_dlg_modal_VER(e)

    def rbt_CSC_113033(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.33")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi3/0/33")
            setKeyInrmt("rbt_CSC_113033")
            open_dlg_modal_VER(e)

    def rbt_CSC_113034(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.63")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi3/0/34")
            setKeyInrmt("rbt_CSC_113034")
            open_dlg_modal_VER(e)

    def rbt_CSC_113036(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.47")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi3/0/36")
            setKeyInrmt("rbt_CSC_113036")
            open_dlg_modal_VER(e)

    def rbt_CSC_113037(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.27")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi3/0/37")
            setKeyInrmt("rbt_CSC_113037")
            open_dlg_modal_VER(e)

    def rbt_CSC_113038(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF66")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi3/0/38")
            setKeyInrmt("rbt_CSC_113038")
            open_dlg_modal_VER(e)

    def rbt_CSC_113039(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.29")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi3/0/39")
            setKeyInrmt("rbt_CSC_113039")
            open_dlg_modal_VER(e)

    def rbt_CSC_113040(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.64")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi3/0/40")
            setKeyInrmt("rbt_CSC_113040")
            open_dlg_modal_VER(e)

    def rbt_CSC_113041(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.44")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi3/0/41")
            setKeyInrmt("rbt_CSC_113041")
            open_dlg_modal_VER(e)

    def rbt_CSC_113042(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF67")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi3/0/42")
            setKeyInrmt("rbt_CSC_113042")
            open_dlg_modal_VER(e)

    def rbt_CSC_113043(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.45")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi3/0/43")
            setKeyInrmt("rbt_CSC_113043")
            open_dlg_modal_VER(e)

    def rbt_CSC_113044(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.50")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi3/0/44")
            setKeyInrmt("rbt_CSC_113044")
            open_dlg_modal_VER(e)

    def rbt_CSC_113045(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.46")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("Gi3/0/45")
            setKeyInrmt("rbt_CSC_113045")
            open_dlg_modal_VER(e)

    # HQ 8th Floor IDF Room key definitions
    def rbt_CSC_IDF(e):
        pass

    def rbt_CSC_14101(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF31")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/1")
            setKeyInrmt("rbt_CSC_14101")
            open_dlg_modal_VER(e)

    def rbt_CSC_14102(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF5")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/2")
            setKeyInrmt("rbt_CSC_14102")
            open_dlg_modal_VER(e)

    def rbt_CSC_14103(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF35")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/3")
            setKeyInrmt("rbt_CSC_14103")
            open_dlg_modal_VER(e)

    def rbt_CSC_14104(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF3")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/4")
            setKeyInrmt("rbt_CSC_14104")
            open_dlg_modal_VER(e)

    def rbt_CSC_14105(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF38")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/5")
            setKeyInrmt("rbt_CSC_14105")
            open_dlg_modal_VER(e)

    def rbt_CSC_14106(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF29")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/6")
            setKeyInrmt("rbt_CSC_14106")
            open_dlg_modal_VER(e)

    def rbt_CSC_14107(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF43")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/7")
            setKeyInrmt("rbt_CSC_14107")
            open_dlg_modal_VER(e)

    def rbt_CSC_14109(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF45")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/9")
            setKeyInrmt("rbt_CSC_14109")
            open_dlg_modal_VER(e)

    def rbt_CSC_141010(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF51")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/10")
            setKeyInrmt("rbt_CSC_141010")
            open_dlg_modal_VER(e)

    def rbt_CSC_141011(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF40")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/11")
            setKeyInrmt("rbt_CSC_141011")
            open_dlg_modal_VER(e)

    def rbt_CSC_141013(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF33")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/13")
            setKeyInrmt("rbt_CSC_141013")
            open_dlg_modal_VER(e)

    def rbt_CSC_141014(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.7")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/14")
            setKeyInrmt("rbt_CSC_141014")
            open_dlg_modal_VER(e)

    def rbt_CSC_141015(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF26")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/15")
            setKeyInrmt("rbt_CSC_141015")
            open_dlg_modal_VER(e)

    def rbt_CSC_141017(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF50")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/17")
            setKeyInrmt("rbt_CSC_141017")
            open_dlg_modal_VER(e)

    def rbt_CSC_141018(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF9")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/18")
            setKeyInrmt("rbt_CSC_141018")
            open_dlg_modal_VER(e)

    def rbt_CSC_141019(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF42")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/19")
            setKeyInrmt("rbt_CSC_141019")
            open_dlg_modal_VER(e)

    def rbt_CSC_141020(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF27")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/20")
            setKeyInrmt("rbt_CSC_141020")
            open_dlg_modal_VER(e)

    def rbt_CSC_141021(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF37")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/21")
            setKeyInrmt("rbt_CSC_141021")
            open_dlg_modal_VER(e)

    def rbt_CSC_141022(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF68")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/22")
            setKeyInrmt("rbt_CSC_141022")
            open_dlg_modal_VER(e)

    def rbt_CSC_141023(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF39")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/23")
            setKeyInrmt("rbt_CSC_141023")
            open_dlg_modal_VER(e)

    def rbt_CSC_141024(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF69")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/24")
            setKeyInrmt("rbt_CSC_141024")
            open_dlg_modal_VER(e)

    def rbt_CSC_141025(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF53")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/25")
            setKeyInrmt("rbt_CSC_141025")
            open_dlg_modal_VER(e)

    def rbt_CSC_141027(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF10")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/27")
            setKeyInrmt("rbt_CSC_141027")
            open_dlg_modal_VER(e)

    def rbt_CSC_141029(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF11")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/29")
            setKeyInrmt("rbt_CSC_141029")
            open_dlg_modal_VER(e)

    def rbt_CSC_141031(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF36")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/31")
            setKeyInrmt("rbt_CSC_141031")
            open_dlg_modal_VER(e)

    def rbt_CSC_141033(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF52")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/33")
            setKeyInrmt("rbt_CSC_141033")
            open_dlg_modal_VER(e)

    def rbt_CSC_141035(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF32")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/35")
            setKeyInrmt("rbt_CSC_141035")
            open_dlg_modal_VER(e)

    def rbt_CSC_141037(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF7")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/37")
            setKeyInrmt("rbt_CSC_141037")
            open_dlg_modal_VER(e)

    def rbt_CSC_141039(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF1")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/39")
            setKeyInrmt("rbt_CSC_141039")
            open_dlg_modal_VER(e)

    def rbt_CSC_141041(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF41")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/41")
            setKeyInrmt("rbt_CSC_141041")
            open_dlg_modal_VER(e)

    def rbt_CSC_141043(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF30")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/43")
            setKeyInrmt("rbt_CSC_141043")
            open_dlg_modal_VER(e)

    def rbt_CSC_141044(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF16")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/44")
            setKeyInrmt("rbt_CSC_141044")
            open_dlg_modal_VER(e)

    def rbt_CSC_141045(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF56")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/45")
            setKeyInrmt("rbt_CSC_141045")
            open_dlg_modal_VER(e)

    def rbt_CSC_141046(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF19")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi1/0/46")
            setKeyInrmt("rbt_CSC_141046")
            open_dlg_modal_VER(e)

    def rbt_CSC_14201(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF8")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi2/0/1")
            setKeyInrmt("rbt_CSC_14201")
            open_dlg_modal_VER(e)

    def rbt_CSC_14203(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF21")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi2/0/3")
            setKeyInrmt("rbt_CSC_14203")
            open_dlg_modal_VER(e)

    def rbt_CSC_14205(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF12")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi2/0/5")
            setKeyInrmt("rbt_CSC_14205")
            open_dlg_modal_VER(e)

    def rbt_CSC_14207(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF14")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi2/0/7")
            setKeyInrmt("rbt_CSC_14207")
            open_dlg_modal_VER(e)

    def rbt_CSC_142010(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ8")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi2/0/10")
            setKeyInrmt("rbt_CSC_142010")
            open_dlg_modal_VER(e)

    def rbt_CSC_142011(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF44")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi2/0/11")
            setKeyInrmt("rbt_CSC_142011")
            open_dlg_modal_VER(e)

    def rbt_CSC_142013(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF22")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi2/0/13")
            setKeyInrmt("rbt_CSC_142013")
            open_dlg_modal_VER(e)

    def rbt_CSC_142015(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF25")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi2/0/15")
            setKeyInrmt("rbt_CSC_142015")
            open_dlg_modal_VER(e)

    def rbt_CSC_142017(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF55")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi2/0/17")
            setKeyInrmt("rbt_CSC_142017")
            open_dlg_modal_VER(e)

    def rbt_CSC_142018(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF2")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi2/0/18")
            setKeyInrmt("rbt_CSC_142018")
            open_dlg_modal_VER(e)

    def rbt_CSC_142019(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF28")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi2/0/19")
            setKeyInrmt("rbt_CSC_142019")
            open_dlg_modal_VER(e)

    def rbt_CSC_142021(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF57")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi2/0/21")
            setKeyInrmt("rbt_CSC_142021")
            open_dlg_modal_VER(e)

    def rbt_CSC_142022(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF15")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi2/0/22")
            setKeyInrmt("rbt_CSC_142022")
            open_dlg_modal_VER(e)

    def rbt_CSC_142025(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF18")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi2/0/25")
            setKeyInrmt("rbt_CSC_142025")
            open_dlg_modal_VER(e)

    def rbt_CSC_142027(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF54")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi2/0/27")
            setKeyInrmt("rbt_CSC_142027")
            open_dlg_modal_VER(e)

    def rbt_CSC_142028(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF20")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi2/0/28")
            setKeyInrmt("rbt_CSC_142028")
            open_dlg_modal_VER(e)

    def rbt_CSC_142032(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF23")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi2/0/32")
            setKeyInrmt("rbt_CSC_142032")
            open_dlg_modal_VER(e)

    def rbt_CSC_142033(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF34")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi2/0/33")
            setKeyInrmt("rbt_CSC_142033")
            open_dlg_modal_VER(e)

    def rbt_CSC_142035(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF17")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi2/0/35")
            setKeyInrmt("rbt_CSC_142035")
            open_dlg_modal_VER(e)

    def rbt_CSC_142036(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF13")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi2/0/36")
            setKeyInrmt("rbt_CSC_142036")
            open_dlg_modal_VER(e)

    def rbt_CSC_142037(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF4")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi2/0/37")
            setKeyInrmt("rbt_CSC_142037")
            open_dlg_modal_VER(e)

    def rbt_CSC_142038(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF24")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi2/0/38")
            setKeyInrmt("rbt_CSC_142038")
            open_dlg_modal_VER(e)

    def rbt_CSC_142040(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF6")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("Gi2/0/40")
            setKeyInrmt("rbt_CSC_142040")
            open_dlg_modal_VER(e)

    # Old HQ Server Room key definitions
    def rbt_CSC_B1(e):
        pass

    def rbt_CSC_13101(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ8")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("Gi1/0/1")
            setKeyInrmt("rbt_CSC_13101")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_13102(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ17")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("Gi1/0/2")
            setKeyInrmt("rbt_CSC_13102")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_13103(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ7")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("Gi1/0/3")
            setKeyInrmt("rbt_CSC_13103")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_13104(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ3")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("Gi1/0/4")
            setKeyInrmt("rbt_CSC_13104")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_13105(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ5")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("Gi1/0/5")
            setKeyInrmt("rbt_CSC_13105")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_13106(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ19")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("Gi1/0/6")
            setKeyInrmt("rbt_CSC_13106")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_13107(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ6")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("Gi1/0/7")
            setKeyInrmt("rbt_CSC_13107")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_13108(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ20")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("Gi1/0/8")
            setKeyInrmt("rbt_CSC_13108")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_13109(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ10")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("Gi1/0/9")
            setKeyInrmt("rbt_CSC_13109")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_131011(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ4")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("Gi1/0/11")
            setKeyInrmt("rbt_CSC_131011")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_131013(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ9")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("Gi1/0/13")
            setKeyInrmt("rbt_CSC_131013")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_131015(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ11")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("Gi1/0/15")
            setKeyInrmt("rbt_CSC_131015")
            open_dlg_modal_VER(e)
       
    def rbt_CSC_131017(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ1")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("Gi1/0/17")
            setKeyInrmt("rbt_CSC_131017")
            open_dlg_modal_VER(e)
       
    def rbt_CSC_131019(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ12")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("Gi1/0/19")
            setKeyInrmt("rbt_CSC_131019")
            open_dlg_modal_VER(e)
       
    def rbt_CSC_131021(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ18")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("Gi1/0/21")
            setKeyInrmt("rbt_CSC_131021")
            open_dlg_modal_VER(e)
       
    def rbt_CSC_131039(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ16")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("Gi1/0/39")
            setKeyInrmt("rbt_CSC_131039")
            open_dlg_modal_VER(e)
       
    def rbt_CSC_131041(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ15")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("Gi1/0/41")
            setKeyInrmt("rbt_CSC_131041")
            open_dlg_modal_VER(e)
       
    def rbt_CSC_131043(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ14")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("Gi1/0/43")
            setKeyInrmt("rbt_CSC_131043")
            open_dlg_modal_VER(e)

    def rbt_CSC_131047(e): # QA Added
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ13")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("Gi1/0/47")
            setKeyInrmt("rbt_CSC_131047")
            open_dlg_modal_VER(e)
    
    # Corner House Server Room key definitions
    def rbt_CSC_CH(e):
        pass
    
    def rbt_CSC_20102(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.5")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("Gi1/0/2")
            setKeyInrmt("rbt_CSC_20102")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_20103(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.7")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("Gi1/0/3")
            setKeyInrmt("rbt_CSC_20103")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_20104(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.10")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("Gi1/0/4")
            setKeyInrmt("rbt_CSC_20104")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_20105(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.9")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("Gi1/0/5")
            setKeyInrmt("rbt_CSC_20105")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_20106(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.6")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("Gi1/0/6")
            setKeyInrmt("rbt_CSC_20106")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_20107(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.1")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("Gi1/0/7")
            setKeyInrmt("rbt_CSC_20107")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_20108(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.4")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("Gi1/0/8")
            setKeyInrmt("rbt_CSC_20108")
            open_dlg_modal_VER(e)

    def rbt_CSC_20109(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.12")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("Gi1/0/9")
            setKeyInrmt("rbt_CSC_20109")
            open_dlg_modal_VER(e)

    def rbt_CSC_201010(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.2")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("Gi1/0/10")
            setKeyInrmt("rbt_CSC_201010")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_201011(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.3")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("Gi1/0/11")
            setKeyInrmt("rbt_CSC_201011")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_201012(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.8")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("Gi1/0/12")
            setKeyInrmt("rbt_CSC_201012")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_201013(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.13")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("Gi1/0/13")
            setKeyInrmt("rbt_CSC_201013")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_201014(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.11")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("Gi1/0/14")
            setKeyInrmt("rbt_CSC_201014")
            open_dlg_modal_VER(e)

    # Demostheni Severi Parking 1 key definistions
    def rbt_CSC_P1(e):
        pass

    def rbt_CSC_4101(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Desmostheni Severi Parking 1 OHQ.PRK1.5")
            setHost4Cam_Global("192.168.201.4")
            setInt4Cam_Global("Gi1/0/1")
            setKeyInrmt("rbt_CSC_4101")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_4102(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Desmostheni Severi Parking 1 OHQ.PRK1.4")
            setHost4Cam_Global("192.168.201.4")
            setInt4Cam_Global("Gi1/0/2")
            setKeyInrmt("rbt_CSC_4102")
            open_dlg_modal_VER(e)

    def rbt_CSC_4103(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Desmostheni Severi Parking 1 OHQ.PRK1.3")
            setHost4Cam_Global("192.168.201.4")
            setInt4Cam_Global("Gi1/0/3")
            setKeyInrmt("rbt_CSC_4103")
            open_dlg_modal_VER(e)

    def rbt_CSC_4104(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Desmostheni Severi Parking 1 OHQ.PRK1.1")
            setHost4Cam_Global("192.168.201.4")
            setInt4Cam_Global("Gi1/0/4")
            setKeyInrmt("rbt_CSC_4104")
            open_dlg_modal_VER(e)

    def rbt_CSC_4108(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Desmostheni Severi Parking 1 OHQ.PRK1.6")
            setHost4Cam_Global("192.168.201.4")
            setInt4Cam_Global("Gi1/0/8")
            setKeyInrmt("rbt_CSC_4108")
            open_dlg_modal_VER(e)

    def rbt_CSC_4107(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Desmostheni Severi Parking 1 OHQ.PRK1.2")
            setHost4Cam_Global("192.168.201.4")
            setInt4Cam_Global("Gi1/0/7")
            setKeyInrmt("rbt_CSC_4107")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_4106(e): # Test asset
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!" # Test asset
            page.update()
        else:
            setDesc4Cam_Global("Desmostheni Severi Parking 1 OHQ.PRK1.9")
            setHost4Cam_Global("192.168.201.4")
            setInt4Cam_Global("Gi1/0/6")
            setKeyInrmt("rbt_CSC_4106")
            open_dlg_modal_VER(e)

    # House 1 key definitions
    def rbt_CSC_H1(e):
        pass

    def rbt_CSC_3101(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 1 H1.6")
            setHost4Cam_Global("192.168.200.3")
            setInt4Cam_Global("Gi1/0/1")
            setKeyInrmt("rbt_CSC_3101")
            open_dlg_modal_VER(e)

    def rbt_CSC_3102(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 1 H1.3")
            setHost4Cam_Global("192.168.200.3")
            setInt4Cam_Global("Gi1/0/2")
            setKeyInrmt("rbt_CSC_3102")
            open_dlg_modal_VER(e)

    def rbt_CSC_3103(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 1 H1.8")
            setHost4Cam_Global("192.168.200.3")
            setInt4Cam_Global("Gi1/0/3")
            setKeyInrmt("rbt_CSC_3103")
            open_dlg_modal_VER(e)

    def rbt_CSC_3104(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 1 H1.9")
            setHost4Cam_Global("192.168.200.3")
            setInt4Cam_Global("Gi1/0/4")
            setKeyInrmt("rbt_CSC_3104")
            open_dlg_modal_VER(e)

    def rbt_CSC_3105(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 1 H1.7")
            setHost4Cam_Global("192.168.200.3")
            setInt4Cam_Global("Gi1/0/5")
            setKeyInrmt("rbt_CSC_3105")
            open_dlg_modal_VER(e)

    def rbt_CSC_3106(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 1 H1.10")
            setHost4Cam_Global("192.168.200.3")
            setInt4Cam_Global("Gi1/0/6")
            setKeyInrmt("rbt_CSC_3106")
            open_dlg_modal_VER(e)

    def rbt_CSC_3107(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 1 H1.2")
            setHost4Cam_Global("192.168.200.3")
            setInt4Cam_Global("Gi1/0/7")
            setKeyInrmt("rbt_CSC_3107")
            open_dlg_modal_VER(e)

    def rbt_CSC_3108(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 1 H1.11")
            setHost4Cam_Global("192.168.200.3")
            setInt4Cam_Global("Gi1/0/8")
            setKeyInrmt("rbt_CSC_3108")
            open_dlg_modal_VER(e)

    def rbt_CSC_31010(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 1 H1.4")
            setHost4Cam_Global("192.168.200.3")
            setInt4Cam_Global("Gi1/0/10")
            setKeyInrmt("rbt_CSC_31010")
            open_dlg_modal_VER(e)

    def rbt_CSC_31011(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 1 H1.5")
            setHost4Cam_Global("192.168.200.3")
            setInt4Cam_Global("Gi1/0/11")
            setKeyInrmt("rbt_CSC_31011")
            open_dlg_modal_VER(e)

    def rbt_CSC_31012(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 1 H1.12")
            setHost4Cam_Global("192.168.200.3")
            setInt4Cam_Global("Gi1/0/12")
            setKeyInrmt("rbt_CSC_31012")
            open_dlg_modal_VER(e)

    # House 2 key definitions
    def rbt_CSC_H2(e):
        pass

    def rbt_CSC_40101(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.2")
            setHost4Cam_Global("192.168.200.40")
            setInt4Cam_Global("Gi1/0/1")
            setKeyInrmt("rbt_CSC_40101")
            open_dlg_modal_VER(e)

    def rbt_CSC_40105(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.14")
            setHost4Cam_Global("192.168.200.40")
            setInt4Cam_Global("Gi1/0/5")
            setKeyInrmt("rbt_CSC_40105")
            open_dlg_modal_VER(e)

    def rbt_CSC_40106(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.7")
            setHost4Cam_Global("192.168.200.40")
            setInt4Cam_Global("Gi1/0/6")
            setKeyInrmt("rbt_CSC_40106")
            open_dlg_modal_VER(e)

    def rbt_CSC_40108(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.9")
            setHost4Cam_Global("192.168.200.40")
            setInt4Cam_Global("Gi1/0/8")
            setKeyInrmt("rbt_CSC_40108")
            open_dlg_modal_VER(e)

    def rbt_CSC_40109(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.8")
            setHost4Cam_Global("192.168.200.40")
            setInt4Cam_Global("Gi1/0/9")
            setKeyInrmt("rbt_CSC_40109")
            open_dlg_modal_VER(e)

    def rbt_CSC_401017(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.6")
            setHost4Cam_Global("192.168.200.40")
            setInt4Cam_Global("Gi1/0/17")
            setKeyInrmt("rbt_CSC_401017")
            open_dlg_modal_VER(e)

    def rbt_CSC_401019(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.10")
            setHost4Cam_Global("192.168.200.40")
            setInt4Cam_Global("Gi1/0/19")
            setKeyInrmt("rbt_CSC_401019")
            open_dlg_modal_VER(e)

    def rbt_CSC_401023(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.19")
            setHost4Cam_Global("192.168.200.40")
            setInt4Cam_Global("Gi1/0/23")
            setKeyInrmt("rbt_CSC_401023")
            open_dlg_modal_VER(e)

    def rbt_CSC_41017(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.20")
            setHost4Cam_Global("192.168.200.41")
            setInt4Cam_Global("Fa0/17")
            setKeyInrmt("rbt_CSC_41017")
            open_dlg_modal_VER(e)

    def rbt_CSC_41019(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.21")
            setHost4Cam_Global("192.168.200.41")
            setInt4Cam_Global("Fa0/19")
            setKeyInrmt("rbt_CSC_41019")
            open_dlg_modal_VER(e)

    def rbt_CSC_41021(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.12")
            setHost4Cam_Global("192.168.200.41")
            setInt4Cam_Global("Fa0/21")
            setKeyInrmt("rbt_CSC_41021")
            open_dlg_modal_VER(e)

    def rbt_CSC_41022(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.18")
            setHost4Cam_Global("192.168.200.41")
            setInt4Cam_Global("Fa0/22")
            setKeyInrmt("rbt_CSC_41022")
            open_dlg_modal_VER(e)

    def rbt_CSC_41023(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.16")
            setHost4Cam_Global("192.168.200.41")
            setInt4Cam_Global("Fa0/23")
            setKeyInrmt("rbt_CSC_41023")
            open_dlg_modal_VER(e)

    def rbt_CSC_41024(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.17")
            setHost4Cam_Global("192.168.200.41")
            setInt4Cam_Global("Fa0/24")
            setKeyInrmt("rbt_CSC_41024")
            open_dlg_modal_VER(e)

    # House 3 key definitions
    def rbt_CSC_H3(e):
        pass

    def rbt_CSC_72017(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 3 H3.16")
            setHost4Cam_Global("192.168.200.72")
            setInt4Cam_Global("Fa0/17")
            setKeyInrmt("rbt_CSC_72017")
            open_dlg_modal_VER(e)

    def rbt_CSC_72018(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 3 H3.21")
            setHost4Cam_Global("192.168.200.72")
            setInt4Cam_Global("Fa0/18")
            setKeyInrmt("rbt_CSC_72018")
            open_dlg_modal_VER(e)

    def rbt_CSC_72019(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 3 H3.2")
            setHost4Cam_Global("192.168.200.72")
            setInt4Cam_Global("Fa0/19")
            setKeyInrmt("rbt_CSC_72019")
            open_dlg_modal_VER(e)

    def rbt_CSC_72020(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 3 H3.17")
            setHost4Cam_Global("192.168.200.72")
            setInt4Cam_Global("Fa0/20")
            setKeyInrmt("rbt_CSC_72020")
            open_dlg_modal_VER(e)

    def rbt_CSC_72021(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 3 H3.20")
            setHost4Cam_Global("192.168.200.72")
            setInt4Cam_Global("Fa0/21")
            setKeyInrmt("rbt_CSC_72021")
            open_dlg_modal_VER(e)

    def rbt_CSC_72022(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 3 H3.18")
            setHost4Cam_Global("192.168.200.72")
            setInt4Cam_Global("Fa0/22")
            setKeyInrmt("rbt_CSC_72022")
            open_dlg_modal_VER(e)

    def rbt_CSC_72023(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 3 H3.14")
            setHost4Cam_Global("192.168.200.72")
            setInt4Cam_Global("Fa0/23")
            setKeyInrmt("rbt_CSC_72023")
            open_dlg_modal_VER(e)

    def rbt_CSC_73017(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 3 H3.9")
            setHost4Cam_Global("192.168.200.73")
            setInt4Cam_Global("Fa0/17")
            setKeyInrmt("rbt_CSC_73017")
            open_dlg_modal_VER(e)

    def rbt_CSC_73018(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 3 H3.8")
            setHost4Cam_Global("192.168.200.73")
            setInt4Cam_Global("Fa0/18")
            setKeyInrmt("rbt_CSC_73018")
            open_dlg_modal_VER(e)

    def rbt_CSC_73019(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 3 H3.13")
            setHost4Cam_Global("192.168.200.73")
            setInt4Cam_Global("Fa0/19")
            setKeyInrmt("rbt_CSC_73019")
            open_dlg_modal_VER(e)

    def rbt_CSC_73020(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 3 H3.15")
            setHost4Cam_Global("192.168.200.73")
            setInt4Cam_Global("Fa0/20")
            setKeyInrmt("rbt_CSC_73020")
            open_dlg_modal_VER(e)

    def rbt_CSC_73021(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 3 H3.5")
            setHost4Cam_Global("192.168.200.73")
            setInt4Cam_Global("Fa0/21")
            setKeyInrmt("rbt_CSC_73021")
            open_dlg_modal_VER(e)

    def rbt_CSC_73022(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 3 H3.19")
            setHost4Cam_Global("192.168.200.73")
            setInt4Cam_Global("Fa0/22")
            setKeyInrmt("rbt_CSC_73022")
            open_dlg_modal_VER(e)

    def rbt_CSC_73023(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 3 H3.3")
            setHost4Cam_Global("192.168.200.73")
            setInt4Cam_Global("Fa0/23")
            setKeyInrmt("rbt_CSC_73023")
            open_dlg_modal_VER(e)

    def rbt_CSC_73024(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 3 H3.6")
            setHost4Cam_Global("192.168.200.73")
            setInt4Cam_Global("Fa0/24")
            setKeyInrmt("rbt_CSC_73024")
            open_dlg_modal_VER(e)

    def rbt_CSC_74017(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 3 H3.4")
            setHost4Cam_Global("192.168.200.74")
            setInt4Cam_Global("Fa0/17")
            setKeyInrmt("rbt_CSC_74017")
            open_dlg_modal_VER(e)

    def rbt_CSC_74018(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 3 H3.12")
            setHost4Cam_Global("192.168.200.74")
            setInt4Cam_Global("Fa0/18")
            setKeyInrmt("rbt_CSC_74018")
            open_dlg_modal_VER(e)

    def rbt_CSC_74020(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 3 H3.10")
            setHost4Cam_Global("192.168.200.74")
            setInt4Cam_Global("Fa0/20")
            setKeyInrmt("rbt_CSC_74020")
            open_dlg_modal_VER(e)

    def rbt_CSC_74021(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 3 H3.1")
            setHost4Cam_Global("192.168.200.74")
            setInt4Cam_Global("Fa0/21")
            setKeyInrmt("rbt_CSC_74021")
            open_dlg_modal_VER(e)

    def rbt_CSC_74022(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 3 H3.7")
            setHost4Cam_Global("192.168.200.74")
            setInt4Cam_Global("Fa0/22")
            setKeyInrmt("rbt_CSC_74022")
            open_dlg_modal_VER(e)

    def rbt_CSC_74023(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 3 H3.11")
            setHost4Cam_Global("192.168.200.74")
            setInt4Cam_Global("Fa0/23")
            setKeyInrmt("rbt_CSC_74023")
            open_dlg_modal_VER(e)

    # House 4 key definitions
    def rbt_CSC_H4(e):
        pass

    def rbt_CSC_100017(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 4 H4.10")
            setHost4Cam_Global("192.168.200.100")
            setInt4Cam_Global("Fa0/17")
            setKeyInrmt("rbt_CSC_100017")
            open_dlg_modal_VER(e)

    def rbt_CSC_100019(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 4 H4.8")
            setHost4Cam_Global("192.168.200.100")
            setInt4Cam_Global("Fa0/19")
            setKeyInrmt("rbt_CSC_100019")
            open_dlg_modal_VER(e)

    def rbt_CSC_100021(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 4 H4.4")
            setHost4Cam_Global("192.168.200.100")
            setInt4Cam_Global("Fa0/21")
            setKeyInrmt("rbt_CSC_100021")
            open_dlg_modal_VER(e)

    def rbt_CSC_100023(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 4 H4.9")
            setHost4Cam_Global("192.168.200.100")
            setInt4Cam_Global("Fa0/23")
            setKeyInrmt("rbt_CSC_100023")
            open_dlg_modal_VER(e)

    def rbt_CSC_101017(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 4 H4.3")
            setHost4Cam_Global("192.168.200.101")
            setInt4Cam_Global("Fa0/17")
            setKeyInrmt("rbt_CSC_101017")
            open_dlg_modal_VER(e)

    def rbt_CSC_101018(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 4 H4.2")
            setHost4Cam_Global("192.168.200.101")
            setInt4Cam_Global("Fa0/18")
            setKeyInrmt("rbt_CSC_101018")
            open_dlg_modal_VER(e)

    def rbt_CSC_101020(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 4 H4.1")
            setHost4Cam_Global("192.168.200.101")
            setInt4Cam_Global("Fa0/20")
            setKeyInrmt("rbt_CSC_101020")
            open_dlg_modal_VER(e)

    def rbt_CSC_101022(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 4 H4.5")
            setHost4Cam_Global("192.168.200.101")
            setInt4Cam_Global("Fa0/22")
            setKeyInrmt("rbt_CSC_101022")
            open_dlg_modal_VER(e)

    def rbt_CSC_101024(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 4 H4.7")
            setHost4Cam_Global("192.168.200.101")
            setInt4Cam_Global("Fa0/24")
            setKeyInrmt("rbt_CSC_101024")
            open_dlg_modal_VER(e)

    # TESTBtn Definition
    def SIM_rbt_CSC_4106(e): # Test asset
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("The test for simulating the reload of the camera was successful")
            setHost4Cam_Global("192.168.201.4")
            setInt4Cam_Global("Gi1/0/6")
            SIM_open_dlg_modal_VER(e)

    # Full TESTBtn Definition
    def SIM_FullTest(e): # Test asset
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            FullSysTestBtn(e)

    # Create login alert-dialoge object
    def open_dlg_UserLogin(e):
        page.dialog = dlg_UserLogin     # Define class dialog as alert-dialog
        dlg_UserLogin.open = True       # View property changed to possitive to display alert
        page.update()                   # Update the page on self

    def close_dlg_UserLogin(e):
        dlg_UserLogin.open = False
        passWordCPT.value = ""
        userNameCPT.value = ""
        page.update()

    def close_dlg_UserLogin_onLogin(e):
        dlg_UserLogin.open = False
        page.update()

    def open_dlg_modal_Story(e):
        if DefaultOrStory == 0:
            dlg = nlxFT.AlertDialog(
                    content=nlxFT.Text(f"{emptMessage}"),
                    content_padding=30
                    )
            # page.anAlert.open = True
            page.dialog = dlg
            dlg.open = True
            page.update()
        else:          
            dlg = nlxFT.AlertDialog(
                    content=nlxFT.Text(f"{reloadedCamsStory}")
                    )
            # page.anAlert.open = True
            page.dialog = dlg
            dlg.open = True
            page.update()

    def open_dlg_modal_VER(e):
        # The following is never called, therefor comented. Remove completely if not needed.
        # onWay2Modal = inGlobal_CamDescription
        currentCam.select = inGlobal_CamDescription
        # Defining definition method to close the alert dialogue.
        def close_modal_VER(e):
            dlg_modal_VER.open = False
            page.update()
        # Defining the main engine of the reload button here. Called from within open_dlg_modal_VER definition.
        def ENG_CSC_General(e):
            close_modal_VER(e)
            RLDCamsAtLeast1(1)
            counter_manager.increment_key(KeyReloaded)
            current_datetime = datetime.datetime.now()
            RLDCamsStory(f"{reloadedCamsStory}\nCamera {inGlobal_CamDescription} reloaded on {current_datetime}")
            status.value = f"Camera {inGlobal_CamDescription} is now in reload process. Please be patient."
            page.update()
            # ----------
            SSHCSCPrmk_Rldr = CSCRldr_Prmk.AssetRldCmdsExe(host=inGlobal_Host, port=22, username=inGlobal_User, password=inGlobal_PassWord, interface=inGlobal_Interface)
            SSHCSCPrmk_Rldr.connect()
            SSHCSCPrmk_Rldr.send_commands()
            SSHCSCPrmk_Rldr.close()
            # ----------  
            status.value = f"Camera {inGlobal_CamDescription} Reloaded."
            page.update()
            with open(session_loggfile, "w")as s_file:
                # s_file.write(f"{reloadedCamsStory}")
                s_file.write(f"User: {inGlobal_User}\n{reloadedCamsStory}")
                print(f"Camera {inGlobal_CamDescription} reloaded on {current_datetime}")
            time.sleep(2)
            status.value = f"Log updated. Please see session actions with the record button or log file {session_loggfile}"
            page.update()
            CamTimesReloaded = counter_manager.get_value(KeyReloaded)
            print(f"{inGlobal_CamDescription} pressed times:", CamTimesReloaded)
        # Verification alert dialogue stractured to check with user if specified asset will indeed be reloaded. 
        # Called when open_dlg_modal_VER is called. 
        dlg_modal_VER = nlxFT.AlertDialog(
            modal=True,
            title=nlxFT.Text("Please Confirm"),
            content=nlxFT.Text(f"Are you sure you want to reboot camera {inGlobal_CamDescription}?"),
            actions=[
                nlxFT.TextButton("Yes", on_click=ENG_CSC_General),
                nlxFT.TextButton("No", on_click=close_modal_VER),
            ],
            actions_alignment=nlxFT.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
            )
        # Called when open_dlg_modal_VER is called. 
        dlg_RldLimiter = nlxFT.AlertDialog(
            title=nlxFT.Text("Warning!"), on_dismiss=lambda e: print("Dialog dismissed!"),
            content=nlxFT.Text(f"Camera {inGlobal_CamDescription} has been reloaded a maximum of 3 times.\n"\
                               "Please open a Jira ticket with the local IT team from a corporate PC.\nhttps://jira.wargaming.net")
        )
        # NLXChecker! Print everything curried up to this point on line.
        print(inGlobal_CamDescription)
        print(inGlobal_Host)
        print(inGlobal_Interface)
        print(KeyReloaded)
        # These are executed at once when definition ENG_CSC_General is called from a key definition
        CamTimesReloaded = counter_manager.get_value(KeyReloaded)
        if (CamTimesReloaded <=2):
            page.dialog = dlg_modal_VER
            dlg_modal_VER.open = True
            page.update()
        else:
            page.dialog = dlg_RldLimiter
            dlg_RldLimiter.open = True
            page.update()

    def SIM_open_dlg_modal_VER(e):
        # Loading simulation description in global variable
        currentCam.select = inGlobal_CamDescription
        # Defining definition method to close the alert dialogue.
        def close_modal_VER(e):
            dlg_modal_VER.open = False
            page.update()
        # Defining the main engine of the reload button here. Called from within open_dlg_modal_VER definition.
        def ENG_CSC_General(e):
            close_modal_VER(e)
            RLDCamsAtLeast1(1)
            RLDCamsStory(f"{reloadedCamsStory}\nCamera reload simulation test")
            status.value = "Camera reload simulation is now being processed. Please be patient."
            page.update()
            # ----------
            SSHCSCPrmk_Rldr = CSCRldr_Prmk.AssetRldCmdsExe(host=inGlobal_Host, port=22, username=inGlobal_User, password=inGlobal_PassWord, interface=inGlobal_Interface)
            SSHCSCPrmk_Rldr.connect()
            SSHCSCPrmk_Rldr.send_commands()
            SSHCSCPrmk_Rldr.close()
            # ----------
            status.value = "Simulation/Test Completed successfully."
            page.update()
            page.update()
        # Verification alert dialogue stractured to check with user if specified asset will indeed be reloaded. 
        # Called when open_dlg_modal_VER is called. 
        dlg_modal_VER = nlxFT.AlertDialog(
            modal=True,
            title=nlxFT.Text("Please Confirm"),
            content=nlxFT.Text(f"Run camera reload Simulation/Test now?\n"\
                               "This means that the application will power cycle any port without connected security cameras to ensure functionality.\n"\
                                "This will ensure accessibility to the Security Network and Network devices. Time to complete: Approx. 30 seconds"),
            actions=[
                nlxFT.TextButton("Yes", on_click=ENG_CSC_General),
                nlxFT.TextButton("No", on_click=close_modal_VER),
            ],
            actions_alignment=nlxFT.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
            )
        
        # NLXChecker! Print everything curried up to this point on line.
        print(inGlobal_CamDescription)
        print(inGlobal_Host)
        print(inGlobal_Interface)
        # These are executed at once when definition ENG_CSC_General is called from a key definition
        page.dialog = dlg_modal_VER
        dlg_modal_VER.open = True
        page.update()

    def FullSysTestBtn(e):
        # Loading simulation description in global variable
        currentCam.select = inGlobal_CamDescription
        # Defining definition method to close the alert dialogue.
        def close_modal_VER(e):
            dlg_modal_VER.open = False
            page.update()

        def close_modal_Hold(e):
            dlg_modal_Hold.open = False
            page.update()

        # Defining the main engine of the reload button here. Called from within open_dlg_modal_VER definition.
        def FullSystemTest_CSC_General(e):
            close_modal_VER(e)
            status.value = "System test in progress. Please be patient."
            page.update()
            page.dialog = dlg_modal_Hold
            dlg_modal_Hold.open = True
            page.update()

            FullTestStory = ""

            # Declare text-files
            FSTCurrent_datetime = datetime.datetime.now()
            FSTFormatted_datetime = FSTCurrent_datetime.strftime("%Y%m%d_%H%M%S")
            FSTSession_loggfile = f"SecNetCSCFTest_FullSysTest_{FSTFormatted_datetime}.txt"

            # Sec. Net. Switch tuple
            SecNetSwitches = ("192.168.77.11", "192.168.77.14", "192.168.77.13", "192.168.77.20",\
                      "192.168.201.4", "192.168.200.3", "192.168.200.40", "192.168.200.41",\
                        "192.168.200.72", "192.168.200.73", "192.168.200.74",\
                            "192.168.200.100", "192.168.200.101")

            # Replace these values with the actual credentials and IP addresses of your Cisco switches
            for SNSwitch in SecNetSwitches:
                activeSwitch = FSSClass.CiscoSwitchChecker(SNSwitch, inGlobal_User, inGlobal_PassWord)
                activeSwitch_result_con = activeSwitch.check_accessibility()
                activeSwitch_RLDSuccess = activeSwitch.reload_port()
                FullTestStory = (f"{FullTestStory}{activeSwitch_result_con}\n")
                FullTestStory = (f"{FullTestStory}{activeSwitch_RLDSuccess}\n")

            with open(FSTSession_loggfile, "w")as FT_file:
                FT_file.write(FullTestStory)

            RLDCamsAtLeast1(1)
            RLDCamsStory(f"{reloadedCamsStory}\nFull system test")
            status.value = "System test completed."
            page.update()
            time.sleep(2)
            status.value = f"Please review the test results by checking the information stored in log file {FSTSession_loggfile}"
            close_modal_Hold(e)
            page.update()

        # Verification alert dialogue stractured to check with user if specified asset will indeed be reloaded. 
        # Called when open_dlg_modal_VER is called. 
        dlg_modal_VER = nlxFT.AlertDialog(
            modal=True,
            title=nlxFT.Text("Please Confirm"),
            content=nlxFT.Text(f"Run full system test now?\n"\
                               "This means that the application will conduct a comprehensive accessibility test on all security network switch devices.\n"\
                                "In addition, the application will check if the active user has the rights to power cycle the security cameras.\n"\
                                    "Kindly be informed that this process will require a considerable amount of time to be completed.\n"\
                                        "The test rerults will be exported to a testfile.\n"\
                                            "Time to complete: Approx. 1.5 minutes"),
            actions=[
                nlxFT.TextButton("Yes", on_click=FullSystemTest_CSC_General),
                nlxFT.TextButton("No", on_click=close_modal_VER),
            ],
            actions_alignment=nlxFT.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!")
            )
        
        dlg_modal_Hold = nlxFT.AlertDialog(
            modal=True,
            title=nlxFT.Text("Testing System"),
            content=nlxFT.Text(f"Full system test in progress. Please wait!!!\n"\
                               "When the testing is complete, this message will automatically close."),
            actions_alignment=nlxFT.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!")
            )

        # These are executed at once when definition ENG_CSC_General is called from a key definition
        page.dialog = dlg_modal_VER
        dlg_modal_VER.open = True
        page.update()

    dlg_UserLogin = nlxFT.AlertDialog(
        modal = True,
        title = nlxFT.Text("Please Login"),
        content_padding = 20,
        content = nlxFT.Container(
            # expand=False,
            width = 550,
            height = 170,
            content =
                nlxFT.Column(
                    expand = False,
                    controls = [
                        nlxFT.Text("Please use your provided credentials to log in. If you do not have\na set of credentials, please send an email to the address provided."),
                        nlxFT.ElevatedButton("cyit@wargaming.net", icon=nlxFT.icons.MAIL_ROUNDED, url="mailto:cyit@wargaming.net"), nlxFT.Divider(height=1.5, color="Transparent"),
                        nlxFT.Row(
                            alignment = nlxFT.MainAxisAlignment.SPACE_EVENLY,
                            controls = [
                            userNameCPT,
                            passWordCPT
                            ]
                        )
                    ]
                ) 
            ),
        actions = [
            nlxFT.FloatingActionButton(icon=nlxFT.icons.LOGIN_ROUNDED, bgcolor=nlxFT.colors.BLUE_300, on_click=login_dlg_UserLogin),
            nlxFT.FloatingActionButton(icon=nlxFT.icons.CANCEL_ROUNDED, bgcolor=nlxFT.colors.BLUE_300, on_click=close_dlg_UserLogin)
        ],
        actions_alignment = nlxFT.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!")
    )

    dlg_Wrong_UserLogin = nlxFT.AlertDialog(
        content = nlxFT.Container(
            content = nlxFT.Column(
                height = 10,
                expand = False,
                controls = [
                    nlxFT.Row(
                        height = 30,
                        alignment = nlxFT.CrossAxisAlignment.CENTER,
                        vertical_alignment = nlxFT.MainAxisAlignment.CENTER,
                        controls = [
                        nlxFT.Text(MSG1)
                        ]
                    )
                ]
            )
        )
    )

    def close_banner(e):
        page.banner.open = False
        page.update()

    def highlight_link(e):
        e.control.style.color = nlxFT.colors.BLUE
        e.control.update()

    def unhighlight_link(e):
        e.control.style.color = None
        e.control.update()

    page.banner =nlxFT.Banner(
        bgcolor=nlxFT.colors.AMBER_100,
        leading=nlxFT.Icon(nlxFT.icons.WARNING_AMBER_ROUNDED, color=nlxFT.colors.ORANGE, size=40),
        content=nlxFT.Text(
            spans=[

                nlxFT.TextSpan(
                    "Oops… It seems that there were some issues connecting to the system.\n"\
                        "Please verify your login credentials and try again.\n"\
                        "If you continue to experience issues, please open a Jira ticket.\n",
                    nlxFT.TextStyle(color="black")
                ),
                nlxFT.TextSpan(
                    "https://jira.wargaming.net",
                    nlxFT.TextStyle(color="black", decoration=nlxFT.TextDecoration.UNDERLINE),
                    url="https://jira.wargaming.net",
                )
            ]
        ),
        actions=[
           nlxFT.TextButton("Retry", on_click=open_dlg_UserLogin),
           nlxFT.TextButton("Cancel", on_click=close_banner)
        ],
    )

    def show_banner_click(e):
        page.banner.open = True
        page.update()

    associationDic = {
        # HQ 1st Floor Server Room
        'GHQ.IDF46': rbt_CSC_11101, 'GHQ.MEZ.66': rbt_CSC_11103, 'GHQ.MEZ.61': rbt_CSC_11104, 'GHQ.IDF59': rbt_CSC_11105, 'GHQ.MEZ.51': rbt_CSC_11106,
        'GHQ.MEZ.42': rbt_CSC_11108, 'GHQ.IDF63': rbt_CSC_11109, 'GHQ.IDF49': rbt_CSC_111011, 'GHQ.MEZ.68': rbt_CSC_111012, 'GHQ.MEZ.54': rbt_CSC_111013,
        'GHQ.IDF48': rbt_CSC_111015, 'GHQ.IDF62': rbt_CSC_111017, 'GHQ.IDF47': rbt_CSC_111019, 'GHQ.MEZ.57': rbt_CSC_111025, 'GHQ.MEZ.19': rbt_CSC_111028,
        'GHQ.MEZ.9': rbt_CSC_111029, 'GHQ.MEZ.15': rbt_CSC_111031, 'GHQ.MEZ.10': rbt_CSC_111033, 'GHQ.MEZ.6': rbt_CSC_111034, 'GHQ.MEZ.1': rbt_CSC_111035,
        'GHQ.MEZ.2': rbt_CSC_111036, 'GHQ.MEZ.11': rbt_CSC_111037, 'GHQ.MEZ.13': rbt_CSC_111040, 'GHQ.MEZ.17': rbt_CSC_111042, 'GHQ.MEZ.4': rbt_CSC_111043,
        'GHQ.MEZ.18': rbt_CSC_111044, 'GHQ.MEZ.14': rbt_CSC_111045, 'GHQ.MEZ.21': rbt_CSC_111046, 'GHQ.MEZ.20': rbt_CSC_111048, 'GHQ.MEZ.28': rbt_CSC_11202,
        'GHQ.IDF65': rbt_CSC_11203, 'GHQ.IDF64': rbt_CSC_11205, 'GHQ.MEZ.25': rbt_CSC_11206, 'GHQ.IDF58': rbt_CSC_11208, 'GHQ.MEZ.38': rbt_CSC_11209,
        'GHQ.MEZ.37': rbt_CSC_112010, 'GHQ.MEZ.40': rbt_CSC_112011, 'GHQ.IDF61': rbt_CSC_112013, 'GHQ.MEZ.55': rbt_CSC_112014, 'GHQ.MEZ.26': rbt_CSC_112016,
        'GHQ.MEZ.58': rbt_CSC_112017, 'GHQ.MEZ.32': rbt_CSC_112020, 'GHQ.IDF60': rbt_CSC_112021, 'GHQ.MEZ.52': rbt_CSC_112022, 'GHQ.MEZ.56': rbt_CSC_112023,
        'GHQ.MEZ.35': rbt_CSC_112024, 'GHQ.MEZ.60': rbt_CSC_112025, 'GHQ.MEZ.24': rbt_CSC_112026, 'GHQ.MEZ.34': rbt_CSC_112027, 'GHQ.MEZ.16': rbt_CSC_112028,
        'GHQ.MEZ.53': rbt_CSC_112029, 'GHQ.MEZ.43': rbt_CSC_112030, 'GHQ.MEZ.12': rbt_CSC_112031, 'GHQ.MEZ.22': rbt_CSC_112032, 'GHQ.MEZ.67': rbt_CSC_112033,
        'GHQ.MEZ.30': rbt_CSC_112034, 'GHQ.MEZ.3': rbt_CSC_112035, 'GHQ.MEZ.5': rbt_CSC_112036, 'GHQ.MEZ.41': rbt_CSC_112038, 'GHQ.MEZ.48': rbt_CSC_112040,
        'GHQ.MEZ.49': rbt_CSC_112042, 'GHQ.MEZ.23': rbt_CSC_113011, 'GHQ.MEZ.39': rbt_CSC_113013, 'GHQ.MEZ.62': rbt_CSC_113015, 'GHQ.MEZ.31': rbt_CSC_113017,
        'GHQ.MEZ.36': rbt_CSC_113019, 'GHQ.MEZ.33': rbt_CSC_113033, 'GHQ.MEZ.63': rbt_CSC_113034, 'GHQ.MEZ.47': rbt_CSC_113036, 'GHQ.MEZ.27': rbt_CSC_113037,
        'GHQ.IDF66': rbt_CSC_113038,'GHQ.MEZ.29': rbt_CSC_113039, 'GHQ.MEZ.64': rbt_CSC_113040, 'GHQ.MEZ.44': rbt_CSC_113041, 'GHQ.IDF67': rbt_CSC_113042,
        'GHQ.MEZ.45': rbt_CSC_113043, 'GHQ.MEZ.50': rbt_CSC_113044, 'GHQ.MEZ.46': rbt_CSC_113045, 'GHQ.MEZ.59': rbt_CSC_11204,
        # HQ 8th Floor IDF Room
        'GHQ.IDF31': rbt_CSC_14101, 'GHQ.IDF5': rbt_CSC_14102, 'GHQ.IDF35': rbt_CSC_14103, 'GHQ.IDF3': rbt_CSC_14104, 'GHQ.IDF38': rbt_CSC_14105,
        'GHQ.IDF29': rbt_CSC_14106, 'GHQ.IDF43': rbt_CSC_14107, 'GHQ.IDF45': rbt_CSC_14109, 'GHQ.IDF51': rbt_CSC_141010, 'GHQ.IDF40': rbt_CSC_141011,
        'GHQ.IDF33': rbt_CSC_141013, 'GHQ.MEZ.7': rbt_CSC_141014, 'GHQ.IDF26': rbt_CSC_141015, 'GHQ.IDF50': rbt_CSC_141017, 'GHQ.IDF9': rbt_CSC_141018,
        'GHQ.IDF42': rbt_CSC_141019, 'GHQ.IDF27': rbt_CSC_141020, 'GHQ.IDF37': rbt_CSC_141021, 'GHQ.IDF68': rbt_CSC_141022, 'GHQ.IDF39': rbt_CSC_141023,
        'GHQ.IDF69': rbt_CSC_141024, 'GHQ.IDF53': rbt_CSC_141025, 'GHQ.IDF10': rbt_CSC_141027, 'GHQ.IDF11': rbt_CSC_141029, 'GHQ.IDF36': rbt_CSC_141031,
        'GHQ.IDF52': rbt_CSC_141033, 'GHQ.IDF32': rbt_CSC_141035, 'GHQ.IDF7': rbt_CSC_141037, 'GHQ.IDF1': rbt_CSC_141039, 'GHQ.IDF41': rbt_CSC_141041,
        'GHQ.IDF30': rbt_CSC_141043, 'GHQ.IDF16': rbt_CSC_141044, 'GHQ.IDF56': rbt_CSC_141045, 'GHQ.IDF19': rbt_CSC_141046, 'GHQ.IDF8': rbt_CSC_14201,
        'GHQ.IDF21': rbt_CSC_14203, 'GHQ.IDF12': rbt_CSC_14205, 'GHQ.IDF14': rbt_CSC_14207, 'GHQ.MEZ8': rbt_CSC_142010, 'GHQ.IDF44': rbt_CSC_142011,
        'GHQ.IDF22': rbt_CSC_142013, 'GHQ.IDF25': rbt_CSC_142015, 'GHQ.IDF55': rbt_CSC_142017, 'GHQ.IDF2': rbt_CSC_142018, 'GHQ.IDF28': rbt_CSC_142019,
        'GHQ.IDF57': rbt_CSC_142021, 'GHQ.IDF15': rbt_CSC_142022, 'GHQ.IDF18': rbt_CSC_142025, 'GHQ.IDF54': rbt_CSC_142027, 'GHQ.IDF20': rbt_CSC_142028,
        'GHQ.IDF23': rbt_CSC_142032, 'GHQ.IDF34': rbt_CSC_142033, 'GHQ.IDF17': rbt_CSC_142035, 'GHQ.IDF13': rbt_CSC_142036, 'GHQ.IDF4': rbt_CSC_142037,
        'GHQ.IDF24': rbt_CSC_142038, 'GHQ.IDF6': rbt_CSC_142040,
        # Old HQ Server Room key definitions
        # WA Added rbt_CSC_131047
        'OHQ8': rbt_CSC_13101, 'OHQ17': rbt_CSC_13102, 'OHQ7': rbt_CSC_13103, 'OHQ3': rbt_CSC_13104, 'OHQ5': rbt_CSC_13105,
        'OHQ19': rbt_CSC_13106, 'OHQ6': rbt_CSC_13107, 'OHQ20': rbt_CSC_13108, 'OHQ10': rbt_CSC_13109, 'OHQ4': rbt_CSC_131011,
        'OHQ9': rbt_CSC_131013, 'OHQ11': rbt_CSC_131015, 'OHQ1': rbt_CSC_131017, 'OHQ12': rbt_CSC_131019, 'OHQ18': rbt_CSC_131021,
        'OHQ16': rbt_CSC_131039, 'OHQ15': rbt_CSC_131041, 'OHQ14': rbt_CSC_131043, 'OHQ13': rbt_CSC_131047,
        # Corner House Server Room
        'CRN.5': rbt_CSC_20102, 'CRN.7': rbt_CSC_20103, 'CRN.10': rbt_CSC_20104, 'CRN.9': rbt_CSC_20105, 'CRN.6': rbt_CSC_20106, 'CRN.1': rbt_CSC_20107,
        'CRN.4': rbt_CSC_20108, 'CRN.12': rbt_CSC_20109, 'CRN.2': rbt_CSC_201010, 'CRN.3': rbt_CSC_201011, 'CRN.8': rbt_CSC_201012, 'CRN.13': rbt_CSC_201013,
        'CRN.11': rbt_CSC_201014,
        # Demostheni Severi Parking 1
        'OHQ.PRK1.5': rbt_CSC_4101, 'OHQ.PRK1.4': rbt_CSC_4102, 'OHQ.PRK1.3': rbt_CSC_4103, 'OHQ.PRK1.1': rbt_CSC_4104, 'OHQ.PRK1.6': rbt_CSC_4108,
        'OHQ.PRK1.2': rbt_CSC_4107, 'OHQ.PRK1.9': rbt_CSC_4106,
        # House 1
        'H1.6': rbt_CSC_3101, 'H1.3':  rbt_CSC_3102, 'H1.8': rbt_CSC_3103, 'H1.9': rbt_CSC_3104, 'H1.7': rbt_CSC_3105, 'H1.10': rbt_CSC_3106,
        'H1.2': rbt_CSC_3107, 'H1.11': rbt_CSC_3108, 'H1.4': rbt_CSC_31010, 'H1.5': rbt_CSC_31011, 'H1.1': rbt_CSC_31012,
        # House 2
        'H2.2': rbt_CSC_40101, 'H2.14': rbt_CSC_40105, 'H2.7': rbt_CSC_40106, 'H2.9': rbt_CSC_40108, 'H2.8': rbt_CSC_40109, 'H2.6': rbt_CSC_401017,
        'H2.10': rbt_CSC_401019, 'H2.19': rbt_CSC_401023, 'H2.20': rbt_CSC_41017, 'H2.21': rbt_CSC_41019, 'H2.12': rbt_CSC_41021, 'H2.18': rbt_CSC_41022,
        'H2.16': rbt_CSC_41023, 'H2.17': rbt_CSC_41024,
        # House 3
        'H3.16': rbt_CSC_72017, 'H3.21': rbt_CSC_72018, 'H3.2': rbt_CSC_72019, 'H3.17': rbt_CSC_72020, 'H3.20': rbt_CSC_72021, 'H3.18': rbt_CSC_72022,
        'H3.14': rbt_CSC_72023, 'H3.9': rbt_CSC_73017, 'H3.8': rbt_CSC_73018, 'H3.13': rbt_CSC_73019, 'H3.15': rbt_CSC_73020, 'H3.5': rbt_CSC_73021,
        'H3.19': rbt_CSC_73022, 'H3.3': rbt_CSC_73023, 'H3.6': rbt_CSC_73024, 'H3.4': rbt_CSC_74017, 'H3.12': rbt_CSC_74018, 'H3.10': rbt_CSC_74020,
        'H3.1': rbt_CSC_74021, 'H3.7': rbt_CSC_74022, 'H3.11': rbt_CSC_74023,
        # House 4
        'H4.10': rbt_CSC_100017, 'H4.8': rbt_CSC_100019, 'H4.4': rbt_CSC_100021, 'H4.9': rbt_CSC_100023, 'H4.3': rbt_CSC_101017, 'H4.2': rbt_CSC_101018,
        'H4.1': rbt_CSC_101020, 'H4.5': rbt_CSC_101022, 'H4.7': rbt_CSC_101024
    }

    def searchEng(e):
        # Load search field content into the search variable...
        toSearch_VAR=SearchFieldCPT.value
        # ...and then to the global variable
        toSearch_Global(toSearch_VAR)
        status.value = ""
        page.update()

        def createBtnList():
            function_dict = {
                'function0': close_SearchEng_Mdl_0,
                'function1': close_SearchEng_Mdl_1,
                'function2': close_SearchEng_Mdl_2,
                'function3': close_SearchEng_Mdl_3,
                'function4': close_SearchEng_Mdl_4,
                'function5': close_SearchEng_Mdl_5,
                'function6': close_SearchEng_Mdl_6,
                'function7': close_SearchEng_Mdl_7,
                'function8': close_SearchEng_Mdl_8,
                'function9': close_SearchEng_Mdl_9,
                'function10': close_SearchEng_Mdl_10,
                'function11': close_SearchEng_Mdl_11
                }
            
            shortListNavi_VAR(0)
            for i, item in enumerate(CamDB.assetLst):
                if inGlobal_Search in item.label:
                    # btnTXT = f"close_SearchEng_Mdl_{naviCount}"
                    # print(f"btnTXT: {btnTXT}")
                    # btnGTR = locals()[btnTXT]
                    btnList[naviCount] = nlxFT.ElevatedButton(text=f"{item.location} CCTV Camera {item.label}", icon=f"{item.locationIcon}",
                                                            bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK,
                                                            height=35, width= 440, on_click=function_dict[f'function{naviCount}'])
                    pointerList[naviCount] = item.label
                    print(f"(Line 179) Definition matched for number: {i}, asset: {item.label}")
                    print(f"(Line 180) Placed in list btnList, position: {naviCount}")
                    shortListNavi_VAR(naviCount+1)
            print(f"(Line 182) Number of elements in list btnList: {len(btnList)}")
            print(f"(Line 183) Button list element 0 type: {type(btnList[0])}")

        # Dismiss Exit
        def close_SearchEng_Mdl(e):
            SearchEng_Mdl.open = False
            SearchFieldCPT.value = ""
            reIniSearchList()
            status.value = ""
            page.update()
            for item in btnList:
                print(type[item])

        # Dismiss 0
        def close_SearchEng_Mdl_0(e):
            SearchEng_Mdl.open = False
            page.update()
            print("Will engage close_SearchEng_Mdl_0!!!")
            print(f"Looking for definistion that contains {pointerList[0]}")
            associationDic[pointerList[0]](e)
            reIniSearchList()
            SearchFieldCPT.value = ""
            status.value = ""
    
        # Dismiss 1
        def close_SearchEng_Mdl_1(e):
            SearchEng_Mdl.open = False
            page.update()
            print("Will engage close_SearchEng_Mdl_0!!!")
            print(f"Looking for definistion that contains {pointerList[1]}")
            associationDic[pointerList[1]](e)
            reIniSearchList()
            SearchFieldCPT.value = ""
            status.value = ""

        # Dismiss 2
        def close_SearchEng_Mdl_2(e):
            SearchEng_Mdl.open = False
            page.update()
            print("Will engage close_SearchEng_Mdl_0!!!")
            print(f"Looking for definistion that contains {pointerList[2]}")
            associationDic[pointerList[2]](e)
            reIniSearchList()
            SearchFieldCPT.value = ""
            status.value = ""

        # Dismiss 3
        def close_SearchEng_Mdl_3(e):
            SearchEng_Mdl.open = False
            page.update()
            print("Will engage close_SearchEng_Mdl_0!!!")
            print(f"Looking for definistion that contains {pointerList[3]}")
            associationDic[pointerList[3]](e)
            reIniSearchList()
            SearchFieldCPT.value = ""
            status.value = ""

        # Dismiss 4
        def close_SearchEng_Mdl_4(e):
            SearchEng_Mdl.open = False
            page.update()
            print("Will engage close_SearchEng_Mdl_0!!!")
            print(f"Looking for definistion that contains {pointerList[4]}")
            associationDic[pointerList[4]](e)
            reIniSearchList()
            SearchFieldCPT.value = ""
            status.value = ""

        # Dismiss 5
        def close_SearchEng_Mdl_5(e):
            SearchEng_Mdl.open = False
            page.update()
            print("Will engage close_SearchEng_Mdl_0!!!")
            print(f"Looking for definistion that contains {pointerList[5]}")
            associationDic[pointerList[5]](e)
            reIniSearchList()
            SearchFieldCPT.value = ""
            status.value = ""

        # Dismiss 6
        def close_SearchEng_Mdl_6(e):
            SearchEng_Mdl.open = False
            page.update()
            print("Will engage close_SearchEng_Mdl_0!!!")
            print(f"Looking for definistion that contains {pointerList[6]}")
            associationDic[pointerList[6]](e)
            reIniSearchList()
            SearchFieldCPT.value = ""
            status.value = ""

        # Dismiss 7
        def close_SearchEng_Mdl_7(e):
            SearchEng_Mdl.open = False
            page.update()
            print("Will engage close_SearchEng_Mdl_0!!!")
            print(f"Looking for definistion that contains {pointerList[7]}")
            associationDic[pointerList[7]](e)
            reIniSearchList()
            SearchFieldCPT.value = ""
            status.value = ""

        # Dismiss 8
        def close_SearchEng_Mdl_8(e):
            SearchEng_Mdl.open = False
            page.update()
            print("Will engage close_SearchEng_Mdl_0!!!")
            print(f"Looking for definistion that contains {pointerList[8]}")
            associationDic[pointerList[8]](e)
            reIniSearchList()
            SearchFieldCPT.value = ""
            status.value = ""

        # Dismiss 9
        def close_SearchEng_Mdl_9(e):
            SearchEng_Mdl.open = False
            page.update()
            print("Will engage close_SearchEng_Mdl_0!!!")
            print(f"Looking for definistion that contains {pointerList[9]}")
            associationDic[pointerList[9]](e)
            reIniSearchList()
            SearchFieldCPT.value = ""
            status.value = ""

        # Dismiss 10
        def close_SearchEng_Mdl_10(e):
            SearchEng_Mdl.open = False
            page.update()
            print("Will engage close_SearchEng_Mdl_0!!!")
            print(f"Looking for definistion that contains {pointerList[10]}")
            associationDic[pointerList[10]](e)
            reIniSearchList()
            SearchFieldCPT.value = ""
            status.value = ""

        # Dismiss 11
        def close_SearchEng_Mdl_11(e):
            SearchEng_Mdl.open = False
            page.update()
            print("Will engage close_SearchEng_Mdl_0!!!")
            print(f"Looking for definistion that contains {pointerList[11]}")
            associationDic[pointerList[11]](e)
            reIniSearchList()
            SearchFieldCPT.value = ""
            status.value = ""

        # These are executed at once when definition ENG_CSC_General is called from a key definition
        countRes()

        if (searchCount > 12):
            print(f"(Line 214) To many results... {searchCount}")
            status.value = "There are too many search results. Please try to be more specific with your search criteria..."
            page.update()
            moreOrLess_VAR(0)
        elif (searchCount == 0):
            print("No results")
            status.value = "No results found..."
            page.update()
            moreOrLess_VAR(0)
        else:
            print(f"(Line 216) Results: {searchCount}")
            createBtnList()
            globalList_VAR(btnList)
            moreOrLess_VAR(1)

        SearchEng_Mdl = nlxFT.AlertDialog(
            modal = True,
            title = nlxFT.Text("Search Results:"),
            content_padding = 20,
            content = nlxFT.Container(
                width = 440,
                height = 530,
                content =
                    nlxFT.Column(
                        # expand = True,
                        alignment = nlxFT.CrossAxisAlignment.START,
                        controls = [
                            btnList[0],
                            btnList[1],
                            btnList[2],
                            btnList[3],
                            btnList[4],
                            btnList[5],
                            btnList[6],
                            btnList[7],
                            btnList[8],
                            btnList[9],
                            btnList[10],
                            btnList[11],
                            
                        ]
                    )
                ),
            actions = [
            nlxFT.FloatingActionButton(icon=nlxFT.icons.CANCEL_ROUNDED, 
                                       bgcolor=nlxFT.colors.BLUE_300, 
                                       on_click=close_SearchEng_Mdl)
            ],
            actions_alignment = nlxFT.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Search dialog dismissed!")
        )

        if moreOrLess == 0:
            print(f"More")
        else:
            print(f"Less")
            page.dialog = SearchEng_Mdl
            SearchEng_Mdl.open = True
            page.update()

    SearchFieldCPT = nlxFT.TextField(width=350, prefix_icon=nlxFT.icons.SEARCH_ROUNDED,
                                    hint_text="Search...", border_radius=10, filled=True, text_size=18,
                                    suffix_text="Hint! Case sensitive", on_submit=searchEng)

    def app_Header_Search():
        return nlxFT.Container(
            width=320,
            bgcolor="081d33",
            content=nlxFT.Row(
                vertical_alignment=nlxFT.CrossAxisAlignment.CENTER,
                controls=[
                    SearchFieldCPT
                ]
            )
        )
    # --------------------

    page.add(
        nlxFT.Container(
            expand=True,
            height=1400,
            width=1200,
            content=nlxFT.Column(
                controls=[
                    # Header panel called here
                    nlxFT.Container(
                        bgcolor="#081d33", border_radius=nlxFT.border_radius.only(top_left=10, top_right=10, bottom_left=4, bottom_right=4),
                        padding=nlxFT.padding.only(left=15, right=15),
                        content=
                            nlxFT.Row(
                                height=70, expand=True, alignment=nlxFT.MainAxisAlignment.SPACE_BETWEEN,
                                # NLX! Header instance controls added here:
                                controls=[app_Header_Brand(), app_Header_Search(), app_Header_Avatar()],
                            )
                    ),
                    # nlxFT.Divider(height=0, color="Transparent"),
                    # User strip
                    nlxFT.Container(
                        border_radius=nlxFT.border_radius.only(top_left=4, top_right=4, bottom_left=4, bottom_right=4),
                        bgcolor="#194d80", padding=nlxFT.padding.only(left=20, right=20),
                        content=
                            nlxFT.Row(
                                expand=True, height=30, alignment=nlxFT.MainAxisAlignment.END,
                                # self-control instances added here:
                                controls=[userComment]
                            )
                    ),
                    # nlxFT.Divider(height=0, color="Transparent"),
                    # Camera panel called here
                    nlxFT.Container(
                        expand=True, height=1000, bgcolor="white10", border=nlxFT.border.all(1, "#ebebeb"), border_radius=8, padding=15,
                        content=nlxFT.Column(
                            expand=True,
                            controls=[
                                nlxFT.Tabs(
                                    selected_index=0, animation_duration=300, label_color="blue",
                                    indicator_color="blue", unselected_label_color="#979797",
                                    tabs=[
                                        # HQ 1st Floor Server Room Camera Keys 
                                        nlxFT.Tab(icon=nlxFT.icons.BUSINESS_ROUNDED, text="HQ",
                                            content=nlxFT.Container(
                                                disabled=False,
                                                padding=15,
                                                content=nlxFT.Column(
                                                    controls=[
                                                        nlxFT.Row(
                                                            controls=[
                                                            nlxFT.Text(value="Nicosia, Demostheni Severi 33, 1st Floor Server Room Cameras", size= 15, color="black")
                                                            ]
                                                        ),
                                                        # Row 1
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF46", tooltip="00:0F:7C:0F:9C:CB", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_11101),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.66", tooltip="00:0F:7C:0D:09:17", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_11103),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.61", tooltip="00:0F:7C:0F:1F:EA", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_11104),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF59", tooltip="00:0f:7C:0F:9C:B7", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_11105),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.51", tooltip="00:0F:7C:0F:20:06", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_11106),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.42", tooltip="00:0F:7C:0E:E1:D1", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_11108)
                                                            ]
                                                        ),
                                                        # Row 2
                                                        nlxFT.Row(
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF63", tooltip="00:0F:7C:0F:9C:B8", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_11109),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF49", tooltip="00:0F:7C:0F:82:FE", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_111011),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.68", tooltip="00:18:AE:8B:E8:DE", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_111012),
                                                                nlxFT.ElevatedButton(text="GHQ MEZ.54", tooltip="3C:EF:8C:C5:06:01", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_111013),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF48", tooltip="00:0F:7C:0F:82:FF", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_111015),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF62", tooltip="00:0F:07C:0F:9C:BC", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_111017)
                                                            ]
                                                        ),
                                                        # Row 3
                                                        nlxFT.Row(
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF47", tooltip="00:0F:7C:0F:83:01", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_111019),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.57", tooltip="00:0F:7C:0E:E1:E4", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_111025),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.19", tooltip="00:0F:7C:0F:98:88", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_111028),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.9", tooltip="00:0F:7C:0D:D5:89", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_111029),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.15", tooltip="00:0F:7C:0D:D5:BD", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_111031),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.10", tooltip="00:0F:7C:0D:D5:8A", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_111033)
                                                            ]
                                                        ),
                                                        # Row 4
                                                        nlxFT.Row(
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.6", tooltip="00:0F:7C:0F:82:79", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_111034),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.1", tooltip="00:0F:7C:0F:82:7E", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_111035),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.2", tooltip="00:0F:7C:0F:82:7D", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_111036),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.11", tooltip="00:0F:7C0F:83:0F", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_111037),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.13", tooltip="00:0F:7C:0F:82:CD", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_111040),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.17", tooltip="00:0F:7C:0F:9C:DA", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_111042)
                                                            ]
                                                        ),
                                                        # Row 5
                                                        nlxFT.Row(
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.4", tooltip="00:0F:7C:0F:82:80", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_111043),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.18", tooltip="00:0F:7C:0F:82:7A", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_111044),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.14", tooltip="00:0F:7C:0D:D5:B9", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_111045),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.21", tooltip="00:0F:7C:0F:68:9B", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_111046),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.20", tooltip="00:0F:7C:0F:9C:EA", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_111048),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.28", tooltip="00:0F:7C:0F:9C:E8", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_11202)
                                                            ]
                                                        ),
                                                        # Row 6
                                                        nlxFT.Row(
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF65", tooltip="00:0F:7C:0F:9C:BA", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_11203),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.59", tooltip="00:0F:7C:0F:1F:E7", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_11204),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.25", tooltip="00:0F:7C:0F:9C:E9", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_11206),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF58", tooltip="3C:EF:8C:C5:06:11", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_11208),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.38", tooltip="00:0F:7C:0::68:9D", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_11209),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.37", tooltip="00:0F:7C:0F:68:99", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112010)
                                                            ]
                                                        ),
                                                        # Row 7
                                                        nlxFT.Row(
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.40", tooltip="00:0F:7C:0E:E1:E8", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112011),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF61", tooltip="00:0F:7C:0F:9C:BB", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112013),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.55", tooltip="00:0F:7C:0F:20:0B", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112014),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.26", tooltip="00:0F:7C:0F:9C:B3", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112016),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.58", tooltip="00:0F:7C:0E:0E:50", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112017),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.32", tooltip="00:0F:7C:0F:98:68", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112020)
                                                            ]
                                                        ),
                                                        # Row 8
                                                        nlxFT.Row(
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF60", tooltip="00:0F:7C:0F:9C:B9", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112021),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.52", tooltip="00:0F:7C:0F:1F:E5", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112022),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.56", tooltip="00:0F:7C:0E:E1:BC", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112023),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.35", tooltip="00:0F:7C:0F:9C:D5", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112024),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.60", tooltip="3C:EF:8C:C5:06:4B", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112025),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.24", tooltip="00:0F:7C:0F:98:7D", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112026)
                                                            ]
                                                        ),
                                                        # Row 9
                                                        nlxFT.Row(
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.34", tooltip="00:0F:7C:0F:9C:D7", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112027),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.16", tooltip="00:0F:7C:0F:82:7C", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112028),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.53", tooltip="00:0F:7C:0D:FA:85", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112029),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.43", tooltip="00:0F:7C:0F:9C:C1", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112030),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.12", tooltip="00:0F:7C:0D:D5:C1", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112031),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.22", tooltip="00:0F:7C:0F:82:7B", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112032)
                                                            ]
                                                        ),
                                                        # Row 10
                                                        nlxFT.Row(
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.67", tooltip="00:0F:7C:10:95:9F", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112033),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.30", tooltip="00:0F:7C:0F:9C:C0", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112034),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.3", tooltip="00:0F:7C:0F:82:7F", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112035),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.5", tooltip="00:0F:7C:0C:74:C8", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112036),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.41", tooltip="00:0F:7C:0F:68:A0", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112038),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.48", tooltip="00:0F:7C:0F:68:9F", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112040)
                                                            ]
                                                        ),
                                                        # Row 11
                                                        nlxFT.Row(
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.49", tooltip="00:0F:7C:0C:75:0C", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_112042),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.23", tooltip="00:0F:7C:0F:9C:DC", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_113011),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.39", tooltip="00:0F:7C:0E:E1:ED", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_113013),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.62", tooltip="00:0F:7C:0F:20:17", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_113015),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.31", tooltip="00:0F:7C:0F:9C:D8", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_113017),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.36", tooltip="00:0F:7C:0F:9C:BD", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_113019)
                                                            ]
                                                        ),
                                                        # Row 12
                                                        nlxFT.Row(
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.33", tooltip="00:0F:7C:0F:9C:D3", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_113033),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.63", tooltip="00:0F:7C:0F:3B:CF", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_113034),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.47", tooltip="00:0F:7C:0D:FA:88", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_113036),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.27", tooltip="00:0F:7C:0F:9C:D1", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_113037),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF66", tooltip="00:0F:7C:0D:FA:8B", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_113038),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.29", tooltip="00:0F:7C:0F:9C:D4", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_113039)
                                                            ]
                                                        ),
                                                        # Row 13
                                                        nlxFT.Row(
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.64", tooltip="00:0F:7C:0D:D5:C2", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_113040),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.44", tooltip="00:0F:7C:0D:FA:E1", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_113041),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF67", tooltip="00:0:7C:10:90:62", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_113042),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.45", tooltip="00:0F:7C:0E:E1:DC", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_113043),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.50", tooltip="00:0F:7C:0F:68:9C", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_113044),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.46", tooltip="00:0F:7C:0E:E2:0D", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_113045)
                                                            ]
                                                        )
                                                    ]
                                                )
                                            )
                                        ),
                                        # HQ 8th Floor IDF Room Camera Keys
                                        nlxFT.Tab(icon=nlxFT.icons.MEETING_ROOM_ROUNDED, text="IDF Room",
                                            content=nlxFT.Container(
                                                # disabled=True,
                                                padding=15,
                                                content=nlxFT.Column(
                                                    controls=[
                                                        nlxFT.Row(
                                                            controls=[
                                                            nlxFT.Text(value="Nicosia, Demostheni Severi 33, 8th Floor IDF Room Cameras", size= 15, color="black")
                                                            ]
                                                        ),
                                                        # Row 1
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF31", tooltip="00:0F:7C:0F:9C:C8", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_14101),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF5", tooltip="00:0F:7C:0F:83:2C", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_14102),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF35", tooltip="00:0F:7C:0F:9C:C7", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_14103),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF3", tooltip="00:0F:7C:0F:83:2B", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_14104),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF38", tooltip="00:0F:7C:0F:9C:D0", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_14105),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF29", tooltip="MAC Address N/A", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_14106)
                                                            ]
                                                        ),
                                                        # Row 2
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF43", tooltip="00:0F:7C:0F:83:00", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_14107),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF45", tooltip="00:0F:7C:0F:82:FB", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_14109),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF51", tooltip="00:0F:7C:0E:E1:E7", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141010),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF40", tooltip="00:0F:7C:0F:9C:83", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141011),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF33", tooltip="00:0F:7C:0F:9C:82", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141013),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.7", tooltip="00:0F:7C:0F:82:D0", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141014)
                                                            ]
                                                        ),
                                                        # Row 3
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF26", tooltip="00:0F:7C:0E:E1:FE", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141015),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF50", tooltip="00:0F:7C:0F:82:FD", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141017),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF9", tooltip="00:0F:7C:0F:83:2D", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141018),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF42", tooltip="00:0F:7C:0F:82:FC", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141019),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF27", tooltip="00:0F:7C:0E:E1:FC", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141020),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF37", tooltip="00:0F:7C:0F:9C:86", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141021)
                                                            ]
                                                        ),
                                                        # Row 4
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF68", tooltip="00:18:AE:9E:79:B4", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141022),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF39", tooltip="00:0F:7C:0F:9C:84", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141023),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF69", tooltip="00:18:AE:9E:79:71", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141024),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF53", tooltip="00:0F:7C:0F:9C:D2", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141025),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF10", tooltip="00:0f:7C:0F:83:0C", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141027),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF11", tooltip="00:0f:7C:0F:82:FA", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141029)
                                                            ]
                                                        ),
                                                        # Row 5
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF36", tooltip="00:0F:7C:0F:9C:CD", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141031),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF52", tooltip="00:0F:7C:10:95:93", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141033),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF32", tooltip="00:0F:7C:0F.9C:CC", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141035),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF7", tooltip="00:0F:7C:0F:83:31", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141037),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF1", tooltip="00:0F:7C:0F:83:2F", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141039),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF41", tooltip="00:0F:7C:0F:9C:CE", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141041)
                                                            ]
                                                        ),
                                                        # Row 6
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF30", tooltip="00:0F:7C:0F:9C:CF", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141043),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF16", tooltip="00:0F:7C:0D:FA:94", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141044),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF56", tooltip="00:0F:7C:0F:9C:CA", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141045),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF19", tooltip="00:0F:7C:0F:82:B0", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_141046),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF8", tooltip="00:0F:7C:0F:82:AB", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_14201),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF21", tooltip="00:50:F9:01:42:FA", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_14203)
                                                            ]
                                                        ),
                                                        # Row 7
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF12", tooltip="3C:EF:8C:C4:CE:05", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_14205),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF14", tooltip="00:0F:7C:0D:D5:BA", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_14207),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ8", tooltip="00:0F:7C:0F:83:0E", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_142010),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF44", tooltip="00:0F:7C:0F:9C:B2", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_142011),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF22", tooltip="00:0F:7C:0F:9C:C2", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_142013),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF25", tooltip="00:0F:7C:0F:9C:BE", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_142015)
                                                            ]
                                                        ),
                                                        # Row 8
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF55", tooltip="00:0F:7C:0F:82:CF", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_142017),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF2", tooltip="00:0F:7C:0F:83:2E", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_142018),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF28", tooltip="00:0F:7C:0F:9C:BF", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_142019),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF57", tooltip="00:0F:7C:0F:82:A9", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_142021),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF15", tooltip="00:0F:7C:0D:FA:8E", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_142022), # QA - Renamed
                                                                nlxFT.ElevatedButton(text="GHQ.IDF18", tooltip="00:0F:7C:0F:83:2A", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_142025)
                                                            ]
                                                        ),
                                                        # Row 9
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF54", tooltip="00:0F:7C:0F:83:0A", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_142027),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF20", tooltip="00:0F:7C:0F:82:AA", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_142028),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF23", tooltip="00:0F:7C:0E:E2:00", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_142032),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF34", tooltip="00:0F:7C:0F:9C:C5", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_142033),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF17", tooltip="00:0F:7C:0F:82:AE", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_142035),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF13", tooltip="00:0F:7C:0D:D5:8B", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_142036)
                                                            ]
                                                        ),
                                                        # Row 9
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF4", tooltip="00:0F:7C:0F:83:30", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_142037),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF24", tooltip="00:0F:7C:0E:E1:FF", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_142038),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF6", tooltip="00:0F:7C:0F:82:AF", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_142040),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF64", tooltip="58:5B:69:1A:3E:66", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_11205)
                                                            ]
                                                        )
                                                    ]
                                                )
                                            )
                                        ),
                                        # Old HQ Camera Keys
                                        nlxFT.Tab(icon=nlxFT.icons.HOME_WORK_ROUNDED, text="Old HQ", 
                                            content=nlxFT.Container(
                                                # disabled=True,
                                                padding=15,
                                                content=nlxFT.Column(
                                                    controls=[
                                                        nlxFT.Row(
                                                            controls=[
                                                            nlxFT.Text(value="Nicosia, Nicosia, Agion Omologiton Ave. 105 Cameras", size= 15, color="black")
                                                            ]
                                                        ),
                                                        # Row 1
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="OHQ8", tooltip="00:0F:7C:0E:E1:F4", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_13101),
                                                                nlxFT.ElevatedButton(text="OHQ17", tooltip="00:0F:7C:0E:E1:7B", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_13102),
                                                                nlxFT.ElevatedButton(text="OHQ7", tooltip="00:0F:7C:0E:0C:CF", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_13103),
                                                                nlxFT.ElevatedButton(text="OHQ3", tooltip="00:0F:7C:0E:0E:4D", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_13104),
                                                                nlxFT.ElevatedButton(text="OHQ5", tooltip="00:0F:7C:0D:FA:F4", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_13105),
                                                                nlxFT.ElevatedButton(text="OHQ19", tooltip="00:0F:7C:0E:0E:4F", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_13106)
                                                            ]
                                                        ),
                                                        # Row 2
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="OHQ6", tooltip="00:0F:7C:0D:FA:F7", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_13107),
                                                                nlxFT.ElevatedButton(text="OHQ20", tooltip="00:18:AE:C2:15:1A", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_13108),
                                                                nlxFT.ElevatedButton(text="OHQ10", tooltip="00:0F:7C:0E:1:F7", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_13109),
                                                                nlxFT.ElevatedButton(text="OHQ4", tooltip="00:0F:7C:0E:E1:E0", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_131011),
                                                                nlxFT.ElevatedButton(text="OHQ9", tooltip="00:0F:7C:0E:E1:DD", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_131013),
                                                                nlxFT.ElevatedButton(text="OHQ11", tooltip="00:18:AE:9E:79:4C", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_131015)
                                                            ]
                                                        ),
                                                        # Row 3
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="OHQ1", tooltip="00:0F:7C:0E:E1:89", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_131017),
                                                                nlxFT.ElevatedButton(text="OHQ12", tooltip="00:0F:7C:0E:E1:AB", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_131019),
                                                                nlxFT.ElevatedButton(text="OHQ18", tooltip="00:0F:7C:0E:E1:F9", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_131021),
                                                                nlxFT.ElevatedButton(text="OHQ16", tooltip="00:0F:7C:0E:E1:F5", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_131039),
                                                                nlxFT.ElevatedButton(text="OHQ15", tooltip="00:0F:7C:0E:E1:F8", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_131041),
                                                                nlxFT.ElevatedButton(text="OHQ14", tooltip="MAC Address N/A", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_131043)
                                                            ]
                                                        ),
                                                        # Row 3
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="OHQ13", tooltip="00:0F:7C:0E:E1:F6", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_131047) # QA - Added
                                                            ]
                                                        )
                                                    ]
                                                )
                                            )
                                        ),
                                        # Corner House Camera Keys
                                        nlxFT.Tab(icon=nlxFT.icons.HOUSE_SIDING_ROUNDED, text="Corner House", 
                                            content=nlxFT.Container(
                                                # disabled=True,
                                                padding=15,
                                                content=nlxFT.Column(
                                                    controls=[
                                                        nlxFT.Row(
                                                            controls=[
                                                            nlxFT.Text(value="Nicosia, Demostheni Severi 31, Corner House Cameras", size= 15, color="black")
                                                            ]
                                                        ),
                                                        # Row 1
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="CRN.5", tooltip="00:0F:7C:0D:09:45", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_20102),
                                                                nlxFT.ElevatedButton(text="CRN.7", tooltip="00:0F:7C:0D:08:AF", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_20103),
                                                                nlxFT.ElevatedButton(text="CRN.10", tooltip="00:0F:7C:0D:09:4D", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_20104),
                                                                nlxFT.ElevatedButton(text="CRN.9", tooltip="00:0F:7C:0C:83:59", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_20105),
                                                                nlxFT.ElevatedButton(text="CRN.6", tooltip="00:0F:7C:10:95:AE", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_20106),
                                                                nlxFT.ElevatedButton(text="CRN.1", tooltip="00:0F:7C:0D:FB:12", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_20107)
                                                            ]
                                                        ),
                                                        # Row 2
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="CRN.4", tooltip="00:0F:7C:0D:FB:11", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_20108),
                                                                nlxFT.ElevatedButton(text="CRN.12", tooltip="00:0F:7C:10:95:A7", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_20109),
                                                                nlxFT.ElevatedButton(text="CRN.2", tooltip="00:0F:7C:0E:E1:F1", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_201010),
                                                                nlxFT.ElevatedButton(text="CRN.3", tooltip="00:0F:7C:0D:08:D2", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_201011),
                                                                nlxFT.ElevatedButton(text="CRN.8", tooltip="00:0F:7C:0D:08:D2", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_201012),
                                                                nlxFT.ElevatedButton(text="CRN.13", tooltip="00:0F:7C:0D:08:D2", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_201013)
                                                            ]
                                                        ),
                                                        # Row 3
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="CRN.11", tooltip="00:0F:7C:10.95ab", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_201014)
                                                            ]
                                                        )
                                                    ]
                                                )
                                            )
                                        ),
                                        # Demostheni Severi Parking 1 Camera Keys
                                        nlxFT.Tab(icon=nlxFT.icons.GARAGE_ROUNDED, text="Parking 1", 
                                            content=nlxFT.Container(
                                                # disabled=True,
                                                padding=15,
                                                content=nlxFT.Column(
                                                    controls=[
                                                        nlxFT.Row(
                                                            controls=[
                                                            nlxFT.Text(value="Nicosia, Demostheni Severi 7, Parking 1 Cameras", size= 15, color="black")
                                                            ]
                                                        ),
                                                        # Row 1
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="PRK1.1", tooltip="00:0F:7C:0E:0D:47 (hosted at OHQ)", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_4104),
                                                                # nlxFT.ElevatedButton(text="OHQ.PRK1.1", tooltip="00:0F:7C:0E:0D:47", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_4104),
                                                                nlxFT.ElevatedButton(text="PRK1.2", tooltip="00:0F:7C:0E:0D:49 (hosted at OHQ)", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_4107),
                                                                # nlxFT.ElevatedButton(text="OHQ.PRK1.2", tooltip="00:0F:7C:0E:0D:49", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_4107),
                                                                nlxFT.ElevatedButton(text="PRK1.3", tooltip="00:0F:7C:10:95:51 (hosted at OHQ)", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_4103),
                                                                # nlxFT.ElevatedButton(text="OHQ.PRK1.3", tooltip="00:0F:7C:10:95:51", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_4103),
                                                                nlxFT.ElevatedButton(text="PRK1.4", tooltip="00:0F:7C:0E:E1:F6 (hosted at OHQ)", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_4102),
                                                                # nlxFT.ElevatedButton(text="OHQ.PRK1.4", tooltip="00:0F:7C:0E:E1:F6", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_4102),
                                                                nlxFT.ElevatedButton(text="PRK1.5", tooltip="3C:EF:8C:C5:06:24 (hosted at OHQ)", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_4101),
                                                                # nlxFT.ElevatedButton(text="OHQ.PRK1.5", tooltip="3C:EF:8C:C5:06:24", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_4101),
                                                                nlxFT.ElevatedButton(text="PRK1.6", tooltip="3C:EF:8C:C5:06:0C (hosted at OHQ)", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_4108)
                                                                # nlxFT.ElevatedButton(text="OHQ.PRK1.6", tooltip="3C:EF:8C:C5:06:0C", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_4108)
                                                            ]
                                                        ),
                                                        # Row 2
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="PRK1.9", tooltip="00:0F:7C:0E:0D:47 (hosted at OHQ)", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_4106) # Test asset
                                                                # nlxFT.ElevatedButton(text="OHQ.PRK1.9", tooltip="00:0F:7C:0E:0D:47", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_4106) # Test asset
                                                            ]
                                                        )
                                                    ]
                                                )
                                            )
                                        ),
                                        # Protaras House H1 Camera Keys
                                        nlxFT.Tab(icon=nlxFT.icons.HOME_ROUNDED, text="H1", 
                                            content=nlxFT.Container(
                                                # disabled=True,
                                                padding=15,
                                                content=nlxFT.Column(
                                                    controls=[
                                                        nlxFT.Row(
                                                            controls=[
                                                            nlxFT.Text(value="Protaras, Kavo Gkreko, 531A Lombardi Gardens, Villa No.5 Cameras", size= 15, color="black")
                                                            ]
                                                        ),
                                                        # Row 1
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="H1.6", tooltip="00:0F:7C:0E:E1:7A", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_3101),
                                                                nlxFT.ElevatedButton(text="H1.3", tooltip="00:0F:7C:0E:E1:E5", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_3102),
                                                                nlxFT.ElevatedButton(text="H1.8", tooltip="00:0F:7C:0E:E1:7D", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_3103),
                                                                nlxFT.ElevatedButton(text="H1.9", tooltip="00:0F:7C:0E:E1:7F", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_3104),
                                                                nlxFT.ElevatedButton(text="H1.7", tooltip="00:0F:7C:0E:E1:fA", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_3105),
                                                                nlxFT.ElevatedButton(text="H1.10", tooltip="00:0F:7C:0E:E1:E1", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_3106)
                                                            ]
                                                        ),
                                                        # Row 2
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="H1.2", tooltip="00:0F:7C:0E:E1:F3", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_3107),
                                                                nlxFT.ElevatedButton(text="H1.11", tooltip="00:18:AE:A7:2A:DD", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_3108),
                                                                nlxFT.ElevatedButton(text="H1.4", tooltip="00:0F:7C:0E:E1:C7", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_31010),
                                                                nlxFT.ElevatedButton(text="H1.5", tooltip="00:0F:7C:0E:E1:7E", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_31011),
                                                                nlxFT.ElevatedButton(text="H1.1", tooltip="00:0F:7C:0E:E1:DA", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_31012)
                                                            ]
                                                        )
                                                    ]
                                                )
                                            )
                                        ),
                                        # Strovolos H2 Camera Keys
                                        nlxFT.Tab(icon=nlxFT.icons.HOME_ROUNDED, text="H2", 
                                            content=nlxFT.Container(
                                                # disabled=True,
                                                padding=15,
                                                content=nlxFT.Column(
                                                    controls=[
                                                        nlxFT.Row(
                                                            controls=[
                                                            nlxFT.Text(value="Nicosia, Strovolos, Finea 7 Cameras", size= 15, color="black")
                                                            ]
                                                        ),
                                                        # Row 1
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="H2.2", tooltip="00:0F:7C:0F:9C:DB", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_40101),
                                                                nlxFT.ElevatedButton(text="H2.14", tooltip="00:0F:7C:0F:9C:8F", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_40105),
                                                                nlxFT.ElevatedButton(text="H2.7", tooltip="00:0F:7C:0F:9C:8D", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_40106),
                                                                nlxFT.ElevatedButton(text="H2.9", tooltip="00:0F:7C:0F:9C:95", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_40108),
                                                                nlxFT.ElevatedButton(text="H2.8", tooltip="00:0F:7C:0F:9C:8B", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_40109),
                                                                nlxFT.ElevatedButton(text="H2.6", tooltip="00:0F:7C:0F:9C:89", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_401017)
                                                            ]
                                                        ),
                                                        # Row 2
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="H2.10", tooltip="00:0F:7C:0F:9C:94", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_401019),
                                                                nlxFT.ElevatedButton(text="H2.19", tooltip="00:0F:7C:0F:9C:93", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_401023),
                                                                nlxFT.ElevatedButton(text="H2.20", tooltip="00:0F:7C:0D:08:D5", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_41017),
                                                                nlxFT.ElevatedButton(text="H2.21", tooltip="3C:EF:8C:C5:06:3D", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_41019),
                                                                nlxFT.ElevatedButton(text="H2.12", tooltip="00:0F:7C:0F:20:04", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_41021),
                                                                nlxFT.ElevatedButton(text="H2.18", tooltip="00:0F:7C:0F:20:05", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_41022)
                                                            ]
                                                        ),
                                                        # Row 3
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="H2.16", tooltip="00:0F:7C:0F:9C:B6", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_41023),
                                                                nlxFT.ElevatedButton(text="H2.17", tooltip="00:0F:7C:0F:20:03", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_41024)
                                                            ]
                                                        ),
                                                    ]
                                                )
                                            )
                                        ),
                                        nlxFT.Tab(icon=nlxFT.icons.HOME_ROUNDED, text="H3", 
                                            content=nlxFT.Container(
                                                # disabled=True,
                                                padding=15,
                                                content=nlxFT.Column(
                                                    controls=[
                                                        nlxFT.Row(
                                                            controls=[
                                                            nlxFT.Text(value="Nicosia, Strovolos, Angaiou 1 Cameras", size= 15, color="black")
                                                            ]
                                                        ),
                                                        # Row 1
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="H3.16", tooltip="00:0F:7C:10.95:67", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_72017),
                                                                nlxFT.ElevatedButton(text="H3.21", tooltip="3C:EF:8C:C5:05:FD", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_72018),
                                                                nlxFT.ElevatedButton(text="H3.2", tooltip="00:0F:7C:0E:0D:23", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_72019),
                                                                nlxFT.ElevatedButton(text="H3.17", tooltip="3C:EF:8C:C5:06:1B", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_72020),
                                                                nlxFT.ElevatedButton(text="H3.20", tooltip="3C:EF:8C:65:6A:D8", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_72021),
                                                                nlxFT.ElevatedButton(text="H3.18", tooltip="3C:EF:8C:C5:06:1A", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_72022)
                                                            ]
                                                        ),
                                                        # Row 2
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="H3.14", tooltip="00:0F:7C:0E:0E:2D", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_72023),
                                                                nlxFT.ElevatedButton(text="H3.9", tooltip="00:0F:7C:0E:0C:CB", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_73017),
                                                                nlxFT.ElevatedButton(text="H3.8", tooltip="00:0F:7C:0E:0D:80", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_73018),
                                                                nlxFT.ElevatedButton(text="H3.13", tooltip="00:0F:7C:0E:0C:CE", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_73019),
                                                                nlxFT.ElevatedButton(text="H3.15", tooltip="00:0F:7C:0E:0E:36", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_73020),
                                                                nlxFT.ElevatedButton(text="H3.5", tooltip="00:0F:7C:0E:0D:7D", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_73021)
                                                            ]
                                                        ),
                                                        # Row 3
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="H3.19", tooltip="3C:EF:8C:65:6ACF", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_73022),
                                                                nlxFT.ElevatedButton(text="H3.3", tooltip="00:0F:7C:0E:0C:CA", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_73023),
                                                                nlxFT.ElevatedButton(text="H3.6", tooltip="3C:EF:8C:C5:06:23", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_73024),
                                                                nlxFT.ElevatedButton(text="H3.4", tooltip="3C:EF:8C:C5:06:1E", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_74017),
                                                                nlxFT.ElevatedButton(text="H3.12", tooltip="00:0F:7C:0E:0C:CD", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_74018),
                                                                nlxFT.ElevatedButton(text="H3.10", tooltip="00:0F:7C:0E:0D:25", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_74020)
                                                            ]
                                                        ),
                                                        # Row 4
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="H3.1", tooltip="00:0F:7C:0E:0D:21", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_74021),
                                                                nlxFT.ElevatedButton(text="H3.7", tooltip="00:0F:7C:0E:0C:CC", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_74022),
                                                                nlxFT.ElevatedButton(text="H3.11", tooltip="00:0F:7C:0E:0D:7C", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_74023)
                                                            ]
                                                        )
                                                    ]
                                                )
                                            )
                                        ),
                                        nlxFT.Tab(icon=nlxFT.icons.HOME_ROUNDED, text="H4", 
                                            content=nlxFT.Container(
                                                # disabled=True,
                                                padding=15,
                                                content=nlxFT.Column(
                                                    controls=[
                                                        nlxFT.Row(
                                                            controls=[
                                                            nlxFT.Text(value="Nicosia, Strovolos, Pangaiou 8 Cameras", size= 15, color="black")
                                                            ]
                                                        ),
                                                        # Row 1
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="H4.10", tooltip="00:0F:7C:0E:0E:28", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_100017),
                                                                nlxFT.ElevatedButton(text="H4.8", tooltip="00:0F:7C:0E:0E:35", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_100019),
                                                                nlxFT.ElevatedButton(text="H4.4", tooltip="00:0F:7C:10.95:92", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_100021),
                                                                nlxFT.ElevatedButton(text="H4.9", tooltip="00:0F:7C:0E:0E:2D", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_100023),
                                                                nlxFT.ElevatedButton(text="H4.3", tooltip="00:0F:7C:10:95:A2", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_101017),
                                                                nlxFT.ElevatedButton(text="H4.2", tooltip="3C:EF:8C:65:6A:CE", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_101018)
                                                            ]
                                                        ),
                                                        # Row 2
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="H4.1", tooltip="00:0F:7C:0E:0E:2A", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_101020),
                                                                nlxFT.ElevatedButton(text="H4.5", tooltip="00:0F:7C:0E:0E:2C", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_101022),
                                                                nlxFT.ElevatedButton(text="H4.7", tooltip="00:0F:7C:0E:E1:F0", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=178, on_click=rbt_CSC_101024)
                                                            ]
                                                        )
                                                    ]
                                                )
                                            )
                                        )
                                    ]
                                )
                            ]
                        )
                    ),
                    nlxFT.Container(
                        bgcolor="white",
                        content=nlxFT.Row(
                            expand=True, height=30, alignment=nlxFT.MainAxisAlignment.CENTER,
                            # self-control instances added here:
                            controls=[
                            nlxFT.ElevatedButton(
                                    text="Simulate/Test Reload", 
                                    icon=nlxFT.icons.DONE_ROUNDED, 
                                    bgcolor=nlxFT.colors.BLUE_GREY_100, 
                                    color=nlxFT.colors.BLACK, 
                                    expand=1,
                                    on_click=SIM_rbt_CSC_4106,
                                    style=nlxFT.ButtonStyle(
                                        shape=nlxFT.RoundedRectangleBorder(radius=4)
                                    )
                                )
                            ,
                            nlxFT.ElevatedButton(
                                    text="Full System Test", 
                                    icon=nlxFT.icons.DONE_ALL_ROUNDED, 
                                    bgcolor=nlxFT.colors.BLUE_GREY_100, 
                                    color=nlxFT.colors.BLACK, 
                                    expand=1, 
                                    on_click=SIM_FullTest,
                                    style=nlxFT.ButtonStyle(
                                        shape=nlxFT.RoundedRectangleBorder(radius=4)
                                    )
                                ),
                            nlxFT.ElevatedButton(
                                    text="Actions Record", 
                                    icon=nlxFT.icons.PENDING_ACTIONS_ROUNDED, 
                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                    color=nlxFT.colors.BLACK,
                                    expand=1, 
                                    on_click=open_dlg_modal_Story,
                                    style=nlxFT.ButtonStyle(
                                        shape=nlxFT.RoundedRectangleBorder(radius=4)
                                    )
                                )
                            ]
                        )
                    ),
                    nlxFT.Container(
                        bgcolor="#081d33", 
                        border_radius=nlxFT.border_radius.only(
                            bottom_left=10, 
                            bottom_right=10, 
                            top_left=4, 
                            top_right=4), 
                            padding=nlxFT.padding.only(left=15, right=15), 
                            content=nlxFT.Row(expand=True, height=50,
                            alignment=nlxFT.MainAxisAlignment.START, 
                            controls=[status]
                        )
                    )
                ]
            )
        )
    )
# Main page definition END

# Set logging level
logging.getLogger("flet_core").setLevel(logging.INFO)

nlxFT.app(target=main)

# NLXComments Post-Ver
"""
Beta Ver. of CRAcc2CSC Show Release: 2.3.1
Assets (to this version):
Inherited from 2.2.5
New Assets (to this version): None
Expectations (to this version): Wider search engine. Returns up to 12 results instead of just 10
Improvments (on functions to this version): QA of version 2.2.X and clean wider search
State: Good
Result: Healthy
References:
https://jira.wargaming.net/browse/INTCY-5250
"""
