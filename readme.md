# Guab

**不更新了，因为我不玩了，哈哈**
## ABOUT
一个Android版`冲顶大会`的Python辅助程序。

## UPDATE
- V1.1 增加题目行数为3的支持

## HOW TO USE
### TOOLS
- Python 3.6 
- 依赖库：pytesseract、opencv、os、requests
- tesseract-ocr 及其简体中文包（包含在Tools文件夹）
- adb调试工具（包含在Tools文件夹）
- 一部安卓手机和一条数据线

### STEPS
- 安装以上所有所需软件，并配置`环境变量`以在命令行下使用。
- 将手机设置为：设置 → 开发者选项`on` → USB调试`on`，用数据线将手机与电脑相连接，在命令行模式下输入 `adb devices`，若返回一串数字字母组合和device，即表示连接成功。我们需要将答题界面的截图发送至电脑。调用`python`中的`os.system()`函数，即为：
    ```python
    os.system("adb shell screencap -p /sdcard/DCIM/demo/demo.png")
    os.system("adb pull /sdcard/DCIM/demo/demo.png C:/Users/Phun/Desktop/guab")
    ```
    请对路径进行适当修改，将pull到电脑的路径与主程序在同一目录下。
- 使用`opencv`对截图进行处理。首先读入图片：
    ```python
    a = cv2.imread('demo.png')
    ```
    在实际答题过程中，题目可能为一行或多行。所以立一个flag：
    ```python
    flag = 1
    ```
    题干和选项的位置并非绝对位置，而是随着题干的长度进行变化。故为了快速检测题目的长度，采取以下方法检测题目长度：
    ```python
    a = cv2.imread('demo.png')
    flag = 1

    for i in range(420,470):
        for j in range(86,130):
            # print(a[i,j,0])
            if a[i,j,0] != 255:
            flag = 2
            break

    for i in range(495,545):
        for j in range(86,130):
            # print(a[i,j,0])
            if a[i,j,0] != 255:
            flag = 3
            break
    ```
    即检测在第二行、第三行的前两个字符的位置是否有字符出现 **（此数值由不同机型决定，此处为Samsung C5000，请根据需求自行调整）**。若出现，则flag改变相应数值。
    ```python
    if flag == 1:    
        title = a[268:485,75:1005]
        ans_1 = a[500:600,105:970]
        ans_2 = a[640:740,105:970]
        ans_3 = a[780:880,105:970]

    elif flag == 2:
        title = a[328:531,75:1005]
        ans_1 = a[570:670,105:970]
        ans_2 = a[710:810,105:970]
        ans_3 = a[850:950,105:970]
        
    elif flag == 3:
        title = a[325:560,75:1005]
        ans_1 = a[650:750,105:970]
        ans_2 = a[790:890,105:970]
        ans_3 = a[930:1030,105:970]
    ```
    `title`表示题干的图像范围，`ans_1/2/3`表示选项的图像范围。示例请见`demo.png`。
- 使用`pytesseract`调用`tesseract-OCR`识别工具识别图片上的文字（**将语言设置为简体中文**），并将识别结果中的空格剔除。
    ```python
    title_fin=pytesseract.image_to_string(title,lang='chi_sim').replace(" ","")
    ans_1_fin=pytesseract.image_to_string(ans_1,lang='chi_sim').replace(" ","")
    ans_2_fin=pytesseract.image_to_string(ans_2,lang='chi_sim').replace(" ","")
    ans_3_fin=pytesseract.image_to_string(ans_3,lang='chi_sim').replace(" ","")
    ```
- 利用`爬虫`，将题干放入搜索引擎中搜索，并将选项进行匹配，并返回相匹配的数量。通过查看各搜索引擎搜索结果源代码可以发现，百度的搜索结果源代码广告居多，内容甚少，而google需要科学上网，且延迟较高。最终选定360搜索。通过分析得知搜索结果的链接的结构如下：
    ```python
    url = "https://www.so.com/s?&q=" + title_fin
    ```
    这里省去了一个完整的爬虫中的很多步骤，仅调用`requests`库中`requests.get()`函数来获取网页的源代码，直接将选项与源代码内容进行匹配，并返回匹配数即可。（识别失败的结果不显示）
    ```python
    if ans_1_fin != "":
        print(ans_1_fin,text.count(ans_1_fin))
    if ans_2_fin != "":
        print(ans_2_fin,text.count(ans_2_fin))
    if ans_3_fin != "":
        print(ans_3_fin,text.count(ans_3_fin))
    ```

## MORE
识别速度不够快，测试用例不够多，仅为`demo版`。

## CONTACT
aaaphun@gmail.com