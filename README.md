第一阶段： 数据构造
- 构建短轨迹和长轨迹数据集，标注每一步推理过程。
对应文件夹的data-create部分，data sample里面有样例数据

第二阶段：知识检索
- 用检索器检索知识库中检索相关文档用于意图识别

第三阶段： 多阶段训练
- 先用短轨迹数据训练基础能力，再用长轨迹数据训练多智能体协作能力。
- 原始Llama-2-7B（论文微调的基座模型） 
    ↓ (短轨迹训练)
SMART_Short_7B (单智能体)
    ↓ (长轨迹训练)  
SMART_7B (多智能体协作)

第四阶段：推理与应用
- 输入复杂问题，模型自动完成意图重构、检索、定位、生成等多阶段推理，输出最终答案。

SMART项目的核心是：用多智能体协作和轨迹学习的方法，让大模型具备复杂知识推理和多阶段任务协作能力，从而更好地解决知识密集型任务。
