from PIL import Image

# 打开原始图片
original_image = Image.open("needygirl.jpg")

# 调整大小为512x512像素
resized_image = original_image.resize((256, 256))

# 保存调整后的图片
resized_image.save("needygirl.png")
