# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/Dev/OpenCobolIDE/forms/ide.ui'
#
# Created: Wed Aug 20 16:14:09 2014
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from pyqode.core.qt import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1202, 824)
        MainWindow.setMinimumSize(QtCore.QSize(900, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ide-icons/rc/silex-192x192.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(256, 256))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.line_2 = QtWidgets.QFrame(self.page)
        self.line_2.setMinimumSize(QtCore.QSize(400, 0))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_9.addWidget(self.line_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 15)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.btNewFile = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btNewFile.sizePolicy().hasHeightForWidth())
        self.btNewFile.setSizePolicy(sizePolicy)
        self.btNewFile.setMinimumSize(QtCore.QSize(200, 0))
        icon = QtGui.QIcon.fromTheme("document-new")
        self.btNewFile.setIcon(icon)
        self.btNewFile.setObjectName("btNewFile")
        self.horizontalLayout_8.addWidget(self.btNewFile)
        self.btOpenFile = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btOpenFile.sizePolicy().hasHeightForWidth())
        self.btOpenFile.setSizePolicy(sizePolicy)
        self.btOpenFile.setMinimumSize(QtCore.QSize(200, 0))
        self.btOpenFile.setStyleSheet("")
        icon = QtGui.QIcon.fromTheme("document-open")
        self.btOpenFile.setIcon(icon)
        self.btOpenFile.setObjectName("btOpenFile")
        self.horizontalLayout_8.addWidget(self.btOpenFile)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.frameRecents = QtWidgets.QFrame(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameRecents.sizePolicy().hasHeightForWidth())
        self.frameRecents.setSizePolicy(sizePolicy)
        self.frameRecents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameRecents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameRecents.setObjectName("frameRecents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frameRecents)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelRecents = QtWidgets.QLabel(self.frameRecents)
        self.labelRecents.setObjectName("labelRecents")
        self.verticalLayout_4.addWidget(self.labelRecents)
        self.listWidgetRecents = RecentFilesListWidget(self.frameRecents)
        self.listWidgetRecents.setMinimumSize(QtCore.QSize(400, 0))
        self.listWidgetRecents.setObjectName("listWidgetRecents")
        self.verticalLayout_4.addWidget(self.listWidgetRecents)
        self.horizontalLayout_5.addWidget(self.frameRecents)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem9)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidgetEditors = TabWidget(self.page_2)
        self.tabWidgetEditors.setObjectName("tabWidgetEditors")
        self.gridLayout_2.addWidget(self.tabWidgetEditors, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBarFile = QtWidgets.QToolBar(MainWindow)
        self.toolBarFile.setObjectName("toolBarFile")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarFile)
        self.toolBarCode = QtWidgets.QToolBar(MainWindow)
        self.toolBarCode.setObjectName("toolBarCode")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarCode)
        self.dockWidgetLogs = QtWidgets.QDockWidget(MainWindow)
        self.dockWidgetLogs.setObjectName("dockWidgetLogs")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidgetLogs = QtWidgets.QTabWidget(self.dockWidgetContents)
        self.tabWidgetLogs.setObjectName("tabWidgetLogs")
        self.tabCompiler = QtWidgets.QWidget()
        self.tabCompiler.setObjectName("tabCompiler")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tabCompiler)
        self.gridLayout_4.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.errorsTable = ErrorsTable(self.tabCompiler)
        self.errorsTable.setMinimumSize(QtCore.QSize(0, 0))
        self.errorsTable.setObjectName("errorsTable")
        self.errorsTable.setColumnCount(5)
        self.errorsTable.setRowCount(0)
        self.gridLayout_4.addWidget(self.errorsTable, 0, 0, 1, 1)
        icon = QtGui.QIcon.fromTheme("emblem-important")
        self.tabWidgetLogs.addTab(self.tabCompiler, icon, "")
        self.tabProgramOutput = QtWidgets.QWidget()
        self.tabProgramOutput.setObjectName("tabProgramOutput")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tabProgramOutput)
        self.gridLayout_5.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.consoleOutput = InteractiveConsole(self.tabProgramOutput)
        self.consoleOutput.setObjectName("consoleOutput")
        self.gridLayout_5.addWidget(self.consoleOutput, 0, 0, 1, 1)
        icon = QtGui.QIcon.fromTheme("media-playback-start")
        self.tabWidgetLogs.addTab(self.tabProgramOutput, icon, "")
        self.gridLayout_3.addWidget(self.tabWidgetLogs, 1, 0, 1, 1)
        self.dockWidgetLogs.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidgetLogs)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1202, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.mnuActiveEditor = QtWidgets.QMenu(self.menuEdit)
        self.mnuActiveEditor.setObjectName("mnuActiveEditor")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuPerspective = QtWidgets.QMenu(self.menuView)
        self.menuPerspective.setObjectName("menuPerspective")
        self.menuCobol = QtWidgets.QMenu(self.menuBar)
        self.menuCobol.setObjectName("menuCobol")
        self.menuProgramType = QtWidgets.QMenu(self.menuCobol)
        self.menuProgramType.setObjectName("menuProgramType")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.dockWidgetNavPanel = QtWidgets.QDockWidget(MainWindow)
        self.dockWidgetNavPanel.setMinimumSize(QtCore.QSize(300, 121))
        self.dockWidgetNavPanel.setObjectName("dockWidgetNavPanel")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_7.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.twNavigation = OutlineTreeWidget(self.dockWidgetContents_2)
        self.twNavigation.setObjectName("twNavigation")
        self.twNavigation.headerItem().setText(0, "1")
        self.twNavigation.header().setVisible(False)
        self.gridLayout_7.addWidget(self.twNavigation, 0, 0, 1, 1)
        self.dockWidgetNavPanel.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidgetNavPanel)
        self.dockWidgetOffsets = QtWidgets.QDockWidget(MainWindow)
        self.dockWidgetOffsets.setMinimumSize(QtCore.QSize(318, 127))
        self.dockWidgetOffsets.setObjectName("dockWidgetOffsets")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tableWidgetOffsets = PicOffsetsTable(self.dockWidgetContents_3)
        self.tableWidgetOffsets.setMinimumSize(QtCore.QSize(300, 0))
        self.tableWidgetOffsets.setDragDropOverwriteMode(False)
        self.tableWidgetOffsets.setShowGrid(True)
        self.tableWidgetOffsets.setObjectName("tableWidgetOffsets")
        self.tableWidgetOffsets.setColumnCount(4)
        self.tableWidgetOffsets.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOffsets.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOffsets.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOffsets.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOffsets.setHorizontalHeaderItem(3, item)
        self.tableWidgetOffsets.horizontalHeader().setDefaultSectionSize(50)
        self.tableWidgetOffsets.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidgetOffsets.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetOffsets.verticalHeader().setVisible(False)
        self.gridLayout_8.addWidget(self.tableWidgetOffsets, 0, 0, 1, 1)
        self.dockWidgetOffsets.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidgetOffsets)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("window-close")
        self.actionQuit.setIcon(icon)
        self.actionQuit.setIconVisibleInMenu(True)
        self.actionQuit.setObjectName("actionQuit")
        self.actionRun = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("media-playback-start")
        self.actionRun.setIcon(icon)
        self.actionRun.setIconVisibleInMenu(True)
        self.actionRun.setObjectName("actionRun")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("help-about")
        self.actionAbout.setIcon(icon)
        self.actionAbout.setIconVisibleInMenu(True)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.actionSave.setIcon(icon)
        self.actionSave.setIconVisibleInMenu(True)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("document-save-as")
        self.actionSaveAs.setIcon(icon)
        self.actionSaveAs.setIconVisibleInMenu(True)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionFullscreen = QtWidgets.QAction(MainWindow)
        self.actionFullscreen.setCheckable(True)
        icon = QtGui.QIcon.fromTheme("view-fullscreen")
        self.actionFullscreen.setIcon(icon)
        self.actionFullscreen.setIconVisibleInMenu(True)
        self.actionFullscreen.setObjectName("actionFullscreen")
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.actionNew.setIcon(icon)
        self.actionNew.setIconVisibleInMenu(True)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("document-open")
        self.actionOpen.setIcon(icon)
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClear = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("edit-clear")
        self.actionClear.setIcon(icon)
        self.actionClear.setIconVisibleInMenu(True)
        self.actionClear.setObjectName("actionClear")
        self.aShowFilesToolbar = QtWidgets.QAction(MainWindow)
        self.aShowFilesToolbar.setCheckable(True)
        self.aShowFilesToolbar.setObjectName("aShowFilesToolbar")
        self.aShowCodeToolbar = QtWidgets.QAction(MainWindow)
        self.aShowCodeToolbar.setCheckable(True)
        self.aShowCodeToolbar.setObjectName("aShowCodeToolbar")
        self.aShowLogsWin = QtWidgets.QAction(MainWindow)
        self.aShowLogsWin.setCheckable(True)
        self.aShowLogsWin.setObjectName("aShowLogsWin")
        self.aShowNavWin = QtWidgets.QAction(MainWindow)
        self.aShowNavWin.setCheckable(True)
        self.aShowNavWin.setObjectName("aShowNavWin")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("preferences-system")
        self.actionPreferences.setIcon(icon)
        self.actionPreferences.setIconVisibleInMenu(True)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("help-contents")
        self.actionHelp.setIcon(icon)
        self.actionHelp.setIconVisibleInMenu(True)
        self.actionHelp.setObjectName("actionHelp")
        self.actionProgram = QtWidgets.QAction(MainWindow)
        self.actionProgram.setCheckable(True)
        self.actionProgram.setChecked(True)
        self.actionProgram.setObjectName("actionProgram")
        self.actionSubprogram = QtWidgets.QAction(MainWindow)
        self.actionSubprogram.setCheckable(True)
        self.actionSubprogram.setObjectName("actionSubprogram")
        self.actionDebug = QtWidgets.QAction(MainWindow)
        self.actionDebug.setObjectName("actionDebug")
        self.actionInfos = QtWidgets.QAction(MainWindow)
        self.actionInfos.setObjectName("actionInfos")
        self.actionWarnings = QtWidgets.QAction(MainWindow)
        self.actionWarnings.setObjectName("actionWarnings")
        self.actionErrors = QtWidgets.QAction(MainWindow)
        self.actionErrors.setObjectName("actionErrors")
        self.actionDebug_level = QtWidgets.QAction(MainWindow)
        self.actionDebug_level.setCheckable(True)
        self.actionDebug_level.setObjectName("actionDebug_level")
        self.actionShowAppLog = QtWidgets.QAction(MainWindow)
        self.actionShowAppLog.setCheckable(True)
        self.actionShowAppLog.setObjectName("actionShowAppLog")
        self.actionClearLog = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ide-icons/rc/edit-clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClearLog.setIcon(icon1)
        self.actionClearLog.setIconVisibleInMenu(True)
        self.actionClearLog.setObjectName("actionClearLog")
        self.actionMinimal = QtWidgets.QAction(MainWindow)
        self.actionMinimal.setObjectName("actionMinimal")
        self.actionClassicView = QtWidgets.QAction(MainWindow)
        self.actionClassicView.setObjectName("actionClassicView")
        self.actionMinimalView = QtWidgets.QAction(MainWindow)
        self.actionMinimalView.setObjectName("actionMinimalView")
        self.actionCompile = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("exec")
        self.actionCompile.setIcon(icon)
        self.actionCompile.setIconVisibleInMenu(True)
        self.actionCompile.setObjectName("actionCompile")
        self.toolBarFile.addAction(self.actionNew)
        self.toolBarFile.addAction(self.actionOpen)
        self.toolBarFile.addSeparator()
        self.toolBarFile.addAction(self.actionSave)
        self.toolBarFile.addAction(self.actionSaveAs)
        self.toolBarCode.addAction(self.actionRun)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.mnuActiveEditor.addSeparator()
        self.menuEdit.addAction(self.mnuActiveEditor.menuAction())
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionPreferences)
        self.menuPerspective.addAction(self.actionClassicView)
        self.menuPerspective.addAction(self.actionMinimalView)
        self.menuView.addAction(self.menuPerspective.menuAction())
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionFullscreen)
        self.menuProgramType.addAction(self.actionProgram)
        self.menuProgramType.addAction(self.actionSubprogram)
        self.menuCobol.addAction(self.menuProgramType.menuAction())
        self.menuCobol.addSeparator()
        self.menuCobol.addAction(self.actionCompile)
        self.menuCobol.addAction(self.actionRun)
        self.menu.addAction(self.actionHelp)
        self.menu.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuCobol.menuAction())
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidgetLogs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OpenCobolIDE"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/ide-icons/rc/silex-192x192.png\"/></p><p align=\"center\"><span style=\" font-size:20pt;\">Welcome to OpenCobolIDE</span><br/></p><p align=\"center\">Click on <span style=\" font-weight:600; font-style:italic;\">New </span>or <span style=\" font-weight:600; font-style:italic;\">Open </span>to get started!</p></body></html>"))
        self.btNewFile.setText(_translate("MainWindow", "New"))
        self.btOpenFile.setText(_translate("MainWindow", "Open"))
        self.labelRecents.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">Recent files</span></p></body></html>"))
        self.toolBarFile.setWindowTitle(_translate("MainWindow", "Toolbar File"))
        self.toolBarCode.setWindowTitle(_translate("MainWindow", "Toolbar Code"))
        self.dockWidgetLogs.setWindowTitle(_translate("MainWindow", "Logs"))
        self.tabWidgetLogs.setTabText(self.tabWidgetLogs.indexOf(self.tabCompiler), _translate("MainWindow", "Issues"))
        self.tabWidgetLogs.setTabToolTip(self.tabWidgetLogs.indexOf(self.tabCompiler), _translate("MainWindow", "Show compiler log"))
        self.tabWidgetLogs.setTabText(self.tabWidgetLogs.indexOf(self.tabProgramOutput), _translate("MainWindow", "Output"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.mnuActiveEditor.setTitle(_translate("MainWindow", "Active editor"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuPerspective.setTitle(_translate("MainWindow", "Perspective"))
        self.menuCobol.setTitle(_translate("MainWindow", "Cobol"))
        self.menuProgramType.setTitle(_translate("MainWindow", "Program type"))
        self.menu.setTitle(_translate("MainWindow", "?"))
        self.dockWidgetNavPanel.setWindowTitle(_translate("MainWindow", "Navigation"))
        self.dockWidgetOffsets.setWindowTitle(_translate("MainWindow", "Offset calculator"))
        self.tableWidgetOffsets.setSortingEnabled(True)
        item = self.tableWidgetOffsets.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Level"))
        item = self.tableWidgetOffsets.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidgetOffsets.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Offset"))
        item = self.tableWidgetOffsets.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "PIC"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setToolTip(_translate("MainWindow", "Exit application (Ctrl+Q)"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionRun.setText(_translate("MainWindow", "Run"))
        self.actionRun.setToolTip(_translate("MainWindow", "Run the current file (F5)"))
        self.actionRun.setShortcut(_translate("MainWindow", "F5"))
        self.actionAbout.setText(_translate("MainWindow", "About OpenCobolIDE"))
        self.actionAbout.setToolTip(_translate("MainWindow", "About OpenCobol IDE (F1)"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setToolTip(_translate("MainWindow", "Save current file (Ctrl+S)"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save as"))
        self.actionSaveAs.setToolTip(_translate("MainWindow", "Save current file as (Ctrl+Shift+S)"))
        self.actionSaveAs.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionFullscreen.setText(_translate("MainWindow", "Fullscreen"))
        self.actionFullscreen.setToolTip(_translate("MainWindow", "Toggle fullscreen (F12)"))
        self.actionFullscreen.setShortcut(_translate("MainWindow", "F11"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setToolTip(_translate("MainWindow", "New file (Ctrl+N)"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "Open a file (Ctrl+O)"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionClear.setText(_translate("MainWindow", "Clear list"))
        self.actionClear.setToolTip(_translate("MainWindow", "Clear list of recent files"))
        self.aShowFilesToolbar.setText(_translate("MainWindow", "Files"))
        self.aShowFilesToolbar.setToolTip(_translate("MainWindow", "Show/Hide the files toolbar"))
        self.aShowCodeToolbar.setText(_translate("MainWindow", "Code"))
        self.aShowCodeToolbar.setToolTip(_translate("MainWindow", "Show/Hide code toolbar"))
        self.aShowLogsWin.setText(_translate("MainWindow", "Logs"))
        self.aShowLogsWin.setToolTip(_translate("MainWindow", "Show/Hide logs window"))
        self.aShowLogsWin.setShortcut(_translate("MainWindow", "F9"))
        self.aShowNavWin.setText(_translate("MainWindow", "Navigation"))
        self.aShowNavWin.setToolTip(_translate("MainWindow", "Show/Hide navigation panel"))
        self.aShowNavWin.setShortcut(_translate("MainWindow", "F10"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionPreferences.setToolTip(_translate("MainWindow", "Edit the application settings"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHelp.setShortcut(_translate("MainWindow", "F1"))
        self.actionProgram.setText(_translate("MainWindow", "Executable"))
        self.actionSubprogram.setText(_translate("MainWindow", "Module"))
        self.actionDebug.setText(_translate("MainWindow", "Debug"))
        self.actionInfos.setText(_translate("MainWindow", "Infos"))
        self.actionWarnings.setText(_translate("MainWindow", "Warnings"))
        self.actionErrors.setText(_translate("MainWindow", "Errors"))
        self.actionDebug_level.setText(_translate("MainWindow", "Debug Log Level"))
        self.actionDebug_level.setToolTip(_translate("MainWindow", "Activate debug messages"))
        self.actionShowAppLog.setText(_translate("MainWindow", "Show window"))
        self.actionShowAppLog.setToolTip(_translate("MainWindow", "Show/hide application log window"))
        self.actionClearLog.setText(_translate("MainWindow", "Clear"))
        self.actionMinimal.setText(_translate("MainWindow", "Minimal"))
        self.actionClassicView.setText(_translate("MainWindow", "Classic"))
        self.actionMinimalView.setText(_translate("MainWindow", "Minimal"))
        self.actionCompile.setText(_translate("MainWindow", "Compile"))
        self.actionCompile.setToolTip(_translate("MainWindow", "Compile the current file (F8)"))
        self.actionCompile.setShortcut(_translate("MainWindow", "F8"))

from pyqode.cobol.widgets import PicOffsetsTable, OutlineTreeWidget
from pyqode.core.widgets import ErrorsTable, TabWidget, InteractiveConsole
from open_cobol_ide.view.widgets import RecentFilesListWidget
from . import ide_rc