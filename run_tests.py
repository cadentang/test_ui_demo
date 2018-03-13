import pytest
import time

"""
说明：

"""

if __name__ == "__main__":
    now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
    pytest.main(["-s", "./test_case/", "--html=./test_report/"+now_time+"report.html",
                 "--self-contained-html", "--reruns", "3"])
