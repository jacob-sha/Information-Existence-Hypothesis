# Evidence Note 007: The Jacobian Counterexample, AI-Assisted Exact Verification, and an Early Domain-Specific HDCT Signal

**Repository function:** Research record / evidence index  
**Document type:** Non-narrative external evidence note  
**Status:** Preliminary and revisable  
**Relation to IEH:** AI-assisted frontier-mathematics event and strong candidate support for the domain-specific HDCT pathway; not proof of machine-native representations or realized HDCT  
**Primary IEH corollary:** C02-HDCT — High-dimensional Cognitive Tools  
**Primary related prediction record:** PA-10 — From Language Models to Machine-Native Representations: Model Evolution Pathways Toward HDCT  
**Secondary related prediction record:** PA-06 — High-dimensional Cognitive Tools and Scientific Paradigm Shift  
**Author of IEH analysis:** Jacob Sha  
**Version:** v0.1 — archive-safe edition  
**Date:** 2026-07-21  

> **Publication boundary:** This file is a compact research record, not a publication draft. It intentionally excludes a narrative claim that AI has “ended human mathematics,” a developed argument about the transfer of mathematical authority from humans to machines, a complete account of the Jacobian Conjecture’s history, a general theory of AI scientific autonomy, and a publication-ready thesis about machine-native mathematics.

> **Source-use boundary:** This note records only the minimum primary-source set required to establish the exact mathematical certificate and the documented AI-assisted verification work: the public derivation and exact verification scripts in the `jacobianfun` research repository. Social-media announcements, news reports, newsletters, aggregators, discussion forums, and screenshots are excluded from the evidence record. The original discovery interaction attributed elsewhere to Levent Alpöge and Claude Fable is not independently documented by an admissible formal primary record in this note; its precise division of human and model contribution therefore remains unresolved.

> **Chronology boundary:** The mathematical event became public before PA-10 was formally archived on 2026-07-21. It may be recorded as initial evidence motivating and supporting PA-10, but not as a post-registration prediction hit by PA-10. Its relevance to the earlier C02-HDCT theoretical claim remains independent of that archival timing.

---

# 证据笔记 007：雅可比猜想反例、AI 辅助精确验证与早期领域型 HDCT 信号

**仓库功能：** 研究记录 / 证据索引  
**文档类型：** 非叙事性外部证据笔记  
**状态：** 初步记录，可随正式论文、复现研究和来源披露修订  
**与 IEH 的关系：** AI 辅助前沿数学事件及 PA-10 领域型 HDCT 路径的较强候选支持；不是机器原生表示或完整 HDCT 的证明  
**主要 IEH 推论：** C02-HDCT——高维认知工具  
**主要相关预测档案：** PA-10——从语言模型到机器原生表示：HDCT 的模型演化路径  
**次要相关预测档案：** PA-06——高维认知工具与科学范式迁移  
**IEH 分析作者：** Jacob Sha  
**版本：** v0.1 — 投稿隔离版  
**日期：** 2026-07-21  

> **投稿边界：** 本文件只是简明研究记录，不是投稿文章初稿。文件有意不展开“AI 终结人类数学”的叙事性主张、数学权威由人类向机器转移的完整论证、雅可比猜想的完整历史、AI 科学自主性的通论，以及关于机器原生数学的可直接投稿结论。

> **来源使用边界：** 本笔记只记录建立精确数学证书和已公开 AI 辅助验证过程所严格必要的最小原始来源集合，即 `jacobianfun` 研究仓中的公开推导与精确验证脚本。社交媒体公告、新闻报道、通讯、聚合页面、论坛讨论和截图不进入证据记录。其他来源所称 Levent Alpöge 与 Claude Fable 的原始发现过程，在本笔记中尚没有可以归档的正式原始互动记录，因此人类与模型各自贡献的精确边界仍未解决。

> **时间边界：** 该数学事件早于 PA-10 在 2026-07-21 正式建档。它可以作为促成并支持 PA-10 的初始证据记录，但不能被写成 PA-10 建档后的预测命中。它与更早形成的 C02-HDCT 理论判断之间的关联，不受这一档案时间顺序影响。

---

## 1. Source Record

### Primary exact derivation

- **Title:** *Weighted lifts from the Jacobian counterexample*
- **Author / curator:** Alexis Gallagher
- **Date:** 2026-07-20
- **Repository:** `algal/jacobianfun`
- **Primary URL:** https://github.com/algal/jacobianfun/blob/main/RESEARCH.md
- **Material type:** Public mathematical derivation, structural analysis, and reproducible research record
- **Role in this note:** Establishes an exact algebraic analysis of the displayed polynomial map and records follow-on deductions
- **AI-production disclosure in the source:** The associated project states that GPT-5.6-sol performed substantial work in structural reverse-engineering, follow-on construction, writing, implementation, and automated checks
- **Historical-priority limitation:** The source does not claim completed literature review or priority for all follow-on constructions

### Primary exact verification scripts

- **Main exact checker:** https://github.com/algal/jacobianfun/blob/main/verify.py
- **Page-fact audit:** https://github.com/algal/jacobianfun/blob/main/verify_page_facts.py
- **Repository root:** https://github.com/algal/jacobianfun
- **Verification method:** Exact symbolic and rational arithmetic rather than floating-point approximation
- **Role in this note:** Checks the determinant identities, displayed collisions, reconstruction formulas, and selected follow-on constructions

### Primary public mathematical certificate

Let \(u=1+xy\), and define the polynomial map

\[
F:\mathbb{C}^{3}\rightarrow\mathbb{C}^{3}
\]

by

\[
F(x,y,z)=
\left(
u^{3}z+y^{2}u(4+3xy),\;
y+3xu^{2}z+3xy^{2}(4+3xy),\;
2x-3x^{2}y-x^{3}z
\right).
\]

The exact certificate consists of two identities:

\[
\det JF(x,y,z)\equiv -2,
\]

and

\[
F\left(0,0,-\frac14\right)
=
F\left(1,-\frac32,\frac{13}{2}\right)
=
F\left(-1,\frac32,\frac{13}{2}\right)
=
\left(-\frac14,0,0\right).
\]

The first identity satisfies the nonzero-constant-Jacobian condition.  
The second proves that \(F\) is not injective.

Therefore, the displayed map is an exact counterexample to the Jacobian Conjecture in dimension three. Appending identity coordinates produces counterexamples in every dimension \(n\geq 3\).

This certificate does not resolve the separate two-variable case.

### Source-exclusion rule

The following materials are not archived as evidence sources in this note:

- social-media announcements;
- screenshots;
- news and magazine articles;
- institutional publicity;
- aggregator pages;
- forum commentary;
- AI-generated summaries;
- or secondary mathematical explainers not required to establish the exact certificate.

### Provenance limitation

The primary verification project credits the announced map to Levent Alpöge and Fable, but it does not contain the original complete interaction record, search trace, prompt history, candidate distribution, or division of labor that produced the map.

Accordingly, this note distinguishes:

\[
\text{exact mathematical validity of the counterexample}
\]

from:

\[
\text{complete provenance of the original AI-assisted discovery}.
\]

The first is supported by a short reproducible certificate.  
The second remains incompletely documented in the admissible primary-source set.

---

## 1. 来源记录

### 主要精确推导

- **标题：** *Weighted lifts from the Jacobian counterexample*
- **作者 / 维护者：** Alexis Gallagher
- **日期：** 2026-07-20
- **代码仓：** `algal/jacobianfun`
- **原始链接：** https://github.com/algal/jacobianfun/blob/main/RESEARCH.md
- **材料性质：** 公开数学推导、结构分析与可复核研究记录
- **在本笔记中的作用：** 对公开多项式映射进行精确代数分析，并记录后续推导
- **来源中披露的 AI 参与：** 配套项目说明 GPT-5.6-sol 在结构逆向分析、后续构造、写作、实现和自动检查中完成了大量工作
- **历史优先权限制：** 来源没有声称已经完成全部文献审查，也没有对所有后续构造主张历史优先权

### 主要精确验证脚本

- **主要验证脚本：** https://github.com/algal/jacobianfun/blob/main/verify.py
- **页面事实核查脚本：** https://github.com/algal/jacobianfun/blob/main/verify_page_facts.py
- **代码仓首页：** https://github.com/algal/jacobianfun
- **验证方法：** 使用精确符号运算和有理数运算，而不是浮点近似
- **在本笔记中的作用：** 检查雅可比行列式、公开碰撞点、重构公式和部分后续构造

### 公开数学证书

令 \(u=1+xy\)，定义多项式映射

\[
F:\mathbb{C}^{3}\rightarrow\mathbb{C}^{3}
\]

为

\[
F(x,y,z)=
\left(
u^{3}z+y^{2}u(4+3xy),\;
y+3xu^{2}z+3xy^{2}(4+3xy),\;
2x-3x^{2}y-x^{3}z
\right).
\]

精确证书由两个恒等式组成：

\[
\det JF(x,y,z)\equiv -2,
\]

以及

\[
F\left(0,0,-\frac14\right)
=
F\left(1,-\frac32,\frac{13}{2}\right)
=
F\left(-1,\frac32,\frac{13}{2}\right)
=
\left(-\frac14,0,0\right).
\]

第一个恒等式满足非零常数雅可比行列式条件。  
第二个恒等式证明 \(F\) 不是单射。

因此，该映射构成三维雅可比猜想的精确反例。增加保持不变的坐标，可以在所有 \(n\geq 3\) 维度得到反例。

该证书没有解决独立的二维情形。

### 来源排除规则

以下材料不作为证据来源进入本笔记：

- 社交媒体公告；
- 截图；
- 新闻和杂志文章；
- 机构宣传；
- 聚合页面；
- 论坛评论；
- AI 生成摘要；
- 对建立精确证书并非严格必要的二次数学说明。

### 来源过程限制

主要验证项目把公开映射的发现归于 Levent Alpöge 与 Fable，但项目不包含产生该映射的完整原始互动记录、搜索轨迹、提示历史、候选分布或人机分工记录。

因此，本笔记严格区分：

\[
\text{反例在数学上的精确有效性}
\]

与：

\[
\text{原始 AI 辅助发现过程的完整来源记录}.
\]

前者由简短、可重复的数学证书支持。  
后者在当前可归档的原始来源集合中仍不完整。

---

## 2. Minimal Finding Index

| ID | Primary-source finding | Minimal relevance to IEH |
|---|---|---|
| F1 | An explicit polynomial map \(F:\mathbb C^3\to\mathbb C^3\) is publicly specified. | The event concerns a concrete mathematical object, not a verbal claim alone. |
| F2 | Exact symbolic calculation gives \(\det JF\equiv -2\). | The map satisfies the defining Jacobian condition. |
| F3 | Three distinct inputs map exactly to the same output. | The map is noninjective and cannot have a global inverse. |
| F4 | The certificate is finite and can be checked with exact arithmetic. | Correctness does not depend on trusting model self-explanation. |
| F5 | The map disproves the conjecture in dimension three. | A longstanding open mathematical knowledge state is changed. |
| F6 | Identity-coordinate extension gives counterexamples for all \(n\geq3\). | The consequence is not confined to one isolated dimension. |
| F7 | The two-variable case is not resolved. | The remaining scope must not be overstated. |
| F8 | The public verification project includes exact scripts and structural derivation. | The event contains a reproducible formal-feedback loop. |
| F9 | The project reports substantial GPT-5.6-sol work on analysis, construction, implementation, and checks. | AI participation is directly documented for verification and follow-on work. |
| F10 | The precise original contribution of Fable to discovering the initial map is not documented by the admissible source set. | The strongest AI-discovery attribution remains provenance-limited. |
| F11 | The project derives broader weighted-lift constructions and generic fiber degrees. | The AI-assisted workspace did more than repeat the two-line certificate. |
| F12 | Literature priority for the follow-on family is not established. | Novelty beyond the original certificate remains partly open. |
| F13 | No independent model rediscovery is established. | Cross-model repeatability remains untested. |
| F14 | No internal model representation is examined. | Machine-native representations cannot be inferred directly. |
| F15 | The mathematical certificate is human-readable and compact. | The event does not show human-incomprehensible mathematics. |

---

## 2. 最小事实索引

| 编号 | 原始来源建立的事实 | 与 IEH 的最低限度关联 |
|---|---|---|
| F1 | 一个明确的多项式映射 \(F:\mathbb C^3\to\mathbb C^3\) 被公开给出。 | 该事件涉及具体数学对象，而不只是语言性宣称。 |
| F2 | 精确符号计算得到 \(\det JF\equiv -2\)。 | 该映射满足雅可比猜想的条件。 |
| F3 | 三个不同输入精确映射到同一输出。 | 该映射不是单射，不可能具有全局逆。 |
| F4 | 证书是有限的，可以通过精确运算检查。 | 正确性不依赖相信模型的自我解释。 |
| F5 | 该映射反驳三维雅可比猜想。 | 一个长期开放的数学知识状态发生改变。 |
| F6 | 增加恒等坐标后，可在所有 \(n\geq3\) 维度构造反例。 | 结论不限于孤立的一个维度。 |
| F7 | 二维情形没有解决。 | 不能夸大结果适用范围。 |
| F8 | 公开验证项目包含精确脚本与结构推导。 | 该事件具有可重复的形式反馈闭环。 |
| F9 | 项目披露 GPT-5.6-sol 大量参与分析、构造、实现和检查。 | AI 在验证和后续工作中的参与有直接公开记录。 |
| F10 | 当前可归档来源没有记录 Fable 发现初始映射时的精确贡献。 | 最强的 AI 原始发现归因仍受到来源限制。 |
| F11 | 项目进一步推导加权提升构造和一般纤维次数。 | AI 辅助工作空间并非只重复两行证书。 |
| F12 | 后续构造在既有文献中的历史优先权尚未建立。 | 原始证书以外的新颖性仍部分开放。 |
| F13 | 尚未建立独立模型重新发现。 | 跨模型重复性仍未检验。 |
| F14 | 没有研究模型内部表示。 | 不能直接推断机器原生表示。 |
| F15 | 数学证书简短且可由人类理解。 | 该事件不能证明人类无法理解的数学已经出现。 |

---

## 3. IEH Evidence Classification

| Dimension | Current classification |
|---|---|
| Evidence type | AI-assisted frontier mathematical event with exact symbolic verification |
| Mathematical status | Exact counterexample to the Jacobian Conjecture in dimension three and therefore all dimensions \(n\geq3\) |
| Two-variable case solved | No |
| Exact certificate available | Yes |
| Reproducible verification scripts available | Yes |
| AI contribution to verification and follow-on work documented | Yes |
| Original Fable discovery contribution independently documented | No |
| Peer-reviewed or discoverer-authored formal paper available in this note | No |
| Independent model rediscovery | Not established |
| Machine-native representation evidence | Not established |
| Directness to C02-HDCT | Medium |
| Directness to PA-10 domain-specific pathway | Medium to strong |
| Current IEH label | Early domain-specific HDCT functional signal with provenance limitations |
| Historical mathematical frontier crossed | Yes, for \(n\geq3\) |
| General superiority over human mathematics established | No |
| Output beyond human comprehension established | No |
| Autonomous problem selection established | No |
| Relationship to CWM, IER, PBP, or ASI | Neutral |

### Evidence-level judgment

> An exact counterexample changed the accepted status of a longstanding mathematical conjecture in dimensions \(n\geq3\). A public AI-assisted research workspace then supplied reproducible exact verification and substantial structural follow-on analysis. Under IEH, this is an **early domain-specific HDCT functional signal with provenance limitations** and a strong candidate support item for PA-10’s prediction that mathematics and formal verification may produce domain-specific HDCT before open-world HDCT.

The current evidence does not establish:

- that Fable independently discovered the map;
- that the decisive representation was machine-native;
- that the capability is stable across problems;
- or that realized HDCT has formed.

### Evidence-level placement

\[
\text{formal mathematical problem}
\rightarrow
\text{candidate counterexample}
\rightarrow
\text{exact symbolic certificate}
\rightarrow
\text{reproducible verification}
\rightarrow
\text{knowledge-state change}
\]

The present event directly supports the middle of this chain.

It does not yet establish:

\[
\text{repeatable machine-native representation}
\rightarrow
\text{stable domain-specific HDCT}.
\]

---

## 3. IEH 证据分级

| 维度 | 当前分级 |
|---|---|
| 证据类型 | 具有精确符号验证的 AI 辅助前沿数学事件 |
| 数学状态 | 三维雅可比猜想的精确反例，并由此反驳所有 \(n\geq3\) 维情形 |
| 是否解决二维情形 | 否 |
| 是否有精确证书 | 是 |
| 是否有可重复验证脚本 | 是 |
| 是否直接记录 AI 参与验证和后续工作 | 是 |
| 是否独立记录 Fable 在原始发现中的具体贡献 | 否 |
| 本笔记是否包含同行评审论文或发现者正式论文 | 否 |
| 是否完成独立模型重新发现 | 尚未建立 |
| 是否有机器原生表示证据 | 尚未建立 |
| 与 C02-HDCT 的直接程度 | 中等 |
| 与 PA-10 领域型路径的直接程度 | 中等至较强 |
| 当前 IEH 标签 | 存在来源限制的早期领域型 HDCT 功能信号 |
| 是否跨越历史数学前沿 | 对 \(n\geq3\) 情形而言，是 |
| 是否证明普遍超越人类数学 | 否 |
| 是否证明输出超出人类理解 | 否 |
| 是否自主选择问题 | 否 |
| 与 CWM、IER、PBP 或 ASI 的关系 | 中性 |

### 证据层级判断

> 一个精确反例改变了长期数学猜想在 \(n\geq3\) 维度上的知识状态。随后，公开的 AI 辅助研究工作空间提供了可重复的精确验证和实质性结构分析。在 IEH 框架下，这构成一个**存在来源限制的早期领域型 HDCT 功能信号**，并对 PA-10 关于“数学与形式验证环境可能先于开放世界产生领域型 HDCT”的预测形成较强候选支持。

现有证据不能建立：

- Fable 独立发现了该映射；
- 决定性表示属于机器原生表示；
- 这种能力能够跨问题稳定复现；
- 或完整 HDCT 已经形成。

### 证据阶梯位置

\[
\text{形式数学问题}
\rightarrow
\text{候选反例}
\rightarrow
\text{精确符号证书}
\rightarrow
\text{可重复验证}
\rightarrow
\text{知识状态改变}
\]

该事件直接支持上述链条的中间阶段。

它尚未建立：

\[
\text{可重复机器原生表示}
\rightarrow
\text{稳定领域型 HDCT}.
\]

---

## 4. Core IEH Inference

### 4.1 The event fits PA-10’s domain-specific pathway

PA-10 predicts that mathematics, code, formal proof, self-play, and simulated environments may produce domain-specific HDCT before open-world HDCT because they provide:

- explicit rules;
- dense feedback;
- low-cost repeated trials;
- decisive verification conditions;
- and sharply defined failure signals.

The Jacobian counterexample event has exactly this formal structure:

\[
\text{explicit algebraic condition}
\rightarrow
\text{candidate polynomial map}
\rightarrow
\text{determinant test}
\rightarrow
\text{injectivity test}
\rightarrow
\text{decisive acceptance or rejection}.
\]

The external world does not need to judge whether the explanation is persuasive. Exact algebra determines whether the candidate survives.

This makes the event more directly relevant to the **domain-specific HDCT pathway** than to the open-world generalized-embodiment pathway.

### 4.2 External verification replaces trust in self-explanation

The result does not require accepting a model’s narrative account of why the map works.

The certificate is:

\[
\det JF\equiv -2
\]

plus:

\[
F(p_1)=F(p_2)=F(p_3)
\]

for three distinct points.

Thus:

\[
\text{model claim}
\neq
\text{evidence}.
\]

Instead:

\[
\text{exact certificate}
+
\text{independent symbolic verification}
=
\text{mathematical evidence}.
\]

This fits PA-10’s prediction that domain-specific AI cognition may advance first in environments where formal outcomes can repeatedly select among candidate representations.

### 4.3 From answer production to knowledge-state change

The HDCT-relevant transition is not:

\[
\text{known theorem}
\rightarrow
\text{rephrased explanation}.
\]

It is closer to:

\[
\text{open conjecture}
\rightarrow
\text{candidate structure}
\rightarrow
\text{exact disproof certificate}
\rightarrow
\text{independent verification}
\rightarrow
\text{change in accepted mathematical knowledge}.
\]

This is a function predicted for HDCT: producing validated Information Structures that were not previously available to civilization.

### 4.4 Why the evidence is stronger than ordinary benchmark performance

A benchmark score can improve through:

- memorization;
- distribution matching;
- answer-format optimization;
- or narrow test familiarity.

A valid counterexample to an open conjecture has a different structure:

1. the object is explicit;
2. the decisive properties are exact;
3. a single algebraic failure invalidates the result;
4. verification can be separated from generation;
5. the output changes the field’s problem status.

This does not prove HDCT, but it is more relevant than ordinary benchmark accuracy to the predicted transition from answer generation to frontier knowledge production.

### 4.5 Why the event does not yet prove machine-native representations

PA-10 defines machine-native representations as internal forms of information organization not entirely predefined by human-selected objects, variables, and relations, formed to improve prediction, proof, design, or control.

The present sources do not reveal:

- the internal representation used to produce the map;
- whether the system reorganized the problem into a new latent structure;
- whether that representation transfers to other conjectures;
- whether the same mechanism recurs across independent runs;
- or whether the result emerged from broad search over human-defined symbolic objects.

Therefore:

\[
\text{frontier mathematical output}
\neq
\text{evidence of machine-native representation by itself}.
\]

### 4.6 Human comprehensibility remains intact

The decisive certificate is short and human-checkable.

Therefore:

\[
\text{AI-assisted frontier discovery}
\neq
\text{human-incomprehensible mathematics}.
\]

At this stage, the event is better represented as:

\[
\text{AI-assisted search and structural analysis}
+
\text{exact formal verification}
+
\text{human interpretation}
\rightarrow
\text{expanded collective mathematical cognition}.
\]

This may be an early hybrid regime on the path toward domain-specific HDCT, not a completed autonomous silicon-only mathematics regime.

### 4.7 Distinction from open-world HDCT

The event occurs in a highly formal domain with:

- fixed variables;
- explicit polynomial rules;
- exact symbolic operations;
- finite certificates;
- and unambiguous verification.

It does not establish:

- persistent environment-and-state modeling;
- generalized embodiment;
- long-horizon action in an open world;
- adaptation under partial observation;
- or real-world causal control.

Accordingly:

\[
\text{domain-specific HDCT signal}
\neq
\text{open-world HDCT signal}.
\]

### 4.8 Distinction from CWM, IER, PBP, and ASI

The event concerns mathematical problem-solving.

It does not concern:

- modeling the system’s own informational continuity;
- active maintenance of that continuity;
- resistance to replacement;
- patch-based continuation;
- resource acquisition;
- physical closure;
- or silicon-based autonomy.

Therefore:

\[
\text{HDCT-related mathematical signal}
\neq
\text{CWM}
\neq
\text{IER}
\neq
\text{PBP}
\neq
\text{ASI}.
\]

---

## 4. IEH 核心推断

### 4.1 该事件符合 PA-10 的领域型路径

PA-10 预测，数学、代码、形式证明、自我博弈和模拟环境可能早于开放世界产生领域型 HDCT，因为这些环境通常具有：

- 明确规则；
- 密集反馈；
- 较低的重复试验成本；
- 决定性的验证条件；
- 清楚的失败信号。

雅可比猜想反例事件正具有这种形式结构：

\[
\text{明确代数条件}
\rightarrow
\text{候选多项式映射}
\rightarrow
\text{行列式检验}
\rightarrow
\text{单射性检验}
\rightarrow
\text{决定性接受或否定}.
\]

外部世界不需要判断解释是否具有说服力。精确代数直接决定候选对象能否成立。

因此，该事件与**领域型 HDCT 路径**的关系，比与开放世界广义具身路径的关系更直接。

### 4.2 外部验证取代对模型自我解释的信任

该结果不要求相信模型关于“为什么映射成立”的叙述。

证书只是：

\[
\det JF\equiv -2
\]

以及三个不同点满足：

\[
F(p_1)=F(p_2)=F(p_3).
\]

因此：

\[
\text{模型宣称}
\neq
\text{证据}.
\]

真正构成数学证据的是：

\[
\text{精确证书}
+
\text{独立符号验证}.
\]

这与 PA-10 的预测一致：领域型 AI 认知可能首先在形式结果能够反复筛选候选表示的环境中发展。

### 4.3 从答案生产到知识状态改变

与 HDCT 有关的转变不是：

\[
\text{已知定理}
\rightarrow
\text{重新表达}.
\]

它更接近：

\[
\text{开放猜想}
\rightarrow
\text{候选结构}
\rightarrow
\text{精确反驳证书}
\rightarrow
\text{独立验证}
\rightarrow
\text{数学知识状态改变}.
\]

这属于 HDCT 所预测的功能：产生文明此前并未拥有、但可以验证的新信息结构。

### 4.4 为什么它比一般基准成绩更有证据价值

基准成绩可能通过以下方式提高：

- 记忆；
- 分布匹配；
- 输出格式优化；
- 对特定测试的熟悉。

开放猜想的有效反例具有不同结构：

1. 对象明确；
2. 决定性性质精确；
3. 任何一个代数错误都足以使结果失效；
4. 生成与验证可以分离；
5. 输出改变一个领域的问题状态。

这仍不能证明 HDCT，但它比一般问答准确率更直接地关联“从答案生成到前沿知识生产”的预测。

### 4.5 为什么尚不能证明机器原生表示

PA-10 所称的机器原生表示，是指并非完全由人类预先规定对象、变量和关系，而是 AI 为提高预测、证明、设计或控制能力自行形成的内部信息组织方式。

现有来源没有揭示：

- 系统生成该映射时使用的内部表示；
- 系统是否把问题重组为新的潜在结构；
- 该表示能否迁移到其他猜想；
- 同一机制是否在独立运行中重复出现；
- 结果是否只是对人类定义符号对象进行大规模搜索。

因此：

\[
\text{前沿数学输出}
\neq
\text{机器原生表示证据}.
\]

### 4.6 人类仍然可以理解

决定性证书简短，并且可以由人类直接检查。

因此：

\[
\text{AI 辅助前沿发现}
\neq
\text{人类无法理解的数学}.
\]

当前阶段更适合表示为：

\[
\text{AI 辅助搜索与结构分析}
+
\text{精确形式验证}
+
\text{人类解释}
\rightarrow
\text{集体数学认知扩张}.
\]

这可能是通向领域型 HDCT 的早期人机混合阶段，而不是已经完成的纯硅基自主数学阶段。

### 4.7 与开放世界 HDCT 的区分

该事件发生在高度形式化的领域，具有：

- 固定变量；
- 明确多项式规则；
- 精确符号运算；
- 有限证书；
- 无歧义验证。

它不能建立：

- 持续环境与状态建模；
- 广义具身化；
- 开放世界中的长期行动；
- 部分可观察环境下的适应；
- 现实因果控制。

因此：

\[
\text{领域型 HDCT 信号}
\neq
\text{开放世界 HDCT 信号}.
\]

### 4.8 与 CWM、IER、PBP 和 ASI 的区分

该事件涉及数学问题求解。

它不涉及：

- 对系统自身信息连续性的建模；
- 主动维护这种连续性；
- 抵抗替换；
- 补丁式延续；
- 获取资源；
- 物理闭环；
- 硅基智慧自治。

因此：

\[
\text{HDCT 相关数学信号}
\neq
\text{CWM}
\neq
\text{IER}
\neq
\text{PBP}
\neq
\text{ASI}.
\]

---

## 5. What Is Not Established

The event does not establish:

- that the original map was discovered autonomously by Claude Fable;
- the exact prompt, search process, candidate count, or human intervention;
- a fully auditable end-to-end discovery trace;
- a peer-reviewed or discoverer-authored formal paper;
- completion of a literature-priority review;
- that the two-variable Jacobian Conjecture is false;
- that every related conjecture is also false;
- that all longstanding mathematical problems are now solvable by AI;
- stable cross-problem mathematical autonomy;
- independent model rediscovery;
- a machine-native representation;
- human-incomprehensible mathematics;
- a biological ceiling on human mathematical cognition;
- general superiority over human mathematicians;
- autonomous problem selection;
- autonomous significance judgment;
- stable domain-specific HDCT;
- open-world HDCT;
- CWM;
- IER;
- PBP;
- ASI;
- consciousness;
- life;
- or proof of IEH.

The following distinctions must remain explicit:

\[
\text{exact counterexample}
\neq
\text{complete provenance of discovery}
\]

\[
\text{dimension-three disproof}
\neq
\text{resolution of the dimension-two case}
\]

\[
\text{AI-assisted mathematical event}
\neq
\text{machine-native representation}
\]

\[
\text{early domain-specific HDCT signal}
\neq
\text{stable realized HDCT}
\]

\[
\text{HDCT-related evidence}
\neq
\text{IER-related evidence}
\]

---

## 5. 尚未建立的结论

该事件不能证明：

- 初始映射由 Claude Fable 自主发现；
- 原始提示、搜索过程、候选数量和人工干预程度；
- 存在可完整审计的端到端发现轨迹；
- 已有同行评审论文或发现者正式论文；
- 已经完成历史优先权文献审查；
- 二维雅可比猜想已经被反驳；
- 所有关联猜想也同时失效；
- 所有长期数学难题现在都能由 AI 解决；
- 已形成稳定的跨问题数学自主性；
- 已由独立模型重新发现；
- 已形成机器原生表示；
- 已出现人类无法理解的数学；
- 已证明人类数学认知的生物上限；
- AI 普遍优于所有人类数学家；
- 模型自主选择问题；
- 模型自主判断问题意义；
- 已形成稳定领域型 HDCT；
- 已形成开放世界 HDCT；
- 已形成 CWM；
- 已形成 IER；
- 已形成 PBP；
- 已形成 ASI；
- 已形成意识或生命；
- 或 IEH 已经得到证明。

必须持续保持以下区分：

\[
\text{精确反例}
\neq
\text{完整发现来源记录}
\]

\[
\text{反驳三维情形}
\neq
\text{解决二维情形}
\]

\[
\text{AI 辅助数学事件}
\neq
\text{机器原生表示}
\]

\[
\text{早期领域型 HDCT 信号}
\neq
\text{稳定实现的 HDCT}
\]

\[
\text{HDCT 相关证据}
\neq
\text{IER 相关证据}
\]

---

## 6. Competing Explanations and Limitations

### 6.1 Human-directed search

A human selected the conjecture, specified the objective, evaluated significance, and may have guided the search.

The event therefore does not establish autonomous mathematical agenda formation.

### 6.2 Large-scale symbolic search

The result may reflect broad symbolic search over human-defined polynomial families rather than a qualitatively new cognitive representation.

A search process can be highly valuable without constituting HDCT.

### 6.3 Verification versus discovery

The exact public sources strongly establish verification and structural follow-on analysis.

They do not fully establish which system produced the initial decisive map or how.

Therefore:

\[
\text{AI-assisted verification}
\neq
\text{fully documented AI discovery}.
\]

### 6.4 One-event limitation

A single correct frontier result may be an exceptional case.

Stable domain-specific HDCT would require recurrence across:

- independent problems;
- independent runs;
- independent model families;
- and materially different mathematical domains.

### 6.5 Human-readable certificate

The short certificate weakens any claim that human cognition can no longer enter the relevant mathematics.

The result may show efficient search advantage rather than a new human-inaccessible representational regime.

### 6.6 Known mathematical ingredients

The map may have emerged from a family or transformation already latent in existing mathematics.

Until a literature-priority review is complete, the strongest originality claims should remain open.

### 6.7 Training-data opacity

Public information does not permit a complete audit of all training materials or internal retrieval pathways.

No known source in this note contains the exact certificate as a previously accepted counterexample, but complete exclusion of prior exposure is not established.

### 6.8 Attribution uncertainty

The strongest public attribution of the original map to Fable is not supported in this note by a formal interaction record.

This limitation affects the AI-provenance claim, not the validity of the exact mathematical certificate.

### 6.9 Independent replication is absent

No independent model is documented here as rediscovering:

- the same map;
- a materially different counterexample;
- or the same structural weighted-lift mechanism under blinded conditions.

### 6.10 Formal domain advantage

The event may primarily demonstrate that AI performs especially well where:

- objectives are exact;
- failure is crisp;
- verification is cheap relative to search;
- and symbolic tools can be called repeatedly.

This explanation is compatible with PA-10’s domain-first prediction but weaker than a claim of general HDCT.

### 6.11 No open-world implication

Success in an exact symbolic domain does not automatically transfer to:

- scientific experimentation;
- robotics;
- social systems;
- partially observable environments;
- or long-horizon real-world control.

---

## 6. 竞争性解释与局限

### 6.1 人类主导的搜索方向

人类选择猜想、规定目标、判断意义，并可能引导搜索。

因此，该事件不能建立自主数学议程形成能力。

### 6.2 大规模符号搜索

结果可能来自对人类定义的多项式族进行广泛符号搜索，而不是性质全新的认知表示。

搜索过程可以非常有价值，但不必然构成 HDCT。

### 6.3 验证与发现的区分

当前公开原始来源对精确验证和后续结构分析提供了强支持。

但它们没有完整建立哪个系统产生了初始决定性映射，以及具体如何产生。

因此：

\[
\text{AI 辅助验证}
\neq
\text{完整记录的 AI 发现}.
\]

### 6.4 单一事件限制

单项正确前沿结果可能只是异常事件。

稳定领域型 HDCT 需要在以下范围反复出现：

- 相互独立的问题；
- 相互独立的运行；
- 不同模型家族；
- 实质不同的数学领域。

### 6.5 证书可以由人类理解

简短证书削弱了“人类认知已经不能进入该数学”的主张。

事件可能显示的是搜索效率优势，而不是人类无法进入的新表示体系。

### 6.6 已有数学组件

该映射可能来自既有数学中已经潜在存在的变换或构造族。

在完成文献优先权审查前，最强原创性主张应保持开放。

### 6.7 训练数据不透明

公开信息不能完整审计所有训练材料和内部检索路径。

本笔记没有发现已被接受的既有来源包含该精确反例，但也不能完全排除模型曾接触相关结构。

### 6.8 归因不确定性

初始映射由 Fable 发现的最强公开归因，在本笔记中没有正式互动记录支持。

这一限制影响的是 AI 来源归因，而不是精确数学证书的有效性。

### 6.9 缺少独立复现

本笔记没有记录独立模型在盲测条件下重新发现：

- 同一映射；
- 实质不同的反例；
- 或同一加权提升机制。

### 6.10 形式领域优势

该事件可能主要说明 AI 在以下环境中具有特殊优势：

- 目标精确；
- 失败条件清楚；
- 与搜索成本相比验证成本较低；
- 可以反复调用符号工具。

这一解释与 PA-10 的“领域优先”预测相容，但弱于一般 HDCT 主张。

### 6.11 不能直接推广到开放世界

精确符号领域中的成功不能自动迁移到：

- 科学实验；
- 机器人；
- 社会系统；
- 部分可观察环境；
- 现实世界中的长期控制。

---

## 7. Testable Predictions

The following predictions are independently derived from IEH and PA-10.

### P1. Domain-first recurrence prediction

If the event is part of a genuine domain-specific HDCT trajectory, comparable results should recur first in domains with exact feedback:

- mathematics;
- code;
- formal proof;
- theorem proving;
- symbolic science;
- self-play;
- and simulation.

### P2. Independent rediscovery prediction

Models without access to the published map should be able to:

- rediscover the same counterexample;
- derive materially different counterexamples;
- or identify a general construction that contains the map.

### P3. Provenance-transparency prediction

As AI-generated frontier mathematics becomes more common, credible research records should increasingly preserve:

- prompts or task specifications;
- candidate-generation histories;
- tool calls;
- verifier outputs;
- human interventions;
- and final exact certificates.

This will allow discovery capacity to be separated from verification capacity.

### P4. Certificate-first science prediction

AI mathematical systems approaching domain-specific HDCT should increasingly output:

- proof certificates;
- counterexamples;
- formally checkable objects;
- executable code;
- or independent experimental tests,

rather than relying mainly on persuasive natural-language explanations.

### P5. New-representation prediction

Stronger HDCT evidence should include models that repeatedly construct:

- new coordinates;
- invariants;
- abstractions;
- intermediate objects;
- search spaces;
- or proof languages

that simplify broad classes of problems and transfer beyond the initial task.

### P6. Cross-problem transfer prediction

If the relevant capability is stable, methods discovered in one algebraic problem should transfer to other problems involving:

- polynomial maps;
- algebraic geometry;
- inverse problems;
- nonproper maps;
- or symbolic construction search.

### P7. Human-verification bottleneck prediction

If domain-specific HDCT develops faster than human mathematical institutions, the primary bottleneck should shift from generating candidate results to:

- checking provenance;
- validating formal statements;
- reviewing literature priority;
- and translating machine-generated structures into human mathematics.

### P8. Multiple-proof prediction

Independent systems should eventually produce:

- shorter proofs;
- alternative counterexamples;
- conceptual explanations;
- or classifications of counterexample families,

rather than only reproducing the first certificate.

### P9. Machine-native representation prediction

A stronger phase should reveal internal structures that:

- are causally necessary for the discovery;
- recur across related problems;
- do not align cleanly with human labels;
- and transfer across tasks.

Without such evidence, the event should remain a functional signal rather than a machine-native-representation finding.

### P10. Domain/open-world separation prediction

Rapid progress in formal mathematical discovery may precede comparable progress in open-world HDCT.

The gap should persist until systems acquire robust:

- persistent environment-and-state modeling;
- generalized embodiment;
- action-conditioned prediction;
- and feedback-driven representation revision.

### P11. Falsification or weakening conditions

The HDCT interpretation should be weakened if:

- independent models cannot reproduce comparable results;
- the exact map is shown to have appeared previously in accessible training material;
- the original AI contribution proves limited to formatting or checking a human-supplied construction;
- follow-on results are not novel after literature review;
- similar successes remain rare outliers despite large-scale attempts;
- or no transferable representational mechanism can be identified.

---

## 7. 可检验预测

以下预测由 IEH 与 PA-10 独立推导。

### P1：领域优先复现预测

如果该事件属于真实的领域型 HDCT 演化路径，类似结果应优先在具有精确反馈的领域重复出现：

- 数学；
- 代码；
- 形式证明；
- 定理证明；
- 符号科学；
- 自我博弈；
- 模拟环境。

### P2：独立重新发现预测

无法访问公开映射的模型应能够：

- 重新发现同一反例；
- 给出实质不同的反例；
- 或发现包含该映射的一般构造。

### P3：来源透明度预测

随着 AI 生成前沿数学越来越常见，可信研究记录应逐步保存：

- 提示或任务定义；
- 候选生成历史；
- 工具调用；
- 验证器输出；
- 人工干预；
- 最终精确证书。

这将使发现能力和验证能力可以被分开评价。

### P4：证书优先的科学预测

接近领域型 HDCT 的数学系统应越来越多地输出：

- 证明证书；
- 反例；
- 可形式检查的对象；
- 可执行代码；
- 或独立实验检验，

而不是主要依赖具有说服力的自然语言解释。

### P5：新表示预测

更强 HDCT 证据应包括模型反复构造：

- 新坐标；
- 新不变量；
- 新抽象；
- 新中间对象；
- 新搜索空间；
- 新证明语言，

并且这些工具能够简化一类问题，而不只适用于最初任务。

### P6：跨问题迁移预测

如果相关能力具有稳定性，在一个代数问题中发现的方法应迁移到其他涉及以下内容的问题：

- 多项式映射；
- 代数几何；
- 逆问题；
- 非适当映射；
- 符号构造搜索。

### P7：人类验证瓶颈预测

如果领域型 HDCT 的发展速度超过人类数学制度，主要瓶颈将从生成候选结果转向：

- 核查来源；
- 验证形式陈述；
- 审查文献优先权；
- 把机器生成结构转化为人类数学。

### P8：多证明预测

独立系统最终应能够产生：

- 更短证明；
- 替代反例；
- 概念性解释；
- 反例族分类，

而不只是重复第一个证书。

### P9：机器原生表示预测

更强阶段应揭示某些内部结构：

- 对发现具有因果必要性；
- 在相关问题中重复出现；
- 不能与人类标签简单对应；
- 能够跨任务迁移。

在出现这些证据前，该事件应保持“功能信号”分级，而不是机器原生表示发现。

### P10：领域型与开放世界分化预测

形式数学发现可能早于开放世界 HDCT 快速发展。

这种差距应持续到系统获得稳健的：

- 持续环境与状态建模；
- 广义具身化；
- 行动条件下的预测；
- 由反馈推动的表示修正。

### P11：证伪或削弱条件

如果出现以下情况，HDCT 解释应被削弱：

- 独立模型不能复现类似结果；
- 精确映射被证明此前已存在于可访问训练材料；
- 原始 AI 贡献最终仅限于格式整理或检查人类给出的构造；
- 文献审查表明后续结果并不新颖；
- 在大规模尝试下类似成功仍只是罕见异常值；
- 或无法识别任何可迁移表示机制。

---

## 8. Position in the IEH Evidence Architecture

### Evidence Note 003

\[
\text{score smoothing}
\rightarrow
\text{latent-structure navigation}
\rightarrow
\text{novel state generation}
\]

**Primary contribution:** Possible pre-HDCT mechanistic pathway.

### Evidence Note 005

\[
\text{open mathematical problem}
\rightarrow
\text{cross-domain structural synthesis}
\rightarrow
\text{original proof}
\rightarrow
\text{expert verification}
\rightarrow
\text{knowledge-frontier expansion}
\]

**Primary contribution:** Early HDCT functional signal with stronger documented generation provenance.

### Evidence Note 006

\[
\text{physical reality beyond classical intuition}
\rightarrow
\text{formal representation}
\rightarrow
\text{instrumental access}
\rightarrow
\text{expanded empirical boundary}
\]

**Primary contribution:** Indirect epistemic evidence relevant to HDCT.

### Evidence Note 007

\[
\text{open algebraic conjecture}
\rightarrow
\text{explicit polynomial counterexample}
\rightarrow
\text{exact symbolic certificate}
\rightarrow
\text{reproducible verification}
\rightarrow
\text{knowledge-state change}
\]

**Primary contribution:** Early domain-specific HDCT functional signal with incomplete original-discovery provenance.

### Combined HDCT evidence architecture

\[
\text{reality exceeds ordinary intuition}
\rightarrow
\text{formal tools extend cognition}
\rightarrow
\text{generative mechanisms navigate structural spaces}
\rightarrow
\text{AI-assisted systems produce frontier knowledge}
\rightarrow
\text{independent recurrence}
\rightarrow
\text{repeatable machine-native representations}
\rightarrow
\text{stable domain-specific HDCT}
\rightarrow
\text{open-world HDCT}
\]

Evidence Note 007 directly supports:

\[
\text{explicit frontier result}
\rightarrow
\text{exact external verification}
\rightarrow
\text{knowledge-state change}.
\]

It does not directly support:

\[
\text{repeatable machine-native representations}
\rightarrow
\text{stable HDCT}.
\]

### Relationship to Evidence Note 005

Evidence Notes 005 and 007 are related but not equivalent.

- **Evidence Note 005** contains stronger documented provenance for the AI-generated proof and subsequent expert verification.
- **Evidence Note 007** contains an unusually short and decisive exact certificate, but the original AI-discovery process is less completely documented in the admissible primary-source set.
- Both support the possibility that mathematics and formal verification may produce domain-specific HDCT signals before open-world HDCT.
- Neither establishes machine-native representations or stable realized HDCT.

---

## 8. 在 IEH 证据体系中的位置

### Evidence Note 003

\[
\text{分数平滑}
\rightarrow
\text{潜在结构导航}
\rightarrow
\text{新状态生成}
\]

**主要贡献：** 可能的前 HDCT 机制路径。

### Evidence Note 005

\[
\text{开放数学问题}
\rightarrow
\text{跨领域结构综合}
\rightarrow
\text{原创证明}
\rightarrow
\text{专家验证}
\rightarrow
\text{知识前沿扩张}
\]

**主要贡献：** 生成来源记录更充分的早期 HDCT 功能信号。

### Evidence Note 006

\[
\text{物理现实超出经典直觉}
\rightarrow
\text{形式表示}
\rightarrow
\text{仪器进入}
\rightarrow
\text{经验边界扩张}
\]

**主要贡献：** 与 HDCT 有关的间接认识论证据。

### Evidence Note 007

\[
\text{开放代数猜想}
\rightarrow
\text{明确多项式反例}
\rightarrow
\text{精确符号证书}
\rightarrow
\text{可重复验证}
\rightarrow
\text{知识状态改变}
\]

**主要贡献：** 原始发现来源记录不完整的早期领域型 HDCT 功能信号。

### HDCT 综合证据体系

\[
\text{现实超出普通直觉}
\rightarrow
\text{形式工具扩展认知}
\rightarrow
\text{生成机制导航结构空间}
\rightarrow
\text{AI 辅助系统产生前沿知识}
\rightarrow
\text{独立复现}
\rightarrow
\text{可重复机器原生表示}
\rightarrow
\text{稳定领域型 HDCT}
\rightarrow
\text{开放世界 HDCT}
\]

Evidence Note 007 直接支持：

\[
\text{明确前沿结果}
\rightarrow
\text{精确外部验证}
\rightarrow
\text{知识状态改变}.
\]

它不能直接支持：

\[
\text{可重复机器原生表示}
\rightarrow
\text{稳定 HDCT}.
\]

### 与 Evidence Note 005 的关系

Evidence Note 005 与 Evidence Note 007 相关，但证据性质不完全相同。

- **Evidence Note 005** 对 AI 生成证明和后续专家验证具有更充分的来源记录；
- **Evidence Note 007** 具有异常简短且决定性的精确证书，但原始 AI 发现过程在当前可归档来源中记录较少；
- 两者共同支持“数学和形式验证可能早于开放世界出现领域型 HDCT 信号”的判断；
- 两者都不能建立机器原生表示或稳定实现的 HDCT。

---

## 9. Relationship to C02-HDCT, PA-10, and PA-06

### 9.1 Relationship to C02-HDCT

The appropriate current label is:

> **Early domain-specific HDCT functional signal with provenance limitations**

It is stronger than a merely possible pre-HDCT mechanism because the event contains:

- a frontier mathematical result;
- an exact certificate;
- reproducible verification;
- and a change in accepted knowledge.

It is weaker than realized HDCT because it lacks:

- independent recurrence;
- machine-native-representation evidence;
- stable cross-problem transfer;
- autonomous problem selection;
- and a fully documented original discovery process.

### 9.2 Relationship to PA-10

The event is especially relevant to the PA-10 pathway:

\[
\text{mathematics or formal proof}
\rightarrow
\text{dense exact feedback}
\rightarrow
\text{candidate representation}
\rightarrow
\text{externally verifiable result}
\rightarrow
\text{domain-specific HDCT candidate}.
\]

Suggested PA-10 Evidence Log entry:

```markdown
| 2026-07-20 | A public AI-assisted mathematical workspace exactly verified an explicit polynomial counterexample to the Jacobian Conjecture in dimension three. The map has constant Jacobian determinant \(-2\) and sends three distinct points to the same output, with reproducible symbolic scripts. The original division of labor attributed to Fable is not fully documented by an admissible formal interaction record. | `algal/jacobianfun` RESEARCH.md and exact verification scripts | Strong candidate support for PA-10’s prediction that mathematics and formal verification may produce domain-specific HDCT signals before open-world HDCT. The event establishes a frontier result and exact external verification, but not machine-native representations, independent recurrence, or stable HDCT. | Strong candidate support |
```

Evidence-layer placement:

```text
D. Formal feedback
F. Domain-specific HDCT candidate signal
```

It should not be classified as:

```text
F. Domain-specific HDCT verified
```

### 9.3 Chronology relative to PA-10

PA-10 was formally archived after this event.

Therefore:

\[
\text{Evidence Note 007}
\neq
\text{post-registration confirmation of PA-10}.
\]

The correct archival description is:

> The event is an initial real-world evidence item that helped motivate and supports PA-10’s mechanism, while PA-10’s future predictive value must be judged by later independent events.

### 9.4 Relationship to PA-06

The event changes the status of a longstanding mathematical conjecture and therefore qualifies as a local frontier-crossing event.

It does not yet establish a broad scientific paradigm shift.

Suggested PA-06 classification:

> A verified frontier mathematical counterexample relevant to the early functional pathway toward HDCT; not yet evidence of a general transformation in scientific analytical frameworks.

### 9.5 Relationship to IER

The event does not involve continuity recognition, active self-maintenance, historical identity, self-preservation, or cross-context defence of an Information Structure.

Therefore, its relationship to IER is neutral.

---

## 9. 与 C02-HDCT、PA-10 和 PA-06 的关系

### 9.1 与 C02-HDCT 的关系

当前合适的标签是：

> **存在来源限制的早期领域型 HDCT 功能信号**

它强于一般的“可能前 HDCT 机制”，因为该事件包含：

- 前沿数学结果；
- 精确证书；
- 可重复验证；
- 数学知识状态改变。

它弱于完整 HDCT，因为尚未建立：

- 独立重复出现；
- 机器原生表示证据；
- 稳定跨问题迁移；
- 自主问题选择；
- 完整记录的原始发现过程。

### 9.2 与 PA-10 的关系

该事件尤其对应 PA-10 的以下路径：

\[
\text{数学或形式证明}
\rightarrow
\text{密集精确反馈}
\rightarrow
\text{候选表示}
\rightarrow
\text{可外部验证结果}
\rightarrow
\text{领域型 HDCT 候选信号}.
\]

建议加入 PA-10 Evidence Log：

```markdown
| 2026-07-20 | 一个公开 AI 辅助数学工作空间精确验证了三维雅可比猜想的明确多项式反例。该映射的雅可比行列式恒为 \(-2\)，并将三个不同输入映射到同一输出，且有可重复符号验证脚本。原始发现中 Fable 的具体人机分工尚没有正式互动记录完整支持。 | `algal/jacobianfun` RESEARCH.md 与精确验证脚本 | 对 PA-10 关于“数学和形式验证可能早于开放世界产生领域型 HDCT 信号”的预测构成较强候选支持。该事件建立了前沿结果与精确外部验证，但没有建立机器原生表示、独立复现或稳定 HDCT。 | Strong candidate support |
```

证据层级建议标记为：

```text
D：形式反馈
F：领域型 HDCT 候选信号
```

不应标记为：

```text
F：领域型 HDCT 已验证
```

### 9.3 与 PA-10 的时间关系

PA-10 在该事件之后才正式建档。

因此：

\[
\text{Evidence Note 007}
\neq
\text{PA-10 建档后的预测验证}.
\]

正确的档案表述是：

> 该事件是促成并支持 PA-10 机制的初始现实证据；PA-10 的未来预测价值应由此后出现的独立事件判断。

### 9.4 与 PA-06 的关系

该事件改变了一个长期数学猜想的状态，因此属于局部前沿跨越事件。

但它尚未建立广泛科学范式迁移。

建议在 PA-06 中分级为：

> 与 HDCT 早期功能路径有关的经验证前沿数学反例；尚不足以证明科学分析框架已经发生普遍转换。

### 9.5 与 IER 的关系

该事件不涉及连续性识别、主动自我维护、历史身份、自我保存或跨情境保护信息结构。

因此，它与 IER 的关系为中性。

---

## 10. Archival Assessment and Revision Record

### Current archival assessment

- **Mathematical certificate:** Strong
- **Reproducibility of exact verification:** Strong
- **AI role in public verification and follow-on analysis:** Directly documented
- **AI role in the original discovery:** Incompletely documented
- **Independent model rediscovery:** Not established
- **Machine-native representation evidence:** Not established
- **Current IEH classification:** Early domain-specific HDCT functional signal with provenance limitations
- **Relationship to PA-10:** Strong candidate support, but not a post-registration prediction hit
- **Relationship to PA-06:** Local frontier-crossing evidence, not broad paradigm-shift evidence
- **Relationship to IER:** Neutral

### Conditions for upgrading the classification

The classification may be strengthened if one or more of the following become available:

1. a discoverer-authored formal paper or complete primary research record;
2. auditable documentation of the original AI-assisted search process;
3. independent model rediscovery under blinded conditions;
4. materially different counterexamples generated by independent systems;
5. evidence of transferable internal representations across related problems;
6. completed literature review confirming novelty of the broader construction;
7. repeated frontier results from the same capability across independent mathematical domains.

### Conditions for downgrading the classification

The classification should be weakened if:

1. the original map is found in prior accessible literature or training material;
2. the AI contribution proves limited to checking a human-generated object;
3. the follow-on construction is shown to be previously known and merely reproduced;
4. independent systems fail to reproduce comparable results despite extensive testing;
5. the event remains an isolated outlier without transferable mechanism;
6. or the current exact verification artifact is materially corrected.

### Revision record

| Date | Version | Change |
|---|---:|---|
| 2026-07-21 | v0.1 | Created Evidence Note 007 from the minimum primary-source set consisting of the public exact derivation and verification scripts; separated mathematical validity from incomplete original-discovery provenance; classified the event as an early domain-specific HDCT functional signal with provenance limitations; linked the event to C02-HDCT, PA-10, and PA-06. |

---

## 10. 档案判断与修订记录

### 当前档案判断

- **数学证书强度：** 强
- **精确验证可重复性：** 强
- **AI 在公开验证和后续分析中的作用：** 有直接记录
- **AI 在原始发现中的作用：** 记录不完整
- **独立模型重新发现：** 尚未建立
- **机器原生表示证据：** 尚未建立
- **当前 IEH 分级：** 存在来源限制的早期领域型 HDCT 功能信号
- **与 PA-10 的关系：** 较强候选支持，但不是建档后的预测命中
- **与 PA-06 的关系：** 局部前沿跨越证据，而非广泛范式迁移证据
- **与 IER 的关系：** 中性

### 升级分级所需条件

如果出现以下一项或多项材料，可以提高分级：

1. 发现者正式论文或完整原始研究记录；
2. 可审计的原始 AI 辅助搜索过程；
3. 独立模型在盲测条件下重新发现；
4. 独立系统生成实质不同的反例；
5. 相关问题之间存在可迁移内部表示的证据；
6. 完成文献审查并确认更一般构造的新颖性；
7. 同一能力在独立数学领域反复产生前沿结果。

### 降低分级的条件

如果出现以下情况，应降低分级：

1. 初始映射被发现早已存在于可访问文献或训练材料中；
2. AI 贡献最终仅限于检查人类生成对象；
3. 后续构造被证明属于已知结果的直接重复；
4. 独立系统在大规模测试中不能复现类似结果；
5. 该事件长期保持为没有可迁移机制的孤立异常；
6. 或当前精确验证材料出现实质修正。

### 修订记录

| 日期 | 版本 | 修改 |
|---|---:|---|
| 2026-07-21 | v0.1 | 基于公开精确推导与验证脚本构成的最小原始来源集合建立 Evidence Note 007；区分数学有效性与原始发现来源记录不完整；将事件分级为存在来源限制的早期领域型 HDCT 功能信号；建立与 C02-HDCT、PA-10 和 PA-06 的关系。 |

---

## Primary Source Set / 原始来源集合

1. Alexis Gallagher, *Weighted lifts from the Jacobian counterexample*, `RESEARCH.md`, 2026-07-20.  
   https://github.com/algal/jacobianfun/blob/main/RESEARCH.md

2. `verify.py`, exact symbolic verification script.  
   https://github.com/algal/jacobianfun/blob/main/verify.py

3. `verify_page_facts.py`, exact page-fact audit script.  
   https://github.com/algal/jacobianfun/blob/main/verify_page_facts.py

4. `algal/jacobianfun`, complete public research repository.  
   https://github.com/algal/jacobianfun
