
# DALL-E Image Generation with OpenAI API and Tencent Cloud

This Streamlit app allows users to generate images using the DALL-E API from OpenAI and Tencent Cloud.

## Installation

1. Clone this repository to your local machine.
2. Install the required packages listed in `requirements.txt`.
3. Set your OpenAI API key in the `openai_api_key` variable in `app.py`.
4. Run the app with the command `python -m streamlit run app.py`.

## Usage

1. Enter a prompt for the image generation in the text input field.
2. Click the "Generate Image" button.
3. Wait for the image to be generated. A spinner animation will be displayed while the image is being generated.
4. The generated image will be displayed with the corresponding prompt caption. If the image generation fails, a warning message will be displayed.

## Notes

- This app is for demonstration purposes only. It is not intended for production use.
- The image generation may take some time to complete, depending on the complexity of the prompt and the load on the DALL-E API.
- Use your OpenAI API key responsibly and be mindful of the associated costs.

# DALL-E 图像生成应用（基于 OpenAI API 和腾讯云）

这个 Streamlit 应用允许用户使用 OpenAI 和腾讯云的 DALL-E API 来生成图片。

## 安装

1. 克隆本仓库到本地。
2. 安装 `requirements.txt` 中列出的必要软件包。
3. 在 `app.py` 文件中的 `openai_api_key` 变量中设置你的 OpenAI API 密钥。
4. 运行命令 `python -m streamlit run app.py` 来启动该应用程序。

## 使用

1. 在文本输入框中输入一个用于图像生成的提示语。
2. 点击 "生成图片" 按钮。
3. 等待图片生成。在生成过程中会显示一个旋转的动画。
4. 生成的图像将会和其对应的提示语标题一起显示出来。如果生成过程失败，会显示一个警告信息。

## 注意事项

- 该应用仅用于演示目的。不适用于生产环境。
- 图像生成的时间会根据提示语的复杂程度和 DALL-E API 的负载情况而不同。
- 在使用 OpenAI API 时要负责任地使用并注意相关费用。
