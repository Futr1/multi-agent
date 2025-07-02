"""
Retriever: 简化版知识检索器
"""
def retrieve_documents(intent: str) -> list:
    """
    输入：检索意图字符串
    输出：文档列表（每个元素为dict: {title, text}）
    """
    # 极简模拟：根据intent返回固定文档
    if "lebron james" in intent.lower():
        return [{
            "title": "LeBron James",
            "text": "LeBron James played for the Miami Heat before the Cavaliers."
        }]
    return [{
        "title": "Unknown",
        "text": "No relevant document found."
    }]

if __name__ == "__main__":
    print(retrieve_documents("LeBron James teams before Cleveland Cavaliers")) 