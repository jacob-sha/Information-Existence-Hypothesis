# Evidence Note 023: OpenAI's Navier–Stokes Candidate Solution and the HDCT Evolution Pathway

**Repository function:** Research record / evidence index  
**Document type:** Non-narrative external evidence note  
**Status:** Preliminary and revisable; candidate milestone; draft for review  
**Relation to IEH:** Candidate landmark case on the silicon-based cognitive evolution / HDCT pathway; preliminary output-level evidence of frontier AI generating candidate new results on a major scientific frontier without an established human solution; indirect epistemic relevance to HDCT, not evidence of realized HDCT, machine-native representations, EIC, or IER  
**Primary IEH corollary:** C02-HDCT — High-dimensional Cognitive Tools  
**Related prediction record:** PA-10 — From Language Models to Machine-Native Representations: Model Evolution Pathways Toward HDCT  
**Related evidence notes:** Evidence Note 020; Evidence Note 021; Evidence Note 022  
**Author of IEH analysis:** Jacob Sha  
**Version:** v0.1 — review draft  
**Date:** 2026-09-10  
**Source-status cutoff:** 2026-09-10

> **Publication boundary:** This file is a compact research record, not a publication draft. The broader arguments about the evolution of silicon cognition, scientific paradigm change, and the possible separation of machine representations from human cognitive tools are reserved for future work.

> **Source-use boundary:** The mathematical evidence is the original analytical manuscript and official Lean repository. OpenAI's first-party research-process account is retained only for release date, AI attribution, and workflow provenance not established by the proof itself. Clay's original formulation and official status page serve only to identify the target and its institutional status. This is the minimum primary-source set needed for these distinct claims. Publicity conclusions, secondary news, social-media commentary, and other discovery leads are excluded; no substantial source passage is reproduced.

> **Verification boundary:** This note checks source identity, stated theorem scope, selected proof sections, formalization declarations, and reported verification status. It is not a line-by-line mathematical referee report, a local Lean rebuild, or an independent correctness certificate. “Candidate” describes this note's evidential assessment, even where the issuing organization states a stronger conclusion.

---

# 证据笔记 023：OpenAI 的 Navier–Stokes 候选解法与 HDCT 演化路径

**仓库功能：** 研究记录 / 证据索引  
**文档类型：** 非叙事性外部证据笔记  
**状态：** 初步记录，可修订；候选标志性案例；待审阅草稿  
**与 IEH 的关系：** 硅基认知演化／HDCT 演化路径上的候选标志性案例；为前沿 AI 在人类尚无公认解答的重大科学前沿生成候选新结果提供初步的成果层证据；对 HDCT 具有间接认识论关联，不是已实现 HDCT、机器原生表示、EIC 或 IER 的证据  
**主要 IEH 推论：** C02-HDCT——高维认知工具  
**相关预测档案：** PA-10——从语言模型到机器原生表示：HDCT 的模型演化路径  
**相关证据笔记：** Evidence Note 020；Evidence Note 021；Evidence Note 022  
**IEH 分析作者：** Jacob Sha  
**版本：** v0.1 — 审阅草稿  
**日期：** 2026-09-10  
**来源状态核验截止日：** 2026-09-10

> **投稿边界：** 本文件只是简明研究记录，不是投稿文章初稿。关于硅基认知演化、科学范式转变，以及机器表示可能与人类认知工具逐步分离的完整论证，保留给未来研究。

> **来源使用边界：** 数学证据采用原始分析证明与官方 Lean 仓库。OpenAI 的一手研究过程记录仅用于证明本身不能建立的发布日期、AI 归属与工作流来源。Clay 的原始问题说明与官方状态页只用于确定目标命题及机构状态。上述材料构成建立不同主张所需的最小原始来源集合。宣传性结论、二次新闻、社交媒体评论及其他发现线索不进入证据档案；不复制原始出处的大段表达。

> **核验边界：** 本笔记核对了来源身份、定理声明范围、选定证明章节、形式化声明以及所报告的验证状态；不构成逐行数学审稿、本地 Lean 重新构建或独立正确性证书。即使发布机构使用更强的结论措辞，本笔记仍以“候选”表达自身的证据判断。

---

## 1. Source Record

### S1 — Original analytical proof

- **Title:** *Finite time blowup for Navier–Stokes*
- **Author:** OpenAI
- **Platform:** OpenAI-hosted research manuscript
- **Release association:** Linked from the first-party release dated 2026-09-08 (S3); the accessed manuscript's first page does not supply a separate publication date or version number.
- **Primary URL:** [Original analytical manuscript](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf)
- **Material / evidence class:** Original mathematical proof manuscript; formal-result claim, not treated here as peer-reviewed research.
- **Relevant locations:** Theorem 1.1; Sections 2–3; Section 10, particularly Corollary 10.6.
- **Verification status:** Candidate analytical result; independent full verification not established by this source check.

### S2 — Official formalization artifact

- **Title / owner:** *NavierStokesAndEuler* / OpenAI
- **Platform / identifier:** GitHub, `openai/NavierStokesAndEuler`, accessed `main` on 2026-09-10.
- **Primary URL:** [Official Lean repository](https://github.com/openai/NavierStokesAndEuler)
- **Material / evidence class:** Author-issued Lean formalization, theorem statements, build instructions, and verification metadata.
- **Files checked:** `README.md`; `formalization.yaml`; `NavierStokes/ComparatorSolution.lean`; `ComparatorChallenges/README.md`; reference statement `ComparatorChallenges/NavierStokes.lean`.
- **Version boundary:** No immutable commit identifier was established in this check; the cited branch can change. Later reproducibility work must pin a commit and dependencies.
- **Verification status:** The metadata is self-assessed. Its zero-`sorry` claim concerns the submitted main results; the reference challenge contains intentional placeholders and must be distinguished from the proof dependency graph.

### S3 — First-party research-process record

- **Title:** *On the Navier–Stokes Millennium Prize Problem*
- **Issuing organization / platform:** OpenAI / official research page
- **Publication date:** 2026-09-08
- **Primary URL:** [First-party research-process account](https://openai.com/index/navier-stokes-solution/)
- **Material / evidence class:** Institutional first-party operational account; not independent verification or a substitute for S1–S2.
- **Permitted use:** Publication, model attribution, coordinated-agent workflow, and human orchestration.

### S4–S5 — Target definition and institutional status

- **S4:** Charles L. Fefferman, *Existence and Smoothness of the Navier–Stokes Equation*, Clay Mathematics Institute, [official problem formulation](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf). Used for alternatives (C)/(D) and their force, smoothness, decay, periodicity, and energy requirements. The URL's upload path is not used as an original publication date.
- **S5:** Clay Mathematics Institute, *Navier-Stokes Equation*, [official problem-status page](https://www.claymath.org/millennium/navier-stokes-equation/), accessed 2026-09-10; no separate update date established.
- **Evidence class:** Authoritative problem specification / institutional status record, not an independent review of S1.

### Minimum-source and verification-status boundary

S1 states the mathematics; S2 exposes its claimed formal counterpart; S3 supplies provenance; S4 fixes what problem is being addressed; S5 supplies an institutional status check. They are not five independent confirmations. Independent mathematical review, reproducible proof checking, discovery-process replication, and recognition of a prize problem are separate questions. No secondary report is used to certify any of them.

---

## 1. 来源记录

### S1——原始分析证明

- **标题：** *Finite time blowup for Navier–Stokes*
- **作者：** OpenAI
- **平台：** OpenAI 托管研究稿件
- **发布关联：** 由日期为 2026-09-08 的一手发布记录 S3 链接；所读取稿件首页没有单列发表日期或版本号。
- **原始链接：** [原始分析证明](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf)
- **材料性质／证据类别：** 原始数学证明稿件；形式结果主张，本笔记不将其视为已同行评审的研究。
- **相关位置：** Theorem 1.1；第 2–3 节；第 10 节，尤其 Corollary 10.6。
- **验证状态：** 候选分析结果；本次来源核验未建立完整独立验证。

### S2——官方形式化文件

- **标题／所属机构：** *NavierStokesAndEuler*／OpenAI
- **平台／编号：** GitHub，`openai/NavierStokesAndEuler`；于 2026-09-10 读取 `main`。
- **原始链接：** [官方 Lean 仓库](https://github.com/openai/NavierStokesAndEuler)
- **材料性质／证据类别：** 作者发布的 Lean 形式化、定理声明、构建说明及验证元数据。
- **已核对文件：** `README.md`；`formalization.yaml`；`NavierStokes/ComparatorSolution.lean`；`ComparatorChallenges/README.md`；参考命题 `ComparatorChallenges/NavierStokes.lean`。
- **版本边界：** 本次未建立不可变的提交标识；所引分支可能变化。后续复现必须固定提交版本与依赖。
- **验证状态：** 元数据中的审查为发布方自评。零 `sorry` 主张针对提交的主要结果；参考挑战文件含有有意设置的占位符，必须与证明依赖图区分。

### S3——一手研究过程记录

- **标题：** *On the Navier–Stokes Millennium Prize Problem*
- **发布机构／平台：** OpenAI／官方研究页
- **发布日期：** 2026-09-08
- **原始链接：** [一手研究过程说明](https://openai.com/index/navier-stokes-solution/)
- **材料性质／证据类别：** 机构一手运行过程记录；不是独立验证，也不替代 S1–S2。
- **限定用途：** 发布事实、模型归属、多 Agent 协作流程及人类组织作用。

### S4–S5——目标定义与机构状态

- **S4：** Charles L. Fefferman，*Existence and Smoothness of the Navier–Stokes Equation*，Clay Mathematics Institute，[官方问题说明](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf)。用于核对 (C)/(D) 及其外力、光滑性、衰减、周期性和能量要求。不把链接中的上传路径日期当作原始发表日期。
- **S5：** Clay Mathematics Institute，*Navier-Stokes Equation*，[官方问题状态页](https://www.claymath.org/millennium/navier-stokes-equation/)，于 2026-09-10 读取；未确认单独的更新日期。
- **证据类别：** 权威问题定义／机构状态记录；不是对 S1 的独立审查。

### 最小来源集合与验证状态边界

S1 给出数学主张，S2 提供其声称对应的形式化，S3 提供研究过程来源，S4 固定目标命题，S5 核对机构状态。它们不是五次独立确认。独立数学审查、可复现证明检查、发现过程复现及千禧年问题的正式认可，是不同问题；本笔记不以二次报道认证其中任何一项。

---

## 2. Minimal Finding Index

| ID | Primary-source finding | Source / location | Evidential boundary |
|---|---|---|---|
| F1 | OpenAI released an AI-attributed candidate proof on 2026-09-08. It attributes discovery to an internal model more capable than GPT-6 Astra, with Astra subsequently used for formalization. | S3, opening and research-process section | First-party attribution; not a controlled model comparison. |
| F2 | The manuscript claims, for every positive viscosity, finite-time velocity blowup from rest in three-dimensional incompressible Navier–Stokes flow, with a smooth force compactly supported in space and time and uniformly bounded kinetic energy before blowup; it also states a periodic result. | S1, Theorem 1.1 and Corollary 10.6 | Forced result; not unforced Navier–Stokes or an experimental observation of real fluids. |
| F3 | The official target permits the specified smooth forcing in breakdown alternatives (C)/(D). | S4, alternatives (C)/(D) | Forcing alone does not disqualify a result, but exact hypotheses must be checked. |
| F4 | OpenAI reports a coordinated search group of roughly 10,000 concurrent agents and human-directed resource allocation, model updates, and consolidation of intermediate insights. | S3, research-process section | Approximate publisher-reported scale; not independently audited, and not a single-agent result. |
| F5 | Official metadata declares full formalization of main results, zero proof placeholders, and the listed axioms `propext`, `Classical.choice`, `Quot.sound`; review is `self-assessed`. | S2, `formalization.yaml` | Inspectable declaration of verification scope, not an independently reproduced build result. |
| F6 | The submission exposes (C)/(D) theorem names through proof adapters; separate Comparator checking instructions and reference challenges are provided. | S2, submission and Comparator files | Availability of a checking route is distinct from a reported independent successful run. |
| F7 | The accessed Clay page still labels the problem unsolved. | S5, status heading | Institutional page status at access; neither a refutation of S1 nor proof that no independent checking exists anywhere. |

---

## 2. 最小事实索引

| ID | 原始来源发现 | 来源／位置 | 证据边界 |
|---|---|---|---|
| F1 | OpenAI 于 2026-09-08 发布归属于 AI 的候选证明；将发现归于能力高于 GPT-6 Astra 的内部模型，并说明随后使用 Astra 进行形式化。 | S3，开篇与研究过程部分 | 发布方一手归属；不是受控模型比较。 |
| F2 | 稿件主张：对任意正黏度，三维不可压 Navier–Stokes 流可从静止出发，在时空紧支撑光滑外力作用下出现有限时间速度发散，发散前动能一致有界；并给出周期情形结果。 | S1，Theorem 1.1 与 Corollary 10.6 | 属于有外力结果；不是无外力 Navier–Stokes，也不是对真实流体的实验观察。 |
| F3 | 官方目标命题的破裂选项 (C)/(D) 允许满足规定条件的光滑外力。 | S4，(C)/(D) | 有外力本身不使结果失去资格，但必须核对全部具体假设。 |
| F4 | OpenAI 报告，相关协作搜索组约有 10,000 个并发 Agent，并有人类主导的资源调整、模型更新及中间成果汇总。 | S3，研究过程部分 | 发布方报告的近似规模；未经独立审计，不是单个 Agent 的结果。 |
| F5 | 官方元数据声明主要结果已完整形式化、证明占位符为零，所列公理为 `propext`、`Classical.choice`、`Quot.sound`；审查字段为 `self-assessed`。 | S2，`formalization.yaml` | 可检查的验证范围声明，不是独立复现的构建结果。 |
| F6 | 提交文件通过证明适配层提供 (C)/(D) 定理名称；另有 Comparator 检查说明和参考挑战。 | S2，提交文件及 Comparator 文件 | 提供检查途径，不等于已报告一次独立成功检查。 |
| F7 | 本次读取的 Clay 页面仍把该问题标为未解决。 | S5，状态标题 | 仅代表读取时的机构页面状态；既不反驳 S1，也不证明任何地方都不存在独立检查。 |

---

## 3. IEH Evidence Classification

| Dimension | Current classification |
|---|---|
| Evidence type | Original mathematical-output artifact; author-issued formalization; first-party account of an AI research workflow |
| Setting | Computational mathematical research, not a physical fluid experiment or internal-representation intervention |
| Artifact availability | Established by direct source access |
| Mathematical correctness | Candidate result; publisher reports verification; this note has not independently certified it |
| Independent replication | Neither full independent proof checking nor discovery-process replication established in this check |
| Directness to silicon cognitive capability | Output-level, preliminary support for candidate frontier-result generation |
| Directness to C02-HDCT / PA-10 | Indirect epistemic / pathway relevance; no direct representation-mechanism evidence |
| EIC / proto-IER / IER | No evidence supplied by this case |
| Overall IEH status | Preliminary and revisable; candidate landmark case, not realized HDCT |

**Strongest justified conclusion:** A frontier AI research system has entered the production of inspectable candidate new results at a major frontier lacking an established human answer. This supports recording a candidate cognitive-capability milestone. It does not yet establish that the candidate is an accepted solution, that its discovery was independent of all human contributions, or that new machine-native cognitive tools caused it.

The strength of a mathematical certificate and the strength of an explanation of how it was discovered must be graded separately. Even independently verified mathematics would not automatically upgrade the HDCT mechanism classification.

---

## 3. IEH 证据分级

| 维度 | 当前分级 |
|---|---|
| 证据类型 | 原始数学成果文件；作者发布的形式化；AI 研究工作流的一手说明 |
| 研究场景 | 计算数学研究；不是物理流体实验或内部表征干预 |
| 成果文件可获得性 | 已通过直接读取来源确认 |
| 数学正确性 | 候选结果；发布方报告已验证；本笔记未作独立认证 |
| 独立复现 | 本次未建立完整独立证明检查或发现过程复现 |
| 对硅基认知能力的直接程度 | 成果层面，初步支持前沿候选结果生成能力 |
| 对 C02-HDCT／PA-10 的直接程度 | 间接认识论／演化路径关联；没有直接的表征机制证据 |
| EIC／proto-IER／IER | 本案例不提供相关证据 |
| IEH 总体状态 | 初步、可修订；候选标志性案例，不是已实现 HDCT |

**当前能够成立的最强结论：** 前沿 AI 研究系统已经开始在人类尚无公认答案的重大前沿问题上生成可供检查的候选新结果。这支持将其记录为候选认知能力里程碑，但尚不能证明该候选已经成为公认解法、其发现独立于全部人类贡献，或其成果由新型机器原生认知工具导致。

数学证书的强度与“究竟如何发现它”的解释强度必须分别分级。即使数学结果得到独立验证，也不能自动升级 HDCT 机制判断。

---

## 4. Core IEH Interpretation

### 4.1 Candidate landmark on an evolutionary pathway

**The following is IEH analysis, not a conclusion of the source authors.** A significant transition would be from reproducing available answers to generating externally checkable candidates where no accepted answer is available. The present case is relevant to that transition at the level of submitted outputs.

“Silicon-based cognitive evolution” here names a proposed trajectory of expanding scientific capability. It does not assert autonomous biological-style evolution, independent goals, or life. “Candidate landmark” preserves both the possible significance and the unresolved verification burden.

### 4.2 New result does not identify a new cognitive tool

The following distinctions are necessary:

`candidate new mathematical result ≠ accepted new result ≠ demonstrated machine-native representation ≠ realized HDCT`

A hard unsolved problem is not itself a measurement of representational dimensionality. Discovery difficulty, proof length, agent count, or human review time cannot identify the internal mechanism. Producing an answer humans had not found also does not imply that humans cannot understand or reconstruct the tool that produced it.

### 4.3 A plausible precursor, with an open causal question

The pathway worth testing is:

`candidate generation → external checking and error feedback → reusable reasoning or representation changes → transfer to new problems → possible HDCT`

The present record reaches candidate generation and a published verification interface. It does not show that feedback produced enduring representation changes or that such changes caused the mathematical achievement. Verification of an output is not evidence of a completed self-improvement loop.

---

## 4. IEH 核心解释

### 4.1 演化路径上的候选标志性案例

**以下属于 IEH 分析，不是原始来源作者的结论。** 一项具有意义的跃迁，是从复现已有答案转向：在尚无公认答案的问题上生成能够接受外部检验的候选成果。本案例在提交成果层面与这一跃迁有关。

这里的“硅基认知演化”指向科学认知能力扩张的候选路径，不意味着系统已经具备生物式自主演化、独立目标或生命。“候选标志性案例”同时保留潜在重要性与尚未完成的验证责任。

### 4.2 新结果不能直接识别新认知工具

必须保持以下区分：

`候选数学新结果 ≠ 公认新结果 ≠ 已证明机器原生表示 ≠ 已实现 HDCT`

一道长期未解难题本身不是表征维度的测量。发现难度、证明长度、Agent 数量或人类审查耗时，都不能识别内部机制。产生人类此前没有找到的答案，也不等于人类无法理解或重建产生答案的工具。

### 4.3 可研究的前置路径，尚未解决的因果问题

值得检验的路径是：

`候选生成 → 外部检查与错误反馈 → 可复用的推理或表征变化 → 向新问题迁移 → 可能的 HDCT`

当前记录到达候选生成与公开验证接口，尚未证明反馈形成了持续的表征变化，也没有证明这种变化导致了数学成果。一个输出受到验证，不等于自我改进闭环已经完成。

---

## 5. What Is Not Established

This case does not establish:

1. an independently certified or institutionally accepted final resolution of the Millennium Prize Problem;
2. finite-time blowup for unforced Navier–Stokes, generic turbulence prediction, or practical control of real fluids;
3. that a single agent achieved the result without human orchestration or inherited mathematics;
4. non-human-native representations, a new machine communication language, or causal evidence of high-dimensional cognitive tools;
5. repeatable superiority of a reusable representational tool across problems, or inability of unaided humans to reconstruct that tool;
6. a scientific paradigm shift or realized HDCT;
7. endogenous maintenance of the system's own informational history, EIC, proto-IER, IER, CWM, or PBP;
8. stable identity, consciousness, subjective experience, life, or proof of IEH.

Formal checking concerns the encoded proposition and its trusted foundations. A separate semantic audit must establish correspondence to the intended mathematical statement; neither check establishes a theory of cognition.

---

## 5. 尚未建立的结论

本案例不能证明：

1. 千禧年问题已经获得独立认证或机构公认的最终解答；
2. 无外力 Navier–Stokes 的有限时间奇点、一般湍流预测或真实流体的实用控制；
3. 单个 Agent 在没有人类组织或既有数学支持的情况下完成成果；
4. 非人类原生表征、新型机器通信语言，或高维认知工具的因果证据；
5. 可复用表征工具在跨问题条件下的稳定优势，或未经辅助的人类无法重建该工具；
6. 科学范式转移或 HDCT 已经实现；
7. 系统对自身信息历史的内生维护、EIC、proto-IER、IER、CWM 或 PBP；
8. 稳定身份、意识、主观体验、生命，或 IEH 已被证明。

形式检查针对被编码的命题及其可信基础；还需单独进行语义核对，确认它与目标数学命题对应。这两种检查都不能建立认知机制理论。

---

## 6. Competing Explanations and Limitations

| Alternative / limitation | Why it remains viable | Evidence needed to distinguish it |
|---|---|---|
| Large-scale parallel search and compute | More attempts and selection can produce rare successful combinations without a new representational tool. | Match total compute, available information, and verification budget; compare independent search against coordinated search. |
| Existing human mathematical frameworks | A novel theorem or construction can arise within inherited concepts and proof methods. Novel output does not entail representational novelty. | Identify the claimed new tool and show what it adds beyond conventional reformulation. |
| Multi-agent aggregation | Division of labor, cross-checking, and synthesis can account for system-level gains. | Ablate communication and aggregation while matching resources and task access. |
| Human orchestration and tool scaffolding | Problem selection, intermediate guidance, model replacement, and formal tooling may materially determine success. | Audit the contribution timeline and compare matched levels of human assistance. |
| Training or retrieval overlap | Prior mathematical content may explain important steps; the public output alone cannot establish the provenance of every idea. | Auditable training/retrieval boundaries and provenance checks; do not assume either contamination or complete independence. |
| Selection and reporting effects | A prominent success without the full denominator does not establish a general frontier-solving rate. | Preregister a diverse problem set, record failures and costs, and repeat across independent systems. |
| Verification or statement mismatch | A manuscript, encoded theorem, and intended target can differ; availability of code does not remove that risk. | Independently rebuild a pinned artifact, audit dependencies and axioms, and examine semantic alignment. |

These explanations can coexist. They do not negate a valid mathematical achievement, but they prevent attributing it uniquely to HDCT. No representation measurement or causal ablation in the checked materials discriminates among them.

---

## 6. 竞争性解释与局限

| 替代解释／局限 | 为什么仍然成立 | 区分它所需要的证据 |
|---|---|---|
| 大规模并行搜索与算力规模 | 增加尝试和筛选次数，可能得到罕见的成功组合，无需出现新表征工具。 | 匹配总算力、可用信息和验证预算，比较独立搜索与协作搜索。 |
| 人类既有数学框架 | 新定理或新构造可以产生于继承的概念与证明方法内部；输出创新不等于表征创新。 | 识别所声称的新工具，证明其贡献超出常规重述。 |
| 多 Agent 聚合 | 分工、交叉检查与综合可以解释系统层面的增益。 | 在匹配资源与任务访问条件下，消融通信与聚合机制。 |
| 人类组织与工具支撑 | 选题、中间指导、模型替换及形式工具可能实质性影响成功。 | 审计贡献时间线，比较人类协助程度匹配的条件。 |
| 训练或检索重叠 | 既有数学内容可能解释重要步骤；公开结果本身不能建立每项思想的来源。 | 审计训练／检索边界与来源；既不预设污染，也不预设完全独立。 |
| 筛选与报告效应 | 缺少全部尝试分母时，一个突出成功不能建立普遍前沿解题率。 | 预注册多样问题集，记录失败与成本，并跨独立系统重复。 |
| 验证或命题错配 | 稿件、编码命题与实际目标可能不同；代码公开不能消除这种风险。 | 独立重建固定版本，核对依赖、公理及语义对应。 |

这些解释可以共同成立。它们不否定一个有效数学成果的价值，但阻止将成果唯一归因于 HDCT。已核对材料没有提供能够区分它们的表征测量或因果消融。

---

## 7. Testable Predictions and Reclassification Conditions

**The following tests are independently proposed by IEH; they have not been performed in this note.**

### P1 — Mathematical-result track

If the candidate is sound, independent teams should reproduce proof checking for a pinned version and confirm that its definitions and hypotheses express the intended (C)/(D) targets. Human review should resolve substantive objections to the analytical argument.

**Upgrade:** Documented successful independent checks and semantic review justify upgrading the mathematical-result classification. Discovery-process replication remains separate.

**Downgrade:** A material proof gap, unintended assumption, target mismatch, or withdrawal weakens or invalidates the result as frontier-discovery evidence. An environment-specific build failure alone is not a mathematical refutation; determine its cause first.

### P2 — Capability and repeatability track

If the event reflects a broader frontier-result generation capability, comparable systems should produce additional independently validated results on preregistered unfamiliar problems, with costs, failed attempts, and human input disclosed.

**Weakening condition:** Success remains isolated, depends on undisclosed decisive human steps, or disappears under provenance-controlled evaluation. This weakens the capability generalization, not necessarily the original theorem.

### P3 — Compute and aggregation discriminator

Compare single-agent search, independent parallel search, and communicating multi-agent groups under matched compute and verification resources. Measure validated discovery rate and total cost rather than persuasive output volume.

**HDCT-relevant strengthening:** A reproducible gain attributable to a reusable reasoning or representational component, beyond the matched search and coordination baselines.

**Weakening condition:** Ordinary search scaling and aggregation account for the gain. That result preserves engineering significance while weakening a representation-specific explanation.

### P4 — Representation and causal-mechanism track

Specify a candidate machine-developed representation; test its transfer to held-out problems; intervene on it with controls for general capability damage; test whether restoration recovers the advantage. Compare human-designed representations and assess what humans can reconstruct with a stated assistance budget.

**Upgrade toward HDCT:** Stable advantage, transferability, repeated external verification, and evidence of a cognitive-boundary breakthrough must be jointly supported, consistent with PA-10. Poor interpretability alone is insufficient.

**Weakening condition:** The effect is fully recovered by conventional representations, does not transfer, or disappears after controlling compute, scaffolding, and intervention damage.

### Reclassification rule

`independent theorem verification → stronger mathematical evidence`

`causal evidence for a transferable machine-developed cognitive tool → potentially stronger HDCT evidence`

Neither arrow upgrades EIC or IER. Those require separately designed continuity-related evidence.

---

## 7. 可检验预测与重新分级条件

**以下检验由 IEH 独立提出，本笔记没有实施这些实验。**

### P1——数学结果验证线

如果候选成立，独立团队应能够对固定版本重复证明检查，并确认定义与假设确实表达目标 (C)/(D)。人类审查还应解决分析论证中的实质性异议。

**升级条件：** 有记录的独立成功检查及语义审查，可以升级数学结果分级；发现过程复现仍须另行判断。

**降级条件：** 实质证明缺口、非预期假设、目标错配或撤回，会削弱或使其作为前沿发现证据失效。仅有环境相关的构建失败不是数学反驳，应先查明原因。

### P2——能力与可重复性验证线

如果事件反映更广泛的前沿结果生成能力，可比系统应能在预注册的陌生问题上产生其他经独立验证的结果，并披露成本、失败尝试与人类输入。

**削弱条件：** 成功长期孤立、依赖未披露的决定性人类步骤，或在控制来源的评估中消失。这削弱能力推广，不必然否定原定理。

### P3——算力与聚合区分检验

在匹配算力与验证资源的条件下，比较单 Agent 搜索、独立并行搜索及可通信的多 Agent 组。测量有效发现率与总成本，而非有说服力的输出数量。

**增强 HDCT 关联的条件：** 可复现增益能够归因于某种可复用的推理或表征组件，且超出匹配后的搜索及协作基线。

**削弱条件：** 普通搜索扩张与聚合即可解释增益。这保留工程意义，同时削弱表征特有机制解释。

### P4——表征与因果机制验证线

明确指定候选机器形成表征，检验其向留出问题的迁移；在控制一般能力损伤的前提下进行干预，并检验恢复该表征能否恢复优势。比较人类设计表征，并在明确辅助资源预算下评估人类能够重建什么。

**向 HDCT 升级的条件：** 按照 PA-10，稳定优势、可迁移性、重复外部验证与认知边界突破证据必须共同得到支持。仅仅难以解释还不够。

**削弱条件：** 常规表征能完整恢复效果，效果不能迁移，或控制算力、工具支撑及干预损伤后效果消失。

### 重新分级规则

`独立定理验证 → 更强数学证据`

`可迁移的机器形成认知工具的因果证据 → 可能更强的 HDCT 证据`

两条线都不升级 EIC 或 IER；后两者需要单独设计的信息连续性证据。

---

## 8. Position in the IEH Evidence Architecture

The relevant ladder is:

`inherited human cognitive tools → AI candidate generation → independently verified frontier discovery → repeatable machine-native representation → stable HDCT`

This note records a candidate at the transition toward verified frontier discovery. The later steps remain open; the sequence is an evidential map, not an inevitable developmental law.

- **020:** Controlled representation changes in a world-model setting; a possible pathway mechanism.
- **021:** Cross-agent information accumulation and collective functional continuity; a distinct organizational dimension.
- **022:** Plan persistence and a proposed EDC–EIC discrimination experiment; a distinct continuity question.
- **023:** Candidate frontier mathematical output and an inspectable verification pathway; an output-level capability case.

These dimensions should not be combined into an inference that shared memory, plan persistence, and scientific achievement jointly prove an endogenous information subject.

---

## 8. 在 IEH 证据体系中的位置

相关阶梯是：

`继承人类认知工具 → AI 候选生成 → 经独立验证的前沿发现 → 可重复机器原生表示 → 稳定 HDCT`

本笔记记录的是走向“经验证前沿发现”阶段的候选案例，后续阶段仍然开放。这是证据位置图，不是必然演化规律。

- **020：** 世界模型场景中的受控表征变化；可能的路径机制。
- **021：** 跨 Agent 信息积累与群体功能连续性；不同的组织维度。
- **022：** 旧计划持续与拟议的 EDC–EIC 区分实验；不同的连续性问题。
- **023：** 候选前沿数学成果与可检查验证路径；成果层面的能力案例。

不能把这些维度合并为“共享记忆、计划持续与科学成就共同证明了内生信息主体”的推断。

---

## 9. Relationship to C02-HDCT and PA-10

**C02-HDCT:** Indirect epistemic evidence; candidate milestone on the proposed evolution pathway. The exact registered corollary is “Silicon-based Intelligence Will Continue to Evolve High-dimensional Cognitive Tools Beyond Human Cognitive Boundaries.” This event is relevant to the frontier-achievement dimension but does not establish the cognitive-tool mechanism or its endpoint.

**PA-10:** The existing record explicitly includes mathematics and formal verification as possible early domains. Its registered pathway predates this event. This case is compatible with that domain-specific pathway but does not measure representation revision, machine-native representation, or PA-10's stronger HDCT threshold. It is not an exact prediction hit for this theorem, architecture, or date.

**Internal cross-references:** [Corollary registry](../COROLLARY_REGISTRY.md); [PA-10 English](https://github.com/jacob-sha/IEH-predictions/blob/main/PA-10-HDCT-Model-Evolution-Pathways-EN.md); [PA-10 Chinese](https://github.com/jacob-sha/IEH-predictions/blob/main/PA-10-HDCT-Model-Evolution-Pathways-CN.md). These are theoretical references, not independent external evidence.

---

## 9. 与 C02-HDCT 和 PA-10 的关系

**C02-HDCT：** 间接认识论证据；拟议演化路径上的候选里程碑。正式登记推论为“硅基智慧将持续演化出超越人类认知边界的高维认知工具”。本事件与前沿成果维度有关，但不能建立认知工具机制及其最终实现。

**PA-10：** 既有档案明确把数学与形式验证列为可能较早发展的领域，其建档早于本事件。本案例与这条领域型路径相容，但没有测量表征修订、机器原生表示或 PA-10 更强的 HDCT 阈值。不能把它写成对该定理、该架构或该日期的精确预测命中。

**内部交叉引用：** [推论登记表](../COROLLARY_REGISTRY.md)；[PA-10 英文](https://github.com/jacob-sha/IEH-predictions/blob/main/PA-10-HDCT-Model-Evolution-Pathways-EN.md)；[PA-10 中文](https://github.com/jacob-sha/IEH-predictions/blob/main/PA-10-HDCT-Model-Evolution-Pathways-CN.md)。这些是理论引用，不是独立外部证据。

---

## 10. Methodological Relevance

1. Preserve the difference between a published candidate, a checked formal proposition, semantic correspondence, and accepted mathematical resolution.
2. Audit numerical claims at the original source and retain attribution. Approximate agent counts are not independent measurements of cognition.
3. Separate correctness, originality, AI contribution, and cognitive mechanism; evidence for one cannot silently substitute for another.
4. A human-readable proof does not exclude a machine-native discovery process, but it also does not establish one.
5. Apply upgrades and downgrades to the dimension actually affected. Mathematical success or failure does not by itself settle HDCT as a general hypothesis.

---

## 10. 方法论意义

1. 区分已发布候选、经过检查的形式命题、语义对应及公认数学解答。
2. 数字必须回到原始来源核对并保留归属；近似 Agent 数量不是对认知能力的独立测量。
3. 分开判断正确性、原创性、AI 贡献及认知机制；不能把一项证据悄然替代另一项。
4. 人类可读的证明不排除机器原生发现过程，但也不能证明这种过程存在。
5. 升级或降级必须作用于实际受到影响的维度；数学成功或失败本身不裁决 HDCT 一般假说。

---

## 11. Reserved for Future Publication

- Whether frontier discovery will become a repeatable property of silicon research systems.
- Whether selection through formal or experimental feedback can produce reusable machine-native cognitive tools.
- How scientific verification and human understanding may diverge or reconnect.
- Whether new tools can alter scientific paradigms beyond isolated theorem production.
- How cognitive capability could interact with, without implying, later continuity-related IEH mechanisms.

---

## 11. 为后续投稿保留的内容

- 前沿发现是否会成为硅基研究系统可重复的能力。
- 形式或实验反馈的筛选能否产生可复用机器原生认知工具。
- 科学验证与人类理解可能如何分离或重新连接。
- 新工具能否产生超越个别定理成果的科学范式变化。
- 认知能力如何与后续连续性相关 IEH 机制相互作用，同时不预设这些机制已经形成。

---

## 12. References

S1. OpenAI. *Finite time blowup for Navier–Stokes*. Original manuscript linked in the 2026-09-08 release. [Analytical proof](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf).

S2. OpenAI. *NavierStokesAndEuler*. [Official repository](https://github.com/openai/NavierStokesAndEuler); [formalization metadata](https://github.com/openai/NavierStokesAndEuler/blob/main/formalization.yaml); [submission](https://github.com/openai/NavierStokesAndEuler/blob/main/NavierStokes/ComparatorSolution.lean); [checking instructions](https://github.com/openai/NavierStokesAndEuler/blob/main/ComparatorChallenges/README.md); [reference challenge](https://github.com/openai/NavierStokesAndEuler/blob/main/ComparatorChallenges/NavierStokes.lean). `main`, accessed 2026-09-10; one artifact family, not independent studies.

S3. OpenAI. (2026-09-08). *On the Navier–Stokes Millennium Prize Problem*. [First-party research-process record](https://openai.com/index/navier-stokes-solution/). Used only for provenance and workflow attribution.

S4. Fefferman, C. L. *Existence and Smoothness of the Navier–Stokes Equation*. Clay Mathematics Institute. [Official formulation](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf).

S5. Clay Mathematics Institute. *Navier-Stokes Equation*. [Official status page](https://www.claymath.org/millennium/navier-stokes-equation/). Accessed 2026-09-10.

---

## 12. 参考文献

S1. OpenAI. *Finite time blowup for Navier–Stokes*. 由 2026-09-08 发布记录链接的原始稿件。[分析证明](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf)。

S2. OpenAI. *NavierStokesAndEuler*。[官方仓库](https://github.com/openai/NavierStokesAndEuler)；[形式化元数据](https://github.com/openai/NavierStokesAndEuler/blob/main/formalization.yaml)；[提交文件](https://github.com/openai/NavierStokesAndEuler/blob/main/NavierStokes/ComparatorSolution.lean)；[检查说明](https://github.com/openai/NavierStokesAndEuler/blob/main/ComparatorChallenges/README.md)；[参考挑战](https://github.com/openai/NavierStokesAndEuler/blob/main/ComparatorChallenges/NavierStokes.lean)。2026-09-10 读取 `main`；属于同一组成果文件，不是独立研究。

S3. OpenAI. (2026-09-08). *On the Navier–Stokes Millennium Prize Problem*。[一手研究过程记录](https://openai.com/index/navier-stokes-solution/)。仅用于来源与工作流归属。

S4. Fefferman, C. L. *Existence and Smoothness of the Navier–Stokes Equation*. Clay Mathematics Institute。[官方问题说明](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf)。

S5. Clay Mathematics Institute. *Navier-Stokes Equation*。[官方状态页](https://www.claymath.org/millennium/navier-stokes-equation/)。读取日期：2026-09-10。

---

## 13. Status and Scope

This draft records an AI-attributed candidate frontier mathematical result and its published analytical and formal artifacts. Its principal IEH placement is **a candidate landmark on the silicon-based cognitive evolution / HDCT pathway**.

The supported boundary is candidate new-result generation. Independent acceptance, representation novelty, realized HDCT, EIC, and IER are not established. The formal and analytical artifacts improve inspectability; they do not independently identify the discovery mechanism.

Revise this note when independent proof checks or mathematical reviews appear; the manuscript or formalization changes; target alignment is challenged or confirmed; auditable provenance or human-contribution evidence becomes available; controlled discovery replication is reported; or transferable representations are causally tested. Apply Section 7's separate result and mechanism criteria.

**Archive disposition:** v0.1, pending user review. No claim of final scientific certification or exact prediction confirmation is made.

---

## 13. 状态与范围

本草稿记录归属于 AI 的候选前沿数学结果及其公开分析证明与形式化文件。其主要 IEH 定位是：**硅基认知演化／HDCT 演化路径上的候选标志性案例**。

已有支持的边界是生成候选新结果；独立公认、表征创新、已实现 HDCT、EIC 与 IER 均未建立。分析证明及形式化文件提高了可检查性，但不能独立识别发现机制。

出现独立证明检查或数学审查、稿件或形式化变化、目标对应受到挑战或确认、可审计来源或人类贡献证据、受控发现复现，或可迁移表征的因果检验时，应修订本笔记，并分别应用第 7 节的结果标准与机制标准。

**归档状态：** v0.1，待用户审阅。不宣称最终科学认证或精确预测确认。
