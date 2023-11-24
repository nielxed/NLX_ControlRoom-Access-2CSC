# GHApp! AlertDialogue
# https://flet.dev/docs/controls/alertdialog
import flet as nlxFT
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

    # Value initializers
    userNameCR = ""    # Initialize a username string glb
    userNameCPT = nlxFT.TextField(label="Username", width=250, border_color="white")                  # Password text-field defined off-definition glb
    passWordCR = ""    # Initialize a password string glb
    passWordCPT = nlxFT.TextField(label="Password", width=250, border_color="white", password=True)   # Password text-field defined off-definition glb and set to hidden
    CRStatus = nlxFT.Text(value="notInit")

    dlg = nlxFT.AlertDialog(
        title = nlxFT.Text("Hello, you!"), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    
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
                    controls=[
                        nlxFT.Text("Please login using your provided credentials.\nIf a user was not provided to you, please sent an email to the following address."),
                        nlxFT.ElevatedButton("cyit@wargaming.net", icon=nlxFT.icons.MAIL_ROUNDED, url="mailto:cyit@wargaming.net"), nlxFT.Divider(height=1.5, color="Transparent"),
                        nlxFT.Row(
                            alignment = nlxFT.MainAxisAlignment.SPACE_EVENLY,
                            controls = [
                            userNameCPT,
                            passWordCPT
                            ],
                        ),
                    ],
                ),    
            ),
        actions = [
            nlxFT.FloatingActionButton(icon=nlxFT.icons.LOGIN_ROUNDED, bgcolor=nlxFT.colors.BLUE_300, on_click=close_dlg_UserLogin,),
            nlxFT.FloatingActionButton(icon=nlxFT.icons.CANCEL_ROUNDED, bgcolor=nlxFT.colors.BLUE_300, on_click=close_dlg_UserLogin)
        ],
        actions_alignment = nlxFT.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!")
    )

    # Create login alert-dialoge object
    def open_dlg_UserLogin(e):
        page.dialog = dlg_UserLogin     # Define class dialog as alert-dialog
        dlg_UserLogin.open = True       # View property changed to possitive to display alert
        page.update()                   # Update the page on self

    page.add(
        nlxFT.ElevatedButton("Open modal dialog", on_click=open_dlg_UserLogin),
        nlxFT.Container(
            content=nlxFT.Row(
                controls=[CRStatus]
            )
        )
    )

nlxFT.app(target=main)

# NLXComments Post-Ver
"""
Said version loads default Flet box with a button that loads a select modal as downloded from https://flet.dev modal (referenced).
Beta version named
Cosmetic initializers added stolen from WGPtn_CRAcc2CSC_SLMain_07062023.py
The version contains an initialized label with a known var "notInit" to see if creds were supplied.
Result: Good
References:
https://flet.dev/docs/controls/alertdialog/#modal
"""