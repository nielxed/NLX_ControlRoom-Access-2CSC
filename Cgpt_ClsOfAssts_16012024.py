# NLX Swrd: CRAcc2CSC (code name: Lothlorien)
# Version: Celeborn
import flet as nlxFT
from flet import (
    TextButton
)
"""
As taken and mod to need from ChatGPT:
The class is a control BTN constructor
"""
# The Class is of type NLXShield
class assetButtonCls:
    def __init__(self, label, assetIP, interface, btnDefinition):
        self.label = label
        self.assetIP = assetIP
        self.interface = interface
        self.btnDefinition = btnDefinition

    def click(self):
        print(f"Button '{self.label}' clicked. Performing action: {self.action}")

class IterableList:
    def __init__(self):
        self.my_list = []

    def add_element(self, element):
        self.my_list.append(element)

    def iterate_list(self):
        for element in self.my_list:
            yield element

# Example usage:
assetBtn = assetButtonCls("GHQ.IDF46", "192.168.77.11", "Gi1/0/2", "rbt_CSC_11101")
assetLst = [assetBtn]
assetBtn = assetButtonCls("GHQ.MEZ.66", "192.168.77.11", "Gi1/0/2", "rbt_CSC_11103")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.61", "192.168.77.11", "Gi1/0/4", "rbt_CSC_11104")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF59", "192.168.77.11", "Gi1/0/5", "rbt_CSC_11105")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.51", "192.168.77.11", "Gi1/0/6", "rbt_CSC_11106")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.42", "192.168.77.11", "Gi1/0/8", "rbt_CSC_11108")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF63", "192.168.77.11", "Gi1/0/9", "rbt_CSC_11109")
assetLst.append(assetBtn)

# Creating button list
# ----------   
btnList = []
for item in assetLst:
    print(item.label)
    print(item.btnDefinition)
    btnList.append(nlxFT.ElevatedButton(text=item.label, bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=item.btnDefinition)) 
# ----------   

# As taken from WGPtn_CRAcc2CSC_311023_102.py
def main(page: nlxFT.Page):
    # Page initializers
    page.bgcolor = "#fdfdfd"
    page.padding = 20
    page.window_height = 940
    page.window_width = 1200
    page.window_maximizable = False
    page.window_maximized = False
    page.window_resizable = False
    page.window_center()

    def app_Header_Brand():
        return nlxFT.Container(
            content=nlxFT.IconButton(
                nlxFT.icons.REMOVE_RED_EYE_ROUNDED,
                icon_color="white"
            )
        )

    def app_Header_Search():
        return nlxFT.Container(
            width=320,
            padding=8,
            bgcolor='white10',
            border_radius=6,
            animate_opacity=320,
            disabled=False,
            content=nlxFT.Row(
                spacing=10,
                vertical_alignment=nlxFT.CrossAxisAlignment.CENTER,
                controls=[
                    nlxFT.Icon(name=nlxFT.icons.SEARCH_ROUNDED, size=17, opacity=0.85),
                    nlxFT.TextField("Search", color="#6A7784")
                ]
            )
        )
    page.add(
        nlxFT.Container(
            expand=True,
            height=1100,
            width=1200,
            content=nlxFT.Column(
                controls=[
                    # Header panel called here
                    nlxFT.Container(
                        bgcolor="#081d33", border_radius=nlxFT.border_radius.only(top_left=10, top_right=10, bottom_left=4, bottom_right=4),
                        padding=nlxFT.padding.only(left=15, right=15),
                        content=
                            nlxFT.Row(
                                height=50, expand=True, alignment=nlxFT.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[app_Header_Brand(), app_Header_Search()],
                            )
                        )
                    ]
                )
            )
        )
    for btn, item in zip(btnList, assetLst):
        # compareTest = item.label
        if "51" in item.label:  
            page.add(
                btn
            )
    
# Load Flet interface
nlxFT.app(target=main)
