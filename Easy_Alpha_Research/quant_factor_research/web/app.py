import streamlit as st
import numpy as np
import pandas as pd

data = pd.read_hdf('statistics.h5', key='data')

mr = data['factor_mean_return'][0]
mean = data['IC_mean'][0]
std = data['IC_std'][0]
per = data['IC_percent'][0]
ir = data['IR'][0]


st.title("单因子分析可视化")

st.markdown("## 因子概览")
st.markdown("<div align='center' style='font-size: 20px'><b>平均收益率: {:.4f}  IC均值: {:.4f}  IC标准差: {:.4f}  IC > 0.02: {:.4f}  IR: {:.4f}</b></div>".format(mr, mean, std, per, ir), unsafe_allow_html=True)

st.markdown("## 因子IC分析")

st.markdown("## 因子收益率分析")