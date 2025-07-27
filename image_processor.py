import sys
import os
from PIL import Image, ImageFilter, ImageEnhance

def process_image(input_path):
    try:
        original = Image.open(input_path).convert('RGB')
        
        resized = original.resize((450, 450))
        
        result = Image.new('RGB', (720, 450))
        
        result.paste(resized, (135, 0))
        
        left_region = resized.crop((0, 0, 135, 450))
        processed_left = process_region(left_region)
        result.paste(processed_left, (0, 0))
        
        right_region = resized.crop((315, 0, 450, 450))
        processed_right = process_region(right_region)
        result.paste(processed_right, (585, 0))
        
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_processed{ext}"
        
        result.save(output_path)
        return output_path
    
    except Exception as e:
        print(f"处理图片时出错: {e}")
        return None

def process_region(region):
    blurred = region.filter(ImageFilter.GaussianBlur(radius=7))
    
    enhancer = ImageEnhance.Brightness(blurred)
    darkened = enhancer.enhance(0.6) # 此为控制两侧暗度的系数
    
    return darkened

if __name__ == "__main__":
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
