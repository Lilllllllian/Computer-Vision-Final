# Computer-Vision-Final
Final Project for CV
## 环境说明

本项目在 [Autodl](https://www.autodl.com) 平台上完成，针对三种方法分别配置了独立运行环境：

###  [Instant-NGP](https://github.com/NVlabs/instant-ngp)
- 基于作者提供的 **CUDA 加速版本**
- 使用 **TurboVNC 打开远程桌面** 进行 GUI 操作
- 推荐环境：
  - 操作系统：Ubuntu 20.04
  - CUDA：11.4+
  - Python：3.8
  - CMake：3.18+
  - 显卡要求：Compute Capability ≥ 7.0（本项目使用 **RTX 3090**）

###  [TensorRF](https://github.com/ashawkey/Tensorf)
- 使用自定义镜像：`image-2f4eece27b`
- 系统配置：
  - 操作系统：Ubuntu 20.04
  - Python：3.8
  - PyTorch：1.11.0
  - CUDA：11.3
- 显存占用：最大约 **10.18 GB**

###  [3D Gaussian Splatting](https://github.com/graphdeco-inria/gaussian-splatting)
- 使用镜像：`image-8c0b7e9d3e`
- 系统配置：
  - 操作系统：Ubuntu 20.04
  - Python：3.8
  - PyTorch：2.0.0
  - CUDA：11.8
- 训练过程依赖：`TensorBoard`、`Open3D` 等可视化组件

---

### Autodl 镜像概览

| 方法                    | GitHub 项目链接                                                                 | 镜像名称          | 操作系统     | Python | PyTorch | CUDA  | 显存占用     |
|-------------------------|----------------------------------------------------------------------------------|------------------|--------------|--------|---------|--------|--------------|
| Instant-NGP             | [NVlabs/instant-ngp](https://github.com/NVlabs/instant-ngp)                     | —                | Ubuntu 20.04 | 3.8    | —       | 11.4+  | —            |
| TensorRF                | [ashawkey/Tensorf](https://github.com/ashawkey/Tensorf)                         | `image-2f4eece27b` | Ubuntu 20.04 | 3.8    | 1.11.0  | 11.3   | 约 10.18 GB  |
| 3D Gaussian Splatting   | [graphdeco-inria/gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting) | `image-8c0b7e9d3e` | Ubuntu 20.04 | 3.8    | 2.0.0   | 11.8   | —            |

---

如需环境复现，请确保系统满足上述配置要求，或直接使用 Autodl 上的预设镜像运行代码。
