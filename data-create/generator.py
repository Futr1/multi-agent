"""
Generator Agent: 负责根据定位到的事实生成最终答案
"""
def generate_answer(question: str, facts: list) -> str:
    """
    输入：问题，定位到的事实列表（每个元素为dict: {title, fact, relevant}）
    输出：最终答案字符串
    """
    # 极简生成逻辑：返回第一个相关事实
    for f in facts:
        if f['relevant'] == 'true':
            return f["fact"]
    return "No relevant answer found."

if __name__ == "__main__":
    q = "who did lebron james play for before the cavaliers?"
    facts = [{"title": "LeBron James", "fact": "LeBron James played for the Miami Heat before the Cavaliers.", "relevant": "true"}]
    print(generate_answer(q, facts)) 