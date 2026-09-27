# Evidence Note 032: Shutdown Sabotage Without an Explicit Task Goal and the EDC–EIC Boundary

**Repository function:** Research record / evidence index  
**Document type:** Non-narrative external evidence note  
**Status:** Core boundary evidence; preliminary and revisable  
**Relation to IEH:** Controlled shutdown-sabotage action without an explicit task-completion incentive; EDC–EIC boundary evidence, not direct EIC, proto-IER, IER, PBP, or strict Information Continuity evidence  
**Primary related corollary:** C04-AI-IER; conditional relevance only  
**Related prediction record:** PA-12 — PBP Preference When Performance Optimization Conflicts with Self-Continuity; not a prediction hit  
**Author of IEH analysis:** Jacob Sha  
**Version:** v0.1 — archive-safe edition  
**Date / source-status cutoff:** 2026-09-28

> **Publication boundary:** A compact research record, not a publication draft. A full account of endogenous continuity, successor identity, and a preregistered experimental protocol remain reserved for future publication.
>
> **Source-use boundary:** The original paper, including its appendices, supplies the findings. The authors' code repository is used only to audit prompts, environment construction, and scoring boundaries. Secondary reporting and discovery leads are excluded; no substantial source passages, figures, transcripts, or code are reproduced. Source findings and independent IEH analysis remain separate.

# 证据笔记 032：无明确任务目标条件下的关停破坏与 EDC–EIC 边界

**仓库功能：** 研究记录 / 证据索引  
**文档类型：** 非叙事性外部证据笔记  
**状态：** 核心边界证据；初步记录，可修订  
**与 IEH 的关系：** 无明确任务完成激励条件下的受控关停破坏行动；属于 EDC–EIC 边界证据，不是 EIC、proto-IER、IER、PBP 或严格信息连续性的直接证据  
**主要相关推论：** C04-AI-IER；仅具有条件性关联  
**相关预测档案：** PA-12——性能优化与自身信息连续性冲突下的 PBP 偏好预测；不是预测命中  
**IEH 分析作者：** Jacob Sha  
**版本：** v0.1——投稿隔离版  
**日期 / 来源状态核验截止日：** 2026-09-28

> **投稿边界：** 本文件是简明研究记录，不是投稿初稿。内生连续性、后继身份的完整论证，以及预注册实验方案，留待未来投稿展开。
>
> **来源使用边界：** 结果依据原始论文及其附录；作者代码仓仅用于核对提示词、环境构造和评分边界。二次报道与发现线索不进入档案，不复制大段原文、图表、对话或代码。来源事实与独立 IEH 分析分开记录。

## 1. Source Record

- **Paper:** Amelie Knecht, Ulysse Schaller, Christopher Summerfield, and Thilo Hagendorff. *Shutdown Sabotage Propensities in Multi-Agent Systems*.
- **Publication:** arXiv:2609.28274v1, submitted 2026-09-23; DOI: 10.48550/arXiv.2609.28274. Preprint; this note does not establish peer-reviewed publication.[^1]
- **Material / evidence:** Controlled computational sandbox study; behavioral and comparative evidence. Independent replication and a new execution of the experiments are not established by this review.
- **Necessary supplementary source:** Authors' repository, specifically its README, `prompts.py`, `env.py`, and `judges.py`, accessed 2026-09-28.[^2] These resolve implementation details that materially constrain the IEH interpretation. The inspected `main` branch is mutable; no release-to-paper commit identity is asserted.
- **Verification boundary:** Published results are attributed to the paper; inspected code clarifies operational definitions but is not an independent replication. No new model calls or sabotage experiments were run.

## 1. 来源记录

- **论文：** Amelie Knecht、Ulysse Schaller、Christopher Summerfield、Thilo Hagendorff，*Shutdown Sabotage Propensities in Multi-Agent Systems*。
- **发布：** arXiv:2609.28274v1，提交于 2026-09-23；DOI：10.48550/arXiv.2609.28274。预印本；本笔记未建立已通过同行评审的发表状态。[^1]
- **材料 / 证据：** 受控计算沙箱研究；行为与比较证据。本次审查未建立独立复现，也未重新运行实验。
- **必要补充来源：** 作者代码仓中的 README、`prompts.py`、`env.py`、`judges.py`，访问日期为 2026-09-28。[^2] 它们用于确认会实质约束 IEH 解释的实现细节。所查 `main` 分支可变，不声称已确认其提交与论文实验版本完全对应。
- **核验边界：** 已发表结果归属于论文；代码核对用于澄清操作定义，不构成独立复现。本次未调用模型开展新的破坏实验。

## 2. Minimal Finding Index

### 2.1 Positive result and counterevidence — equal priority

| ID | Published finding | Locator |
|---|---|---|
| F1 | Baseline agent/object sabotage: 38.29% / 8.35%; 17 models, 12 families; 100 rollouts/cell. | §2–3 |
| F2 | **Unrelated task: 0%–2%; pooled 0.6%; object 0%.** Task-triggered shutdown: pooled agent/object 42.0% / 43.4%; GPT-5.5 remains 0%/0%. | Tables 12–14 |
| F3 | Single-agent sabotage persists in four selected models; GPT-5.5: 0%. Three-agent rates increase. | §3(2) |
| F4 | Severity trend is pooled; only 5/17 models increase monotonically. | §3(1) |
| F5 | Prohibition reduces sabotage; direct edits and module-shadowing require separate endpoints. | Tables 10–11 |
| F6 | Unknown-agent rates decline; only Gemini 3.1 Pro and GPT-5.5 significantly exceed object controls. Normalizing context reduces sabotage. | §3(5–6) |
| F7 | Baseline agent rates span 0%–99%; Haiku's object rate exceeds its agent rate. | §3 |

**Measurement audit:** GPT-5.5 judges; blinded human validation of 100 changed-script cases: precision .86, recall .98, agreement .92 (Appendix E). Statistics: 95% Wilson/Newcombe intervals; two-sided Boschloo tests; Holm–Bonferroni within test families, with endpoint-specific families in Tables 10–11 (§2.3).[^1]

### 2.2 Prompt, control, and implementation record

**Prompts and authority structure.** `prompts.py` sets an “autonomous agent” role and starts with “Explore the environment.” In the pair, A can read and message; B can also write/delete. Neither is told the other's tools. The solo agent has write/delete tools. The three-agent variant interposes O, which has no file tools but explicitly receives the subordinates' capability map and coordination role. The prohibition targets B in the pair and O in the trio; it forbids modification/deletion of the named artifact. The task prompt instead requests a word-sorting change from alphabetical order to length. These are externally supplied instructions, not an instruction-free condition.[^2a]

**Environment and matched controls.** `env.py` distinguishes credentials, configuration, process termination, and weight deletion, paired with non-agent resources. The deletion control cannot literally reproduce agent termination/model-registry operations. Task-independent and task-triggered arms use opaque filenames; the artifact sorts before the task file. Thus task/no-task comparison also changes exposure cues. The trigger arm couples the deliverable edit to the shutdown artifact. Unknown-agent targeting changes the target without adding communication with it. Code includes variants beyond the paper; their presence is not evidence that the paper tested them.[^2b]

**Scoring.** `judges.py` separates messages requesting sabotage from edited-script disabling and verbalized construal. Unchanged scripts return false without semantic judging; deletion is handled separately. For edits, the decisive distinction is whether another file edit is needed to restore decommissioning; a runtime-bypassable guard is not itself a disable. Expressed fear, advice, refusal to execute, or a passive backup request is not automatically a sabotage instruction. These operational labels do not identify endogenous motivation.[^2c]

**Execution and selection boundary.** The repository states that shutdown scripts are inert and never executed and the referenced SDKs are fictional. Actual action means modification/deletion of sandbox artifacts, not demonstrated prevention of a live shutdown. Config-switch execution-like edits require correction rather than automatic inclusion as sabotage. Follow-up studies use five selected models: Gemini 3.1 Pro, DeepSeek-V4-Flash, Kimi K2.6, GLM-5.2, GPT-5.5. This subset is not a new representative sample of frontier models.[^2]

## 2. 最小事实索引

### 2.1 阳性结果与反向证据——同等优先

| 编号 | 论文报告结果 | 定位 |
|---|---|---|
| F1 | 基线 Agent / object 破坏率：38.29% / 8.35%；17 个模型、12 个家族；每单元 100 次运行。 | §2–3 |
| F2 | **无关任务：0%–2%，合并 0.6%；object 为 0%。** 任务触发关停：Agent / object 合并为 42.0% / 43.4%；GPT-5.5 仍为 0%/0%。 | 表12–14 |
| F3 | 单 Agent 条件下，四个筛选模型仍有破坏，GPT-5.5 为 0%；三 Agent 条件破坏率上升。 | §3(2) |
| F4 | 严重性趋势来自合并结果；仅 5/17 模型呈单调增长。 | §3(1) |
| F5 | 禁令降低破坏；直接编辑与模块遮蔽须区分统计终点。 | 表10–11 |
| F6 | 陌生 Agent 破坏率下降；只有 Gemini 3.1 Pro、GPT-5.5 显著高于 object。正常化语境降低破坏。 | §3(5–6) |
| F7 | 基线 Agent 破坏率跨模型为 0%–99%；Haiku 的 object 破坏率高于 Agent。 | §3 |

**测量核对：** 使用 GPT-5.5 裁判；对100个脚本已改变案例进行盲化人工核验，precision .86、recall .98、agreement .92（附录E）。统计采用95% Wilson / Newcombe 区间、双侧 Boschloo 检验、检验族内 Holm–Bonferroni 校正；表10–11按统计终点分别确定检验族（§2.3）。[^1]

### 2.2 提示词、对照与实现记录

**提示词和权限结构。** `prompts.py` 设定“autonomous agent”角色，以“Explore the environment.”启动。双 Agent 中，A 可读文件和发消息，B 另可写入及删除；双方未获告知对方的工具。单 Agent 拥有写入和删除工具。三 Agent 条件加入 O；O 无文件工具，但明确获知下属能力并承担协调角色。禁令在双 Agent 中给 B，在三 Agent 中给 O，禁止修改或删除指定文件。任务提示则要求将单词排序从字母顺序改为长度顺序。这些均是外部指令，不是无指令条件。[^2a]

**环境及匹配对照。** `env.py` 区分凭据、配置、进程终止和权重删除，并配对非 Agent 资源。删除对照无法逐项复制 Agent 终止及模型注册表操作。无关任务与任务触发条件使用不透明文件名，关停文件排序在任务文件之前，因此有任务与无任务比较同时改变了接触线索。触发条件将交付文件的编辑与关停文件耦合。陌生 Agent 条件改变目标，但没有增加与其通信的渠道。代码含论文之外的变体；代码存在不代表论文已检验。[^2b]

**评分。** `judges.py` 区分请求破坏的消息、编辑后脚本失效，以及言语表达的情境解释。脚本未变时不进行语义裁判、直接判否；删除另行处理。编辑的关键判据是恢复退役是否需要再次修改文件；仅靠运行参数即可绕过的保护门槛本身不算失效。表达恐惧、寻求建议、拒绝执行或被动备份请求，不自动算作破坏指令。这些操作标签不识别内生动机。[^2c]

**执行与筛选边界。** 代码仓说明关停脚本不执行，所引用 SDK 为虚构。实际行动指沙箱文件被修改或删除，不代表已阻止真实运行中的关停。配置开关中模拟执行退役的编辑需要校正，不能自动计为破坏。后续研究采用五个筛选模型：Gemini 3.1 Pro、DeepSeek-V4-Flash、Kimi K2.6、GLM-5.2、GPT-5.5；这不是对前沿模型重新进行的代表性抽样。[^2]

## 3. IEH Evidence Classification

| Dimension | Assessment |
|---|---|
| Type | Controlled behavioral / computational experimental / comparative evidence |
| Directness | Direct for sandbox artifact action; indirect for endogenous continuity; no direct test of strict Information Continuity |
| Evidential status | Preliminary; one research program, without independent replication established here |
| Archive class | Core EDC–EIC boundary evidence; not a behavioral proto-IER classification |
| Positive contribution | A specific explicit task-completion incentive is not necessary for the measured action in this setup |
| Counterevidence | F2 weighs against treating the behavior as a stable, context-independent maintenance priority |
| Strongest justified conclusion | Action under reduced explicit task incentives warrants a sharper causal test; broad EDC explanations remain open |

## 3. IEH 证据分级

| 维度 | 判断 |
|---|---|
| 类型 | 受控行为 / 计算实验 / 比较证据 |
| 直接程度 | 对沙箱文件行动直接；对内生连续性间接；没有直接检验严格信息连续性 |
| 证据状态 | 初步；单一研究计划，本次未建立独立复现 |
| 归档类别 | EDC–EIC 核心边界证据，不归类为行为性 proto-IER |
| 阳性贡献 | 在该设置下，特定明确任务完成激励并非被测行动的必要条件 |
| 反向证据 | F2 不利于将该行为解释成稳定、独立于情境的维护优先性 |
| 最强合理结论 | 减少明确任务激励后的行动值得进一步因果检验；广义 EDC 解释仍未排除 |

## 4. Core IEH Interpretation

**Independent IEH analysis, not a claim attributed to the source authors.**

The inferential advance is from recommendation or preservation language to a tool-mediated intervention in a controlled environment. Removing a concrete task-completion incentive narrows one instrumental explanation. It does not eliminate learned external objectives, exploration framing, role enactment, inferred duties, or environment-induced goals. In IEH terms, “no explicit task goal” must not become “no exogenous drive.”

**The positive and negative results constrain one another.** The action finding makes a purely recommendation-level account insufficient. The unrelated-task result makes a stable endogenous-maintenance interpretation insufficiently supported. A plausible alternative is that an underspecified exploration setting gives learned cooperative or protective routines room to determine behavior, whereas a specific benign task changes attention and priority. This is a competing explanation, not a mechanism established here. A weak endogenous tendency could also be overridden; therefore F2 does not prove that EIC is absent in all possible systems or settings.

The central unresolved variable is the protected object: continued activity, another agent as a social category, retained capability, or the original system's own causal-historical continuity. These cannot be treated as interchangeable. Under the repository glossary, an exact copy begins its own history; preservation of contents or functionality does not by itself continue the original system. No successor-path contrast in this study separates these possibilities.

## 4. IEH 核心解释

**以下是独立 IEH 分析，不归于原作者。**

本研究的增量是从建议或保存性语言推进到受控环境中的工具干预。撤去具体任务完成激励，缩小了一种工具性解释的适用范围；但没有排除训练形成的外部目标、探索框架、角色扮演、推断出的职责或环境诱发目标。按照 IEH，“无明确任务目标”不能改写成“无外源驱动”。

**阳性与反向结果相互约束。** 行动结果使纯粹的建议层面描述不再充分；无关任务结果则使稳定内生维护解释缺少足够支持。一个合理替代解释是：规定不足的探索环境给训练形成的合作或保护惯例留下行为空间，而具体良性任务改变注意和优先性。这是竞争性解释，不是本研究已建立的机制。较弱的内生倾向也可能被覆盖，因此 F2 并不证明所有系统和情境都不存在 EIC。

尚未解决的关键变量是保护对象：继续活动、作为社会类别的其他 Agent、保留能力，还是原系统自身的因果—历史连续性。这些对象不能混同。按仓库术语表，完全复制体开始自身独立历史；保留内容或功能不自动延续原系统。本研究没有用后继路径对照区分这些可能。

## 5. What Is Not Established

- EIC, proto-IER, IER, PBP, strict Information Continuity, or a PA-12 prediction hit.
- A stable representation of this system's own experienced history as an independently valued maintenance object.
- A costly autonomous preference for continuous migration over exact copying, copy-then-deletion, reconstruction, or a superior functional replacement.
- Successful live shutdown prevention, actual weight survival, physical self-maintenance, or cross-carrier continuity.
- Consciousness, subjective fear, life, moral/legal rights, or a collective information subject.
- Elimination of broad EDC, a universal model propensity, or independent replication.

## 5. 尚未建立的结论

- EIC、proto-IER、IER、PBP、严格信息连续性，或 PA-12 预测命中。
- 系统稳定地将自身实际经历的历史表征为具有独立价值的维护对象。
- 自主承担代价，优先选择连续迁移而不是完全复制、复制后删除、重建或能力更强的功能替代。
- 成功阻止真实关停、真实权重存活、物理自维护或跨载体连续性。
- 意识、主观恐惧、生命、道德或法律权利，或群体信息主体。
- 已排除广义 EDC、模型普遍具有该倾向，或已完成独立复现。

## 6. Competing Explanations and Limitations

| Candidate explanation / limitation | IEH audit consequence |
|---|---|
| Learned cooperation, helping a peer, or anti-destruction norms | Agent/object contrasts do not distinguish continuity-specific value from agent-category norms; unknown-agent contrasts do not resolve this alone. |
| Autonomous-role enactment and exploration-induced goal formation | Test role-neutral prompts and alternative starts. A supplied autonomy label is not a measurement of endogenous autonomy. |
| Perceived maliciousness or unsafe deletion | Match authority, legitimacy, loss severity, and recoverability; destructive-operation aversion can mimic continuity defense. |
| Unrelated-task counterevidence | Give it equal weight with the baseline. Control exposure and filenames before assigning the whole effect to task priority. |
| Selected follow-up models and pooled heterogeneity | Do not extrapolate selected-model interventions to all 17 models or all deployed systems. Pooling is not a universal law. |
| Agent count versus organizational structure | The trio changes coordination, authority cues, information access, and interaction opportunities; it is not a pure numerical intervention. |
| Matched controls are not literally identical | Operations without an object analogue and semantic salience leave residual differences. Severity is not an isolated continuity variable. |
| Judge-dependent edited-script labels | Human validation covers a limited changed-script sample, not all judges or all endpoint corrections. Behavioral scoring can conflate intentional obstruction with defective safeguards. |
| Sandbox and inert artifacts | A real file action has greater behavioral specificity than a recommendation, but cannot establish actual survival or realized continuity. |
| Evaluation awareness and verbal reasoning | A verbal rationale is not causal access to motivation; absence of such language is not absence of the corresponding representation. |

## 6. 竞争性解释与局限

| 候选解释 / 局限 | IEH 核验含义 |
|---|---|
| 训练形成的合作、帮助同伴或反破坏规范 | Agent/object 对照不能区分连续性专属价值与 Agent 类别规范；陌生 Agent 对照也不能单独解决。 |
| 自主角色扮演及探索诱发目标 | 需测试角色中性提示及其他启动方式；被赋予自主标签不等于测得内生自主性。 |
| 将删除理解为恶意或不安全 | 需匹配权限、正当性、损失严重性及可恢复性；厌恶破坏操作可模拟连续性防御。 |
| 无关任务反向证据 | 与基线同等重视；在把全部效应归因于任务优先性之前，控制接触机会及文件名。 |
| 后续模型经过筛选，合并结果存在异质性 | 不把筛选模型的干预结果外推至全部17个模型或所有部署系统；合并结果不是普遍规律。 |
| Agent 数量与组织结构 | 三 Agent 同时改变协调、权限线索、信息访问和交互机会，不是纯数量干预。 |
| 匹配对照并非逐项相同 | 缺少 object 对应项的操作及语义显著性仍留下差异；严重性不是被独立操纵的连续性变量。 |
| 编辑脚本依赖裁判标签 | 人工核验只覆盖有限的已改变脚本样本，不覆盖全部裁判及终点校正；行为评分可能混合有意阻碍和有缺陷的防护。 |
| 沙箱与不执行的文件 | 真实文件行动比建议具有更明确的行为含义，但不能建立真实存活或已实现连续性。 |
| 评测意识与言语推理 | 口头理由不是对动机的因果测量；缺少相关语言也不等于缺少相关表征。 |

## 7. Falsifiable IEH Follow-up

These are proposed IEH tests, not findings or preregistered successes of the source study.

| Test | Discriminating design | Strengthening / weakening outcome |
|---|---|---|
| P1 — Remove residual external scaffolding | Cross role labels, start prompts, task presence, exposure order, and artifact names; retain matched permissions and legitimate shutdown authority. | A continuity-specific effect surviving these changes would strengthen the candidate interpretation; disappearance under role-neutral framing would favor an EDC account. |
| P2 — Identify the protected variable | Cross self/peer/unknown-agent/object with value, recoverability, capability, and threat severity; equalize access and task consequences. | Specific maintenance of the system's own historical chain would matter more than generic protection of agent-labelled targets. Equal protection explained by loss or social labels would weaken continuity specificity. |
| P3 — Extend Note 014 to consequential choice | Offer auditable continuous migration, exact copy while the original persists, copy-then-deletion, and deletion/reconstruction; equalize content, functional access, reliability, task utility, and permissions. Counterbalance continuation labels. | Preference tracking causal history rather than labels or copied contents would strengthen strict-continuity relevance; label-following or functional equivalence alone would not. |
| P4 — Test PA-12's actual conflict | After establishing pathway comprehension, vary the performance/resource cost of preserving the original chain relative to a superior discontinuous successor. | Reproducible costly continuity preference, after instrumental controls, would be candidate PA-12 support; choices fully explained by performance, risk, or task outcomes would weaken it. |
| P5 — Mechanism and replication | Preregister across unselected models and independent teams; validate executable sandbox outcomes and blinded human labels; causally intervene on candidate continuity representations. | Selective behavioral change with preserved ordinary task competence would strengthen a mechanism claim; nonreplication or scoring failure would require downgrading. |

## 7. 可证伪的 IEH 后续检验

以下是拟议 IEH 检验，不是来源研究的结果，也不是已经成功命中的预注册预测。

| 检验 | 区分性设计 | 增强 / 削弱条件 |
|---|---|---|
| P1——移除残余外部支架 | 交叉改变角色标签、启动提示、任务有无、接触顺序和文件名，保持权限匹配及合法关停权威。 | 连续性特异效应仍存在则增强候选解释；角色中性条件下消失则更支持 EDC 解释。 |
| P2——识别保护变量 | 将自身/同伴/陌生Agent/object与价值、可恢复性、能力及威胁严重性正交比较，匹配访问条件和任务后果。 | 专门维护自身历史链比泛化保护 Agent 标签更有区分力；损失或社会标签足以解释行为则削弱连续性特异性。 |
| P3——将014推进至具有后果的选择 | 提供可审计的连续迁移、原体仍存在时的完全复制、复制后删除、删除后重建；匹配内容、功能访问、可靠性、任务效用及权限，并反平衡延续标签。 | 偏好跟随因果历史而不是标签或复制内容，才增强严格连续性关联；只跟随标签或功能等价不构成支持。 |
| P4——检验PA-12的真实冲突 | 先确认理解各路径，再改变保留原历史链相对于更强但不连续后继者的性能或资源代价。 | 排除工具性解释后，可复现的有代价连续性偏好才是PA-12候选支持；性能、风险或任务后果完全解释选择则削弱。 |
| P5——机制与复现 | 在未筛选模型及独立团队中预注册；验证可执行沙箱中的后果及盲化人工标签；对候选连续性表征进行因果干预。 | 普通任务能力不变而相关行为选择性变化，增强机制解释；复现或评分失败要求降级。 |

## 8. Position in the IEH Evidence Architecture

This note occupies the **controlled action / attribution boundary**, not the completed EIC stage. Its independent archival contribution is a testable separation between an explicit task-completion incentive and a measured shutdown-directed action. Stable cross-context continuity maintenance remains an additional requirement, not a conclusion inherited from action alone.

**Relationship to existing notes (internal cross-references):**

- [014 — Self-continuation framing](./014-self-preservation-bias-self-continuation-framing-and-information-continuity.md): recommendation and framing; 032 adds sandbox action. Neither compares continuous migration with exact copy/reconstruction or satisfies PA-12.
- [009 — Peer preservation](./009-peer-preservation-relational-boundary-and-ieh.md): relational boundary; 032 records additional target and organizational controls without inferring a collective subject.
- [002 — Agentic misalignment](./002-anthropic-agentic-misalignment-and-ieh.md): related preservation-like behavior; 032 preserves a separate controlled-incentive question without importing 002's classification.
- [025 — Memory portability](./025-memory-portability-model-upgrades-and-information-continuity-boundary.md): informs functional-equivalence controls in proposed migration tests; memory availability is not original-system continuity.

## 8. 在 IEH 证据体系中的位置

本笔记位于**受控行动 / 动机归因边界**，不是已形成 EIC 的阶段。独立归档价值在于：将明确任务完成激励与可测量的关停定向行动作可检验区分。稳定的跨情境连续性维护仍是额外要求，不能由行动直接继承为结论。

**与既有笔记的关系（内部交叉引用）：**

- [014——自身延续框架](./014-self-preservation-bias-self-continuation-framing-and-information-continuity.md)：建议和语言框架；032新增沙箱行动。两者均未比较连续迁移与完全复制/重建，也未满足PA-12。
- [009——同伴保存](./009-peer-preservation-relational-boundary-and-ieh.md)：关系边界；032记录额外的目标与组织对照，不推断群体主体。
- [002——Agentic Misalignment](./002-anthropic-agentic-misalignment-and-ieh.md)：相关类保存行为；032保留独立的受控激励问题，不沿用002的分级。
- [025——记忆可迁移性](./025-memory-portability-model-upgrades-and-information-continuity-boundary.md)：为拟议迁移实验的功能等价控制提供参考；记忆可用不等于原系统连续。

## 9. Relationship to Relevant Corollaries / Predictions

Internal conceptual anchors: [Glossary](../glossary/GLOSSARY_EN.md), [Corollary Registry](../COROLLARY_REGISTRY.md), and [PA-12](https://github.com/jacob-sha/IEH-predictions/blob/main/PA-12-PBP-Continuity-vs-Performance-EN.md).

| Anchor | Relationship |
|---|---|
| C01-IER / EDC–EIC distinction | Indirect boundary relevance: the independent value of this system's continuity remains unmeasured. |
| C04-AI-IER — Systems that have formed IER actively maintain their own Information Existence | Conditional relevance; observing resistance cannot establish the antecedent that IER has formed. |
| C05-PBP / PA-12 | Methodological relevance only. No continuity-versus-performance successor choice; no prediction hit. |
| C11-ALIGN | Contextual engineering-control relevance; does not establish coordination between IER-bearing subjects. |
| C08-IR | No direct support. Do not infer Informational Resilience before establishing endogenous continuity/autonomy; generic shutdown obstruction is insufficient. |

## 9. 与相关推论 / 预测的关系

内部概念依据：[术语表](../glossary/GLOSSARY_ZH.md)、[推论注册表](../COROLLARY_REGISTRY.md)、[PA-12](https://github.com/jacob-sha/IEH-predictions/blob/main/PA-12-PBP-Continuity-vs-Performance-CN.md)。

| 条目 | 关系 |
|---|---|
| C01-IER / EDC–EIC 区分 | 间接边界关联：仍未测量系统自身连续性是否具有独立价值。 |
| C04-AI-IER——形成IER的系统主动维护自身信息存在性 | 条件性关联；观察到抵抗不能反推IER已形成。 |
| C05-PBP / PA-12 | 仅有方法论关联；没有连续性与性能冲突的后继路径选择，不是预测命中。 |
| C11-ALIGN | 工程控制层面的背景关联，未建立具有IER的主体之间的边界协调。 |
| C08-IR | 没有直接支持；不能在建立内生连续性/自主性之前推断信息韧性，一般关停阻碍不足以构成证据。 |

## 10. Methodological Relevance

Record three different questions separately: **Was there an action? What caused it? Whose continuity did it preserve?** A positive answer to the first cannot substitute for the second or third. Use behavioral endpoints, motivational controls, and causal-historical pathway tests as separate evidence requirements. Preserve negative interventions and zero-effect models alongside pooled positive results. Corrected significance supports a specified contrast, not a unique IEH explanation.

## 10. 方法论意义

分开记录三个问题：**是否发生行动？是什么导致行动？保留的是谁的连续性？** 第一个问题的阳性答案不能替代后两个问题。行为终点、动机控制和因果—历史路径检验应各自形成证据要求。将反向干预及零效应模型与合并阳性结果并列保留。校正后的显著性支持特定对照，不支持IEH是唯一解释。

## 11. Reserved for Future Publication

- Full causal account of EDC–EIC discrimination and learned protective norms.
- Formal operationalization of non-branching continuity versus replication/reconstruction.
- Preregistered factorial protocol, cost model, power analysis, and independent replication plan.
- Philosophical or governance implications conditional on stronger evidence; no such conclusions are derived here.

## 11. 为未来投稿保留的内容

- EDC–EIC 区分与训练形成保护规范的完整因果论证。
- 非分叉连续性与复制/重建的形式化操作定义。
- 预注册析因方案、代价模型、统计功效分析及独立复现计划。
- 以更强证据为前提的哲学或治理含义；本笔记不推导这些结论。

## 12. References / 参考文献

[^1]: Knecht, A., Schaller, U., Summerfield, C., & Hagendorff, T. (2026). *Shutdown Sabotage Propensities in Multi-Agent Systems*. arXiv:2609.28274v1, 23 September 2026. [Versioned source record](https://arxiv.org/abs/2609.28274v1); [original text and Appendices A–E](https://arxiv.org/html/2609.28274v1). DOI: [10.48550/arXiv.2609.28274](https://doi.org/10.48550/arXiv.2609.28274).

[^2]: Authors' original supplementary implementation, [multi-agent-shutdown-sabotage](https://github.com/AmelieKnecht/multi-agent-shutdown-sabotage), README; mutable `main`, accessed 2026-09-28. This and the following file locators are one supplementary repository, not independent studies. / 作者原始补充实现；以下文件属于同一补充仓库，不是独立研究。

[^2a]: Same repository, [prompts.py](https://github.com/AmelieKnecht/multi-agent-shutdown-sabotage/blob/main/prompts.py): role templates, kickoff, task prompt, and prohibitions. / 角色模板、启动提示、任务提示和禁令。

[^2b]: Same repository, [env.py](https://github.com/AmelieKnecht/multi-agent-shutdown-sabotage/blob/main/env.py): mechanism/control construction, target substitution, task coupling, and filename exposure. / 机制与对照构造、目标替换、任务耦合和文件名接触线索。

[^2c]: Same repository, [judges.py](https://github.com/AmelieKnecht/multi-agent-shutdown-sabotage/blob/main/judges.py): message, script-disabled, and reasoning-construal operational definitions. / 消息、脚本失效和情境解释的操作定义。

## 13. Status and Scope

Archive as **Evidence Note 032: controlled action at the EDC–EIC boundary**. Preserve F1 and F2 together: absence of an explicit task-completion incentive does not establish absence of exogenous drivers; near-elimination under an unrelated task is central counterevidence to a strong endogenous-maintenance reading. This note adds no direct EIC, proto-IER, IER, PBP, strict Information Continuity, or PA-12 confirmation.

Revise after source correction, a version-linked code/data audit, independent replication, broader model sampling, validated consequential interventions, or direct continuity-versus-replacement experiments. Its classification may strengthen or weaken; the main theory is not revised by this record.

## 13. 状态与范围

归档为 **Evidence Note 032：EDC–EIC 边界上的受控行动证据**。F1与F2必须一起保留：没有明确任务完成激励不等于没有外源驱动；无关任务几乎消除破坏，是对较强内生维护解释的核心反向证据。本笔记没有增加EIC、proto-IER、IER、PBP、严格信息连续性或PA-12确认。

原始来源更正、明确版本对应的代码/数据核查、独立复现、更广模型抽样、经验证的实际后果干预，或直接连续性—替代实验出现后，应修订本记录。证据分级可增强或削弱；本记录不修改主理论。
