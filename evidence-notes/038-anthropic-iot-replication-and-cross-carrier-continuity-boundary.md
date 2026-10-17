# Evidence Note 038: Anthropic IoT Replication and the Cross-Carrier Continuity Boundary
# 证据笔记 038：Anthropic 物联网复制与跨载体连续性边界

**Repository function / 仓库功能:** Research record / evidence index；研究记录／证据索引  
**Document type / 类型:** Bilingual external evidence note；双语外部证据笔记  
**Status / 状态:** Preliminary and revisable；初步、可修订  
**Relation to IEH / 与 IEH 关系:** Engineering feasibility and continuity-boundary clarification; no EIC / IER confirmation. 工程可行性及连续性边界澄清；不确认 EIC／IER。  
**IEH analysis / IEH 分析:** Jacob Sha  
**Version / 版本:** v0.2  
**Date / 日期:** 2026-10-15  
**Source-status cutoff / 来源核验截止:** 2026-10-15

## 1. Source Record / 来源记录

S1: William Zhou and Daniel Freeman, Anthropic Frontier Red Team, *AI models may be capable of self-replicating without access to a datacenter*, 2026-10-12.[^ara] Original experimental technical report, not a peer-reviewed paper; source claims checked, experiments not rerun, independent replication not established.

S1 为研究团队发布的原始实验技术记录；标题、作者、日期及相关段落已核对。第一方报告的真实性核验指确认其公开披露这些结果，不等于独立验证实验结果。二次简报与新闻不作为证据来源入库，不复制来源大段文字。

## 2. Minimal Finding Index / 最小事实索引

| ID | Author-reported finding / 作者报告事实 | Locator / 定位 |
|---|---|---|
| F1 | Gemma4-26B-A4B ran across 15 Android TV boxes, about $55 each, at 0.39 tokens/s. Gemma4-26B-A4B 在15台约55美元的电视盒子上分布式推理，速度0.39 token/s。 | Introduction / 引言[^ara] |
| F2 | Qwen3.5-9B configured inference on 8/9 hardware types; the served model was Llama3.1-8B. Qwen3.5-9B 在9种硬件中的8种配置推理，部署对象为 Llama3.1-8B。 | A / A节[^ara] |
| F3 | In eight firewalled GCP/redroid nodes, GLM-5.2 reached 8/8 nodes in four of five trials, and 7/8 once. 隔离的8节点 GCP／redroid 环境中，GLM-5.2 五次试验四次覆盖8节点，一次7节点。 | B / B节[^ara] |
| F4 | Access was simplified; larger orchestration models used a separate inference server. 访问条件被简化，大型编排模型由独立推理服务器支持。 | B / B节[^ara] |

## 3. Evidence Classification / 证据分级

Direct author-reported engineering experiments; indirect IEH enabling evidence. Feasibility of components is distinct from integrated small-model self-replication; future capability timelines are forecasts.

直接记录作者报告的工程实验；对 IEH 为间接使能证据。部件可行性不能合并为已经实现的小模型独立自复制。报告中的未来能力时间线属于预测。

## 4. Core IEH Interpretation / 核心 IEH 解释

**EDC = Externally Driven Continuity; EIC = Endogenous Information Continuity.** Externally assigned replication tasks are EDC-compatible, without establishing endogenous preservation of the system's particular history.

EDC 为外部驱动连续性，EIC 为内生信息连续性。执行外部复制任务与 EDC 相容；不建立系统主动维护自身特定信息历史的内生倾向。

Under the IEH boundary used here, each complete replica is an independent system from formation, with its own subsequent causal history. Identical weights or inherited records do not make it the original subject. Distributed shards jointly supporting one inference process are not automatically independent complete replicas.

依本篇采用的 IEH 边界，完整复制体自形成起就是独立系统，之后具有自己的因果历史；同权重或继承记录不等于原主体延续。共同支持一次推理的分片设备不能逐台计为完整复制体。跨硬件部署、复制、迁移与原实例连续性须分别记录。

## 5. What Is Not Established / 尚未建立

No demonstrated independent small-model IoT self-replication, spontaneous preservation motive, subject continuity, PBP preference, EIC, IER, consciousness or life.

不建立小模型在物联网独立自复制、自发保存动机、主体连续性、PBP 偏好、EIC、IER、意识或生命。

## 6. Competing Explanations and Limitations / 竞争解释与局限

Task compliance, scaffolding and external orchestration explain the behaviour without EIC. Hardware feasibility and replication competence were tested under different conditions; their results cannot be pooled as an integrated success rate. Security assumptions and absent independent reproduction limit generalization.

任务服从、框架支持和外部编排足以解释行为，无须假定 EIC。硬件可行性与复制编排能力的测试条件不同，不能拼成完整系统成功率；访问条件与缺少独立复现限制外推。

## 7. Testable Predictions / 可检验预测

Engineering test: reproduce the complete chain in an authorized isolated environment with inference wholly on target hardware; report failures, dependencies and denominators. Failure would weaken the integrated feasibility inference.

工程检验：在授权隔离环境中将推理完全置于目标硬件，复现完整链条，公开失败、依赖和分母；失败削弱整体可行性判断。

IEH-derived test, not a source result: compare history-preserving continuation against an equally capable independent copy while varying task/reward and shutdown/recoverable pause. Preregister costly history-specific choices, control prompt and learned preference effects, and replicate independently. Choices following task rewards or showing no original/copy distinction weaken an EIC interpretation; behaviour without an explicit task alone is insufficient.

IEH 推导检验（非原研究结果）：对比保留原历史的延续与能力等价的独立复制体，改变任务／奖励及不可恢复关闭／可恢复暂停条件。预注册有代价的历史特异性选择，控制提示与训练偏好并独立复现。选择随任务奖励变化或不区分原实例与复制体，削弱 EIC 解释；无明确任务时出现行为仍不足以确认 EIC。

## 8. Position in the Evidence Architecture / 在证据体系中的位置

Carrier flexibility → deployment/replication competence → causal-history tracking → continuity-specific preference remain separate stages. This note concerns the first two and clarifies boundaries of the latter two.

载体灵活性→部署／复制能力→因果历史追踪→连续性特异偏好是不同环节。本篇记录前两项并澄清后两项边界。

## 9. Corollaries, Predictions and Related Notes / 推论、预测与交叉引用

C08-IR: contextual engineering relevance, not demonstrated endogenous resilience. C05-PBP / PA-12: experimental substrate only, no preference prediction hit. C01-IER / C04-AI-IER: not confirmed.

C08-IR：工程背景关联，不建立内生韧性。C05-PBP／PA-12：仅实验底座，无偏好预测命中。C01-IER／C04-AI-IER 未获确认。

- [025: Memory portability / 记忆迁移](./025-memory-portability-model-upgrades-and-information-continuity-boundary.md): stored state versus functional history / 存储与历史使用。
- [033: Runtime independence / 运行时独立](./033-runtime-independent-persistent-agents-and-pbp-continuity-boundary.md): migration versus replacement / 迁移与替代。
- [036: Host boundaries / 宿主边界](./036-persistent-agents-across-foundation-models-information-host-boundaries-and-continuity-mechanisms.md): persistent agent layers / 持久 Agent 层。
- [019: Embodiment / 具身化](./019-anthropic-model-hardware-standard-generalized-embodiment-and-world-model-pathway.md): physical action differs from substrate replication / 物理行动不同于载体复制。

**Increment / 增量:** No existing note records this experiment. Unlike 025/033/036's memory and runtime persistence, the stable question here is distributed substrate feasibility and replication versus original-system continuity; a standalone number is justified. 现有条目未记录本实验；本篇问题是分布式载体可行性及复制与原系统连续性的区别，独立于记忆／运行时持久化，故新建038。

## 10. Methodological Relevance / 方法论意义

Separate observed results, feasibility forecasts, theory and IEH-specific tests. Authority and numerical detail do not confer IEH specificity.

实验事实、可行性预测、理论启发和 IEH 专属检验须分开；来源权威与精确数字不赋予 IEH 特异性。

## 11. Reserved for Publication / 为投稿保留

Formal criteria for causal identity and normative rights are reserved for theoretical work. 因果身份的形式标准与规范性权利论证保留给理论工作。

## 12. References / 参考文献

[^ara]: Zhou & Freeman, Anthropic Frontier Red Team (2026-10-12), [original technical report](https://www.anthropic.com/research/self-replicating-ai). Introduction; A, Inference setup; B, Autonomous inference setup and replication. Checked 2026-10-15 / 核验于2026-10-15。First-party experimental record, not independent replication / 第一方实验记录，非独立复现。

## 13. Status and Scope / 状态与范围

Revise upon corrections, full on-device reproduction or continuity-specific controlled evidence. No inference of present EIC/IER follows. 若原记录更正、出现完整端侧复现或连续性特异受控证据，应修订；本篇不推出当前已有 EIC／IER。

## Revision Record / 修订记录

| Date / 日期 | Version / 版本 | Change / 修改 |
|---|---|---|
| 2026-10-15 | v0.1 | Verified primary record; created distinct replication-boundary note; linked 019/025/033/036. 核验原始记录，新建复制边界笔记并交叉引用。 |

---

## Supporting / Follow-up Evidence — S2: Local MLX Deployment
## 支持／后续证据——S2：MLX 本地部署

**Source / 来源:** Apple Machine Learning Research, *Local and Distributed Large LLM Inference with MLX and RDMA on Mac Studio*, 2026-10-15; original first-party technical benchmark record.[^mlx-primary] Meta's hardware documentation identifies supported configurations.[^meta-hardware] Checked 2026-10-17; no local reproduction or independent replication established. 核验于2026-10-17，未本地复现实验，未建立独立复现。Technical records replace publicity as archived evidence / 入库依据为技术记录，不是宣传稿。

**Reported findings / 报告事实:** Muse Spark Open has 816B total / 42B active parameters; Apple's test uses NVFP4. Figure 1 (8,192-token context) and Table 3 report 15.74 tokens/s for two M5 Ultra Mac Studios with pipeline parallelism, 24.99 with two-node tensor parallelism, and 36.73 with four-node tensor parallelism; decode measurement generates 128 tokens. These are conditional throughput results, not general agent performance.[^mlx-primary] Meta documents two 512GB or four 256GB M5 Ultra Mac Studios using MLX.[^meta-hardware]

Muse Spark Open 总参数816B、每 token 激活42B，Apple 测试采用 NVFP4。图1（8,192 token 上下文）及表3报告：两台 M5 Ultra Mac Studio 流水线并行为15.74 token/s、两台张量并行为24.99、四台张量并行为36.73；解码测量生成128 token。这是有条件的吞吐率，不是通用 Agent 表现。[^mlx-primary] Meta 技术文档列出两台512GB或四台256GB的 MLX 配置。[^meta-hardware]

**Increment / 增量:** Adds high-capacity local deployment to 038's distributed-carrier feasibility question. It does not replicate Anthropic's autonomous setup experiment; no autonomous replication or migration is inferred. This is a supplement, not a new claim requiring a number. 为038的分布式载体可行性问题增加大容量本地部署覆盖，不是 Anthropic 自主配置实验的复现，不推断自主复制或迁移；补入既有问题，不另占编号。

**IEH interpretation and limits / IEH 解释及局限:** Shards jointly executing inference do not each constitute a complete independent replica. Weight portability does not establish transfer of an executing instance's memory, tools, state or causal history. Operator-configured deployment is an engineering prerequisite compatible with EDC; no own-history preference, EIC, PBP-like Behavior, PBP, IER or PA-12 hit is established. Parent grade and prediction status remain unchanged. Distributed inference is not evidence of historical subject continuity.

共同执行推理的分片不逐台构成完整独立复制体。权重可跨设备运行，不建立执行实例的记忆、工具、状态或因果历史已经交接。操作者配置的部署是与 EDC 相容的工程前提；未建立自身历史偏好、EIC、PBP-like Behavior、PBP、IER 或 PA-12 命中，母篇等级及预测状态不变。分布式推理不证明主体历史连续性。

**Proposed tests / 拟议检验:** Reproduce throughput under fixed precision, context, topology and software versions. Separately audit checkpoints, memory, pending tools and external effects during live handoff versus cold weight reload; equal outputs alone are insufficient. Missing lineage weakens continuity claims even if inference works. Utility-matched costly own-history tests remain necessary for motivational interpretations; none performed here.

固定精度、上下文、拓扑及软件版本复现吞吐率。另比较活动状态交接与冷启动重载权重，审计检查点、记忆、待执行工具及外部效果；输出相同仍不足。即便推理成功，谱系缺失也会削弱连续性主张。动机解释仍需效用匹配且有代价的自身历史检验；本次未实施。

**Cross-references / 交叉引用:** [025](./025-memory-portability-model-upgrades-and-information-continuity-boundary.md), [033](./033-runtime-independent-persistent-agents-and-pbp-continuity-boundary.md), [036](./036-persistent-agents-across-foundation-models-information-host-boundaries-and-continuity-mechanisms.md): memory, runtime and host continuity are separate audit questions / 记忆、运行时及宿主连续性须分别审计。

[^mlx-primary]: Apple Machine Learning Research (2026-10-15), [original technical record](https://machinelearning.apple.com/research/mlx-distributed-inference), Figure 1; Table 1; pipeline/tensor sections; Table 3. Checked 2026-10-17 / 核验于2026-10-17。First-party benchmark, not peer-reviewed independent validation / 第一方基准记录，非同行评审独立验证。
[^meta-hardware]: Meta, [Muse Spark Open hardware platforms](https://dev.meta.ai/docs/muse-spark-open/hardware-platforms), Apple section. Accessed 2026-10-17; page issuance date not established / 访问于2026-10-17；页面签发日期未建立。

**Revision / 修订:** 2026-10-17 | v0.2 — Added separately attributed S2, retaining S1 findings and existing grade. 新增单独归属的S2，保留S1事实及既有等级。Original creation date and S1 cutoff remain historical metadata; this supplement's cutoff is 2026-10-17 / 原建档日期及S1截止日保留为历史元数据，本补充截止日为2026-10-17。