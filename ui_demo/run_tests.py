import pytest
import time


"""
说明：
py.tes
--rerun 2    用例失败再重跑2次
--html 报告放置的位置

"""
if __name__ == "__main__":
    now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
    pytest.main(["-s", "./test_case/", "--html=./test_report/"+now_time+"report.html",
                 "--self-contained-html", "--reruns", "3"])
