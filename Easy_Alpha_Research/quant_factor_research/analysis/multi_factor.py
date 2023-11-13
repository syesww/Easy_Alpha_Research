# 多因子相关性分析
def calculate_factor_correlation(factor_ic_values):
    # 将每个因子的Series对象合并成一个DataFrame
    factor_df = pd.concat(factor_ic_values, axis=1)
    
    # 计算因子之间的相关性
    correlation_matrix = factor_df.corr(method='spearman')
    
    # 绘制相关性矩阵的热力图
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Factor Correlation Heatmap')
    plt.show()
    
    return correlation_matrix