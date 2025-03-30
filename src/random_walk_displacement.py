import numpy as np
import matplotlib.pyplot as plt

def random_walk_displacement(num_steps, num_simulations):
    """
    模拟随机行走并返回每次模拟的最终位移

    参数:
    num_steps (int): 随机行走的步数
    num_simulations (int): 模拟的次数

    返回:
    numpy.ndarray: 形状为(2, num_simulations)的数组，表示每次模拟的最终位移
    """
    # TODO: 检查输入参数的有效性
    
    # TODO: 实现随机行走算法
    # 提示：
    # 1. 使用 np.random.choice 生成随机步长 ([-1, 1])
    # 2. 生成形状为 (2, num_simulations, num_steps) 的数组
    # 3. 对步数维度求和得到最终位移
    
    pass

def plot_displacement_distribution(final_displacements, bins=30):
    """
    绘制位移分布直方图

    参数:
    final_displacements (list): 包含每次模拟最终位移的列表
    bins (int): 直方图的组数
    """
    # TODO: 实现位移分布的直方图绘制
    # 1. 计算每次模拟的最终位移
    # 2. 使用plt.hist绘制直方图
    # 3. 添加标题和标签
    pass

def plot_displacement_square_distribution(final_displacements, bins=30):
    """
    绘制位移平方分布直方图

    参数:
    final_displacements (list): 包含每次模拟最终位移的列表
    bins (int): 直方图的组数
    """
    # TODO: 实现位移平方分布的直方图绘制
    # 1. 计算位移平方
    # 2. 使用plt.hist绘制直方图
    # 3. 添加标题和标签
    pass

if __name__ == "__main__":
    # 可调整的参数
    num_steps = 1000  # 随机行走的步数
    num_simulations = 1000  # 模拟的次数
    bins = 30  # 直方图的组数

    # TODO: 完成主程序逻辑
    # 1. 调用random_walk_displacement获取模拟结果
    # 2. 绘制位移分布直方图
    # 3. 绘制位移平方分布直方图

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

def plot_poisson_pmf(lambda_param=8, max_l=20):
    """绘制泊松分布的概率质量函数
    
    参数:
        lambda_param (float): 泊松分布参数λ
        max_l (int): 最大的l值
    """
    l_values = np.arange(max_l)
    pmf = (lambda_param**l_values * np.exp(-lambda_param)) / factorial(l_values)
    
    plt.figure(figsize=(10, 6))
    plt.plot(l_values, pmf, 'bo-', label='Theoretical Distribution')
    plt.title(f'Poisson Probability Mass Function (λ={lambda_param})')
    plt.xlabel('l')
    plt.ylabel('p(l)')
    plt.grid(True)
    plt.legend()
    return pmf

def simulate_coin_flips(n_experiments=10000, n_flips=100, p_head=0.08):
    """模拟多组抛硬币实验
    
    参数:
        n_experiments (int): 实验组数N
        n_flips (int): 每组抛硬币次数
        p_head (float): 正面朝上的概率
        
    返回:
        ndarray: 每组实验中正面朝上的次数
    """
    results = []  #记录硬币正面朝上的次数
    for i in range(n_experiments):
        coins = np.random.choice([0,1],n_flips, p=[1-p_head,p_head]) #抛硬币100次
        results.append(coins.sum())

    return np.array(results)

def compare_simulation_theory(n_experiments=10000, lambda_param=8):
    """比较实验结果与理论分布
    
    参数:
        n_experiments (int): 实验组数
        lambda_param (float): 泊松分布参数λ
    """
    # 进行实验模拟
    results = simulate_coin_flips(n_experiments)
    
    # 计算理论分布
    max_l = max(int(lambda_param * 2), max(results) + 1)
    l_values = np.arange(max_l)
    pmf = (lambda_param**l_values * np.exp(-lambda_param)) / factorial(l_values)
    
    # 绘制直方图和理论曲线
    plt.figure(figsize=(12, 7))
    plt.hist(results, bins=range(max_l+1), density=True, alpha=0.7, 
             label='Simulation Results', color='skyblue')
    plt.plot(l_values, pmf, 'r-', label='Theoretical Distribution', linewidth=2)
    
    plt.title(f'Poisson Distribution Comparison (N={n_experiments}, λ={lambda_param})')
    plt.xlabel('Number of Heads')
    plt.ylabel('Frequency/Probability')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # 打印统计信息
    print(f"实验均值: {np.mean(results):.2f} (理论值: {lambda_param})")
    print(f"实验方差: {np.var(results):.2f} (理论值: {lambda_param})")

if __name__ == "__main__":
    # 设置随机种子
    np.random.seed(42)
    
    # 1. 绘制理论分布
    plot_poisson_pmf()
    
    # 2&3. 进行实验模拟并比较结果
    compare_simulation_theory()
    
    plt.show()
