from manim import *
import numpy as np

class aiaa2711(Scene):
    def opening(self):
        text = Text("Thoroughly Understand Cross Entropy in 8 Minutes", font_size=24)
        #subtext
        subtext = Text("from dice to machine learning", font_size=16).next_to(text, DOWN)
        self.play(Write(text),Write(subtext))
        self.wait(1) # 等待时间，随配音调整
        self.play(FadeOut(text), FadeOut(subtext))
    
    def weather(self):
        cloud = ImageMobject("rain.png")
        rain_probability = Text("80%", font_size=48).next_to(cloud, UP)
        
        # 创建右侧晴天图标和实际天气文本
        sunshine = ImageMobject("sunshine.png")
        # sunshine.pixel_array = 255 - sunshine.pixel_array  # 调整亮度
        actual_weather = Text("Actual Weather", font_size=48).next_to(sunshine, UP)
        
        self.play(FadeIn(cloud), FadeIn(rain_probability))
        self.play(Transform(cloud, sunshine), Transform(rain_probability, actual_weather))
        self.wait(1) # 等待时间，随配音调整
        # self.play(FadeOut(cloud), FadeOut(rain_probability))
        
        self.play(cloud.animate.shift(LEFT * 4), rain_probability.animate.shift(LEFT * 4))
        
        text_1 = Text("Accuracy of prediction?", font_size=30).shift(RIGHT*2 + UP*2)
        Text_2 = Text("How to quantify accuracy?", font_size=30).shift(RIGHT*2)
        
        self.play(Write(text_1), Write(Text_2))
        
        # 清除文本和云朵
        self.play(FadeOut(text_1), FadeOut(Text_2), FadeOut(cloud), FadeOut(rain_probability))
        
        
    def show_connection(self):
        text_cross_entropy = Text("Cross Entropy", font_size=48).shift(UP*2)
        
        self.play(Write(text_cross_entropy))
        self.play(text_cross_entropy.animate.shift(LEFT * 4))
        
          # 创建右侧的文件名文本
        files = [
            "Image Classification",
            "Language Model",
            "GAN",
            "..."
        ]
        
        file_texts = []
        for i, file in enumerate(files):
            file_text = Text(file, font_size=16).shift(RIGHT * 4 + UP * (1 - i))
            file_texts.append(file_text)
        
        # 逐个显示文件名
        arrows = []
        for file_text in file_texts:
            self.play(Write(file_text, run_time=0.2))
            arrow = Arrow(
                start=file_text.get_left(),
                end=text_cross_entropy.get_right(),
                color=BLUE,
                buff=0.2
            )
            arrows.append(arrow)
            self.play(Create(arrow, run_time=0.2))
            self.wait(0.5)  # 等待时间，随配音调整
        
        self.wait(2)  # 等待时间，随配音调整
        
        # 淡出所有元素
        self.play(
            FadeOut(text_cross_entropy),
            *[FadeOut(file_text) for file_text in file_texts],
            *[FadeOut(arrow) for arrow in arrows]
        )

    def dice(self):
        # 加载骰子图片（确保路径正确）
        dices = [
            ImageMobject("骰子1.png"),
            ImageMobject("骰子2.png"),
            ImageMobject("骰子3.png"),
            ImageMobject("骰子4.png"),
            ImageMobject("骰子5.png"),
            ImageMobject("骰子6.png")
        ]
        
        # 将骰子排列为 2x3 网格（靠右对齐）
        grid = Group(*dices).arrange_in_grid(rows=2, cols=3, buff=0.5).to_edge(RIGHT).shift(UP * 0.5)
        
        text_line0 = Text("Roll a homogeneous dice", font_size=36).shift(LEFT*3)
        
        # 骰子淡入动画
        self.play(
            LaggedStart(
                *[FadeIn(dice) for dice in dices],
                lag_ratio=0.3
            ),
            Write(text_line0),
            run_time=2
        )
        
        self.play(grid.animate.shift(LEFT * 14), text_line0.animate.shift(LEFT * 14))        
        # 创建骰子标签
        dice_labels = [Text(f"{i+1}", font_size=36) for i in range(6)]
        
        # 创建概率分布直方图
        bar_chart = BarChart(
            [1/6]*6,
            bar_names=[f"{i+1}" for i in range(6)],
            bar_colors=[BLUE, GREEN, RED, YELLOW, PINK, ORANGE],
            y_range=[0, 0.2, 0.05],
            y_length=5,
            x_length=10,
            x_axis_config={"font_size": 36},
            y_axis_config={"font_size": 36}
        ).scale(0.5)
        
        # 将骰子图片和标签组合为 Group
        dice_groups = Group(*[
            Group(dices[i], dice_labels[i]).arrange(DOWN) 
            for i in range(6)
        ]).arrange(RIGHT, buff=0.5)
        
        # 整体布局
        all_objects = Group(dice_groups, bar_chart).arrange(DOWN, buff=1)
        
        # 添加标签和图表动画
        self.play(FadeIn(all_objects))
        
        # 添加概率公式
        text_probability = MathTex(r"P(A) = \frac{1}{6}", font_size=36).next_to(bar_chart, UP)
        self.play(Write(text_probability)) 
        self.wait(2)  # 等待时间，随配音调整
        
        # 淡出所有对象
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        
        text_line1 = Text(
            "For each result of the dice,", 
            font_size=36
        ).shift(UP * 2)
        text_line2 = Text(
            "the amount of information it brings is the same", 
            font_size=36
        ).next_to(text_line1, DOWN)
        
        self.play(Write(text_line1))
        self.play(Write(text_line2))
        
        # 加载骰子图片并放大
        dice_images = [
            ImageMobject(f"骰子{i+1}.png").scale(1.0)  # 放大骰子图片
            for i in range(6)
        ]
        
        # 初始骰子
        current_dice = dice_images[0].next_to(text_line2, DOWN * 2)
        self.play(FadeIn(current_dice))
        
        # 循环变换动画
        for i in range(1, 6):
            next_dice = dice_images[i].move_to(current_dice)
            self.play(Transform(current_dice, next_dice), run_time=0.2)
            self.wait(0.2)  # 等待时间，随配音调整
        
        self.wait(1)  # 等待时间，随配音调整
        
        text_impossible = Text("Impossible Event woud make you very surprise", font_size=24).shift(RIGHT * 2 + DOWN * 2)
        number = Text("dice = 7 or -1 ", font_size=24).next_to(text_impossible, UP)
        self.play(Write(text_impossible))
        self.play(Write(number))
        
        # 淡出所有对象
        self.wait(1)  # 等待时间，随配音调整
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        self.wait(2)

    def info_formula(self):
        # 创建坐标系
        axes = Axes(
            x_range=[0, 5, 0.5],
            y_range=[0, 5, 0.5],
            x_length=6,
            y_length=6,
            axis_config={"color": WHITE},
            tips=False  # 隐藏坐标轴箭头
        )
        labels = axes.get_axis_labels(x_label="P(A)", y_label="I")
        
        # 定义 y = 1/x 的右侧分支（x > 0）
        func = axes.plot(lambda x: 1/x, x_range=[0.25, 3.8], color=YELLOW)
        
        # 创建渐近线（x=0和y=0）
        asymptote_x = DashedLine(axes.c2p(0,0), axes.c2p(0,4), color=GRAY)
        asymptote_y = DashedLine(axes.c2p(0,0), axes.c2p(4,0), color=GRAY)
        
        # 创建移动点及标签（修正坐标转换）
        moving_dot = Dot(color=BLUE).scale(0.5)

        
        # 动画序列
        self.play(Create(axes), Write(labels))
        self.play(Create(func), Create(VGroup(asymptote_x, asymptote_y)))
        
        # 初始化点位置（x=1, y=1）
        moving_dot.move_to(axes.c2p(1, 1))
        label = always_redraw(lambda : Tex(
            r"({:.2f}, {:.2f})".format(
                *axes.p2c(moving_dot.get_center())  # 关键修正点
            ), 
            color=WHITE
        ).next_to(moving_dot, UR, buff=0.1))
        self.play(FadeIn(moving_dot), FadeIn(label))
        
        # 定义点的运动轨迹（x从1 → 0.3 → 3.5）
        x_tracker = ValueTracker(1)
        moving_dot.add_updater(lambda m: m.move_to(
            axes.c2p(x_tracker.get_value(), 1/x_tracker.get_value())
        ))
        
        self.play(x_tracker.animate.set_value(0.3), run_time=2)
        self.wait(1)
        self.play(x_tracker.animate.set_value(3.5), run_time=3)
        self.wait(2)
        
        # 1. 移除点和标签
        self.play(FadeOut(moving_dot), FadeOut(label))
        
        # 2. 缩小并移动坐标系到右侧
        graph_group = Group(axes, labels, func, asymptote_x, asymptote_y)
        self.play(
            graph_group.animate.scale(0.6).to_edge(RIGHT).shift(UP*0.5),
            run_time=1
        )
        
        # 3. 显示信息量公式
        formula = MathTex(r"I(A) = \frac{1}{P(A)}", color=YELLOW, font_size=48).shift(LEFT* 3 + UP*1)
        formula_desc = Text(
            "Information is inversely proportional\n to probability of event",
            font_size=24,
            color=GRAY
        ).next_to(formula, DOWN, buff=0.5)
        
        self.play(Write(formula), FadeIn(formula_desc))
        self.wait(2)
        
        # 4. 将所有元素移动出场景
        self.play(
            formula.animate.shift(LEFT * 14).scale(0.5),
            formula_desc.animate.shift(LEFT *14).scale(0.5),
            graph_group.animate.shift(LEFT * 14).scale(0.5)
        )
        self.wait(1)
        
    def info_formula2(self):
        # === 画面分割 ===
        divider_line = Line(UP*3, DOWN*3, color=GREY)
        self.play(Create(divider_line))
        
        # 上部：概率计算（移除手动位移，使用对齐参数）
        prob_formula = MathTex(
            r"P(B) = \left(\frac{1}{6}\right)^{10} = ",
            f"{(1/6)**10:.2e}",
            font_size=36,
            color=YELLOW
        ).shift(RIGHT*3 + UP * 1)  # 固定左对齐
        
        # 下部：信息量公式换行处理
        info_formula = MathTex(
            r"I(B) &= I(A) + I(A) + \cdots + I(A)\\",
            r"&= 10 \cdot I(A)",  # 使用换行符 \\
            font_size=36,
            color=BLUE
        ).arrange(DOWN, aligned_edge=LEFT).next_to(prob_formula, DOWN, buff=0.8)
        
        self.play(Write(prob_formula), Write(info_formula), run_time=2)
        self.wait(3)  # 等待时间，随配音调整
        
        # 创建坐标系（调整范围和尺寸）
        axes = Axes(
            x_range=[0, 3, 0.5],  # x轴范围和步长：0到1，步长0.1
            y_range=[-1, 5, 1],    # y轴范围和步长：0到5，步长1
            x_length=5,            # x轴长度
            y_length=5,            # y轴长度
            tips=False, # 隐藏坐标轴箭头
            axis_config={"color": WHITE, "label_direction": DOWN},
        ).shift(LEFT * 3.5)  # 固定左对齐
        axes_labels = axes.get_axis_labels(x_label="P(A)", y_label="I(a)").scale(0.8)

        # 创建函数图像
        func_graph = axes.plot(
            lambda x: -np.log(x) if x != 0 else 0,
            x_range=(0.03, 2.5, 0.01),  # 定义域：x从0.01到1（避开x=0的点）
            color=YELLOW
        )

        # 添加网格线以增强可读性
        grid = NumberPlane(
            x_range=axes.x_range,  
            y_range=axes.y_range,    
            x_length=axes.x_length,
            y_length=axes.y_length,
            axis_config={"color": BLUE_E},
        ).add_coordinates().shift(LEFT * 3.5)  # 固定左对齐

        # 添加公式到坐标轴下方
        formula = MathTex(r"I(a) = -\log(P(A))").next_to(axes, DOWN)

        # 将所有元素添加到场景中
        self.play(FadeIn(axes), Create(axes_labels), FadeIn(grid))
        self.play(Create(func_graph))
        self.play(Write(formula))
        
        self.play(FadeOut(axes), FadeOut(axes_labels), FadeOut(grid), FadeOut(func_graph), FadeOut(prob_formula), FadeOut(info_formula), FadeOut(divider_line))
        self.play(formula.animate.move_to(ORIGIN).scale(1.5))
        self.wait(1)  # 等待时间，随配音调整

    def final_formula(self):
        # 期望的公式
        uncertainty_text = Text("The uncertainty of the entire system ?", font_size=24).shift(UP * 2)
        
        # 创建正态分布图像
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 1, 0.5],
            x_length=4,
            y_length=2,
            axis_config={"color": WHITE},
            tips = False,  # 隐藏坐标轴箭头
        ).shift(DOWN).scale(0.8)  # 缩小坐标系
        
        normal_dist = axes.plot(
            lambda x: np.exp(-x**2 / 2) / np.sqrt(2 * np.pi),
            color=YELLOW
        ).scale(0.8)  # 缩小正态分布图像
        
        # 显示文本和正态分布图像
        self.play(Write(uncertainty_text))
        self.play(FadeIn(axes), FadeIn(normal_dist))
        self.wait(2)
        
        # 将正态分布图像和文本移动到右侧
        group = VGroup(uncertainty_text, axes, normal_dist)
        self.play(group.animate.shift(RIGHT * 4))
        self.wait(1)
        
        # 在左侧显示期望E(X)的公式定义
        expectation_formula = MathTex(
            r"E(X) = \sum_{i=1}^{n} x_i \cdot P(x_i)",
            font_size=36,
            color=BLUE
        ).shift(LEFT * 3)
        
        self.play(Write(expectation_formula))
        self.wait(1)
        
        # 将期望公式变换为香农熵公式
        entropy_formula = MathTex(
            r"H(X) = -\sum_{i=1}^{n} P(x_i) \log P(x_i)",
            font_size=36,
            color=BLUE
        ).shift(LEFT * 3)
        
        self.play(TransformMatchingTex(expectation_formula, entropy_formula))
        self.wait(1)
        
        # 淡出所有元素
        self.play(FadeOut(group), FadeOut(entropy_formula))
        # 添加关于信息量的完整定义
        info_def = VGroup(
            MathTex(r"\Omega = \{x_1, x_2, \ldots, x_n\}", font_size=48),
            MathTex(r"I(x_i) = -\log P(x_i)", font_size=48),
            MathTex(r"H(X) = E(I) = -\sum P(x_i) \log P(x_i)", font_size=48),
            Text("An indicator to measure the degree of chaos in the entire system", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        # 将组合内容移动并放大到屏幕中心
        self.play(Write(info_def))
        self.wait(3)

        
    def construct(self):
        self.opening()
        self.weather()
        self.show_connection()
        self.dice()
        self.info_formula()
        self.info_formula2()
        self.final_formula()
