import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def update_position(event):
    if event.inaxes == ax:
        x = event.xdata
        y = event.ydata
        
        # Xử lý giá trị tọa độ chuột âm
        if x is not None and y is not None:
            z = np.sqrt(x**2 + y**2)
            if z != 0:
                # Tính toán góc quay theo tọa độ chuột âm
                angle = np.arctan2(y, x)
                new_x = z * np.cos(angle)
                new_y = z * np.sin(angle)
                new_z_cone = np.sqrt(new_x**2 + new_y**2)
                
                # Vẽ hình nón mới dựa trên tọa độ mới
                ax.clear()
                phi, theta = np.mgrid[0.0:0.5 * np.pi:100j, 0.0:2.0 * np.pi:100j]
                r = np.sin(phi) * new_z_cone
                x = r * np.cos(theta)
                y = r * np.sin(theta)
                z_cone = np.sqrt(x**2 + y**2)
                ax.plot_surface(x, y, z_cone, color='blue', alpha=0.5)
                
                # Vẽ trục tọa độ
                ax.quiver(0, 0, 0, 1, 0, 0, color='red', arrow_length_ratio=0.1)  # Trục x
                ax.quiver(0, 0, 0, 0, 1, 0, color='green', arrow_length_ratio=0.1)  # Trục y
                ax.quiver(0, 0, 0, 0, 0, 1, color='blue', arrow_length_ratio=0.1)  # Trục z
                
                plt.draw()

fig.canvas.mpl_connect('motion_notify_event', update_position)

plt.show()
