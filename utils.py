from meilisearch import Client

# 你的 Meilisearch 配置
MEILI_URL = "http://192.168.31.13:7700"
MEILI_API_KEY = "rzHvvVSus8cu_jgZ1UuXB5SyfXAGeSUMIlITMov9uig"  # 如果你启用了 API 密钥，请填写

MEILI_INDEX = "articles"  # 索引名称，需要预先创建并导入数据

client = Client(MEILI_URL, MEILI_API_KEY)

def search_documents_by_keywords(keywords: str, limit: int = 5):
    """
    使用关键词（以空格分隔）在 Meilisearch 中执行全文搜索。对于重要的关键词，应该在关键词左右两边加上英文双引号，这表示只有一定出现这个关键词的文章才会返回
    """
    index = client.index(MEILI_INDEX)
    params = {
        'attributesToCrop': ['content'],
        'cropLength': 1000,  # 裁剪内容长度为1000个词
        "limit": limit
    }
    result = index.search(keywords, params)

    hits = result.get("hits", [])
    formatted_results = []
    for hit in hits:
        if '_formatted' in hit and 'content' in hit['_formatted']:
            formatted_results.append({
                "title": hit['_formatted'].get('title', "无标题"),
                "content": hit['_formatted']['content']
            })
        elif 'content' in hit:
            formatted_results.append({
                "title": hit.get("title", "无标题"),
                "content": hit["content"]
            })
    return formatted_results
