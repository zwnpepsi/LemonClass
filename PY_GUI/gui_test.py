# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/11/6 14:30
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : gui_test.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import sys
from PyQt5 import (QtWidgets, QtCore)

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(480, 320)
widget.setWindowTitle("Hello, PyQt5.8!")
widget.show()
sys.exit(app.exec())