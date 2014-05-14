# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Integration.ui'
#
# Created: Wed May 14 11:35:32 2014
#      by: PyQt4 UI code generator 4.10.4
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


class Ui_xrs_integration_widget(object):
    def setupUi(self, xrs_integration_widget):
        xrs_integration_widget.setObjectName(_fromUtf8("xrs_integration_widget"))
        xrs_integration_widget.resize(1120, 587)
        self.horizontalLayout_17 = QtGui.QHBoxLayout(xrs_integration_widget)
        self.horizontalLayout_17.setMargin(5)
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.horizontal_splitter = QtGui.QSplitter(xrs_integration_widget)
        self.horizontal_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.horizontal_splitter.setObjectName(_fromUtf8("horizontal_splitter"))
        self.layoutWidget = QtGui.QWidget(self.horizontal_splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_9.setSpacing(3)
        self.verticalLayout_9.setMargin(0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.img_pg_layout = GraphicsLayoutWidget(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_pg_layout.sizePolicy().hasHeightForWidth())
        self.img_pg_layout.setSizePolicy(sizePolicy)
        self.img_pg_layout.setMinimumSize(QtCore.QSize(200, 0))
        self.img_pg_layout.setBaseSize(QtCore.QSize(300, 0))
        self.img_pg_layout.setFrameShape(QtGui.QFrame.StyledPanel)
        self.img_pg_layout.setObjectName(_fromUtf8("img_pg_layout"))
        self.verticalLayout_9.addWidget(self.img_pg_layout)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.x_lbl = QtGui.QLabel(self.layoutWidget)
        self.x_lbl.setMinimumSize(QtCore.QSize(50, 0))
        self.x_lbl.setObjectName(_fromUtf8("x_lbl"))
        self.horizontalLayout_13.addWidget(self.x_lbl)
        self.y_lbl = QtGui.QLabel(self.layoutWidget)
        self.y_lbl.setMinimumSize(QtCore.QSize(50, 0))
        self.y_lbl.setObjectName(_fromUtf8("y_lbl"))
        self.horizontalLayout_13.addWidget(self.y_lbl)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.int_lbl = QtGui.QLabel(self.layoutWidget)
        self.int_lbl.setObjectName(_fromUtf8("int_lbl"))
        self.verticalLayout_4.addWidget(self.int_lbl)
        self.horizontalLayout_16.addLayout(self.verticalLayout_4)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(1)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.two_theta_lbl = QtGui.QLabel(self.layoutWidget)
        self.two_theta_lbl.setMinimumSize(QtCore.QSize(50, 0))
        self.two_theta_lbl.setObjectName(_fromUtf8("two_theta_lbl"))
        self.horizontalLayout_12.addWidget(self.two_theta_lbl)
        self.d_lbl = QtGui.QLabel(self.layoutWidget)
        self.d_lbl.setMinimumSize(QtCore.QSize(50, 0))
        self.d_lbl.setObjectName(_fromUtf8("d_lbl"))
        self.horizontalLayout_12.addWidget(self.d_lbl)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.q_lbl = QtGui.QLabel(self.layoutWidget)
        self.q_lbl.setObjectName(_fromUtf8("q_lbl"))
        self.verticalLayout_3.addWidget(self.q_lbl)
        self.horizontalLayout_16.addLayout(self.verticalLayout_3)
        self.verticalLayout_9.addLayout(self.horizontalLayout_16)
        self.vertical_splitter = QtGui.QSplitter(self.horizontal_splitter)
        self.vertical_splitter.setOrientation(QtCore.Qt.Vertical)
        self.vertical_splitter.setObjectName(_fromUtf8("vertical_splitter"))
        self.tabWidget = QtGui.QTabWidget(self.vertical_splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.image_tab = QtGui.QWidget()
        self.image_tab.setObjectName(_fromUtf8("image_tab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.image_tab)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.load_img_btn = QtGui.QPushButton(self.image_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_img_btn.sizePolicy().hasHeightForWidth())
        self.load_img_btn.setSizePolicy(sizePolicy)
        self.load_img_btn.setMinimumSize(QtCore.QSize(179, 0))
        self.load_img_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.load_img_btn.setObjectName(_fromUtf8("load_img_btn"))
        self.horizontalLayout_2.addWidget(self.load_img_btn)
        self.prev_img_btn = QtGui.QPushButton(self.image_tab)
        self.prev_img_btn.setMinimumSize(QtCore.QSize(50, 0))
        self.prev_img_btn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.prev_img_btn.setObjectName(_fromUtf8("prev_img_btn"))
        self.horizontalLayout_2.addWidget(self.prev_img_btn)
        self.next_img_btn = QtGui.QPushButton(self.image_tab)
        self.next_img_btn.setMinimumSize(QtCore.QSize(50, 0))
        self.next_img_btn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.next_img_btn.setObjectName(_fromUtf8("next_img_btn"))
        self.horizontalLayout_2.addWidget(self.next_img_btn)
        self.auto_img_btn = QtGui.QPushButton(self.image_tab)
        self.auto_img_btn.setObjectName(_fromUtf8("auto_img_btn"))
        self.horizontalLayout_2.addWidget(self.auto_img_btn)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.image_tab)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_4.setMargin(5)
        self.gridLayout_4.setHorizontalSpacing(5)
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.img_browse_by_name_rb = QtGui.QRadioButton(self.groupBox)
        self.img_browse_by_name_rb.setChecked(True)
        self.img_browse_by_name_rb.setObjectName(_fromUtf8("img_browse_by_name_rb"))
        self.gridLayout_4.addWidget(self.img_browse_by_name_rb, 0, 0, 1, 1)
        self.img_browse_by_time_rb = QtGui.QRadioButton(self.groupBox)
        self.img_browse_by_time_rb.setObjectName(_fromUtf8("img_browse_by_time_rb"))
        self.gridLayout_4.addWidget(self.img_browse_by_time_rb, 0, 1, 1, 1)
        self.autoproces_cb = QtGui.QCheckBox(self.groupBox)
        self.autoproces_cb.setObjectName(_fromUtf8("autoproces_cb"))
        self.gridLayout_4.addWidget(self.autoproces_cb, 1, 0, 1, 2)
        self.gridLayout_3.addWidget(self.groupBox, 0, 1, 2, 1)
        self.img_filename_lbl = QtGui.QLabel(self.image_tab)
        self.img_filename_lbl.setObjectName(_fromUtf8("img_filename_lbl"))
        self.gridLayout_3.addWidget(self.img_filename_lbl, 1, 0, 1, 1)
        self.groupBox1 = QtGui.QGroupBox(self.image_tab)
        self.groupBox1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox1.setObjectName(_fromUtf8("groupBox1"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.groupBox1)
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setMargin(5)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.mask_use_cb = QtGui.QCheckBox(self.groupBox1)
        self.mask_use_cb.setChecked(True)
        self.mask_use_cb.setObjectName(_fromUtf8("mask_use_cb"))
        self.horizontalLayout_14.addWidget(self.mask_use_cb)
        self.mask_transparent_cb = QtGui.QCheckBox(self.groupBox1)
        self.mask_transparent_cb.setObjectName(_fromUtf8("mask_transparent_cb"))
        self.horizontalLayout_14.addWidget(self.mask_transparent_cb)
        self.gridLayout_3.addWidget(self.groupBox1, 2, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.image_tab)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setMargin(5)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.img_levels_absolute_rb = QtGui.QRadioButton(self.groupBox_2)
        self.img_levels_absolute_rb.setChecked(True)
        self.img_levels_absolute_rb.setObjectName(_fromUtf8("img_levels_absolute_rb"))
        self.horizontalLayout_15.addWidget(self.img_levels_absolute_rb)
        self.img_levels_percentage_rb = QtGui.QRadioButton(self.groupBox_2)
        self.img_levels_percentage_rb.setObjectName(_fromUtf8("img_levels_percentage_rb"))
        self.horizontalLayout_15.addWidget(self.img_levels_percentage_rb)
        self.gridLayout_3.addWidget(self.groupBox_2, 2, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.groupBox_3 = QtGui.QGroupBox(self.image_tab)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setMargin(5)
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.image_rb = QtGui.QRadioButton(self.groupBox_3)
        self.image_rb.setChecked(True)
        self.image_rb.setObjectName(_fromUtf8("image_rb"))
        self.horizontalLayout_18.addWidget(self.image_rb)
        self.cake_rb = QtGui.QRadioButton(self.groupBox_3)
        self.cake_rb.setObjectName(_fromUtf8("cake_rb"))
        self.horizontalLayout_18.addWidget(self.cake_rb)
        self.horizontalLayout_19.addWidget(self.groupBox_3)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem2)
        self.label_10 = QtGui.QLabel(self.image_tab)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_19.addWidget(self.label_10)
        self.calibration_lbl = QtGui.QLabel(self.image_tab)
        self.calibration_lbl.setObjectName(_fromUtf8("calibration_lbl"))
        self.horizontalLayout_19.addWidget(self.calibration_lbl)
        self.verticalLayout.addLayout(self.horizontalLayout_19)
        spacerItem3 = QtGui.QSpacerItem(20, 55, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.tabWidget.addTab(self.image_tab, _fromUtf8(""))
        self.spectra_tab = QtGui.QWidget()
        self.spectra_tab.setObjectName(_fromUtf8("spectra_tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.spectra_tab)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.spec_load_btn = QtGui.QPushButton(self.spectra_tab)
        self.spec_load_btn.setMinimumSize(QtCore.QSize(75, 0))
        self.spec_load_btn.setMaximumSize(QtCore.QSize(75, 16777215))
        self.spec_load_btn.setObjectName(_fromUtf8("spec_load_btn"))
        self.horizontalLayout_4.addWidget(self.spec_load_btn)
        self.spec_previous_btn = QtGui.QPushButton(self.spectra_tab)
        self.spec_previous_btn.setMinimumSize(QtCore.QSize(10, 0))
        self.spec_previous_btn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spec_previous_btn.setObjectName(_fromUtf8("spec_previous_btn"))
        self.horizontalLayout_4.addWidget(self.spec_previous_btn)
        self.spec_next_btn = QtGui.QPushButton(self.spectra_tab)
        self.spec_next_btn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spec_next_btn.setObjectName(_fromUtf8("spec_next_btn"))
        self.horizontalLayout_4.addWidget(self.spec_next_btn)
        self.spec_filename_lbl = QtGui.QLabel(self.spectra_tab)
        self.spec_filename_lbl.setObjectName(_fromUtf8("spec_filename_lbl"))
        self.horizontalLayout_4.addWidget(self.spec_filename_lbl)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.filename_lbl_2 = QtGui.QLabel(self.spectra_tab)
        self.filename_lbl_2.setObjectName(_fromUtf8("filename_lbl_2"))
        self.horizontalLayout.addWidget(self.filename_lbl_2)
        self.spec_directory_txt = QtGui.QLineEdit(self.spectra_tab)
        self.spec_directory_txt.setObjectName(_fromUtf8("spec_directory_txt"))
        self.horizontalLayout.addWidget(self.spec_directory_txt)
        self.spec_directory_btn = QtGui.QPushButton(self.spectra_tab)
        self.spec_directory_btn.setObjectName(_fromUtf8("spec_directory_btn"))
        self.horizontalLayout.addWidget(self.spec_directory_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.spec_autocreate_cb = QtGui.QCheckBox(self.spectra_tab)
        self.spec_autocreate_cb.setChecked(True)
        self.spec_autocreate_cb.setObjectName(_fromUtf8("spec_autocreate_cb"))
        self.horizontalLayout_11.addWidget(self.spec_autocreate_cb)
        spacerItem4 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.label_7 = QtGui.QLabel(self.spectra_tab)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_11.addWidget(self.label_7)
        self.spec_browse_by_name_rb = QtGui.QRadioButton(self.spectra_tab)
        self.spec_browse_by_name_rb.setChecked(True)
        self.spec_browse_by_name_rb.setObjectName(_fromUtf8("spec_browse_by_name_rb"))
        self.horizontalLayout_11.addWidget(self.spec_browse_by_name_rb)
        self.spec_browse_by_time_rb = QtGui.QRadioButton(self.spectra_tab)
        self.spec_browse_by_time_rb.setObjectName(_fromUtf8("spec_browse_by_time_rb"))
        self.horizontalLayout_11.addWidget(self.spec_browse_by_time_rb)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.widget = QtGui.QWidget(self.spectra_tab)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_10.setMargin(0)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setMinimumSize(QtCore.QSize(35, 0))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_10.addWidget(self.label_8)
        self.spec_unit_tth_rb = QtGui.QRadioButton(self.widget)
        self.spec_unit_tth_rb.setChecked(True)
        self.spec_unit_tth_rb.setObjectName(_fromUtf8("spec_unit_tth_rb"))
        self.horizontalLayout_10.addWidget(self.spec_unit_tth_rb)
        self.spec_unit_q_rb = QtGui.QRadioButton(self.widget)
        self.spec_unit_q_rb.setText(_fromUtf8(""))
        self.spec_unit_q_rb.setObjectName(_fromUtf8("spec_unit_q_rb"))
        self.horizontalLayout_10.addWidget(self.spec_unit_q_rb)
        self.label_9 = QtGui.QLabel(self.widget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_10.addWidget(self.label_9)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.verticalLayout_2.addWidget(self.widget)
        spacerItem6 = QtGui.QSpacerItem(20, 136, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.tabWidget.addTab(self.spectra_tab, _fromUtf8(""))
        self.overlay_tab = QtGui.QWidget()
        self.overlay_tab.setObjectName(_fromUtf8("overlay_tab"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.overlay_tab)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setMargin(5)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.overlay_add_btn = QtGui.QPushButton(self.overlay_tab)
        self.overlay_add_btn.setObjectName(_fromUtf8("overlay_add_btn"))
        self.horizontalLayout_3.addWidget(self.overlay_add_btn)
        self.overlay_del_btn = QtGui.QPushButton(self.overlay_tab)
        self.overlay_del_btn.setObjectName(_fromUtf8("overlay_del_btn"))
        self.horizontalLayout_3.addWidget(self.overlay_del_btn)
        self.overlay_clear_btn = QtGui.QPushButton(self.overlay_tab)
        self.overlay_clear_btn.setObjectName(_fromUtf8("overlay_clear_btn"))
        self.horizontalLayout_3.addWidget(self.overlay_clear_btn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.overlay_lw = QtGui.QListWidget(self.overlay_tab)
        self.overlay_lw.setObjectName(_fromUtf8("overlay_lw"))
        self.horizontalLayout_6.addWidget(self.overlay_lw)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.overlay_tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.overlay_scale_sb = QtGui.QDoubleSpinBox(self.overlay_tab)
        self.overlay_scale_sb.setMinimumSize(QtCore.QSize(90, 0))
        self.overlay_scale_sb.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.overlay_scale_sb.setDecimals(4)
        self.overlay_scale_sb.setMaximum(999999.0)
        self.overlay_scale_sb.setSingleStep(0.01)
        self.overlay_scale_sb.setObjectName(_fromUtf8("overlay_scale_sb"))
        self.gridLayout.addWidget(self.overlay_scale_sb, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.overlay_tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.overlay_offset_sb = QtGui.QDoubleSpinBox(self.overlay_tab)
        self.overlay_offset_sb.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.overlay_offset_sb.setDecimals(3)
        self.overlay_offset_sb.setMinimum(-999999999.0)
        self.overlay_offset_sb.setMaximum(999999999.0)
        self.overlay_offset_sb.setSingleStep(100.0)
        self.overlay_offset_sb.setProperty("value", 0.0)
        self.overlay_offset_sb.setObjectName(_fromUtf8("overlay_offset_sb"))
        self.gridLayout.addWidget(self.overlay_offset_sb, 2, 1, 1, 1)
        self.overlay_show_cb = QtGui.QCheckBox(self.overlay_tab)
        self.overlay_show_cb.setChecked(True)
        self.overlay_show_cb.setObjectName(_fromUtf8("overlay_show_cb"))
        self.gridLayout.addWidget(self.overlay_show_cb, 3, 0, 1, 3)
        self.overlay_scale_step_txt = QtGui.QLineEdit(self.overlay_tab)
        self.overlay_scale_step_txt.setMaximumSize(QtCore.QSize(80, 16777215))
        self.overlay_scale_step_txt.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.overlay_scale_step_txt.setObjectName(_fromUtf8("overlay_scale_step_txt"))
        self.gridLayout.addWidget(self.overlay_scale_step_txt, 1, 2, 1, 1)
        self.overlay_offset_step_txt = QtGui.QLineEdit(self.overlay_tab)
        self.overlay_offset_step_txt.setMaximumSize(QtCore.QSize(80, 16777215))
        self.overlay_offset_step_txt.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.overlay_offset_step_txt.setObjectName(_fromUtf8("overlay_offset_step_txt"))
        self.gridLayout.addWidget(self.overlay_offset_step_txt, 2, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.overlay_tab)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem7)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.overlay_save_set_btn = QtGui.QPushButton(self.overlay_tab)
        self.overlay_save_set_btn.setObjectName(_fromUtf8("overlay_save_set_btn"))
        self.horizontalLayout_5.addWidget(self.overlay_save_set_btn)
        self.overlay_load_set_btn = QtGui.QPushButton(self.overlay_tab)
        self.overlay_load_set_btn.setObjectName(_fromUtf8("overlay_load_set_btn"))
        self.horizontalLayout_5.addWidget(self.overlay_load_set_btn)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.overlay_set_as_bkg_btn = QtGui.QPushButton(self.overlay_tab)
        self.overlay_set_as_bkg_btn.setCheckable(True)
        self.overlay_set_as_bkg_btn.setObjectName(_fromUtf8("overlay_set_as_bkg_btn"))
        self.horizontalLayout_5.addWidget(self.overlay_set_as_bkg_btn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.overlay_tab, _fromUtf8(""))
        self.phase_tab = QtGui.QWidget()
        self.phase_tab.setObjectName(_fromUtf8("phase_tab"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.phase_tab)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setMargin(5)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.phase_add_btn = QtGui.QPushButton(self.phase_tab)
        self.phase_add_btn.setObjectName(_fromUtf8("phase_add_btn"))
        self.horizontalLayout_7.addWidget(self.phase_add_btn)
        self.phase_edit_btn = QtGui.QPushButton(self.phase_tab)
        self.phase_edit_btn.setObjectName(_fromUtf8("phase_edit_btn"))
        self.horizontalLayout_7.addWidget(self.phase_edit_btn)
        self.phase_delete_btn = QtGui.QPushButton(self.phase_tab)
        self.phase_delete_btn.setObjectName(_fromUtf8("phase_delete_btn"))
        self.horizontalLayout_7.addWidget(self.phase_delete_btn)
        self.phase_clear_btn = QtGui.QPushButton(self.phase_tab)
        self.phase_clear_btn.setObjectName(_fromUtf8("phase_clear_btn"))
        self.horizontalLayout_7.addWidget(self.phase_clear_btn)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.phase_lw = QtGui.QListWidget(self.phase_tab)
        self.phase_lw.setObjectName(_fromUtf8("phase_lw"))
        self.horizontalLayout_9.addWidget(self.phase_lw)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_6 = QtGui.QLabel(self.phase_tab)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.phase_tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.phase_pressure_sb = QtGui.QDoubleSpinBox(self.phase_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phase_pressure_sb.sizePolicy().hasHeightForWidth())
        self.phase_pressure_sb.setSizePolicy(sizePolicy)
        self.phase_pressure_sb.setMinimumSize(QtCore.QSize(110, 0))
        self.phase_pressure_sb.setSizeIncrement(QtCore.QSize(2, 0))
        self.phase_pressure_sb.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.phase_pressure_sb.setMinimum(-999999999.0)
        self.phase_pressure_sb.setMaximum(999999999.0)
        self.phase_pressure_sb.setSingleStep(0.5)
        self.phase_pressure_sb.setObjectName(_fromUtf8("phase_pressure_sb"))
        self.gridLayout_2.addWidget(self.phase_pressure_sb, 1, 1, 1, 1)
        self.phase_pressure_step_txt = QtGui.QLineEdit(self.phase_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phase_pressure_step_txt.sizePolicy().hasHeightForWidth())
        self.phase_pressure_step_txt.setSizePolicy(sizePolicy)
        self.phase_pressure_step_txt.setMaximumSize(QtCore.QSize(80, 16777215))
        self.phase_pressure_step_txt.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.phase_pressure_step_txt.setObjectName(_fromUtf8("phase_pressure_step_txt"))
        self.gridLayout_2.addWidget(self.phase_pressure_step_txt, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.phase_tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.phase_temperature_sb = QtGui.QDoubleSpinBox(self.phase_tab)
        self.phase_temperature_sb.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.phase_temperature_sb.setMaximum(999999999.0)
        self.phase_temperature_sb.setSingleStep(100.0)
        self.phase_temperature_sb.setObjectName(_fromUtf8("phase_temperature_sb"))
        self.gridLayout_2.addWidget(self.phase_temperature_sb, 2, 1, 1, 1)
        self.phase_temperature_step_txt = QtGui.QLineEdit(self.phase_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phase_temperature_step_txt.sizePolicy().hasHeightForWidth())
        self.phase_temperature_step_txt.setSizePolicy(sizePolicy)
        self.phase_temperature_step_txt.setMaximumSize(QtCore.QSize(80, 16777215))
        self.phase_temperature_step_txt.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.phase_temperature_step_txt.setObjectName(_fromUtf8("phase_temperature_step_txt"))
        self.gridLayout_2.addWidget(self.phase_temperature_step_txt, 2, 2, 1, 1)
        self.phase_apply_to_all_cb = QtGui.QCheckBox(self.phase_tab)
        self.phase_apply_to_all_cb.setChecked(True)
        self.phase_apply_to_all_cb.setObjectName(_fromUtf8("phase_apply_to_all_cb"))
        self.gridLayout_2.addWidget(self.phase_apply_to_all_cb, 3, 0, 1, 3)
        self.verticalLayout_7.addLayout(self.gridLayout_2)
        spacerItem9 = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem9)
        self.horizontalLayout_9.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.phase_save_set_btn = QtGui.QPushButton(self.phase_tab)
        self.phase_save_set_btn.setObjectName(_fromUtf8("phase_save_set_btn"))
        self.horizontalLayout_8.addWidget(self.phase_save_set_btn)
        self.phase_load_set_btn = QtGui.QPushButton(self.phase_tab)
        self.phase_load_set_btn.setObjectName(_fromUtf8("phase_load_set_btn"))
        self.horizontalLayout_8.addWidget(self.phase_load_set_btn)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem10)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.tabWidget.addTab(self.phase_tab, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.special_tab = QtGui.QWidget()
        self.special_tab.setObjectName(_fromUtf8("special_tab"))
        self.tabWidget.addTab(self.special_tab, _fromUtf8(""))
        self.spectrum_pg_layout = GraphicsLayoutWidget(self.vertical_splitter)
        self.spectrum_pg_layout.setSizeIncrement(QtCore.QSize(1, 2))
        self.spectrum_pg_layout.setBaseSize(QtCore.QSize(300, 300))
        self.spectrum_pg_layout.setFrameShape(QtGui.QFrame.StyledPanel)
        self.spectrum_pg_layout.setFrameShadow(QtGui.QFrame.Sunken)
        self.spectrum_pg_layout.setObjectName(_fromUtf8("spectrum_pg_layout"))
        self.horizontalLayout_17.addWidget(self.horizontal_splitter)

        self.retranslateUi(xrs_integration_widget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(xrs_integration_widget)

    def retranslateUi(self, xrs_integration_widget):
        xrs_integration_widget.setWindowTitle(_translate("xrs_integration_widget", "Form", None))
        self.x_lbl.setText(_translate("xrs_integration_widget", "X:", None))
        self.y_lbl.setText(_translate("xrs_integration_widget", "Y:", None))
        self.int_lbl.setText(_translate("xrs_integration_widget", "I:", None))
        self.two_theta_lbl.setText(_translate("xrs_integration_widget", "2Th:      ", None))
        self.d_lbl.setText(_translate("xrs_integration_widget", "d:     ", None))
        self.q_lbl.setText(_translate("xrs_integration_widget", "Q:", None))
        self.load_img_btn.setText(_translate("xrs_integration_widget", "Load", None))
        self.prev_img_btn.setText(_translate("xrs_integration_widget", "<", None))
        self.next_img_btn.setText(_translate("xrs_integration_widget", ">", None))
        self.auto_img_btn.setText(_translate("xrs_integration_widget", ">>", None))
        self.groupBox.setTitle(_translate("xrs_integration_widget", "Browse", None))
        self.img_browse_by_name_rb.setText(_translate("xrs_integration_widget", "By Name", None))
        self.img_browse_by_time_rb.setText(_translate("xrs_integration_widget", "By Time", None))
        self.autoproces_cb.setText(_translate("xrs_integration_widget", "autoprocess", None))
        self.img_filename_lbl.setText(_translate("xrs_integration_widget", "filename", None))
        self.groupBox1.setTitle(_translate("xrs_integration_widget", "Mask", None))
        self.mask_use_cb.setText(_translate("xrs_integration_widget", "Use", None))
        self.mask_transparent_cb.setText(_translate("xrs_integration_widget", "Transparent", None))
        self.groupBox_2.setTitle(_translate("xrs_integration_widget", "Levels", None))
        self.img_levels_absolute_rb.setText(_translate("xrs_integration_widget", "Absolute", None))
        self.img_levels_percentage_rb.setText(_translate("xrs_integration_widget", "Percentage", None))
        self.groupBox_3.setTitle(_translate("xrs_integration_widget", "Show", None))
        self.image_rb.setText(_translate("xrs_integration_widget", "Image", None))
        self.cake_rb.setText(_translate("xrs_integration_widget", "Cake", None))
        self.label_10.setText(_translate("xrs_integration_widget", "Calibration:", None))
        self.calibration_lbl.setText(_translate("xrs_integration_widget", "None", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.image_tab),
                                  _translate("xrs_integration_widget", "Img", None))
        self.spec_load_btn.setText(_translate("xrs_integration_widget", "Load", None))
        self.spec_previous_btn.setText(_translate("xrs_integration_widget", "<", None))
        self.spec_next_btn.setText(_translate("xrs_integration_widget", ">", None))
        self.spec_filename_lbl.setText(_translate("xrs_integration_widget", "filename", None))
        self.filename_lbl_2.setText(_translate("xrs_integration_widget", "Directory:", None))
        self.spec_directory_btn.setText(_translate("xrs_integration_widget", "...", None))
        self.spec_autocreate_cb.setText(_translate("xrs_integration_widget", "autocreate", None))
        self.label_7.setText(_translate("xrs_integration_widget", "Browse", None))
        self.spec_browse_by_name_rb.setText(_translate("xrs_integration_widget", "By Name", None))
        self.spec_browse_by_time_rb.setText(_translate("xrs_integration_widget", "By Time", None))
        self.label_8.setText(_translate("xrs_integration_widget", "Unit:", None))
        self.spec_unit_tth_rb.setText(_translate("xrs_integration_widget", " 2 Theta", None))
        self.label_9.setText(_translate("xrs_integration_widget",
                                        "<html><head/><body><p>Q (A<span style=\" vertical-align:super;\">-1</span>)</p></body></html>",
                                        None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.spectra_tab),
                                  _translate("xrs_integration_widget", "Spec", None))
        self.overlay_add_btn.setText(_translate("xrs_integration_widget", "Add", None))
        self.overlay_del_btn.setText(_translate("xrs_integration_widget", "Delete", None))
        self.overlay_clear_btn.setText(_translate("xrs_integration_widget", "Clear ", None))
        self.label_3.setText(_translate("xrs_integration_widget", "Scale:", None))
        self.label_4.setText(_translate("xrs_integration_widget", "Offset:", None))
        self.overlay_show_cb.setText(_translate("xrs_integration_widget", "Show", None))
        self.overlay_scale_step_txt.setText(_translate("xrs_integration_widget", "0.01", None))
        self.overlay_offset_step_txt.setText(_translate("xrs_integration_widget", "100", None))
        self.label_5.setText(_translate("xrs_integration_widget", "Step", None))
        self.overlay_save_set_btn.setText(_translate("xrs_integration_widget", "Save Set", None))
        self.overlay_load_set_btn.setText(_translate("xrs_integration_widget", "Load Set", None))
        self.overlay_set_as_bkg_btn.setText(_translate("xrs_integration_widget", "Set as Background", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.overlay_tab),
                                  _translate("xrs_integration_widget", "Overlay", None))
        self.phase_add_btn.setText(_translate("xrs_integration_widget", "Add", None))
        self.phase_edit_btn.setText(_translate("xrs_integration_widget", "Edit", None))
        self.phase_delete_btn.setText(_translate("xrs_integration_widget", "Delete", None))
        self.phase_clear_btn.setText(_translate("xrs_integration_widget", "Clear", None))
        self.label_6.setText(_translate("xrs_integration_widget", "Step", None))
        self.label.setText(_translate("xrs_integration_widget", "P:", None))
        self.phase_pressure_step_txt.setText(_translate("xrs_integration_widget", "0.5", None))
        self.label_2.setText(_translate("xrs_integration_widget", "T:", None))
        self.phase_temperature_step_txt.setText(_translate("xrs_integration_widget", "100", None))
        self.phase_apply_to_all_cb.setText(_translate("xrs_integration_widget", "Apply to all phases", None))
        self.phase_save_set_btn.setText(_translate("xrs_integration_widget", "Save Set", None))
        self.phase_load_set_btn.setText(_translate("xrs_integration_widget", "Load Set", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.phase_tab),
                                  _translate("xrs_integration_widget", "Phase", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("xrs_integration_widget", "Bkg", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.special_tab),
                                  _translate("xrs_integration_widget", "X", None))


from pyqtgraph import GraphicsLayoutWidget
