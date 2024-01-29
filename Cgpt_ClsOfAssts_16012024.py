# NLX Swrd: CRAcc2CSC (code name: Lothlorien)
# Version: Celeborn
import flet as nlxFT
# from flet import (
#     TextButton
# )
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
assetBtn = assetButtonCls("GHQ.IDF49", "192.168.77.11", "Gi1/0/9", "rbt_CSC_111011")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.68", "192.168.77.11", "Gi1/0/9", "rbt_CSC_111012")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ MEZ.54", "192.168.77.11", "Gi1/0/9", "rbt_CSC_111013")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF48", "192.168.77.11", "Gi1/0/9", "rbt_CSC_111015")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF62", "192.168.77.11", "Gi1/0/9", "rbt_CSC_111017")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF47", "192.168.77.11", "Gi1/0/9", "rbt_CSC_111019")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.57", "192.168.77.11", "Gi1/0/9", "rbt_CSC_111025")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.19", "192.168.77.11", "Gi1/0/9", "rbt_CSC_111028")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.9", "192.168.77.11", "Gi1/0/9", "rbt_CSC_111029")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.15", "192.168.77.11", "Gi1/0/9", "rbt_CSC_111031")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.10", "192.168.77.11", "Gi1/0/9", "rbt_CSC_111033")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.6", "192.168.77.11", "Gi1/0/9", "rbt_CSC_111034")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.1", "192.168.77.11", "Gi1/0/9", "rbt_CSC_111035")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.2", "192.168.77.11", "Gi1/0/9", "rbt_CSC_111036")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.11", "192.168.77.11", "Gi1/0/9", "rbt_CSC_111037")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.13", "192.168.77.11", "Gi1/0/9", "rbt_CSC_111040")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.17", "192.168.77.11", "Gi1/0/9", "rbt_CSC_111042")
assetLst.append(assetBtn)

# Creating button list
# ----------   
btnList = []
for item in assetLst:
    print(item.label)
    print(item.btnDefinition)
    btnList.append(nlxFT.ElevatedButton(text=item.label, bgcolor=nlxFT.colors.BLUE_GREY_100, color=nlxFT.colors.BLACK, width=175, on_click=item.btnDefinition)) 
# ----------   

def app_Header_Brand():
        return nlxFT.Container(
            content=nlxFT.IconButton(
                nlxFT.icons.REMOVE_RED_EYE_ROUNDED,
                icon_color="white"
            )
        )

def app_Header_Avatar():
    return nlxFT.Container(
        content=nlxFT.IconButton(nlxFT.icons.PERSON_2_ROUNDED, icon_color="white")
    )

def app_Header_Search():
    return nlxFT.Container(
        width=450,
        padding=4,
        # bgcolor='white10',
        bgcolor="081d33",
        border_radius=6,
        # animate_opacity=320,
        disabled=False,
        content=nlxFT.Row(
            # spacing=10,
            # vertical_alignment=nlxFT.CrossAxisAlignment.CENTER,
            controls=[
                nlxFT.Icon(name=nlxFT.icons.SEARCH_ROUNDED, size=25, color="white"),
                nlxFT.TextField(bgcolor="white", text_size=15, width=400, hint_text="Search....")

            ]
        )
    )

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
                                # controls=[app_Header_Brand(), app_Header_Avatar()]
                                controls=[app_Header_Brand(), app_Header_Search(), app_Header_Avatar()]
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
# nlxFT.app(target=main)
