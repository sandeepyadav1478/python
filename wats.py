# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wats.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import json
import time
import os.path
from os import path
from beeply import notes
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow,QListWidget,QListWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from ibm_watson import TextToSpeechV1
from ibm_watson import SpeechToTextV1
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
api=IAMAuthenticator("Fr1sIw0MVmpEnBzMQQifCVqW8g8gUrwT0yLFeCnwG4gn")
speech2 = SpeechToTextV1(authenticator=api)
speech2.set_service_url("https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/c5ca64ad-da78-48ba-8908-46692d80216e")
api1=IAMAuthenticator("oy7NkalihbjECm8i9zNBH01jIfEnGWuVAu01fwwk57Sj")
text2 = TextToSpeechV1(authenticator=api1)
text2.set_service_url("https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/13fa20c6-adcc-4a12-a4a7-d788d384a3c0")
mybeep=notes.beeps(200)
class MainWindow(QMainWindow):
    fileName=""
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setObjectName("MainWindow")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setFixedSize(590, 597)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setWindowTitle(" WATSON S<=>T")
        self.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 591, 651))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(14)
        font.setItalic(True)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.119, stop:0 rgba(35, 208, 194, 255), stop:1 rgba(2, 124, 156, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.fileloc = QtWidgets.QLineEdit(self.frame)
        self.fileloc.setGeometry(QtCore.QRect(30, 160, 431, 31))
        self.fileloc.setAutoFillBackground(False)
        self.fileloc.setStyleSheet("border:1px solid white;border-top-right-radius: 15px 15px;border-top-left-radius: 15px 15px;border-bottom-right-radius: 15px 15px;border-bottom-left-radius: 15px 15px;color:white;")
        self.fileloc.setInputMask("")
        self.fileloc.setText("")
        self.fileloc.setFrame(True)
        self.fileloc.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.fileloc.setAlignment(QtCore.Qt.AlignCenter)
        self.fileloc.setDragEnabled(True)
        self.fileloc.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.fileloc.setClearButtonEnabled(True)
        self.fileloc.setObjectName("fileloc")
        self.hdivider1 = QtWidgets.QFrame(self.frame)
        self.hdivider1.setWindowModality(QtCore.Qt.ApplicationModal)
        self.hdivider1.setGeometry(QtCore.QRect(-10, 70, 601, 41))
        self.hdivider1.setStyleSheet("")
        self.hdivider1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hdivider1.setFrameShape(QtWidgets.QFrame.HLine)
        self.hdivider1.setObjectName("hdivider1")
        self.header = QtWidgets.QLabel(self.frame)
        self.header.setGeometry(QtCore.QRect(160, 20, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(16)
        self.header.setFont(font)
        self.header.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.header.setAutoFillBackground(False)
        self.header.setStyleSheet("background-color:transparent;color:white;")
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.btn_browse = QtWidgets.QPushButton(self.frame)
        self.btn_browse.setGeometry(QtCore.QRect(470, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Nasalization")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_browse.setFont(font)
        self.btn_browse.setStyleSheet("border:1px solid white;border-top-right-radius: 15px 15px;border-top-left-radius: 15px 15px;border-bottom-right-radius: 15px 15px;border-bottom-left-radius: 15px 15px;color:white;")
        self.btn_browse.setObjectName("btn_browse")
        self.btn_tts = QtWidgets.QPushButton(self.frame)
        self.btn_tts.setGeometry(QtCore.QRect(50, 240, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Nasalization")
        self.btn_tts.setFont(font)
        self.btn_tts.setAutoFillBackground(False)
        self.btn_tts.setStyleSheet("border:1px solid white;border-top-right-radius: 15px 15px;border-top-left-radius: 15px 15px;border-bottom-right-radius: 15px 15px;border-bottom-left-radius: 15px 15px;color:white;")
        self.btn_tts.setAutoDefault(False)
        self.btn_tts.setObjectName("btn_tts")
        self.statusbar = QtWidgets.QLabel(self.frame)
        self.statusbar.setGeometry(QtCore.QRect(30, 400, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Rajdhani")
        font.setPointSize(14)
        self.statusbar.setFont(font)
        self.statusbar.setStyleSheet("background-color:transparent;color:#333;color:white;")
        self.statusbar.setObjectName("statusbar")
        self.btn_sst = QtWidgets.QPushButton(self.frame)
        self.btn_sst.setGeometry(QtCore.QRect(310, 240, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Nasalization")
        self.btn_sst.setFont(font)
        self.btn_sst.setAutoFillBackground(False)
        self.btn_sst.setStyleSheet("border:1px solid white;border-top-right-radius: 15px 15px;border-top-left-radius: 15px 15px;border-bottom-right-radius: 15px 15px;border-bottom-left-radius: 15px 15px;color:white;")
        self.btn_sst.setAutoDefault(False)
        self.btn_sst.setObjectName("btn_sst")
        self.hdivider1_2 = QtWidgets.QFrame(self.frame)
        self.hdivider1_2.setWindowModality(QtCore.Qt.ApplicationModal)
        self.hdivider1_2.setGeometry(QtCore.QRect(-10, 350, 601, 41))
        self.hdivider1_2.setAutoFillBackground(False)
        self.hdivider1_2.setStyleSheet("")
        self.hdivider1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hdivider1_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.hdivider1_2.setObjectName("hdivider1_2")
        self.status_list = QtWidgets.QListWidget(self.frame)
        self.status_list.setGeometry(QtCore.QRect(25, 431, 521, 151))
        font = QtGui.QFont()
        font.setFamily("Rajdhani")
        font.setPointSize(11)
        self.status_list.setFont(font)
        self.status_list.setStyleSheet("border:1px solid white;border-top-right-radius: 15px 15px;border-top-left-radius: 15px 15px;border-bottom-right-radius: 15px 15px;border-bottom-left-radius: 15px 15px;color:white;padding:10px;")
        self.status_list.setObjectName("status_list")
        self.ins = QtWidgets.QLabel(self.frame)
        self.ins.setGeometry(QtCore.QRect(30, 310, 521, 31))
        font = QtGui.QFont()
        font.setFamily("Rajdhani")
        font.setPointSize(11)
        self.ins.setFont(font)
        self.ins.setStyleSheet("background-color:transparent;color:#333;color:black;")
        self.ins.setAlignment(QtCore.Qt.AlignCenter)
        self.ins.setObjectName("ins")
        self.err = QtWidgets.QLabel(self.frame)
        self.err.setGeometry(QtCore.QRect(30, 120, 521, 31))
        font = QtGui.QFont()
        font.setFamily("Nasalization")
        font.setPointSize(10)
        self.err.setFont(font)
        self.err.setStyleSheet("background-color:transparent;color:#ff1a1a;")
        self.err.setAlignment(QtCore.Qt.AlignCenter)
        self.err.setObjectName("err")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.btn_browse.clicked.connect(self.openFileNameDialog)
        self.btn_tts.clicked.connect(self.textreader)
        self.btn_sst.clicked.connect(self.speechreader)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files(*.*);;Text Files(*.txt);;MPEG-1 Audio (*.mp3)", options=options)
        ext=self.fileName.find(".txt")
        ext1=self.fileName.find(".mp3")
        if self.fileName:
            if ext != -1:
                self.listdata("Imported Text file :"+self.fileName,"darkGreen")
                self.fileloc.setText(self.fileName)
            elif ext1 != -1:
                self.listdata("Imported MP3 file :"+self.fileName,"darkGreen")
                self.fileloc.setText(self.fileName)            
            else:
                self.listdata("Invalid file format :"+self.fileName,"yellow")
                self.err.setText("Invalid file format")                

        else:
            self.listdata("Invalid file format or No file picked","yellow")
        self.status_list.scrollToBottom()
        mybeep.hear('C_')
    def textreader(self):
        self.listdata("Converting...","white")
        filepath=self.fileName
        if filepath=="":
            self.err.setText("Choose a file")
            mybeep.hear('C_')
            return
        if filepath.find(".mp3") != -1:
            self.err.setText("Wrong operation")
            self.listdata("Operation Terminated.","yellow")
            mybeep.hear('C_')
            self.status_list.scrollToBottom()
            return
        QApplication.setOverrideCursor(Qt.WaitCursor)
        with open(filepath) as tf:
            data=tf.read()
            tf.close()
            if data == "":
                self.status_list.addItem("Empty Text file")
            filepath=filepath.replace(".txt",".mp3")
            fn=self.fwriter(filepath,".mp3")
            with open(fn,"wb") as audf:
                try:
                    audf.write(text2.synthesize(data,accept ="audio/mp3",voice="en-US_AllisonVoice").get_result().content)
                except ApiException as ex1:
                    self.listdata("Method failed with status code:\n" +str(ex1.code)+":"+ex1.message,"red")
                    self.err.setText(ex1.message)
                else:  
                    self.listdata("Text file converted sucessfully\nMP3 at this location :"+fn,"darkGreen")    
            self.status_list.scrollToBottom()
        mybeep.hear('E_')   
        QApplication.restoreOverrideCursor()

    def speechreader(self):
        if self.fileName=="":
            self.err.setText("Choose a file")
            return
        if self.fileName.find(".txt") != -1:
            self.err.setText("Wrong operation")
            self.listdata("Operation Terminated.","yellow")
            mybeep.hear('C_')
            self.status_list.scrollToBottom()
            return
        self.listdata("Converting...","white")
        QApplication.setOverrideCursor(Qt.WaitCursor)

        with open(self.fileName,"rb") as audiof:
            try:
                result = speech2.recognize(audio = audiof,content_type="audio/mp3").get_result()
            except ApiException as ex1:
                self.listdata("Method failed with status code:\n" +str(ex1.code)+":"+ex1.message,"red")
                self.err.setText(ex1.message)
            else:
                self.fileName=self.fileName.replace('.mp3','.txt')
                fn=str(self.fwriter(self.fileName,".txt"))
                tf=open(fn,'w')
                tf.write(result['results'][0]['alternatives'][0]['transcript'])
                self.listdata("Successfully converted, Confidence level:"+str(result['results'][0]['alternatives'][0]['confidence'])+"\n and Exported text file at: "+fn,"darkGreen")
                tf.close()
            self.status_list.scrollToBottom()
        mybeep.hear('E_')
        QApplication.restoreOverrideCursor()

    def listdata(self,data,color):
        temp=QListWidgetItem(data)
        if color=='red':
            temp.setForeground(Qt.red)
        if color=='darkGreen':
            temp.setForeground(Qt.darkGreen)
        if color=='yellow':
            temp.setForeground(Qt.yellow)
        if color=='white':
            temp.setForeground(Qt.white)
        if color=='black':
            temp.setForeground(Qt.black)
        self.status_list.addItem(temp)

    def fwriter(self,floc,typ):
        if floc=="":
            return
        elif str(path.exists(floc))=="True":
            floc=floc.replace(typ,'')
            floc=floc+"1"
            floc=floc+typ
            return self.fwriter(floc,typ)
        else:
            return floc

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.fileloc.setPlaceholderText(_translate("MainWindow", "Enter file location"))
        self.header.setText(_translate("MainWindow", "IBM WATSON S2T,T2S"))
        self.btn_browse.setText(_translate("MainWindow", "Browse"))
        self.btn_tts.setText(_translate("MainWindow", "Text to Speech"))
        self.statusbar.setText(_translate("MainWindow", "Status"))
        self.btn_sst.setText(_translate("MainWindow", "Speech to Text"))
        self.ins.setText(_translate("MainWindow", "*Enter Your file Location then press any botton according to requirement.\n*File Format:'.mp3' or '.text',Text Size: <=5Kb"))
        self.err.setText(_translate("MainWindow", ""))
        self.listdata("Program Initialized.","black")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MW1= MainWindow()
    MW1.show()
    sys.exit(app.exec_())
