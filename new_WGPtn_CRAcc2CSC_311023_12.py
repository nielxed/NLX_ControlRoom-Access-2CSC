# NLX Swrd: CRAcc2CSC (code name: Lothlorien)
# Version: Celeborn
import flet as nlxFT
import Cgpt_VerAcc_31123_cl as Vrfr
import Cgpt_ENG101_71123_cl as CSCRldr
import time
"""
A material design alert dialog.
An alert dialog informs the user about situations that require acknowledgement. 
An alert dialog has an optional title and an optional list of actions. The title is displayed
above the content and the actions are displayed below the content.
"""

# Main Flet software for CR actions described in footer refference.
"""
This main softy is of type NLXSword
"""

# Global definistions START
MSG1 = "Invalid username and/or password!"
MSG2 = "Please log in before you can perform actions."
userNameCR = ""                                                                                 # Initialize a username string glb
userNameCPT = nlxFT.TextField(label="Username", width=250, border_color="white")                # Password text-field defined off-definition glb
global passWordCR
passWordCR = ""                                                                                 # Initialize a password string glb
passWordCPT = nlxFT.TextField(label="Password", width=250, border_color="white", password=True) # Password text-field defined off-definition glb and set to hidden
CRStatus = nlxFT.Text(value="notInit")
status = nlxFT.Text(value="Welcome! Please Login.", size= 15, color="white")
# Global definistions END

# Global setters START
def setChecker_Out():
    global inMain_loginChecker
    inMain_loginChecker = 0

def setChecker_In():
    global inMain_loginChecker
    inMain_loginChecker = 1

def setUserName_Global(USR):
    global inGlobal_User
    inGlobal_User = USR

def setPassWord_Global(PSW):
    global inGlobal_PassWord
    inGlobal_PassWord = PSW

def setHost4Cam_Global(HST):
    global inGlobal_Host
    inGlobal_Host = HST

def setInt4Cam_Global(INT):
    global inGlobal_Interface
    inGlobal_Interface = INT

def setDesc4Cam_Global(DESC):
    global inGlobal_CamDescription
    inGlobal_CamDescription = DESC

def sureVAR_Global(SR):
    global rbtCSCInt
    rbtCSCInt = 0
# Global setters END

# Global definitions START
def reset_Creds():
    userNameCPT.value = ""
    passWordCPT.value = ""

def app_Header_Brand():
        return nlxFT.Container(
            content=nlxFT.Row(
                controls=[
                nlxFT.Icon(name=nlxFT.icons.LOCAL_FIRE_DEPARTMENT_ROUNDED, color="white"),
                nlxFT.Text("Celeborn 0.1.2", size=15, color="white")
                ]
            )
        )
# Global definitions END

# Main page definition START
def main(page: nlxFT.Page):
    # Page initializers
    page.bgcolor = "#fdfdfd"
    page.padding = 20
    page.window_height = 1270
    page.window_width = 1200
    page.window_maximizable = False
    page.window_maximized = False
    page.window_resizable = False
    page.window_center()
    page.title = "Lothlorien"
    
    # inMain initializers
    setChecker_Out()
    setDesc4Cam_Global("")

    def app_Header_Search():
        return nlxFT.Container(
            width=320,
            padding=8,
            bgcolor='white10',
            border_radius=6,
            animate_opacity=320,            
            content=nlxFT.Row(
                spacing=10,
                vertical_alignment=nlxFT.CrossAxisAlignment.CENTER,
                controls=[
                    nlxFT.Icon(name=nlxFT.icons.SEARCH_ROUNDED, size=17, opacity=0.85),
                    # TextField not defined (134507062023)
                    nlxFT.Text("Search", size=14, color="#6A7784")
                ]
            )
        )

    def app_Header_Avatar():
        return nlxFT.Container(
            content=nlxFT.IconButton(nlxFT.icons.PERSON_2_ROUNDED, on_click=open_dlg_UserLogin, icon_color="white")
        )

    def login_dlg_UserLogin(e):
        userNameCR = userNameCPT.value
        # passWordCR = passWordCPT.value
        host = "192.168.201.4"
        port = 22  # or the port you use for SSH
        timeout = 10  # you can adjust the timeout value if necessary
        close_dlg_UserLogin(e)
        status.value = "Login in progress... Please Wait!"
        page.update()
        time.sleep(3)

        ssh_verifier = Vrfr.SSHVerifier(host, userNameCPT.value, passWordCPT.value, port, timeout)
        if ssh_verifier.verify_ssh_access():
            status.value = f"User {userNameCR} logged in successfully!"
            page.update()
            setUserName_Global(userNameCPT.value)
            setPassWord_Global(passWordCPT.value)
            setChecker_In()
            reset_Creds()
        else:
            open_dlg_ER(e)
            reset_Creds()
            # reset_BaseCreds()
            status.value = "Unable to login. Please try again!"
            page.update()

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
            setInt4Cam_Global("1/0/2")
            open_dlg_modal_VER(e)

    def rbt_CSC_11103(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.66")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/3")
            open_dlg_modal_VER(e)

    def rbt_CSC_11104(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.61")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/4")
            open_dlg_modal_VER(e)

    def rbt_CSC_11105(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF59")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/5")
            open_dlg_modal_VER(e)

    def rbt_CSC_11106(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.51")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/6")
            open_dlg_modal_VER(e)

    def rbt_CSC_11108(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.42")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/8")
            open_dlg_modal_VER(e)

    def rbt_CSC_11109(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF63")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/9")
            open_dlg_modal_VER(e)

    def rbt_CSC_111011(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF49")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/11")
            open_dlg_modal_VER(e)

    def rbt_CSC_111012(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.68")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/12")
            open_dlg_modal_VER(e)

    def rbt_CSC_111013(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.54")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/13")
            open_dlg_modal_VER(e)

    def rbt_CSC_111015(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF48")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/15")
            open_dlg_modal_VER(e)

    def rbt_CSC_111017(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF62")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/17")
            open_dlg_modal_VER(e)

    def rbt_CSC_111019(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF47")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/19")
            open_dlg_modal_VER(e)

    def rbt_CSC_111025(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.57")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/25")
            open_dlg_modal_VER(e)

    def rbt_CSC_111028(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.19")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/28")
            open_dlg_modal_VER(e)

    def rbt_CSC_111029(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.9")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/29")
            open_dlg_modal_VER(e)

    def rbt_CSC_111031(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.15")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/31")
            open_dlg_modal_VER(e)

    def rbt_CSC_111033(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.10")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/33")
            open_dlg_modal_VER(e)

    def rbt_CSC_111034(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.6")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/34")
            open_dlg_modal_VER(e)

    def rbt_CSC_111035(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.1")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/35")
            open_dlg_modal_VER(e)

    def rbt_CSC_111036(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.2")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/36")
            open_dlg_modal_VER(e)

    def rbt_CSC_111037(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.11")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/37")
            open_dlg_modal_VER(e)

    def rbt_CSC_111040(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.13")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/40")
            open_dlg_modal_VER(e)

    def rbt_CSC_111042(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.17")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/42")
            open_dlg_modal_VER(e)

    def rbt_CSC_111043(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.4")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/43")
            open_dlg_modal_VER(e)

    def rbt_CSC_111044(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.18")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/44")
            open_dlg_modal_VER(e)

    def rbt_CSC_111045(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.14")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/45")
            open_dlg_modal_VER(e)

    def rbt_CSC_111046(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.21")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/46")
            open_dlg_modal_VER(e)

    def rbt_CSC_111048(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.20")
            setHost4Cam_Global("192.168.77.11")
            setInt4Cam_Global("1/0/48")
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
            setInt4Cam_Global("1/0/1")
            open_dlg_modal_VER(e)

    def rbt_CSC_14102(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF5")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/2")
            open_dlg_modal_VER(e)

    def rbt_CSC_14103(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF35")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/3")
            open_dlg_modal_VER(e)

    def rbt_CSC_14104(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF3")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/4")
            open_dlg_modal_VER(e)

    def rbt_CSC_14105(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF38")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/5")
            open_dlg_modal_VER(e)

    def rbt_CSC_14106(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF29")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/6")
            open_dlg_modal_VER(e)

    def rbt_CSC_14107(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF43")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/7")
            open_dlg_modal_VER(e)

    def rbt_CSC_14109(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF45")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/9")
            open_dlg_modal_VER(e)

    def rbt_CSC_141010(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF51")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/10")
            open_dlg_modal_VER(e)

    def rbt_CSC_141011(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF40")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/11")
            open_dlg_modal_VER(e)

    def rbt_CSC_141013(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF33")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/13")
            open_dlg_modal_VER(e)

    def rbt_CSC_141014(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ.7")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/14")
            open_dlg_modal_VER(e)

    def rbt_CSC_141015(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF26")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/15")
            open_dlg_modal_VER(e)

    def rbt_CSC_141017(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF50")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/17")
            open_dlg_modal_VER(e)

    def rbt_CSC_141018(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF9")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/18")
            open_dlg_modal_VER(e)

    def rbt_CSC_141019(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF42")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/19")
            open_dlg_modal_VER(e)

    def rbt_CSC_141020(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF27")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/20")
            open_dlg_modal_VER(e)

    def rbt_CSC_141021(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF37")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/21")
            open_dlg_modal_VER(e)

    def rbt_CSC_141022(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF68")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/22")
            open_dlg_modal_VER(e)

    def rbt_CSC_141023(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF39")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/23")
            open_dlg_modal_VER(e)

    def rbt_CSC_141024(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF69")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/24")
            open_dlg_modal_VER(e)

    def rbt_CSC_141025(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF53")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/25")
            open_dlg_modal_VER(e)

    def rbt_CSC_141027(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF10")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/27")
            open_dlg_modal_VER(e)

    def rbt_CSC_141029(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF11")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/29")
            open_dlg_modal_VER(e)

    def rbt_CSC_141031(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF36")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/31")
            open_dlg_modal_VER(e)

    def rbt_CSC_141033(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF52")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/33")
            open_dlg_modal_VER(e)

    def rbt_CSC_141035(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF32")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/35")
            open_dlg_modal_VER(e)

    def rbt_CSC_141037(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF7")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/37")
            open_dlg_modal_VER(e)

    def rbt_CSC_141039(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF1")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/39")
            open_dlg_modal_VER(e)

    def rbt_CSC_141041(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF41")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/41")
            open_dlg_modal_VER(e)

    def rbt_CSC_141043(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF30")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/43")
            open_dlg_modal_VER(e)

    def rbt_CSC_141044(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF16")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/44")
            open_dlg_modal_VER(e)

    def rbt_CSC_141045(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF56")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/45")
            open_dlg_modal_VER(e)

    def rbt_CSC_141046(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF19")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("1/0/46")
            open_dlg_modal_VER(e)

    def rbt_CSC_14201(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF8")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("2/0/1")
            open_dlg_modal_VER(e)

    def rbt_CSC_14203(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF21")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("2/0/3")
            open_dlg_modal_VER(e)

    def rbt_CSC_14205(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF12")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("2/0/5")
            open_dlg_modal_VER(e)

    def rbt_CSC_14207(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF14")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("2/0/7")
            open_dlg_modal_VER(e)

    def rbt_CSC_142010(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.MEZ8")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("2/0/10")
            open_dlg_modal_VER(e)

    def rbt_CSC_142011(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF44")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("2/0/11")
            open_dlg_modal_VER(e)

    def rbt_CSC_142013(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF22")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("2/0/13")
            open_dlg_modal_VER(e)

    def rbt_CSC_142015(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF25")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("2/0/15")
            open_dlg_modal_VER(e)

    def rbt_CSC_142017(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF55")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("2/0/17")
            open_dlg_modal_VER(e)

    def rbt_CSC_142018(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF2")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("2/0/18")
            open_dlg_modal_VER(e)

    def rbt_CSC_142019(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF28")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("2/0/19")
            open_dlg_modal_VER(e)

    def rbt_CSC_142021(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF57")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("2/0/21")
            open_dlg_modal_VER(e)

    def rbt_CSC_142022(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF14")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("2/0/22")
            open_dlg_modal_VER(e)

    def rbt_CSC_142025(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF18")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("2/0/25")
            open_dlg_modal_VER(e)

    def rbt_CSC_142027(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF54")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("2/0/27")
            open_dlg_modal_VER(e)

    def rbt_CSC_142028(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF20")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("2/0/28")
            open_dlg_modal_VER(e)

    def rbt_CSC_142032(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF23")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("2/0/32")
            open_dlg_modal_VER(e)

    def rbt_CSC_142033(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF34")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("2/0/33")
            open_dlg_modal_VER(e)

    def rbt_CSC_142035(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF17")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("2/0/35")
            open_dlg_modal_VER(e)

    def rbt_CSC_142036(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF13")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("2/0/36")
            open_dlg_modal_VER(e)

    def rbt_CSC_142037(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF4")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("2/0/37")
            open_dlg_modal_VER(e)

    def rbt_CSC_142038(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF24")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("2/0/38")
            open_dlg_modal_VER(e)

    def rbt_CSC_142040(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("GHQ GHQ.IDF6")
            setHost4Cam_Global("192.168.77.14")
            setInt4Cam_Global("2/0/40")
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
            setInt4Cam_Global("1/0/1")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_13102(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ17")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("1/0/2")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_13103(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ7")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("1/0/3")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_13104(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ3")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("1/0/4")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_13105(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ5")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("1/0/5")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_13106(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ19")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("1/0/6")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_13107(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ6")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("1/0/7")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_13108(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ20")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("1/0/8")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_13109(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ10")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("1/0/9")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_131011(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ4")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("1/0/11")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_131013(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ9")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("1/0/13")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_131015(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ11")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("1/0/15")
            open_dlg_modal_VER(e)
       
    def rbt_CSC_131017(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ1")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("1/0/17")
            open_dlg_modal_VER(e)
       
    def rbt_CSC_131019(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ12")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("1/0/19")
            open_dlg_modal_VER(e)
       
    def rbt_CSC_131021(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ18")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("1/0/21")
            open_dlg_modal_VER(e)
       
    def rbt_CSC_131039(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ16")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("1/0/15")
            open_dlg_modal_VER(e)
       
    def rbt_CSC_131041(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ15")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("1/0/15")
            open_dlg_modal_VER(e)
       
    def rbt_CSC_131043(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("WG OHQ OHQ14")
            setHost4Cam_Global("192.168.77.13")
            setInt4Cam_Global("1/0/43")
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
            setInt4Cam_Global("1/0/2")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_20103(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.7")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("1/0/3")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_20104(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.10")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("1/0/4")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_20105(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.9")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("1/0/5")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_20106(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.6")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("1/0/6")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_20107(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.1")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("1/0/7")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_20108(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.4")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("1/0/8")
            open_dlg_modal_VER(e)

    def rbt_CSC_20109(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.12")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("1/0/9")
            open_dlg_modal_VER(e)

    def rbt_CSC_201010(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.2")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("1/0/10")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_201011(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.3")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("1/0/11")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_201012(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.8")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("1/0/12")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_201013(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.13")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("1/0/13")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_201014(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Corner House CRN.11")
            setHost4Cam_Global("192.168.77.20")
            setInt4Cam_Global("1/0/14")
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
            setInt4Cam_Global("1/0/1")
            open_dlg_modal_VER(e)
    
    def rbt_CSC_4102(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Desmostheni Severi Parking 1 OHQ.PRK1.4")
            setHost4Cam_Global("192.168.201.4")
            setInt4Cam_Global("1/0/2")
            open_dlg_modal_VER(e)

    def rbt_CSC_4103(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Desmostheni Severi Parking 1 OHQ.PRK1.3")
            setHost4Cam_Global("192.168.201.4")
            setInt4Cam_Global("1/0/3")
            open_dlg_modal_VER(e)

    def rbt_CSC_4104(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Desmostheni Severi Parking 1 OHQ.PRK1.1")
            setHost4Cam_Global("192.168.201.4")
            setInt4Cam_Global("1/0/4")
            open_dlg_modal_VER(e)

    def rbt_CSC_4106(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Desmostheni Severi Parking 1 OHQ.PRK1.6")
            setHost4Cam_Global("192.168.201.4")
            setInt4Cam_Global("1/0/6")
            open_dlg_modal_VER(e)

    def rbt_CSC_4107(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Desmostheni Severi Parking 1 OHQ.PRK1.2")
            setHost4Cam_Global("192.168.201.4")
            setInt4Cam_Global("1/0/7")
            open_dlg_modal_VER(e)

    def rbt_CSC_4108(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Desmostheni Severi Parking 1 9OHQ.PRK1.6")
            setHost4Cam_Global("192.168.201.4")
            setInt4Cam_Global("1/0/8")
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
            setInt4Cam_Global("1/0/1")
            open_dlg_modal_VER(e)

    def rbt_CSC_3102(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 1 H1.3")
            setHost4Cam_Global("192.168.200.3")
            setInt4Cam_Global("1/0/2")
            open_dlg_modal_VER(e)

    def rbt_CSC_3103(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 1 H1.8")
            setHost4Cam_Global("192.168.200.3")
            setInt4Cam_Global("1/0/3")
            open_dlg_modal_VER(e)

    def rbt_CSC_3104(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 1 H1.9")
            setHost4Cam_Global("192.168.200.3")
            setInt4Cam_Global("1/0/4")
            open_dlg_modal_VER(e)

    def rbt_CSC_3105(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 1 H1.7")
            setHost4Cam_Global("192.168.200.3")
            setInt4Cam_Global("1/0/5")
            open_dlg_modal_VER(e)

    def rbt_CSC_3106(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 1 H1.10")
            setHost4Cam_Global("192.168.200.3")
            setInt4Cam_Global("1/0/6")
            open_dlg_modal_VER(e)

    def rbt_CSC_3107(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 1 H1.2")
            setHost4Cam_Global("192.168.200.3")
            setInt4Cam_Global("1/0/7")
            open_dlg_modal_VER(e)

    def rbt_CSC_3108(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 1 H1.11")
            setHost4Cam_Global("192.168.200.3")
            setInt4Cam_Global("1/0/8")
            open_dlg_modal_VER(e)

    def rbt_CSC_31010(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 1 H1.4")
            setHost4Cam_Global("192.168.200.3")
            setInt4Cam_Global("1/0/10")
            open_dlg_modal_VER(e)

    def rbt_CSC_31011(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 1 H1.11")
            setHost4Cam_Global("192.168.200.3")
            setInt4Cam_Global("1/0/11")
            open_dlg_modal_VER(e)

    def rbt_CSC_31012(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 1 H1.12")
            setHost4Cam_Global("192.168.200.3")
            setInt4Cam_Global("1/0/12")
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
            setInt4Cam_Global("1/0/1")
            open_dlg_modal_VER(e)

    def rbt_CSC_40105(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.14")
            setHost4Cam_Global("192.168.200.40")
            setInt4Cam_Global("1/0/5")
            open_dlg_modal_VER(e)

    def rbt_CSC_40106(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.7")
            setHost4Cam_Global("192.168.200.40")
            setInt4Cam_Global("1/0/6")
            open_dlg_modal_VER(e)

    def rbt_CSC_40108(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.9")
            setHost4Cam_Global("192.168.200.40")
            setInt4Cam_Global("1/0/8")
            open_dlg_modal_VER(e)

    def rbt_CSC_40109(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.8")
            setHost4Cam_Global("192.168.200.40")
            setInt4Cam_Global("1/0/9")
            open_dlg_modal_VER(e)

    def rbt_CSC_401017(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.6")
            setHost4Cam_Global("192.168.200.40")
            setInt4Cam_Global("1/0/17")
            open_dlg_modal_VER(e)

    def rbt_CSC_401019(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.10")
            setHost4Cam_Global("192.168.200.40")
            setInt4Cam_Global("1/0/19")
            open_dlg_modal_VER(e)

    def rbt_CSC_401023(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.19")
            setHost4Cam_Global("192.168.200.40")
            setInt4Cam_Global("1/0/23")
            open_dlg_modal_VER(e)

    def rbt_CSC_41017(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.20")
            setHost4Cam_Global("192.168.200.41")
            setInt4Cam_Global("0/17")
            open_dlg_modal_VER(e)

    def rbt_CSC_41019(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.20")
            setHost4Cam_Global("192.168.200.41")
            setInt4Cam_Global("0/19")
            open_dlg_modal_VER(e)

    def rbt_CSC_41021(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.20")
            setHost4Cam_Global("192.168.200.41")
            setInt4Cam_Global("0/21")
            open_dlg_modal_VER(e)

    def rbt_CSC_41022(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.20")
            setHost4Cam_Global("192.168.200.41")
            setInt4Cam_Global("0/22")
            open_dlg_modal_VER(e)

    def rbt_CSC_41023(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.20")
            setHost4Cam_Global("192.168.200.41")
            setInt4Cam_Global("0/23")
            open_dlg_modal_VER(e)

    def rbt_CSC_41024(e):
        if inMain_loginChecker == 0:
            status.value = "You have to be loged in to the system before performing any actions. Please login!"
            page.update()
        else:
            setDesc4Cam_Global("Home 2 H2.20")
            setHost4Cam_Global("192.168.200.41")
            setInt4Cam_Global("0/24")
            open_dlg_modal_VER(e)

    # House 3 key definitions
    def rbt_CSC_H3(e):
        pass

    # House 4 key definitions
    def rbt_CSC_H4(e):
        pass

    def ENG_CSC_General(e):
        close_modal_VER(e)
        # status.value = f"{inGlobal_Host}, {inGlobal_User}, {inGlobal_PassWord}, {inGlobal_Interface}"
        # page.update()
        status.value = f"Camera {inGlobal_CamDescription} is now in reload process"
        page.update()
        SSHCSC_Rldr = CSCRldr.CSCReloader(inGlobal_Host, inGlobal_User, inGlobal_PassWord, inGlobal_Interface)
        SSHCSC_Rldr.Reload_CSC()
        status.value = f"Camera {inGlobal_CamDescription} Reloaded."
        page.update()

    def open_dlg_ER(e):
        page.dialog = dlg_Wrong_UserLogin
        dlg_Wrong_UserLogin.open = True
        page.update()

    # Create login alert-dialoge object
    def open_dlg_UserLogin(e):
        page.dialog = dlg_UserLogin     # Define class dialog as alert-dialog
        dlg_UserLogin.open = True       # View property changed to possitive to display alert
        page.update()                   # Update the page on self

    def open_dlg_modal_VER(e):
        # dlg_modal_VER.title = "asd"
        page.dialog = dlg_modal_VER
        dlg_modal_VER.open = True
        page.update()

    def close_dlg_UserLogin(e):
        dlg_UserLogin.open = False
        page.update()

    def close_modal_VER(e):
        dlg_modal_VER.open = False
        page.update()

    dlg_modal_VER = nlxFT.AlertDialog(
        modal=True,
        title=nlxFT.Text("Please Confirm"),
        content=nlxFT.Text("Are you sure you want to reboot this camera?"),
        # content=nlxFT.Text(f"Are you sure you want to reboot this camera?"),
        actions=[
            nlxFT.TextButton("Yes", on_click=ENG_CSC_General),
            nlxFT.TextButton("No", on_click=close_modal_VER),
        ],
        actions_alignment=nlxFT.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

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
                        nlxFT.Text("Please login using your provided credentials.\nIf a set was not provided to you, please sent an email to the following address."),
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

    page.add(
        nlxFT.Container(
            expand=True,
            height=1200,
            width=1200,
            content=nlxFT.Column(
                controls=[
                    # Header panel called here
                    nlxFT.Container(
                        bgcolor="#081d33", border_radius=nlxFT.border_radius.only(top_left=8, top_right=8),
                        padding=nlxFT.padding.only(left=15, right=15),
                        content=
                            nlxFT.Row(
                                height=60, expand=True, alignment=nlxFT.MainAxisAlignment.SPACE_BETWEEN,
                                # NLX! Header instance controls added here:
                                controls=[app_Header_Brand(), app_Header_Search(), app_Header_Avatar()],
                            )
                    ),
                    nlxFT.Divider(height=1.5, color="Transparent"),
                    # Camera panel called here
                    nlxFT.Container(
                        expand=True, height=770, bgcolor="white10", border=nlxFT.border.all(1, "#ebebeb"), border_radius=8, padding=15,
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
                                                                nlxFT.ElevatedButton(text="GHQ.IDF46", tooltip="00:0F:7C:0F:9C:CB", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_11101),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.66", tooltip="00:0F:7C:0D:09:17", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_11103),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.61", tooltip="00:0F:7C:0F:1F:EA", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_11104),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF59", tooltip="00:0f:7C:0F:9C:B7", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_11105),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.51", tooltip="00:0F:7C:0F:20:06", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_11106),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.42", tooltip="00:0F:7C:0E:E1:D1", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_11108)
                                                            ]
                                                        ),
                                                        # Row 2
                                                        nlxFT.Row(
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF63", tooltip="00:0F:7C:0F:9C:B8", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_11109),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF49", tooltip="00:0F:7C:0F:82:FE", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_111011),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.68", tooltip="00:18:AE:8B:E8:DE", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_111012),
                                                                nlxFT.ElevatedButton(text="GHQ MEZ.54", tooltip="3C:EF:8C:C5:06:01", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_111013),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF48", tooltip="00:0F:7C:0F:82:FF", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_111015),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF62", tooltip="00:0F:07C:0F:9C:BC", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_111017)
                                                            ]
                                                        ),
                                                        # Row 3
                                                        nlxFT.Row(
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF47", tooltip="00:0F:7C:0F:83:01", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_111019),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.57", tooltip="00:0F:7C:0E:E1:E4", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_111025),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.19", tooltip="00:0F:7C:0F:98:88", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_111028),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.9", tooltip="00:0F:7C:0D:D5:89", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_111029),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.15", tooltip="00:0F:7C:0D:D5:BD", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_111031),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.10", tooltip="00:0F:7C:0D:D5:8A", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_111033)
                                                            ]
                                                        ),
                                                        # Row 4
                                                        nlxFT.Row(
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.6", tooltip="00:0F:7C:0F:82:79", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_111034),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.1", tooltip="00:0F:7C:0F:82:7E", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_111035),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.2", tooltip="00:0F:7C:0F:82:7D", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_111036),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.11", tooltip="00:0F:7C0F:83:0F", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_111037),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.13", tooltip="00:0F:7C:0F:82:CD", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_111040),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.17", tooltip="00:0F:7C:0F:9C:DA", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_111042)
                                                            ]
                                                        ),
                                                        # Row 5
                                                        nlxFT.Row(
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.4", tooltip="00:0F:7C:0F:82:80", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_111043),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.18", tooltip="00:0F:7C:0F:82:7A", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_111044),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.14", tooltip="00:0F:7C:0D:D5:B9", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_111045),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.21", tooltip="00:0F:7C:0F:68:9B", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_111046),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.20", tooltip="00:0F:7C:0F:9C:EA", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_111048)
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
                                                                nlxFT.ElevatedButton(text="GHQ.IDF31", tooltip="00:0F:7C:0F:9C:C8", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_14101),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF5", tooltip="00:0F:7C:0F:83:2C", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_14102),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF35", tooltip="00:0F:7C:0F:9C:C7", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_14103),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF3", tooltip="00:0F:7C:0F:83:2B", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_14104),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF38", tooltip="00:0F:7C:0F:9C:D0", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_14105),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF29", tooltip="MAC Address N/A", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_14106)
                                                            ]
                                                        ),
                                                        # Row 2
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF43", tooltip="00:0F:7C:0F:83:00", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_14107),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF45", tooltip="00:0F:7C:0F:82:FB", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_14109),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF51", tooltip="00:0F:7C:0E:E1:E7", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141010),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF40", tooltip="00:0F:7C:0F:9C:83", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141011),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF33", tooltip="00:0F:7C:0F:9C:82", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141013),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ.7", tooltip="00:0F:7C:0F:82:D0", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141014)
                                                            ]
                                                        ),
                                                        # Row 3
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF26", tooltip="00:0F:7C:0E:E1:FE", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141015),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF50", tooltip="00:0F:7C:0F:82:FD", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141017),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF9", tooltip="00:0F:7C:0F:83:2D", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141018),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF42", tooltip="00:0F:7C:0F:82:FC", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141019),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF27", tooltip="00:0F:7C:0E:E1:FC", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141020),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ37", tooltip="00:0F:7C:0F:9C:86", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141021)
                                                            ]
                                                        ),
                                                        # Row 4
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF68", tooltip="00:18:AE:9E:79:B4", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141022),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF39", tooltip="00:0F:7C:0F:9C:84", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141023),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF69", tooltip="00:18:AE:9E:79:71", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141024),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF53", tooltip="00:0F:7C:0F:9C:D2", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141025),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF10", tooltip="00:0f:7C:0F:83:0C", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141027),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF11", tooltip="00:0f:7C:0F:82:FA", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141029)
                                                            ]
                                                        ),
                                                        # Row 5
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF36", tooltip="00:0F:7C:0F:9C:CD", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141031),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF52", tooltip="00:0F:7C:10:95:93", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141033),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF32", tooltip="00:0F:7C:0F.9C:CC", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141035),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF7", tooltip="00:0F:7C:0F:83:31", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141037),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF1", tooltip="00:0F:7C:0F:83:2F", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141039),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF41", tooltip="00:0F:7C:0F:9C:CE", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141041)
                                                            ]
                                                        ),
                                                        # Row 6
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF30", tooltip="00:0F:7C:0F:9C:CF", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141043),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF16", tooltip="00:0F:7C:0D:FA:94", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141044),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF56", tooltip="00:0F:7C:0F:9C:CA", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141045),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF19", tooltip="00:0F:7C:0F:82:B0", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_141046),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF8", tooltip="00:0F:7C:0F:82:AB", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_14201),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF21", tooltip="00:50:F9:01:42:FA", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_14203)
                                                            ]
                                                        ),
                                                        # Row 7
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF12", tooltip="3C:EF:8C:C4:CE:05", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_14205),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF14", tooltip="00:0F:7C:0D:D5:BA", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_14207),
                                                                nlxFT.ElevatedButton(text="GHQ.MEZ8", tooltip="00:0F:7C:0F:83:0E", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_142010),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF44", tooltip="00:0F:7C:0F:9C:B2", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_142011),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF22", tooltip="00:0F:7C:0F:9C:C2", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_142013),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF25", tooltip="00:0F:7C:0F:9C:BE", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_142015)
                                                            ]
                                                        ),
                                                        # Row 8
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF55", tooltip="00:0F:7C:0F:82:CF", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_142017),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF2", tooltip="00:0F:7C:0F:83:2E", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_142018),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF28", tooltip="00:0F:7C:0F:9C:BF", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_142019),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF57", tooltip="00:0F:7C:0F:82:A9", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_142021),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF14", tooltip="00:0F:7C:0D:FA:8E", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_142022),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF18", tooltip="00:0F:7C:0F:83:2A", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_142025)
                                                            ]
                                                        ),
                                                        # Row 9
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF54", tooltip="00:0F:7C:0F:83:0A", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_142027),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF20", tooltip="00:0F:7C:0F:82:AA", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_142028),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF23", tooltip="00:0F:7C:0E:E2:00", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_142032),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF34", tooltip="00:0F:7C:0F:9C:C5", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_142033),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF17", tooltip="00:0F:7C:0F:82:AE", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_142035),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF13", tooltip="00:0F:7C:0D:D5:8B", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_142036)
                                                            ]
                                                        ),
                                                        # Row 9
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="GHQ.IDF4", tooltip="00:0F:7C:0F:83:30", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_142037),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF24", tooltip="00:0F:7C:0E:E1:FF", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_142038),
                                                                nlxFT.ElevatedButton(text="GHQ.IDF6", tooltip="00:0F:7C:0F:82:AF", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_142040)
                                                            ]
                                                        )
                                                    ]
                                                )
                                            )
                                        ),
                                        # Old HQ Camera Keys
                                        nlxFT.Tab(icon=nlxFT.icons.HOME_ROUNDED, text="Old HQ", 
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
                                                                nlxFT.ElevatedButton(text="OHQ8", tooltip="00:0F:7C:0E:E1:F4", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_13101),
                                                                nlxFT.ElevatedButton(text="OHQ17", tooltip="00:0F:7C:0E:E1:7B", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_13102),
                                                                nlxFT.ElevatedButton(text="OHQ7", tooltip="00:0F:7C:0E:0C:CF", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_13103),
                                                                nlxFT.ElevatedButton(text="OHQ3", tooltip="00:0F:7C:0E:0E:4D", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_13104),
                                                                nlxFT.ElevatedButton(text="OHQ5", tooltip="00:0F:7C:0D:FA:F4", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_13105),
                                                                nlxFT.ElevatedButton(text="OHQ19", tooltip="00:0F:7C:0E:0E:4F", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_13106)
                                                            ]
                                                        ),
                                                        # Row 2
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="OHQ6", tooltip="00:0F:7C:0D:FA:F7", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_13107),
                                                                nlxFT.ElevatedButton(text="OHQ20", tooltip="00:18:AE:C2:15:1A", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_13108),
                                                                nlxFT.ElevatedButton(text="OHQ10", tooltip="00:0F:7C:0E:1:F7", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_13109),
                                                                nlxFT.ElevatedButton(text="OHQ4", tooltip="00:0F:7C:0E:E1:E0", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_131011),
                                                                nlxFT.ElevatedButton(text="OHQ9", tooltip="00:0F:7C:0E:E1:DD", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_131013),
                                                                nlxFT.ElevatedButton(text="OHQ11", tooltip="00:18:AE:9E:79:4C", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_131015)
                                                            ]
                                                        ),
                                                        # Row 3
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="OHQ1", tooltip="00:0F:7C:0E:E1:89", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_131017),
                                                                nlxFT.ElevatedButton(text="OHQ12", tooltip="00:0F:7C:0E:E1:AB", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_131019),
                                                                nlxFT.ElevatedButton(text="OHQ18", tooltip="00:0F:7C:0E:E1:F9", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_131021),
                                                                nlxFT.ElevatedButton(text="OHQ16", tooltip="00:0F:7C:0E:E1:F5", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_131039),
                                                                nlxFT.ElevatedButton(text="OHQ15", tooltip="00:0F:7C:0E:E1:F8", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_131041),
                                                                nlxFT.ElevatedButton(text="OHQ14", tooltip="MAC Address N/A", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_131043)
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
                                                                nlxFT.ElevatedButton(text="CRN.5", tooltip="00:0F:7C:0D:09:45", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_20102),
                                                                nlxFT.ElevatedButton(text="CRN.7", tooltip="00:0F:7C:0D:08:AF", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_20103),
                                                                nlxFT.ElevatedButton(text="CRN.10", tooltip="00:0F:7C:0D:09:4D", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_20104),
                                                                nlxFT.ElevatedButton(text="CRN.9", tooltip="00:0F:7C:0C:83:59", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_20105),
                                                                nlxFT.ElevatedButton(text="CRN.5", tooltip="00:0F:7C:10:95:AE", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_20106),
                                                                nlxFT.ElevatedButton(text="CRN.1", tooltip="00:0F:7C:0D:FB:12", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_20107)
                                                            ]
                                                        ),
                                                        # Row 2
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="CRN.4", tooltip="00:0F:7C:0D:FB:11", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_20108),
                                                                nlxFT.ElevatedButton(text="CRN.12", tooltip="00:0F:7C:10:95:A7", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_20109),
                                                                nlxFT.ElevatedButton(text="CRN.2", tooltip="00:0F:7C:0E:E1:F1", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_201010),
                                                                nlxFT.ElevatedButton(text="CRN.3", tooltip="00:0F:7C:0D:08:D2", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_201011),
                                                                nlxFT.ElevatedButton(text="CRN.8", tooltip="00:0F:7C:0D:08:D2", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_201012),
                                                                nlxFT.ElevatedButton(text="CRN.13", tooltip="00:0F:7C:0D:08:D2", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_201013)
                                                            ]
                                                        ),
                                                        # Row 3
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="CRN.11", tooltip="000f.7c10.95ab", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_201014)
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
                                                                nlxFT.ElevatedButton(text="OHQ.PRK1.1", tooltip="00:0F:7C:0E:0D:47", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_4104),
                                                                nlxFT.ElevatedButton(text="OHQ.PRK1.2", tooltip="00:0F:7C:0E:0D:49", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_4107),
                                                                nlxFT.ElevatedButton(text="OHQ.PRK1.3", tooltip="00:0F:7C:10:95:51", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_4103),
                                                                nlxFT.ElevatedButton(text="OHQ.PRK1.4", tooltip="00:0F:7C:0E:E1:F6", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_4102),
                                                                nlxFT.ElevatedButton(text="OHQ.PRK1.5", tooltip="3C:EF:8C:C5:06:24", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_4101),
                                                                nlxFT.ElevatedButton(text="OHQ.PRK1.6", tooltip="3C:EF:8C:C5:06:0C", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_4108)
                                                            ]
                                                        ),
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="Test", tooltip="00:0F:7C:0E:0D:47", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_4106)
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
                                                                nlxFT.ElevatedButton(text="H1.6", tooltip="00:0F:7C:0E:E1:7A", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_3101),
                                                                nlxFT.ElevatedButton(text="H1.3", tooltip="00:0F:7C:0E:E1:E5", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_3102),
                                                                nlxFT.ElevatedButton(text="H1.8", tooltip="00:0F:7C:0E:E1:7D", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_3103),
                                                                nlxFT.ElevatedButton(text="H1.9", tooltip="00:0F:7C:0E:E1:7F", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_3104),
                                                                nlxFT.ElevatedButton(text="H1.7", tooltip="00:0F:7C:0E:E1:fA", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_3105),
                                                                nlxFT.ElevatedButton(text="H1.10", tooltip="00:0F:7C:0E:E1:E1", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_3106)
                                                            ]
                                                        ),
                                                        # Row 2
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="H1.2", tooltip="00:0F:7C:0E:E1:F3", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_3107),
                                                                nlxFT.ElevatedButton(text="H1.11", tooltip="00:18:AE:A7:2A:DD", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_3108),
                                                                nlxFT.ElevatedButton(text="H1.4", tooltip="00:0F:7C:0E:E1:C7", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_31010),
                                                                nlxFT.ElevatedButton(text="H1.5", tooltip="00:0F:7C:0E:E1:7E", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_31011),
                                                                nlxFT.ElevatedButton(text="H1.1", tooltip="00:0F:7C:0E:E1:DA", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_31012)
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
                                                                nlxFT.ElevatedButton(text="H2.2", tooltip="00:0F:7C:0F:9C:DB", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_40101),
                                                                nlxFT.ElevatedButton(text="H2.14", tooltip="00:0F:7C:0F:9C:8F", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_40105),
                                                                nlxFT.ElevatedButton(text="H2.7", tooltip="00:0F:7C:0F:9C:8D", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_40106),
                                                                nlxFT.ElevatedButton(text="H2.9", tooltip="00:0F:7C:0F:9C:95", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_40108),
                                                                nlxFT.ElevatedButton(text="H2.8", tooltip="00:0F:7C:0F:9C:8B", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_40109),
                                                                nlxFT.ElevatedButton(text="H2.5", tooltip="00:0F:7C:0F:9C:89", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_401017)
                                                            ]
                                                        ),
                                                        # Row 1
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="H2.10", tooltip="00:0F:7C:0F:9C:94", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_401019),
                                                                nlxFT.ElevatedButton(text="H2.19", tooltip="00:0F:7C:0F:9C:93", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_401023),
                                                                nlxFT.ElevatedButton(text="H2.20", tooltip="00:0F:7C:0D:08:D5", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_41017),
                                                                nlxFT.ElevatedButton(text="H2.21", tooltip="3C:EF:8C:C5:06:3D", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_41019),
                                                                nlxFT.ElevatedButton(text="H2.12", tooltip="00:0F:7C:0F:20:04", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_41021),
                                                                nlxFT.ElevatedButton(text="H2.18", tooltip="00:0F:7C:0F:20:05", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_41022)
                                                            ]
                                                        ),
                                                        # Row 1
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="H2.16", tooltip="00:0F:7C:0F:9C:B6", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_41023),
                                                                nlxFT.ElevatedButton(text="H2.17", tooltip="00:0F:7C:0F:20:03", bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=rbt_CSC_41024)
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
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
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
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
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
                    nlxFT.Divider(height=1.5, color="Transparent"),
                    # Status bar panel called here
                    nlxFT.Container(
                        # bgcolor="#081d33", border_radius=8, padding=nlxFT.padding.only(left=15, right=15),
                        bgcolor="#081d33", border_radius=nlxFT.border_radius.only(bottom_left=8, bottom_right=8), 
                            padding=nlxFT.padding.only(left=15, right=15),
                        content=nlxFT.Row(
                            expand=True, height=60, alignment=nlxFT.MainAxisAlignment.END,
                            # self-control instances added here:
                            controls=[status]
                        )
                    )
                ]
            )
        )
    )
# Main page definition END

nlxFT.app(target=main)

# NLXComments Post-Ver
"""
Beta 1 Ver. of CRAcc2CSC loads interface broaken into site panels that contain elevated BTNs. These BTNs reload asset targets
located in the sites. To Enable the BTNs (keys) the piece promts the user to login using a set of provided credentials 
configured in AD (active Directory). While connected the keys promt the user to confirm actions that correspond to each key.
This version will be tidied to fix data sets that are not being loaded and modified correcty.
Beta version named
Assets:
None
New Assets:
None
Result: Good
References:
https://jira.wargaming.net/browse/INTCY-5250
"""
