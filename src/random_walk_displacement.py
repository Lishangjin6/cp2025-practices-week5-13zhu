import numpy as np
import matplotlib.pyplot as plt


def random_walk_displacement(num_steps, num_simulations):
    """
    模拟随机行走并返回每次模拟的最终位移

    参数:
    num_steps (int): 随机行走的步数，必须大于0
    num_simulations (int): 模拟的次数，必须大于0

    返回:
    np.ndarray: 形状为(2, num_simulations)的数组，包含每次模拟在x和y方向的最终位移
    """
    if num_steps <= 0:
        raise ValueError("num_steps must be greater than 0")
    if num_simulations <= 0:
        raise ValueError("num_simulations must be greater than 0")

    # 生成随机方向数组，形状为(2, num_simulations, num_steps)
    directions = np.random.choice([-1, 1], size=(2, num_simulations, num_steps))
    # 对步数维度求和，得到每次模拟的最终位移
    final_displacements = directions.sum(axis=2)

    return final_displacements


def calculate_displacements(final_displacements):
    """
    计算每次模拟的总位移

    参数:
    final_displacements (np.ndarray): 形状为(2, num_simulations)的数组，包含每次模拟在x和y方向的最终位移

    返回:
    np.ndarray: 包含每次模拟总位移的数组
    """
    return np.sqrt(final_displacements[0] ** 2 + final_displacements[1] ** 2)


def calculate_displacements_square(final_displacements):
    """
    计算每次模拟的总位移的平方

    参数:
    final_displacements (np.ndarray): 形状为(2, num_simulations)的数组，包含每次模拟在x和y方向的最终位移

    返回:
    np.ndarray: 包含每次模拟总位移平方的数组
    """
    return final_displacements[0] ** 2 + final_displacements[1] ** 2


def plot_distribution(data, title, xlabel, ylabel, bins=30):
    """
    绘制分布直方图

    参数:
    data (np.ndarray): 要绘制直方图的数据
    title (str): 直方图的标题
    xlabel (str): x轴标签
    ylabel (str): y轴标签
    bins (int): 直方图的组数
    """
    plt.hist(data, bins=bins, density=True, alpha=0.7, color='b')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # 可调整的参数
    num_steps = 1000  # 随机行走的步数
    num_simulations = 1000  # 模拟的次数
    bins = 30  # 直方图的组数

    try:
        # 模拟随机行走
        displacements = random_walk_displacement(num_steps, num_simulations)

        # 计算总位移
        total_displacements = calculate_displacements(displacements)
        # 绘制位移分布直方图
        plot_distribution(total_displacements, 'Random Walk Displacement Distribution',
                          'Final Displacement', 'Probability Density', bins)

        # 计算总位移的平方
        total_displacements_square = calculate_displacements_square(displacements)
        # 绘制位移平方分布直方图
        plot_distribution(total_displacements_square, 'Random Walk Displacement Square Distribution',
                          'Final Displacement Square', 'Probability Density', bins)
    except ValueError as e:
        print(e)
