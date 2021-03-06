# -*- coding: utf8 -*-
# Dioptas - GUI program for fast processing of 2D X-ray data
# Copyright (C) 2017  Clemens Prescher (clemens.prescher@gmail.com)
# Institute for Geology and Mineralogy, University of Cologne
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from qtpy import QtWidgets

from ...CustomWidgets import NumberTextField, LabelAlignRight, SpinBoxAlignRight, FlatButton, \
    CheckableFlatButton, DoubleSpinBoxAlignRight, VerticalSpacerItem, HorizontalSpacerItem, \
    DoubleMultiplySpinBoxAlignRight


class BackgroundWidget(QtWidgets.QWidget):
    def __init__(self):
        super(BackgroundWidget, self).__init__()

        self._layout = QtWidgets.QVBoxLayout()

        self.image_background_gb = QtWidgets.QGroupBox('Image Background', self)
        self._image_background_gb_layout = QtWidgets.QGridLayout(self.image_background_gb)
        self._image_background_gb_layout.setSpacing(6)

        self.load_image_btn = FlatButton('Load')
        self.filename_lbl = QtWidgets.QLabel('None')
        self.remove_image_btn = FlatButton('Remove')
        self.scale_sb = DoubleSpinBoxAlignRight()
        self.offset_sb = DoubleSpinBoxAlignRight()

        self.scale_step_msb = DoubleMultiplySpinBoxAlignRight()
        self.offset_step_msb = DoubleMultiplySpinBoxAlignRight()

        self._image_background_gb_layout.addWidget(self.load_image_btn, 0, 0)
        self._image_background_gb_layout.addWidget(self.remove_image_btn, 1, 0)
        self._image_background_gb_layout.addWidget(self.filename_lbl, 0, 1, 1, 8)
        self._image_background_gb_layout.addWidget(LabelAlignRight('Scale:'), 1, 1)
        self._image_background_gb_layout.addWidget(self.scale_sb, 1, 2)
        self._image_background_gb_layout.addWidget(self.scale_step_msb, 1, 3)
        self._image_background_gb_layout.addItem(HorizontalSpacerItem(), 1, 4)
        self._image_background_gb_layout.addWidget(LabelAlignRight('Offset:'), 1, 5)
        self._image_background_gb_layout.addWidget(self.offset_sb, 1, 6)
        self._image_background_gb_layout.addWidget(self.offset_step_msb, 1, 7)
        self._image_background_gb_layout.addItem(HorizontalSpacerItem(), 1, 8)

        self.image_background_gb.setLayout(self._image_background_gb_layout)

        self._layout.addWidget(self.image_background_gb)

        self.setLayout(self._layout)

        self.pattern_background_gb = QtWidgets.QGroupBox('Pattern Background')
        self._pattern_background_gb = QtWidgets.QGridLayout()

        self.smooth_with_sb = DoubleSpinBoxAlignRight()
        self.iterations_sb = SpinBoxAlignRight()
        self.poly_order_sb = SpinBoxAlignRight()
        self.x_range_min_txt = NumberTextField('0')
        self.x_range_max_txt = NumberTextField('50')
        self.inspect_btn = CheckableFlatButton('Inspect')

        self._smooth_layout = QtWidgets.QHBoxLayout()
        self._smooth_layout.addWidget(LabelAlignRight('Smooth Width:'))
        self._smooth_layout.addWidget(self.smooth_with_sb)
        self._smooth_layout.addWidget(LabelAlignRight('Iterations:'))
        self._smooth_layout.addWidget(self.iterations_sb)
        self._smooth_layout.addWidget(LabelAlignRight('Poly Order:'))
        self._smooth_layout.addWidget(self.poly_order_sb)

        self._range_layout = QtWidgets.QHBoxLayout()
        self._range_layout.addWidget(QtWidgets.QLabel('X-Range:'))
        self._range_layout.addWidget(self.x_range_min_txt)
        self._range_layout.addWidget(QtWidgets.QLabel('-'))
        self._range_layout.addWidget(self.x_range_max_txt)
        self._range_layout.addSpacerItem(HorizontalSpacerItem())

        self._pattern_background_gb.addLayout(self._smooth_layout, 0, 0)
        self._pattern_background_gb.addLayout(self._range_layout, 1, 0)

        self._pattern_background_gb.addWidget(self.inspect_btn, 0, 2, 2, 1)
        self._pattern_background_gb.addItem(HorizontalSpacerItem(), 0, 3, 2, 1)

        self.pattern_background_gb.setLayout(self._pattern_background_gb)

        self._layout.addWidget(self.pattern_background_gb)
        self._layout.addSpacerItem(VerticalSpacerItem())

        self.setLayout(self._layout)
        self.style_widgets()

    def style_widgets(self):
        self.style_image_background_widgets()
        self.style_pattern_background_widgets()

    def style_image_background_widgets(self):
        step_txt_width = 70
        self.scale_step_msb.setMaximumWidth(step_txt_width)
        self.scale_step_msb.setMinimumWidth(step_txt_width)
        self.offset_step_msb.setMaximumWidth(step_txt_width)

        sb_width = 110
        self.scale_sb.setMaximumWidth(sb_width)
        self.scale_sb.setMinimumWidth(sb_width)
        self.offset_sb.setMaximumWidth(sb_width)
        self.offset_sb.setMinimumWidth(sb_width)

        self.scale_sb.setMinimum(-9999999)
        self.scale_sb.setMaximum(9999999)
        self.scale_sb.setValue(1)
        self.scale_sb.setSingleStep(0.01)

        self.pattern_background_gb.setCheckable(True)
        self.pattern_background_gb.setChecked(False)

        self.scale_step_msb.setMaximum(10.0)
        self.scale_step_msb.setMinimum(0.01)
        self.scale_step_msb.setValue(0.01)

        self.offset_step_msb.setMaximum(100000.0)
        self.offset_step_msb.setMinimum(0.01)
        self.offset_step_msb.setValue(100.0)

        self.offset_sb.setMaximum(999999998)
        self.offset_sb.setMinimum(-99999999)

    def style_pattern_background_widgets(self):
        self.smooth_with_sb.setValue(0.100)
        self.smooth_with_sb.setMinimum(0)
        self.smooth_with_sb.setMaximum(10000000)
        self.smooth_with_sb.setSingleStep(0.005)
        self.smooth_with_sb.setDecimals(3)
        self.smooth_with_sb.setMaximumWidth(100)

        self.iterations_sb.setMaximum(99999)
        self.iterations_sb.setMinimum(1)
        self.iterations_sb.setValue(150)
        self.poly_order_sb.setMaximum(999999)
        self.poly_order_sb.setMinimum(1)
        self.poly_order_sb.setValue(50)

        self.x_range_min_txt.setMaximumWidth(70)
        self.x_range_max_txt.setMaximumWidth(70)

        self.inspect_btn.setMaximumHeight(150)
