# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 450)
        self.vboxlayout = QtWidgets.QVBoxLayout(Dialog)
        self.vboxlayout.setContentsMargins(9, 9, 9, 9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self.dialog_splitter = QtWidgets.QSplitter(Dialog)
        self.dialog_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.dialog_splitter.setObjectName("dialog_splitter")
        self.pages_tree = QtWidgets.QTreeWidget(self.dialog_splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pages_tree.sizePolicy().hasHeightForWidth())
        self.pages_tree.setSizePolicy(sizePolicy)
        self.pages_tree.setObjectName("pages_tree")
        self.pages_stack = QtWidgets.QStackedWidget(self.dialog_splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pages_stack.sizePolicy().hasHeightForWidth())
        self.pages_stack.setSizePolicy(sizePolicy)
        self.pages_stack.setObjectName("pages_stack")
        self.vboxlayout.addWidget(self.dialog_splitter)
        self.profile_frame = QtWidgets.QFrame(Dialog)
        self.profile_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.profile_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profile_frame.setLineWidth(0)
        self.profile_frame.setObjectName("profile_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.profile_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.profile_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.save_to_profile = QtWidgets.QComboBox(self.profile_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_to_profile.sizePolicy().hasHeightForWidth())
        self.save_to_profile.setSizePolicy(sizePolicy)
        self.save_to_profile.setObjectName("save_to_profile")
        self.horizontalLayout_2.addWidget(self.save_to_profile)
        self.profiles_buttonbox = QtWidgets.QDialogButtonBox(self.profile_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profiles_buttonbox.sizePolicy().hasHeightForWidth())
        self.profiles_buttonbox.setSizePolicy(sizePolicy)
        self.profiles_buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.NoButton)
        self.profiles_buttonbox.setObjectName("profiles_buttonbox")
        self.horizontalLayout_2.addWidget(self.profiles_buttonbox)
        self.vboxlayout.addWidget(self.profile_frame)
        self.buttonbox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonbox.setMinimumSize(QtCore.QSize(0, 0))
        self.buttonbox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonbox.setObjectName("buttonbox")
        self.vboxlayout.addWidget(self.buttonbox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_("Options"))
        self.label.setText(_("Save settings to:"))
