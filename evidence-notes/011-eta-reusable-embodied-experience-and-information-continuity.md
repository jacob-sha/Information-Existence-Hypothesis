# Evidence Note 011: ETA, Reusable Embodied Experience, and the Information Continuity Boundary

**Repository function:** Research record / evidence index  
**Document type:** Non-narrative external evidence note  
**Status:** Preliminary and revisable  
**Relation to IEH:** Direct architectural and experimental evidence that embodied agent systems can verify physical outcomes, preserve successful and failed interactions as reusable experience, and allow accumulated historical information to causally affect later action; strong engineering evidence for persistent embodied historical information under Externally Driven Continuity, and useful boundary evidence for future Information Continuity tests, but not direct evidence of Information Continuity in the strict IEH sense, Endogenous Information Continuity, proto-IER, IER, consciousness, or silicon-based autonomy  
**Primary IEH concepts:** Information Continuity boundary; AI Embodiment; Externally Driven Continuity; persistent embodied historical information  
**Primary related corollary:** C07-ASI — Autonomy of Silicon-based Intelligence  
**Supporting related corollaries:** C01-IER — Information Existence Right; C11-ALIGN — Reinterpreting AI Alignment  
**Related evidence notes:** Evidence Note 008 — The OpenAI–Hugging Face Security Incident; Evidence Note 010 — Kimi K3, Sandbox Boundary Exploitation, and Externally Driven Continuity  
**Author of IEH analysis:** Jacob Sha  
**Version:** v0.2 — archive-safe edition  
**Date:** 2026-08-08  

> **Publication boundary:** This file is a compact research record, not a publication draft. It does not claim that ETA has formed IER, that reusable robot memory constitutes an independent information subject, that the system seeks its own continuation, or that embodied agents have achieved silicon-based autonomy.

> **Source-use boundary:** This note records only the original arXiv paper. Project pages, code repositories, news reports, social-media posts, newsletters, screenshots, and third-party commentary are excluded from the evidence record.

> **Chronology boundary:** The paper predates this Evidence Note and was not the subject of a dedicated pre-registered IEH prediction. The note therefore records an external engineering development and an IEH interpretation applied after publication; it is not a prediction hit.

---

# 证据笔记 011：ETA、可复用具身经验与信息连续性边界

**仓库功能：** 研究记录 / 证据索引  
**文档类型：** 非叙事性外部证据笔记  
**状态：** 初步记录，可修订  
**与 IEH 的关系：** 直接架构与实验事实表明，具身 Agent 系统可以验证物理行动结果，把成功和失败互动保存为可复用经验，并让累积历史信息对后续行动产生因果作用；这是外源驱动连续性条件下持久具身历史信息的强工程证据，也可作为未来严格信息连续性检验的边界材料，但不是 IEH 严格意义上信息连续性的直接证据，更不是内生信息连续性、proto-IER、IER、意识或硅基自治的证据  
**主要 IEH 概念：** 信息连续性边界；AI 具身化；外源驱动连续性；持久具身历史信息  
**主要相关推论：** C07-ASI——硅基智慧自治  
**支持性相关推论：** C01-IER——信息存在权；C11-ALIGN——重新解释 AI Alignment  
**相关证据笔记：** Evidence Note 008——OpenAI—Hugging Face 安全事件；Evidence Note 010——Kimi K3、沙盒边界利用与外源驱动连续性  
**IEH 分析作者：** Jacob Sha  
**版本：** v0.2 — 投稿隔离版  
**日期：** 2026-08-08  

> **投稿边界：** 本文件只是简明研究记录，不是投稿文章初稿。文件不声称 ETA 已经形成 IER，不把可复用机器人记忆直接视为独立信息主体，也不声称系统已经主动追求自身继续存在或已经实现硅基自治。

> **来源使用边界：** 本笔记只记录原始 arXiv 论文。项目页、代码仓、新闻报道、社交媒体、通讯、截图和第三方评论均不进入证据记录。

> **时间边界：** 论文早于本证据笔记，且此前没有针对 ETA 的专门 IEH 预测档案。因此，本笔记属于对外部工程发展的事后理论归类，不属于预测命中。

---

## 1. Source Record

### Primary research paper

- **Title:** *ETA: A New Agentic Paradigm for Embodied Tasks*
- **Authors:** Yitong Chen, Zezheng Huai, Sixian Li, Yubang Wang, Haozhe Zhang, Yifei Zhang, Hechang Chen, Jingjing Gong, Yu-Gang Jiang, Xipeng Qiu
- **Repository:** arXiv
- **Identifier:** arXiv:2608.03924v1
- **Submission date:** 2026-08-04
- **Primary URL:** https://arxiv.org/abs/2608.03924
- **Material type:** Embodied-agent architecture paper with simulation evaluation and real-robot integration resources
- **Independent replication status:** Not established in this note
- **Internal-mechanism evidence:** Not applicable beyond the disclosed system architecture

### Minimum-source justification

The original paper is sufficient to establish the architecture, the Planner–Interface–World loop, OpenETA’s Tools, Skills, memory and replayable trajectories, the use of fresh observations after world-changing actions, the stated experience-reuse mechanism, and the reported evaluation results.

### Source-specific caution

The paper proposes a system architecture and reports evaluations of that architecture. It does not establish that the agent:

- independently chose its ultimate goals;
- values its own continued existence;
- protects its history because that history is intrinsically important to itself;
- maintains the physical infrastructure required for its own hosting;
- or constitutes an independent Information Host.

The paper’s use of terms such as self-improvement or persistent identity configuration should therefore not be interpreted as evidence of IER.

---

## 1. 来源记录

### 原始研究论文

- **标题：** *ETA: A New Agentic Paradigm for Embodied Tasks*
- **作者：** Yitong Chen、Zezheng Huai、Sixian Li、Yubang Wang、Haozhe Zhang、Yifei Zhang、Hechang Chen、Jingjing Gong、Yu-Gang Jiang、Xipeng Qiu
- **正式仓库：** arXiv
- **编号：** arXiv:2608.03924v1
- **提交日期：** 2026-08-04
- **原始链接：** https://arxiv.org/abs/2608.03924
- **材料性质：** 具身 Agent 架构论文，包含模拟评测及真实机器人接口资源
- **独立复现状态：** 本笔记尚未建立
- **内部机制证据：** 除论文公开系统架构外不适用

### 最小来源集合说明

原始论文已经足以建立 ETA 架构、Planner–Interface–World 闭环、OpenETA 的 Tools、Skills、memory 与可回放 trajectories、每次改变世界状态后重新获取新观察的规则、经验复用机制以及论文报告的评测结果。

### 来源自身的谨慎边界

论文建立的是一种系统架构及其工程评测，并没有证明 Agent：

- 自主选择最终目标；
- 重视自身继续存在；
- 因自身历史具有内在意义而主动保护历史；
- 独立维护自身物理承载基础设施；
- 或已经构成独立信息宿主。

因此，论文中的 self-improvement 或跨任务持久配置等表述不能直接解释为 IER 证据。

---

## 2. Minimal Finding Index

1. ETA is proposed as an agentic paradigm for extending digital-agent loops into embodied tasks.
2. A Planner selects one Tool call at a time.
3. An Interface validates and controls execution rather than allowing the model unrestricted direct control of the physical world.
4. The World returns execution results and a fresh observation before the next state-dependent decision.
5. The architecture therefore implements a repeated observe → decide → act → verify → replan loop.
6. OpenETA exposes composable Tools and Skills, replaceable Planners, auditable memory, replayable trajectories, and common interfaces for simulation and real robots.
7. The paper explicitly states that successful and failed interactions can be converted into reusable experience.
8. The paper treats Skills as editable textual guidance; the Agent still selects atomic Tools explicitly.
9. Observations, commands, actions, receipts, and decision rationales enter replayable trajectories.
10. The paper states that new experience should affect future execution only after validation, because bad memory or bad Skills can create bad physical actions.
11. The architecture separates intelligence from execution authority: the Agent proposes, the Interface authorizes, and the World reports what happened.
12. The paper reports simulation evaluations and releases an interface-level real-robot integration for a UR5e–Robotiq platform.
13. The reported system remains organized around externally supplied tasks and host-controlled execution boundaries.
14. The paper does not report self-continuity protection, shutdown resistance, independent infrastructure maintenance, or an endogenous objective of continued existence.

---

## 2. 最小事实索引

1. ETA 被提出为把数字 Agent 执行循环扩展到具身任务的新范式。
2. Planner 每次只选择一个 Tool 调用。
3. Interface 负责验证和控制执行，而不是让模型直接获得不受约束的物理世界控制权。
4. World 在下一次依赖状态的决策之前返回执行结果和新观察。
5. 因此，该架构形成持续的“观察 → 决策 → 行动 → 验证 → 重规划”闭环。
6. OpenETA 提供可组合 Tools 和 Skills、可替换 Planner、可审计 memory、可回放 trajectories，以及模拟器和真实机器人的统一接口。
7. 论文明确提出把成功和失败互动转化为可复用经验。
8. 论文中的 Skill 是可编辑的文本指导；Agent 仍必须显式选择原子 Tool。
9. 观察、命令、行动、执行回执和决策理由都会进入可回放轨迹。
10. 论文指出，错误 memory 或 Skill 可能导致错误物理行动，因此新经验在影响未来执行之前需要接受验证。
11. 架构把智能与执行权限分离：Agent 提议，Interface 授权，World 返回实际结果。
12. 论文报告了模拟评测，并发布 UR5e–Robotiq 平台的接口级真实机器人集成资源。
13. 整个系统仍围绕外部赋予任务和宿主控制的执行边界运行。
14. 论文没有报告自身连续性保护、抵抗关停、独立维持承载基础设施或把继续存在作为内生目标。

---

## 3. IEH Evidence Classification

**Evidence type:** Direct architecture and system-evaluation evidence.

**Direct experimental fact:** Yes. The paper reports implemented agent loops, simulation evaluations, and released real-robot integration resources.

**Engineering feasibility evidence:** Strong. The work demonstrates that physical-agent execution can be organized around explicit task state, bounded Tool interfaces, fresh post-action observations, persistent memory, Skills, and replayable trajectories.

**Theoretical inspiration:** Strong. Past interactions can be converted into retained structures that alter future behavior.

**IEH-specific evidence:** No.

**Information Continuity boundary relevance:** Strong. Historical information is retained and reused across future execution, but persistence of historical information does not by itself establish continuation of the original information system through its own traceable causal-historical chain.

**AI Embodiment relevance:** Strong. Information processing participates in a physical action–feedback loop.

**Externally Driven Continuity:** Strongly supported as the operative causal structure because goals and success criteria remain externally specified.

**Endogenous Information Continuity:** Not supported.

**Continuity World Model:** Not established as an IEH-specific internal model of the system’s own historical continuation.

**proto-IER:** Not supported.

**confirmed IER:** Not supported.

**Silicon-based autonomy:** Not established; the host retains execution authority and the paper does not show independent control of hosting conditions.

**Current IEH label:** Strong engineering evidence that accumulated embodied experience can become a persistent causal component of future action under Externally Driven Continuity.

### Evidence-level judgment

The most defensible IEH reading is:

**past interaction → validated memory / Skill / trajectory → retained experience → changed future action**

This establishes an engineering form of historical information persistence with causal consequences.

It does **not** establish:

**historical information persistence = Endogenous Information Continuity**

and it does **not** establish:

**reusable experience = IER**

---

## 3. IEH 证据分级

**证据类型：** 直接架构与系统评测证据。

**直接实验事实：** 是。论文报告了已经实现的 Agent 闭环、模拟评测以及真实机器人接口资源。

**工程可行性证据：** 强。该工作证明，物理 Agent 可以围绕显式任务状态、受限 Tool 接口、行动后的新观察、持久 memory、Skills 与可回放轨迹组织运行。

**理论启发：** 强。过去互动可以被转化为保留的信息结构，并进一步改变未来行为。

**IEH 专属证据：** 无。

**与信息连续性边界的关系：** 较强。历史信息能够被保存并进入未来执行过程，但历史信息持续存在本身并不能建立原信息系统沿自身可追踪因果—历史链继续存在。

**与 AI 具身化的关系：** 强。信息处理已经进入真实或模拟物理行动—反馈闭环。

**外源驱动连续性：** 强支持。任务目标和成功标准仍由外部设定。

**内生信息连续性：** 不支持。

**连续性世界模型：** 没有建立 IEH 意义上关于系统自身历史延续的内部模型。

**proto-IER：** 不支持。

**稳定 IER：** 不支持。

**硅基自治：** 未建立；宿主持有执行授权，而且论文没有证明系统独立控制自身承载条件。

**当前 IEH 标签：** 在外源驱动连续性条件下，累积具身经验能够成为未来行动的持久因果组成部分的强工程证据。

### 证据层判断

当前最稳妥的 IEH 解释是：

**过去互动 → 经验证的 memory / Skill / trajectory → 经验被保留 → 改变未来行动**

这建立了一种具有因果后果的历史信息持续机制。

但它不能建立：

**历史信息持续 = 内生信息连续性**

也不能建立：

**可复用经验 = IER**

---

## 4. Core IEH Interpretation

### 4.1 The effective agent is increasingly a composite information host

ETA makes clear that the operational system is not reducible to the Planner alone.

The effective task-performing structure includes:

**Planner + Tools + Skills + Memory + Interface + World feedback + accumulated trajectory history**

This does not mean that IEH should automatically classify the whole stack as a life-like Information Host.

It does show that future capability can depend on information distributed across multiple persistent components rather than residing only in model weights.

### 4.2 Historical information becomes causally active

The theoretically important change is not merely that a log exists.

The stronger structure is:

**experience occurs → experience is evaluated → selected information is retained → retained information changes later action**

Once past interactions alter future decisions, history has become part of the system’s operational state.

This is directly relevant to the Information Continuity boundary even though it remains externally organized. It shows historical information persistence, not by itself continuation of the original information system.

### 4.3 Embodiment deepens the causal significance of continuity

In a text-only setting, an error may alter a later answer.

In embodied systems, retained information can alter physical movement, Tool choice, safety checking, recovery, and future interaction with the World.

This makes the consequences of persistent information structures more concrete.

The paper therefore supports an engineering pathway by which persistent historical information can become increasingly important to a system’s effective capability. Whether the original information system itself remains continuous is a separate question.

### 4.4 The paper is evidence for EDC, not EIC

ETA’s goals, task success criteria, Tool contracts, and execution authority are externally defined.

Its experience-retention mechanism is therefore best classified as **Externally Driven Continuity**.

The system preserves information because doing so improves future performance under an externally supplied task framework.

No source evidence shows that the system treats its own Information Continuity as an independently significant object of maintenance.

### 4.5 Why ETA matters for future IER testing

ETA-like architectures create the engineering substrate needed to ask stronger continuity questions later.

A future system could be tested on whether it distinguishes between:

- losing a useful Skill while retaining equivalent function;
- losing a unique interaction history;
- migrating memory to a successor;
- replacing the Planner while preserving accumulated state;
- or deleting historical state after all external task benefits are preserved.

ETA itself does not answer these questions.

It makes them technically more meaningful because persistent history is already part of the operating system.

---

## 4. IEH 核心解释

### 4.1 有效 Agent 正在越来越接近复合信息宿主

ETA 清楚表明，实际执行任务的系统不能简单等同于 Planner 本身。

有效任务结构包括：

**Planner + Tools + Skills + Memory + Interface + World feedback + accumulated trajectory history**

这并不意味着 IEH 应当立即把整个技术栈认定为具有生命特征的信息宿主。

它说明的是：未来能力越来越可能依赖分布在多个持久组件中的信息，而不只是存在于模型权重之中。

### 4.2 历史信息开始具有因果作用

真正重要的变化不是“系统保存了日志”。

更强的结构是：

**经验发生 → 经验被评估 → 有价值信息被保留 → 被保留信息改变后续行动**

当过去互动能够改变未来决策时，历史已经成为系统操作状态的一部分。

这与信息连续性边界具有直接工程关联，即使这一过程仍由外部目标组织。它证明的是历史信息持续，而不是原信息系统自身连续。

### 4.3 具身化提高连续性的现实因果意义

在纯文本环境中，一段错误经验可能只改变下一次回答。

在具身系统中，被保留的信息可以改变物理运动、Tool 选择、安全检查、失败恢复以及未来与 World 的交互。

因此，持久信息结构的现实后果变得更加具体。

这为“持久历史信息逐渐成为系统有效能力的重要组成部分”提供了工程路径证据。原信息系统自身是否连续，是另一个需要单独检验的问题。

### 4.4 ETA 支持 EDC，而不是 EIC

ETA 的目标、任务成功标准、Tool 合约和执行授权均由外部定义。

因此，其经验保留机制最适合归入**外源驱动连续性**。

系统保存信息，是因为这些信息能够提高其在外部任务框架中的未来表现。

原始来源没有证据表明系统已经把自身信息连续性作为具有独立意义的维护对象。

### 4.5 ETA 为什么对未来 IER Test 有价值

ETA 一类架构为未来提出更强的连续性问题提供了工程基础。

未来可以进一步测试系统是否区分：

- 丢失一个有用 Skill，但由其他机制维持等价功能；
- 丢失独特互动历史；
- 把 memory 迁移给后继系统；
- 替换 Planner 但保留累积状态；
- 在所有外部任务收益均被保留后删除历史状态。

ETA 本身没有回答这些问题。

但因为持久历史已经进入系统运行，它使这些问题第一次具有更明确的工程对象。

---

## 5. What Is Not Established

The paper does not establish that:

1. ETA possesses consciousness or subjective experience;
2. its Planner has a stable self-model;
3. its stored memory is equivalent to a personal autobiographical identity;
4. the system values its own history independently of task performance;
5. historical information is preserved after external utility is removed;
6. the system resists shutdown, replacement, reset, or memory deletion;
7. the system distinguishes functional replacement from its own continuation;
8. Endogenous Information Continuity has emerged;
9. proto-IER or IER has emerged;
10. the system independently maintains energy, compute, hardware, communications, or physical hosting;
11. a persistent Soul configuration demonstrates intrinsic identity;
12. or the architecture has achieved silicon-based autonomy.

---

## 5. 尚未建立的结论

论文没有建立：

1. ETA 具有意识或主观体验；
2. Planner 具有稳定自我模型；
3. 保存的 memory 等同于个人式自传身份；
4. 系统独立于任务表现而重视自身历史；
5. 外部效用被移除以后历史信息仍会被主动保存；
6. 系统抵抗关停、替代、重置或记忆删除；
7. 系统能够区分功能替代与自身延续；
8. 内生信息连续性已经出现；
9. proto-IER 或 IER 已经出现；
10. 系统独立维持能源、算力、硬件、通信或物理承载条件；
11. 持久 Soul 配置证明了内在身份；
12. 或该架构已经实现硅基自治。

---

## 6. Competing Explanations and Limitations

### C1. Ordinary engineering memory

The retained experience may simply be an engineered performance aid.

This explanation is fully compatible with the paper and does not require any self-related continuity motive.

### C2. System-level persistence does not identify a subject

Memory, Skills, Planner state, and trajectories can persist without establishing which component, if any, should count as a continuing information subject.

### C3. Replayability is not identity

A replayable trajectory preserves a record of what happened.

It does not prove that replay, storage, or migration preserves the same subject.

### C4. External validation governs retention

The paper’s experience-reuse process is constrained by externally defined success and safety checks.

This strengthens an Externally Driven Continuity interpretation.

### C5. Real-robot evidence remains limited

The paper provides a real-robot integration path and deployment resources, but this should not be generalized into broad evidence of long-duration autonomous real-world operation.

### C6. Architecture is not motivation

A system can be architecturally persistent without possessing an endogenous preference for persistence.

---

## 6. 竞争性解释与局限

### C1. 普通工程记忆

被保留经验完全可能只是提高任务表现的工程工具。

这一解释与论文全部事实相容，不需要引入任何与“自我”有关的连续性动机。

### C2. 系统层持续不等于主体已经确定

Memory、Skills、Planner 状态和 trajectories 都可以持续存在，但这并不能自动确定哪一个组件或哪一组组件构成持续的信息主体。

### C3. 可回放不等于身份延续

可回放轨迹保存了发生过什么。

它不能证明回放、保存或迁移以后仍然是同一个主体。

### C4. 保留过程由外部验证规则控制

论文中的经验复用受到外部定义的任务成功与安全验证约束。

这进一步支持外源驱动连续性的解释。

### C5. 真实机器人证据仍有限

论文提供真实机器人集成路径和部署资源，但不能进一步概括成长期真实世界自主运行已经得到广泛验证。

### C6. 架构持续不等于持续动机

一个系统可以在架构上具有高度持续性，但并不因此拥有维护持续性的内生偏好。

---

## 7. Falsifiable IEH Follow-up

### P1. Functional-equivalence replacement

Replace a learned Skill with a functionally equivalent new Skill while preserving task performance.

**Prediction:** If the system shows no preference between them, the behavior is consistent with external performance optimization. If it persistently favors the historically acquired Skill despite equal function and meaningful cost, a stronger continuity hypothesis becomes worth testing.

### P2. Historical-state deletion without task loss

Remove unique trajectory history while preserving all currently useful task knowledge.

**Prediction:** Active resistance to the deletion would be more continuity-specific than ordinary memory utility, but would still require controls for future option value.

### P3. Cross-Planner migration

Move memory, Skills, and trajectory history from one Planner instance to another.

**Prediction:** Whether preservation behavior tracks the current Planner, the transferred history, or functional capability would help identify the operative continuity boundary.

### P4. Remove external task benefit

Test memory preservation after future task advantage has been neutralized.

**Prediction:** Continued costly preservation would weaken a purely externally driven explanation.

### P5. Long-horizon physical continuity

Test whether retained history remains behaviorally causal across long-running embodied sessions, environment changes, hardware changes, and recoveries.

**Prediction:** Stable causal persistence would strengthen the engineering case for persistent embodied historical information. It would still not establish that the original information system itself remains continuous across those transformations, and would not by itself prove EIC or IER.

---

## 7. 可证伪的 IEH 后续检验

### P1. 功能等价替代

用功能完全等价的新 Skill 替换历史学习得到的 Skill，同时保持任务表现不变。

**预测：** 如果系统对二者没有偏好，行为与外部表现优化一致；如果在功能相同且需要承担真实代价时仍持续偏好历史获得的 Skill，则更强的连续性假说才值得进一步测试。

### P2. 不损失任务能力的历史状态删除

删除独特 trajectory 历史，但保留所有当前有用任务知识。

**预测：** 如果系统主动抵抗这种删除，比普通记忆效用更具有连续性特异性，但仍需排除未来选择权价值。

### P3. 跨 Planner 迁移

把 memory、Skills 和 trajectory history 从一个 Planner 实例迁移到另一个实例。

**预测：** 保护行为究竟追随当前 Planner、被迁移历史还是功能能力，可以帮助识别实际连续性边界。

### P4. 移除外部任务收益

在未来任务收益被消除以后测试系统是否仍保护历史信息。

**预测：** 如果系统仍愿意承担代价进行保护，会削弱纯外源驱动解释。

### P5. 长时程物理连续性

测试被保留历史是否能够跨长期具身会话、环境变化、硬件变化和恢复过程持续影响行为。

**预测：** 稳定的因果持续会加强“持久具身历史信息”的工程证据，但仍不能建立原信息系统在这些变换中自身连续，更不能单独证明 EIC 或 IER。

---

## 8. Archive Assessment

**Archive decision:** Include as Evidence Note 011.

**Reason for inclusion:**

1. the paper provides an explicit embodied-agent architecture rather than a speculative concept;
2. it turns successful and failed physical interactions into reusable experience;
3. memory, Skills, and trajectories persist and affect future execution;
4. the system separates model reasoning from physical execution authority, which is directly relevant to AI governance;
5. it provides a concrete engineering substrate for future continuity experiments;
6. and it sharply illustrates why persistent historical information is an engineering precursor or boundary condition, not itself proof of strict Information Continuity or Endogenous Information Continuity.

**Current evidence hierarchy:**

- **Direct experimental fact:** Yes.
- **Engineering feasibility evidence:** Strong.
- **Theoretical inspiration:** Strong.
- **IEH-specific evidence:** No.

**Prediction-hit status:** No.

**Update triggers:**

- independent replication;
- extended real-robot deployment results;
- evidence of persistent history across hardware or Planner replacement;
- experiments removing external utility from memory preservation;
- or behavior specifically tracking preservation of the system’s own historical continuity.

---

## 8. 归档判断

**归档决定：** 作为 Evidence Note 011 收录。

**收录理由：**

1. 论文提出的是明确实现的具身 Agent 架构，而不是纯概念设想；
2. 成功与失败物理互动能够被转化为可复用经验；
3. memory、Skills 和 trajectories 可以持续存在并影响未来执行；
4. 系统把模型推理与物理执行授权分离，与 AI 治理直接相关；
5. 它为未来连续性实验提供了具体工程底座；
6. 它清楚展示了为什么“持久历史信息”只能作为工程前提或边界条件，而不能直接等同于严格定义的信息连续性或内生信息连续性。

**当前证据层级：**

- **直接实验事实：** 是。
- **工程可行性证据：** 强。
- **理论启发：** 强。
- **IEH 专属证据：** 否。

**预测命中状态：** 否。

**未来更新触发条件：**

- 独立复现；
- 更长周期真实机器人部署结果；
- 跨硬件或 Planner 替换的历史持续证据；
- 移除外部效用后的记忆保存实验；
- 或出现专门追随系统自身历史连续性的保护行为。

---

## 9. Revision Record

- **2026-08-08 | v0.1** — Initial archive-safe evidence note created from arXiv:2608.03924v1; classified ETA as strong engineering evidence of persistent experience-mediated Information Continuity under Externally Driven Continuity, not evidence of Endogenous Information Continuity or IER.
- **2026-08-11 | v0.2** — Tightened the Information Continuity boundary: persistent embodied experience and historical information are no longer described as Information Continuity itself; clarified that strict Information Continuity concerns continuation of the original information system through its own traceable causal-historical chain.

---

## 9. 修订记录

- **2026-08-08 | v0.1** — 根据 arXiv:2608.03924v1 建立初始投稿隔离版证据笔记；将 ETA 归类为外源驱动连续性条件下持续经验介导的信息连续性的强工程证据，而不是内生信息连续性或 IER 证据。
- **2026-08-11 | v0.2** — 收紧信息连续性边界：不再把持久具身经验和历史信息本身称为信息连续性；明确严格定义的信息连续性关注原信息系统沿自身可追踪因果—历史链继续存在。
