# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/8 0:13
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : main_smoke.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import pytest
pytest.main(['-m','smoke','--html','TestReport/test_smoke_report.html'])