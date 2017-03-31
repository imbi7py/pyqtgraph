# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqtgraph/graphicsItems/PlotItem/plotConfigTemplate.ui'
#
# Created: Fri Mar 31 10:35:34 2017
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(481, 840)
        self.averageGroup = QtGui.QGroupBox(Form)
        self.averageGroup.setGeometry(QtCore.QRect(0, 640, 242, 182))
        self.averageGroup.setCheckable(True)
        self.averageGroup.setChecked(False)
        self.averageGroup.setObjectName(_fromUtf8("averageGroup"))
        self.gridLayout_5 = QtGui.QGridLayout(self.averageGroup)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.avgParamList = QtGui.QListWidget(self.averageGroup)
        self.avgParamList.setObjectName(_fromUtf8("avgParamList"))
        self.gridLayout_5.addWidget(self.avgParamList, 0, 0, 1, 1)
        self.decimateGroup = QtGui.QFrame(Form)
        self.decimateGroup.setGeometry(QtCore.QRect(10, 140, 191, 171))
        self.decimateGroup.setObjectName(_fromUtf8("decimateGroup"))
        self.gridLayout_4 = QtGui.QGridLayout(self.decimateGroup)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.clipToViewCheck = QtGui.QCheckBox(self.decimateGroup)
        self.clipToViewCheck.setObjectName(_fromUtf8("clipToViewCheck"))
        self.gridLayout_4.addWidget(self.clipToViewCheck, 7, 0, 1, 3)
        self.maxTracesCheck = QtGui.QCheckBox(self.decimateGroup)
        self.maxTracesCheck.setObjectName(_fromUtf8("maxTracesCheck"))
        self.gridLayout_4.addWidget(self.maxTracesCheck, 8, 0, 1, 2)
        self.downsampleCheck = QtGui.QCheckBox(self.decimateGroup)
        self.downsampleCheck.setObjectName(_fromUtf8("downsampleCheck"))
        self.gridLayout_4.addWidget(self.downsampleCheck, 0, 0, 1, 3)
        self.peakRadio = QtGui.QRadioButton(self.decimateGroup)
        self.peakRadio.setChecked(True)
        self.peakRadio.setObjectName(_fromUtf8("peakRadio"))
        self.gridLayout_4.addWidget(self.peakRadio, 6, 1, 1, 2)
        self.maxTracesSpin = QtGui.QSpinBox(self.decimateGroup)
        self.maxTracesSpin.setObjectName(_fromUtf8("maxTracesSpin"))
        self.gridLayout_4.addWidget(self.maxTracesSpin, 8, 2, 1, 1)
        self.forgetTracesCheck = QtGui.QCheckBox(self.decimateGroup)
        self.forgetTracesCheck.setObjectName(_fromUtf8("forgetTracesCheck"))
        self.gridLayout_4.addWidget(self.forgetTracesCheck, 9, 0, 1, 3)
        self.meanRadio = QtGui.QRadioButton(self.decimateGroup)
        self.meanRadio.setObjectName(_fromUtf8("meanRadio"))
        self.gridLayout_4.addWidget(self.meanRadio, 3, 1, 1, 2)
        self.subsampleRadio = QtGui.QRadioButton(self.decimateGroup)
        self.subsampleRadio.setObjectName(_fromUtf8("subsampleRadio"))
        self.gridLayout_4.addWidget(self.subsampleRadio, 2, 1, 1, 2)
        self.autoDownsampleCheck = QtGui.QCheckBox(self.decimateGroup)
        self.autoDownsampleCheck.setChecked(True)
        self.autoDownsampleCheck.setObjectName(_fromUtf8("autoDownsampleCheck"))
        self.gridLayout_4.addWidget(self.autoDownsampleCheck, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 2, 0, 1, 1)
        self.downsampleSpin = QtGui.QSpinBox(self.decimateGroup)
        self.downsampleSpin.setMinimum(1)
        self.downsampleSpin.setMaximum(100000)
        self.downsampleSpin.setProperty("value", 1)
        self.downsampleSpin.setObjectName(_fromUtf8("downsampleSpin"))
        self.gridLayout_4.addWidget(self.downsampleSpin, 1, 1, 1, 1)
        self.transformGroup = QtGui.QFrame(Form)
        self.transformGroup.setGeometry(QtCore.QRect(10, 10, 171, 101))
        self.transformGroup.setObjectName(_fromUtf8("transformGroup"))
        self.gridLayout = QtGui.QGridLayout(self.transformGroup)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.logYCheck = QtGui.QCheckBox(self.transformGroup)
        self.logYCheck.setObjectName(_fromUtf8("logYCheck"))
        self.gridLayout.addWidget(self.logYCheck, 2, 0, 1, 1)
        self.logXCheck = QtGui.QCheckBox(self.transformGroup)
        self.logXCheck.setObjectName(_fromUtf8("logXCheck"))
        self.gridLayout.addWidget(self.logXCheck, 1, 0, 1, 1)
        self.fftCheck = QtGui.QCheckBox(self.transformGroup)
        self.fftCheck.setObjectName(_fromUtf8("fftCheck"))
        self.gridLayout.addWidget(self.fftCheck, 0, 0, 1, 1)
        self.derivativeCheck = QtGui.QCheckBox(self.transformGroup)
        self.derivativeCheck.setObjectName(_fromUtf8("derivativeCheck"))
        self.gridLayout.addWidget(self.derivativeCheck, 3, 0, 1, 1)
        self.phasemapCheck = QtGui.QCheckBox(self.transformGroup)
        self.phasemapCheck.setObjectName(_fromUtf8("phasemapCheck"))
        self.gridLayout.addWidget(self.phasemapCheck, 4, 0, 1, 1)
        self.pointsGroup = QtGui.QGroupBox(Form)
        self.pointsGroup.setGeometry(QtCore.QRect(10, 550, 234, 58))
        self.pointsGroup.setCheckable(True)
        self.pointsGroup.setObjectName(_fromUtf8("pointsGroup"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.pointsGroup)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.autoPointsCheck = QtGui.QCheckBox(self.pointsGroup)
        self.autoPointsCheck.setChecked(True)
        self.autoPointsCheck.setObjectName(_fromUtf8("autoPointsCheck"))
        self.verticalLayout_5.addWidget(self.autoPointsCheck)
        self.gridGroup = QtGui.QFrame(Form)
        self.gridGroup.setGeometry(QtCore.QRect(10, 460, 221, 81))
        self.gridGroup.setObjectName(_fromUtf8("gridGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.xGridCheck = QtGui.QCheckBox(self.gridGroup)
        self.xGridCheck.setObjectName(_fromUtf8("xGridCheck"))
        self.gridLayout_2.addWidget(self.xGridCheck, 0, 0, 1, 2)
        self.yGridCheck = QtGui.QCheckBox(self.gridGroup)
        self.yGridCheck.setObjectName(_fromUtf8("yGridCheck"))
        self.gridLayout_2.addWidget(self.yGridCheck, 1, 0, 1, 2)
        self.gridAlphaSlider = QtGui.QSlider(self.gridGroup)
        self.gridAlphaSlider.setMaximum(255)
        self.gridAlphaSlider.setProperty("value", 128)
        self.gridAlphaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.gridAlphaSlider.setObjectName(_fromUtf8("gridAlphaSlider"))
        self.gridLayout_2.addWidget(self.gridAlphaSlider, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridGroup)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.alphaGroup = QtGui.QGroupBox(Form)
        self.alphaGroup.setGeometry(QtCore.QRect(10, 390, 234, 60))
        self.alphaGroup.setCheckable(True)
        self.alphaGroup.setObjectName(_fromUtf8("alphaGroup"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.alphaGroup)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.autoAlphaCheck = QtGui.QCheckBox(self.alphaGroup)
        self.autoAlphaCheck.setChecked(False)
        self.autoAlphaCheck.setObjectName(_fromUtf8("autoAlphaCheck"))
        self.horizontalLayout.addWidget(self.autoAlphaCheck)
        self.alphaSlider = QtGui.QSlider(self.alphaGroup)
        self.alphaSlider.setMaximum(1000)
        self.alphaSlider.setProperty("value", 1000)
        self.alphaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.alphaSlider.setObjectName(_fromUtf8("alphaSlider"))
        self.horizontalLayout.addWidget(self.alphaSlider)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.averageGroup.setToolTip(_translate("Form", "Display averages of the curves displayed in this plot. The parameter list allows you to choose parameters to average over (if any are available).", None))
        self.averageGroup.setTitle(_translate("Form", "Average", None))
        self.clipToViewCheck.setToolTip(_translate("Form", "Plot only the portion of each curve that is visible. This assumes X values are uniformly spaced.", None))
        self.clipToViewCheck.setText(_translate("Form", "Clip to View", None))
        self.maxTracesCheck.setToolTip(_translate("Form", "If multiple curves are displayed in this plot, check this box to limit the number of traces that are displayed.", None))
        self.maxTracesCheck.setText(_translate("Form", "Max Traces:", None))
        self.downsampleCheck.setText(_translate("Form", "Downsample", None))
        self.peakRadio.setToolTip(_translate("Form", "Downsample by drawing a saw wave that follows the min and max of the original data. This method produces the best visual representation of the data but is slower.", None))
        self.peakRadio.setText(_translate("Form", "Peak", None))
        self.maxTracesSpin.setToolTip(_translate("Form", "If multiple curves are displayed in this plot, check \"Max Traces\" and set this value to limit the number of traces that are displayed.", None))
        self.forgetTracesCheck.setToolTip(_translate("Form", "If MaxTraces is checked, remove curves from memory after they are hidden (saves memory, but traces can not be un-hidden).", None))
        self.forgetTracesCheck.setText(_translate("Form", "Forget hidden traces", None))
        self.meanRadio.setToolTip(_translate("Form", "Downsample by taking the mean of N samples.", None))
        self.meanRadio.setText(_translate("Form", "Mean", None))
        self.subsampleRadio.setToolTip(_translate("Form", "Downsample by taking the first of N samples. This method is fastest and least accurate.", None))
        self.subsampleRadio.setText(_translate("Form", "Subsample", None))
        self.autoDownsampleCheck.setToolTip(_translate("Form", "Automatically downsample data based on the visible range. This assumes X values are uniformly spaced.", None))
        self.autoDownsampleCheck.setText(_translate("Form", "Auto", None))
        self.downsampleSpin.setToolTip(_translate("Form", "Downsample data before plotting. (plot every Nth sample)", None))
        self.downsampleSpin.setSuffix(_translate("Form", "x", None))
        self.logYCheck.setText(_translate("Form", "Log Y", None))
        self.logXCheck.setText(_translate("Form", "Log X", None))
        self.fftCheck.setText(_translate("Form", "Power Spectrum (FFT)", None))
        self.derivativeCheck.setText(_translate("Form", "dy/dx", None))
        self.phasemapCheck.setText(_translate("Form", "Y vs. Y\'", None))
        self.pointsGroup.setTitle(_translate("Form", "Points", None))
        self.autoPointsCheck.setText(_translate("Form", "Auto", None))
        self.xGridCheck.setText(_translate("Form", "Show X Grid", None))
        self.yGridCheck.setText(_translate("Form", "Show Y Grid", None))
        self.label.setText(_translate("Form", "Opacity", None))
        self.alphaGroup.setTitle(_translate("Form", "Alpha", None))
        self.autoAlphaCheck.setText(_translate("Form", "Auto", None))

