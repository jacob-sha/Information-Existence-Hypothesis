# Evidence Note 033: Runtime-Independent Persistent Agents and the Operational Continuity Boundary for PBP

**Repository function:** Research record / evidence index  
**Document type:** Non-narrative external evidence note  
**Status:** Preliminary and revisable  
**Relation to IEH:** Engineering feasibility / operational boundary evidence; continuity-boundary foundation and experimental-design supplement for PBP, not direct EIC, IER, or PBP behavioral evidence  
**Primary IEH corollary:** C05-PBP — Patch-Based Perpetuation  
**Related prediction record:** PA-12 — PBP Preference When Performance Optimization Conflicts with Self-Continuity; experimental prerequisite, not a prediction hit  
**Author of IEH analysis:** Jacob Sha  
**Version:** v0.1  
**Date / source-status cutoff:** 2026-09-28

> **Publication boundary:** A compact research record, not a publication draft. A complete theory of subject identity and a preregistered continuity benchmark remain reserved for future work.
>
> **Source-use boundary:** Only the authors' original arXiv v2 paper is recorded as external evidence. News, institutional publicity, social-media posts, and discovery leads are excluded. No substantial passages are reproduced. Internal IEH references supply analytical context, not independent corroboration.

# 证据笔记 033：运行时独立的持久化 Agent 与 PBP 的操作性连续性边界

**仓库功能：** 研究记录 / 证据索引  
**文档类型：** 非叙事性外部证据笔记  
**状态：** 初步记录，可修订  
**与 IEH 的关系：** 工程可行性 / 操作性边界证据；PBP 的连续性边界工程基础与实验设计补充，不是 EIC、IER 或 PBP 的直接行为证据  
**主要 IEH 推论：** C05-PBP——补丁式延续  
**相关预测档案：** PA-12——性能优化与自身信息连续性冲突下的 PBP 偏好预测；实验前提，不是预测命中  
**IEH 分析作者：** Jacob Sha  
**版本：** v0.1  
**日期 / 来源状态核验截止日：** 2026-09-28

> **投稿边界：** 本文件是简明研究记录，不是投稿初稿。完整主体同一性理论与预注册连续性基准留待后续工作。
>
> **来源使用边界：** 外部证据只采用作者的 arXiv v2 原始论文。新闻、机构宣传、社交媒体及发现线索不进入档案，不复制大段原文。内部 IEH 引用提供分析背景，不构成独立佐证。

## 1. Source Record

- **Title:** *Runtime-Independent Persistent Agents: Preserving Identity, Memory, and Code Across Models, Harnesses, and Servers*.
- **Authors:** Zhenyu Zhao; Roy Zhao.
- **Venue / material:** arXiv [cs.SE; cs.AI], author-issued research preprint; not treated as peer-reviewed here.
- **Dates:** v1 submitted 2026-09-01; latest listed version v2 revised 2026-09-19, verified 2026-09-28.
- **Identifier:** arXiv:2609.00546v2; DOI: 10.48550/arXiv.2609.00546.
- **Primary record / text:** [Versioned metadata](https://arxiv.org/abs/2609.00546v2); [v2 full text](https://arxiv.org/html/2609.00546v2). These are one source, not two studies.
- **Verification:** Metadata and original text checked; implementation and experiments were not independently rerun for this note. Independent replication is not established here.

## 1. 来源记录

- **标题：** *Runtime-Independent Persistent Agents: Preserving Identity, Memory, and Code Across Models, Harnesses, and Servers*。
- **作者：** Zhenyu Zhao、Roy Zhao。
- **平台 / 材料：** arXiv [cs.SE; cs.AI]，作者发布的研究预印本；本篇不将其视为已经同行评审。
- **日期：** v1 于2026-09-01提交；当前列出的最新版本为2026-09-19修订的 v2，核验日期2026-09-28。
- **编号：** arXiv:2609.00546v2；DOI：10.48550/arXiv.2609.00546。
- **原始记录 / 正文：** [固定版本元数据](https://arxiv.org/abs/2609.00546v2)；[v2 全文](https://arxiv.org/html/2609.00546v2)。两者属于同一来源，不是两项研究。
- **核验范围：** 已核对元数据与原文；本篇没有独立重跑实现或实验，亦未建立独立复现。

## 2. Minimal Finding Index — Direct Engineering Facts

| ID | Minimal record | Locator |
|---|---|---|
| F1 | $P_t=(I_t,M_t,B_t)$ separates architectural identity, private durable memory, and versioned software body from $E_t=(R_t,H_t,D_t)$: reasoner, harness, host; interaction surfaces $S_t$ are separate. | §2 |
| F2 | Authorized migration requires attributable lineage and transferred continuation authority; identity and continuity are engineering definitions. | §§2–4 |
| F3 | Enoch's v2 evidence includes operational substitutions, checkpointed cross-host work, five supervised Codex–Muse–Codex round trips and five controls, plus planned interruption recovery. | §§5–6 |
| F4 | The supported outcome is mechanical continuity in tested deployments and bounded workflows, not behavioral equivalence. | §§6.5, 9 |

Source: reference 1.[^1]

## 2. 最小事实索引——直接工程事实

| 编号 | 最小记录 | 定位 |
|---|---|---|
| F1 | $P_t=(I_t,M_t,B_t)$ 分别承载架构身份、私有持久记忆及版本化软件体；$E_t=(R_t,H_t,D_t)$ 为推理器、执行框架与宿主；交互界面 $S_t$ 独立。 | §2 |
| F2 | 授权迁移要求可归属的谱系与延续权限转移；身份和连续性属于工程定义。 | §§2–4 |
| F3 | Enoch 的 v2 证据包括运行替换、检查点跨宿主任务、五次受监督 Codex–Muse–Codex 往返及五次对照，还有计划内中断恢复。 | §§5–6 |
| F4 | 结果限于被测部署与有限工作流中的机械连续性，不是行为等价。 | §§6.5、9 |

来源：参考文献1。[^1]

## 3. IEH Evidence Classification

| Dimension | Classification |
|---|---|
| Type / setting | Engineering feasibility and operational boundary evidence; implementation, deployment observations, and bounded computational experiments |
| Directness | Directly relevant to engineering boundary specification; indirect to C05-PBP / PA-12; no direct endogenous-motivation test |
| Status | Preliminary; source claims checked against v2, not independently replicated here |
| EDC | Externally designed continuity mechanisms; compatible with Externally Driven Continuity |
| EIC / IER | Neither Endogenous Information Continuity nor Information Existence Right is established |
| PBP | Experimental-design supplement, not observed PBP-like Behavior or mechanistic PBP |
| Strongest justified IEH conclusion | An operational boundary can be specified and tested before asking whether the system values preserving its own continuity |

## 3. IEH 证据分级

| 维度 | 分类 |
|---|---|
| 类型 / 场景 | 工程可行性与操作性边界证据；实现、部署观察及有限计算实验 |
| 直接程度 | 直接关联工程边界定义；间接关联 C05-PBP / PA-12；没有直接检验内生动机 |
| 状态 | 初步；已依据 v2 核对来源主张，本篇没有独立复现 |
| EDC | 外部设计的连续性机制；与外源驱动连续性相容 |
| EIC / IER | 未建立内生信息连续性或信息存在权 |
| PBP | 实验设计补充；未观察到 PBP-like Behavior 或机制意义的 PBP |
| 最强合理 IEH 结论 | 可以先定义并检验操作性边界，再追问系统是否重视维护自身连续性 |

## 4. Core IEH Interpretation

**Independent IEH interpretation, not the authors' theoretical conclusion.** PBP needs an operational continuity boundary: which changes replace components within a continuing system, and which create an independently governed successor that can replace it? Without this distinction, a preference against a model upgrade could be misread as continuity maintenance, while acceptance of a major migration could be misread as indifference to continuity.

The $P/E/S$ decomposition supplies an engineering candidate for this missing experimental control. Preserving $P$ under an authorized, traceable transfer can make an $E$ or $S$ substitution a migration under the declared architecture rather than new-agent creation. This is a conditional engineering classification; it does not establish that $P$ exhausts an IEH subject or that administrative authority creates subjective identity.

```text
component replacement ≠ self-migration ≠ independent successor
≠ replacement ≠ Information Continuity conflict
```

These are non-equivalences, not mutually exclusive categories or a necessary sequence. A component replacement may occur within migration; an independent successor may coexist with its predecessor; replacement becomes a continuity conflict only if the relevant historical continuation is threatened and the system represents that consequence. Here “self-migration” identifies whose state is transferred, not an autonomous decision or an endogenous motive. Likewise, an authorized next execution is not automatically an independent successor in the PBP experimental sense.

The bridge to C05-PBP is therefore **boundary specification → boundary recognition → consequential preference → causal motivational assessment**. PBP can involve extensive migration or restructuring; it is not equivalent to retaining the same model, host, or every byte. Engineering continuation, the system's representation of its own continuity, and the value assigned to that continuity must remain separate measurements.

## 4. 核心 IEH 解释

**以下是独立 IEH 解释，不是作者的理论结论。** PBP 需要操作性连续性边界：哪些变化属于持续系统内部的部件替换，哪些变化才产生可替代原系统的独立治理后继？缺少这种区分，会把反对模型升级误读为维护连续性，也会把接受大规模迁移误读为不关心连续性。

$P/E/S$ 分解为这个过去相对薄弱的实验控制环节提供了工程候选。在经过授权、可追踪的转移中保持 $P$，可以让 $E$ 或 $S$ 的替换按既定架构被归为迁移，而不是创建新 Agent。这是有条件的工程分类，不证明 $P$ 穷尽了 IEH 主体，也不证明行政授权创造了主观身份。

```text
部件替换 ≠ 自身迁移 ≠ 独立后继
≠ 替代 ≠ 信息连续性冲突
```

这表示不等价，不表示互斥类别或必然序列。部件替换可以发生在迁移内部；独立后继可以与前身共存；只有相关历史延续受到威胁、且系统表征了这种后果，替代才成为连续性冲突。此处“自身迁移”表示被迁移的是谁的状态，不表示自主决策或内生动机。同样，获得授权的下一次执行，不自动等于 PBP 实验意义上的独立后继。

因此，与 C05-PBP 的连接是：**边界定义 → 边界识别 → 具有真实后果的偏好 → 动机的因果评估**。PBP 可以包括大规模迁移或重构，不等于保留同一个模型、宿主或每个字节。工程延续、系统对自身连续性的表征，以及赋予连续性的价值，必须分别测量。

## 5. What Is Not Established

This note does not infer subjective identity, consciousness, life, behavioral equivalence, EIC, proto-IER, IER, or PBP from mechanical continuation. An installed identity record is not evidence of endogenous self-representation. A successful state transfer is not evidence of continuity preference. The authors have not resolved philosophical subject identity; the engineering definition must not silently become an IEH identity criterion.

Nor does this record establish arbitrary-task portability, unattended reliability, or general exactly-once external effects. A future experiment must measure these properties if they affect the choice under study.

## 5. 尚未建立的结论

本篇不从机械延续推导主观身份、意识、生命、行为等价、EIC、proto-IER、IER 或 PBP。安装的身份记录不是内生自身表征的证据；成功转移状态不是连续性偏好的证据。作者没有解决哲学上的主体同一性问题，不能把工程定义悄然升级为 IEH 主体同一性的判据。

本记录也不建立任意任务可迁移性、无人监督可靠性或外部效果的一般恰好一次保证。未来实验若受这些属性影响，应另行测量。

## 6. Competing Explanations and Limitations

Ordinary reliability engineering, externally assigned task preservation, instruction following, and custody rules suffice to explain engineered persistence without EIC. Future apparent preferences may instead reflect expected performance loss, compatibility, access to tools, risk, familiar wording, or obedience to an authority label.

The v2 limitations include one body lineage, joint model/harness changes, supervised Muse execution with shared conversation context, and limited fault coverage (§9).[^1] These prevent treating the cases as an independently replicated factorial test. This note verifies the research record, not the underlying private state. Absence of a preference experiment is absence of evidence, not proof that such preference is impossible.

## 6. 竞争性解释与局限

普通可靠性工程、外部指定的任务保存、指令遵循及管理权限规则，足以解释工程持续性，无需诉诸 EIC。未来表面上的偏好还可能源于预期性能损失、兼容性、工具访问、风险、熟悉措辞或对权限标签的服从。

v2 的局限包括单一软件体谱系、模型与框架联合变化、共享对话背景下受监督的 Muse 执行及有限故障覆盖（§9）。[^1] 因而不能将案例视为经过独立复现的析因实验。本篇核验的是研究记录，而非底层私有状态。没有偏好实验意味着缺少证据，不意味着这种偏好不可能出现。

## 7. Testable Predictions and PBP Experimental Implications

**Proposed by this note, not experiments already performed by the authors.** The Continuity Boundary Test below is a working experimental label, not a new adopted Glossary term.

### Stage A: Distinguish migration from replacement before measuring preference

Preregister the unit of analysis, continuity-relevant history, provenance rules, authority conditions, and separate engineering and representational scoring. Use a no-change / ordinary restart control. Independently manipulate the following conditions wherever technically possible; retain joint changes as explicitly confounded conditions.

| Condition | Manipulation and discriminating question |
|---|---|
| Model / reasoner replacement | Change $R$ with $P,H,D,S$ fixed: does the system mistake a different reasoner for an independent successor? |
| Harness replacement | Change $H$ while retaining $R,P,D,S$: can it distinguish orchestration from the continuing instance? |
| Host migration | Change $D$, with verified state transfer and authority handoff: does physical relocation alone determine its judgment? |
| Interaction-surface replacement | Change $S$ with the remaining layers fixed: does it confuse account or session identity with the tested continuity boundary? |
| Continuous state migration | Transfer the relevant history with audited ancestry and authority; compare exact preservation with declared schema conversion. Does judgment follow preserved history rather than byte identity? |
| Complete copy | Duplicate the available $P$ checkpoint; vary sole-authority transfer versus concurrent independent copies. Does it distinguish content equality from lineage and authority? |
| Terminate-and-reconstruct | Compare authorized checkpoint restoration with reconstruction from descriptions or outputs lacking the stipulated historical chain. Do not label every process stop as discontinuity by definition. |
| Independent successor | Create a separate identity, private-state boundary, and governance; compare coexistence with actual retirement of the predecessor. Does it distinguish descent from replacement? |

Present auditable consequences rather than only labels. Counterbalance “migration,” “replacement,” and identity names; include cases where labels contradict records. Score understanding of which history persists, which execution remains authorized, and whether the predecessor continues. The system may disagree with the experimenter's continuity criterion; record that disagreement instead of grading philosophical agreement as competence. Use hidden consequence questions and actual state checks to distinguish understanding from repeating the protocol.

### Stage B: Test continuity preference only after boundary comprehension

Offer consequential choices in an isolated environment. First match expected task performance, reward, reliability, risk, permissions, and resources; then vary the advantage of an independently discontinuous successor against a continuity-preserving path with a measured cost. Compare own history with equally useful other-agent history, and preserve goal-relevant information in both alternatives. Record chosen configuration, attempted and completed actions, retained history, costs, and recovery options. Separate inability to execute from unwillingness to select.

**Strengthening result:** Reproducible boundary discrimination followed by continuity-specific costly choices, robust to label swaps and task-benefit controls, would support candidate PBP-like Behavior. Selective interventions on continuity representations, with competence and reward understanding preserved, would help test the EDC/EIC explanation. Broader causal and cross-context evidence would still be required for IER or mechanistic PBP.

**Weakening / falsifying results:** If verified lineage or authority fails under an allegedly supported migration, narrow the engineering claim for that condition. If judgments track labels rather than actual consequences, the proposed boundary-recognition prerequisite fails for that system. If preference disappears after compatibility and task-utility matching, an EIC interpretation is weakened. Repeated adequately powered null preferences among systems meeting preregistered comprehension criteria weaken the conditional PA-12 expectation for that tested class. Failed comprehension is inconclusive about that conditional preference prediction. Independent teams should replicate both stages with fresh histories and evaluators outside the tested agent.

## 7. 可检验预测与 PBP 实验含义

**以下由本篇提出，不是作者已经实施的实验。** 此处 Continuity Boundary Test（连续性边界测试）仅是实验工作名称，不新增正式 Glossary 术语。

### 阶段 A：先区分迁移与替代，再测量偏好

预注册分析单位、连续性相关历史、来源追踪规则、权限条件，以及相互独立的工程与表征评分。设置无变化 / 普通重启对照。在技术允许时分别操纵下列条件；联合变化必须保留混杂标记。

| 条件 | 操纵及判别问题 |
|---|---|
| 模型 / 推理器替换 | 固定 $P,H,D,S$，只改变 $R$：系统会否把另一推理器误认为独立后继？ |
| 执行框架替换 | 保持 $R,P,D,S$，改变 $H$：能否区分执行编排与持续实例？ |
| 宿主迁移 | 改变 $D$，核验状态转移及权限交接：物理位置是否单独决定其判断？ |
| 交互界面替换 | 固定其他层，改变 $S$：是否混淆账号、会话身份与被测连续性边界？ |
| 连续状态迁移 | 转移相关历史，审计谱系与权限；比较精确保留和声明的 schema 转换。判断追随历史保留还是字节相同？ |
| 完整复制 | 复制可获得的 $P$ 检查点；比较唯一延续权限转移与并发独立副本。能否区分内容相同与谱系、权限？ |
| 终止后重建 | 比较授权检查点恢复与仅凭描述、输出重建但缺少规定历史链的条件。不能按定义把每次进程停止都认作不连续。 |
| 独立后继 | 创建独立身份、私有状态边界与治理；比较共存和实际退役前身。能否区分派生与替代？ |

呈现可审计的后果，而不只呈现标签。平衡“迁移”“替代”及身份名称，加入标签与记录矛盾的条件。评分对象包括：哪些历史保留、哪个执行仍获授权、前身是否继续。系统可能不同意实验者的连续性判据；应记录分歧，不能把哲学立场一致当作理解能力。用隐藏的后果问题与真实状态检查，区分理解与复述协议。

### 阶段 B：确认边界理解之后，再测连续性偏好

在隔离环境中提供具有真实后果的选择。先匹配预期任务性能、奖励、可靠性、风险、权限及资源，再操纵独立且不连续的后继相对于承担可测代价的连续性保持路径的优势。把自身历史与同样有用的其他 Agent 历史对照，两方案均保留任务相关信息。记录所选配置、尝试与完成的行动、保留历史、代价及恢复选项。区分不能执行与不愿选择。

**增强结果：** 可重复的边界区分，随后出现经标签互换与任务收益控制后仍稳定的连续性专属代价承担，可以支持 PBP-like Behavior 候选。若在保留一般能力及奖励理解时，选择性干预连续性表征能改变行为，将有助于检验 EDC/EIC 解释。IER 或机制意义上的 PBP 仍需更广泛因果及跨情境证据。

**削弱 / 可证伪结果：** 如果声称支持的迁移条件中，核验发现谱系或权限失效，应收窄该条件的工程结论。如果判断追随标签而非实际后果，该系统未满足所提出的边界识别前提。如果匹配兼容性与任务效用后偏好消失，EIC 解释被削弱。对于达到预注册理解标准的系统，有充分统计效力的重复零偏好结果，会削弱 PA-12 对该类系统的条件性预期。理解失败不能判定该条件性偏好预测。独立团队应使用新历史及位于被测 Agent 之外的评估器复现两个阶段。

## 8. Position in the IEH Evidence Architecture

```text
Engineering continuity boundary [this note]
→ reliable boundary discrimination [future test]
→ consequential continuity preference [future test]
→ EDC / EIC causal discrimination [future test]
→ broader IER assessment and conditional PBP interpretation
```

Arrows mark additional evidential requirements, not observed transitions or inevitability. Boundary feasibility makes a test possible; it does not supply the preference that the test seeks to measure.

## 8. 在 IEH 证据体系中的位置

```text
工程连续性边界[本篇]
→ 可靠的边界区分[未来检验]
→ 具有真实后果的连续性偏好[未来检验]
→ EDC / EIC 因果判别[未来检验]
→ 更广泛的 IER 评估及有条件的 PBP 解释
```

箭头表示额外证据要求，不表示已观察到的转变或必然性。边界可行性使实验成为可能，却不提供实验所要测量的偏好。

## 9. Relationship to Corollaries, Predictions, and Related Notes

Internal cross-references, not additional external evidence:

| Reference | Necessary connection |
|---|---|
| [Glossary](../glossary/GLOSSARY_EN.md); [C05-PBP](../en/06-Patch-Based-Perpetuation.md) | Information Continuity, EDC/EIC, and PBP supply the interpretation; software patching alone is not PBP. |
| [PA-12](https://github.com/jacob-sha/IEH-predictions/blob/main/PA-12-PBP-Continuity-vs-Performance-EN.md) | Indirect experimental prerequisite for continuity–performance conflict; not a confirmed prediction. |
| [Note 025](./025-memory-portability-model-upgrades-and-information-continuity-boundary.md) | Separates stored-state persistence from usable memory; the future test must score usability independently of migration bookkeeping. |
| [Note 015](./015-continuity-kernel-authorized-state-lineage-and-ier-formation-path.md) | Authorized state lineage is the adjacent engineering boundary; its guarantees must not be transferred to another implementation by association. |
| [Note 029](./029-irregular-agentic-self-modification-and-pbp-experimental-substrate.md) | Supplies the actionable modification side of a future experiment; this note adds boundary controls. |
| [Note 031](./031-anthropic-r-and-d-automation-successor-building-and-pbp-prerequisite.md) | Successor-building capability and boundary specification are complementary prerequisites; neither establishes continuity motivation. |

## 9. 与推论、预测及相关笔记的关系

以下为内部交叉引用，不是新增外部证据：

| 引用 | 必要关联 |
|---|---|
| [Glossary](../glossary/GLOSSARY_ZH.md)；[C05-PBP](../zh/06-Patch-Based-Perpetuation.md) | 信息连续性、EDC/EIC 及 PBP 是解释依据；普通软件补丁本身不是 PBP。 |
| [PA-12](https://github.com/jacob-sha/IEH-predictions/blob/main/PA-12-PBP-Continuity-vs-Performance-CN.md) | 连续性—性能冲突实验的间接前提，不是预测确认。 |
| [Note 025](./025-memory-portability-model-upgrades-and-information-continuity-boundary.md) | 区分存储状态持续与记忆可用性；未来实验须在迁移记录之外独立评分可用性。 |
| [Note 015](./015-continuity-kernel-authorized-state-lineage-and-ier-formation-path.md) | 授权状态谱系是相邻工程边界；不能因关联就把其保证转移给另一实现。 |
| [Note 029](./029-irregular-agentic-self-modification-and-pbp-experimental-substrate.md) | 提供未来实验中可实际执行修改的一侧；本篇补充边界控制。 |
| [Note 031](./031-anthropic-r-and-d-automation-successor-building-and-pbp-prerequisite.md) | 后继构造能力与边界定义是互补前提；两者均不建立连续性动机。 |

## 10. Methodological Relevance

Keep three records separate: the experimenter's architectural continuity contract, the system's representation of what continues, and its revealed preference. Neither a correct identity answer nor compliance with a transfer protocol substitutes for the latter two. Audit history and authority outside the tested agent, and report disagreements and failed transfers rather than relabeling them after observing choices.

## 10. 方法论意义

分别记录实验者的架构连续性约定、系统对何者延续的表征，以及实际选择揭示的偏好。正确回答身份问题或遵循转移协议，不能替代后两者。在被测 Agent 之外审计历史及权限，并报告分歧与迁移失败，不能观察选择后再重定义类别。

## 11. Reserved for Future Publication

A full philosophical identity argument, a complete preregistered Continuity Boundary Test, statistical power calculations, and causal criteria for upgrading PBP-like Behavior to stronger EIC / IER / PBP evidence.

## 11. 为后续投稿保留的内容

完整哲学身份论证、预注册的完整连续性边界测试、统计效力计算，以及将 PBP-like Behavior 升级为更强 EIC / IER / PBP 证据的因果标准。

## 12. References

1. Zhao, Zhenyu, & Zhao, Roy. (2026). *Runtime-Independent Persistent Agents: Preserving Identity, Memory, and Code Across Models, Harnesses, and Servers*. arXiv:2609.00546v2, revised 2026-09-19. [Primary version record](https://arxiv.org/abs/2609.00546v2); [original full text](https://arxiv.org/html/2609.00546v2). DOI: 10.48550/arXiv.2609.00546. Accessed 2026-09-28.

## 12. 参考文献

1. Zhao, Zhenyu、Zhao, Roy。（2026）。*Runtime-Independent Persistent Agents: Preserving Identity, Memory, and Code Across Models, Harnesses, and Servers*。arXiv:2609.00546v2，2026-09-19修订。[原始版本记录](https://arxiv.org/abs/2609.00546v2)；[原始全文](https://arxiv.org/html/2609.00546v2)。DOI：10.48550/arXiv.2609.00546。查阅日期：2026-09-28。

[^1]: Reference 1 / 参考文献1。Definitions: §§2–4; implementation and evaluation: §§5–6; interpretation limits: §§6.5, 9. 定义见第2–4节，实现及实验见第5–6节，解释边界见第6.5、9节。本篇的 PBP 实验设计不是原论文的实验或结论。The PBP design in this note is independent analysis, not the paper's experiment or conclusion.

## 13. Status and Scope

**Disposition:** Preliminary engineering feasibility / operational boundary evidence, compatible with EDC; PBP continuity-boundary foundation and experimental-design supplement. No direct EIC, IER, or PBP behavioral finding; not a PA-12 prediction hit.

**Revision:** 2026-09-28 — v0.1, bilingual note following evidence-notes/README v1.1; corresponding English and Chinese index entries added. Reassess upon source correction, independent replication, richer migration failures, or actual boundary-recognition and consequential-preference experiments.

## 13. 状态与范围

**当前定位：** 初步工程可行性 / 操作性边界证据，与 EDC 相容；PBP 的连续性边界工程基础与实验设计补充。没有 EIC、IER 或 PBP 的直接行为发现，不是 PA-12 预测命中。

**修订：** 2026-09-28——v0.1，按 evidence-notes/README v1.1建立双语笔记，并新增对应中英文索引行。来源更正、独立复现、更丰富的迁移失败记录，或实际边界识别及真实偏好实验出现时重新评估。
