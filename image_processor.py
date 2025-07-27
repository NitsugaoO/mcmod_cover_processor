import sys
import os
from PIL import Image, ImageFilter, ImageEnhance

def process_image(input_path):
    """处理图片并保存结果"""
    try:
        # 打开图片并转换为RGB
        original = Image.open(input_path).convert('RGB')
        
        # 调整大小为150x150
        resized = original.resize((150, 150))
        
        # 创建新画布 (240x150)
        result = Image.new('RGB', (240, 150))
        
        # 将调整后的图片粘贴到中央 (45-195位置)
        result.paste(resized, (45, 0))
        
        # 处理左侧区域
        left_region = resized.crop((0, 0, 45, 150))
        processed_left = process_region(left_region)
        result.paste(processed_left, (0, 0))
        
        # 处理右侧区域
        right_region = resized.crop((105, 0, 150, 150))
        processed_right = process_region(right_region)
        result.paste(processed_right, (195, 0))
        
        # 生成输出路径
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_processed{ext}"
        
        # 保存结果
        result.save(output_path)
        return output_path
    
    except Exception as e:
        print(f"处理图片时出错: {e}")
        return None

def process_region(region):
    """处理图像区域：模糊 + 调暗"""
    # 高斯模糊
    blurred = region.filter(ImageFilter.GaussianBlur(radius=7))
    
    # 降低亮度
    enhancer = ImageEnhance.Brightness(blurred)
    darkened = enhancer.enhance(0.6)  # 60%亮度
    
    return darkened

if __name__ == "__main__":
    # 检查是否有拖放的文件
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
        
        if os.path.isfile(input_path):
            output_path = process_image(input_path)
            if output_path:
                print(f"图片处理完成! 已保存为: {output_path}")
                print("3秒后窗口将自动关闭...")
                import time
                time.sleep(3)
            else:
                input("按回车键退出...")
        else:
            print("错误: 提供的路径不是文件")
            input("按回车键退出...")
    else:
        print("请将图片文件拖放到此脚本上运行")
        print("或者通过命令行: python image_processor.py <图片路径>")
        input("按回车键退出...")