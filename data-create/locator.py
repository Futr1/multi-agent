"""
Locator Agent: 负责判断文档与问题的相关性并提取事实
"""
def locate_fact(question: str, docs: list) -> list:
    """
    输入：问题，检索到的文档列表（每个元素为dict: {title, text}）
    输出：相关性判断和事实列表
    """
    results = []
    for doc in docs:
        # 极简相关性判断逻辑
        if any(word in doc['text'].lower() for word in question.lower().split()):
            results.append({
                'title': doc['title'],
                'fact': doc['text'][:100],  # 截取前100字作为事实
                'relevant': 'true'
            })
        else:
            results.append({
                'title': doc['title'],
                'fact': 'Lacking Supporting Facts',
                'relevant': 'false'
            })
    return results

if __name__ == "__main__":
    q = "who did lebron james play for before the cavaliers?"
    docs = [{"title": "LeBron James", "text": "LeBron James played for the Miami Heat before the Cavaliers."}]
    print(locate_fact(q, docs)) 