from agents.reconstructor import reconstruct_intent
from core.retriever import retrieve_documents
from agents.locator import locate_fact
from agents.generator import generate_answer


def multi_agent_pipeline(question: str, verbose=True):
    """
    多智能体推理主流程
    输入：原始问题
    输出：最终答案和推理轨迹
    """
    # 1. 意图重构
    intent = reconstruct_intent(question)
    if verbose:
        print(f"[Reconstructor] intent: {intent}")
    # 2. 检索
    docs = retrieve_documents(intent)
    if verbose:
        print(f"[Retriever] docs: {docs}")
    # 3. 事实定位
    facts = locate_fact(question, docs)
    if verbose:
        print(f"[Locator] facts: {facts}")
    # 4. 答案生成
    answer = generate_answer(question, facts)
    if verbose:
        print(f"[Generator] answer: {answer}")
    return answer

if __name__ == "__main__":
    q = "who did lebron james play for before the cavaliers?"
    print("Final Answer:", multi_agent_pipeline(q)) 