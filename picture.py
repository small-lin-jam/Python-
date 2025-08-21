from PIL import Image, ImageDraw, ImageFont
import random

# 随机生成四个字母
def random_char():
    return chr(random.randint(65, 90))

# 随机生成颜色
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# 创建一张验证码图片
def create_code():
    # 定义图片大小
    width, height = 120, 50
    # 创建一张空白图片
    im = Image.new('RGB', (width, height), 'white')
    # 创建画笔
    draw = ImageDraw.Draw(im)
    # 定义字体样式和大小
    font = ImageFont.truetype('arial.ttf', 36)
    # 在图片上绘制四个字母
    for i in range(4):
        draw.text((30*i+15, 5), random_char(), font=font, fill=random_color())
    # 加入干扰点和线条
    for i in range(50):
        draw.point((random.randint(0,width), random.randint(0,height)), fill=random_color())
        draw.line((random.randint(0,width), random.randint(0,height), random.randint(0,width), random.randint(0,height)), fill=random_color())
    # 返回验证码图片和对应的文字
    return im, ''.join([random_char() for i in range(4)])

# 调用函数生成验证码图片和文字
im, code = create_code()
# 保存图片到本地
im.save('code.png', 'png')