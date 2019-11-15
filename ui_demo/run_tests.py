import pytest
import time


"""
说明：
py.tes
--rerun 2    用例失败再重跑2次
--html 报告放置的位置

"""

# -*- coding:utf-8 -*-

import sys, getopt


def main(argv):
    inputfile = ""
    outputfile = ""

    try:
        # 这里的 h 就表示该选项无参数，i:表示 i 选项后需要有参数
        opts, args = getopt.getopt(argv, "hi:o:", ["infile=", "outfile=", "version", "help"])
        # 第一个是 (option, value) 元组的列表。 第二个是参数列表，包含那些没有'-'或'--'的参数
    except getopt.GetoptError:
        print('test_arg.py -i <inputfile> -o <outputfile>')
        print('or: test_arg.py --infile=<inputfile> --outfile=<outputfile>')
        print('or: test_arg.py --version --help')
        sys.exit(2)

    if len(args) > 0:  # 表示有未识别的参数格式
        print('test_arg.py -i <inputfile> -o <outputfile>')
        print('or: test_arg.py --infile=<inputfile> --outfile=<outputfile>')
        print('or: test_arg.py --version --help')
        sys.exit(1)
    else:
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print('test_arg.py -i <inputfile> -o <outputfile>')
                print('or: test_arg.py --infile=<inputfile> --outfile=<outputfile>')
                print('or: test_arg.py --version --help')

                sys.exit()
            elif opt in ("-i", "--infile"):
                inputfile = arg
            elif opt in ("-o", "--outfile"):
                outputfile = arg
            elif opt in ("--version"):
                print('0.0.1')
                sys.exit()

    print('Input file : ', inputfile)
    print('Output file: ', outputfile)


if __name__ == "__main__":
    main(sys.argv[1:])
# if __name__ == "__main__":
#     now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
#     pytest.main(["-s", "./test_case/", "--html=./test_report/"+now_time+"report.html",
#                  "--self-contained-html", "--reruns", "3"])
