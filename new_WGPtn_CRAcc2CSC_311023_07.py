# NLX Swrd: CRAcc2CSC (code name: Lothlorien)
# Version: Celeborn
import flet as nlxFT
import Cgpt_VerAcc_31123_cl as Vrfr
"""
A material design alert dialog.
An alert dialog informs the user about situations that require acknowledgement. 
An alert dialog has an optional title and an optional list of actions. The title is displayed
above the content and the actions are displayed below the content.
"""

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
    ERR=0

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
                nlxFT.Text("Celeborn 0.0.7", size=15, color="white")
                ]
            )
        )
    
    def reset_Creds():
        userNameCR = ""
        userNameCPT.value = ""
        passWordCR = ""
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
        username = userNameCR
        password = passWordCR
        port = 22  # or the port you use for SSH
        timeout = 10  # you can adjust the timeout value if necessary
        close_dlg_UserLogin(e)

        ssh_verifier = Vrfr.SSHVerifier(host, username, password, port, timeout)
        if ssh_verifier.verify_ssh_access():
            ERR = 0
            status.value = f"User {userNameCR} logged in successfully!"
            page.update()
        else:
            ERR = 1
            open_dlg_ERR(e)
            reset_Creds

    def open_dlg_ERR(e):
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
                        nlxFT.Text("Invalid username and/or password!")
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
                                                                    data = {
                                                                        "IP": "192.168.201.13",
                                                                        "MAC": "000f.7c0e.0d47",
                                                                        "Interface": "1/0/4",
                                                                    }
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
dlg_Wrong_UserLogin is the "Invalid username and/or password!" popup modal.
User login feedback on status bar. 
Module "Cgpt_VerAcc_31123_cl" imported
Result: Good
References:
https://flet.dev/docs/controls/alertdialog/#modal
"""
