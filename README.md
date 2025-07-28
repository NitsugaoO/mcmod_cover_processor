# mcmod_cover_processor

把正方形模组封面图片转换为 MC 百科要求的模组封面规格.

Python 代码, 使用 Deepseek 写的.

使用前需先安装 Python 和 ````pillow```` 库:

````pip install pillow````

然后你可以将正方形的图片直接拖到这个 image_processor.py 文件上 (文件设置为使用 Python 运行), 或者运行 .py 文件把图片拖到窗口中, 或者用 ````python image_processor.py 图片文件````

处理后的图片保存在原图同一目录, 文件名添加 _processed 后缀.

Tips: 可以通过 CurseForge 的模组封面 url 去除 ````/thumbnails```` 和 ````/64/64```` 字段得到高清模组封面图.
