import matplotlib.pyplot as plt
# 在绘图之前,我们需要一个figure对象作为画板
# fig = plt.figure()
# Axes,绘图基准(轴),相当于画纸,在画板上的画纸上画
# ax = fig.add_subplot(111)
"""
在画板的第1行第1列的第1个位置作画,fig.add_subplot(2, 2, 1)的方式生成Axes,2,2确定了画板的划分,1表是第一个Axes
需要一次生成每个Axes:
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(224)
Multiple Axes
一次性生成所有Axes:
fig, axes = plt.subplots(nrows = 2, ncols = 2)
axes[0, 0].set(title = 'Upper Left')
axes[0, 1].set(title = 'Upper Right')
axes[1, 0].set(title = 'Lower Left')
axes[1, 1].set(title = 'Lower Right')
"""
# ax.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='An Example Axes',
#        ylabel='Y-Axis', xlabel='X-Axis')
plt.plot([1,2,3,4], [10,20,25,30], color="lightblue", linewidth=3)
plt.xlim(0.5, 4,5)
plt.show()
x = np.linspace