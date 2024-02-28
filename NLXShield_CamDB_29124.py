# The Class is of type NLXShield
class assetButtonCls:
    def __init__(self, label, location, locationIcon, assetIP, interface, btnDefinition):
        self.label = label
        self.location = location
        self.locationIcon = locationIcon
        self.assetIP = assetIP
        self.interface = interface
        self.btnDefinition = btnDefinition

    def click(self):
        print(f"Button '{self.label}' clicked. Performing action: {self.action}")

# Remove if not used
# Note! Currently not in use
class IterableList:
    def __init__(self):
        self.my_list = []

    def add_element(self, element):
        self.my_list.append(element)

    def iterate_list(self):
        for element in self.my_list:
            yield element

# Example usage:
# Global HQ 1st Floor Server Room Cameras
# --------------------
assetBtn = assetButtonCls("GHQ.IDF46", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/2", "rbt_CSC_11101")
assetLst = [assetBtn]
assetBtn = assetButtonCls("GHQ.MEZ.66", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/2", "rbt_CSC_11103")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.61", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/4", "rbt_CSC_11104")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF59", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/5", "rbt_CSC_11105")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.51", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/6", "rbt_CSC_11106")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.42", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/8", "rbt_CSC_11108")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF63", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/9", "rbt_CSC_11109")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF49", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/11", "rbt_CSC_111011")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.68", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/12", "rbt_CSC_111012")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.54", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/13", "rbt_CSC_111013") # QA Fixed
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF48", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/15", "rbt_CSC_111015")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF62", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/17", "rbt_CSC_111017")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF47", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/19", "rbt_CSC_111019")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.57", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/25", "rbt_CSC_111025")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.19", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/28", "rbt_CSC_111028")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.9", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/29", "rbt_CSC_111029")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.15", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/31", "rbt_CSC_111031")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.10", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/33", "rbt_CSC_111033")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.6", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/34", "rbt_CSC_111034")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.1", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/35", "rbt_CSC_111035")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.2", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/36", "rbt_CSC_111036")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.11", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/37", "rbt_CSC_111037")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.13", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/40", "rbt_CSC_111040")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.17", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/42", "rbt_CSC_111042")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.4", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/43", "rbt_CSC_111043")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.18", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/44", "rbt_CSC_111044")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.14", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/45", "rbt_CSC_111045")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.21", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/46", "rbt_CSC_111046")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.20", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi1/0/48", "rbt_CSC_111048")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.28", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/2", "rbt_CSC_11202")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF65", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/3", "rbt_CSC_11203")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.59", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/4", "rbt_CSC_11204") # QA
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF64", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/5", "rbt_CSC_11204") # QA
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.25", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/6", "rbt_CSC_11206")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF58", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/8", "rbt_CSC_11208") # QA
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.38", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/9", "rbt_CSC_11209")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.37", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/10", "rbt_CSC_112010")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.40", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/11", "rbt_CSC_112011")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF61", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/13", "rbt_CSC_112013")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.55", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/14", "rbt_CSC_112014")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.26", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/16", "rbt_CSC_112016")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.58", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/17", "rbt_CSC_112017")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.32", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/20", "rbt_CSC_112020")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF60", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi20/21", "rbt_CSC_112021")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.52", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/22", "rbt_CSC_112022")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.56", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/23", "rbt_CSC_112023")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.35", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/24", "rbt_CSC_112024")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.60", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/25", "rbt_CSC_112025")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.24", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/26", "rbt_CSC_112026")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.34", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/27", "rbt_CSC_112027")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.16", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/28", "rbt_CSC_112028")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.53", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/29", "rbt_CSC_112029")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.43", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/30", "rbt_CSC_112030")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.12", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/31", "rbt_CSC_112031")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.22", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/32", "rbt_CSC_112032")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.67", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/33", "rbt_CSC_112033")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.30", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/34", "rbt_CSC_112034")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.3", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/35", "rbt_CSC_112035")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.5", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/36", "rbt_CSC_112036")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.41", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/38", "rbt_CSC_112038")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.48", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/40", "rbt_CSC_112040")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.49", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi2/0/42", "rbt_CSC_112042")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.23", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi3/0/1", "rbt_CSC_113011")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.39", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi3/0/13", "rbt_CSC_113013")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.62", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi3/0/15", "rbt_CSC_113015")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.31", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi3/0/17", "rbt_CSC_113017")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.36", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi3/0/19", "rbt_CSC_113019")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.33", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi3/0/33", "rbt_CSC_113033")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.63", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi3/0/34", "rbt_CSC_113034")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.47", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi3/0/36", "rbt_CSC_113036")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.27", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi3/0/37", "rbt_CSC_113037")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF66", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi3/0/38", "rbt_CSC_113038")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.29", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi3/0/39", "rbt_CSC_113039")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.64", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi3/0/40", "rbt_CSC_113040")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.44", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi3/0/41", "rbt_CSC_113041")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF67", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi3/0/42", "rbt_CSC_113042")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.45", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi3/0/43", "rbt_CSC_113043")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.50", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi3/0/44", "rbt_CSC_113044")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.46", "HQ", "BUSINESS_ROUNDED", "192.168.77.11", "Gi3/0/45", "rbt_CSC_113045")
assetLst.append(assetBtn)
# --------------------

# Global HQ 8th Floor IDF Room Cameras
# --------------------
assetBtn = assetButtonCls("GHQ.IDF31", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/1", "rbt_CSC_14101")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF5", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/2", "rbt_CSC_14102")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF35", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/3", "rbt_CSC_14103")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF3", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/4", "rbt_CSC_14104")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF38", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/5", "rbt_CSC_14105")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF29", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/6", "rbt_CSC_14106")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF43", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/7", "rbt_CSC_14107")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF45", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/9", "rbt_CSC_14109")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF51", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/10", "rbt_CSC_141010")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF40", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/11", "rbt_CSC_141011")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF33", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/13", "rbt_CSC_141013")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.7", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/14", "rbt_CSC_141014")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF26", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/15", "rbt_CSC_141015")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF50", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/17", "rbt_CSC_141017")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF9", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/18", "rbt_CSC_141018")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF42", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/19", "rbt_CSC_141019")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF27", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/20", "rbt_CSC_141020")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF37", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/21", "rbt_CSC_141021") # Corrected
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF68", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/22", "rbt_CSC_141022")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF39", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/23", "rbt_CSC_141023")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF69", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/24", "rbt_CSC_141024")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF53", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/25", "rbt_CSC_141025")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF10", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/27", "rbt_CSC_141027")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF11", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/29", "rbt_CSC_141029")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF36", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/31", "rbt_CSC_141031")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF52", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/33", "rbt_CSC_141033")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF32", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/35", "rbt_CSC_141035")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF7", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/37", "rbt_CSC_141037")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF1", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/37", "rbt_CSC_141037")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF41", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/41", "rbt_CSC_141041")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF30", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/43", "rbt_CSC_141043")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF16", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/44", "rbt_CSC_141044")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF56", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/45", "rbt_CSC_141045")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF19", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi1/0/46", "rbt_CSC_141046")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF8", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi2/0/1", "rbt_CSC_14201")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF21", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi2/0/3", "rbt_CSC_14203")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF12", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi2/0/5", "rbt_CSC_14205")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF14", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi2/0/7", "rbt_CSC_14207")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.MEZ.8", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi2/0/10", "rbt_CSC_142010")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF44", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi2/0/11", "rbt_CSC_142011")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF22", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi2/0/13", "rbt_CSC_142013")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF25", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi2/0/15", "rbt_CSC_142015")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF55", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi2/0/17", "rbt_CSC_142017")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF2", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi2/0/18", "rbt_CSC_142018")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF28", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi2/0/19", "rbt_CSC_142019")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF57", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi2/0/21", "rbt_CSC_142021")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF15", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi2/0/22", "rbt_CSC_142022") # QA Corrected
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF18", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi2/0/25", "rbt_CSC_142025")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF54", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi2/0/27", "rbt_CSC_142027")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF20", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi2/0/28", "rbt_CSC_142028")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF23", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi2/0/32", "rbt_CSC_142032")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF34", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi2/0/33", "rbt_CSC_142033")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF17", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi2/0/35", "rbt_CSC_142035")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF13", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi2/0/36", "rbt_CSC_142036")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF4", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi2/0/37", "rbt_CSC_142037")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF24", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi2/0/38", "rbt_CSC_142038")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("GHQ.IDF6", "HQ IDF Room", "MEETING_ROOM_ROUNDED", "192.168.77.14", "Gi2/0/40", "rbt_CSC_142040")
assetLst.append(assetBtn)
# --------------------

# OLD HQ Server Room Cameras
# --------------------
assetBtn = assetButtonCls("OHQ8", "Old HQ Server Room", "HOME_WORK_ROUNDED", "192.168.77.13", "Gi1/0/1", "rbt_CSC_13101")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ17", "Old HQ Server Room", "HOME_WORK_ROUNDED", "192.168.77.13", "Gi1/0/2", "rbt_CSC_13102")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ3", "Old HQ Server Room", "HOME_WORK_ROUNDED", "192.168.77.13", "Gi1/0/4", "rbt_CSC_13104")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ5", "Old HQ Server Room", "HOME_WORK_ROUNDED", "192.168.77.13", "Gi1/0/5", "rbt_CSC_13105")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ19", "Old HQ Server Room", "HOME_WORK_ROUNDED", "192.168.77.13", "Gi1/0/6", "rbt_CSC_13106")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ6", "Old HQ Server Room", "HOME_WORK_ROUNDED", "192.168.77.13", "Gi1/0/7", "rbt_CSC_13107")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ20", "Old HQ Server Room", "HOME_WORK_ROUNDED", "192.168.77.13", "Gi1/0/8", "rbt_CSC_13108")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ10", "Old HQ Server Room", "HOME_WORK_ROUNDED", "192.168.77.13", "Gi1/0/9", "rbt_CSC_13109")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ4", "Old HQ Server Room", "HOME_WORK_ROUNDED", "192.168.77.13", "Gi1/0/11", "rbt_CSC_131011")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ9", "Old HQ Server Room", "HOME_WORK_ROUNDED", "192.168.77.13", "Gi1/0/13", "rbt_CSC_131013")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ11", "Old HQ Server Room", "HOME_WORK_ROUNDED", "192.168.77.13", "Gi1/0/15", "rbt_CSC_131015")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ1", "Old HQ Server Room", "HOME_WORK_ROUNDED", "192.168.77.13", "Gi1/0/17", "rbt_CSC_131017")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ12", "Old HQ Server Room", "HOME_WORK_ROUNDED", "192.168.77.13", "Gi1/0/19", "rbt_CSC_131019")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ18", "Old HQ Server Room", "HOME_WORK_ROUNDED", "192.168.77.13", "Gi1/0/21", "rbt_CSC_131021")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ16", "Old HQ Server Room", "HOME_WORK_ROUNDED", "192.168.77.13", "Gi1/0/39", "rbt_CSC_131039")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ15", "Old HQ Server Room", "HOME_WORK_ROUNDED", "192.168.77.13", "Gi1/0/41", "rbt_CSC_131041")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ14", "Old HQ Server Room", "HOME_WORK_ROUNDED", "192.168.77.13", "Gi1/0/43", "rbt_CSC_131043")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ13", "Old HQ Server Room", "HOME_WORK_ROUNDED", "192.168.77.13", "Gi1/0/47", "rbt_CSC_131047") # QA Added
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ7", "Old HQ Server Room", "HOME_WORK_ROUNDED", "192.168.77.13", "Gi1/0/3", "rbt_CSC_13103")
assetLst.append(assetBtn)
# --------------------

# Corner House Server Room Cameras
# --------------------
assetBtn = assetButtonCls("CRN.5", "Corner House Server Room", "HOUSE_SIDING_ROUNDED", "192.168.77.20", "Gi1/0/2", "rbt_CSC_20102")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("CRN.7", "Corner House Server Room", "HOUSE_SIDING_ROUNDED", "192.168.77.20", "Gi1/0/3", "rbt_CSC_20103")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("CRN.10", "Corner House Server Room", "HOUSE_SIDING_ROUNDED", "192.168.77.20", "Gi1/0/4", "rbt_CSC_20104")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("CRN.9", "Corner House Server Room", "HOUSE_SIDING_ROUNDED", "192.168.77.20", "Gi1/0/5", "rbt_CSC_20105")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("CRN.6", "Corner House Server Room", "HOUSE_SIDING_ROUNDED", "192.168.77.20", "Gi1/0/6", "rbt_CSC_20106")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("CRN.1", "Corner House Server Room", "HOUSE_SIDING_ROUNDED", "192.168.77.20", "Gi1/0/7", "rbt_CSC_20107")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("CRN.4", "Corner House Server Room", "HOUSE_SIDING_ROUNDED", "192.168.77.20", "Gi1/0/8", "rbt_CSC_20108")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("CRN.12", "Corner House Server Room", "HOUSE_SIDING_ROUNDED", "192.168.77.20", "Gi1/0/9", "rbt_CSC_20109")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("CRN.2", "Corner House Server Room", "HOUSE_SIDING_ROUNDED", "192.168.77.20", "Gi1/0/10", "rbt_CSC_201010")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("CRN.3", "Corner House Server Room", "HOUSE_SIDING_ROUNDED", "192.168.77.20", "Gi1/0/11", "rbt_CSC_201011")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("CRN.8", "Corner House Server Room", "HOUSE_SIDING_ROUNDED", "192.168.77.20", "Gi1/0/12", "rbt_CSC_201012")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("CRN.13", "Corner House Server Room", "HOUSE_SIDING_ROUNDED", "192.168.77.20", "Gi1/0/13", "rbt_CSC_201013")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("CRN.11", "Corner House Server Room", "HOUSE_SIDING_ROUNDED", "192.168.77.20", "Gi1/0/14", "rbt_CSC_201014")
assetLst.append(assetBtn)
# --------------------

# Parking 1 Cameras
# --------------------
assetBtn = assetButtonCls("OHQ.PRK1.1", "Parking 1", "GARAGE_ROUNDED", "192.168.201.4", "Gi1/0/4", "rbt_CSC_4104")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ.PRK1.2", "Parking 1", "GARAGE_ROUNDED", "192.168.201.4", "Gi1/0/7", "rbt_CSC_4107")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ.PRK1.3", "Parking 1", "GARAGE_ROUNDED", "192.168.201.4", "Gi1/0/3", "rbt_CSC_4103")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ.PRK1.4", "Parking 1", "GARAGE_ROUNDED", "192.168.201.4", "Gi1/0/2", "rbt_CSC_4102")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ.PRK1.5", "Parking 1", "GARAGE_ROUNDED", "192.168.201.4", "Gi1/0/1", "rbt_CSC_4101")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ.PRK1.6", "Parking 1", "GARAGE_ROUNDED", "192.168.201.4", "Gi1/0/8", "rbt_CSC_4108") # Tested up to here
assetLst.append(assetBtn)
assetBtn = assetButtonCls("OHQ.PRK1.9", "Parking 1", "GARAGE_ROUNDED", "192.168.201.4", "Gi1/0/6", "rbt_CSC_4106") # Test asset
assetLst.append(assetBtn)
# --------------------

# House 1 Cameras
# --------------------
assetBtn = assetButtonCls("H1.6", "House 1", "HOME_ROUNDED", "192.168.200.3", "Gi1/0/8", "rbt_CSC_3101")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H1.3", "House 1", "HOME_ROUNDED", "192.168.200.3", "Gi1/0/2", "rbt_CSC_3102")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H1.8", "House 1", "HOME_ROUNDED", "192.168.200.3", "Gi1/0/3", "rbt_CSC_3103")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H1.9", "House 1", "HOME_ROUNDED", "192.168.200.3", "Gi1/0/4", "rbt_CSC_3104")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H1.7", "House 1", "HOME_ROUNDED", "192.168.200.3", "Gi1/0/5", "rbt_CSC_3105")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H1.10", "House 1", "HOME_ROUNDED", "192.168.200.3", "Gi1/0/6", "rbt_CSC_3106")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H1.2", "House 1", "HOME_ROUNDED", "192.168.200.3", "Gi1/0/7", "rbt_CSC_3107")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H1.11", "House 1", "HOME_ROUNDED", "192.168.200.3", "Gi1/0/8", "rbt_CSC_3108")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H1.4", "House 1", "HOME_ROUNDED", "192.168.200.3", "Gi1/0/10", "rbt_CSC_31010")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H1.5", "House 1", "HOME_ROUNDED", "192.168.200.3", "Gi1/0/11", "rbt_CSC_31011")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H1.1", "House 1", "HOME_ROUNDED", "192.168.200.3", "Gi1/0/12", "rbt_CSC_31012")
assetLst.append(assetBtn)
# --------------------

# House 2 Cameras
# --------------------
assetBtn = assetButtonCls("H2.2", "House 2", "HOME_ROUNDED", "192.168.200.40", "Gi1/0/1", "rbt_CSC_40101")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H2.14", "House 2", "HOME_ROUNDED", "192.168.200.40", "Gi1/0/1", "rbt_CSC_40105")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H2.7", "House 2", "HOME_ROUNDED", "192.168.200.40", "Gi1/0/1", "rbt_CSC_40106")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H2.9", "House 2", "HOME_ROUNDED", "192.168.200.40", "Gi1/0/1", "rbt_CSC_40108")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H2.8", "House 2", "HOME_ROUNDED", "192.168.200.40", "Gi1/0/1", "rbt_CSC_40109")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H2.6", "House 2", "HOME_ROUNDED", "192.168.200.40", "Gi1/0/1", "rbt_CSC_401017")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H2.10", "House 2", "HOME_ROUNDED", "192.168.200.40", "Gi1/0/19", "rbt_CSC_401019")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H2.19", "House 2", "HOME_ROUNDED", "192.168.200.40", "Gi1/0/23", "rbt_CSC_401023")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H2.20", "House 2", "HOME_ROUNDED", "192.168.200.41", "Fa0/17", "rbt_CSC_41017")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H2.21", "House 2", "HOME_ROUNDED", "192.168.200.41", "Fa0/19", "rbt_CSC_41019")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H2.12", "House 2", "HOME_ROUNDED", "192.168.200.41", "Fa0/21", "rbt_CSC_41021")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H2.18", "House 2", "HOME_ROUNDED", "192.168.200.41", "Fa0/22", "rbt_CSC_41022")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H2.16", "House 2", "HOME_ROUNDED", "192.168.200.41", "Fa0/23", "rbt_CSC_41023")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H2.17", "House 2", "HOME_ROUNDED", "192.168.200.41", "Fa0/24", "rbt_CSC_41024")
assetLst.append(assetBtn)
# --------------------

# House 3 Cameras
# --------------------
assetBtn = assetButtonCls("H3.16", "House 3", "HOME_ROUNDED", "192.168.200.72", "Fa0/17", "rbt_CSC_72017")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H3.21", "House 3", "HOME_ROUNDED", "192.168.200.72", "Fa0/18", "rbt_CSC_72018")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H3.2", "House 3", "HOME_ROUNDED", "192.168.200.72", "Fa0/19", "rbt_CSC_72019")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H3.17", "House 3", "HOME_ROUNDED", "192.168.200.72", "Fa0/20", "rbt_CSC_72020")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H3.20", "House 3", "HOME_ROUNDED", "192.168.200.72", "Fa0/21", "rbt_CSC_72021")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H3.18", "House 3", "HOME_ROUNDED", "192.168.200.72", "Fa0/22", "rbt_CSC_72022")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H3.14", "House 3", "HOME_ROUNDED", "192.168.200.72", "Fa0/23", "rbt_CSC_72023")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H3.9", "House 3", "HOME_ROUNDED", "192.168.200.73", "Fa0/17", "rbt_CSC_73017")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H3.8", "House 3", "HOME_ROUNDED", "192.168.200.73", "Fa0/18", "rbt_CSC_73018")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H3.13", "House 3", "HOME_ROUNDED", "192.168.200.73", "Fa0/19", "rbt_CSC_73019")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H3.15", "House 3", "HOME_ROUNDED", "192.168.200.73", "Fa0/20", "rbt_CSC_73020")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H3.5", "House 3", "HOME_ROUNDED", "192.168.200.73", "Fa0/21", "rbt_CSC_73021")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H3.19", "House 3", "HOME_ROUNDED", "192.168.200.73", "Fa0/22", "rbt_CSC_73022")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H3.3", "House 3", "HOME_ROUNDED", "192.168.200.73", "Fa0/23", "rbt_CSC_73023")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H3.6", "House 3", "HOME_ROUNDED", "192.168.200.74", "Fa0/24", "rbt_CSC_73024")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H3.4", "House 3", "HOME_ROUNDED", "192.168.200.74", "Fa0/17", "rbt_CSC_74017")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H3.12", "House 3", "HOME_ROUNDED", "192.168.200.74", "Fa0/18", "rbt_CSC_74018")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H3.10", "House 3", "HOME_ROUNDED", "192.168.200.74", "Fa0/20", "rbt_CSC_74020")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H3.1", "House 3", "HOME_ROUNDED", "192.168.200.74", "Fa0/21", "rbt_CSC_74021")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H3.7", "House 3", "HOME_ROUNDED", "192.168.200.74", "Fa0/22", "rbt_CSC_74022")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H3.11", "House 3", "HOME_ROUNDED", "192.168.200.74", "Fa0/23", "rbt_CSC_74023")
assetLst.append(assetBtn)
# --------------------

# House 4 Cameras
# --------------------
assetBtn = assetButtonCls("H4.10", "House 4", "HOME_ROUNDED", "192.168.200.100", "Fa0/17", "rbt_CSC_100017")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H4.8", "House 4", "HOME_ROUNDED", "192.168.200.100", "Fa0/19", "rbt_CSC_100019")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H4.4", "House 4", "HOME_ROUNDED", "192.168.200.100", "Fa0/21", "rbt_CSC_100021")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H4.9", "House 4", "HOME_ROUNDED", "192.168.200.100", "Fa0/23", "rbt_CSC_100023")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H4.3", "House 4", "HOME_ROUNDED", "192.168.200.101", "Fa0/17", "rbt_CSC_101017")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H4.2", "House 4", "HOME_ROUNDED", "192.168.200.101", "Fa0/18", "rbt_CSC_101018")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H4.1", "House 4", "HOME_ROUNDED", "192.168.200.101", "Fa0/20", "rbt_CSC_101020")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H4.5", "House 4", "HOME_ROUNDED", "192.168.200.101", "Fa0/22", "rbt_CSC_101022")
assetLst.append(assetBtn)
assetBtn = assetButtonCls("H4.7", "House 4", "HOME_ROUNDED", "192.168.200.101", "Fa0/24", "rbt_CSC_101024")
assetLst.append(assetBtn)
# --------------------