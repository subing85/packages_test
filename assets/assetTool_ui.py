# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assetTool_ui.ui'
#
# Created: Sun Jun  3 13:56:09 2018
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow_asset(object):
    def setupUi(self, MainWindow_asset):
        MainWindow_asset.setObjectName(_fromUtf8("MainWindow_asset"))
        MainWindow_asset.resize(569, 433)
        self.centralwidget = QtGui.QWidget(MainWindow_asset)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setContentsMargins(10, 30, 10, 10)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_workStatus = QtGui.QLabel(self.groupBox)
        self.label_workStatus.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_workStatus.setObjectName(_fromUtf8("label_workStatus"))
        self.gridLayout.addWidget(self.label_workStatus, 6, 0, 1, 1)
        self.lineEdit_renderVersion = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_renderVersion.setObjectName(_fromUtf8("lineEdit_renderVersion"))
        self.gridLayout.addWidget(self.lineEdit_renderVersion, 4, 1, 1, 1)
        self.label_modelVersion = QtGui.QLabel(self.groupBox)
        self.label_modelVersion.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_modelVersion.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_modelVersion.setObjectName(_fromUtf8("label_modelVersion"))
        self.gridLayout.addWidget(self.label_modelVersion, 2, 0, 1, 1)
        self.label_renderVersion = QtGui.QLabel(self.groupBox)
        self.label_renderVersion.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_renderVersion.setObjectName(_fromUtf8("label_renderVersion"))
        self.gridLayout.addWidget(self.label_renderVersion, 4, 0, 1, 1)
        self.label_puppetVersion = QtGui.QLabel(self.groupBox)
        self.label_puppetVersion.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_puppetVersion.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_puppetVersion.setObjectName(_fromUtf8("label_puppetVersion"))
        self.gridLayout.addWidget(self.label_puppetVersion, 3, 0, 1, 1)
        self.label_assetType = QtGui.QLabel(self.groupBox)
        self.label_assetType.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_assetType.setObjectName(_fromUtf8("label_assetType"))
        self.gridLayout.addWidget(self.label_assetType, 1, 0, 1, 1)
        self.lineEdit_assetName = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_assetName.setObjectName(_fromUtf8("lineEdit_assetName"))
        self.gridLayout.addWidget(self.lineEdit_assetName, 0, 1, 1, 1)
        self.lineEdit_assetPath = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_assetPath.setObjectName(_fromUtf8("lineEdit_assetPath"))
        self.gridLayout.addWidget(self.lineEdit_assetPath, 5, 1, 1, 1)
        self.label_assetName = QtGui.QLabel(self.groupBox)
        self.label_assetName.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_assetName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_assetName.setObjectName(_fromUtf8("label_assetName"))
        self.gridLayout.addWidget(self.label_assetName, 0, 0, 1, 1)
        self.comboBox_assetType = QtGui.QComboBox(self.groupBox)
        self.comboBox_assetType.setObjectName(_fromUtf8("comboBox_assetType"))
        self.gridLayout.addWidget(self.comboBox_assetType, 1, 1, 1, 1)
        self.label_assetPath = QtGui.QLabel(self.groupBox)
        self.label_assetPath.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_assetPath.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_assetPath.setObjectName(_fromUtf8("label_assetPath"))
        self.gridLayout.addWidget(self.label_assetPath, 5, 0, 1, 1)
        self.lineEdit_modelVersion = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_modelVersion.setObjectName(_fromUtf8("lineEdit_modelVersion"))
        self.gridLayout.addWidget(self.lineEdit_modelVersion, 2, 1, 1, 1)
        self.lineEdit_puppetVersion = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_puppetVersion.setObjectName(_fromUtf8("lineEdit_puppetVersion"))
        self.gridLayout.addWidget(self.lineEdit_puppetVersion, 3, 1, 1, 1)
        self.comboBox_workStatus = QtGui.QComboBox(self.groupBox)
        self.comboBox_workStatus.setObjectName(_fromUtf8("comboBox_workStatus"))
        self.gridLayout.addWidget(self.comboBox_workStatus, 6, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.horizontalLayout_2.addWidget(self.treeWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.button_refresh = QtGui.QPushButton(self.centralwidget)
        self.button_refresh.setObjectName(_fromUtf8("button_refresh"))
        self.horizontalLayout.addWidget(self.button_refresh)
        self.button_create = QtGui.QPushButton(self.centralwidget)
        self.button_create.setObjectName(_fromUtf8("button_create"))
        self.horizontalLayout.addWidget(self.button_create)
        self.button_close = QtGui.QPushButton(self.centralwidget)
        self.button_close.setObjectName(_fromUtf8("button_close"))
        self.horizontalLayout.addWidget(self.button_close)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_cridits = QtGui.QVBoxLayout()
        self.verticalLayout_cridits.setObjectName(_fromUtf8("verticalLayout_cridits"))
        self.verticalLayout.addLayout(self.verticalLayout_cridits)
        MainWindow_asset.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_asset)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_asset)

    def retranslateUi(self, MainWindow_asset):
        MainWindow_asset.setWindowTitle(_translate("MainWindow_asset", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow_asset", "Studio Asset", None))
        self.label_workStatus.setText(_translate("MainWindow_asset", "Work Status", None))
        self.label_modelVersion.setText(_translate("MainWindow_asset", "Model Version", None))
        self.label_renderVersion.setText(_translate("MainWindow_asset", "Render Version", None))
        self.label_puppetVersion.setText(_translate("MainWindow_asset", "Puppet Version", None))
        self.label_assetType.setText(_translate("MainWindow_asset", "Asset Type", None))
        self.label_assetName.setText(_translate("MainWindow_asset", "Asset Name", None))
        self.label_assetPath.setText(_translate("MainWindow_asset", "Asset Path", None))
        self.button_refresh.setText(_translate("MainWindow_asset", "Refresh", None))
        self.button_create.setText(_translate("MainWindow_asset", "Create", None))
        self.button_close.setText(_translate("MainWindow_asset", "Close", None))

