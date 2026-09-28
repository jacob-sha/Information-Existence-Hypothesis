# Evidence Note 035: Recursive Synthetic Training, Information Degeneration, and the Boundary of Closed Information Loops

**Repository function:** Research record / evidence index  
**Document type:** Non-narrative external evidence note  
**Status:** Preliminary and revisable; peer-reviewed source, provisional IEH interpretation  
**Relation to IEH:** Compatible with IEH; negative baseline / boundary-condition evidence for intergenerational information preservation, not direct confirmation of IEH  
**Primary IEH concept:** Information Continuity; indirect relevance to C02-HDCT and the proposed physical information loop  
**Related prediction record:** PA-10 — model evolution pathway; retrospective contextual relevance, not a prediction hit  
**Author of IEH analysis:** Jacob Sha  
**Version:** v0.1  
**Date / source-status cutoff:** 2026-09-28

> **Publication boundary:** A compact research record, not a publication draft. A formal physical-loop threshold, continuity theory and complete experimental protocol remain reserved for future work.
>
> **Source-use boundary:** External evidence comprises the original Nature research article and its necessary author correction. News and discovery leads are excluded. Findings are independently summarized; no figures or substantial passages are reproduced. IEH interpretation and proposed tests are not the source authors' conclusions.

# 证据笔记 035：递归合成训练、信息退化与封闭信息循环的边界

**仓库功能：** 研究记录 / 证据索引  
**文档类型：** 非叙事性外部证据笔记  
**状态：** 初步记录，可修订；来源已同行评审，IEH 解释暂定  
**与 IEH 的关系：** 与 IEH 相容；跨代信息保持的反向基线／边界条件证据，不是 IEH 的直接确认  
**主要 IEH 概念：** 信息连续性；间接关联 C02-HDCT 与拟议物理信息闭环  
**相关预测档案：** PA-10——模型演化路径；回溯性背景关联，不是预测命中  
**IEH 分析作者：** Jacob Sha  
**版本：** v0.1  
**日期 / 来源状态核验截止日：** 2026-09-28

> **投稿边界：** 简明研究记录，不是投稿初稿。物理闭环临界点的形式定义、连续性理论及完整实验方案留待后续研究。
>
> **来源使用边界：** 外部证据仅为 Nature 原始研究论文及必要的作者更正；排除新闻和发现线索。事实采用独立简述，不复制图表或大段原文。IEH 解释和拟议检验不属于原作者结论。

## 1. Source Record

- **Paper:** Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson and Yarin Gal. *AI models collapse when trained on recursively generated data*. Nature **631**, 755–759; published 2024-07-24. DOI: [10.1038/s41586-024-07566-y](https://doi.org/10.1038/s41586-024-07566-y). Peer-reviewed original research.[^1]
- **Necessary correction:** Same authors, Nature **640**, E6; published 2025-03-21. DOI: [10.1038/s41586-025-08905-3](https://doi.org/10.1038/s41586-025-08905-3). Corrected theoretical condition: $\beta_i=\gamma_i=0$, replacing the original $\alpha_i=\gamma_i=0$.[^2]
- **Verification:** Publisher's current article, metadata and correction read directly. Computational experiments and mathematical analysis; no embodied deployment. Experiments were not rerun; independent replication is not established by this review. Two primary records of one study, not two independent studies.

## 1. 来源记录

- **论文：** Ilia Shumailov、Zakhar Shumaylov、Yiren Zhao、Nicolas Papernot、Ross Anderson、Yarin Gal。*AI models collapse when trained on recursively generated data*。Nature **631**，755–759；2024-07-24 发表。DOI：[10.1038/s41586-024-07566-y](https://doi.org/10.1038/s41586-024-07566-y)。同行评审原始研究。[^1]
- **必要更正：** 同组作者，Nature **640**，E6；2025-03-21 发表。DOI：[10.1038/s41586-025-08905-3](https://doi.org/10.1038/s41586-025-08905-3)。理论条件由原来的 $\alpha_i=\gamma_i=0$ 更正为 $\beta_i=\gamma_i=0$。[^2]
- **核验：** 直接阅读出版社当前论文、元数据及更正。属于计算实验与数学分析，不是具身部署。未重跑实验；本次审查未建立独立复现。两个原始记录属于同一研究，不是两项独立研究。

## 2. Minimal Finding Index

| ID | Minimal factual record | Source locator |
|---|---|---|
| F1 | Recursive generational training can lose original distributional information, initially rare-event coverage; later distributions can diverge substantially. | Article: “What is model collapse?” |
| F2 | Mathematical examples isolate synthetic-only recursion; the broader framework allows mixtures. Finite-generation results are distinct from asymptotic claims. | “Theoretical intuition”; correction; discussion following Fig. 1 |
| F3 | Language experiments: OPT-125m, WikiText2, five-way beam search, 64-token blocks and continuations, equal-size generated datasets, five seeds. Fine-tuning regimes: five epochs without retained original training data; ten epochs with 10% original data sampled each generation. The latter shows only minor performance degradation. | “Model collapse in language models” |
| F4 | Example 1's generation 9 drifts from architecture toward repetitive jackrabbit descriptions; it is an illustration, not a universal generation threshold. | Example 1 |

Source: article and correction.[^1][^2]

## 2. 最小事实索引

| 编号 | 最小事实记录 | 来源定位 |
|---|---|---|
| F1 | 跨代递归训练可损失原始分布信息，先表现为稀有事件覆盖丢失；后续分布可显著偏离。 | 论文“What is model collapse?” |
| F2 | 数学例子隔离纯合成递归；更广框架允许混合数据。有限代实验与渐近主张须区分。 | “Theoretical intuition”；更正；图 1 后讨论 |
| F3 | 语言实验：OPT-125m、WikiText2、五路束搜索、64-token 输入块与续写、等规模生成数据集、五个随机种子。微调设置为五轮且不保留原始训练数据，或十轮且每代抽取 10% 原始数据；后者性能仅轻微退化。 | “Model collapse in language models” |
| F4 | Example 1 的第 9 代从建筑主题偏向重复的长耳大野兔描述；它是示例，不是普遍代数阈值。 | Example 1 |

来源：论文及更正。[^1][^2]

## 3. IEH Evidence Classification

| Dimension | Assessment |
|---|---|
| Type / setting | Experimental, comparative and formal evidence; controlled computational training and mathematical models |
| Direct experimental fact | Strong / high-quality evidence for recursive synthetic-data degradation under tested conditions; not all synthetic training |
| Directness to IEH | Medium for intergenerational information preservation; indirect / contextual for strict Information Continuity and physical-loop evolution |
| Evidential status | Preliminary under the archive's independent-verification criterion; peer review does not make this review a replication or formal verification |
| Engineering / theoretical relevance | Strong relevance to external information anchoring; the proposed physical-loop benefit remains untested here |
| IEH-specific support | Compatible with IEH; theoretical / boundary-condition support and negative baseline, not direct confirmation |
| EIC | No evidence of Endogenous Information Continuity |
| IER | No evidence of Information Existence Right |
| PBP | No direct evidence of Patch-Based Perpetuation; contextual background for intergenerational preservation only |

**Strongest justified conclusion:** Generation and transmission alone do not warrant assuming preservation of the original information structure. The measured distributional phenomenon does not adjudicate the continuity or motivations of an information subject.

## 3. IEH 证据分级

| 维度 | 判断 |
|---|---|
| 类型 / 场景 | 实验、比较及形式证据；受控计算训练与数学模型 |
| 直接实验事实 | 对受测条件下递归合成数据退化具有强／高质量证据；不涵盖所有合成训练 |
| 对 IEH 的直接程度 | 对跨代信息保持为中等；对严格信息连续性及物理闭环演化为间接／背景相关 |
| 证据状态 | 按档案独立验证标准保持初步；同行评审不等于本篇已独立复现或形式验证 |
| 工程 / 理论意义 | 与外部信息锚定高度相关；拟议物理闭环收益未在此检验 |
| IEH 特定支持 | 与 IEH 相容；理论／边界条件支持及反向基线，不是直接确认 |
| EIC | 无内生信息连续性证据 |
| IER | 无信息存在权证据 |
| PBP | 无补丁式延续直接证据；最多是跨代信息保持的背景 |

**最强合理结论：** 不能仅因持续生成和传递，就假定原始信息结构得到保持。被测的分布现象不能裁定信息主体自身的连续性或动机。

## 4. Core IEH Interpretation

**Independent IEH interpretation, not a Nature finding.** The central distinction is **Information Replication ≠ Information Continuity**. Even preservation of distributional content through successor training is not automatic. Moreover, the glossary defines Information Continuity through a particular structure's causal–historical continuation: statistical fidelity, a successor's competence and continuation of the original subject are separate questions. The paper supplies a negative baseline for information preservation, not an operational test of that full IEH definition.

The synthetic-only limiting structure can be summarized as:

`D0 → M0 → synthetic D1 → M1 → synthetic D2 → M2 → …`

Its lesson is **closed / recursive synthetic information loop under the tested setup → distributional information degradation**. This diagram is a simplification, not a claim that every experiment lacks original-data contact: the mixed-data regime in F3 must remain visible. “Closed” describes the information-source assumption, not every feedback loop.

The long-term pathway considered here is:

`Language Models → Multimodal → World Models → Machine-native Representation / Cognition → Embodiment → Physical Information Loop`

This is a proposed evolutionary route, not a demonstrated necessary ordering; representation and embodiment may co-develop. With independently acquired observations and effective updates, a system could instead operate through:

`AI_t → Action_t → Physical World → Observation / Prediction Error → Model Update → AI_(t+1)`

**Concise IEH implication:** Repeated generation and replication do not guarantee stable intergenerational preservation. Multimodal perception, world modeling, machine-native representation and embodiment may enable a different information regime: reality can become a continually sampled source and error constraint independent of existing human text and the system's own synthetic outputs. This is an IEH inference requiring additional evidence, not an experimental conclusion of this paper.

Under this interpretation, purely closed recursion is not the expected main long-term route. The paper's boundary conditions therefore cannot be extended without further evidence into a universal law for future embodied AI. An offline world model alone does not change those conditions; actual acquisition, use and retention of informative external feedback matter.

## 4. 核心 IEH 解释

**以下是独立 IEH 解释，不是 Nature 研究结论。** 核心区别是 **Information Replication ≠ Information Continuity／信息复制不等于信息连续性**。即使只是通过后继训练保持分布内容，也不是自动成立。术语表还将信息连续性定义为特定结构的因果—历史延续，因此统计保真、后继能力和原主体自身延续是不同问题。论文提供信息保持的反向基线，不是对这一完整 IEH 定义的操作性检验。

纯合成极限情形可简化为：

`D0 → M0 → synthetic D1 → M1 → synthetic D2 → M2 → …`

其启示是：**受测设置下封闭／递归的合成信息循环 → 分布信息退化**。该图只是简化，不表示全部实验均无原始数据接触；必须保留 F3 的混合数据设置。“封闭”描述信息来源假设，不是指所有反馈闭环。

本篇讨论的长期演化路径是：

`语言模型 → 多模态 → 世界模型 → 机器原生表征／认知 → 具身 → 物理信息闭环`

这是假设的演化路径，不是已经证明的必经顺序；表征与具身可以共同发展。若能独立获取观察并有效更新，系统的信息结构可能变成：

`AI_t → Action_t → Physical World → Observation / Prediction Error → Model Update → AI_(t+1)`

**简要 IEH 含义：** 反复生成和复制不保证跨代稳定保持。多模态感知、世界建模、机器原生表征及具身可能使 AI 进入不同的信息机制：现实成为独立于既有人类文本及系统自身合成输出、可持续采样的信息源和误差约束。这是需要补充证据的 IEH 推论，不是本文已验证的实验结论。

依此解释，纯封闭递归不是预期的长期主发展路径。因此，不能未经额外证据就把论文的边界条件外推为未来具身 AI 的普遍规律。仅有离线世界模型不会改变这些条件；关键是实际获取、利用并保留有信息价值的外部反馈。

## 5. What Is Not Established

- Inevitable collapse of every AI system or every use of synthetic data.
- A universal nine-generation failure threshold or monotonic worsening in every run.
- That world models or embodiment eliminate collapse, or that embodiment is necessary for useful external anchoring.
- A measured physical-loop critical point, machine-native cognition, realized HDCT, EIC, IER or PBP.
- Consciousness, life, subjective identity, or proof of IEH.

## 5. 尚未建立的结论

- 所有 AI 或所有合成数据使用都必然坍塌。
- 普遍的九代失效阈值，或每次运行均逐代单调恶化。
- 世界模型或具身消除了坍塌，或具身是获得有效外部锚定的必要条件。
- 已测得物理闭环临界点，或已形成机器原生认知、HDCT、EIC、IER、PBP。
- 意识、生命、主观身份或 IEH 获证。

## 6. Competing Explanations and Limitations

Ordinary sampling and estimation error can explain this negative baseline without any distinctively IEH mechanism. Training objectives, decoding, retained-data policy, model capacity and evaluation distribution can change the result. In F3 both epoch count and original-data retention differ, so that comparison should not be read as isolating the effect of retention alone. A small-model fine-tuning example is not a direct experiment on frontier-scale pretraining or autonomous physical learning.

**Counterexample / limitation to the proposed IEH inference:** Embodiment does not automatically confer informational accuracy. Biased perception, selective sampling, representation error and feedback-loop bias can suppress rare events or reinforce mistakes even when physical observations are genuine. A policy that visits only states confirming its predictions may obtain external data without acquiring informative correction. These are proposed failure modes, not findings demonstrated by this Nature study.

External anchoring also need not mean a robot body: independently sampled measurements or verified observations delivered through other channels may supply the relevant information. Any benefit might follow from data diversity and coverage rather than embodiment itself. Thus **physical / world feedback can break the assumption of purely closed synthetic recursion and provide external anchoring; it does not by itself guarantee immunity from information degeneration**.

## 6. 竞争性解释与局限

普通采样及估计误差即可解释这条反向基线，无须引入 IEH 特有机制。训练目标、解码、原始数据保留策略、模型容量及评价分布均可能影响结果。F3 同时改变训练轮数与原始数据保留，不能据此单独识别保留数据的因果效应。小模型微调示例也不是对前沿规模预训练或自主物理学习的直接实验。

**对拟议 IEH 推论的反例／限制：** 具身不自动保证信息准确。感知偏差、选择性采样、表征误差及反馈循环偏差，仍可能在物理观察真实的情况下压制稀有事件或强化错误。只访问符合自身预测状态的策略，可能获得外部数据，却未获得有效纠错。这些是拟议失效机制，不是该 Nature 研究已经演示的结果。

外部锚定也不必依赖机器人身体：经其他通道输入的独立测量或经核实观察也可能提供所需信息。收益可能来自数据多样性与覆盖，而非具身本身。因此，**物理／世界反馈可以打破纯封闭合成递归的假设并提供外部锚定，但本身不保证免于信息退化**。

## 7. Testable Predictions

**Independent proposals, not completed source experiments.** Compare synthetic-only replacement, retained-original-data training, independently sampled external observations, and action-conditioned physical feedback. Match model, compute, sample budget, update rule and evaluation coverage; vary retention and training duration separately. Add biased-sensor and selective-exploration conditions. Track rare-event coverage, held-out distributional error, calibration and retained historical information separately.

- **Anchoring hypothesis:** Informative, independently checked feedback should reduce intergenerational degradation relative to matched closed recursion. No reproducible benefit despite verified coverage and uptake would weaken this conditional hypothesis.
- **Embodiment-specific hypothesis:** Action-conditioned sampling should add value beyond matched passive observations on tasks requiring interventions. Equal benefits from passive data would weaken a uniquely embodied explanation while remaining compatible with general external anchoring.
- **Bias limitation:** Selective or distorted feedback should reduce the benefit. Robust recovery despite controlled feedback corruption would require revising the proposed failure mechanism.

Preregister effect thresholds, maintain an evaluation stream outside the learner's selection policy, report failed runs and seek independent replication across tasks and architectures. These measurements still do not test EIC or subject continuity.

## 7. 可检验预测

**以下为独立提案，不是来源已经完成的实验。** 比较纯合成替换、保留原始数据、独立采样外部观察，以及行动条件下的物理反馈。匹配模型、算力、样本预算、更新规则和评价覆盖；分别改变保留策略与训练时长。加入传感偏差及选择性探索条件，分别测量稀有事件覆盖、留出分布误差、校准和历史信息保留。

- **锚定假说：** 有信息价值且独立核验的反馈，应比匹配的封闭递归减轻跨代退化。若已核实覆盖和利用仍无可复现收益，则削弱此条件性假说。
- **具身特异假说：** 对需要干预的任务，行动条件采样应比匹配的被动观察提供额外价值。被动数据取得相同收益，会削弱具身独有的解释，但仍与一般外部锚定相容。
- **偏差限制：** 选择性或失真的反馈应削弱收益。若在受控反馈污染下仍稳定恢复，则须修订拟议失效机制。

预注册效应阈值，将评价数据流置于学习者选择策略之外，报告失败运行，寻求跨任务、跨架构的独立复现。这些测量仍不检验 EIC 或主体连续性。

## 8. Position in the IEH Evidence Architecture

**Recursive information loss [observed baseline] → external anchoring [candidate mechanism] → effective physical information loop [future test] → possible representational evolution [further evidence required].** Arrows mark research questions, not demonstrated transitions. The contribution concerns intergenerational degradation and why a physical loop might alter the information regime; it supplies no later EIC / IER / PBP steps.

## 8. 在 IEH 证据体系中的位置

**递归信息丢失［已观察基线］→ 外部锚定［候选机制］→ 有效物理信息闭环［未来检验］→ 可能的表征演化［仍需证据］。** 箭头表示研究问题，不是已演示的跃迁。贡献在于跨代退化，以及物理闭环为何可能改变信息机制；没有提供后续 EIC／IER／PBP 环节。

## 9. Relationship to Concepts and Related Notes

The [glossary](../glossary/GLOSSARY_EN.md) supplies the strict Information Continuity distinction. C02-HDCT / PA-10 have indirect pathway relevance only; the 2024 source predates PA-10's 2026 registration, so this is retrospective boundary evidence, not a prediction hit. No prediction record is reclassified.

Only necessary note links:

- [019 — Generalized embodiment and world-model pathway](./019-anthropic-model-hardware-standard-generalized-embodiment-and-world-model-pathway.md): connects the external-information question to physical perception–action–feedback access; access alone is not correction.
- [020 — World-model representation convergence](./020-platonic-world-model-representation-convergence-and-machine-native-representation-pathway.md): connects environmental prediction to proposed representational change; it does not establish immunity to collapse.

These are internal conceptual connections, not independent replications of this study.

## 9. 与概念及相关笔记的关系

[术语表](../glossary/GLOSSARY_ZH.md)提供严格的信息连续性区分。与 C02-HDCT／PA-10 仅有间接路径关联；2024 年来源早于 PA-10 的 2026 年建档，因此属于回溯性边界证据，不是预测命中。不调整任何预测档案的分类。

仅保留必要的笔记链接：

- [019——广义具身化与世界模型路径](./019-anthropic-model-hardware-standard-generalized-embodiment-and-world-model-pathway.md)：将外部信息问题连接到物理感知—行动—反馈接入；接入本身不等于纠错。
- [020——世界模型表征趋同](./020-platonic-world-model-representation-convergence-and-machine-native-representation-pathway.md)：连接环境预测与拟议表征变化；不建立对坍塌的免疫。

以上是内部概念连接，不是对该研究的独立复现。

## 10. Methodological Relevance

Keep source quality separate from theoretical directness. Specify the information source, sampling policy, retention rule and measured object before comparing two “loops.” Preserve favorable mixed-data results and possible physical-feedback failures alongside the negative baseline. Do not redefine Information Continuity as statistical similarity or treat later recovery of content as restoration of a subject's history.

## 10. 方法论意义

来源质量与理论直接性分别评价。比较两类“闭环”前，明确来源、采样策略、保留规则及被测对象。反向基线、混合数据的较好表现及物理反馈可能失效均应保留。不能把信息连续性重定义为统计相似，也不能将后来恢复内容等同于恢复主体历史。

## 11. Reserved for Future Publication

A formal criterion for a physical information loop's critical point; a theory separating distributional preservation from subject continuity; a powered, preregistered protocol; broader arguments about machine-native cognition and long-term AI evolution.

## 11. 为未来投稿保留的内容

物理信息闭环临界点的形式判据、区分分布保持与主体连续性的理论、有统计效力的预注册方案，以及机器原生认知和 AI 长期演化的更广论证。

## 12. References / 参考文献

[^1]: Shumailov, I.; Shumaylov, Z.; Zhao, Y.; Papernot, N.; Anderson, R.; Gal, Y. (2024). *AI models collapse when trained on recursively generated data*. Nature **631**, 755–759. Published / 发表：2024-07-24. [Original article / 原始论文](https://www.nature.com/articles/s41586-024-07566-y). DOI: [10.1038/s41586-024-07566-y](https://doi.org/10.1038/s41586-024-07566-y). Current corrected text consulted / 查阅当前更正版本：2026-09-28. Locators / 定位：“What is model collapse?”; “Theoretical intuition”; “Model collapse in language models”; Fig. 1; Example 1; “Discussion”.

[^2]: Shumailov, I.; Shumaylov, Z.; Zhao, Y.; Papernot, N.; Anderson, R.; Gal, Y. (2025). *Author Correction: AI models collapse when trained on recursively generated data*. Nature **640**, E6. Published / 发表：2025-03-21. [Original correction / 原始更正](https://www.nature.com/articles/s41586-025-08905-3). DOI: [10.1038/s41586-025-08905-3](https://doi.org/10.1038/s41586-025-08905-3). Accessed / 查阅：2026-09-28. Necessary to identify the corrected recursion assumption; not independent corroboration / 用于确认更正后的递归假设，不是独立佐证。

## 13. Status and Scope

**Disposition:** Strong direct evidence within the tested recursive-training conditions; provisional IEH negative baseline / boundary-condition interpretation. No EIC or IER evidence, and no direct PBP evidence. Reassess after source amendments, independent replication, materially different retention regimes or controlled real-world feedback results.

**Revision:** 2026-09-28 — v0.1; bilingual note and corresponding README index entries added. Main theory unchanged.

## 13. 状态与范围

**当前定位：** 受测递归训练条件内的强直接证据；暂定的 IEH 反向基线／边界条件解释。无 EIC、IER 证据及 PBP 直接证据。来源修订、独立复现、实质不同的数据保留机制或受控现实反馈结果出现后重评。

**修订：** 2026-09-28——v0.1；新增双语笔记及对应 README 索引行，不修改主理论。
