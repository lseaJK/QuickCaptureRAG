# CONSENSUS - QuickCaptureRAG DemoV1

本文档基于 `ALIGNMENT_DemoV1.md` 的内容，固化了 Demo V1 的最终需求和技术方案，作为后续开发阶段的唯一基准。

## 1. 需求描述 (Requirement Description)

开发一个功能可用的最小可行性产品 (MVP)，验证从 **截图** 到 **AI处理**，再到 **知识库问答** 的核心链路。用户可以通过客户端界面触发截图，系统自动分析截图内容并存入本地知识库，随后用户可以针对知识库内容进行提问。

## 2. 技术实现方案 (Technical Implementation Plan)

- **客户端 (Client):** Tauri + React
- **服务端 (Server):** Python + FastAPI
- **AI 核心 (AI Core):**
  - **多模态嵌入 (Multimodal Embedding):** Jina Embeddings v4 (输入图片，输出图片嵌入和文本描述)
  - **问答生成 (Answer Generation):** Google Gemini 2.5 Pro API
- **向量数据库 (Vector DB):** ChromaDB (本地文件存储)
- **结构化数据存储 (Structured Data):** 本地 SQLite 数据库
- **RAG 框架 (RAG Framework):** LlamaIndex

## 3. 核心功能流程 (Core Functional Flow)

1.  **触发:** 用户在 Tauri 客户端点击“截图”按钮。
2.  **捕获:** 客户端完成截图，并将图像数据发送到 FastAPI 后端。
3.  **处理:**
    - 后端接收图像，调用 **Jina Embeddings v4** API。
    - Jina API 对图像进行分析，一次性返回该图像的**文本描述**和对应的**向量嵌入 (Embeddings)**。
4.  **存储:**
    - Jina 返回的文本描述和元数据存入本地 SQLite 数据库。
    - Jina 返回的向量嵌入存入本地 ChromaDB。
5.  **查询:**
    - 用户在客户端输入问题。
    - 后端调用 **Jina Embeddings v4** 模型，生成问题的文本向量嵌入。
    - 使用此嵌入在 ChromaDB 中进行相似度搜索，检索相关知识（即，之前由Jina生成的文本描述）。
6.  **响应:**
    - 将检索到的知识与原始问题一同发送给 **Gemini 2.5 Pro API**，生成最终回答。
    - 将回答返回给客户端展示。

## 4. 任务边界与验收标准 (Task Boundaries & Acceptance Criteria)

### 任务边界 (In Scope)

- 实现上述核心功能流程。
- 客户端提供一个截图按钮和一个问答界面。
- API Key 通过根目录下的 `.env` 文件进行配置。

### 范围之外 (Out of Scope)

- 全局快捷键截图。
- 任务队列与后台处理。
- 文件智能重命名、快速标签系统。
- 对话式追问、历史对话管理。
- 用户账户系统。

### 验收标准 (Acceptance Criteria)

- 用户可以成功完成一次截图到知识库的存储。
- 用户针对已存储的截图内容提问，能够得到相关的、由AI生成的回答。
- 整个流程无明显崩溃或错误。

## 5. 关键配置 (Key Configuration)

- **Gemini API Key:** 必须在项目根目录的 `.env` 文件中配置 `GEMINI_API_KEY` 变量。
