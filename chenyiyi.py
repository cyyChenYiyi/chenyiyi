import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import io
import numpy as np
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
st.set_page_config(page_title="陈奕羿Chenyiyi", page_icon="https://static.codemao.cn/coco/player/unstable/ryB93wJY0.image/png?hash=Fv21fonr92VybYwCRBeXhZPyZJs9", layout="wide", initial_sidebar_state="auto", menu_items=None)

# 辅助函数
def img_change(img, rc, bc, gc):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            if len(img_array[x, y]) == 4:  # 检查像素值是否包含四个元素
                r, g, b, a = img_array[x, y]  # 分别取出RGBA值
                img_array[x, y] = (b, g, r, a)  # 重新赋值，保持 alpha 通道不变
            else:
                r, g, b = img_array[x, y]  # 对于RGB图片，正常处理
                img_array[x, y] = (b, g, r)
    return img

def adjust_brightness(image, brightness):
    enhancer = ImageEnhance.Brightness(image)
    factor = 0.1 + (brightness / 50.0)
    adjusted_image = enhancer.enhance(factor)
    return adjusted_image

def img_to_bytes(image):
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr.getvalue()

def apply_filter(img, filter_type):
    if filter_type == '模糊':
        return img.filter(ImageFilter.BLUR)
    elif filter_type == '锐化':
        return img.filter(ImageFilter.SHARPEN)
    elif filter_type == '边缘增强':
        return img.filter(ImageFilter.EDGE_ENHANCE)
    elif filter_type == '高斯模糊':
        return img.filter(ImageFilter.GaussianBlur(radius=2))
    elif filter_type == '浮雕效果':
        return img.filter(ImageFilter.EMBOSS)
    else:
        return img

def plot_function(func_str, x_range):
    x = np.linspace(x_range[0], x_range[1], 400)
    y = eval(func_str)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.title('Function Plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    st.pyplot()

# 页面布局
st.title("Chenyiyi的网站")

# 第一个大板块：个人介绍和兴趣推荐
with st.container():
    st.header("个人介绍与兴趣推荐")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("个人介绍")
        st.markdown("### 总述")
        st.markdown("我是陈奕羿，一名初中生")
        st.markdown("### 联系方式")
        st.markdown("邮箱：18250858915@163.com")
        st.markdown("QQ：3302931192")
        st.markdown("微信：18250858915")
        st.markdown("### 个人简介")
        st.markdown("我热爱编程，喜欢阅读科幻小说，喜欢科幻电影")
        st.markdown("### 关于这个网站")
        st.markdown("这个网站是我用streamlit框架搭建的，目前还在完善中")
        st.markdown("目前实现的功能有：1、展示个人简介 2、展示个人兴趣 3、展示个人项目4、智慧词典5、数学函数图像绘制6、图片处理7、音乐播放")
        
    with col2:
        st.subheader("兴趣推荐")
        st.markdown('开始阅读之前，不妨先听听**我最喜欢的歌曲**吧~')
        # 打开音频文件
        audio_file = open('Chenyiyi_music.mp3', 'rb')
        audio_bytes = audio_file.read()

        # 使用st.audio函数播放音频
        st.audio(audio_bytes, format='audio/mp3')
        st.markdown("我的爱好是**写代码**和**阅读**")
        # 使用Tabs来显示原图和修改后的图
        taba, tabb = st.tabs(["编程", "阅读"])
        with taba:
            st.markdown('### 总述')
            st.markdown('我~~熟练~~掌握***python***、***html***和***css***，目前还在学习C++')
            st.markdown('[****跳转至github主页****](https://github.com/cyyChenYiyi/ "github主页")')
            st.markdown('### 项目')
            st.markdown("#### ClassGuardian")
            st.markdown('[****跳转至项目github主页****](https://github.com/cyyChenYiyi/ClassGuardian "ClassGuardian github主页")')
            st.markdown('基于python+html，实现了以下功能：')
            st.markdown('1、一键给教室电脑上锁，防止学生课间偷玩电脑')
            st.markdown('2、教师只需拿出手机扫码即可关闭锁机')
            st.markdown('3、显示距离上课时间等小功能')
            st.image("Chenyiyi_image1.png")
            st.markdown("#### blog")
            st.markdown('[****跳转至项目github主页****](https://github.com/cyyChenYiyi/cyychenyiyi.github.io "项目github主页")')
            st.markdown('基于开源项目Gmeek，实现了blog')
            st.markdown('[****跳转至Blog****](https://cyychenyiyi.github.io "Blog")')
            st.markdown('> 剩余部分老旧项目暂不展示')
            
        with tabb:
            st.markdown('### 总述')
            st.markdown('我热爱阅读文学作品，比较喜欢小说、散文')
            st.markdown('当然也很喜欢科幻文学作品，特别推荐《三体》《流浪地球》')
            st.image("Chenyiyi_image2.jpg")
            st.markdown('书籍是人类进步的阶梯，希望你也能阅读起来！')

# 第二个大板块：工具和留言
with st.container():
    st.header("工具和留言")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("图片处理工具")
        # 图片增加滤镜功能
        st.markdown('#### 图片增加滤镜')
        filter_file = st.file_uploader('上传图片进行滤镜处理', type=['png', 'jpg', 'jpeg'], key='filter_upload')
        filter_type = st.selectbox('选择滤镜类型', ['原图', '模糊', '锐化', '边缘增强', '高斯模糊', '浮雕效果'])
        
        tab_filter_original, tab_filter_modified = st.tabs(["原图", "滤镜后"])
        if filter_file:
            img_filter = Image.open(filter_file)
            with tab_filter_original:
                st.image(img_filter, caption="原始图片")
            
            if filter_type != '原图':
                filtered_img = apply_filter(img_filter, filter_type)
            else:
                filtered_img = img_filter
            
            with tab_filter_modified:
                st.image(filtered_img, caption="滤镜后的图片")
            
            # 保存处理后图片以便下载
            filtered_img_bytes = img_to_bytes(filtered_img)
            st.download_button("下载处理后的图片", filtered_img_bytes, f"{filter_type}_image.png")
        
        # 图片换色功能
        st.markdown('#### 图片换色')
        uploaded_file = st.file_uploader('上传图片', type=['png', 'jpg', 'jpeg'], key='color_change_upload')
        
        # 滑块和恢复默认值按钮
        a = st.slider(label='请输入参数1', min_value=0, max_value=3, value=0, step=1, help="请输入参数1")
        if st.button('重置参数1', key='reset_a'):
            a = 0
        b = st.slider(label='请输入参数2', min_value=0, max_value=3, value=0, step=1, help="请输入参数2")
        if st.button('重置参数2', key='reset_b'):
            b = 0
        c = st.slider(label='请输入参数3', min_value=0, max_value=3, value=0, step=1, help="请输入参数3")
        if st.button('重置参数3', key='reset_c'):
            c = 0
        
        tab1, tab2 = st.tabs(["原图", "修改后"])
        if uploaded_file:
            img = Image.open(uploaded_file)
            with tab1:
                st.image(img, caption="原始图片")
                original_img_bytes = img_to_bytes(img)  # 保存原始图片以便下载
                st.download_button("下载原始图片", original_img_bytes, "original_image.png")
                
            modified_img = img_change(img.copy(), a, b, c)
            with tab2:
                st.image(modified_img, caption="修改后的图片")
                modified_img_bytes = img_to_bytes(modified_img)  # 保存修改后图片以便下载
                st.download_button("下载修改后图片", modified_img_bytes, "modified_image.png")
        else:
            st.warning("请上传图片以使用工具。")
        
        # 图片灰度图转换功能
        st.markdown('#### 图片灰度图转换')
        grayscale_file = st.file_uploader('上传图片进行灰度转换', type=['png', 'jpg', 'jpeg'], key='grayscale_upload')
        brightness = st.slider('调整亮度', min_value=0, max_value=100, value=50, step=1, help="调整图片的亮度")
        if st.button('重置亮度', key='reset_brightness'):
            brightness = 50
        
        tab3, tab4 = st.tabs(["原图", "灰度图"])
        if grayscale_file:
            img_gray = Image.open(grayscale_file).convert('L')
            with tab3:
                st.image(img_gray, caption="原始图片")
                original_gray_img_bytes = img_to_bytes(img_gray)  # 保存原始灰度图片以便下载
                st.download_button("下载原始灰度图", original_gray_img_bytes, "original_gray_image.png")
            
            with tab4:
                if brightness != 50:
                    adjusted_img_gray = adjust_brightness(img_gray, brightness)
                    st.image(adjusted_img_gray, caption="灰度图")
                    adjusted_gray_img_bytes = img_to_bytes(adjusted_img_gray)  # 保存调整后灰度图以便下载
                    st.download_button("下载调整后的灰度图", adjusted_gray_img_bytes, "adjusted_gray_image.png")
                else:
                    st.image(img_gray, caption="灰度图")
                    original_gray_img_bytes = img_to_bytes(img_gray)  # 保存原始灰度图以便下载
                    st.download_button("下载灰度图", original_gray_img_bytes, "gray_image.png")
        else:
            st.warning("请上传图片进行灰度图转换。")
        
        # 图片添加水印功能
        st.markdown('#### 图片添加水印')
        base_image_file = st.file_uploader('上传主图', type=['png', 'jpg', 'jpeg'], key='base_image')
        watermark_file = st.file_uploader('上传水印图', type=['png', 'jpg', 'jpeg'], key='watermark_image')
        
        opacity = st.slider('水印透明度', min_value=0, max_value=100, value=50, step=1)
        size = st.slider('水印大小', min_value=0.1, max_value=2.0, value=1.0, step=0.1)
        position = st.selectbox('水印位置', ['左上', '右上', '左下', '右下', '中心'])
        
        if base_image_file and watermark_file:
            base_image = Image.open(base_image_file).convert("RGBA")
            watermark = Image.open(watermark_file).convert("RGBA")
            
            # 调整水印大小
            watermark = watermark.resize((int(watermark.width * size), int(watermark.height * size)))
            
            # 设置水印透明度
            alpha = watermark.split()[3]
            alpha = alpha.point(lambda p: p * (opacity / 100.0))
            watermark.putalpha(alpha)
            
            # 计算水印位置
            if position == '左上':
                position = (0, 0)
            elif position == '右上':
                position = (base_image.width - watermark.width, 0)
            elif position == '左下':
                position = (0, base_image.height - watermark.height)
            elif position == '右下':
                position = (base_image.width - watermark.width, base_image.height - watermark.height)
            else:  # 中心
                position = ((base_image.width - watermark.width) // 2, (base_image.height - watermark.height) // 2)
            
            # 添加水印
            base_image.paste(watermark, position, watermark)
            
            # 显示原图与水印添加后的图
            tab5, tab6 = st.tabs(["原图", "修改后"])
            
            with tab5:
                st.image(base_image, caption="原始主图")
                original_watermark_img_bytes = img_to_bytes(base_image)  # 保存原始主图以便下载
                st.download_button("下载原始主图", original_watermark_img_bytes, "original_base_image.png")
            
            with tab6:
                st.image(base_image, caption="添加水印后的图片")
                watermarked_img_bytes = img_to_bytes(base_image)  # 保存带水印后的图以便下载
                st.download_button("下载带水印的图片", watermarked_img_bytes, "watermarked_image.png")
        else:
            st.warning("请上传主图和水印图。")

    with col2:
        st.subheader("函数图像工具")
        # 函数图像工具的代码
        func_input = st.text_input("请输入函数表达式，例如 'x**2' 或 'np.sin(x)':")
        x_min = st.number_input("请输入x的最小值：", value=-10.0)
        x_max = st.number_input("请输入x的最大值：", value=10.0)
        if func_input and x_min < x_max:
            plot_function(func_input, (x_min, x_max))
        def read_words_dict(file_path):  
            with open(file_path, 'r', encoding='utf-8') as f:  
                words_list = f.read().split('\n')  
            words_dict = {word_info[1]: [int(word_info[0]), word_info[2]] for word_info in [line.split('#') for line in words_list if line.strip()] if len(word_info) >= 3}  
            return words_dict  
    
        def read_check_out_times(file_path):  
            times_dict = {}  
            try:  
                with open(file_path, 'r', encoding='utf-8') as f:  
                    for line in f:  
                        stripped_line = line.strip()  
                        if stripped_line:  # 确保行不为空  
                            parts = stripped_line.split('#')  
                            if len(parts) == 2:  
                                try:  
                                    key = int(parts[0])  
                                    value = int(parts[1])  
                                    times_dict[key] = value  
                                except ValueError:  
                                    print(f"跳过无效行: {line.strip()}, 因为无法将某些部分转换为整数")  
            except FileNotFoundError:  
                print(f"文件未找到: {file_path}")  
            return times_dict
        
        def update_check_out_times(file_path, times_dict):  
            with open(file_path, 'w', encoding='utf-8') as f:  
                for k, v in times_dict.items():  
                    f.write(f"{k}#{v}\n")  
        

        words_dict = read_words_dict('words_space.txt')  
        times_dict = read_check_out_times('check_out_times.txt')  
        
        st.subheader('智慧学英语')  
        word = st.text_input('请输入您想查询的单词')  
        
        if st.button('查询'):  
            if word == "chenyiyi":  
                st.markdown("***恭喜你触发彩蛋***，6")  
                st.balloons()  
                st.snow()  
            elif word == "python":  
                st.code('print("hello, world")')  
                st.write("恭喜你触发彩蛋，这是一行python代码，python n.蛇")  
            elif word in words_dict:  
                # 获取单词编号  
                word_id = words_dict[word][0]  
                # 更新查询次数  
                if word_id in times_dict:  
                    times_dict[word_id] += 1  
                else:  
                    times_dict[word_id] = 1  
                
                # 保存到文件  
                update_check_out_times('check_out_times.txt', times_dict)  
                
                # 显示信息  
                st.markdown("##### 解释")  
                st.markdown(f"**{words_dict[word][1]}**")  
                st.markdown("##### 查询次数")  
                st.write(f"**{times_dict[word_id]}**")  
            else:  
                st.write("该单词不在词典中。")
        st.subheader('影视解析')
        st.write("请输入影视链接：")
        movie_link = st.text_input("影视链接")
        if st.button("解析"):
            video_url = "https://jx.xmflv.com/?url=" + movie_link
            components.iframe(video_url, width=700, height=400)
    
    with col3:
        st.subheader('我的留言区')

        # 尝试从文件中加载内容，并检查格式
        try:
            with open('leave_messages.txt', 'r', encoding='utf-8') as f:
                messages_list = f.read().split('\n')
            # 确保每个msg非空且格式正确
            messages_list = [msg.split('#') for msg in messages_list if msg and len(msg.split('#')) == 4]
        except Exception as e:
            st.error(f"读取文件时出错：{e}")
            messages_list = []

        # 显示消息
        if messages_list:
            for i in messages_list:
                if len(i) == 4:  # 现在只处理完全符合预期格式的留言
                    emoji = i[3] if i[3].strip() else '👌'  # 使用指定的表情或默认表情
                    with st.chat_message(emoji):
                        st.write(i[1], ':', i[2])
        else:
            st.write("没有留言显示。")

        # 输入新消息
        name = st.text_input('我是')
        new_message = st.text_input('想要说的话……')
        emoji = st.text_input('头像（使用表情包键入）', '🤵')
        if st.button('留言'):
            new_id = str(int(messages_list[-1][0]) + 1) if messages_list else '1'
            messages_list.append([new_id, name, new_message, emoji])  # 添加新留言

            # 尝试写入文件
            try:
                message = '\n'.join('#'.join(map(str, m)) for m in messages_list).strip()
                with open('leave_messages.txt', 'w', encoding='utf-8') as f:
                    f.write(message)
            except Exception as e:
                st.error(f"写入文件时出错：{e}")
# 脚注
st.caption("欢迎访问Chenyiyi的网站，希望您有所收获!")
