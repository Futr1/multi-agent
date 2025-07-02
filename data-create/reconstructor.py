"""
Reconstructor Agent: 负责将原始问题重写为检索意图
"""

def reconstruct_intent(question: str) -> str:
    """
    输入：原始问题
    输出：检索意图字符串
    """
    # 极简prompt模板
    prompt = f"Given a question, provide a knowledge search intent to help better retrieve the answer from external document.\nQuestion: {question}\nSearch Intent:"
    # 这里直接模拟返回（真实场景可用LLM生成）
    if "lebron james" in question.lower():
        return "LeBron James teams before Cleveland Cavaliers"
    return f"Search intent for: {question}"

if __name__ == "__main__":
    q = "who did lebron james play for before the cavaliers?"
    print(reconstruct_intent(q)) 