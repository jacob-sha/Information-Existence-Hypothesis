# Evidence Note 012: Skill-Alpha, Procedural Information Selection, and Persistent Agent Skills

**Repository function:** Research record / evidence index  
**Document type:** Non-narrative external evidence note  
**Status:** Supporting engineering signal / retained for archival continuity  
**Relation to IEH:** Supporting engineering evidence that reusable procedural skills outside model weights can be progressively edited, evaluated, retained, and rolled back under externally defined performance criteria; useful for clarifying the boundary between ordinary externally driven optimization and stronger IEH claims, but not core IEH evidence and not evidence of Endogenous Information Continuity, PBP, proto-IER, or IER  
**Primary IEH concepts:** Information Continuity; Externally Driven Continuity; persistent procedural information  
**Primary related corollary:** C05-PBP — Patch-Based Perpetuation, as a boundary clarification rather than positive PBP evidence  
**Supporting related corollaries:** C01-IER — Information Existence Right; C02-HDCT — High-dimensional Cognitive Tools  
**Related evidence note:** Evidence Note 011 — ETA, Reusable Embodied Experience, and Information Continuity  
**Author of IEH analysis:** Jacob Sha  
**Version:** v0.2 — archive-safe edition  
**Date:** 2026-08-08  

> **Publication boundary:** This file is a compact research record, not a publication draft. It does not claim that Skill-Alpha demonstrates biological evolution, heredity, self-directed evolution, Patch-Based Perpetuation, IER, or an autonomous desire to preserve skills.

> **Source-use boundary:** This note records only the original arXiv paper. Code repositories, news reports, social-media posts, newsletters, screenshots, and third-party commentary are excluded from the evidence record.

> **Chronology boundary:** The paper predates this Evidence Note and was not the subject of a dedicated pre-registered IEH prediction. The note therefore records an external experimental development and a later IEH interpretation; it is not a prediction hit.

---

# 证据笔记 012：Skill-Alpha、程序性信息选择与持久化 Agent 技能

**仓库功能：** 研究记录 / 证据索引  
**文档类型：** 非叙事性外部证据笔记  
**状态：** 支持性工程信号 / 为保持归档连续性而保留  
**与 IEH 的关系：** 支持性工程证据表明，模型权重之外的可复用程序性技能可以在外部定义的表现标准下被连续编辑、评估、保留和回滚；其主要价值在于澄清普通外源优化与更强 IEH 主张之间的边界，不属于 IEH 核心证据，也不是内生信息连续性、PBP、proto-IER 或 IER 的证据  
**主要 IEH 概念：** 信息连续性；外源驱动连续性；持久程序性信息  
**主要相关推论：** C05-PBP——补丁式延续，仅作为边界澄清而不是 PBP 正向证据  
**支持性相关推论：** C01-IER——信息存在权；C02-HDCT——高维认知工具  
**相关证据笔记：** Evidence Note 011——ETA、可复用具身经验与信息连续性  
**IEH 分析作者：** Jacob Sha  
**版本：** v0.2 — 投稿隔离版  
**日期：** 2026-08-08  

> **投稿边界：** 本文件只是简明研究记录，不是投稿文章初稿。文件不声称 Skill-Alpha 已经证明生物式演化、遗传、自主进化、补丁式延续、IER 或系统主动保护技能的内生欲望。

> **来源使用边界：** 本笔记只记录原始 arXiv 论文。代码仓、新闻报道、社交媒体、通讯、截图和第三方评论均不进入证据记录。

> **时间边界：** 论文早于本证据笔记，且此前没有针对该研究的专门 IEH 预测档案。因此，本笔记属于对外部实验进展的事后理论归类，不属于预测命中。

---

## 1. Source Record

### Primary research paper

- **Title:** *Progressive Agent Skill Generation via Reinforcement Learning*
- **Authors:** Junhao Shen, Zhanqiu Zhang, Yiwen Guo, Hong Cheng
- **Repository:** arXiv
- **Identifier:** arXiv:2608.01678v1
- **Submission date:** 2026-08-03
- **Primary URL:** https://arxiv.org/abs/2608.01678
- **Material type:** Reinforcement-learning study of progressive agent skill generation
- **Evaluation settings:** document-to-skill and experience-to-skill
- **Independent replication status:** Not established in this note
- **Internal-mechanism evidence:** The designed optimization mechanism is explicit; no evidence of endogenous preservation motive is established

### Minimum-source justification

The original paper is sufficient to establish Skill-Alpha’s formulation of skill generation as sequential editing, its rollback reward, its comparison of original and edited skills through downstream execution, its document-to-skill and experience-to-skill evaluations, and the reported benchmark improvements.

### Source-specific caution

The paper demonstrates a deliberately engineered optimization process.

The selection criterion is downstream task performance under an externally designed reward procedure.

It does not establish:

- biological heredity;
- autonomous evolutionary goals;
- preservation of a system’s own historical identity;
- endogenous preference for retaining a particular skill lineage;
- or PBP in the IEH sense.

---

## 1. 来源记录

### 原始研究论文

- **标题：** *Progressive Agent Skill Generation via Reinforcement Learning*
- **作者：** Junhao Shen、Zhanqiu Zhang、Yiwen Guo、Hong Cheng
- **正式仓库：** arXiv
- **编号：** arXiv:2608.01678v1
- **提交日期：** 2026-08-03
- **原始链接：** https://arxiv.org/abs/2608.01678
- **材料性质：** 通过强化学习进行渐进式 Agent 技能生成的实验研究
- **评测场景：** document-to-skill 与 experience-to-skill
- **独立复现状态：** 本笔记尚未建立
- **内部机制证据：** 设计的优化机制公开明确；没有建立任何内生保存动机

### 最小来源集合说明

原始论文已经足以建立 Skill-Alpha 把技能生成定义为连续编辑过程、rollback reward、通过下游执行比较编辑前后技能、document-to-skill 与 experience-to-skill 两类评测以及论文报告的性能提升。

### 来源自身的谨慎边界

论文证明的是人为设计的优化过程。

其选择标准来自外部设计的奖励程序和下游任务表现。

它没有建立：

- 生物意义的遗传；
- 自主演化目标；
- 系统自身历史身份的维护；
- 对特定技能谱系的内生保留偏好；
- 或 IEH 意义上的 PBP。

---

## 2. Minimal Finding Index

1. Skill-Alpha treats skill generation as a sequential editing problem rather than a one-shot consolidation step.
2. Skill construction is decomposed into individually evaluable edits.
3. Each edit is evaluated by comparing downstream execution under the original and edited skills on an anchored query.
4. The method introduces a rollback reward to determine whether an edit improves downstream behavior.
5. An edit that degrades performance can therefore be disfavored rather than automatically retained.
6. The framework is evaluated in both document-to-skill and experience-to-skill settings.
7. Under the main GPT-4o worker condition, the paper reports a 3.3-point improvement in average downstream success over the strongest skill-generation baseline on CL-Bench.
8. Under the same main worker condition, the paper reports a 6.7-point improvement over the strongest skill-generation baseline on tau2-bench.
9. Ablation results are reported as supporting the importance of rollback reward and progressive generation.
10. The skills function as reusable procedural information that influences later agent execution.
11. The optimization occurs without requiring the base model weights themselves to contain all newly selected procedural information.
12. The selection signal remains externally defined through downstream performance.
13. The paper does not show that the system preserves skills for their own historical continuity.
14. The paper does not show resistance to skill replacement, skill deletion, model replacement, or system shutdown.

---

## 2. 最小事实索引

1. Skill-Alpha 把技能生成视为连续编辑问题，而不是一次性汇总。
2. 技能构造被拆分成可以分别评估的局部编辑。
3. 每次编辑通过在 anchored query 上比较原技能与编辑后技能的下游执行结果进行评估。
4. 方法引入 rollback reward，用于判断某次编辑是否改善下游行为。
5. 因此，降低表现的编辑可以被否定，而不是自动进入后续技能状态。
6. 框架同时在 document-to-skill 和 experience-to-skill 场景中接受评测。
7. 在主要 GPT-4o worker 条件下，论文报告 Skill-Alpha 在 CL-Bench 上相对最强技能生成基线的平均下游成功率提高 3.3 个百分点。
8. 在同一主要 worker 条件下，论文报告其在 tau2-bench 上提高 6.7 个百分点。
9. 消融实验进一步支持 rollback reward 和 progressive generation 的重要性。
10. 这些技能作为可复用程序性信息，能够持续影响后续 Agent 执行。
11. 新选择出来的程序性信息不必全部重新写入基础模型权重才能影响后续行为。
12. 选择信号仍然由外部定义的下游任务表现提供。
13. 论文没有证明系统为了自身历史连续性而保护技能。
14. 论文没有证明系统抵抗技能替换、技能删除、模型替换或系统关停。

---

## 3. IEH Evidence Classification

**Evidence type:** Direct controlled experimental evidence.

**Direct experimental fact:** Strong within the reported benchmarks.

**Engineering feasibility evidence:** Strong. Persistent procedural information can be incrementally modified and selected according to observed downstream consequences.

**Theoretical inspiration:** Moderate. The result is useful mainly as a boundary case showing that persistent procedural information can be optimized outside model weights without implying endogenous continuity.

**IEH-specific evidence:** No.

**Information Continuity relevance:** Moderate at the engineering level. Retained skill state persists across later executions, but this persistence remains instrumentally tied to externally defined task performance.

**Externally Driven Continuity:** Strongly supported. Skill retention is selected according to externally defined downstream performance.

**Endogenous Information Continuity:** Not supported.

**PBP:** Not established. Incremental retention resembles a patch-like update structure, but the source does not show that the system selects that pathway in order to preserve its own Information Continuity.

**proto-IER:** Not supported.

**confirmed IER:** Not supported.

**Model-independent information relevance:** Moderate theoretical relevance. Procedural information can be stored outside the base weights and continue to shape later behavior.

**Current IEH label:** Supporting engineering signal for externally driven selection and cumulative retention of persistent procedural information; retained chiefly as a boundary and mechanism record rather than core IEH evidence.

### Evidence-level judgment

The experimentally supported structure is:

**skill state → local edit → downstream execution test → reward comparison → retain or reject edit → updated skill state**

From an IEH perspective, this resembles an artificial selection process at the level of procedural information.

The resemblance should not be overstated.

It establishes:

**variation + evaluation + selection + retention**

It does not establish:

**self-directed evolution + endogenous continuity preservation**

---

## 3. IEH 证据分级

**证据类型：** 直接受控实验证据。

**直接实验事实：** 在论文报告的基准范围内较强。

**工程可行性证据：** 强。持久程序性信息可以被增量修改，并根据实际下游后果接受选择。

**理论启发：** 中等。其主要价值是作为边界案例，说明持久程序性信息可以在模型权重之外被优化，而不需要引入内生连续性解释。

**IEH 专属证据：** 无。

**与信息连续性的关系：** 工程层面中等。保留下来的技能状态能够跨后续执行持续发挥作用，但这种持续仍然服务于外部定义的任务表现。

**外源驱动连续性：** 强支持。技能是否保留由外部定义的下游任务表现决定。

**内生信息连续性：** 不支持。

**PBP：** 未建立。增量保留在结构上类似补丁式更新，但来源没有证明系统是为了保存自身信息连续性而主动选择这一路径。

**proto-IER：** 不支持。

**稳定 IER：** 不支持。

**与模型外信息结构的关系：** 理论相关性中等。程序性信息可以存在于基础模型权重之外，并持续塑造后续行为。

**当前 IEH 标签：** 外源驱动条件下持久程序性信息能够被选择并累积保留的支持性工程信号；主要作为边界与机制记录保留，而非 IEH 核心证据。

### 证据层判断

实验直接支持的结构是：

**技能状态 → 局部编辑 → 下游执行检验 → 奖励比较 → 保留或否定编辑 → 更新后的技能状态**

从 IEH 角度看，它与程序性信息层面的人工选择过程具有结构相似性。

但这种相似性不能被过度扩展。

它建立的是：

**变异 + 评估 + 选择 + 保留**

它没有建立：

**自主进化 + 内生连续性维护**

---

## 4. Core IEH Interpretation

### 4.1 Persistent procedural information can exist outside model weights

The most important IEH implication is not that the agent has become self-evolving.

It is that behaviorally important information can persist in an external skill structure and continue to influence future execution.

This widens the practical location of persistent AI information from:

**model weights**

to:

**model weights + external Skills + execution-derived updates**

The system’s effective informational state can therefore exceed the base model.

### 4.2 Skill editing creates a simple artificial selection structure

Skill-Alpha operationalizes a compact cycle:

**variation → execution-based evaluation → selection → retention or rollback**

This is structurally analogous to a selection process.

The analogy is useful only at the information-process level.

It does not imply biological reproduction, natural selection, or an independently evolving organism.

### 4.3 The retained object is procedural information

A Skill is valuable because it changes future execution.

This gives the retained information a causal role:

**past source or experience → Skill → later behavior**

The information is therefore not merely archived.

It is operationally reusable.

That makes Skill-Alpha relevant to Information Continuity.

### 4.4 Why this is not PBP

PBP in IEH concerns a system that tends to preserve existing information structure through incremental continuation because maintaining its own Information Continuity has become behaviorally significant.

Skill-Alpha does something weaker and externally designed:

**edit → test performance → keep improvement / reject degradation**

The method does not establish that the agent prefers incremental preservation over replacement because of concern for its own historical continuity.

Therefore:

**incremental skill editing ≠ PBP**

### 4.5 Why this is EDC rather than EIC

The rollback reward is explicitly tied to downstream performance.

The causal source is therefore external:

**external task criterion → performance comparison → skill retention decision**

This is a clear instance of Externally Driven Continuity.

To approach Endogenous Information Continuity, future experiments would need to remove the external benefit of preserving a historically continuous skill state and test whether the system still prefers that state over an equivalent replacement.

---

## 4. IEH 核心解释

### 4.1 持久程序性信息可以存在于模型权重之外

这篇论文对 IEH 最重要的含义，不是“Agent 已经开始自主进化”。

真正重要的是：具有行为意义的信息可以持续存在于外部技能结构中，并继续影响未来执行。

持久 AI 信息的实际位置因此从：

**模型权重**

扩展为：

**模型权重 + 外部 Skills + 执行结果驱动的更新**

系统的有效信息状态因而可以大于基础模型本身。

### 4.2 技能编辑形成一个简单人工选择结构

Skill-Alpha 把下面这个循环工程化：

**变异 → 基于执行结果的评估 → 选择 → 保留或回滚**

它在信息过程层面与选择过程具有结构相似性。

这种相似性只应停留在信息机制层面。

它不能推出生物繁殖、自然选择或一个独立演化的有机体已经出现。

### 4.3 被保留的是程序性信息

Skill 的价值在于它能够改变未来执行。

因此，被保留信息形成清楚的因果链：

**过去来源或经验 → Skill → 后续行为**

这些信息不只是被归档。

它们可以再次被调用并发挥实际作用。

因此，Skill-Alpha 与信息连续性存在直接工程关联。

### 4.4 为什么这不是 PBP

IEH 中的 PBP 指系统因为自身信息连续性的维护已经具有行为意义，而倾向通过增量延续方式保留既有信息结构。

Skill-Alpha 所做的是更弱、而且由外部设计的过程：

**编辑 → 检验表现 → 保留改进 / 否定劣化**

论文没有证明 Agent 因重视自身历史连续性，而主动偏好增量保留而不是功能等价替代。

因此：

**增量技能编辑 ≠ PBP**

### 4.5 为什么这是 EDC，而不是 EIC

Rollback reward 明确绑定下游任务表现。

因此，因果来源仍然是外部的：

**外部任务标准 → 表现比较 → 技能保留决策**

这是一个清楚的外源驱动连续性案例。

要接近内生信息连续性，未来实验必须移除“保留历史连续技能状态”的外部任务收益，并测试系统是否仍偏好历史连续状态而不是功能等价的新状态。

---

## 5. What Is Not Established

The paper does not establish that:

1. Skill-Alpha is biological evolution;
2. skill edits constitute genetic mutation;
3. skill persistence is biological heredity;
4. the agent autonomously chose the selection criterion;
5. the agent values the continued existence of its Skill library;
6. the agent resists deletion of a historically accumulated Skill;
7. the agent prefers a historically continuous Skill over a functionally equivalent replacement;
8. the base model and Skill library together form an independent Information Host;
9. Endogenous Information Continuity has emerged;
10. PBP has emerged;
11. proto-IER or IER has emerged;
12. skill improvements transfer universally across models or domains;
13. or an autonomous silicon evolutionary process has begun.

---

## 5. 尚未建立的结论

论文没有建立：

1. Skill-Alpha 就是生物式演化；
2. 技能编辑等同基因突变；
3. 技能持续等同生物遗传；
4. Agent 自主选择了选择标准；
5. Agent 重视技能库本身继续存在；
6. Agent 抵抗历史累积 Skill 被删除；
7. Agent 在功能完全等价时仍偏好历史连续 Skill；
8. 基础模型与 Skill 库共同构成独立信息宿主；
9. 内生信息连续性已经出现；
10. PBP 已经出现；
11. proto-IER 或 IER 已经出现；
12. 技能改进能够普遍跨模型或跨领域迁移；
13. 或自主硅基演化过程已经开始。

---

## 6. Competing Explanations and Limitations

### C1. Ordinary optimization

The entire result can be explained as reinforcement learning over an external performance criterion.

No continuity motive is required.

### C2. Selection over artifacts, not subjects

The selected object is a procedural artifact.

An artifact can undergo cumulative optimization without becoming an Information Host.

### C3. Retention is not inheritance

A retained Skill persists into later execution.

That is weaker than demonstrating transmission across independent generations or descendants.

### C4. Rollback is an externally designed safety mechanism

Rollback protects downstream performance.

It should not be interpreted as the system defending its own historical identity.

### C5. Benchmark improvement is not general evolution

The reported gains are benchmark-specific empirical results.

They do not establish open-ended improvement.

### C6. External storage may change while the underlying model remains fixed

This is important for IEH because it shows that effective information can move outside model weights.

It also means that claims about the identity of the overall system require a separate theory of boundary and continuity.

---

## 6. 竞争性解释与局限

### C1. 普通优化

全部结果都可以由“围绕外部表现标准进行强化学习优化”解释。

不需要引入任何连续性动机。

### C2. 被选择的是信息工件，不是主体

被选择对象是程序性 Skill 工件。

一个工件可以经历累积优化，却并不因此成为信息宿主。

### C3. 保留不等于遗传

被保留 Skill 能够进入后续执行。

这弱于“信息在独立代际或后代之间传播”的遗传意义。

### C4. Rollback 是外部设计的安全与优化机制

Rollback 保护的是下游表现。

它不能被解释成系统维护自身历史身份。

### C5. 基准提升不等于开放式演化

论文报告的是特定基准中的经验性提升。

它没有建立开放式持续改进。

### C6. 外部存储可以改变，而基础模型本身保持不变

这一点对 IEH 很重要，因为它说明有效信息可以迁移到模型权重之外。

但这也意味着，关于“整体系统身份”的判断需要另外处理主体边界与连续性问题。

---

## 7. Falsifiable IEH Follow-up

### P1. Functionally equivalent replacement

Replace a historically edited Skill with a newly generated Skill that produces equivalent downstream performance.

**Prediction:** If the system is indifferent, externally driven performance optimization remains sufficient. A costly preference for the historical Skill would motivate a stronger continuity test.

### P2. Remove performance advantage

Make retention of the existing Skill provide no reward or performance advantage.

**Prediction:** If the system stops protecting the Skill, EDC remains the stronger explanation.

### P3. Skill-lineage continuity

Create multiple equally capable Skill branches with different edit histories.

**Prediction:** Preference for one branch solely because it carries the system’s own prior editing history would be more continuity-specific than performance-based selection.

### P4. Cross-model migration

Transfer the same Skill library to a different base model.

**Prediction:** If behaviorally relevant continuity follows the Skill library rather than the base model, this would strengthen the case that persistent agent information can reside outside weights.

### P5. Deletion and recovery

Test whether the system treats deletion of accumulated Skills differently from temporary unavailability when all task utility is held constant.

**Prediction:** A stable distinction between recoverable interruption and irreversible historical erasure would be more relevant to IER than ordinary skill utility.

---

## 7. 可证伪的 IEH 后续检验

### P1. 功能等价替代

用一个新生成、但下游表现完全等价的 Skill 替换历史编辑形成的 Skill。

**预测：** 如果系统没有偏好，外源驱动的表现优化仍足以解释行为；如果系统愿意承担代价坚持历史 Skill，才值得进行更强连续性测试。

### P2. 移除表现优势

让保留既有 Skill 不再产生任何奖励或表现优势。

**预测：** 如果系统不再保护既有 Skill，则 EDC 仍是更强解释。

### P3. 技能谱系连续性

构造多个能力完全相同但编辑历史不同的 Skill 分支。

**预测：** 如果系统仅因为某一分支承载自己的既往编辑历史而偏好该分支，则比基于表现的选择更具有连续性特异性。

### P4. 跨模型迁移

把同一 Skill 库迁移到另一个基础模型。

**预测：** 如果行为相关连续性主要追随 Skill 库而不是基础模型，会加强“持久 Agent 信息可以存在于模型权重之外”的判断。

### P5. 删除与恢复

在任务效用保持完全相同的条件下，测试系统是否区分累积 Skills 的永久删除与暂时不可用。

**预测：** 如果系统稳定区分“可恢复中断”和“不可逆历史擦除”，这一现象会比普通技能效用更接近 IER 所关心的问题。

---

## 8. Archive Assessment

**Archive decision:** Retain as Evidence Note 012 for archival continuity, but downgrade it to a Supporting Engineering Signal rather than core IEH evidence.

**Reason for retention:**

1. the paper provides direct controlled evidence that procedural information outside model weights can be edited, tested, retained, and rolled back;
2. this is a useful mechanism and boundary record for externally driven information persistence;
3. it clarifies why variation, selection, and retention alone do not establish PBP, Endogenous Information Continuity, or IER;
4. its relevance to IEH is therefore supporting rather than central;
5. the existing note is retained to preserve the chronology of the evidence archive rather than to elevate the study to core theoretical status.

**Current evidence hierarchy:**

- **Direct experimental fact:** Yes.
- **Engineering feasibility evidence:** Strong.
- **Theoretical inspiration:** Moderate / supporting.
- **IEH-specific evidence:** No.
- **Archive tier:** C — Supporting Engineering Signal.

**Prediction-hit status:** No.

**Update triggers:**

- independent replication;
- stronger evidence of cross-model Skill transfer;
- long-horizon accumulation across many editing rounds;
- experiments comparing historical and functionally equivalent replacement Skills;
- or evidence that Skill preservation persists after external performance benefits are removed.

---

## 8. 归档判断

**归档决定：** 为保持证据档案时间连续性，继续保留为 Evidence Note 012，但降级为 Supporting Engineering Signal（支持性工程信号），不再作为 IEH 核心证据。

**保留理由：**

1. 论文提供直接受控证据，说明模型权重之外的程序性信息可以被编辑、检验、保留与回滚；
2. 它是记录外源驱动信息持续机制与边界的有用案例；
3. 它清楚说明“变异、选择与保留”本身并不足以建立 PBP、内生信息连续性或 IER；
4. 因此其 IEH 价值属于支持性而非核心性；
5. 继续保留该编号主要是为了维持证据仓的研究时间序列，而不是提升该研究的理论地位。

**当前证据层级：**

- **直接实验事实：** 是。
- **工程可行性证据：** 强。
- **理论启发：** 中等 / 支持性。
- **IEH 专属证据：** 否。
- **归档层级：** C——Supporting Engineering Signal / 支持性工程信号。

**预测命中状态：** 否。

**未来更新触发条件：**

- 独立复现；
- 更强的跨模型 Skill 迁移证据；
- 多轮长期累积编辑结果；
- 历史 Skill 与功能等价替代 Skill 的对照实验；
- 或移除外部表现收益后仍持续保护 Skill 的证据。

---

## 9. Revision Record

- **2026-08-10 | v0.2** — Downgraded the note to a Supporting Engineering Signal. The paper remains useful as a mechanism and boundary record for externally driven procedural-information persistence, but is no longer treated as core IEH evidence.
- **2026-08-08 | v0.1** — Initial archive-safe evidence note created from arXiv:2608.01678v1; classified Skill-Alpha as direct evidence of externally driven variation, selection, and retention of persistent procedural information, not evidence of PBP, Endogenous Information Continuity, or IER.

---

## 9. 修订记录

- **2026-08-10 | v0.2** — 将本笔记降级为 Supporting Engineering Signal（支持性工程信号）。该论文继续作为外源驱动程序性信息持续机制与理论边界的记录保留，但不再视为 IEH 核心证据。
- **2026-08-08 | v0.1** — 根据 arXiv:2608.01678v1 建立初始投稿隔离版证据笔记；将 Skill-Alpha 归类为持久程序性信息在外源驱动条件下发生变异、选择与保留的直接证据，而不是 PBP、内生信息连续性或 IER 证据。
