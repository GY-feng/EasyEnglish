import cv2
import numpy as np

class PictureCutting:
    def __init__(self,pic_path):
        '''
        :param pic_path: 需要被切割并且转化的地址
        '''
        self.path=pic_path
        pass
    def recognize_cutting(self,color='yellow'):
        '''
        实现图像的自动识别黄色颜色块，并且切割成小块
        :param color:暂时只能设置成黄色，后期可以增加其他的颜色选择
        :return: 返回切割后的地址
        '''
        # 读取图像
        image = cv2.imread(self.path)

        # 转换为 HSV 颜色空间
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # 定义黄色范围
        lower_color = np.array([20, 100, 100])  # 低阈值
        upper_color = np.array([30, 255, 255])  # 高阈值

        # 创建掩模
        mask = cv2.inRange(hsv, lower_color, upper_color)
        filename= '../../../mask.png'
        cv2.imwrite(filename, mask)
        return filename
