import os
import asyncio
from pathlib import Path
import google.generativeai as genai
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from watchfiles import awatch

# 加载.env文件中的环境变量
load_dotenv()

# 配置Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    # 在实际应用中，这里应该用更优雅的方式处理错误，例如日志记录
    print("错误：未在.env文件中找到GEMINI_API_KEY")
    # raise RuntimeError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)

app = FastAPI(title="QuickCaptureRAG Backend API")

# 定义截图文件存放的目录
# 注意：这里我们指向用户图片目录下的QuickCapture文件夹，与Tauri前端的设置保持一致
CAPTURE_DIR = Path.home() / "Pictures" / "QuickCapture"


async def watch_for_new_screenshots():
    """一个异步任务，用于监控指定目录中的新文件。"""
    print(f"开始监控目录: {CAPTURE_DIR}")
    # 确保目录存在
    CAPTURE_DIR.mkdir(parents=True, exist_ok=True)

    async for changes in awatch(CAPTURE_DIR):
        for change_type, path in changes:
            # 我们只关心新增的文件
            if change_type == 1:  # 1 corresponds to 'add'
                print(f"检测到新截图: {path}")
                # TODO: 在这里将文件路径添加到处理队列中
                # 例如: await add_to_processing_queue(path)


@app.on_event("startup")
async def startup_event():
    """在应用启动时，创建一个后台任务来监控文件。"""
    loop = asyncio.get_event_loop()
    loop.create_task(watch_for_new_screenshots())


@app.get("/")
def read_root():
    """根路由，用于检查服务是否正在运行。"""
    return {"message": "QuickCaptureRAG Backend is running."}


@app.get("/test-gemini", summary="测试与Gemini API的连接")
async def test_gemini_connection():
    """
    发送一个简单的请求到Gemini Pro模型，以验证API密钥和连接是否正常。
    """
    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="服务器错误：GEMINI_API_KEY未配置，无法测试连接。",
        )
    try:
        # 创建模型实例
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        # 发送一个简单的文本提示
        response = await model.generate_content_async(
            "你好, Gemini! 请确认你已收到此消息。"
        )
        return {"status": "success", "response": response.text.strip()}
    except Exception as e:
        # 捕获并返回任何在API调用期间发生的错误
        raise HTTPException(status_code=500, detail=f"连接Gemini API失败: {str(e)}")
