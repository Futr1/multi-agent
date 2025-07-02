import json
import os
from core.pipeline import multi_agent_pipeline
from agents.locator import locate_fact
from agents.generator import generate_answer

def train_short_trajectory(data_path):
    print("=== 短轨迹训练（单智能体） ===")
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for item in data:
        print(f"\n[ID: {item['id']}] 问题: {item['instruction']}")
        # 这里只演示Locator和Generator的单步能力
        if '<|Locator|>' in item['instruction']:
            # 模拟检索文档
            docs = [{"title": "LeBron James", "text": "LeBron James played for the Miami Heat before the Cavaliers."}]
            facts = locate_fact(item['instruction'], docs)
            print("[Locator] 定位结果:", facts)
        if '<|Generator|>' in item['instruction']:
            # 模拟定位到的事实
            facts = [{"title": "Ricky Martin", "fact": "He also acted on stage and on TV in Mexico.", "relevant": "true"}]
            answer = generate_answer(item['instruction'], facts)
            print("[Generator] 生成答案:", answer)


def train_long_trajectory(data_path):
    print("=== 长轨迹训练（多智能体协作） ===")
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for item in data:
        print(f"\n[ID: {item['id']}] 问题: {item['instruction']}")
        answer = multi_agent_pipeline(item['instruction'], verbose=True)
        print("[最终答案]", answer)

if __name__ == "__main__":
    # 运行短轨迹训练
    train_short_trajectory(os.path.join('data', 'short_trajectory.json'))
    # 运行长轨迹训练
    train_long_trajectory(os.path.join('data', 'long_trajectory.json')) 