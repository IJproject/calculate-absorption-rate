import numpy as np

# 積分条件
number_of_divisions = 10000
integral_start_value = 0 
integral_finish_value = 20

wave_length = np.linspace(integral_start_value, integral_finish_value, number_of_divisions)

def absorption_intensity(x):
    return x**2

def absorption_rate(x):
    return x

# Numpyを使用して積分計算
amount_of_absorption = np.trapz(absorption_rate(wave_length) * absorption_intensity(wave_length), wave_length)


if __name__ == '__main__':
    print('積分計算結果: ', amount_of_absorption)
    print('PyCharm')