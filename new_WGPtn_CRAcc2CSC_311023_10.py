# NLX Swrd: CRAcc2CSC (code name: Lothlorien)
# Version: Celeborn
import flet as nlxFT
import Cgpt_VerAcc_31123_cl as Vrfr
import Cgpt_ENG101_71123_cl as CSCRldr
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

LGStateNum = 0

def main(page: nlxFT.Page):
    # Page initializers
    page.bgcolor="#fdfdfd"
    page.padding=20
    page.window_height=1270
    page.window_width=1200
    page.window_maximizable=False
    page.window_maximized=False
    page.window_resizable=False
    page.title = "Lothlorien"
    MSG1 = "Invalid username and/or password!"
    MSG2 = "Please log in before actions"

    # Value initializers        
    userNameCR = ""                                                                                 # Initialize a username string glb
    userNameCPT = nlxFT.TextField(label="Username", width=250, border_color="white")                # Password text-field defined off-definition glb
    passWordCR = ""                                                                                 # Initialize a password string glb
    passWordCPT = nlxFT.TextField(label="Password", width=250, border_color="white", password=True) # Password text-field defined off-definition glb and set to hidden
    CRStatus = nlxFT.Text(value="notInit")
    status = nlxFT.Text(value="Welcome! Please set provided credential.", size= 15, color="white")

    def app_Header_Brand():
        return nlxFT.Container(
            content=nlxFT.Row(
                controls=[
                nlxFT.Icon(name=nlxFT.icons.LOCAL_FIRE_DEPARTMENT_ROUNDED, color="white"),
                nlxFT.Text("Celeborn 0.1.0", size=15, color="white")
                ]
            )
        )
    
    def reset_Creds():
        userNameCPT.value = ""
        passWordCPT.value = ""

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
        passWordCR = passWordCPT.value
        host = "192.168.201.4"
        port = 22  # or the port you use for SSH
        timeout = 10  # you can adjust the timeout value if necessary
        close_dlg_UserLogin(e)

        ssh_verifier = Vrfr.SSHVerifier(host, userNameCR, passWordCR, port, timeout)
        if ssh_verifier.verify_ssh_access():
            status.value = f"User {userNameCR} logged in successfully!"
            page.update()
        else:
            open_dlg_ER(e)
            reset_Creds

    # def Run_EngineCSC(e):
    def Run_EngineCSC(AHost:str, DInt:str):
        SSHCSC_Rldr = CSCRldr.CSCReloader(AHost, userNameCPT.value, passWordCPT.value, DInt)
        SSHCSC_Rldr.Reload_CSC()
        # print(userNameCR, passWordCR)
        # status.value = f"{userNameCPT.value}, {passWordCPT.value}"
        # page.update()
        
    def open_dlg_ER(e):
        page.dialog = dlg_Wrong_UserLogin
        dlg_Wrong_UserLogin.open = True
        page.update()

    # Create login alert-dialoge object
    def open_dlg_UserLogin(e):
        page.dialog = dlg_UserLogin     # Define class dialog as alert-dialog
        dlg_UserLogin.open = True       # View property changed to possitive to display alert
        page.update()                   # Update the page on self

    def close_dlg_UserLogin(e):
        dlg_UserLogin.open = False
        page.update()

    dlg_UserLogin = nlxFT.AlertDialog(
        modal = True,
        title = nlxFT.Text("Please provide your credential"),
        content_padding = 20,
        content = nlxFT.Container(
            # expand=False,
            width = 550,
            height = 170,
            content =
                nlxFT.Column(
                    expand = False,
                    controls = [
                        nlxFT.Text("Please login using your provided credentials.\nIf a user was not provided to you, please sent an email to the following address."),
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
                                        nlxFT.Tab(icon=nlxFT.icons.BUSINESS_ROUNDED, text="HQ", 
                                            content=nlxFT.Container(
                                                disabled=False,
                                                padding=15,
                                                content=nlxFT.Column(
                                                    controls=[
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.IDF46",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0F:9C:CB",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0f.9ccb",
                                                                        "Interface": "1/0/1",
                                                                    },
                                                                    # on_click=Run_EngineCSC("192.168.77.11","1/0/1")
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.MEZ.66",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0D:09:17",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0d.0917",
                                                                        "Interface": "1/0/3",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.MEZ.61",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0F:1F:EA",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0f.1fea",
                                                                        "Interface": "1/0/4",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.IDF59",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0f:7C:0F:9C:B7",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0f.9cb7",
                                                                        "Interface": "1/0/5",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.MEZ.51",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0F:20:06",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0f.2006",
                                                                        "Interface": "1/0/5",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.MEZ.42",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0E:E1D1",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0e.e1d1",
                                                                        "Interface": "1/0/5",
                                                                    }
                                                                )
                                                            ]
                                                        ),
                                                    nlxFT.Row(
                                                        controls=[
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.IDF63",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0F:9C:B8",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0f.9cb8",
                                                                        "Interface": "1/0/9",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.IDF49",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0F:82:FE",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0f.82fe",
                                                                        "Interface": "1/0/11",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.MEZ.68",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:18:AE:8B:E8:DE",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "0018.ae8b.e8de",
                                                                        "Interface": "1/0/12",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ MEZ.54",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="3C:EF:8C:C5:06:01",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "3cef.8cc5.0601",
                                                                        "Interface": "1/0/13",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.IDF48",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0F:82:FF",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0f.82ff",
                                                                        "Interface": "1/0/15",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.IDF62",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:07C:0F:9C:BC",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0f.9cbc",
                                                                        "Interface": "1/0/17",
                                                                    }
                                                                )
                                                            ]
                                                        ),
                                                        nlxFT.Row(
                                                        controls=[
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.IDF47",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0F:83:01",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0f.8301",
                                                                        "Interface": "1/0/19",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.MEZ.57",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0E:E1:E4",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0e.e1e4",
                                                                        "Interface": "1/0/25",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.MEZ.19",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0F:98:88",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "0018.ae8b.e8de",
                                                                        "Interface": "1/0/28",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.MEZ.9",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0D:D5:89",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0d.d589",
                                                                        "Interface": "1/0/29",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.MEZ.15",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0D:D5:BD",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0d.d5bd",
                                                                        "Interface": "1/0/31",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.MEZ.10",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0D:D5:8A",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0d.d58a",
                                                                        "Interface": "1/0/33",
                                                                    }
                                                                )
                                                            ]
                                                        ),
                                                        nlxFT.Row(
                                                        controls=[
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.MEZ.6",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0F:82:79",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0f.8279",
                                                                        "Interface": "1/0/34",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.MEZ.1",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0F:827E",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0f.827e",
                                                                        "Interface": "1/0/35",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.MEZ.2",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0F:82:7D",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0f.827d",
                                                                        "Interface": "1/0/36",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.MEZ.11",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C0F:83:0F",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0f.830f",
                                                                        "Interface": "1/0/37",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.MEZ.13",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0F:82:CD",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0f.82cd",
                                                                        "Interface": "1/0/40",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.MEZ.17",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0F:9C:DA",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0f.9cda",
                                                                        "Interface": "1/0/42",
                                                                    }
                                                                )
                                                            ]
                                                        ),
                                                        nlxFT.Row(
                                                        controls=[
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.MEZ.4",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0F:82:80",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0f.8280",
                                                                        "Interface": "1/0/43",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.MEZ.18",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0F:82:7A",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0f.827a",
                                                                        "Interface": "1/0/44",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.MEZ.14",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0D:D5:B9",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0f.827d",
                                                                        "Interface": "1/0/45",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.MEZ.21",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0F:68:9B",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0f.689b",
                                                                        "Interface": "1/0/46",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="GHQ.MEZ.20",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0F:9C:EA",
                                                                    data = {
                                                                        "IP": "192.168.77.11",
                                                                        "MAC": "000f.7c0f.9cea",
                                                                        "Interface": "1/0/48",
                                                                    }
                                                                )
                                                            ]
                                                        )
                                                    ]
                                                )
                                            )
                                        ),
                                        nlxFT.Tab(icon=nlxFT.icons.MEETING_ROOM_ROUNDED, text="IDF Room",
                                            content=nlxFT.Container(
                                                # disabled=True,
                                                padding=15,
                                                content=nlxFT.Column(
                                                    controls=[
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(text="OHQ.PRK1.1", expand=1, on_click=Run_EngineCSC("192.168.201.4", "1/0/6")),
                                                                # nlxFT.ElevatedButton(text="OHQ.PRK1.1", on_click=Run_EngineCSC),
                                                            ]
                                                        )
                                                    ]
                                                )
                                            )
                                        ),
                                        nlxFT.Tab(icon=nlxFT.icons.HOME_ROUNDED, text="Old HQ", 
                                            content=nlxFT.Container(
                                                # disabled=True,
                                                padding=15,
                                                content=nlxFT.Column(
                                                    controls=[
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                            ]
                                                        )
                                                    ]
                                                )
                                            )
                                        ),
                                        nlxFT.Tab(icon=nlxFT.icons.HOUSE_SIDING_ROUNDED, text="Corner House", 
                                            content=nlxFT.Container(
                                                # disabled=True,
                                                padding=15,
                                                content=nlxFT.Column(
                                                    controls=[
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                            ]
                                                        )
                                                    ]
                                                )
                                            )
                                        ),
                                        nlxFT.Tab(icon=nlxFT.icons.GARAGE_ROUNDED, text="Parking 1", 
                                            content=nlxFT.Container(
                                                # disabled=True,
                                                padding=15,
                                                content=nlxFT.Column(
                                                    controls=[
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                                nlxFT.ElevatedButton(
                                                                    text="OHQ.PRK1.1",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0E:0D:47",
                                                                    # data = {
                                                                    #     "IP": "192.168.201.13",
                                                                    #     "MAC": "000f.7c0e.0d47",
                                                                    #     "Interface": "1/0/4",
                                                                    # },
                                                                    # on_click=Run_EngineCSC("192.168.201.4", "1/0/6")
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="OHQ.PRK1.2",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0E:0D:49",
                                                                    data = {
                                                                        "IP": "192.168.201.14",
                                                                        "MAC": "000f.7c0e.0d49",
                                                                        "Interface": "1/0/7",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="OHQ.PRK1.3",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:10:95:51",
                                                                    data = {
                                                                        "IP": "192.168.201.12",
                                                                        "MAC": "000f.7c10.9551",
                                                                        "Interface": "1/0/3",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="OHQ.PRK1.4",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="00:0F:7C:0E:E1:F6",
                                                                    data = {
                                                                        "IP": "192.168.201.15",
                                                                        "MAC": "000f.7c0e.e1f6",
                                                                        "Interface": "1/0/2",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="OHQ.PRK1.5",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="3C:EF:8C:C5:06:24",
                                                                    data = {
                                                                        "IP": "192.168.201.10",
                                                                        "MAC": "3cef.8cc5.0624",
                                                                        "Interface": "1/0/1",
                                                                    }
                                                                ),
                                                                nlxFT.ElevatedButton(
                                                                    text="OHQ.PRK1.6",
                                                                    bgcolor=nlxFT.colors.BLUE_GREY_100,
                                                                    color=nlxFT.colors.BLACK,
                                                                    expand=1,
                                                                    tooltip="3C:EF:8C:C5:06:0C",
                                                                    data = {
                                                                        "IP": "192.168.201.11",
                                                                        "MAC": "3cef.8cc5.060c",
                                                                        "Interface": "1/0/8",
                                                                    }
                                                                )
                                                            ]
                                                        )
                                                    ]
                                                )
                                            )
                                        ),
                                        nlxFT.Tab(icon=nlxFT.icons.HOME_ROUNDED, text="H1", 
                                            content=nlxFT.Container(
                                                # disabled=True,
                                                padding=15,
                                                content=nlxFT.Column(
                                                    controls=[
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                            ]
                                                        )
                                                    ]
                                                )
                                            )
                                        ),
                                        nlxFT.Tab(icon=nlxFT.icons.HOME_ROUNDED, text="H2", 
                                            content=nlxFT.Container(
                                                # disabled=True,
                                                padding=15,
                                                content=nlxFT.Column(
                                                    controls=[
                                                        nlxFT.Row(
                                                            # Camera buttons go here!
                                                            controls=[
                                                            ]
                                                        )
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

nlxFT.app(target=main)

# NLXComments Post-Ver
"""
Said version loads default Flet box with a button that loads a select modal as downloded from https://flet.dev modal (referenced).
Beta version named
Copying more assets from WGPtn_CRAcc2CSC_SLClass_07062023_011.py
Assets:
None
New Assets:
CSC Engine imported for 1st Beta Cgpt_ENG101_71123_cl.py
Result: Faulty ->   Exception has occurred: ScrapliAuthenticationFailed
                    password prompt seen more than once, assuming auth failed
References:
https://jira.wargaming.net/browse/INTCY-5250
"""
