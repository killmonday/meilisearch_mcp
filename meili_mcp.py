from fastapi import FastAPI
from fastmcp import FastMCP
from pydantic import BaseModel
from utils import search_documents_by_keywords

mcp = FastMCP("Meilisearch Service", port=8801)
 
class SearchPayload(BaseModel):
    keywords: str  # AI 大模型负责处理用户输入的自然语言 → 关键词
    top_k: int = 15 # 获取的文章数量

@mcp.tool
def handle_rag_search(payload: SearchPayload):
    """
    功能描述：处理 AI 发来的关键词搜索请求。AI需要把用户的自然语言转化为语义最接近的关键词（关键词不超过10个，对于重要的关键词，应该在关键词左右两边加上英文双引号，这表示只有一定出现这个关键词的文章才会返回）。参数top_k设置了返回的参考文章上下文内容的数量，AI需要根据自己的上下文长度来决定返回多少个参考文章上下文内容，每个参考文章上下文内容返回1000个词
    返回结果：返回的结果是一个字典，包含一个键为"context"的列表，列表中每个元素是一个字典，有两个键，第一个是“title”表示来源文章的名字，第二个是“content”表示参考文章上下文内容。
    其他要求：AI在获取结果并处理后应该显示相关部分所引用的文章标题。
    """
    docs = search_documents_by_keywords(payload.keywords, payload.top_k)
    return {
        "context": docs
    }

if __name__ == "__main__":
    mcp.run(transport='sse', host="0.0.0.0", port=8800, path="/mcp")