#!/usr/bin/env python
# -*- coding: utf-8 -*

import sys
from PySide import QtCore, QtGui, QtNetwork, QtUiTools

class ConnectWindow(object):
    def __init__(self, uifile):
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(uifile)
        self.server = self.ui.findChild(QtGui.QWidget, "server")
        self.port = self.ui.findChild(QtGui.QWidget, "port")
        self.name = self.ui.findChild(QtGui.QWidget, "name")

class TalkMainWindow(object):
    def __init__(self, uifile):
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(uifile)
        self.connectButton = self.ui.findChild(QtGui.QWidget, "connectButton")
        self.talkMain = self.ui.findChild(QtGui.QWidget, "talkMain")
        self.messageEdit = self.ui.findChild(QtGui.QWidget, "messageEdit")
        self.sendButton = self.ui.findChild(QtGui.QWidget, "sendButton")

        self.connectButton.clicked.connect(self.connect)
        self.ui.closeEvent = self.closeEvent

        self.socket = QtNetwork.QTcpSocket(self.ui)
        self.socket.readyRead.connect(self.readData)
        self.socket.error.connect(self.displayError)

    def connect(self):
        cw = ConnectWindow("connect.ui")
        if cw.ui.exec_() == QtGui.QDialog.Accepted:
            self.socket.connectToHost(cw.server.text(), int(cw.port.text()))
            if self.socket.waitForConnected(1000):
                self.name = cw.name.text()
                self.send("login %s" % self.name)
                self.sendButton.clicked.connect(self.sendClick)
                self.messageEdit.returnPressed.connect(self.sendClick)
                self.messageEdit.setFocus()

    def readData(self):
        message = self.socket.readLine().data().decode("utf-8")
        self.talkMain.append(message)

    def send(self, message):
        self.socket.write(message.encode("utf-8"))

    def sendClick(self):
        self.send("say %s" % (self.messageEdit.text()))
        self.messageEdit.clear()
        self.messageEdit.setFocus()

    def displayError(self):
        QtGui.QMessageBox.information(self.ui, "Connection", "Error during connection")

    def closeEvent(self, event):
        self.socket.disconnectFromHost()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    tmw = TalkMainWindow("talk.ui")
    tmw.ui.show()
    sys.exit(app.exec_())
