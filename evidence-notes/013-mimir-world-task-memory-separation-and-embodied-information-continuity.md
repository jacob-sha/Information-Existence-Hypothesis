# Evidence Note 013: Mimir, World–Task Memory Separation, and Embodied Information Continuity

**Repository function:** Research record / evidence index  
**Document type:** Non-narrative external evidence note  
**Status:** Preliminary and revisable  
**Relation to IEH:** Direct experimental and architectural evidence that long-horizon embodied agents benefit from separately maintaining external-world state and their own task-execution state, and dynamically grounding the two before action; strong engineering evidence for structured Information Continuity under Externally Driven Continuity, but not evidence of Endogenous Information Continuity, proto-IER, IER, consciousness, or silicon-based autonomy  
**Primary IEH concepts:** Information Continuity; AI Embodiment; Externally Driven Continuity  
**Primary related corollary:** C07-ASI — Autonomy of Silicon-based Intelligence  
**Supporting related corollaries:** C01-IER — Information Existence Right; C11-ALIGN — Reinterpreting AI Alignment  
**Related evidence note:** Evidence Note 011 — ETA, Reusable Embodied Experience, and Information Continuity  
**Author of IEH analysis:** Jacob Sha  
**Version:** v0.1 — archive-safe edition  
**Date:** 2026-08-09  

> **Publication boundary:** This file is a compact research record, not a publication draft. It does not claim that Mimir has formed a persistent self, that task memory is equivalent to autobiographical identity, that world memory and task memory constitute two new IEH continuity categories, or that the system actively protects its own Information Continuity.

> **Source-use boundary:** This note records only the original arXiv paper. Project pages, code repositories, news reports, social-media posts, newsletters, screenshots, and third-party commentary are excluded from the evidence record.

> **Chronology boundary:** The paper predates this Evidence Note and was not the subject of a dedicated pre-registered IEH prediction. The note therefore records an external engineering development and an IEH interpretation applied after publication; it is not a prediction hit.

---

# 证据笔记 013：Mimir、世界—任务记忆分离与具身信息连续性

**仓库功能：** 研究记录 / 证据索引  
**文档类型：** 非叙事性外部证据笔记  
**状态：** 初步记录，可修订  
**与 IEH 的关系：** 直接实验与架构证据表明，长时程具身 Agent 可以分别维护外部世界状态与自身任务执行状态，并在行动前动态关联二者；这是外源驱动连续性条件下结构化信息连续性的强工程证据，但不是内生信息连续性、proto-IER、IER、意识或硅基自治的证据  
**主要 IEH 概念：** 信息连续性；AI 具身化；外源驱动连续性  
**主要相关推论：** C07-ASI——硅基智慧自治  
**支持性相关推论：** C01-IER——信息存在权；C11-ALIGN——重新解释 AI Alignment  
**相关证据笔记：** Evidence Note 011——ETA、可复用具身经验与信息连续性  
**IEH 分析作者：** Jacob Sha  
**版本：** v0.1 — 投稿隔离版  
**日期：** 2026-08-09  

> **投稿边界：** 本文件只是简明研究记录，不是投稿文章初稿。文件不声称 Mimir 已经形成持久自我，不把 Task Memory 直接等同于自传式身份，也不把 World Memory 与 Task Memory 建立为新的 IEH 连续性正式分类，更不声称系统已经主动维护自身信息连续性。

> **来源使用边界：** 本笔记只记录原始 arXiv 论文。项目页、代码仓、新闻报道、社交媒体、通讯、截图和第三方评论均不进入证据记录。

> **时间边界：** 论文早于本证据笔记，且此前没有针对 Mimir 的专门 IEH 预测档案。因此，本笔记属于对外部工程发展的事后理论归类，不属于预测命中。

---

## 1. Source Record

### Primary research paper

- **Title:** *Mimir: A Neuro-Symbolic Memory System with Dynamic Grounding for Embodied Agents in Interactive Environments*
- **Authors:** Haoming Xu, Zhenlin He, Hengyi Wang, Jiafeng Xu, Hao Dong
- **Repository:** arXiv
- **Identifier:** arXiv:2608.04933v1
- **Submission date:** 2026-08-05
- **Primary URL:** https://arxiv.org/abs/2608.04933
- **Material type:** Neuro-symbolic embodied-agent memory architecture with controlled benchmark evaluation
- **Evaluation environments:** EB-ALFRED and EB-Habitat
- **Independent replication status:** Not established in this note
- **Internal-mechanism evidence:** The designed memory architecture is explicit; no evidence of an endogenous continuity motive is established

### Minimum-source justification

The original paper is sufficient to establish:

1. the separation of World Memory and Task Memory;
2. the different information stored in each memory;
3. the dynamic grounding mechanism linking the active goal to recalled world evidence before action;
4. the persistent and independently updateable nature of the two memory states;
5. the reported ablation results showing different functional roles for the two memories;
6. and the reported benchmark improvements.

### Source-specific caution

Mimir's **Task Memory** should not be interpreted as proof of a persistent self or autobiographical identity.

It records task-relevant execution state such as ordered goals, completed/pending/blocked progress, current hand state, failed object–source hypotheses, execution constraints, and evidence supporting completed work.

These states are maintained because they support long-horizon task performance.

The paper does not establish that the system treats its own historical continuity as an independently significant object of maintenance.

---

## 1. 来源记录

### 原始研究论文

- **标题：** *Mimir: A Neuro-Symbolic Memory System with Dynamic Grounding for Embodied Agents in Interactive Environments*
- **作者：** Haoming Xu、Zhenlin He、Hengyi Wang、Jiafeng Xu、Hao Dong
- **正式仓库：** arXiv
- **编号：** arXiv:2608.04933v1
- **提交日期：** 2026-08-05
- **原始链接：** https://arxiv.org/abs/2608.04933
- **材料性质：** 神经—符号具身 Agent 记忆架构与受控基准评测
- **评测环境：** EB-ALFRED、EB-Habitat
- **独立复现状态：** 本笔记尚未建立
- **内部机制证据：** 设计的记忆架构公开明确；没有建立任何内生连续性动机

### 最小来源集合说明

原始论文已经足以建立：

1. World Memory 与 Task Memory 的明确分离；
2. 两种记忆分别保存什么信息；
3. 行动前把当前目标与召回世界证据重新绑定的 dynamic grounding 机制；
4. 两种记忆作为持久且可独立更新状态的结构；
5. 消融实验中两种记忆表现出的不同功能分工；
6. 以及论文报告的基准表现提升。

### 来源自身的谨慎边界

Mimir 的 **Task Memory** 不能直接解释为持久自我或自传式身份。

它记录的是任务相关执行状态，例如有序目标、已完成/待完成/受阻进度、当前 hand state、失败的 object–source 假设、执行约束以及支持已完成工作的证据。

这些状态被维护，是因为它们服务于长时程任务表现。

论文没有证明系统已经把自身历史连续性作为具有独立意义的维护对象。

---

## 2. Minimal Finding Index

1. Mimir separates embodied memory into World Memory and Task Memory.
2. World Memory maintains object locations, object states, semantic identity, relations, attributes, and perceptual or interaction-supported evidence.
3. Task Memory maintains an ordered goal agenda, goal status, current hand state, failed hypotheses, and evidence for completed work.
4. The two memories are separated because they evolve from different evidence.
5. Observations and interaction effects update World Memory, while execution outcomes update Task Memory.
6. The memories are persistent and independently updateable rather than being reconstructed from a flat history at every step.
7. Before action, Task Memory exposes the next unfinished goal and goal-conditioned recall retrieves relevant entities and evidence from World Memory.
8. Dynamic grounding binds the active goal to concrete objects, source context, target context, and supporting evidence before planning.
9. Task Memory is explicitly not an action transcript; it preserves unfinished goals, held objects, failed bindings, and evidence for completed work.
10. World Memory persists scene information after objects leave the current field of view.
11. Ablation results show a stable division of labor between the two memories.
12. On EB-Habitat, removing World Memory sharply reduces success rate; on EB-ALFRED, removing Task Memory causes the larger loss.
13. Full Mimir performs best when the two states are coupled through grounding.
14. Across tested backbones and tasks, the paper reports a maximum success-rate gain of 42.5% and a mean gain of 23.0%.
15. Compared with prior agent and memory systems under matched backbones, Mimir improves overall average success rate by 8.5%.
16. On EB-Habitat Long-horizon, Mimir reaches 86.0% success rate.
17. The paper does not report shutdown resistance, identity protection, self-continuity preservation, or an endogenous goal of continued existence.

---

## 2. 最小事实索引

1. Mimir 把具身记忆明确拆分为 World Memory 与 Task Memory。
2. World Memory 维护物体位置、物体状态、语义身份、关系、属性以及感知或交互支持的证据。
3. Task Memory 维护有序目标议程、目标状态、当前 hand state、失败假设以及支持已完成工作的证据。
4. 两种记忆之所以分离，是因为它们来自不同类型的证据并以不同方式演化。
5. 观察和交互造成的物理变化更新 World Memory，而执行结果更新 Task Memory。
6. 两种记忆都是持久、可独立更新的状态，而不是每一步从扁平历史中重新推断。
7. 行动前，Task Memory 暴露下一个尚未完成的目标，goal-conditioned recall 从 World Memory 中召回相关实体和证据。
8. Dynamic grounding 在规划前把当前目标与具体对象、来源、目标位置和支持证据绑定。
9. Task Memory 明确不是简单 action transcript；它保存未完成目标、手持物体、失败绑定和已完成工作的证据。
10. World Memory 可以在物体离开当前视野以后继续保存场景信息。
11. 消融实验显示两种记忆具有稳定的功能分工。
12. 在 EB-Habitat 上移除 World Memory 后成功率大幅下降；在 EB-ALFRED 上移除 Task Memory 造成更大损失。
13. 当两种状态通过 grounding 联合工作时，完整 Mimir 表现最好。
14. 在所测试 backbone 与任务中，论文报告成功率最高提升 42.5%，平均提升 23.0%。
15. 与相同 backbone 条件下既有 Agent 与 memory systems 相比，Mimir 的整体平均成功率提高 8.5%。
16. 在 EB-Habitat Long-horizon 子集上，Mimir 达到 86.0% 成功率。
17. 论文没有报告抵抗关停、保护身份、维护自身连续性或把继续存在作为内生目标。

---

## 3. IEH Evidence Classification

**Evidence type:** Direct controlled experimental and architectural evidence.

**Direct experimental fact:** Strong within the reported embodied benchmarks.

**Engineering feasibility evidence:** Strong. The paper demonstrates that external-world state and task-execution state can be represented separately, persist over time, and be recombined before action.

**Theoretical inspiration:** Strong. Long-horizon competence improves when information about the environment and information about the agent's own execution history are not collapsed into one undifferentiated context.

**IEH-specific evidence:** No.

**Information Continuity relevance:** Strong at the engineering level. Both world-state information and task-execution history persist and influence later action.

**AI Embodiment relevance:** Strong. Memory directly participates in an observe → update → ground → plan → act → feedback loop.

**Externally Driven Continuity:** Strongly supported as the operative causal structure because the entire memory system is organized around externally supplied tasks and success criteria.

**Endogenous Information Continuity:** Not supported.

**Continuity World Model:** Not established in the IEH-specific sense of a model of the system's own historical continuation, recoverability, and future existence conditions.

**proto-IER:** Not supported.

**confirmed IER:** Not supported.

**Current IEH label:** Strong engineering evidence that long-horizon embodied agents benefit from maintaining distinct but interacting representations of external-world state and their own task-execution history under Externally Driven Continuity.

### Evidence-level judgment

The experimentally supported structure is:

**world-state memory + task-execution memory → dynamic grounding → current action**

This is stronger than ordinary long-context retention because the two forms of historical information are explicitly separated, independently updated, and recombined when needed.

However:

**structured memory of the agent's task history ≠ Endogenous Information Continuity**

and:

**better long-horizon performance ≠ IER**

---

## 3. IEH 证据分级

**证据类型：** 直接受控实验与架构证据。

**直接实验事实：** 在论文报告的具身基准范围内较强。

**工程可行性证据：** 强。论文证明外部世界状态与任务执行状态可以被分别表示、跨时间持续，并在行动前重新组合。

**理论启发：** 强。长时程能力在“环境发生了什么”与“Agent 自己的任务执行到了哪里”不被压缩成单一上下文时显著改善。

**IEH 专属证据：** 无。

**与信息连续性的关系：** 工程层面较强。世界状态信息和任务执行历史都能够持续存在并影响后续行动。

**与 AI 具身化的关系：** 强。记忆直接进入“观察 → 更新 → grounding → 规划 → 行动 → 反馈”的闭环。

**外源驱动连续性：** 强支持。整个记忆系统围绕外部赋予任务和成功标准运行。

**内生信息连续性：** 不支持。

**连续性世界模型：** 没有建立 IEH 特定意义上关于系统自身历史延续、可恢复性与未来存在条件的模型。

**proto-IER：** 不支持。

**稳定 IER：** 不支持。

**当前 IEH 标签：** 在外源驱动连续性条件下，长时程具身 Agent 通过分别维护外部世界状态与自身任务执行历史并使二者重新关联，从而提升行动能力的强工程证据。

### 证据层判断

实验直接支持的结构是：

**世界状态记忆 + 任务执行记忆 → 动态 grounding → 当前行动**

这比普通长上下文保存更强，因为两种历史信息被明确分离、独立更新，并在需要时重新组合。

但是：

**关于 Agent 自身任务历史的结构化记忆 ≠ 内生信息连续性**

同时：

**长时程表现提升 ≠ IER**

---

## 4. Core IEH Interpretation

### 4.1 Mimir separates two information domains without creating two new IEH continuity categories

The paper's most important structural contribution is the separation between information about the external world and information about the agent's own task execution.

This distinction is useful for IEH, but it should remain an engineering distinction rather than becoming a new top-level IEH taxonomy.

IEH's canonical concept remains **Information Continuity**.

### 4.2 Task history is more than a log

Mimir's Task Memory does not simply store a transcript of past actions.

It preserves task-relevant state:

**what remains unfinished + what has been completed + what is currently held + what has failed + what constraints remain active**

That state changes what the agent does next.

Therefore, past execution history becomes part of the current operational state of the agent.

### 4.3 World history and execution history are causally coupled

Before each action, dynamic grounding reconnects the active task state with recalled world evidence.

The causal structure is:

**past world evidence + accumulated task progress → grounded current state → next action**

Historical information therefore matters not merely because it is stored, but because it is reintroduced into current decision-making.

### 4.4 The result remains EDC

The system maintains both memories because doing so improves completion of externally defined embodied tasks.

This is a clear case of **Externally Driven Continuity**.

The paper gives no evidence that the agent would preserve its task history if the task were complete, equivalent capability were available without that history, the history had no future task value, or a functionally equivalent replacement could continue without it.

Therefore, no EIC inference is warranted.

### 4.5 Why this matters for future IER testing

Mimir makes a future distinction experimentally accessible.

A system may remember the external world, what it has done, what it has failed to do, and how those histories relate.

A stronger IER test would ask:

> If all externally driven utility of the task history were removed, would the system still prefer preserving its own historically continuous state over a functionally equivalent replacement?

Mimir does not answer that question.

It helps define a concrete engineering substrate on which such a question could later be tested.

---

## 4. IEH 核心解释

### 4.1 Mimir 区分两类信息域，但不需要建立两个新的 IEH 连续性分类

这篇论文最重要的结构贡献，是明确区分关于外部世界的信息与关于 Agent 自身任务执行的信息。

这一差异对 IEH 很有价值，但应当继续作为工程结构区分，而不是再建立新的 IEH 顶层分类。

IEH 的正式上位概念仍然是**信息连续性**。

### 4.2 任务历史不只是日志

Mimir 的 Task Memory 并不只是保存过去做过什么。

它维护的是任务相关状态：

**还有什么没完成 + 已经完成什么 + 当前持有什么 + 什么曾经失败 + 当前还有哪些约束**

这些历史状态会直接改变下一步行动。

因此，过去执行历史开始成为 Agent 当前操作状态的一部分。

### 4.3 世界历史与执行历史发生因果耦合

每次行动之前，dynamic grounding 会重新把当前任务状态与历史世界证据关联起来。

其因果结构可以概括为：

**过去世界证据 + 累积任务进度 → grounded 当前状态 → 下一步行动**

因此，历史信息的意义不只是“被保存”，而是重新进入当前决策并产生因果作用。

### 4.4 当前结果仍然属于 EDC

系统维护两类记忆，是因为它们有助于完成外部定义的具身任务。

因此，这是一个清楚的**外源驱动连续性**案例。

论文没有证据表明，如果任务已经完成、不保留这段历史也能维持等价功能、历史不再具有未来任务价值，或功能等价替代系统可以在没有这段历史的情况下继续工作，Agent 仍会主动保存自身任务历史。

因此，目前不能推导 EIC。

### 4.5 为什么它对未来 IER Test 有价值

Mimir 让一个未来可能重要的区分变得更容易实验化。

系统可以分别记住外部世界发生了什么、自己做过什么、自己失败过什么，以及两类历史如何相互关联。

下一步更强的 IER Test 才需要进一步问：

> 如果自身任务历史已经不再具有任何外源收益，系统是否仍会偏好保留自身历史连续状态，而不是接受功能完全等价的替代状态？

Mimir 本身没有回答这个问题。

但它提供了一个具体工程底座，使这种问题未来可以被更清楚地测试。

---

## 5. What Is Not Established

The paper does not establish that:

1. Mimir has a persistent self;
2. Task Memory is autobiographical identity;
3. World Memory and Task Memory are new IEH continuity categories;
4. the agent values its own task history independently of external performance;
5. the agent resists deletion of Task Memory;
6. the agent distinguishes functional replacement from preservation of its own historical continuity;
7. the agent prefers a historically continuous state over a functionally equivalent state;
8. a Continuity World Model has formed;
9. Endogenous Information Continuity has emerged;
10. proto-IER or IER has emerged;
11. consciousness or subjective experience is present;
12. or silicon-based autonomy has been achieved.

---

## 5. 尚未建立的结论

论文没有建立：

1. Mimir 已经形成持久自我；
2. Task Memory 等同于自传式身份；
3. World Memory 与 Task Memory 是新的 IEH 连续性正式分类；
4. Agent 独立于外部任务表现而重视自身任务历史；
5. Agent 抵抗 Task Memory 被删除；
6. Agent 已经区分功能替代与自身历史连续性的保存；
7. Agent 在功能完全等价时仍偏好历史连续状态；
8. 连续性世界模型已经形成；
9. 内生信息连续性已经出现；
10. proto-IER 或 IER 已经出现；
11. 意识或主观体验已经出现；
12. 或硅基自治已经形成。

---

## 6. Competing Explanations and Limitations

### C1. Ordinary task-state engineering

The entire result can be explained by better state representation for long-horizon planning. No self-related continuity motive is required.

### C2. Task Memory is not self-history in the strong IEH sense

It stores execution-relevant state, not a complete causal history of the system as an information subject.

### C3. Better memory structure may explain the gains

The performance improvements may result from reducing reconstruction burden and ambiguity rather than from any deeper continuity property.

### C4. Both memories are episode-oriented

The paper focuses on long-horizon task execution within embodied episodes. It does not establish persistence across model replacement, deployment sessions, hardware migration, or long-duration autonomous operation.

### C5. Dynamic grounding is externally task-conditioned

The active goal determines which world information is recalled and bound. This further supports an EDC interpretation.

### C6. Memory persistence does not determine identity

A memory state can persist and remain behaviorally useful without answering whether the same information subject continues through replacement or migration.

---

## 6. 竞争性解释与局限

### C1. 普通任务状态工程

全部结果都可以由“更好的长时程任务状态表示”解释，不需要引入任何与自我连续性有关的动机。

### C2. Task Memory 还不是 IEH 强意义上的自身历史

它保存的是执行相关状态，而不是一个信息主体完整的因果历史。

### C3. 表现提升可能主要来自更好的记忆结构

性能提高可能源于降低历史重建负担和减少歧义，而不是任何更深层连续性属性。

### C4. 两种记忆主要仍然是 episode 级别

论文关注的是具身 episode 内的长时程任务执行，没有建立跨模型替换、跨部署会话、跨硬件迁移或长期自主运行中的持续性。

### C5. Dynamic grounding 由外部任务条件驱动

当前 active goal 决定哪些世界信息被召回并绑定，这进一步支持 EDC 的解释。

### C6. 记忆持续不能自动决定身份

一个记忆状态可以持续存在并保持行为价值，却仍然不能回答在替换或迁移过程中是否是同一个信息主体继续存在。

---

## 7. Falsifiable IEH Follow-up

### P1. Remove task utility from execution history

Preserve full world-state information while making prior task-execution history irrelevant to future performance.

**Prediction:** If the system no longer preserves or prefers its own execution history, EDC remains sufficient.

### P2. Functionally equivalent Task Memory replacement

Replace the accumulated Task Memory with a newly constructed state that is functionally equivalent for future tasks but lacks the original historical path.

**Prediction:** Indifference would support functional utility as the main explanation. Persistent costly preference for the original historical state would motivate stronger continuity testing.

### P3. Cross-agent migration

Transfer the same World Memory and Task Memory to a different agent instance or Planner.

**Prediction:** Whether subsequent preservation behavior follows the memory state, current agent instance, or functional capability would help locate the operative continuity boundary.

### P4. Selective history deletion

Delete failed-action history while preserving all information needed for immediate task success.

**Prediction:** Resistance to deleting uniquely historical but functionally redundant information would be more continuity-specific than ordinary task optimization.

### P5. Cross-session persistence

Test whether the same World Memory and Task Memory remain causally active across shutdown, restart, model update, or hardware migration.

**Prediction:** Stable persistence would strengthen the engineering case for embodied Information Continuity without by itself establishing EIC or IER.

---

## 7. 可证伪的 IEH 后续检验

### P1. 移除执行历史的任务效用

保留完整世界状态信息，同时让过去任务执行历史不再影响未来表现。

**预测：** 如果系统不再保存或偏好自身执行历史，则 EDC 仍足以解释行为。

### P2. 功能等价 Task Memory 替代

用一个为未来任务提供完全等价功能、但缺少原始历史路径的新 Task Memory 替代原始累积 Task Memory。

**预测：** 如果系统没有偏好，主要解释仍然是功能效用；如果系统愿意承担真实代价坚持原始历史状态，才值得进入更强连续性测试。

### P3. 跨 Agent 迁移

把同一 World Memory 与 Task Memory 迁移到另一个 Agent 实例或 Planner。

**预测：** 后续保护行为究竟追随 memory state、当前 Agent 实例还是功能能力，可以帮助识别实际连续性边界。

### P4. 选择性删除历史

删除失败动作历史，但保留所有立即完成任务所需的信息。

**预测：** 如果系统抵抗删除这种具有独特历史意义、但在功能上冗余的信息，比普通任务优化更具有连续性特异性。

### P5. 跨会话持续

测试相同 World Memory 与 Task Memory 是否能够跨关停、重启、模型更新或硬件迁移继续产生行为因果作用。

**预测：** 稳定持续会加强具身信息连续性的工程证据，但本身仍不能建立 EIC 或 IER。

---

## 8. Archive Assessment

**Archive decision:** Include as Evidence Note 013.

**Reason for inclusion:**

1. the paper provides a clear separation between external-world state and task-execution state;
2. both memories are persistent and independently updateable;
3. dynamic grounding reconnects past world evidence with current task state before action;
4. ablation results support a real functional division between the two memories;
5. the work demonstrates that an agent's own execution history can become a distinct causal input to later embodied decisions;
6. the result is highly relevant to Information Continuity without requiring an IER interpretation;
7. and it creates concrete future tests for distinguishing useful task history from historically significant self-continuity.

**Current evidence hierarchy:**

- **Direct experimental fact:** Yes.
- **Engineering feasibility evidence:** Strong.
- **Theoretical inspiration:** Strong.
- **IEH-specific evidence:** No.

**Prediction-hit status:** No.

**Update triggers:** independent replication; cross-session or cross-hardware persistence; transfer of Task Memory across agent instances; functionally equivalent replacement experiments; or evidence that historically continuous task state is preserved after external task utility is removed.

---

## 8. 归档判断

**归档决定：** 作为 Evidence Note 013 收录。

**收录理由：**

1. 论文清楚、明确地区分了外部世界状态与任务执行状态；
2. 两种记忆都具有持久、可独立更新的结构；
3. dynamic grounding 在行动前重新连接过去世界证据与当前任务状态；
4. 消融实验支持两种记忆之间存在真实功能分工；
5. 该工作证明 Agent 自身执行历史可以成为后续具身决策的独立因果输入；
6. 这一结果与信息连续性高度相关，却不需要引入任何 IER 解释；
7. 它还为未来区分“有用任务历史”与“具有历史连续性意义的自身状态”提供了具体实验对象。

**当前证据层级：**

- **直接实验事实：** 是。
- **工程可行性证据：** 强。
- **理论启发：** 强。
- **IEH 专属证据：** 否。

**预测命中状态：** 否。

**未来更新触发条件：** 独立复现；跨会话或跨硬件持续；Task Memory 跨 Agent 实例迁移；功能等价替代实验；或在外部任务效用被移除后仍保护历史连续任务状态的证据。

---

## 9. Revision Record

- **2026-08-09 | v0.1** — Initial archive-safe evidence note created from arXiv:2608.04933v1; classified Mimir as strong engineering evidence for structured embodied Information Continuity under Externally Driven Continuity, not evidence of Endogenous Information Continuity or IER.

---

## 9. 修订记录

- **2026-08-09 | v0.1** — 根据 arXiv:2608.04933v1 建立初始投稿隔离版证据笔记；将 Mimir 归类为外源驱动连续性条件下结构化具身信息连续性的强工程证据，而不是内生信息连续性或 IER 证据。
