# QuickCaptureRAG 智能知识库

QuickCaptureRAG 是一个基于 Tauri + React + Python FastAPI 构建的本地化智能知识库应用。它旨在帮助用户快速捕捉、存储和检索多模态信息（文本、图片等），并通过 RAG (Retrieval-Augmented Generation) 技术提供智能问答能力。

本项目 `DemoV1` 版本旨在跑通核心流程，实现基础的文本知识录入和问答功能。

## ✨ 功能特性

- **快速知识捕捉**: 支持快速录入文本、图片等多种格式的资料。
- **本地化存储**: 所有数据存储在本地，使用 ChromaDB 进行向量化管理，确保数据隐私和安全。
- **智能问答**: 基于存储的知识内容，提供精准、高效的问答体验。
- **多模态支持**: 采用 Jina Embeddings v4 嵌入模型，具备处理文本和图像的统一能力，为未来的图文混合检索奠定基础。
- **跨平台桌面应用**: 基于 Tauri 构建，可打包为 Windows, macOS 和 Linux 桌面应用。

## 🛠️ 技术栈

- **前端**: `React`, `TypeScript`, `Vite`, `Tauri`
- **后端**: `Python`, `FastAPI`
- **向量数据库**: `ChromaDB`
- **嵌入模型**: `Jina Embeddings v4` (多模态)

## 📂 项目结构

```
QuickCaptureRAG/
├── app-backend/        # Python FastAPI 后端
├── app-frontend/       # React + Tauri 前端
├── data/               # ChromaDB 数据库文件
├── docs/               # 项目文档 (包括PRD、设计文档等)
├── .env.example        # 环境变量示例文件
├── install-deps.bat    # 依赖安装脚本
├── start-dev.bat       # 开发环境启动脚本
└── stop-dev.bat        # 开发环境停止脚本
```

## 🚀 快速开始 (DemoV1)

请按照以下步骤在本地安装和运行本项目。

### 1. 环境准备

- [Node.js](https://nodejs.org/en/) (v18 或更高版本)
- [Python](https://www.python.org/) (v3.10 或更高版本)
- [Rust](https://www.rust-lang.org/) (Tauri 打包需要)

### 2. 克隆项目

```bash
git clone <your-repository-url>
cd QuickCaptureRAG
```

### 3. 配置环境变量

复制 `.env.example` 文件并重命名为 `.env`。

```bash
copy .env.example .env
```

根据需要修改 `.env` 文件中的配置，例如 API Keys 等（如果未来需要）。

### 4. 安装依赖

直接运行根目录下的依赖安装脚本。该脚本会自动安装前端和后端的全部依赖。

```bash
.\install-deps.bat
```

### 5. 运行 DemoV1

运行开发环境启动脚本，它会同时启动 FastAPI 后端服务和 Tauri 前端应用。

```bash
.\start-dev.bat
```

成功启动后，Tauri 桌面应用窗口将会自动弹出。

### 6. 停止服务

当你需要停止所有正在运行的开发服务时，执行以下脚本：

```bash
.\stop-dev.bat
```

---
欢迎对本项目进行贡献！如有任何问题，请提交 Issue。
