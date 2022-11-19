from PyQt5.QtWidgets import *
from PyQt5 import uic
import xml.etree.ElementTree as et
from lxml import etree

#parser = etree.XMLParser(dtd_validation=True)
#tree = etree.parse(r'C:\Users\LEGION\OneDrive\Desktop\Python\Pressure vessel GUI\App.qml', parser)



class XGui(QMainWindow):
    def __init__(self):
        super(XGui,self).__init__()
        uic.loadUi(r'C:\Users\LEGION\OneDrive\Desktop\Python\Pressure vessel GUI\App.qml', self)
        self.show()
def main():
    app=QApplication([])
    window=XGui()
    app.exec()
if __name__ == '__main__':
    main()


