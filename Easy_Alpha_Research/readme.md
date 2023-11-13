# Easy Alpha Research
## 1.简介
主要展示我的单因子分析框架，包括数据的下载、数据的预处理、单因子有效性的分析以及使用Openai接口的一些尝试

## 2.使用方法
主要分析在/Easy_Alpha_Research/quant_factor_research/analysis/single_factor_analyse.ipynb这个文件里
除此之外我还准备了一个基于streamlit的因子可视化（没有写完），位于web文件夹里
Openai-plugins的尝试我并没有写下去，有想法可以重构一下这个部分

## 3.注意事项
- Alphalens已经不再支持当前版本的pandas，因此我在开源的基础上修改了原有的Alphalens使其支持我的研究环境，在使用的时候可以将其作为new_alphalens导入

- 数据的下载基于米筐的开放接口（现在不付费已经用不了了），所以我下载了部分示例在data文件夹里