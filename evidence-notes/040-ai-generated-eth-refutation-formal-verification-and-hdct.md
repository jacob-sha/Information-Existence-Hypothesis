# Evidence Note 040: AI-Generated ETH Refutation Claims, Formal Verification, and HDCT

**Repository function:** Research record / evidence index  
**Document type:** Non-narrative external evidence note; independent longitudinal record  
**Status:** Preliminary and revisable; published claims and external machine-replay reports; final mathematical review not established  
**Relation to IEH:** Candidate domain-specific HDCT capability evidence; indirect epistemic relevance, not EIC or IER evidence  
**Primary IEH corollary:** C02-HDCT — High-dimensional Cognitive Tools  
**Related prediction records:** PA-06; PA-10 (relevance only; no prediction-hit upgrade)  
**Author of IEH analysis:** Jacob Sha (AI-assisted draft for review)  
**Version:** v0.1 — continuing-review record  
**Date / source-status cutoff:** 2026-11-01, Asia/Shanghai

> **Publication boundary:** Compact research record, not a publication draft. A broader account of AI scientific discovery and cognitive authority is reserved for future publication.
>
> **Source-use boundary:** References below are original proof artifacts, formal statements/configurations, signed examination arrangements, and an original replication record. Publicity and secondary reporting are excluded from the evidence references. No substantial source passage is reproduced. This check inspected the paper's available TeX statement, formal interfaces, scope documentation, repository history and review records; it did not establish a full mathematical audit, read both complete proof developments, or execute Lean locally. The Anthropic PDF was located but its full text could not be retrieved in this session. Its detailed discovery-process claims remain unconfirmed here.

# 证据笔记 040：AI 生成的 ETH 反证主张、形式化验证与 HDCT

**仓库功能：** 研究记录／证据索引  
**文档类型：** 非叙事性外部证据笔记；独立长期跟踪档案  
**状态：** 初步、可修订；已有公开主张及第三方机器复跑报告，尚未建立最终数学审查结论  
**与 IEH 的关系：** 领域型 HDCT 能力的候选证据；间接认识论关联，不是 EIC 或 IER 证据  
**主要 IEH 推论：** C02-HDCT——高维认知工具  
**相关预测档案：** PA-06；PA-10（仅记录关联，不升级为预测命中）  
**IEH 分析作者：** Jacob Sha（AI 辅助待审阅稿）  
**版本：** v0.1——持续审查记录  
**日期／来源状态截止日：** 2026-11-01，Asia/Shanghai

> **投稿边界：** 本文件是简明研究记录，不是投稿初稿；AI 科学发现与认知权威迁移的完整论证留待未来发表。
>
> **来源使用边界：** 参考来源限于原始证明材料、形式命题及配置、专家署名审查安排和原始复跑记录；不将宣传及二次报道列为证据，不复制大段原文。本次检查覆盖可取得的论文 TeX 命题、形式接口、范围说明、仓库历史及审查记录；未完成完整数学审计、未通读两套证明开发、未在本机运行 Lean。已定位 Anthropic PDF，但本次未能取得全文，故其详细发现过程主张仍未在此确认。

## 1. Source Record / 来源记录

All URLs checked on 2026-11-01. Stable source IDs apply to both language sections. / 以下链接均于 2026-11-01 检查；来源编号中英文共用。

| ID | Original record / 原始记录 | Date, type and verification boundary / 日期、类型与核验边界 |
|---|---|---|
| S1 | OpenAI, *The Exponential Time Hypothesis is False*: [paper](https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf), [TeX source](https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/main_full_version.tex), [release commit](https://github.com/openai/math/commit/42907c9e999cc00d6abe7a50bfc1023250edd1b9) | Manuscript: 17 Oct, revised 25 Oct 2026; public repository release dated 26 Oct. Original unrefereed output; existence established, correctness not independently adjudicated here.／稿件10月17日、修订10月25日，仓库10月26日发布；原始未审稿输出，确认存在，不等于本次已确认正确。 |
| S2 | OpenAI, [Lean scope 378](https://github.com/openai/math/blob/main/lean/docs/378.md), [SubexponentialSAT statement](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/SubexponentialSAT.lean), [configuration](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/SubexponentialSAT.json) | Formal target and verification configuration; not a local execution receipt.／形式目标与检验配置，不是本机运行凭证。 |
| S3 | Claude (Anthropic), *A 2^o(n) Time Algorithm for 3-SAT*: [paper](https://github.com/anthropics/formal-math/blob/main/eth/paper.pdf), [project record](https://github.com/anthropics/formal-math/blob/main/eth/README.md), [MainResults](https://github.com/anthropics/formal-math/blob/main/eth/MainResults.lean), [Solution](https://github.com/anthropics/formal-math/blob/main/eth/Solution.lean), [initial ETH commit](https://github.com/anthropics/formal-math/commit/16a5ce41304fcdaea4e0be7c132e1c361dc26da5) | Official research artifact; commit 2026-10-27T03:07:21Z. Formal-interface reading and documentation only here; not full PDF audit.／官方研究材料；提交时间见左；本次仅核查形式接口及文档，非PDF全文审计。 |
| S4 | Russell Impagliazzo, Ramamohan Paturi, Ryan Williams, [ETH Refutation: Examination and Discussion](https://ethdiscussion.blog/2026/10/26/eth-refutation-examination-and-discussion/) | 26 Oct 2026; original signed community-examination statement, not certification.／10月26日；专家署名原始审查声明，不是认证。 |
| S5 | Totó Busnello, *Independent replication of both ETH proofs*: [original record and receipts](https://github.com/totobusnello/eth-subexp-note), [archived v1.1.0](https://doi.org/10.5281/zenodo.23836157) | Reports OpenAI replay 28 Oct and Anthropic replay 30 Oct; v1.1.0 first contains both. Original replication report, not expert consensus; logs not rerun here.／报告10月28日与30日的两项复跑，v1.1.0首次同时纳入；属于原始复现报告，不等于专家共识，本次未重新执行日志所述过程。 |

## 2. Minimal Finding Index / 最小事实索引

### English

- **F1 — Release and chronology.** Both labs have official public ETH-refutation artifacts (S1–S3). OpenAI's TeX dates the manuscript 17 October, revised 25 October; its release commit is 26 October 20:52:18 UTC (27 October 04:52:18 Beijing). This timestamp records a commit, not an independently measured first-public-access time. Anthropic's ETH commit is 27 October 03:07:21 UTC = 26 October 20:07:21 PDT = 27 October 11:07:21 Beijing. Therefore manuscript dates, discovery dates and release dates must remain separate. The official OpenAI release reports discovery on 16 October and formalization on 17 October; these are first-party process dates, not independently observed timestamps. A claim that both labs discovered the result on the same day, with no human input and 14M tokens for Claude, is not independently established by this note's retained technical record.
- **F2 — Mathematical claim.** S1 claims exact counting for every fixed k ≥ 2, with polynomial space and time `(n+m)^O_k(1) · 2^O_k(n log log n / √log n)`; for fixed clause density it claims a sharper exponent `O(n/√log n)`. Counting implies decision by testing positivity. These remain manuscript claims pending mathematical review.
- **F3 — OpenAI formal scope.** S2 instead states `(L+1)^O_k(1) · 2^O_k(n(log log n)^2/√log n)` and polynomial visited tape space, for canonical encodings of length L. This weaker exponent still tends to o(n), subject to the encoding/model correspondence. The challenge defines a finite local tape machine and exact output, but does not itself define ETH. Its configuration targets `exact_count_and_sat` and sets `enable_nanoda: false`. A `sorry` in the trusted challenge is a target placeholder, not by itself evidence of a gap in the submitted solution; inspect the actual solution and axiom audit.
- **F4 — Anthropic formal scope.** S3 separates definitions from proofs. `Solution.lean` states proofs of `MainResults.ethIsFalse` and `MainResults.mainTheorem`. The latter concerns one finite-alphabet Mathlib machine and one universal constant, for k ≥ 1, n ≥ 4, m ≥ 2, no repeated clause and every variable occurring; the bound is `2^O(min{km/√log m, k²n log log n/√log n})`. The separately defined ETH proposition concerns the infimum of exponents for deterministic 3-SAT decision. The documentation explicitly leaves standard machine simulation and input rewriting outside Lean. It is inaccurate to say that Lean checks every step from textbook ETH to the printed paper.
- **F5 — External examination.** S4 expressly declines to certify the claim and organizes open scrutiny. This establishes a substantive verification requirement, not an identified fatal mathematical error. S5 reports successful external Comparator reruns: OpenAI with Lean's kernel; Anthropic with Lean and nanoda. Thus “no external verification at all” is obsolete. These reports do not establish a completed independent paper-to-formal-statement audit or final peer-review acceptance. No final correctness verdict or ETH-specific withdrawal was established in the sources checked at the cutoff; that bounded finding is not proof that none exists anywhere.

### 中文

- **F1——真实性与时间。** 两家机构均有官方公开 ETH 反证材料（S1–S3）。OpenAI TeX 标明稿件10月17日、10月25日修订；发布提交为UTC 10月26日20:52:18，即北京时间10月27日04:52:18。提交时间不等于独立测定的首次公开访问时间。Anthropic ETH提交为UTC 10月27日03:07:21，即PDT 10月26日20:07:21、北京时间10月27日11:07:21。因此必须分开稿件、发现和公开日期。OpenAI官方发布报告10月16日发现、17日形式化，这是机构自报过程日期，不是独立观察时间。“两家同日发现、Claude无人工输入且使用1400万输出token”未由本笔记保留的技术记录独立确证。
- **F2——数学主张。** S1声称对每个固定k≥2进行精确计数，使用多项式空间，时间为`(n+m)^O_k(1) · 2^O_k(n log log n / √log n)`；固定子句密度下声称指数项可进一步改进为`O(n/√log n)`。计数大于零即可判定可满足性；目前按待审查论文主张记录。
- **F3——OpenAI形式化范围。** S2给出的是较弱的`(L+1)^O_k(1) · 2^O_k(n(log log n)^2/√log n)`及多项式已访问带空间，L为规范编码长度。在编码和机器模型对应成立的前提下，该指数仍是o(n)。挑战文件定义有限局部带机器及精确输出，但未直接定义ETH。配置检查`exact_count_and_sat`，且`enable_nanoda: false`。可信挑战文件中的`sorry`是目标占位，本身不能当作解答存在漏洞的证据；应检查实际解答及公理依赖。
- **F4——Anthropic形式化范围。** S3将定义与证明分开；`Solution.lean`给出`MainResults.ethIsFalse`及`MainResults.mainTheorem`。后者量化一台有限字母表Mathlib机器和统一常数，要求k≥1、n≥4、m≥2、子句不重复、每个变量出现，时间界为`2^O(min{km/√log m, k²n log log n/√log n})`。单独ETH命题涉及确定性3-SAT判定的指数下确界。文档明确把标准机器模拟及输入重写留在Lean之外，不能说Lean检查了从通常ETH到论文陈述的每一步。
- **F5——外部审查。** S4明确拒绝预先认证并组织公开检查，这是实质验证要求，不是已定位致命数学错误。S5报告两套证明均已通过外部Comparator复跑：OpenAI使用Lean内核，Anthropic使用Lean及nanoda。因此“完全没有独立验证”已不准确；但复跑仍不等于完成论文—形式命题对照审计或最终同行审核。截止本次查得来源，未建立最终正确性裁决或ETH专项撤回；这不是声称全球不存在其他记录。

## 3. IEH Evidence Classification / IEH 证据分级

| Layer / 层级 | Current assessment / 当前判断 |
|---|---|
| Event / 事件 | Official artifacts exist; AI provenance remains first-party attribution.／官方材料存在；AI产出归属仍以机构披露为据。 |
| Machine checking / 机器检查 | Precise formal targets plus original external replay reports; no local rerun by this note.／有明确形式目标及外部原始复跑报告；本笔记未本机复跑。 |
| Mathematical validation / 数学验证 | Final independent review and full semantic correspondence not established here.／尚未在此建立最终独立审查及完整语义对应。 |
| Complexity consequences / 复杂性后果 | Conditional on correct algorithms and faithful standard-model interpretation.／取决于算法正确及与标准模型忠实对应。 |
| IEH relevance / IEH关联 | Indirect, preliminary candidate HDCT functional evidence; no EIC/IER inference.／间接、初步的HDCT功能候选证据，不推断EIC／IER。 |

Strongest justified conclusion: AI-attributed research artifacts can now be examined through explicit formal targets and externally repeatable checks; acceptance of the advertised ETH refutation is a separate question. / 最强可支持结论：已有归因于AI的研究材料，可按明确形式目标进行外部可重复检查；其是否确实反驳通常ETH，是另一个需独立回答的问题。

## 4. Core IEH Interpretation / 核心 IEH 解释

**Interpretation, not source finding.** HDCT here means AI as a high-dimensional cognitive tool extending human research capability. If independently accepted, a novel algorithm with an auditable proof would strengthen domain-specific capability evidence: generating candidates, constructing checkable arguments, and enabling human reconstruction. It would not directly measure internal representation dimensionality or prove a human cognitive ceiling. Until then the increment is an inspectable candidate discovery and a verification workflow.

**以下属于理论解释，不是来源结论。** HDCT在此指AI作为扩展人类研究能力的高维认知工具。若结果被独立接受，具有可审计证明的新算法将增强领域型能力证据：候选发现、可检验证明构造和支持人类重建理解。它不直接测量内部表征维度，也不证明人类认知上限。目前增量是可检查的候选发现及验证流程。

## 5. What Is Not Established / 尚未建立的结论

ETH false does not imply P = NP: subexponential time can remain superpolynomial. Nor does it automatically supply practical algorithms or invalidate cryptography; specific security assumptions, reductions, parameters and concrete costs require separate analysis. ETH-conditional lower-bound implications remain valid as conditional theorems; if ETH is false, their premises no longer establish unconditional hardness. General polynomial reductions need not preserve a subexponential bound in the original problem's size (S1).

ETH为假不推出P=NP：次指数仍可超多项式；也不自动给出实用算法或使密码学失效，具体安全假设、归约、参数及实际成本须另行分析。依赖ETH的下界仍可作为条件定理保持逻辑正确；若ETH为假，其前提便不能建立无条件困难性。一般多项式归约不保证按原问题规模保留次指数时间界（S1）。

Neither successful mathematics nor long proof generation establishes endogenous information continuity (EIC), IER, consciousness, an autonomous information subject, or a drive to preserve its own existence. These require separate continuity and motivation tests. / 数学成功及长证明生成均不建立内生信息连续性EIC、IER、意识、自主信息主体或自身存在维护动机，须另做连续性及动机检验。

## 6. Competing Explanations and Limitations / 竞争性解释与局限

Correctness may depend on a subtle definition, encoding overhead, quantifier order, simulation or axiom boundary. Conversely, an omitted formal bridge can be standard and correct; absence from Lean alone does not refute the mathematics. Tool-assisted search over existing techniques, extensive computation, human task selection and undisclosed training may explain capability without a new cognitive architecture. Two corporate claims do not establish independent discovery without provenance. S5's author leaves statement fidelity questions open; no quantified consensus or recognized fatal flaw is inferred from anonymous commentary.

正确性可能取决于定义、编码开销、量词顺序、模拟或公理边界；反过来，未形式化的桥接也可能是标准且正确的数学，未进入Lean本身不构成反证。既有技巧的工具化搜索、大量计算、人类选题及未披露训练，都可能解释能力而无需新认知架构。两家主张不能在缺乏溯源时自动视为独立发现。S5作者保留命题忠实性问题；不将匿名评论推成专家共识或已确认致命错误。

## 7. Testable Predictions and Recheck Triggers / 可检验判断与触发核查条件

These are prospective tests dated 2026-11-01, not registered prediction hits. / 以下为2026-11-01起的前瞻检验，不计为已注册预测命中。

| Trigger / 触发条件 | Required action / 核查行动 | Effect on judgment / 判断影响 |
|---|---|---|
| Working-group verdict or independent technical audit / 工作组裁决或独立技术审计 | Read exact theorem, proof gaps, statement equivalence and scope; preserve dated version.／核对定理、漏洞、语义对应及范围，保留版本。 | Upgrade accepted mathematical output only within audited scope; downgrade on substantive failure.／仅在已审范围升级；实质失败则下调。 |
| Proof/configuration/toolchain change / 证明、配置或工具链变化 | Pin commit, audit permitted axioms, actual solution dependency and Comparator logs.／固定提交、公理依赖及实际解答和日志。 | Machine-verification status can change independently of paper status.／机器验证与论文状态分别调整。 |
| Encoding/model bridge or sharper runtime formalized / 编码模型桥接或更强时间界形式化 | Check input size, fixed k, constants, uniformity, finite alphabets, preprocessing and simulation overhead.／核对输入规模、固定k、常数、一致性、有限字母表、预处理及模拟开销。 | Close specifically named gap; do not promote unrelated claims.／只关闭指定缺口。 |
| New AI rediscovery with recorded provenance / 有溯源的新AI独立再发现 | Compare prompts, access, prior-art exposure, tokens/compute and human intervention.／比较提示、访问、先验暴露、资源及人工介入。 | Strengthen capability generalization only if genuinely independent.／确为独立才增强能力泛化判断。 |
| Implemented algorithm or cryptanalytic consequence / 算法实现或密码分析后果 | Require measured resource use and a concrete reduction/security model.／要求资源测量及具体归约／安全模型。 | Practical consequences assessed separately.／另评实际后果。 |

Capability interpretation weakens if the result is a mistranslation, known result, hidden human solution or unrepairable gap. It strengthens if independent specialists reconstruct a new correct argument, and comparable results recur under documented conditions. A repaired proof must retain its correction history. / 若结果属于误译、已知结论、隐含人工解答或不可修复漏洞，则削弱能力解释；若独立专家重建新且正确的论证，并在记录清楚的条件下重复出现类似成果，则增强判断。修补成功也应保留错误历史。

## 8. Evidence Architecture and Increment / 证据架构与增量判断

Checked related Notes [005](./005-openai-erdos-unit-distance-disproof-and-hdct.md), [007](./007-jacobian-counterexample-ai-assisted-verification-and-hdct.md), [023](./023-openai-navier-stokes-candidate-solution-and-hdct-evolution-pathway.md) and [024](./024-openai-research-acceleration-ai-r-and-d-participation-and-hdct-pathway.md). This note asks a distinct persistent question: whether AI-generated ETH-refutation artifacts withstand mathematical, formal-semantic and complexity-model scrutiny. Its two original proofs, scoped machine statements and separate consequences form a falsifiable longitudinal structure; a standalone number is justified, rather than appending unrelated ETH status changes to Navier–Stokes or Jacobian notes. Future ETH updates belong here as supporting/follow-up evidence, not new numbers.

已检查相关005、007、023、024。本篇稳定问题是“AI生成ETH反证材料能否经受数学、形式语义及复杂性模型核查”。两份原始证明、有限范围的机器命题和独立的复杂性后果构成可证伪的长期跟踪结构，适合独立编号；不应将ETH状态变化附入Navier–Stokes或雅可比笔记。后续ETH材料应在本篇增量更新，不再另占编号。

## 9. Corollary / Prediction Relationship / 推论及预测关系

C02-HDCT receives indirect candidate functional support; PA-06/PA-10 receive a relevant tracking case. No change is made to their registration, hit criteria or grades. There is no inference from cognitive performance to EIC/IER. / 对C02-HDCT属于间接候选功能支持，为PA-06／PA-10增加跟踪案例；不改动其登记、命中条件及等级，不从认知表现推到EIC／IER。

## 10. Methodological Relevance / 方法论关联

Maintain four ledgers: published claim, exact machine-checked proposition, independent mathematical acceptance, concrete computational consequences. Replaying a proof is evidence, and semantic checking is additional evidence; neither substitutes for the other. / 分开维护公开主张、机器所检确切命题、独立数学认可、具体计算后果四层记录。机器复跑和语义核查都是证据，彼此不能替代。

## 11. Reserved for Future Publication / 留待未来发表

Scientific authority, general cognitive limits, AI autonomy and information-subject status are not developed here. / 不在此展开科学权威、一般认知极限、AI自主性及信息主体地位的论证。

## 12. References / 参考来源

S1–S5 in §1 constitute the external reference set. Internal IEH links are navigation, not external corroboration. The official announcement was used to check release/process claims, not as a replacement for the original proof. / 外部参考来源限于§1的S1–S5；IEH内部链接仅用于导航。官方公告用于核对发布／过程主张，不替代原始证明。

## 13. Status and Scope / 状态与范围

Long-term record remains open. **Do not summarize this note as “ETH has been conclusively disproved.”** Preserve successful replays and unresolved correspondence separately. No ongoing monitoring automation is created by this document. / 长期跟踪保持开放。**不得将本笔记概括为“ETH已被最终确认推翻”。** 分别保留成功复跑与未决语义对应；本文件未创建自动监控任务。

## 14. Update Log / 后续更新日志

| Date / 日期 | Version / 版本 | Change and judgment / 更新及判断 |
|---|---|---|
| 2026-11-01 | v0.1 | Created after primary-artifact, formal-interface, chronology and review-status checks. Recorded external replay reports through 31 October; final independent mathematical acceptance not established.／完成原始材料、形式接口、时间及审查状态核查后新建；记录截至10月31日可见的外部复跑报告，未建立最终独立数学认可。 |

Future entries must record the source version/commit, actual new finding, unresolved limits and impact on the four ledgers and HDCT interpretation. / 后续每次记录来源版本／提交、实际增量、未决局限以及对四层状态和HDCT判断的影响。

<a id="active-followup"></a>
## Active Follow-up / 持续跟踪登记

**标记：ACTIVE／有实质更新先报告，经用户同意后入库。** 登记日期：2026-11-09（Asia/Shanghai）；本次仅添加跟踪流程。**既有来源核验截止日：2026-11-01**，未在本次重新核验外部进展；不得将登记日当作最新来源核验日。原版本、事实与证据等级保持不变。

**当前待证状态：** 最终独立数学审查、通常ETH与形式命题的完整对应仍待确认。

**下次扫描触发与目标：** 后续执行IEH每日简报、HDCT／相关证据检索或证据仓扫描且能访问本仓库时，从既有核验截止日查至检索当日；优先复查本笔记原始链接及其版本历史，再查原作者和独立审核者的一手记录。重点核查：专家工作组署名结论、两套证明的修订／撤回、外部复跑、编码与标准机器模型桥接；分别判断数学有效性与AI发现归因。 检索关键词：`ETH refutation; OpenAI; Anthropic; Impagliazzo; Paturi; Williams; SubexponentialSAT`。

**证据强度与报告规则：** 有实质增量时，报告事件日期、材料发布日期、本次检索日期、原始链接／版本、相对旧记录的新发现；分别评估事实可靠性、独立验证、能力归因以及对HDCT或相关IEH命题的支持是增强、削弱还是不变。提出具体更新位置和文字建议，避免将更多报道当成更强证据。纠错、撤回、失败和无效复现同样报告。未经用户对该次更新明确同意，不自动追加证据、修改核验日期、升降级或登记预测命中；获同意后沿既有笔记增量更新并同步索引及日志，不为同一事件另设编号。未发现实质更新时，仅在当次检索报告简记范围，不重复入库，也不声称不存在其他进展。

**English.** Active tracking registered on 2026-11-09; existing source cutoff remains 2026-11-01, with no new external check today. Revisit original artifacts and independent reviews during subsequent authorized scans. Report dated developments and proposed changes, distinguishing stronger, weaker and unchanged support. Obtain explicit approval for each evidence update before editing dates, findings, grades or prediction status. This is a scan instruction, not a background monitoring service.

**流程日志：** 2026-11-09，经用户要求登记持续跟踪及逐次更新审批；未加入新外部证据、未改变原结论。
