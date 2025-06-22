import open3d as o3d

# 读取点云
pcd = o3d.io.read_point_cloud("output2/point_cloud/iteration_7000/point_cloud.ply")

# 计算法线（如果点云没有法线，可以估计一下）
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))

# 创建可视化窗口
vis = o3d.visualization.Visualizer()
vis.create_window(window_name="高级点云展示", width=1280, height=720)
vis.add_geometry(pcd)

# 设置点云颜色
pcd.paint_uniform_color([0.1, 0.7, 0.1])  # 亮亮的绿

# 修改渲染选项
opt = vis.get_render_option()
opt.background_color = [0, 0, 0]          # 背景黑色
opt.point_size = 3.0                      # 点大小
opt.show_coordinate_frame = True          # 显示坐标轴
opt.light_on = True                       # 开启光照
opt.mesh_show_back_face = True

# 运行可视化窗口
vis.run()
vis.destroy_window()


