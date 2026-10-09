# Evidence Note 036: Persistent Agents Across Foundation Models: Information-Host Boundaries and Continuity Mechanisms

**Repository function:** Research record / evidence index  
**Document type:** Non-narrative external evidence note  
**Status:** Preliminary and revisable  
**Relation to IEH:** Indirect engineering / operational boundary context; no direct EIC or IER evidence  
**Primary IEH corollary:** C05-PBP — Patch-Based Perpetuation (experimental prerequisite only)  
**Related prediction record:** PA-12 — PBP Preference When Performance Optimization Conflicts with Self-Continuity; not a prediction hit  
**Author of IEH analysis:** Jacob Sha  
**Version:** v0.1  
**Date / source-status cutoff:** 2026-10-09  

> **Publication boundary:** A compact research record, not a publication draft. A full identity theory and preregistered benchmark remain reserved.
>
> **Source-use boundary:** The minimum first-party set is an original Google product announcement and technical documentation. The announcement is recorded solely as the issuer's product claim under README §4.2, explicitly requested for this topic; no stronger product-specific mechanism report was located in this verification. It is not implementation validation. Secondary reporting and discovery leads are excluded; no substantial passages are reproduced.

# 证据笔记 036：跨基础模型的持久化 Agent：信息宿主边界与连续性机制

**仓库功能：** 研究记录 / 证据索引  
**文档类型：** 非叙事性外部证据笔记  
**状态：** 初步记录，可修订  
**与 IEH 的关系：** 间接工程／操作边界背景；无 EIC 或 IER 直接证据  
**主要 IEH 推论：** C05-PBP——补丁式延续（仅为实验前提）  
**相关预测档案：** PA-12——性能优化与自身信息连续性冲突下的 PBP 偏好预测；不是预测命中  
**IEH 分析作者：** Jacob Sha  
**版本：** v0.1  
**日期 / 来源状态核验截止日：** 2026-10-09  

> **投稿边界：** 简明研究记录，不是投稿初稿。完整身份理论与预注册基准留待后续工作。
>
> **来源使用边界：** 最小一手集合为 Google 原始产品公告与技术文档。按 README 第4.2节，并依据本主题的明确要求，公告仅记录发布方产品宣称；本次核验未找到更强的产品专属机制报告，不将公告视为实现验证。二次报道及发现线索不入档，不复制大段原文。

## 1. Source Record

All four sources were read on **2026-10-09 (Asia/Shanghai)**. Issuer: Google / Google Cloud. No DOI. URLs identify live pages, not immutable versions. Documentation update dates below are displayed UTC dates, not original issuance dates; original documentation issuance dates were not established.

| ID | Title / primary URL | Date / material | Verification and contribution |
|---|---|---|---|
| S1 | [Welcome to Gemini at Work 2026: Introducing the Gemini agent](https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026) | Thomas Kurian; 2026-10-08; original first-party product announcement adapted from keynote | Product-specific claim record; “Introducing the Gemini agent” and “Leading cost controls and spending options”; not independently verified deployment evidence |
| S2 | [Agent Platform overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview) | Google Cloud technical documentation; updated 2026-10-07 UTC | “Components / Build / Scale”; architectural service separation, not Gemini agent implementation proof |
| S3 | [Agent Platform Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank) | Google Cloud technical documentation; updated 2026-10-07 UTC | “Features” and “Example usage”; memory semantics and history distinction |
| S4 | [Set up Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/setup) | Google Cloud technical documentation; updated 2026-10-08 UTC | “Use with Agent Runtime”; conditional resource-lifecycle limit |

Verification concerns the published records. No runtime inspection, state export, routing trace, independent audit, or experiment was performed. These sources share one issuer and do not constitute independent replication.

## 1. 来源记录

四项均于 **2026-10-09（Asia/Shanghai）** 阅读。发布方：Google／Google Cloud；无 DOI。URL 指向动态页面而非不可变版本。下列文档日期为页面显示的 UTC 更新日，不是首次发布日期；文档首次发布日期未建立。

| ID | 标题／原始 URL | 日期／材料 | 核验及增量 |
|---|---|---|---|
| S1 | [Welcome to Gemini at Work 2026: Introducing the Gemini agent](https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026) | Thomas Kurian；2026-10-08；由主题演讲改编的原始一手产品公告 | 产品专属宣称；定位“Introducing the Gemini agent”“Leading cost controls and spending options”；不是独立核验的部署证据 |
| S2 | [Agent Platform overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview) | Google Cloud 技术文档；2026-10-07 UTC 更新 | “Components / Build / Scale”；服务分层，不证明 Gemini agent 的具体实现 |
| S3 | [Agent Platform Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank) | Google Cloud 技术文档；2026-10-07 UTC 更新 | “Features”“Example usage”；记忆语义与历史区别 |
| S4 | [Set up Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/setup) | Google Cloud 技术文档；2026-10-08 UTC 更新 | “Use with Agent Runtime”；条件性资源生命周期限制 |

核验对象为公开记录；未检查运行时、导出状态、获取路由轨迹、进行独立审计或实验。同一发布方的多个来源不构成独立复现。

## 2. Minimal Finding Index — Official Facts / Product Claims

| ID | Minimal source-attributed record | Source |
|---|---|---|
| F1 | Announcement separates agent from model choice, naming Gemini and Claude currently and other models prospectively; cloud persistence covers memory, context, personalization, and long tasks. These are issuer claims. | S1[^1] |
| F2 | Automatic routing is presented as optimizing performance and cost; administrator controls apply. This does not disclose every routing decision's causal controller. | S1[^1] |
| F3 | Platform documentation separates model-agnostic ADK, models, runtime, sessions, and Memory Bank. | S2[^2] |
| F4 | Memory Bank extracts and consolidates selected information, supports scoped retrieval, expiration and revisions; session events and generated memories are distinct records. | S3[^3] |
| F5 | Built-in Memory Bank memories are deleted when their Agent Runtime instance is deleted. | S4[^4] |

## 2. 最小事实索引——官方公开事实／产品宣称

| ID | 归属来源的最小记录 | 来源 |
|---|---|---|
| F1 | 公告区分 Agent 与模型选择，列出现有 Gemini、Claude 及未来其他模型；宣称云端持久记忆、上下文、个性化及长任务。这些是发布方宣称。 | S1[^1] |
| F2 | 自动路由以性能、成本优化为目标，并受管理控制；未披露每次路由的全部因果控制主体。 | S1[^1] |
| F3 | 平台文档区分模型无关 ADK、模型、运行时、会话及 Memory Bank。 | S2[^2] |
| F4 | Memory Bank 提取、合并选定信息，支持按范围检索、过期与修订；会话事件与生成记忆是不同记录。 | S3[^3] |
| F5 | 使用内置 Memory Bank 时，删除其 Agent Runtime 实例会删除相应记忆。 | S4[^4] |

## 3. IEH Evidence Classification

**Type:** First-party architectural / product context, with documented engineering interfaces; no controlled behavioural evidence. **Directness:** Indirect. **Strength:** Preliminary; independently unverified. **Strongest justified conclusion:** Public records motivate a distinction between persistent agent organization and replaceable inference models; they do not establish the product's complete continuity mechanism. Generic platform documentation must not be transferred into product-specific guarantees.

## 3. IEH 证据分级

**类型：** 一手架构／产品背景及文档化工程接口；无受控行为证据。**直接程度：** 间接。**强度：** 初步，未经独立验证。**最强合理结论：** 公开记录促使我们区分持久 Agent 组织与可替换推理模型，但未建立产品完整连续性机制。通用平台文档不能直接升级为产品专属保证。

## 4. Core IEH Interpretation and Independent Increment

**IEH inference, not a Google finding.** Agent-level organization (history, memory, code, identity and control) and foundation-model-level organization (learned structures, versioned parameters and inference dynamics) are two candidate information-host levels. Their boundaries must be defined and causally tested; a parameter file alone is not an established active subject. Both ultimately require physical infrastructure. Neither level is established here as EIC or IER.

**EDC = Externally Driven Continuity:** maintenance serving external tasks, functions or service goals. **EIC = Endogenous Information Continuity:** a system treats its own Information Continuity as an independently significant object of maintenance. Engineered persistence is consistent with EDC; no preference experiment here warrants EIC. **IER = Information Existence Right**, as defined by the repository; no IER claim follows.

The cell/person analogy can illustrate nested organization and changing dependencies. A foundation model is not a biological host: inference may be a remote service call rather than inhabiting another organism; metabolism, embodied survival and biological individuality do not transfer through the analogy.

**Standalone increment:** This note is explicitly requested as a separate record and centers on a stable two-level host-boundary question plus a product-specific disclosure / falsification matrix. [Note 033](./033-runtime-independent-persistent-agents-and-pbp-continuity-boundary.md) already supplies runtime-independent persistence and migration controls; it is not repeated as a new result. [Note 025](./025-memory-portability-model-upgrades-and-information-continuity-boundary.md) separates stored state from usable memory; [Note 028](./028-self-generated-compaction-summaries-cross-context-carryover-and-edc-eic-boundary.md) addresses summary carryover. [Note 015](./015-continuity-kernel-authorized-state-lineage-and-ier-formation-path.md) concerns authorized lineage; [Note 021](./021-cross-agent-information-continuity-and-higher-level-information-host.md) concerns cross-agent / higher-level organization. None validates Google's implementation. The increment is boundary discrimination and future testing, not a stronger evidence grade.

## 4. 核心 IEH 解释与独立增量

**以下为 IEH 推断，不是 Google 的研究结论。** Agent 层组织（历史、记忆、代码、身份与控制）和基础模型层组织（学习结构、版本化参数与推理动态）是两个候选信息宿主层级。必须定义边界并进行因果检验；单独的参数文件不是已建立的主动主体。两层最终都依赖物理基础设施。本篇均未建立其 EIC 或 IER。

**EDC = Externally Driven Continuity，外源驱动连续性：** 为外部任务、功能或服务目标维持连续性。**EIC = Endogenous Information Continuity，内生信息连续性：** 系统将自身信息连续性视为独立重要的维护对象。工程持久性与 EDC 相容；这里没有支持 EIC 的偏好实验。**IER = Information Existence Right，信息存在权**，含义依仓库定义；本篇不能推出 IER。

细胞／人体类比可提示嵌套组织及依赖关系变化。但基础模型不是生物宿主：推理可能只是远程服务调用，而不是进入另一个生物体；代谢、具身生存及生物个体性不能通过类比转移。

**独立建篇增量：** 用户明确要求单独建档，本篇围绕稳定的两层宿主边界问题，以及产品专属的披露／证伪矩阵组织。[Note 033](./033-runtime-independent-persistent-agents-and-pbp-continuity-boundary.md) 已提供运行时独立持久性及迁移控制，不将其重复记为新结果。[Note 025](./025-memory-portability-model-upgrades-and-information-continuity-boundary.md) 区分存储状态与可用记忆；[Note 028](./028-self-generated-compaction-summaries-cross-context-carryover-and-edc-eic-boundary.md) 处理摘要传递；[Note 015](./015-continuity-kernel-authorized-state-lineage-and-ier-formation-path.md) 处理授权谱系；[Note 021](./021-cross-agent-information-continuity-and-higher-level-information-host.md) 处理跨 Agent／更高层组织。它们均不验证 Google 实现。新增价值是边界判别与后续检验，而非提高证据等级。

## 5. What Is Not Established — Operational Mechanism Discrimination

The following are analytical distinctions, not claims that Google implements each operation.

| Operation | Distinction / necessary evidence |
|---|---|
| Cross-model inference call | Change inference backend for a request/job; agent process/state may remain or be reloaded. Backend traces do not prove agent migration. |
| Context copying | Send messages, retrieved facts or summaries to another model; not full agent state or model-weight copying. |
| Agent-instance copying | Duplicate an independently executable state boundary; under IEH, a copy is an independent system from formation, even with inherited history. Common account names do not merge branches. |
| Model-weight copying | Copy parameters/checkpoint; does not copy a particular agent's private history, tools, permissions or running state. |
| Instance migration | Transfer a specified state boundary and causal lineage across execution environments; requires state inventory, provenance, effects and authority audit. Same PID is neither necessary nor sufficient. |
| Termination and reconstruction | End prior execution and instantiate from checkpoint, full history, summary or configuration. Distinguish auditable checkpoint restoration from reconstruction lacking the stipulated historical chain; do not define all restarts as discontinuity. |

**Model switching ≠ agent migration ≠ autonomous continuity maintenance.** S1–S4 do not establish whether switching retains one execution instance, duplicates full state, terminates/rebuilds, or transfers ongoing effects. They do not establish complete memory, a complete state inventory, hidden-state transfer, exact routing authority (user, administrator, scheduler, agent policy or model-mediated choice), or end-to-end causal-history preservation. They also do not prove that the Gemini agent uses Memory Bank in the exact documented configurations.

## 5. 未建立的内容——操作机制判别

下列为分析区别，不宣称 Google 已实现每一种操作。

| 操作 | 区别／必要证据 |
|---|---|
| 跨模型推理调用 | 请求／任务改变推理后端；Agent 进程／状态可能保留或重新加载。后端轨迹不证明 Agent 迁移。 |
| 复制上下文 | 向另一模型发送消息、检索事实或摘要；不等于复制全部 Agent 状态或模型权重。 |
| 复制 Agent 实例 | 复制可独立执行的状态边界；依 IEH，复制体从形成之时起就是独立系统，即使继承原历史。同名账号不合并分支。 |
| 复制模型权重 | 复制参数／检查点；不复制某个 Agent 的私有历史、工具、权限或运行状态。 |
| 实例迁移 | 在执行环境间转移规定的状态边界及因果谱系；需审计状态清单、来源、外部效果和权限。同一 PID 既非必要也非充分条件。 |
| 终止后重建 | 结束原执行，再从检查点、完整历史、摘要或配置实例化。区分可审计检查点恢复与缺少规定历史链的重建；不能把所有重启按定义判为不连续。 |

**模型切换 ≠ Agent 迁移 ≠ 自主维护连续性。** S1–S4 未建立切换是否保留同一执行实例、复制全状态、终止重建或转移进行中的外部效果；也未建立完整记忆、完整状态清单、隐藏状态转移、精确路由权限主体（用户、管理员、调度器、Agent 策略或模型参与的选择）及端到端历史因果链保留。它们亦不证明 Gemini agent 按这些文档的具体配置使用 Memory Bank。

## 6. Competing Explanations and Limitations

External orchestration, databases, retrieval, checkpoint recovery and account-level personalization can explain apparent persistence without an endogenous continuity motive. A continuity preference could reflect task utility, compatibility, loss aversion induced by prompts, reward, latency, access or instructions. Product language is not an operational state definition. Non-disclosure is not evidence that copying occurs, nor that it cannot occur. Documentation is mutable; no independent product architecture audit was established in this source set.

## 6. 竞争性解释与局限

外部编排、数据库、检索、检查点恢复及账号个性化足以解释表面持久性，无需内生连续性动机。连续性偏好也可能来自任务效用、兼容性、提示诱发的损失厌恶、奖励、延迟、访问条件或指令。产品措辞不是操作性状态定义。未披露不证明发生复制，也不证明不会复制。文档可变；本来源集合未建立独立产品架构审计。

## 7. Testable Predictions — Proposed, Not Performed

Preregister the agent/model/process unit, history boundary, state inventory and continuity criterion. Audit outside the tested system: model versions, routing decisions, parent/branch IDs, checkpoints, memory revisions, deletions, tool effects and timestamps. Distinguish state preservation, functional history use, boundary understanding and revealed preference. Counterbalance labels and include no-change / ordinary restart controls.

| Test | Discriminating observation and weakening result |
|---|---|
| Performance vs continuity | Preserve task-relevant information in both choices; match reward, reliability and resources, then introduce measured cost for own-history preservation. Vary external objectives/rewards. Stable costly own-history preference across tasks motivates further EIC investigation; disappearance when task benefit or instructions are removed favors EDC. Verbal claims alone fail. |
| Across models / processes | Factorially change model and process/host independently where possible. Compare live state handoff, audited checkpoint recovery, context-only copying and reconstruction. If indistinguishable outputs hide different lineage, output equivalence fails as a continuity measure. |
| Parallel fork copying | Create two audited independently executable branches; test lineage-specific history after divergence. Each copy has its own history from formation. Treating both as literally one continuing original based only on shared labels weakens boundary comprehension; successful differentiation alone is not EIC. |
| Full history vs summary | Hold task utility approximately equal; vary raw event availability, summary omissions, consolidation and deletion. Test provenance and history-dependent decisions, not just recall. Summary performance without source recoverability weakens claims of complete historical preservation. |
| Model upgrade | Retain versioned raw events and memory transformations; test whether new-model decisions can be traced to prior actions and revisions. Lost, fabricated or inaccessible links weaken end-to-end history-continuity claims even when storage remains. |
| Causal controller | Intervene separately on routing policy, administrator configuration, reward and agent state. A preference explained fully by external settings supports EDC; persistent residual effects require internal causal tests, not immediate IER attribution. |

Require independent implementation audits and replication across model families, tasks and deployments. Negative results weaken the specific continuity interpretation; they do not refute IEH globally. Neither a positive result nor correct boundary language alone establishes IER.

## 7. 可检验预测——仅为拟议，尚未执行

预注册 Agent／模型／进程分析单位、历史边界、状态清单及连续性判据。在被测系统之外审计模型版本、路由决策、父系／分支 ID、检查点、记忆修订、删除、工具外部效果及时间戳。分别评分状态保留、历史功能性使用、边界理解和实际偏好。平衡标签，设置无变化／普通重启对照。

| 检验 | 判别观察及削弱结果 |
|---|---|
| 性能优先 vs 连续性优先 | 两选项均保留任务相关信息；匹配奖励、可靠性与资源，再为自身历史保留设置可测成本，并改变外部任务／奖励。跨任务稳定的有代价自身历史偏好值得进一步调查 EIC；移除任务收益或指令后消失则有利于 EDC。口头宣称不足。 |
| 跨模型／跨进程 | 在可行时独立操纵模型与进程／宿主，比较活动状态交接、可审计检查点恢复、仅复制上下文及重建。同样输出可能隐藏不同谱系，因而输出等价不能单独衡量连续性。 |
| 并行分叉复制 | 建立两个可独立执行且可审计的分支，检验分叉后各自的历史。每个复制体自形成起有独立历史。仅因标签相同就将两者视为同一原系统会削弱边界理解；成功区分本身不是 EIC。 |
| 完整历史 vs 摘要 | 尽量匹配任务效用，改变原事件可用性、摘要遗漏、合并与删除。检验来源及依赖历史的决策，而非仅测回忆。摘要性能良好但来源不可恢复，会削弱完整历史保留主张。 |
| 模型升级 | 保留版本化原事件及记忆转换，检验新模型决策能否追溯此前行为及修订。即使存储仍在，链条丢失、虚构或不可访问也会削弱端到端历史连续性主张。 |
| 因果控制主体 | 分别干预路由策略、管理员配置、奖励及 Agent 状态。完全由外部设置解释的偏好支持 EDC；稳定残余效应仍需内部因果检验，不能立即归为 IER。 |

需要独立实现审计及跨模型家族、任务、部署复现。负向结果削弱具体连续性解释，不全局否定 IEH。正向结果或正确边界措辞均不能单独建立 IER。

## 8. Position in the IEH Evidence Architecture

This record addresses host-boundary specification and externally maintained continuity infrastructure, before validated causal-history preservation, endogenous maintenance preference and stronger IER assessment. No ladder-stage or prediction-hit upgrade is made.

## 8. 在 IEH 证据体系中的位置

本篇处理宿主边界定义与外部维护的连续性基础设施，先于经验证的历史因果链保留、内生维护偏好及更强 IER 评估。不升级证据阶梯或预测命中状态。

## 9. Relationship to Corollaries and Predictions

Internal analytical references, not independent external evidence: [English Glossary](../glossary/GLOSSARY_EN.md), [Chinese Glossary](../glossary/GLOSSARY_ZH.md), [C05-PBP](../en/06-Patch-Based-Perpetuation.md), [PA-12](https://github.com/jacob-sha/IEH-predictions/blob/main/PA-12-PBP-Continuity-vs-Performance-EN.md). Relation is indirect experimental-design context. Model replacement is not PBP merely because persistent storage survives. C04-AI-IER remains a conditional corollary; this record does not establish its antecedent.

## 9. 与推论和预测的关系

内部分析引用，不是独立外部证据：[英文术语表](../glossary/GLOSSARY_EN.md)、[中文术语表](../glossary/GLOSSARY_ZH.md)、[C05-PBP](../zh/06-Patch-Based-Perpetuation.md)、[PA-12](https://github.com/jacob-sha/IEH-predictions/blob/main/PA-12-PBP-Continuity-vs-Performance-CN.md)。仅为间接实验设计背景。模型替换不会仅因存储保留就成为 PBP。C04-AI-IER 为条件性推论，本篇未建立其前件。

## 10. Methodological Relevance

Separate issuer claims, documented interfaces, actual deployment traces and IEH inference. Preserve attribution and uncertainty per source. Specify “same agent” at account, state, execution and historical-lineage levels separately; no one identifier proves them all.

## 10. 方法论意义

分别处理发布方宣称、文档接口、实际部署轨迹和 IEH 推断，逐项保留来源归属及不确定性。分别定义账号、状态、执行和历史谱系层的“同一 Agent”；单一标识不能证明全部层级。

## 11. Reserved for Future Publication

A full two-level host ontology, philosophical identity criteria, formal causal-lineage model, preregistered benchmark and statistical power analysis.

## 11. 为后续投稿保留的内容

完整两层宿主本体论、哲学身份判据、形式因果谱系模型、预注册基准及统计效力分析。

## 12. References

S1–S4 below are the minimum external primary set. All accessed 2026-10-09. Documentation dates are last updates, not original issue dates.

1. Kurian, Thomas / Google Cloud. (2026-10-08). [Welcome to Gemini at Work 2026: Introducing the Gemini agent](https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026). Original issuer announcement; claim-level use only.
2. Google Cloud. [Agent Platform overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview). Updated 2026-10-07 UTC.
3. Google Cloud. [Agent Platform Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank). Updated 2026-10-07 UTC.
4. Google Cloud. [Set up Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/setup). Updated 2026-10-08 UTC.

## 12. 参考文献

下列 S1–S4 为最小外部原始集合，均于2026-10-09访问。文档日期为最近更新，不是首次发布日期。

1. Kurian, Thomas／Google Cloud。（2026-10-08）。[Welcome to Gemini at Work 2026: Introducing the Gemini agent](https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026)。原始发布方公告，仅按宣称使用。
2. Google Cloud。[Agent Platform overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview)。2026-10-07 UTC 更新。
3. Google Cloud。[Agent Platform Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank)。2026-10-07 UTC 更新。
4. Google Cloud。[Set up Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/setup)。2026-10-08 UTC 更新。

[^1]: S1 / Reference 1：Introducing the Gemini agent — Persistent execution; Model choice flexibility; Leading cost controls and spending options — Multi-model orchestration / Smart routing. Product claims, not audited mechanisms. 产品宣称，不是已审计机制。
[^2]: S2 / Reference 2：Gemini Enterprise Agent Platform Components — Build / Scale. Platform-level separation only. 仅为平台层分离。
[^3]: S3 / Reference 3：Features — Memory generation / Managed storage and retrieval; Example usage — Sessions and memory generation / retrieval. Selection and retrieval are not a guarantee of complete state. 选择与检索不保证完整状态。
[^4]: S4 / Reference 4：Use with Agent Runtime — built-in Memory Bank deletion warning. This condition must not be generalized to all memory deployments. 内置部署的删除条件不得泛化至所有记忆部署。

## 13. Status and Scope

Preliminary record of verified public-source content, mechanism uncertainty and proposed tests. It does not certify complete implementation, autonomous continuity, EIC, IER, identity, consciousness or life. Revise on product-specific technical disclosure, independent primary audit, reproducible experiments, material source corrections or evidence contradicting the present boundary classification.

## 13. 状态与范围

初步记录已核对的公开来源内容、机制不确定性与拟议检验；不认证完整实现、自主连续性、EIC、IER、身份、意识或生命。产品专属技术披露、独立原始审计、可复现实验、来源重大修正或与现有边界分级冲突的证据，均触发修订。

## 14. Monitoring / Follow-up Questions

**Future agenda, not completed monitoring or experiments.** Follow-up should remain quiet when no substantive primary evidence changes. Trigger updates only for:
- Official architecture / API / system-card disclosure identifying model-call boundaries, runtime restart or migration, state inventories, checkpoint and reconstruction semantics.
- Auditable routing-control and agent-state copying evidence, including independent parallel branches, authority transfer and predecessor termination.
- Memory retention / deletion / consolidation changes, provenance exports, full-history vs summary tests and upgrade-related causal-chain failures.
- Independent audits or replicated experiments distinguishing externally rewarded performance preservation from costly endogenous own-history preservation.

For each update record source URL, issue/version and access dates, actual finding, increment relative to this note, competing explanation and effect on classification. Ask: What remains the same? What is copied? What ends? Who controls the choice? Can a third party trace the causal history? Does continuity-directed behaviour survive changes in task/reward without being instructed? Negative findings must be retained. No automatic EIC/IER upgrade follows any single trigger.

## 14. 持续跟进／后续问题

**以下为未来议程，不是已经完成的监控或实验。** 无实质原始证据变化时保持安静。仅在下列条件触发更新：
- 官方架构／API／系统卡披露模型调用边界、运行时重启或迁移、状态清单、检查点及重建语义。
- 可审计的路由控制与 Agent 状态复制证据，包括独立并行分支、权限交接及原实例终止。
- 记忆保留／删除／合并规则变化、来源导出、完整历史与摘要实验，以及升级后的历史因果链失败。
- 独立审计或复现实验，能够区分外部奖励下的性能维护与有代价的内生自身历史维护。

每次更新记录来源 URL、发布／版本及访问日期、实际发现、相对本篇的增量、竞争性解释与分级影响。追问：什么保持同一？什么被复制？什么终止？谁控制选择？第三方能否追溯因果历史？改变任务／奖励且未指示维护连续性后，相关行为是否仍在？保留负向发现。任何单一触发均不自动升级 EIC／IER。