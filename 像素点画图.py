# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File:          像素点画图
IDE:           PyCharm
Description:
Author:        Rice
date:          2020/12/15 11:40
-------------------------------------------------
"""
import turtle
from PIL import Image


class DrawPic(object):
    """
    1. 本程序通过分析图片的大小来控制绘画的位置
    2. 分析图片大小自动控制像素点的数量，保证绘画的速度与质量。
    3. 针对任意类型的图片(卡通, 动漫, 文字...)
    """
    def __init__(self, pic_file_name):
        self.pic_name = pic_file_name
        self.t = turtle.Turtle()
        self.s = turtle.Screen()

        self.img = Image.open(self.pic_name)
        self.len = self.img.size[0]
        self.width = self.img.size[1]
        self.pic = self.img.load()
        self.mode1 = 4
        self.mode2 = 0

        self.setup()

    def setup(self):
        self.t.hideturtle()
        self.s.colormode(255)
        self.s.setup(1920, 1080)

    def process_info(self):
        print("图片解析中, 请稍等...")
        print("检测到图片大小为：", self.len, "x", self.width, "正在根据图片尺寸调用相关函数...")

        if self.len * self.width > 450 * 450:
            self.mode1 = 6

        if self.len * self.width > 600 * 900:
            self.mode1 = 8
            print("图片尺寸过大会导致效果不佳！！！")
            print("推荐尺寸：500x500内")

        self.mode2 = self.mode1 / 2
        print("----------------------------")
        print()

    def draw_pixel(self, _i, _j, _color):
        self.s.tracer(0)
        self.t.up()
        self.t.goto(-self.len + _i * self.mode1, self.width - _j * self.mode1)
        self.t.down()
        self.t.pencolor(_color)
        self.t.dot(self.mode1)

    def draw_pic(self):
        x = 0
        y = 0
        x0_num = int(self.len / self.mode2)
        y0_num = int(self.width / self.mode2)
        for i in range(x0_num):
            for j in range(y0_num):
                color = self.pic[i * self.mode2, j * self.mode2]
                color = color[:3]
                self.draw_pixel(i, j, color)

                if x == self.width * 2:
                    x = 0
                    y += 1
                else:
                    x += 1
            print("\r绘画中,当前进度：", y * "|", end="")

        print()
        print("----------------------------")
        print("ok, 画完了！！！")

    def done(self):
        turtle.done()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('图片名称', type=str)
    args = str(parser.parse_args())
    loc = args.index("=")

    dp = DrawPic(args[loc+2:-2])
    dp.process_info()
    dp.draw_pic()
    dp.done()
