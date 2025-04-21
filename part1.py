from manim import *

class aiaa2711(Scene):
    def opening(self):
        text = Text("Thoroughly Understand Cross Entropy in 8 Minutes", font_size=24)
        #subtext
        subtext = Text("from dice to machine learning", font_size=16).next_to(text, DOWN)
        self.play(Write(text),Write(subtext))
        self.wait(1)
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
        self.wait(1)
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
            self.wait(0.5)
        
        self.wait(2)
        
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
        
        # 骰子淡入动画
        self.play(
            LaggedStart(
                *[FadeIn(dice) for dice in dices],
                lag_ratio=0.3
            ),
            run_time=3
        )
        
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
        self.wait(2)
        
        # 淡出所有对象
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        
        

        
    def construct(self):
        # self.opening()
        # self.weather()
        # self.show_connection()
        self.dice()
