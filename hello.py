import sys
from PyQt5 import QtCore, QtGui, QtWidgets
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('ai')
    w.show()
    sys.exit(app.exec_())
