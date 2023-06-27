# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(957, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.BackgroundFrame = QtWidgets.QFrame(self.centralwidget)
        self.BackgroundFrame.setStyleSheet("#BackgroundFrame{\n"
"   /*border: 1px solid black; */\n"
"   border-radius: 5px;\n"
"}")
        self.BackgroundFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BackgroundFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BackgroundFrame.setObjectName("BackgroundFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.BackgroundFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MenuBar = QtWidgets.QWidget(self.BackgroundFrame)
        self.MenuBar.setStyleSheet("#MenuBar{\n"
"   background-color: #ffffff;\n"
"   /*border: none;\n"
"   border-right: 1px solid white; */\n"
"   border-top-left-radius: 5px;\n"
"   border-bottom-left-radius: 5px;\n"
"}\n"
"\n"
"QFrame{\n"
"   background-color: rgb(0, 120, 215);\n"
"}\n"
"\n"
"QWidget{\n"
"    background-color: rgb(0, 120, 215);\n"
"}")
        self.MenuBar.setObjectName("MenuBar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.MenuBar)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TitleSection = QtWidgets.QWidget(self.MenuBar)
        self.TitleSection.setStyleSheet("QWidget{\n"
"    border-top-left-radius: 5px;\n"
"}")
        self.TitleSection.setObjectName("TitleSection")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.TitleSection)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.TitleContainer = QtWidgets.QWidget(self.TitleSection)
        self.TitleContainer.setObjectName("TitleContainer")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.TitleContainer)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.TitleButton = QtWidgets.QPushButton(self.TitleContainer)
        self.TitleButton.setStyleSheet("#TitleButton{\n"
"   background-color: none;\n"
"   border-radius: none;\n"
"   padding: 0px;\n"
"   margin: 4px;\n"
"   margin-top: 8px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/Icons/apeW.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TitleButton.setIcon(icon)
        self.TitleButton.setIconSize(QtCore.QSize(27, 27))
        self.TitleButton.setObjectName("TitleButton")
        self.gridLayout_6.addWidget(self.TitleButton, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.TitleContainer, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addWidget(self.TitleSection, 0, QtCore.Qt.AlignTop)
        self.ContentSection = QtWidgets.QWidget(self.MenuBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ContentSection.sizePolicy().hasHeightForWidth())
        self.ContentSection.setSizePolicy(sizePolicy)
        self.ContentSection.setStyleSheet("QPushButton{\n"
"    border-radius: none;\n"
"    background-color: none;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: rgb(0, 108, 190);\n"
"}\n"
"\n"
"#ContentSection{\n"
"    border-radius: none;\n"
"    background-color: none;\n"
"}")
        self.ContentSection.setObjectName("ContentSection")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.ContentSection)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.TopSpaceFrame = QtWidgets.QFrame(self.ContentSection)
        self.TopSpaceFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TopSpaceFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TopSpaceFrame.setObjectName("TopSpaceFrame")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.TopSpaceFrame)
        self.gridLayout_18.setContentsMargins(0, 20, 0, 10)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        spacerItem = QtWidgets.QSpacerItem(20, 175, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_18.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.TopSpaceFrame)
        self.VideoPageFrame = QtWidgets.QFrame(self.ContentSection)
        self.VideoPageFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VideoPageFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VideoPageFrame.setObjectName("VideoPageFrame")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.VideoPageFrame)
        self.gridLayout_14.setContentsMargins(0, 10, 0, 10)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.VideoPageBtn = QtWidgets.QPushButton(self.VideoPageFrame)
        self.VideoPageBtn.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("UI/Icons/Video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.VideoPageBtn.setIcon(icon1)
        self.VideoPageBtn.setIconSize(QtCore.QSize(22, 22))
        self.VideoPageBtn.setObjectName("VideoPageBtn")
        self.gridLayout_14.addWidget(self.VideoPageBtn, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.VideoPageFrame)
        self.ModelPageFrame = QtWidgets.QFrame(self.ContentSection)
        self.ModelPageFrame.setStyleSheet("QFrame{\n"
"    border-bottom-right-radius: 5px;\n"
"}")
        self.ModelPageFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ModelPageFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ModelPageFrame.setObjectName("ModelPageFrame")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.ModelPageFrame)
        self.gridLayout_15.setContentsMargins(0, 10, 0, 10)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.ModelPageBtn = QtWidgets.QPushButton(self.ModelPageFrame)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("UI/Icons/Model.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ModelPageBtn.setIcon(icon2)
        self.ModelPageBtn.setIconSize(QtCore.QSize(22, 22))
        self.ModelPageBtn.setObjectName("ModelPageBtn")
        self.gridLayout_15.addWidget(self.ModelPageBtn, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.ModelPageFrame)
        self.FinalPageFrame = QtWidgets.QFrame(self.ContentSection)
        self.FinalPageFrame.setStyleSheet("QFrame{\n"
"    background-color: #ffffff;\n"
"}")
        self.FinalPageFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FinalPageFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FinalPageFrame.setObjectName("FinalPageFrame")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.FinalPageFrame)
        self.gridLayout_16.setContentsMargins(0, 10, 0, 10)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.FinalPageBtn = QtWidgets.QPushButton(self.FinalPageFrame)
        self.FinalPageBtn.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("UI/Icons/Final.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FinalPageBtn.setIcon(icon3)
        self.FinalPageBtn.setIconSize(QtCore.QSize(22, 22))
        self.FinalPageBtn.setObjectName("FinalPageBtn")
        self.gridLayout_16.addWidget(self.FinalPageBtn, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.FinalPageFrame)
        self.BottomSpaceFrame = QtWidgets.QFrame(self.ContentSection)
        self.BottomSpaceFrame.setStyleSheet("QFrame{\n"
"    border-top-right-radius: 5px; \n"
"}")
        self.BottomSpaceFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BottomSpaceFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BottomSpaceFrame.setObjectName("BottomSpaceFrame")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.BottomSpaceFrame)
        self.gridLayout_19.setContentsMargins(0, 10, 0, 20)
        self.gridLayout_19.setSpacing(0)
        self.gridLayout_19.setObjectName("gridLayout_19")
        spacerItem1 = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_19.addItem(spacerItem1, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.BottomSpaceFrame)
        self.verticalLayout_2.addWidget(self.ContentSection)
        self.BottomSection = QtWidgets.QWidget(self.MenuBar)
        self.BottomSection.setStyleSheet("#BottomSection{\n"
"    border-bottom-left-radius: 5px;\n"
"}")
        self.BottomSection.setObjectName("BottomSection")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.BottomSection)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.SettingsBtn = QtWidgets.QPushButton(self.BottomSection)
        self.SettingsBtn.setStyleSheet("#SettingsBtn{\n"
"    background-color: none;\n"
"    border-radius: none;\n"
"    padding: 0px;\n"
"    margin: 4px;\n"
"    margin-top: 8px;\n"
"    margin-bottom: 8px;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("UI/Icons/settingH.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SettingsBtn.setIcon(icon4)
        self.SettingsBtn.setIconSize(QtCore.QSize(24, 24))
        self.SettingsBtn.setObjectName("SettingsBtn")
        self.gridLayout_17.addWidget(self.SettingsBtn, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.BottomSection)
        self.horizontalLayout.addWidget(self.MenuBar, 0, QtCore.Qt.AlignLeft)
        self.MainWidget = QtWidgets.QWidget(self.BackgroundFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainWidget.sizePolicy().hasHeightForWidth())
        self.MainWidget.setSizePolicy(sizePolicy)
        self.MainWidget.setStyleSheet("#MainWidget{\n"
"   border-top-right-radius: 5px;\n"
"   border-bottom-right-radius: 5px\n"
"}")
        self.MainWidget.setObjectName("MainWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MainWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TitleBar = QtWidgets.QWidget(self.MainWidget)
        self.TitleBar.setStyleSheet("#TitleBar{\n"
"   background-color: rgb(255, 255, 255);\n"
"   border-top-right-radius: 5px;\n"
"}")
        self.TitleBar.setObjectName("TitleBar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.TitleBar)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.TitleNameContainer = QtWidgets.QWidget(self.TitleBar)
        self.TitleNameContainer.setObjectName("TitleNameContainer")
        self.horizontalLayout_2.addWidget(self.TitleNameContainer)
        self.ButtonContainer = QtWidgets.QWidget(self.TitleBar)
        self.ButtonContainer.setStyleSheet("QPushButton{\n"
"   color: rgb(0, 0, 0);\n"
"   border-radius: none;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(0, 120, 215);\n"
"}\n"
"#CloseButton{\n"
"   border-top-right-radius: 5px;\n"
"} \n"
"#CloseButton:hover{\n"
"   background-color: rgb(170, 0, 0);\n"
"}")
        self.ButtonContainer.setObjectName("ButtonContainer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.ButtonContainer)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.MinContainer = QtWidgets.QWidget(self.ButtonContainer)
        self.MinContainer.setObjectName("MinContainer")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.MinContainer)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.MinimizeButton = QtWidgets.QPushButton(self.MinContainer)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("UI/Icons/minusB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MinimizeButton.setIcon(icon5)
        self.MinimizeButton.setIconSize(QtCore.QSize(41, 27))
        self.MinimizeButton.setObjectName("MinimizeButton")
        self.gridLayout_2.addWidget(self.MinimizeButton, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.MinContainer)
        self.MaxContainer = QtWidgets.QWidget(self.ButtonContainer)
        self.MaxContainer.setObjectName("MaxContainer")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.MaxContainer)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.MaximizeButton = QtWidgets.QPushButton(self.MaxContainer)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("UI/Icons/maximizeB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MaximizeButton.setIcon(icon6)
        self.MaximizeButton.setIconSize(QtCore.QSize(41, 28))
        self.MaximizeButton.setObjectName("MaximizeButton")
        self.gridLayout_3.addWidget(self.MaximizeButton, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.MaxContainer)
        self.CloseContainer = QtWidgets.QWidget(self.ButtonContainer)
        self.CloseContainer.setObjectName("CloseContainer")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.CloseContainer)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.CloseButton = QtWidgets.QPushButton(self.CloseContainer)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("UI/Icons/closeB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CloseButton.setIcon(icon7)
        self.CloseButton.setIconSize(QtCore.QSize(41, 28))
        self.CloseButton.setObjectName("CloseButton")
        self.gridLayout_4.addWidget(self.CloseButton, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.CloseContainer)
        self.horizontalLayout_2.addWidget(self.ButtonContainer, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.TitleBar, 0, QtCore.Qt.AlignTop)
        self.Content = QtWidgets.QWidget(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Content.sizePolicy().hasHeightForWidth())
        self.Content.setSizePolicy(sizePolicy)
        self.Content.setStyleSheet("#Content{\n"
"   border-bottom-right-radius: 5px;\n"
"   background-color: rgb(255, 255, 255);\n"
"}")
        self.Content.setObjectName("Content")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.Content)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.stackedWidget = QtWidgets.QStackedWidget(self.Content)
        self.stackedWidget.setObjectName("stackedWidget")
        self.VideoPage = QtWidgets.QWidget()
        self.VideoPage.setStyleSheet("")
        self.VideoPage.setObjectName("VideoPage")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.VideoPage)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.VidPageBackground = QtWidgets.QWidget(self.VideoPage)
        self.VidPageBackground.setStyleSheet("")
        self.VidPageBackground.setObjectName("VidPageBackground")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.VidPageBackground)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.VideoBox = QtWidgets.QWidget(self.VidPageBackground)
        self.VideoBox.setMinimumSize(QtCore.QSize(640, 0))
        self.VideoBox.setSizeIncrement(QtCore.QSize(1, 0))
        self.VideoBox.setObjectName("VideoBox")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.VideoBox)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.VideoFrame = QtWidgets.QFrame(self.VideoBox)
        self.VideoFrame.setStyleSheet("#VideoFrame{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}")
        self.VideoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VideoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VideoFrame.setObjectName("VideoFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.VideoFrame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.VideoContainer = QtWidgets.QWidget(self.VideoFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoContainer.sizePolicy().hasHeightForWidth())
        self.VideoContainer.setSizePolicy(sizePolicy)
        self.VideoContainer.setObjectName("VideoContainer")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.VideoContainer)
        self.gridLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.ImportVidbtn = QtWidgets.QPushButton(self.VideoContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImportVidbtn.sizePolicy().hasHeightForWidth())
        self.ImportVidbtn.setSizePolicy(sizePolicy)
        self.ImportVidbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ImportVidbtn.setStyleSheet("#ImportVidbtn{\n"
"    border-radius: 5px;\n"
"    border-color: #0078d7;\n"
"    border: 1px solid gray;\n"
"    margin: 20px;\n"
"}")
        self.ImportVidbtn.setObjectName("ImportVidbtn")
        self.gridLayout_9.addWidget(self.ImportVidbtn, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.VideoContainer)
        self.VideoTools = QtWidgets.QWidget(self.VideoFrame)
        self.VideoTools.setStyleSheet("QPushButton{\n"
"    border-radius: none;\n"
"}")
        self.VideoTools.setObjectName("VideoTools")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.VideoTools)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.ToolsContainer = QtWidgets.QFrame(self.VideoTools)
        self.ToolsContainer.setStyleSheet("#ToolsContainer{\n"
"    background-color: rgb(240, 240, 240);\n"
"    border-radius: 5px;\n"
"}")
        self.ToolsContainer.setObjectName("ToolsContainer")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.ToolsContainer)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.PreviousFrame = QtWidgets.QPushButton(self.ToolsContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PreviousFrame.sizePolicy().hasHeightForWidth())
        self.PreviousFrame.setSizePolicy(sizePolicy)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("UI/Icons/previousBu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PreviousFrame.setIcon(icon8)
        self.PreviousFrame.setObjectName("PreviousFrame")
        self.horizontalLayout_5.addWidget(self.PreviousFrame)
        self.PlaynPause = QtWidgets.QPushButton(self.ToolsContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlaynPause.sizePolicy().hasHeightForWidth())
        self.PlaynPause.setSizePolicy(sizePolicy)
        self.PlaynPause.setObjectName("PlaynPause")
        self.horizontalLayout_5.addWidget(self.PlaynPause)
        self.NextFrame = QtWidgets.QPushButton(self.ToolsContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NextFrame.sizePolicy().hasHeightForWidth())
        self.NextFrame.setSizePolicy(sizePolicy)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("UI/Icons/nextBu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NextFrame.setIcon(icon9)
        self.NextFrame.setObjectName("NextFrame")
        self.horizontalLayout_5.addWidget(self.NextFrame)
        self.horizontalSlider = QtWidgets.QSlider(self.ToolsContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setStyleSheet("QSlider{\n"
"    margin-top: 0px;\n"
"    margin-bottom: 0px;\n"
"    margin-right: 5px;\n"
"    margin-left: 5px;\n"
"}\n"
"                                          \n"
"QSlider::groove{                                            \n"
"   border-radius: 1px;\n"
"   height: 3px;\n"
"   margin: 0px;\n"
"   background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QSlider::handle{\n"
"   border: none;\n"
"   height: 10px;\n"
"   width: 10px;\n"
"   margin: -4px;\n"
"   border-radius: 5px;\n"
"   background-color: rgb(0, 120, 215);\n"
"}")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_5.addWidget(self.horizontalSlider)
        self.PreviewBtn = QtWidgets.QPushButton(self.ToolsContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PreviewBtn.sizePolicy().hasHeightForWidth())
        self.PreviewBtn.setSizePolicy(sizePolicy)
        self.PreviewBtn.setStyleSheet("#PreviewBtn{\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 120, 215);\n"
"    background-color: rgb(0, 120, 215);\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 5px;\n"
"    padding-left: 15px;\n"
"    padding-right: 15px;\n"
"}\n"
"\n"
"#PreviewBtn::hover{\n"
"    background-color:rgb(0, 108, 190);\n"
"    border-color:  rgb(0, 120, 215);\n"
"}\n"
"\n"
"#PreviewBtn::selected{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.PreviewBtn.setObjectName("PreviewBtn")
        self.horizontalLayout_5.addWidget(self.PreviewBtn)
        self.gridLayout_12.addWidget(self.ToolsContainer, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.VideoTools)
        self.gridLayout_10.addWidget(self.VideoFrame, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.VideoBox)
        self.VideoOptions = QtWidgets.QFrame(self.VidPageBackground)
        self.VideoOptions.setStyleSheet("#VideoOptions{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-bottom-right-radius: 5px;\n"
"}")
        self.VideoOptions.setObjectName("VideoOptions")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.VideoOptions)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.widget = QtWidgets.QWidget(self.VideoOptions)
        self.widget.setObjectName("widget")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.listView = QtWidgets.QListWidget(self.widget)
        self.listView.setStyleSheet("#listView{\n"
"   background-color: rgb(255, 255, 255);\n"
"}")
        self.listView.setObjectName("listView")
        self.gridLayout_13.addWidget(self.listView, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.widget, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.VideoOptions)
        self.gridLayout_8.addWidget(self.VidPageBackground, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.VideoPage)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_7.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.Content)
        self.horizontalLayout.addWidget(self.MainWidget)
        self.gridLayout.addWidget(self.BackgroundFrame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ImportVidbtn.setText(_translate("MainWindow", "Import Video"))
        self.PreviewBtn.setText(_translate("MainWindow", "Preview"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
