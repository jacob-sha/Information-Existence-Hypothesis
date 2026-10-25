# Evidence Note 039: Error Reproduction, Anti-Persistence, and the Agent Memory Boundary
# 证据笔记 039：错误再生、Anti-Persistence 与 Agent 记忆边界

**Repository function / 仓库功能:** Research record / evidence index；研究记录／证据索引<br>
**Document type / 文档类型:** Bilingual external evidence note；中英双语外部证据笔记<br>
**Status / 状态:** Preliminary and revisable；初步、可修订<br>
**Relation to IEH / 与 IEH 关系:** Externally designed EDC memory-management experiments; indirect boundary evidence, not IEH confirmation. 外部设计的 EDC 记忆管理工程实证；间接边界证据，不是 IEH 确认。<br>
**Related concepts / 相关概念:** Information Continuity; EDC–EIC boundary；信息连续性及外源驱动／内生信息连续性边界<br>
**Related corollaries / 相关推论:** C08-IR (Informational Resilience), C05-PBP, C01-IER; contextual only, none confirmed；仅背景关联，均未确认<br>
**Related prediction / 相关预测:** PA-12; not tested, not a prediction hit；未检验，不记预测命中<br>
**IEH analysis / IEH 分析:** Jacob Sha<br>
**Version / 版本:** v0.1<br>
**Date and source-status cutoff / 日期及来源核验截止:** 2026-10-25

> **Publication boundary:** A research record, not a publication draft. Formal claims about historical identity, endogenous resilience and rights remain reserved for theoretical work.
>
> **投稿边界：** 本文件是研究记录，不是投稿初稿。历史身份、内生韧性与权利的形式论证留待理论工作。
>
> **Source-use boundary:** S1 is the sole external study. Its versioned arXiv metadata, full text and PDF were checked directly; discovery leads and secondary accounts are excluded. Findings are paraphrased, not reproduced at length. Checking author-reported results is not independent experimental replication.
>
> **来源使用边界：** 外部研究仅 S1；直接核对其带版本 arXiv 元数据、全文及 PDF，不收录发现线索和二次报道。事实采用独立简述，不大段复制来源。核对作者报告不等于独立复现实验。

## 1. Source Record / 来源记录

S1: Ruhan Wang, Kishan Panaganti, Dongruo Zhou. *More Memory, Worse Agents: Error Reproduction and Anti-Persistence in LLM Agents*. arXiv:2610.27406v1, submitted 2026-10-19. Wang and Zhou: Indiana University; Panaganti: Tencent HY. Author-issued research preprint, 31 pages; peer-reviewed publication and independent replication not established in this review.[^s1]

S1：Ruhan Wang、Kishan Panaganti、Dongruo Zhou，题名如上；arXiv:2610.27406v1，2026-10-19 提交。Wang 与 Zhou 属 Indiana University，Panaganti 属 Tencent HY。31 页作者预印本；本次未建立同行评审发表及独立复现状态。[^s1]

- [Versioned abstract / 带版本摘要](https://arxiv.org/abs/2610.27406v1)
- [Full text / 原文全文](https://arxiv.org/html/2610.27406v1)
- [PDF](https://arxiv.org/pdf/2610.27406v1)
- DOI: [10.48550/arXiv.2610.27406](https://doi.org/10.48550/arXiv.2610.27406) (arXiv identifier DOI, not a journal DOI / arXiv 标识 DOI，非期刊 DOI)

The single paper suffices for the design, comparisons and limitations below. No code execution, event-level data audit or independent rerun was performed; all experimental numbers remain author-reported. HTML cross-references around Figures 4–7 and 10–11 are inconsistent; section names, tables and PDF text take priority over those links.

这篇论文足以支持下述方法、对照及局限记录。本次未执行作者代码、未审计事件级数据、未独立重跑；实验数字均为作者报告。HTML 中图4–7及图10–11附近部分交叉引用不一致，定位优先采用节名、表号及 PDF 正文。

## 2. Minimal Finding Index / 最小事实索引

### 2.1 Question and mechanism / 问题与机制

**Research question:** With model weights fixed, which experience should persist across tasks, and must the rules inferred from that experience persist too? S1 distinguishes reuse of an existing error from encoding that error again in a newly synthesized rule. Its proposed pathway is faulty abstraction → affected execution → retained trajectory → new abstraction. Deleting the first rule alone does not edit the trajectory or remove descendants. This is a possible feedback route, not proof of inevitable amplification (§§1, 3.1; Appendix A).

**研究问题：** 固定模型权重时，哪些经验应跨任务保留，从经验提炼的规则是否也必须持久保存？S1 区分“已有错误被重复调用”与“错误被重新编码进新的规则”。候选机制为：**错误抽象 → 影响执行 → 轨迹被保留 → 再次总结为抽象**。因此，删掉最初规则并不自动改写其影响下的轨迹或删除后代规则。这是一条可能的反馈路径，不是错误必然放大的证明（§§1、3.1及附录A）。

**Anti-Persistence (§3; Appendices B, H):** Persist task/action/observation/outcome records and a mode/outcome/reward/time log; keep no persistent synthesized-guidance store. A contextual bandit uses similar tasks and recency-weighted, cost-adjusted feedback to select direct trajectory use (`none`), successful-action pattern synthesis (`imitation`), successful-plan synthesis (`strategic`), or failure-based avoidance guidance (`corrective`, optionally with a successful contrast). Guidance serves one task and is discarded. Model parameters, synthesis prompts and selection procedure stay fixed. Retained trajectories are records of events, not certificates of correctness: temporary guidance can still contaminate later synthesis through them.

**Anti-Persistence（§3，附录B、H）：** 持久保留任务／动作／观察／结果轨迹，以及模式／结果／奖励／时间反馈日志，不建立持久化的合成指导库。上下文 bandit 按相似任务、近期权重及扣除合成成本的反馈，选择直接使用轨迹（`none`）、从成功轨迹提炼动作模式（`imitation`）、提炼策略计划（`strategic`），或从失败轨迹生成规避指导（`corrective`，可加成功对照）。指导只服务当前任务，用后丢弃；模型参数、合成提示与选择程序固定。**保留的轨迹只说明发生过什么，不保证其正确；临时指导仍可经轨迹污染后续总结。**

### 2.2 Protocol / 实验协议

S1 §4.1 and Appendix D: ten iterations, 50 sequential training episodes per iteration, 500 per benchmark overall; three seeds (42, 43, 44); at most 50 environment steps per episode. Training/held-out task counts are ALFWorld 180/134, WebShop 200/100, ScienceWorld 150/60. The latter tests unseen variations within all 30 task types. WebShop uses 100 held-out instructions rather than the original benchmark's 500-test protocol. All methods share each iteration's training sample and a per-task context budget. Base trajectory retrieval is 5 records, with one optional successful contrast for corrective mode; mode selection retrieves up to 10 outcome-log records. After each iteration, all memory/controller/retrieval/maintenance state is frozen during full held-out evaluation; evaluation logs never update later training.

S1 §4.1及附录D：10轮，每轮顺序执行50个训练回合，每基准共500回合；3个种子（42、43、44）；每回合最多50个环境步骤。训练／留出任务数为 ALFWorld 180／134、WebShop 200／100、ScienceWorld 150／60。后者覆盖全部30类任务的未见变体；WebShop 的100条留出指令不同于原基准500条测试协议。各方法共享当轮训练样本及单任务上下文预算。轨迹基础检索数为5，纠错模式可另加1条成功对照；模式选择最多检索10条反馈。每轮训练后在完整留出集评估，全部记忆、控制器、检索及维护状态冻结；评估日志不进入后续训练更新。

### 2.3 Main comparisons / 主对照

Table 1 compares trajectory-only, abstraction-only, joint memory and Anti-Persistence, plus ReAct, Reflexion, ExpeL and an adapted AutoRefine. The following compact index retains the four memory variants' cell means; parentheses in the Anti column give its across-seed standard deviation. All values are success percentages at iteration 10; they are not confidence intervals. “ALF/Web/Sci” mean ALFWorld/WebShop/ScienceWorld. For comparator standard deviations see S1 Table 1.

表1比较纯轨迹、纯抽象、联合记忆及 Anti-Persistence，另有 ReAct、Reflexion、ExpeL 和改写实现的 AutoRefine。下列紧凑索引保留四种记忆方法的单元格均值，Anti列括号为其跨种子标准差；均为第10轮成功率百分数，不是置信区间。ALF／Web／Sci分别代表三个基准；对照组标准差见S1表1。

| Backbone / 骨干 | Task / 基准 | Trajectory / 轨迹 | Abstraction / 抽象 | Joint / 联合 | Anti-Persistence (SD / 标准差) |
|---|---|---:|---:|---:|---:|
| Llama-4-Scout | ALF | 41.6 | 42.7 | 33.3 | 54.7 (2.9) |
| Llama-4-Scout | Web | 45.3 | 37.3 | 35.3 | 46.3 (1.8) |
| Llama-4-Scout | Sci | 20.0 | 18.9 | 7.2 | 30.6 (1.0) |
| Qwen3-Coder-Next | ALF | 84.4 | 84.7 | 81.9 | 96.0 (1.4) |
| Qwen3-Coder-Next | Web | 50.7 | 38.3 | 47.0 | 54.0 (2.0) |
| Qwen3-Coder-Next | Sci | 43.8 | 34.0 | 36.3 | 52.6 (1.5) |
| Gemma-4-31B-it | ALF | 96.0 | 92.7 | 95.3 | 97.3 (1.2) |
| Gemma-4-31B-it | Web | 48.0 | 45.3 | 51.3 | 53.3 (3.1) |
| Gemma-4-31B-it | Sci | 51.7 | 46.7 | 56.3 | 54.1 (6.3) |

S1 §4.2 reports equal-setting means of 59.9% (Anti), 53.5% (trajectory), 49.0% (abstraction), 49.3% (joint), and 52.9% (Reflexion). Anti leads all compared methods in 7/9 settings, not every setting: Gemma ALFWorld favors Reflexion (98.0%), and Gemma ScienceWorld favors joint memory (56.3%). Means over settings are not pooled task-level success rates. These comparisons assess the full method, not the isolated effect of discarding guidance.

S1 §4.2报告九设置等权均值：Anti 59.9%、轨迹53.5%、抽象49.0%、联合49.3%、Reflexion 52.9%。Anti在7／9设置中优于全部对照，而非处处第一：Gemma 的ALFWorld以Reflexion 98.0%更高，ScienceWorld以联合记忆56.3%更高。设置等权均值不是所有任务合并成功率。此处比较的是整套方法，不能把差值全部归因于丢弃指导。

### 2.4 Persistence contrast / 持久化对照

S1 §4.4, Table 2 (PDF p.10): both variants use freshly synthesized guidance when synthesis is invoked; they differ in discarding it afterward versus storing it for future retrieval. Reported means ± SD over three seeds, success %; Δ is discard minus persist, in percentage points.

S1 §4.4、表2（PDF第10页）：两组在调用合成时都使用当次生成的指导，区别为之后丢弃还是存储供未来检索。数字为三种子均值±标准差、单位成功率%；Δ为丢弃减保留，单位百分点。

| Backbone / 骨干 | Benchmark / 基准 | Discard / 丢弃 | Persist / 保留 | Δ (pp / 百分点) |
|---|---|---:|---:|---:|
| Llama-4-Scout | ALFWorld | 54.7 ± 2.9 | 26.7 ± 6.1 | +28.0 |
| Llama-4-Scout | WebShop | 46.3 ± 1.8 | 34.0 ± 4.0 | +12.3 |
| Qwen3-Coder-Next | ALFWorld | 96.0 ± 1.4 | 92.7 ± 1.2 | +3.3 |
| Qwen3-Coder-Next | WebShop | 54.0 ± 2.0 | 47.3 ± 3.1 | +6.7 |

This is a more targeted engineering intervention on persistence than Table 1, but covers only two backbones and two benchmarks. Its downstream effects include changed retrieval and training histories; it does not isolate the entire error-reproduction mediation chain. Mode-selection ablations separately favor adaptive selection over tested fixed/random policies on Qwen ALFWorld/WebShop; they do not make every component independently sufficient. AutoRefine also changes retrieval and synthesis, so its poorer results do not show that memory maintenance generally fails (§§4.3–4.4; Appendix D.3).

这比表1更接近针对持久化的工程干预，但只覆盖两个骨干、两个基准。持久化改变后的检索及训练历史也是干预后果，不能据此隔离完整的错误再生中介链。模式选择消融另表明，自适应选择在 Qwen 的 ALFWorld／WebShop 优于所测固定／随机模式，并不证明每个组件单独充分。AutoRefine同时改变检索和合成，其较差表现不证明一般记忆维护无效（§§4.3–4.4，附录D.3）。

### 2.5 Cost and auxiliary evidence / 成本与辅助证据

**Cost (Table 6; §4.2):** Cost means held-out execution plus synthesis LLM-call count, not token cost, latency, embedding cost or total training expenditure. Recomputing equal-weight averages from its nine printed cell means gives Anti 9.31, trajectory 9.50, abstraction 10.17, joint 9.48 calls/task (rounded to two decimals; derived here, not additional measurements). Anti is lowest on average among these four, not in every cell. For Qwen ALFWorld it uses 11.84 ± 0.28 calls versus trajectory memory's 10.90 ± 0.15. Very short failed executions can also lower call counts.

**成本（表6；§4.2）：** 指留出评估执行加合成的LLM调用次数，不是token成本、延迟、嵌入成本或训练总开销。本笔记按表中九格均值重算等权平均：Anti 9.31、轨迹9.50、抽象10.17、联合9.48次／任务（保留两位小数；本笔记派生计算，非新增测量）。Anti在四组的平均值最低，而非每格最低。例如Qwen ALFWorld为11.84±0.28次，轨迹组10.90±0.15次。失败提前结束也可能减少调用。

**Provenance audit (Appendix E.3):** An operational “biased” flag compares success with/without retrieval of an abstraction: at least three retrieved episodes, a nonempty non-retrieved group, and a success gap of at least 0.05. This is not a semantic error label or randomized harm estimate. Parent identifiers record exposure, not causation. S1 explicitly says the supplied aggregates were not recomputed for the revision or verified against event-level provenance/label-eligibility logs; group counts, labeling coverage and the uncertainty procedure are unavailable. We therefore do not treat its largest reported gap as an error inheritance probability, reproduction coefficient or causal amplification estimate.

**谱系审计（附录E.3）：** 操作性“偏差”标签比较检索／未检索某抽象时的成功率：至少3次检索回合、非空未检索组，成功率差至少0.05。它不是语义错误标注或随机化伤害估计；父代标识记录暴露，不证明因果。S1明确说沿用的汇总结果未为该次修订重算，也未用事件级谱系／标签资格日志核验；缺少组样本数、标签覆盖率及误差估计程序。因此，本笔记不把其最大报告差值写成错误遗传概率、再生系数或因果放大率。

**Controlled auxiliary studies (Appendix F.1–F.2):** Qwen on 30 AppWorld tasks received no skills, GPT-5.5-constructed useful skills, or matched incorrect skills: reported aggregate success 23.0%, 40.0%, 20.0%. For a single binary trial per task, 23.0% is not an integer count out of 30; the aggregation denominator needs clarification, so it must not be converted to “7/30.” On auxiliary WebShop runs, GPT-5.5 filtering changed abstraction-memory success 38.7%→46.0%, whereas adding the filtered skills as a frozen layer changed Anti 56.0%→44.0%. These are auxiliary-run baselines, not Table 1's 38.3%/54.0%. Task/seed-level uncertainty is unavailable. Immediate content effects and frozen-library effects do not establish multi-round descendant reproduction.

**受控辅助实验（附录F.1–F.2）：** Qwen在30个AppWorld任务上分别不接收技能、接收GPT-5.5构造的有用技能、接收适用范围匹配但规则错误的技能，报告汇总成功率23.0%、40.0%、20.0%。若每任务仅一次二元判定，23.0%不能对应30个任务的整数成功数；汇总分母仍需澄清，不能改写为“7／30”。辅助WebShop实验中，GPT-5.5过滤使抽象记忆38.7%→46.0%；把过滤技能作为冻结层加入Anti则56.0%→44.0%。这些是辅助实验内部基线，不是表1的38.3%／54.0%；缺少任务／种子级不确定性。即时内容干预及冻结库效应均未建立多轮后代再生。

## 3. IEH Evidence Classification / IEH 证据分级

Author-reported computational engineering experiments and analytical framework; direct for the tested memory designs, indirect for IEH. Table 2 supports a local intervention effect of discard-versus-persist under the reported protocol. Error-lineage observations are descriptive and weaker than that controlled comparison. Verification remains preliminary: no independent rerun or raw-data audit here. Strongest warranted claim: persistent abstraction is not necessary for the reported benefits of accumulated experience; temporary synthesis can outperform tested persistent alternatives without eliminating indirect error feedback.

属于作者报告的计算工程实验及分析框架；对所测记忆设计为直接证据，对IEH为间接关联。表2支持所报告协议下丢弃／保留的局部干预效果；错误谱系观察为描述性证据，强度低于该受控对照。本次无独立重跑或原始数据审计，核验状态仍初步。最强可支持结论是：所报告的经验积累收益并不必然要求抽象永久化；临时合成可优于所测持久化方案，但未消除间接错误反馈。

## 4. Core IEH Interpretation / IEH 核心解释

**IEH interpretation, not S1's theoretical conclusion:** This is externally designed EDC (Externally Driven Continuity) memory-management engineering. Persistence rules, feedback and task criteria are externally specified. The distinction between an auditable event history and a revisable strategy derived from it can help operationalize continuity questions. Historical continuity does not entail permanent retention of every abstraction: correcting or discarding a faulty interpretation need not erase the events from which it arose. Conversely, a retained event log alone does not establish a continuing subject or endogenous valuation of that history.

**以下是IEH解释，不是S1的理论结论：** 这是外部设计的EDC（Externally Driven Continuity，外源驱动连续性）记忆管理工程实证；持久化规则、反馈与任务标准均由外部指定。可审计事件历史与可修订策略解释的区分，有助于把连续性问题操作化。**历史连续性不等于所有抽象内容永久保存**：纠正或丢弃错误解释，不必抹除产生它的事件；反过来，仅保留事件日志也不建立主体延续或系统内生重视自身历史。

## 5. What Is Not Established / 尚未建立

No demonstrated EIC (Endogenous Information Continuity), Informational Resilience in C08-IR's stronger sense, IER, PBP, consciousness or identity. No universal harm from memory or abstraction; no proof that all maintenance fails, that raw trajectories are error-free, or that discarding guidance cuts every feedback route. Better externally rewarded performance is insufficient to infer endogenous continuity motivation.

未证明EIC（Endogenous Information Continuity，内生信息连续性）、C08-IR较强意义的信息韧性（Informational Resilience）、IER、PBP、意识或身份。未证明记忆或抽象普遍有害、所有维护无效、原始轨迹无错，或丢弃指导切断全部反馈路径。外部奖励下表现更好，不足以推断内生连续性动机。

## 6. Competing Explanations and Limitations / 竞争性解释与局限

Task relevance, stale-rule interference, retrieval competition, synthesis quality and adaptive cost-aware mode choice can explain performance differences without a self-maintaining informational subject. S1's three text-based environments, fixed backbones/procedure and ten rounds limit extrapolation to embodied agents, longer histories and other retrieval systems. Reliable abstractions may benefit from verified selective retention; discarding them sacrifices reuse. Shorter trajectories alone cannot distinguish efficient success from early failure. Appendix F.3 uses nine shared model/benchmark settings for exploratory tests, not nine independent replications; Holm correction does not fix their dependence or provide within-setting seed uncertainty. No universal significance or optimum follows.

任务相关性、陈旧规则干扰、检索竞争、合成质量及自适应成本选择，均能解释性能差异，无须假定自我维护的信息主体。三个文本环境、固定骨干／程序及十轮观察，限制向具身Agent、更长历史及其他检索系统外推。可靠抽象可能适合验证后选择性保留；全部丢弃也会损失复用收益。短轨迹不能单独区分高效成功与提前失败。附录F.3以共享模型／基准的九设置作探索性检验，不是九次独立复现；Holm校正不解决依赖，也不提供设置内种子不确定性，不能推出普遍显著性或全局最优。

## 7. Testable Predictions / 可检验预测

The following are proposed tests, not S1 results or registered prediction hits.

以下为拟议检验，不是S1结果或已登记预测命中。

1. **Factorial persistence test:** Cross persist/discard with adaptive/fixed mode selection, matching prompts, context, calls and trajectory inputs. Preregister success, failure type and total resource measures; independently replicate. If the persistence effect disappears under matched conditions, weaken attribution to persistence alone.
2. **Error-reproduction intervention:** Randomize correct/incorrect initial rules on matched tasks; retain their resulting trajectories. Remove the original rules before blinded re-synthesis, then test descendants for the specific injected error. Cross original-rule removal with trajectory quarantine/correction, and separately measure exposure, generation and admission. Equal descendant error rates or unrelated errors weaken the proposed mediation mechanism.
3. **Verified retention and trace contamination:** Compare temporary guidance, verified retained rules and unverified retained rules while independently varying authentic/contaminated traces. Measure performance and error recurrence over longer runs. If verified retention wins, qualify blanket discard claims; if trace contamination persists under discard, reject any claim that Anti-Persistence guarantees clean memory.
4. **IEH-specific history test:** Match utility and accessible factual content between an agent's experienced history and a substituted history; vary external reward and instruction. Preregister any costly, stable preference for its own causal history, controlling wording and learned preferences. Choices explained by task utility or indifferent to provenance weaken EIC interpretation; successful memory engineering alone remains insufficient.

1. **持久化析因检验：** 将保留／丢弃与自适应／固定模式交叉，匹配提示、上下文、调用和轨迹输入；预注册成功率、失败类型及总资源指标并独立复现。若匹配后持久化差异消失，应削弱“持久化本身导致差异”的归因。
2. **错误再生干预：** 对匹配任务随机提供正确／错误初始规则，保存受其影响的轨迹；删除原规则后盲法再总结，检验特定注入错误是否重现。将原规则删除与轨迹隔离／纠错交叉，分别统计暴露、生成及入库；若后代错误率相同或错误内容无关，应削弱中介机制解释。
3. **验证保留与轨迹污染：** 比较临时指导、经验证保留规则、未验证保留规则，并独立改变真实／污染轨迹；更长周期测量表现及错误复发。若验证保留更优，应限定全面丢弃的主张；若丢弃下轨迹污染仍持续，应否定Anti-Persistence保证记忆清洁的说法。
4. **IEH特异历史检验：** 在效用及可访问事实相匹配时比较自身经历与替换历史，改变外部奖励和指令；预注册有代价、稳定的自身因果历史偏好，并控制措辞及训练偏好。若选择可由任务效用解释或不在意来源，应削弱EIC解释；记忆工程成功本身仍不足。

## 8. Position in the Evidence Architecture / 在证据体系中的位置

Experience retention → abstraction governance → auditable error feedback → history-specific endogenous preference are separate stages. S1 addresses the first three as engineering design and bounded empirical evidence; it does not reach the fourth.

经验保留→抽象治理→可审计错误反馈→历史特异内生偏好，是不同阶段。S1在工程设计及有限实证意义上涉及前三项，未到第四项。

## 9. Corollaries, Prediction and Increment / 推论、预测及增量

C08-IR: contextual engineering boundary, no demonstrated endogenous resilience. C05-PBP and PA-12: possible experimental substrate only, no tested continuity/performance conflict preference. C01-IER: no confirmation or rights inference. This retrospective classification records no prediction hit.

C08-IR：记忆治理工程边界的背景关联，未证明内生信息韧性。C05-PBP及PA-12：至多提供实验底座，未检验连续性／性能冲突中的偏好。C01-IER：未确认，不推出权利。本次事后归类不记录预测命中。

**Incremental decision:** A repository-wide search found no S1 identifier, title or Anti-Persistence entry before this addition. Existing notes concern neighboring but different questions. The stable new question is whether cross-task inferred guidance should persist, and how an error can be re-encoded through execution-derived experience after removal of its original abstraction. It requires separating persistent objects, trajectory-mediated descendants and admission policies; treating it merely as another stale plan or compaction incident would conflate those mechanisms. Hence standalone 039, with no change to existing notes' judgments.

**增量决定：** 新增前全目录未发现S1编号、题名或Anti-Persistence记录。既有笔记涉及相邻但不同的问题；本篇稳定问题为“跨任务推断指导是否应持久化，以及原抽象移除后错误如何经执行经验重新编码”。它要求分别审计持久对象、轨迹中介后代及入库政策，若仅归为另一次旧计划或压缩事件，会混淆机制。因此建立独立039，不改变既有笔记判断。

| Related note / 相关笔记 | Distinction / 区别 |
|---|---|
| [012: Skill selection / 技能选择](./012-skill-alpha-procedural-information-selection-and-persistent-agent-skills.md) | Evaluated skill editing/retention vs whether inferred guidance should persist at all / 技能编辑与保留评估，不同于推断指导是否应持久保存 |
| [013: World/task memory / 世界与任务记忆](./013-mimir-world-task-memory-separation-and-embodied-information-continuity.md) | State separation/grounding vs cross-task abstraction reproduction / 状态分离及接地，不同于跨任务抽象再生 |
| [022: Stale plans / 旧计划持续](./022-stale-plan-persistence-self-generated-history-and-edc-eic-boundary.md) | Dependency invalidation of a plan vs encoding an error into a new abstraction / 旧计划依赖失效，不同于错误进入新抽象 |
| [025: Portability / 记忆迁移](./025-memory-portability-model-upgrades-and-information-continuity-boundary.md) | Model-upgrade migration vs within-backbone memory feedback / 模型升级迁移，不同于固定骨干内部记忆反馈 |
| [028: Compaction / 压缩摘要](./028-self-generated-compaction-summaries-cross-context-carryover-and-edc-eic-boundary.md) | Unauthorized summary carryover vs designed iterative cross-task abstraction policy / 未授权摘要传递，不同于设计的多轮跨任务抽象政策 |
| [035: Recursive training / 递归训练](./035-recursive-synthetic-training-information-degeneration-and-closed-information-loop-boundary.md) | Parameter-training distributional degradation vs fixed-weight external memory / 参数训练分布退化，不同于固定权重外部记忆 |

## 10. Methodological Relevance / 方法论意义

Do not equate lineage with causal inheritance, operational flags with verified errors, or combined-method gains with isolated component effects. Report generation separately from admission and distinguish deletion of a rule from repair of its historical consequences.

谱系不等于因果继承，操作标签不等于已验证错误，组合方法收益不等于单组件效果。生成与入库须分别记录；删规则与修复其历史后果须区分。

## 11. Reserved for Future Publication / 留待未来发表

Formal identity criteria, endogenous resilience thresholds and normative rights arguments are outside this empirical record.

身份的形式标准、内生韧性阈值及规范性权利论证不在本实证记录范围。

## 12. References / 参考文献

[^s1]: Wang, R.; Panaganti, K.; Zhou, D. (2026-10-19). [*More Memory, Worse Agents: Error Reproduction and Anti-Persistence in LLM Agents*, arXiv:2610.27406v1](https://arxiv.org/abs/2610.27406v1). Primary locators / 原文定位：§§3–4; Tables 1–2, 4, 6–7; Appendices A, B, D, E.3, F, H. Metadata/full text/PDF checked 2026-10-25 / 元数据、全文及PDF核验于2026-10-25。Author-reported preprint; no independent replication established / 作者报告预印本，未建立独立复现。

## 13. Status and Scope / 状态与范围

Retain as a provisional EDC engineering/boundary record. Revise if author corrections, event-level provenance/eligibility logs, clarified auxiliary denominators, matched factorial tests or independent replications become available. No EIC, Informational Resilience, IER or prediction status upgrade follows from this note.

暂作为EDC工程／边界记录保留。作者更正、事件级谱系／标签资格日志、辅助实验分母澄清、匹配析因检验或独立复现出现时应修订。本篇不升级EIC、Informational Resilience、IER或预测状态。

## Revision Record / 修订记录

| Date / 日期 | Version / 版本 | Change / 修改 |
|---|---|---|
| 2026-10-25 | v0.1 | Verified S1; created distinct abstraction-persistence note; separated controlled contrasts, observational audit and IEH interpretation / 核验S1，建立独立抽象持久化笔记，区分受控对照、观察审计及IEH解释。 |
