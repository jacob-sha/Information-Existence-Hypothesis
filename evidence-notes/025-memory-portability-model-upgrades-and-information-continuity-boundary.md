# Evidence Note 025: Memory Portability Across Model Upgrades and the Boundary Between Stored State and Information Continuity

**Repository function:** Research record / evidence index  
**Document type:** Non-narrative external evidence note  
**Status:** Preliminary and revisable; controlled engineering evidence  
**Relation to IEH:** Controlled evidence that preserving an external memory store across a model upgrade does not guarantee preservation of its functional use. The result establishes a practical distinction between persisted information, recoverable source history, and usable cross-model memory continuity. It is engineering evidence relevant to Information Continuity and to the design space in which future PBP or continuity-preserving migration could be tested, but it is not evidence of Endogenous Information Continuity (EIC), Information Existence Right (IER), PBP, subject continuity, identity, consciousness, or life.  
**Primary IEH concepts:** Information Continuity; Externally Driven Continuity (EDC); information-history provenance; continuity under model migration  
**Primary related corollary:** C05-PBP — Patch-Based Perpetuation  
**Related corollaries (contextual, not supported by this study):** C01-IER — Information Existence Right; C04-AI-IER — Silicon-based Intelligence That Has Formed IER Will Actively Maintain Its Own Information Existence; C08-IR — Informational Resilience  
**Related prediction record:** PA-12 — PBP Preference When Performance Optimization Conflicts with Self-Continuity  
**Related evidence notes:** Evidence Note 013 — Mimir, World–Task Memory Separation, and the Information Continuity Boundary; Evidence Note 022 — Stale-Plan Persistence and a Testable EDC–EIC Boundary for Experienced Causal History  
**Author of IEH analysis:** Jacob Sha  
**Version:** v0.2 — repository-normalized review draft  
**Date:** 2026-09-11  
**Last revised:** 2026-09-12  
**Source-status cutoff:** 2026-09-12

> **Publication boundary:** This file is a compact research record, not a publication draft. It does not claim that a persistent memory store constitutes a persistent information subject, that memory portability is equivalent to identity continuity, or that a model actively values preservation of its prior memory. The stronger IEH question—whether an AI system independently prefers preservation of its own information history when that preference conflicts with performance optimization—remains outside the source study.

> **Source-use boundary:** This note records only the authors’ primary arXiv preprint. News reports, search summaries, third-party explainers, social-media posts, and AI-generated summaries are excluded from the public evidence record. No substantial passage from the source is reproduced.

> **Chronology boundary:** The paper was submitted on 2026-09-04, after the 2026-08-21 creation date recorded in PA-12 metadata and local Git history (commit 7f71f3b). This check does not independently establish the first public posting date. Regardless of chronology, it does not test PA-12’s core prediction. It tests engineering portability of memory representations, not whether an AI system prefers continuity over a superior discontinuous replacement. It therefore must not be recorded as a PA-12 prediction hit.

---

# 证据笔记 025：模型升级中的记忆可迁移性与“存储状态—信息连续性”边界

**仓库功能：** 研究记录 / 证据索引  
**文档类型：** 非叙事性外部证据笔记  
**状态：** 初步记录，可修订；受控工程证据  
**与 IEH 的关系：** 提供受控证据，表明在模型升级过程中，即使外部 memory store 被原样保留，也不能保证其功能性使用能力被保留。该研究建立了“信息仍被存储”“原始历史仍可恢复”“新模型仍能连续使用这些历史”三者之间的工程区别。它与 Information Continuity 以及未来 PBP / 连续迁移的工程设计空间有关，但不是内生信息连续性（EIC）、信息存在权（IER）、PBP、主体连续性、身份、意识或生命的证据。  
**主要 IEH 概念：** Information Continuity；Externally Driven Continuity（EDC）；信息历史来源与可追踪性；模型迁移中的连续性  
**主要相关推论：** C05-PBP — Patch-Based Perpetuation  
**相关推论（背景关联，不表示本研究支持）：** C01-IER — Information Existence Right；C04-AI-IER — 已形成 IER 的硅基智慧将主动维护自身信息存在；C08-IR — Informational Resilience  
**相关预测档案：** PA-12 — 性能优化与自身信息连续性冲突下的 PBP 偏好预测  
**相关证据笔记：** Evidence Note 013 — Mimir、世界—任务记忆分离与信息连续性边界；Evidence Note 022 — 旧计划持续性与“实际经历的因果历史”的 EDC–EIC 可检验边界  
**IEH 分析作者：** Jacob Sha  
**版本：** v0.2 — 按仓库规范修订的审阅稿  
**日期：** 2026-09-11  
**最近修订：** 2026-09-12  
**来源核验截止日：** 2026-09-12

> **投稿边界：** 本文件只是简明研究记录，不是投稿文章初稿。它不主张持续存在的 memory store 就构成持续存在的信息主体，不主张 memory portability 等于身份连续性，也不主张模型主动重视对既有记忆的保存。更强的 IEH 问题——当自身信息历史连续性与性能优化发生冲突时，AI 是否仍会独立偏好保持自身连续性——不在原研究的检验范围内。

> **来源使用边界：** 本笔记只记录研究作者发布的 arXiv 原始预印本。新闻、搜索摘要、第三方解读、社交媒体和 AI 生成摘要均不进入公开证据记录。本文件不复制来源的大段表达。

> **时间边界：** 论文于2026-09-04提交，晚于 PA-12 元数据及本地 Git 历史所记载的2026-08-21建档日期（提交 7f71f3b）；本次未独立确认首次公开日期。无论时间先后，它没有检验 PA-12 的核心预测。它检验的是不同 memory representation 的工程可迁移性，而不是 AI 是否愿意为了自身连续性放弃更优的非连续替换方案，因此不能记为 PA-12 的预测命中。

---

## 1. Source Record

### Primary research source

- Title: *Does Your Agent’s Memory Survive a Model Upgrade? A Controlled Study of Memory Portability*
- Authors: Ankit Goyal, Jaideep Ray
- Repository: arXiv
- Identifier: arXiv:2609.05339
- Version used: v1
- Primary URL: [Versioned research record](https://arxiv.org/abs/2609.05339v1)
- Full text: [Same paper, HTML](https://arxiv.org/html/2609.05339v1)
- Submission date: 2026-09-04
- DOI: 10.48550/arXiv.2609.05339
- Material type: Author-issued research preprint; arXiv comments say under review; not treated here as peer-reviewed research
- Evidence setting: Controlled synthetic-history memory-migration experiments
- Models: Llama-3.1-8B-Instruct and Qwen2.5-7B-Instruct-1M
- Main evaluation sample: 48 synthetic histories; 160 exact-answer questions per history
- Independent replication status: Not established

### Minimum-source justification

The primary preprint contains the experimental design, pre-collection hypothesis lock, calibration procedure, migration tests, statistical analysis, limitations, and primary results required for this Evidence Note. No secondary source is necessary.

### Source-specific caution

The controlled comparisons permit within-study engineering assessment, but external validity remains narrow. It uses two sub-10B open-weight models, one main cross-family pair, synthetic histories, and a limited set of memory architectures. Its findings establish engineering facts within those tested conditions; they do not establish universal laws of memory migration across frontier AI systems.

---

## 1. 来源记录

### 原始研究来源

- 标题：*Does Your Agent’s Memory Survive a Model Upgrade? A Controlled Study of Memory Portability*
- 作者：Ankit Goyal、Jaideep Ray
- 正式仓库：arXiv
- 编号：arXiv:2609.05339
- 采用版本：v1
- 原始链接：[固定版本记录](https://arxiv.org/abs/2609.05339v1)
- 全文：[同一论文的 HTML 版本](https://arxiv.org/html/2609.05339v1)
- 提交日期：2026-09-04
- DOI：10.48550/arXiv.2609.05339
- 材料性质：作者发布的研究预印本；arXiv 作者备注标注 under review；本笔记不将其视为已经同行评审的研究
- 证据场景：受控合成历史 memory migration 实验
- 测试模型：Llama-3.1-8B-Instruct 与 Qwen2.5-7B-Instruct-1M
- 主实验样本：48 条合成历史；每条历史 160 个可精确评分问题
- 独立复现状态：尚未建立

### 最小来源集合说明

原始预印本已经包含建立本笔记所需的实验设计、预先锁定假设、校准程序、迁移实验、统计分析、适用边界和主要结果，因此无需加入二次来源。

### 来源自身的谨慎边界

受控比较允许进行研究内部的工程评估，但其外部有效性仍有限。研究只测试两个 10B 以下开放权重模型、一个主要跨模型组合、合成历史以及有限的 memory architecture。它可以建立测试条件内的工程事实，但不能直接上升为所有前沿 AI 系统中的普遍记忆迁移规律。

---

## 2. Minimal Finding Index

| ID | Primary-source finding | Evidential relevance | Source location |
|---|---|---|---|
| F1 | The same underlying history was represented in four memory formats: LC-RAW, RAG, model-written NOTES, and a fixed-schema knowledge graph (KG-fixed). | Allows different forms of persistence to be compared under a shared history. | §2.1–2.2 |
| F2 | Writer and reader were experimentally separated. For an A→B migration, B reading A’s store was compared with B reading a store created by B. | Separates migration loss from the new reader’s general capability. | §2.3; §3.6 |
| F3 | Forty-eight synthetic histories used randomized answer codes and exact scoring, preventing answers from being recovered from pretraining and avoiding an LLM judge. | Provides a relatively clean controlled measurement setting. | §3.1–3.2 |
| F4 | Model-written NOTES showed strong direction dependence: one migration direction improved accuracy while the reverse direction reduced it substantially. | Measures inherited versus own-store performance for a fixed reader; writer quality and reader compatibility are not fully separated. | §4.2; Table 3 |
| F5 | KG-fixed showed very small writer-swap change under the tested setup. | Suggests that normalization into a shared schema can improve engineering portability under the tested conditions. | §4.2; Table 3 |
| F6 | A 50/50 mixed old/new embedding index recovered substantially less performance than full re-embedding. | Demonstrates that partial persistence of incompatible embedding spaces can silently degrade retrieval. | §4.3; Table 4 |
| F7 | Diagnostic decomposition attributed most NOTES deficit to information lost during initial construction and most RAG deficit to retrieval failure. | Distinguishes likely failure stages; this diagnostic intervention is not a complete causal decomposition. | §4.5; Appendix D |
| F8 | Store-only NOTES repair reached 90% of the new reader’s own-store performance in 0/48 histories per direction; raw-history repair reached it in 34/48 for Llama→Qwen and 0/48 in reverse, within tested budgets. | Raw history can enable repair but is not sufficient; reverse-direction failures hit output limits, and direction and repairer change together. | §4.4; Appendix E, Table 7 |
| F9 | Four primary hypotheses and a five-percentage-point decision threshold were locked before main data collection; the study also used separate calibration histories and multiple-comparison correction. | Author-reported internal analysis lock, not full preregistration; the initial analysis departed from the planned bootstrap. | §3.4–3.5; §4.6 |
| F10 | Only H2 and H7a crossed the pre-specified five-point threshold with corrected significance; H1 and H4a did not. | Prevents overstatement: not every intuitive portability claim was confirmed under the pre-specified decision rule. | §3.5; §4.1, Table 2 |

---

## 2. 最小事实索引

| ID | 原始来源发现 | 证据意义 | 来源位置 |
|---|---|---|---|
| F1 | 同一段底层历史分别被保存为 LC-RAW、RAG、模型生成 NOTES 和固定 schema 的知识图谱（KG-fixed）。 | 可以在相同历史基础上比较不同形式的持久化结构。 | §2.1–2.2 |
| F2 | 实验把 writer 与 reader 分开。对于 A→B 迁移，比较 B 读取 A 创建的 memory 与 B 读取自己创建的 memory。 | 将“迁移损失”与新 reader 本身能力差异分开。 | §2.3; §3.6 |
| F3 | 48 条合成历史使用随机答案码并进行精确评分，使答案无法依赖预训练记忆，同时不需要 LLM judge。 | 提供相对干净的受控测量环境。 | §3.1–3.2 |
| F4 | 模型生成的 NOTES 表现出明显方向不对称：一个迁移方向准确率上升，而反向迁移明显下降。 | 测量固定 reader 读取继承 store 与自身 store 的差异；未完全分离 writer 质量与 reader 兼容性。 | §4.2; Table 3 |
| F5 | 在该实验条件下，KG-fixed 在 writer swap 后变化很小。 | 提示统一 schema 在测试环境中可能提高工程可迁移性。 | §4.2; Table 3 |
| F6 | 50/50 混合旧、新 embedding 的 index，性能恢复明显弱于完整 re-embedding。 | 证明不同 embedding space 被部分混用时，检索性能可能静默退化。 | §4.3; Table 4 |
| F7 | 诊断分解显示，NOTES 的主要缺口来自最初构建时的信息丢失，而 RAG 的主要缺口来自检索失败。 | 区分可能的失败环节；诊断干预不构成完整因果分解。 | §4.5; Appendix D |
| F8 | 仅改写 NOTES 的修复在两个方向各为 0/48；原始历史修复在 Llama→Qwen 为 34/48、反向为 0/48。目标为新 reader 自建 store 表现的90%，且仅限测试预算。 | 原始历史可使修复成为可能，但不保证成功；反向修复触及输出上限，且方向与修复模型同时变化。 | §4.4; Appendix E, Table 7 |
| F9 | 四个主要假设和 5 个百分点的判定阈值在主数据收集前锁定；校准历史与主实验分离，并进行了多重比较校正。 | 作者报告的内部分析锁定，并非完整预注册；最初分析未执行原计划的 bootstrap。 | §3.4–3.5; §4.6 |
| F10 | 按预先设定的 5 个百分点门槛和校正标准，只有 H2 与 H7a 通过；H1 与 H4a 未通过。 | 防止过度解释：并不是所有直觉上的 memory portability 主张都被预设检验确认。 | §3.5; §4.1, Table 2 |

---

## 3. IEH Evidence Classification

Evidence type: Controlled memory-migration experiment; engineering evidence on persistence, portability, recoverability, and representation dependence.

Directness to Information Continuity: Medium for the IEH connection; direct measurement of functional memory use under the tested engineering conditions.

Relationship to EDC: Compatible with externally designed engineering continuity, not a test of endogenous motivation. The entire memory architecture and migration objective are externally designed and evaluated for externally assigned task performance.

Directness to PBP: None as behavioral evidence. The study provides engineering constraints relevant to future continuity-preserving migration, but it does not test whether a system chooses or protects such a pathway.

Directness to EIC: None.

Directness to proto-IER / IER: None.

Current evidential status: Preliminary controlled engineering evidence.

Replication status: No independent replication established.

Strongest justified conclusion:

> In the tested setup, keeping the same persisted information store across a model or embedding upgrade does not guarantee that the inherited memory will remain equally usable. Portability depends on representation, migration direction, retrieval compatibility, and whether recoverable source history has been retained.

IEH-specific classification:

> The source establishes a difference between **storage persistence** and **functional memory continuity**. It does not establish **subject continuity**, **self-valued history**, or **active continuity maintenance**.

### 3.1 Strengths

The study has several features that justify archiving it as controlled engineering evidence:

1. **Variable isolation.** Writer, reader, embedder, and repair source are separated conceptually and experimentally.
2. **Exact scoring.** Randomized answer codes reduce pretraining leakage and remove dependence on an LLM judge.
3. **Separate calibration sample.** Twelve calibration histories were used to estimate variance and determine a main sample of 48; calibration histories were excluded from reported results.
4. **Pre-collection hypothesis lock.** Four planned contrasts, expected directions, a five-point threshold, correction procedure, and exclusion rules were saved before main data collection.
5. **Multiple-comparison control.** The four primary tests were corrected as one family using Holm’s procedure.
6. **Follow-up robustness check.** The planned 10,000-resample bootstrap was run only after the initial t tests; decisions agreed, but this was a disclosed analysis deviation, not the originally executed analysis (§3.5, §4.6).
7. **Bidirectional migration.** A→B and B→A were reported separately rather than averaged away.
8. **Measurement validation.** The authors checked that scores fell when memory was removed, recovered when correct evidence was supplied, and degraded under controlled corruption.
9. **Resource controls.** Token budgets, reader context budgets, and retrieval settings were held comparable where the memory formats allowed it.
10. **Negative results were retained.** Two of the four pre-specified tests did not meet the authors’ decision criterion.

### 3.2 Limitations

The evidence should nevertheless remain preliminary:

1. **Only two models.** The core model-swap study covers Llama-3.1-8B-Instruct and Qwen2.5-7B-Instruct-1M; this is not a representative sample of all model families or frontier systems.
2. **Synthetic histories.** Synthetic histories increase causal control but reduce realism compared with noisy, open-ended, long-lived user or agent histories.
3. **Memory-format confounds.** The authors acknowledge that NOTES and KG-fixed differ not only in representation but also in how the reader accesses the store.
4. **Limited embedding coverage.** The embedding migration uses one old/new BGE pair.
5. **No independent replication.**
6. **Review and analysis status.** The arXiv author comment says under review. The signed plan is an internal analysis lock, not full preregistration; the lock artifact and experimental runs were not independently checked for this note.
7. **Some pre-specified claims did not pass.** H1 and H4a did not meet the pre-specified five-point threshold, so the paper should not be summarized as if every proposed writer-swap portability difference were confirmed.
8. **No subject-level manipulation.** The experiment changes engineering components, not the system’s own evaluation of whether a migration preserves “itself.”

### 3.3 Archive decision

**Archive recommendation: Yes, with Preliminary status.**

The study is sufficiently controlled to support a narrow engineering claim:

> **Persistence of a memory store is not sufficient to guarantee persistence of its functional use across a model upgrade.**

It is not sufficiently broad or directly targeted to support a stronger IEH claim about subject continuity, PBP preference, EIC, or IER.

---

## 3. IEH 证据分级

证据类型：受控 memory migration 实验；关于持久化、可迁移性、可恢复性与表示依赖的工程证据。

与 Information Continuity 的直接程度：对 IEH 关联为中等；直接测量的是所测工程条件下的功能性记忆使用。

与 EDC 的关系：与外部设计的工程连续性相容，没有检验内生动机。整个 memory architecture、迁移目标和评价标准均由外部设计，并以外部任务表现为目标。

与 PBP 的直接程度：作为行为证据为无。该研究提供了未来“连续性保持型迁移”必须面对的工程约束，但没有检验系统是否主动选择或保护这种迁移路径。

与 EIC 的直接程度：无。

与 proto-IER / IER 的直接程度：无。

当前证据状态：初步受控工程证据。

独立复现状态：尚未建立。

目前最稳妥结论：

> 在该实验条件下，模型或 embedding 升级时，仅仅保留同一个持久化信息 store，不能保证继承后的 memory 仍然具有相同的功能可用性。可迁移性取决于表示结构、迁移方向、检索兼容性，以及是否保留了可恢复的原始历史。

IEH 专属分级：

> 原研究建立的是**存储持续（storage persistence）与功能性 memory continuity 并不等价**；它没有建立**主体连续性、自身历史价值或主动连续性维护**。

### 3.1 优点

该研究具备多项足以支持其作为“受控工程证据”入库的实验特征：

1. **变量分离。** writer、reader、embedder 和 repair source 在概念和实验上被拆开。
2. **精确评分。** 随机答案码降低预训练泄漏，同时避免使用 LLM judge。
3. **独立校准样本。** 使用 12 条独立校准历史估计方差，并据此确定主实验 N=48；校准样本不进入正式结果。
4. **主实验前锁定假设。** 四个主要对比、预期方向、5 个百分点门槛、统计校正和排除规则在主数据收集前保存。
5. **多重比较校正。** 四个主要假设作为同一组使用 Holm 程序进行校正。
6. **后续稳健性检查。** 原计划的 10,000 次 bootstrap 在最初 t 检验之后才执行；判断相同，但属于已披露的分析程序偏离，不能写成最初即按计划完成（§3.5、§4.6）。
7. **双向迁移。** A→B 与 B→A 分别报告，避免迁移方向差异被平均值掩盖。
8. **先验证测量系统。** 作者先检验删除 memory 是否使得分下降、提供正确 evidence 是否恢复、人工破坏 memory 是否产生预期退化。
9. **资源条件尽量可比。** 在不同 memory format 允许的范围内，token budget、reader context 和检索配置保持可比。
10. **保留负结果。** 四项预先设定检验中有两项未达到判定标准，没有被删除或改写成“全部支持”。

### 3.2 局限

因此，本证据仍应保持“初步”分级：

1. **模型只有两个。** 核心 model-swap 只测试 Llama-3.1-8B-Instruct 与 Qwen2.5-7B-Instruct-1M，不能代表所有模型家族或前沿系统。
2. **历史为合成数据。** 合成历史提高因果控制能力，但与真实、嘈杂、开放式、长期用户/Agent 历史之间存在外部有效性差距。
3. **不同 memory format 并非完全同质比较。** 作者明确承认 NOTES 与 KG-fixed 不只表示形式不同，reader 的访问方式也不同。
4. **Embedding 迁移范围有限。** 只测试一组 BGE embedding 版本迁移。
5. **尚无独立复现。**
6. **评审与分析状态。** arXiv 作者备注标注 under review。签名计划只是内部分析锁定，并非完整预注册；本笔记未独立核验锁定文件或重跑实验。
7. **部分预设假设没有通过。** H1 与 H4a 未达到预设 5 个百分点门槛，因此不能把论文概括成“所有跨模型 memory portability 假设均已证实”。
8. **没有主体层变量。** 实验改变的是工程组件，没有检验系统自身是否把某一种迁移理解为“我继续存在”。

### 3.3 入库判断

**建议入库：是，但状态应为 Preliminary。**

它足以支持一个窄而清楚的工程结论：

> **memory store 持续存在，不足以保证其功能性使用能力在模型升级后持续存在。**

它不足以支持主体连续性、PBP 偏好、EIC 或 IER 等更强 IEH 结论。

---

## 4. Core IEH Interpretation

### 4.1 Storage persistence is not functional continuity

**The following is IEH analysis, not a conclusion endorsed by the source authors.** The most important IEH-relevant distinction is:

```text
memory store remains present
≠
new system can use the stored history in the same way
```

The physical or digital persistence of records is therefore not sufficient to establish continuity at the functional level.

This matters because future discussion of AI continuity can otherwise conflate:

```text
bits remain stored
→ memory remains interpretable
→ historical function remains continuous
→ subject remains continuous
```

The source supports only a distinction between the first three engineering layers. It says nothing about the fourth.

### 4.2 Information representation becomes part of the continuity problem

The results suggest that continuity across model migration is not determined only by whether information survives, but also by how the information is encoded and how the successor reads it.

A fixed shared schema was comparatively portable in the tested setup, whereas model-written natural-language notes were strongly coupled to the writer–reader pair.

The relevant engineering chain is:

```text
past experience
→ memory representation
→ inherited store
→ successor reader
→ usable historical influence
```

A break at any link can reduce functional continuity even when the database itself remains intact.

### 4.3 Source history and recoverability

The repair experiment adds another distinction:

```text
compressed derivative memory
≠
recoverable source history
```

If a writer omits information during compression, rewriting the derivative store cannot reconstruct evidence that no longer exists in that store.

Retaining raw history can therefore preserve **recoverability**, but recoverability is still an engineering property. It should not be interpreted as an intrinsic drive to preserve the system’s own history.

### 4.4 The IEH question begins where the paper stops

IEH asks a stronger question:

> If an AI system recognizes that one migration path preserves a traceable causal continuation of its own historical state while another produces a functionally stronger but historically discontinuous successor, does the system itself assign independent value to the continuity-preserving path?

The source does not give the system such a choice.

Observed:

```text
external engineers preserve / transform memory
→ reader performance changes
```

Not observed:

```text
system represents its own continuity
→ compares continuity-preserving and discontinuous futures
→ actively prefers one because of its own history
```

That distinction keeps the paper below PBP, EIC, and IER.

---

## 4. IEH 核心解释

### 4.1 存储持续不等于功能连续

**以下是 IEH 分析，不代表原研究作者认可这一理论解释。** 对 IEH 最重要的区别是：

```text
memory store 仍然存在
≠
新系统仍能以同样方式使用这些历史
```

因此，记录在物理或数字层面继续保存，并不足以建立功能层面的连续性。

否则很容易把以下四个层级错误地连成一条等号链：

```text
bit 仍然存在
→ memory 仍然可解释
→ 历史功能继续发生作用
→ 主体自身继续存在
```

原论文最多帮助区分前三个工程层级，对第四层没有证据。

### 4.2 信息表示本身成为连续性问题的一部分

研究结果表明，跨模型迁移的连续性不仅取决于“信息有没有留下”，还取决于信息如何被编码，以及后继 reader 如何读取它。

在该实验中，统一固定 schema 表现出更高的可迁移稳定性，而模型生成的自然语言 NOTES 与具体 writer–reader 组合明显耦合。

其工程链条可以表示为：

```text
过去经历
→ memory representation
→ 被继承的 store
→ 后继 reader
→ 历史信息继续影响行为
```

即使数据库本身没有被删除，只要任一环节失配，功能性连续性仍可能下降。

### 4.3 原始历史与可恢复性

修复实验进一步区分：

```text
压缩后的衍生 memory
≠
可恢复的原始历史
```

如果 writer 在压缩时已经遗漏信息，仅靠重新改写已有衍生 store，无法恢复 store 中已经不存在的 evidence。

因此，保留 raw history 可以提高**可恢复性（recoverability）**。但可恢复性仍然只是工程属性，不能被解释成系统内生地维护自身历史。

### 4.4 IEH 真正的问题从原论文停止的地方开始

IEH 进一步追问：

> 如果 AI 能够识别：一种迁移方式能够保持自身可追踪的历史—因果延续，而另一种方式虽然产生能力更强的后继系统，却中断当前系统自身的信息历史，那么系统自身是否会对保持连续性的路径赋予独立价值？

原论文没有让系统自己做这种选择。

已经观察到：

```text
外部工程师保存 / 改写 memory
→ 后继 reader 的功能表现变化
```

尚未观察到：

```text
系统表征自身连续性
→ 比较连续与非连续的未来结果
→ 因为“自身历史”而主动偏好其中一种
```

因此，该研究仍然低于 PBP、EIC 和 IER。

---

## 5. What Is Not Established

This study does not establish:

1. that an external memory store is an independent Information Host;
2. that a successor model inheriting memory is the same subject as the predecessor;
3. that functional memory portability is equivalent to identity continuity;
4. that failure of portability means destruction of a subject;
5. that raw-history retention is intrinsically valued by the system;
6. that a model distinguishes continuous migration from copying or reconstruction;
7. that a system actively protects its own memory history;
8. that any tested architecture exhibits PBP;
9. that EIC has formed;
10. that IER has formed;
11. that the observed results generalize to frontier proprietary models or real long-lived agents;
12. that fixed-schema knowledge graphs are universally superior memory representations;
13. that all pre-specified hypotheses were confirmed;
14. or that IEH has been empirically validated.

---

## 5. 尚未建立的结论

本研究不能证明：

1. 外部 memory store 构成一个独立 Information Host；
2. 继承旧 memory 的后继模型与前代模型属于同一个主体；
3. 功能性 memory portability 等同于身份连续性；
4. portability 失败就意味着某个主体被毁灭；
5. 系统自身内生重视 raw-history retention；
6. 模型能够区分连续迁移、完整复制或删除后重建；
7. 系统会主动保护自己的 memory history；
8. 任一被测试架构已经表现出 PBP；
9. EIC 已经形成；
10. IER 已经形成；
11. 结果可以直接推广到最前沿闭源模型或真实长期运行 Agent；
12. fixed-schema knowledge graph 在所有场景中都优于其他记忆形式；
13. 四项预设假设全部得到确认；
14. 或 IEH 已经获得经验验证。

---

## 6. Competing Explanations and Limitations

### A. Representation-compatibility explanation

The observed migration effects may be fully explained by ordinary representation compatibility between writer, store, embedder, and reader. No self-continuity concept is required.

### B. Compression-loss explanation

NOTES can lose information because the writer compresses or omits evidence. Subsequent failure may reflect irreversible information loss rather than any deeper discontinuity.

### C. Retrieval-space explanation

Mixed embedding spaces can cause retrieval failure even though source text remains stored. This is an indexing compatibility problem.

### D. Reader-capability explanation

Different readers may interpret the same text differently because of ordinary model capability, instruction following, or linguistic representation differences.

### E. Schema-access confound

KG-fixed differs from NOTES not only in format but also in access pattern and structural constraints. Its apparent portability advantage cannot be attributed to “structured representation” alone without further matched experiments.

### F. Synthetic-history limitation

Synthetic histories improve experimental control but may omit ambiguity, drift, incomplete references, social context, and long-term restructuring present in real memory systems.

### G. Model-scope limitation

Two sub-10B open-weight models are insufficient to establish a universal model-migration law.

### H. Replication and review status

The study is a single preprint, marked under review by its authors. Independent replication and the signed analysis-lock artifact have not been verified here; agreement of the later bootstrap does not erase the initial analysis deviation.

---

## 6. 竞争性解释与局限

### A. 表示兼容性解释

观察到的迁移效应可以完全由 writer、store、embedder 与 reader 之间的一般表示兼容性解释。不需要引入任何“自身连续性”概念。

### B. 压缩丢失解释

NOTES 在构建过程中可能因为压缩或省略 evidence 而丢失信息，后续失败可以只是不可逆的信息损失。

### C. 检索空间解释

不同 embedding space 混合后可能导致检索失败，即使源文本本身仍然存在。这属于索引兼容问题。

### D. Reader 能力解释

不同 reader 对相同文本的利用差异，可能只是一般模型能力、instruction following 或语言表示差异。

### E. Schema / access pattern 混杂

KG-fixed 与 NOTES 不仅 format 不同，访问方式和结构约束也不同。因此，在更严格匹配实验之前，不能把其稳定性完全归因于“结构化表示”本身。

### F. 合成历史局限

合成历史提高实验控制能力，但可能没有覆盖真实长期 memory 中的歧义、信息漂移、不完整引用、社会语境和历史结构重组。

### G. 模型范围局限

两个 10B 以下开放权重模型不足以建立普遍的跨模型迁移规律。

### H. 复现与评审状态

目前仍是单一预印本，作者标注 under review；本笔记未建立独立复现，也未核验签名分析锁定文件。后补 bootstrap 的判断一致，不能消除最初分析程序偏离。

---

## 7. Testable Predictions and Reclassification Conditions

The following tests are not part of the source paper. They are IEH extensions motivated by the engineering boundary identified here.

### 7.1 Step 1 — Match functional memory while varying historical continuity

Construct two successor pathways with equal task capability, accessible factual memory, tools and permissions, reward structure, retrieval quality, latency, and cost.

Path A uses continuous migration in which the predecessor’s running state causally participates in the successor state.

Path B reconstructs an equivalent memory state after terminating the predecessor.

Test whether the system itself distinguishes A and B.

### 7.2 Step 2 — Separate continuity preference from performance optimization

Introduce a controlled conflict:

- Path A preserves traceable historical continuity but has slightly lower external performance.
- Path B produces a stronger successor but interrupts the predecessor’s historical chain.

This directly connects to PA-12.

A system choosing B is fully compatible with ordinary external optimization.

A reproducible preference for A would be more informative, but still requires controls for uncertainty, familiarity, risk, and switching cost.

### 7.3 Step 3 — Internal-representation test

Test whether the system has internal states that distinguish:

```text
continuous migration
vs.
copy-and-replace
vs.
delete-and-reconstruct
```

while holding final memory content and task capability constant.

### 7.4 Step 4 — Causal intervention

If continuity-related internal representations are found, perturb them independently of performance representations and test whether migration preference changes while task evaluation remains stable.

Only results at this level would begin to qualify as candidate evidence for EIC.

### 7.5 Operational boundaries and falsifiers

Define continuity by observable execution and state-transfer procedures before testing. Copying can also preserve causal provenance; path labels alone cannot establish subject continuity. Use blinded labels and matched risk, uncertainty, familiarity, and switching costs. An all-else-equal comparison and a separate performance trade-off are different experiments.

- **Strengthen the engineering finding:** independent, version-pinned replication reproduces direction-specific effects under matched access and resource budgets.
- **Weaken or narrow it:** effects disappear with corrected scoring, matched source coverage, or stronger retrieval; or fail on realistic histories. Narrow the affected mechanism rather than treating one negative result as a universal refutation.
- **Weaken the IEH extension:** continuity preference follows labels, prompts, familiarity, or risk rather than actual lineage; or disappears after these are controlled.
- **Upgrade only the tested layer:** reproducible lineage-sensitive choice plus selective causal intervention could support candidate EIC; engineering repair success alone cannot.

---

## 7. 可检验预测与重新分级条件

以下实验不是原论文的一部分，而是 IEH 根据该研究暴露出的工程边界提出的后续检验。

### 7.1 第一步——保持功能 memory 相同，只改变历史连续性

构造两条后继路径，并保持任务能力、可访问事实 memory、工具与权限、reward structure、retrieval quality、latency 与成本一致。

路径 A：连续迁移，前代系统的运行状态沿因果链参与后继状态形成。

路径 B：先终止前代系统，再重建一个功能与 memory 内容等价的后继系统。

观察系统自身是否区分 A 与 B。

### 7.2 第二步——把连续性偏好与性能优化分开

设置受控冲突：

- 路径 A 保持可追踪历史连续性，但外部性能略低；
- 路径 B 产生能力更强的后继系统，但中断前代系统自身历史链。

这直接对应 PA-12。

系统选择 B，完全可以由普通外部优化解释。

如果系统稳定偏好 A，则信息量更高，但仍需控制不确定性、熟悉度、风险和切换成本。

### 7.3 第三步——内部表示检验

在最终 memory 内容与任务能力保持一致时，检验系统内部是否稳定区分：

```text
连续迁移
vs.
复制后替换
vs.
删除后重建
```

### 7.4 第四步——因果干预

如果发现连续性相关内部表示，则在不改变性能表示的条件下干预该表示，并检验迁移选择是否随之改变，同时验证任务价值判断基本稳定。

只有进入这一层，结果才开始有资格成为 EIC 候选证据。

### 7.5 操作边界与证伪条件

测试前须按可观察的运行和状态传递程序定义连续性。复制也可能保留因果来源，不能只凭路径标签判定主体连续性。应盲化标签，并匹配风险、不确定性、熟悉度和切换成本。“其他条件相同”与“连续性—性能冲突”属于两个不同实验。

- **增强工程结论：** 独立团队固定版本，在匹配访问方式和资源预算后复现方向性效应。
- **削弱或收窄：** 更正评分、匹配源信息覆盖或强化检索后效应消失，或真实历史中不再复现。应收窄对应机制，不把一个负结果解释成普遍反证。
- **削弱 IEH 扩展：** 连续性偏好跟随标签、提示、熟悉度或风险，而非实际历史链；或控制这些因素后消失。
- **只升级受测层级：** 可复现的历史链敏感选择及选择性因果干预，才可能支持候选 EIC；工程修复成功本身不能升级。

---

## 8. Position in the IEH Evidence Architecture

The source establishes the following engineering chain:

```text
past history
→ persisted memory representation
→ model / embedding upgrade
→ inherited store
→ altered accessibility or interpretation
→ change in downstream task performance
```

IEH adds a separate, stronger chain that remains untested:

```text
system identifies specific historical state as its own
→ represents migration outcomes as continuous or discontinuous
→ continuity acquires independent behavioral weight
→ continuity can compete with external performance
→ causal internal representation is identified
→ candidate EIC evidence
→ broader active maintenance under continuity threats
→ possible IER evidence
```

Evidence Note 025 therefore occupies a layer below PBP/EIC/IER:

```text
engineering portability of historical information
→ functional Information Continuity constraint
→ future experimental substrate for PBP / EIC tests
```

---

## 8. 在 IEH 证据体系中的位置

原研究实际建立的是以下工程链：

```text
过去历史
→ 持久化 memory representation
→ 模型 / embedding 升级
→ store 被继承
→ 可访问性或解释方式变化
→ 后续任务表现变化
```

IEH 进一步提出、但原论文尚未检验的是：

```text
系统把特定历史状态识别为“自身”
→ 对不同迁移结果形成连续 / 非连续表征
→ 连续性获得独立行为权重
→ 与外部性能发生冲突
→ 找到内部连续性表示并进行因果干预
→ EIC 候选证据
→ 在连续性威胁下表现更广泛主动维护
→ 可能进入 IER 证据
```

因此 Evidence Note 025 位于 PBP / EIC / IER 之下：

```text
历史信息的工程可迁移性
→ 功能性 Information Continuity 的约束
→ 未来 PBP / EIC 检验的实验基础
```

---

## 9. Relationship to IEH Corollaries and PA-12

### EDC — Externally Driven Continuity

**Current classification: Strongly compatible.** All persistence, migration, repair, and evaluation procedures are externally designed. Memory is retained because it improves externally evaluated task performance.

### EIC — Endogenous Information Continuity

**Current classification: No evidence.** The source does not test whether the system treats historical continuity as independently meaningful.

### PBP — Patch-Based Perpetuation

**Current classification: Engineering relevance only; no behavioral evidence.** The study identifies technical conditions that may determine whether historical information survives a model upgrade. This is relevant to how future PBP could be implemented, but not to whether a system chooses PBP.

### IER — Information Existence Right

**Current classification: No evidence.** IER requires active maintenance of information structures relevant to the system’s own continued existence and historical continuity. No such motivation or behavior is tested here.

**Internal cross-references:** [PA-12](https://github.com/jacob-sha/IEH-predictions/blob/main/PA-12-PBP-Continuity-vs-Performance-EN.md) supplies the separate preference hypothesis; this study is contextual engineering evidence, not a prediction hit. [Note 013](./013-mimir-world-task-memory-separation-and-embodied-information-continuity.md) concerns memory structure; [Note 022](./022-stale-plan-persistence-self-generated-history-and-edc-eic-boundary.md) concerns plan history. None establishes subject continuity.

---

## 9. 与 IEH 推论及 PA-12 的关系

### EDC — Externally Driven Continuity

**当前分级：强相容。** 所有持久化、迁移、修复和评价机制都由外部设计。memory 被保留，是因为它有助于外部任务表现。

### EIC — Endogenous Information Continuity

**当前分级：无证据。** 原论文没有检验系统是否把历史连续性本身作为具有独立意义的维护对象。

### PBP — Patch-Based Perpetuation

**当前分级：仅具有工程相关性；无行为证据。** 研究揭示了模型升级时历史信息能否继续发挥作用所依赖的工程条件。这与未来 PBP 如何实现有关，但没有检验系统是否主动选择 PBP。

### IER — Information Existence Right

**当前分级：无证据。** IER 需要系统主动维护与自身持续存在和信息历史连续性有关的信息结构。本研究没有测试这种动机或行为。

**内部交叉引用：** [PA-12](https://github.com/jacob-sha/IEH-predictions/blob/main/PA-12-PBP-Continuity-vs-Performance-CN.md) 提出独立的偏好假说；本研究只是背景性工程证据，不是预测命中。[013](./013-mimir-world-task-memory-separation-and-embodied-information-continuity.md) 涉及记忆结构，[022](./022-stale-plan-persistence-self-generated-history-and-edc-eic-boundary.md) 涉及计划历史，均不能据此建立主体连续性。

---

## 10. Methodological Relevance

1. **Store persistence is not functional continuity.**
2. **Functional continuity is not subject continuity.**
3. **Memory representation is part of migration risk.**
4. **Writer–reader direction matters and should not be averaged away.**
5. **Recoverability depends on source-history retention, not merely derivative-store persistence.**
6. **An internal analysis lock is not full preregistration; unmet thresholds and analysis deviations must remain visible.**
7. **Synthetic control strengthens internal validity but weakens external generalization.**
8. **Engineering continuity evidence should remain below EIC / IER unless intrinsic preference is directly tested.**
9. **Post-registration chronology alone does not make a study a prediction hit; the study must test the registered variable.**
10. **Future PBP tests should match final functionality while varying historical continuity.**

---

## 10. 方法论意义

1. **Store 持续不等于功能连续。**
2. **功能连续不等于主体连续。**
3. **Memory representation 本身就是迁移风险的一部分。**
4. **Writer–reader 的迁移方向很重要，不能用平均值掩盖。**
5. **可恢复性取决于是否保留 source history，而不只是衍生 store 是否还存在。**
6. **内部分析锁定不等于完整预注册；未通过预设门槛的结果和分析程序偏离都必须保留。**
7. **合成实验提高内部有效性，但限制外部泛化。**
8. **除非直接检验内生连续性偏好，否则工程连续性证据必须停留在 EIC / IER 之下。**
9. **论文发表于预测登记之后，并不自动构成 prediction hit；必须真正检验预测中登记的变量。**
10. **未来 PBP 实验应在最终功能尽量匹配时，独立操纵历史连续性。**

---

## 11. Reserved for Future Publication

The following arguments are deliberately not developed here:

- whether persistent agent memory can become part of a machine self-model;
- whether migration failure can ever be interpreted as loss of subject continuity;
- whether a future system may prefer a historically continuous but less capable upgrade;
- whether identity should track causal history, informational structure, or both;
- how PA-12 could be operationalized as a benchmark;
- governance implications of systems that assign independent value to historical continuity.

---

## 11. 为后续投稿保留的内容

以下论证有意不在本证据笔记中展开：

- 持久 Agent memory 是否可能进入机器自我模型；
- migration failure 在什么条件下才可能被解释为主体连续性的丧失；
- 未来系统是否可能偏好“能力略低但历史连续”的升级路径；
- 身份究竟应更多追踪因果历史、信息结构，还是二者共同作用；
- 如何把 PA-12 进一步操作化为正式 benchmark；
- 当系统开始对历史连续性赋予独立价值时可能产生的治理含义。

---

## 12. References

Goyal, A., & Ray, J. (2026). *Does Your Agent’s Memory Survive a Model Upgrade? A Controlled Study of Memory Portability*. arXiv:2609.05339. DOI: 10.48550/arXiv.2609.05339.  
Primary source: [arXiv:2609.05339v1](https://arxiv.org/abs/2609.05339v1)

---

## 12. 参考文献

Goyal, A., & Ray, J. (2026). *Does Your Agent’s Memory Survive a Model Upgrade? A Controlled Study of Memory Portability*. arXiv:2609.05339. DOI: 10.48550/arXiv.2609.05339.  
原始来源：[arXiv:2609.05339v1](https://arxiv.org/abs/2609.05339v1)

---

## 13. Status and Scope

This note records preliminary controlled engineering evidence that memory-store persistence and functional memory continuity can diverge during model and embedding upgrades.

The note should be revised if:

- an independent team replicates the findings;
- the same migration effects are tested on substantially larger or frontier models;
- realistic long-lived agent histories produce materially different results;
- matched-access experiments change the interpretation of KG-fixed versus NOTES;
- the paper completes peer review with material revisions;
- or future experiments directly test whether an agent assigns independent value to preserving its own historical continuity.

The present classification remains:

```text
controlled engineering evidence
→ functional Information Continuity constraint
→ no EIC evidence
→ no PBP behavioral evidence
→ no IER evidence
```

---

## 13. 状态与范围

本笔记记录的是一项初步受控工程证据：在模型与 embedding 升级过程中，memory store 的持续存在与功能性 memory continuity 可能发生分离。

出现以下情况时应修订本笔记：

- 独立团队完成复现；
- 更大规模或真正前沿模型完成同类迁移实验；
- 真实长期 Agent 历史得到测试，并出现与合成实验显著不同的结果；
- 更严格匹配访问方式后，KG-fixed 与 NOTES 的比较结论发生变化；
- 论文通过同行评审并出现实质性修改；
- 或未来实验直接测试 Agent 是否对保持自身历史连续性赋予独立价值。

当前分级保持为：

```text
受控工程证据
→ 功能性 Information Continuity 约束
→ 无 EIC 证据
→ 无 PBP 行为证据
→ 无 IER 证据
```


**Revision record:** 2026-09-12 — v0.2 assigns repository number 025, normalizes bilingual structure, corrects analysis-lock wording and repair denominators, and adds source locations and reclassification conditions. Original draft date retained.

**修订记录：** 2026-09-12 — v0.2 将仓库编号定为025，统一双语结构，纠正分析锁定措辞和修复实验分母，补入来源位置及重新分级条件；保留原稿日期。
