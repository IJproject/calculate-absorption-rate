import os
import numpy as np
from scipy.constants import pi, c, h, k
from data_list import data_list

whole_energy = 390.1046951106533 #全輻射エネルギー
dir_path = '/absorption-spectrum-data/' #吸収スペクトルデータのディレクトリ

def calculate(data):

    # プランクの熱輻射公式
    def absorption_intensity(x):
        return (2 * h * c**2 / x**5) * (1 / (np.exp((h * c) / (x * k * 288)) - 1))

    #ファイルの読み込み
    material = data['material']
    # vertical_devisions = data['vertical_devisions']
    # file_name = material + '.txt'
    # with open(dir_path + file_name, 'r') as file:
    #     print("ファイル読み込み")

    # 積分条件
    number_of_divisions = 10000 #分割数
    lambda_start = 1 * 10 ** (-6) #積分範囲の下限
    lambda_finish = 2 * 10 ** (-5) #積分範囲の上限

    # 積分に用いる変数の準備
    wave_length = np.linspace(lambda_start, lambda_finish, number_of_divisions) #各微小領域の波長の配列
    dx = (lambda_finish - lambda_start) / number_of_divisions  #区間の幅

    # 区分求積
    amount_of_absorption = 0
    for i in range(number_of_divisions - 1):
        # 各微小領域の面積を計算して合計する
        amount_of_absorption += pi * (absorption_intensity(wave_length[i]) + absorption_intensity(wave_length[i+1])) / 2 * dx

    amount_of_absorption_rate = amount_of_absorption / whole_energy * 100

    # 計算結果の出力
    with open('result.txt', 'a') as file:
        file.write('「' + material + '」の吸収エネルギー割合：' + str(amount_of_absorption_rate) + '%' + '\n')
        file.write('「' + material + '」の地表への再放射割合：' + str(amount_of_absorption_rate / 2) + '%' + '\n\n')

if __name__ == '__main__':

    for data in data_list:
        calculate(data)