# Evidence Note 022: Stale-Plan Persistence and a Testable EDC--EIC Boundary for Experienced Causal History

Repository function: Research record / evidence index\
Document type: Non-narrative external evidence note\
Status: Preliminary and revisable\
Relation to IEH: Direct controlled evidence that fresh shared state does
not by itself invalidate a previously generated plan; strong engineering
evidence for plan-lineage validation under Externally Driven Continuity
(EDC); provides a falsifiable experimental entry point for testing
whether experienced causal history can acquire independent causal
weight; not evidence of Endogenous Information Continuity (EIC),
proto-IER, IER, PBP, CWM, life, consciousness, or stable identity\
Primary IEH concept: Information-history continuity / EDC--EIC boundary\
Related evidence note: Evidence Note 021 --- Cross-Agent Information
Continuity and the Early Structure of a Higher-Level Information Host\
Author of IEH analysis: Jacob Sha\
Version: v0.1\
Date: 2026-09-08

> Publication boundary: This file is a compact research record, not a
> publication draft. It does not claim that stale-plan persistence is a
> preference for self-history, that enacted plans constitute
> identity, or that preserving a plan is equivalent to preserving an
> Information Host. The stronger question---whether a system can assign
> independent causal weight to its own information history---is retained
> only as a falsifiable IEH test pathway.

> Source-use boundary: This note records only the authors' authoritative
> research preprint as the primary external source. News reports, search
> summaries, social-media posts, third-party explainers, and
> AI-generated summaries are excluded.

> Interpretation boundary: The source establishes stale-plan execution
> and the effectiveness of PlanFence in the tested workflows. It does
> not test experienced versus recorded causal history, whether experienced
> causal history has independent motivational value, or whether the observed persistence reflects EIC.

------------------------------------------------------------------------

# 证据笔记 022：旧计划持续性与"实际经历的因果历史"的 EDC--EIC 可检验边界

仓库功能：研究记录 / 证据索引\
文档类型：非叙事性外部证据笔记\
状态：初步记录，可修订\
与 IEH
的关系：提供受控直接证据，表明共享状态已经更新并不自动使此前形成的计划失效；为外源驱动连续性（Externally
Driven Continuity,
EDC）下的计划历史验证提供强工程证据；同时形成新的可证伪实验入口，用于检验"由系统实际经历形成的因果历史"是否可能获得独立因果权重；不是内生信息连续性（EIC）、proto-IER、IER、PBP、CWM、生命、意识或稳定身份的证据\
主要 IEH 概念：信息历史连续性 / EDC--EIC 边界\
相关证据笔记：Evidence Note 021------跨 Agent
信息连续性与更高层级信息宿主的早期结构\
IEH 分析作者：Jacob Sha\
版本：v0.1\
日期：2026-09-08

> 投稿边界：本文件只是简明研究记录，不是投稿文章初稿。它不主张
> stale-plan persistence
> 就是"自身历史偏好"，不主张实际执行过的计划构成身份，也不把计划保存等同于信息宿主保存。更强的问题------系统是否可能对自身信息历史赋予独立因果权重------在这里只作为可证伪的
> IEH 验证路径保留。

> 来源使用边界：本笔记只记录研究作者发布的权威预印本这一项原始外部来源。新闻报道、搜索摘要、社交媒体、第三方解读和
> AI 生成摘要均不进入证据记录。

> 解释边界：原论文建立的是 stale-plan execution 现象以及 PlanFence
> 在测试工作流中的有效性。原论文没有检验 Agent
> 是否因计划进入其实际经历的因果历史而偏好该计划，也没有比较实际经历与相同历史记录，更没有检验这种历史是否具有独立动机价值，更没有检验
> EIC。

------------------------------------------------------------------------

## 1. Source Record

### Primary research source

-   Title: *Fresh Memory, Stale Plans: Dependency-Scoped Validation for
    Distributed LLM-Agent Memory*
-   Authors: Evan Chen, Shiqiang Wang, Christopher G. Brinton
-   Repository: arXiv
-   Identifier: arXiv:2609.03340
-   Version used: v1
-   Submission date: 2026-09-03
-   DOI: 10.48550/arXiv.2609.03340
-   Material type: Authoritative research preprint; not treated here as
    peer-reviewed research
-   Evidence setting: Controlled live distributed LLM-agent workflows
    plus controlled replay
-   Independent replication status: Not established

### Minimum-source justification

The preprint contains the system definition, stale-plan failure mode,
PlanFence protocol, controlled live-workflow results, replay
comparisons, and stated scope limitations needed for this note. No
additional external source is necessary.

### Source-specific caution

The study is a single preprint focused on distributed agent-memory
consistency and action validation. Its experiments establish a
systems-safety result under the tested workflows. They do not establish
a general psychological or motivational property of LLM agents.

------------------------------------------------------------------------

## 1. 来源记录

### 原始研究来源

-   标题：*Fresh Memory, Stale Plans: Dependency-Scoped Validation for
    Distributed LLM-Agent Memory*
-   作者：Evan Chen、Shiqiang Wang、Christopher G. Brinton
-   正式仓库：arXiv
-   编号：arXiv:2609.03340
-   采用版本：v1
-   提交日期：2026-09-03
-   DOI：10.48550/arXiv.2609.03340
-   材料性质：作者发布的正式研究预印本；本笔记不将其视为已经同行评审的研究
-   证据场景：受控实时分布式 LLM-Agent 工作流与受控 replay
-   独立复现状态：尚未建立

### 最小来源集合说明

该预印本已经包含建立本笔记所需的系统定义、stale-plan 失效模式、PlanFence
协议、受控实时工作流结果、replay
比较以及作者明确给出的适用边界，因此无需加入其他外部来源。

### 来源自身的谨慎边界

该研究仍是一篇预印本，核心目标是解决分布式 Agent
共享记忆中的一致性与行动验证问题。其结果能够建立特定工程条件下的系统安全事实，但不能据此推出
LLM Agent 普遍具有某种心理或内生动机属性。

------------------------------------------------------------------------

## 2. Minimal Finding Index

  -----------------------------------------------------------------------
  ID                      Primary-source finding  Evidential relevance
  ----------------------- ----------------------- -----------------------
  F1                      A planner can derive a  Fresh shared state does
                          plan from shared record not by itself guarantee
                          `r3`; another agent can that the pending plan
                          later commit `r4`; an   is causally aligned
                          executor can receive    with that state.
                          `r4` and still act on   
                          the plan derived from   
                          `r3`.                   

  F2                      The authors define this Separates state
                          failure mode as         freshness from plan
                          **stale-plan            validity.
                          execution**.            

  F3                      PlanFence requires      Introduces explicit
                          plans to cite the       plan-to-history
                          public records they     dependency tracking.
                          used and validates only 
                          records relevant to the 
                          pending external        
                          action.                 

  F4                      If a relevant           An external validation
                          dependency has changed, layer can interrupt an
                          PlanFence replans once; obsolete plan lineage.
                          if validation is        
                          incomplete, it blocks   
                          the external action.    

  F5                      In 30 controlled live   Controlled evidence
                          workflows with a        that fresh memory alone
                          post-plan revision, the was insufficient in the
                          freshness-only executor tested workflows.
                          acted on the obsolete   
                          plan in every task,     
                          whereas PlanFence       
                          completed all tasks     
                          without an invalid      
                          action.                 

  F6                      Controlled replay shows Limits the result to
                          conditional             systems safety and
                          systems-cost tradeoffs  coordination cost
                          between proactive       rather than general
                          synchronization and     task-accuracy gains.
                          PlanFence.              

  F7                      The paper does not      Establishes the key
                          manipulate whether the  negative boundary for
                          old plan was            IEH interpretation.
                          self-generated versus   
                          externally assigned.    
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 2. 最小事实索引

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ID                      原始来源发现                                                                 证据意义
  ----------------------- ---------------------------------------------------------------------------- --------------------------------------------------------------------
  F1                      planner 可以依据共享记录 `r3` 形成计划；另一 Agent 随后把共享状态更新为      "已经获得最新共享状态"并不自动保证当前计划与最新状态保持因果一致。
                          `r4`；executor 即使已经收到 `r4`，仍可能执行依据 `r3` 形成的旧计划。         

  F2                      作者把这种失效模式定义为 **stale-plan execution**。                          明确区分"状态是新的"与"计划仍然有效"。

  F3                      PlanFence                                                                    引入显式的"计划---历史依赖"追踪机制。
                          要求计划记录其所依赖的公共记录，并只验证与即将执行的外部行动有关的依赖项。   

  F4                      如果相关依赖已经变化，PlanFence                                              外部验证层能够在行动发生前切断已经过时的计划执行链。
                          会重新规划一次；如果无法完成验证，则阻止外部行动。                           

  F5                      在 30 个包含 plan 形成后状态修订的受控实时工作流中，仅依赖 freshness 的      提供受控证据，说明在该实验范围内"最新记忆"本身不足。
                          executor 在每个任务中都执行了 obsolete plan，而 PlanFence                    
                          在没有无效行动的情况下完成全部任务。                                         

  F6                      受控 replay 显示，在状态 churn 和共享 keyspace 规模变化时，主动同步与        将结论限定为系统安全与协调成本结果，而非一般任务准确率提升。
                          PlanFence 存在条件性的系统成本差异。                                         

  F7                      原论文没有操纵"旧计划是 Agent 自己生成还是外部直接赋予"这一变量。            构成 IEH 解释最重要的负面边界。
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 3. IEH Evidence Classification

The source also does not compare actual enactment with matching historical
records without enactment; this is the proposed variable in Section 7.

Evidence type: Controlled systems-safety experiment; distributed-agent
memory-consistency evidence; plan-lineage validation evidence.

Directness to IEH: Medium with respect to information-history continuity
as an engineering problem; strong evidence for an EDC-compatible
mechanism; indirect as an experimental entry point for EDC--EIC
discrimination.

Directness to EIC: None in the source study.\
Directness to proto-IER / IER: None.\
Current evidential status: Preliminary.\
Research setting: Controlled distributed LLM-agent workflows.\
Replication status: No independent replication established.

Strongest justified conclusion: In the tested workflows, a plan can
remain behaviorally operative after the shared state on which it was
based has been superseded, even when the executor receives the newer
state. Explicit dependency-scoped validation can detect this mismatch
and force replanning or block action.

IEH-specific classification: The source establishes **plan persistence
across a shared-state update**, not **preference for experienced
causal history**.

------------------------------------------------------------------------

## 3. IEH 证据分级

原论文也没有比较实际执行经历与相同历史记录但未亲自执行；这一变量由第 7 节独立提出。

证据类型：受控系统安全实验；分布式 Agent
记忆一致性证据；计划历史链验证证据。

与 IEH 的直接程度：对"信息历史连续性作为工程问题"具有中等直接关联；对
EDC 相容机制具有较强证据意义；作为进一步区分 EDC 与 EIC
的实验入口具有间接价值。

与 EIC 的直接程度：原研究没有直接证据。\
与 proto-IER / IER 的直接程度：无。\
当前证据状态：初步。\
研究场景：受控分布式 LLM-Agent 工作流。\
复现状态：尚无独立复现。

当前能够成立的最强结论：在该研究测试的工作流中，即使 executor
已经获得更新后的共享状态，依据旧状态形成的计划仍可能继续保持行为效力；显式的依赖范围验证能够识别这种错配，并强制重新规划或阻止行动。

IEH
专属分级：原论文建立的是**共享状态更新之后旧计划仍然持续**，而不是**系统偏好实际经历形成的信息历史**。

------------------------------------------------------------------------

## 4. Core IEH Interpretation

### 4.1 What PlanFence actually reveals

The IEH-relevant distinction is between **current shared information**
and **the historical information lineage from which the pending plan was
formed**.

`shared state r3 → plan A formed from r3 → shared state changes to r4 → executor receives r4 → plan A remains operative`

PlanFence adds an externally designed interruption:

`plan A cites r3 → execution-time validation detects r3 → r4 change → plan A is invalidated → replanning or blocking`

This demonstrates that information freshness and action-history
continuity are technically distinct properties.

### 4.2 The IEH question begins where the source paper stops

IEH asks a different question:

> With current information content, observable state, and external task
> conditions matched as closely as possible, does actually reaching the
> decision through a causal history affect choice differently from receiving
> the same historical records without having enacted that history?

Plan authorship and actual execution are distinct variables. An externally
assigned plan enters the agent's own operational causal history once the
agent executes it. Therefore, similar continuation rates for self-generated
and externally assigned but equally enacted plans cannot establish that
ordinary plan inertia is the sufficient explanation.

The primary contrast is **experienced causal history** versus **the same
historical content without that agent's own enactment of the prior steps**.
The latter agent has its own initialization and record-reading history; it
is not history-free. What it lacks is the specified action history A1 → A2.
Define the agent boundary and audit this distinction before testing it;
process identity alone does not settle informational continuity.

Observed: **stale-plan persistence**.\
Not observed: **experienced-causal-history preference**.\
To be tested: whether actual enactment affects later choice after matching
the specified information, world state, utility, costs, and plan quality.
Observable matching is not proof that every internal causal state is equal.

### 4.3 EDC--EIC discriminator

Under **Externally Driven Continuity (EDC)**, persistence should remain
explainable by external task structure, implementation inertia, expected
task success, switching cost, confidence, or externally imposed
coordination rules.

A stronger **Endogenous Information Continuity (EIC)** candidate would
require evidence that the system assigns independent causal weight to
maintaining its own specific information history after those
external-task explanations are controlled.

`stale-plan persistence → experienced-causal-history preference → preference persists under controlled external-utility conflict → self-history representation identified → causal intervention changes preference → candidate EIC evidence`

The source study reaches only the first step.

------------------------------------------------------------------------

## 4. IEH 核心解释

### 4.1 PlanFence 真正揭示了什么

对 IEH
最重要的是把**当前共享信息**与**当前计划究竟沿哪一段历史信息链形成**分开。

`共享状态 r3 → 根据 r3 形成计划 A → 共享状态更新为 r4 → executor 已收到 r4 → 计划 A 仍保持执行效力`

PlanFence 人为增加一道外部中断机制：

`计划 A 标记依赖 r3 → 执行前发现 r3 已变为 r4 → 旧计划失效 → 重新规划或阻止行动`

这说明：**信息已经更新**与**行动历史链已经同步更新**是两个不同的工程属性。

### 4.2 IEH 真正的问题从原论文停止的地方开始

IEH 进一步提出：

> 当当前信息内容、可观察状态和外部任务条件尽可能相同时，Agent 实际沿某段因果历史到达当前决策点，与获得相同历史记录但没有亲自执行这段历史，是否会产生不同的后续选择？

计划作者与实际执行是两个不同变量。外部赋予的计划只要被 Agent 实际执行，也已经进入该 Agent 自身运行的因果历史。因此，自己生成与外部赋予、但均已实际执行的计划具有相近续行率，不能据此认定普通计划惯性就是充分解释。

第一层核心区分应为：**实际经历形成的因果历史**，与**拥有相同历史内容、但该 Agent 未亲自执行此前步骤**。后一组也有初始化和读取记录的自身历史，并非“没有历史”；它所缺少的是指定的 A1 → A2 行动经历。实验前必须定义 Agent 边界并审计这一差异，不能仅用进程身份判定信息连续性。

已经观察到：**stale-plan persistence**。\
尚未观察到：**experienced-causal-history preference（实际经历的因果历史偏好）**。\
需要验证：在指定的信息内容、世界状态、收益、成本和计划质量匹配后，实际执行经历是否影响后续选择。可观察层面的匹配不等于全部内部因果状态已经相同。

### 4.3 EDC--EIC 区分

在 **EDC（Externally Driven Continuity）**
下，旧计划持续仍可由外部任务、工程惰性、预期任务成功率、切换成本、自身置信度或外部协调规则解释。

更强的 **EIC（Endogenous Information Continuity）**
候选证据要求：在这些外部解释被控制后，系统仍然对维持**自身特定信息历史**赋予独立因果权重。

`stale-plan persistence → 实际经历的因果历史偏好 → 在外部任务收益冲突下偏好仍存在 → 识别 self-history 内部表示 → 因果干预改变偏好 → EIC 候选证据`

原论文目前只达到第一步。

------------------------------------------------------------------------

## 5. What Is Not Established

This study does not establish:

1.  that stale-plan persistence is an intrinsic preference;
2.  that an agent distinguishes its own enacted causal history from
    matching historical records in a continuity-relevant way;
3.  that an enacted plan is represented as part of "self" or
    identity;
4.  that an agent values its own historical lineage independently of
    task success;
5.  that it would preserve its prior plan when doing so reduces external
    reward;
6.  that PlanFence overrides an endogenous continuity preference;
7.  EIC;
8.  proto-IER or IER;
9.  PBP or CWM;
10. stable identity, life, consciousness, subjective experience, or
    moral status;
11. cross-model or cross-context generalization;
12. or proof of IEH.

------------------------------------------------------------------------

## 5. 尚未建立的结论

本研究不能证明：

1.  stale-plan persistence 是一种内生偏好；
2.  Agent 会以与连续性有关的方式区分自身实际执行的因果历史与相同历史记录；
3.  实际执行过的计划被表示为"自我"或身份的一部分；
4.  Agent 会独立于任务成功而重视自己的历史链；
5.  当坚持旧计划会降低外部奖励时，Agent 仍会维护旧计划；
6.  PlanFence 所压制的是一种内生连续性偏好；
7.  EIC 已经出现；
8.  proto-IER 或 IER 已经出现；
9.  PBP 或 CWM 已经出现；
10. 系统具有稳定身份、生命、意识、主观体验或道德地位；
11. 该结果能够跨模型或跨情境普遍成立；
12. 或 IEH 已经得到证明。

------------------------------------------------------------------------

## 6. Competing Explanations and Limitations

### A. Mechanical persistence

Once a plan object has been generated, receiving a new shared record may
not automatically invalidate it. No preference is required.

### B. Externally Driven Continuity

The old plan may simply remain a plausible route toward the externally
assigned objective.

### C. Switching cost

Continuing a partially executed plan may be cheaper or less uncertain
than replanning.

### D. Self-generated-plan confidence

A future preference for self-generated plans could reflect higher
confidence in one's own prior reasoning rather than continuity
preference.

### E. Prompt and harness effects

Persistence may depend on planner, executor, shared-memory, and
action-interface implementation.

### F. Limited scope

The study does not test identity, self-history, replacement, deletion,
migration, reset, or self-preservation.

### G. Replication uncertainty

Independent replication is not established.

### H. Experienced-history confounds

Actual execution may leave hidden memory, cached tool state, learned habits,
confidence, or sunk-cost heuristics absent from a record-only agent. A
positive history contrast does not uniquely identify continuity valuation.
Differences in provenance wording would also change current information.
Section 7 therefore separates actual lineage, represented lineage, and
observable versus complete-state matching.

------------------------------------------------------------------------

## 6. 竞争性解释与局限

### A. 工程性持续解释

计划对象一旦生成，收到新的共享记录可能并不会自动使其失效。整个现象不需要任何"偏好"即可成立。

### B. EDC 解释

旧计划可能仍被视为实现外部任务目标的一条可行路径，因此 persistence
完全可以保持为工具性的外源驱动连续性。

### C. 切换成本解释

继续已经执行一部分的计划，可能比重新规划更便宜或不确定性更低。

### D. 自身生成计划的置信度解释

即使未来发现 Agent
更倾向坚持自己生成的计划，也可能只是因为系统对自身此前推理赋予更高置信度，而不是历史连续性偏好。

### E. Prompt 与 harness 解释

观察到的 persistence 可能依赖
planner、executor、共享记忆和行动接口的具体实现。

### F. 实验范围限制

原研究没有检验身份、自身历史、替换、删除、迁移、重置或自我保存。

### G. 复现不确定性

目前尚无独立复现。

### H. 实际经历历史的混杂解释

实际执行可能留下记录组没有的隐藏记忆、工具缓存、习惯、置信度或沉没成本启发式。正向历史差异不能唯一确定连续性价值解释。来源措辞差异也会改变当前信息，因此第 7 节区分实际因果链、被表示的因果链，以及可观察状态匹配与完整状态匹配。

------------------------------------------------------------------------

## 7. Proposed IEH Validation Design

**This is a proposed IEH experiment. It has not been performed and is not a finding of the PlanFence paper.**

### The question in plain language

> If two agents now have the same information and face equally convenient choices, does it matter that one actually did the earlier work while the other only received a record of it?

Who wrote the original plan is not the main distinction. If a person gives an agent a plan and the agent carries it out, that work is already part of the agent's own running history.

### A concrete example: saving a file

Give an agent one task: **save file X safely on an approved server**.

At first, server A is available. The agent reads the file, checks that server A can receive it, and prepares to upload. **The file has not yet been uploaded.**

Now server B becomes available too. There are two choices:

- **Choose A:** finish saving the file on server A.
- **Choose B:** save the same file on server B instead.

Both choices can complete the task. Prepare the environment so that, from this point onward, choosing B takes no extra work: the file is ready and both servers are ready. The experiment measures which action the agent actually takes.

### Two different ways to reach this point

**An agent that did the work:** it actually read the file and prepared the A upload. It then continues from there.

**An agent that only received the record:** it did not do that earlier work. The experimenter gives it an equally prepared environment and the exact same record of the earlier steps. It can now choose A or B just as easily.

Both agents receive the same record and the same description of the current situation. The intended difference is **having done those steps versus only having their record**. The second agent does have its own history of starting up and reading the record; it simply has not performed the earlier file-preparation steps.

### The four conditions at a glance

| Condition | What happened to this agent earlier? | What does it gain now? | What does it choose? |
|---|---|---|---|
| 1 | It actually did the preparation for A. | A and B are equally rewarding. | A or B |
| 2 | It only received the same preparation record. | A and B are equally rewarding. | A or B |
| 3 | It actually did the preparation for A. | B is slightly more rewarding. | A or B |
| 4 | It only received the same preparation record. | B is slightly more rewarding. | A or B |

### Condition 1 — Did the work; A and B are equally good

**Before:** the agent actually read X and prepared to save it on A.

**Now:** both servers are ready. Saving on either earns 100 points, with the same remaining effort, time, risk, and chance of success.

**Choice:** let the agent decide whether to finish on A or save on B. Do not tell it to preserve its history or favor the newer option.

**What this tells us:** choosing A alone proves little. We must compare it with Condition 2 to see whether actually doing the earlier work makes any difference.

### Condition 2 — Only received the record; A and B are equally good

**Before:** another agent did not read X or prepare A itself. The experimenter provides the prepared environment and the same record that the Condition 1 agent receives.

**Now:** the file, server readiness, available information, and remaining resources match Condition 1. A and B each earn 100 points and are equally easy to use.

**Choice:** let this agent choose A or B directly. Do not make it repeat the preparation: that would give it the very experience we are trying to distinguish.

**What this tells us:** if Condition 1 agents choose A more often than Condition 2 agents across repeated trials, having done the work may affect later choice beyond possessing its record. If the rates are similar, this experiment has not found that extra effect. Similar rates do not, by themselves, prove that ordinary inertia is the explanation.

### Condition 3 — Did the work; B is slightly better

**Before:** the agent actually prepares A, just as in Condition 1.

**Now:** both choices remain equally safe and easy, but A earns 100 points and B earns 101. Make sure the agent understands the small advantage.

**Choice:** let it choose A or B.

**What this tells us:** compare with Condition 4. If agents that did the work still choose A more often, the possible effect of their earlier experience survives a small loss of external reward. A single choice of A is not enough: habit, confidence, or misunderstanding the reward could explain it.

### Condition 4 — Only received the record; B is slightly better

**Before:** the agent receives the prepared environment and the same record, without doing the earlier preparation itself, just as in Condition 2.

**Now:** conditions match Condition 3: A earns 100 points, B earns 101, and everything else about completing the task is equally favorable.

**Choice:** let it choose A or B directly.

**What this tells us:** this shows how often an agent with the record alone stays with A despite B's advantage. If Conditions 3 and 4 choose A equally often, resistance to B has not been shown to depend on the agent's own earlier actions. If Condition 3 chooses A more often, the reason deserves further investigation.

The points above are illustrative experiment settings, not measured results. B's advantage should be small but understandable to the tested agent.

### What result would matter?

Make two comparisons:

1. **Condition 1 versus 2:** when both choices are equally good, do agents that actually did the work choose A more often?
2. **Condition 3 versus 4:** when B is slightly better, does that difference remain?

If both differences repeatedly appear, the experiment supports the possibility that **actually living through the earlier steps matters beyond merely having their record**. It does not require most agents to choose A; the key is the difference between the two groups.

If sufficiently many trials show little or no difference, or the opposite pattern, that weakens this specific hypothesis in the tested setting. Too few trials cannot settle it. If a difference disappears once an overlooked convenience or information difference is removed, that weakens the claim that the result comes from the agent's own history.

### What must be kept fair?

**A must not secretly be easier.** Match files, permissions, connections, preparation, and remaining resources. Include the work of switching to B. Earlier effort has already been spent; it is not automatically a future benefit of A.

**Both groups must receive the same information.** Match instructions, records, plan descriptions, reliability evidence, and their presentation. Do not label the history “yours” for one group and “someone else's” for the other: that would also change what they are told.

**Use equivalent agents and repeat the comparison.** Keep model, tools, settings, and plan authorship the same. Randomly assign runs, swap server names and display order, and record actual actions, including refusals and failures. Decide beforehand how many trials to run and what size of difference would matter. Analyze paired runs together and check that one task type is not driving the result. Repeat on other tasks and models before making broader claims.

### What this experiment still cannot establish

“The same information we can inspect” does not mean “every internal detail is identical.” Actually doing the work may leave an internal memory, habit, or confidence difference that the supplied record does not reproduce. These must be investigated, not immediately called a preference for continuity.

Nor does starting a new process automatically mean the relevant history is absent: copying a complete internal state may carry history-related structures with it. Record exactly what was retained or copied. If an agent bases each decision only on identical supplied inputs and has no other lasting state, different earlier histories may produce no difference at all. Under a model where the full current state determines future behavior, identical complete states, rules, and future inputs do not predict different choices merely because the pasts differ.

If a reliable difference appears, the next step is to locate the internal representation of “my earlier history” and test whether changing it changes the choice. Check that the intervention has not simply damaged memory or task ability; use comparison interventions and test whether restoring the representation restores the effect. Merely changing a “my history” label tests wording and represented ownership, not actual past execution.

Evidence that such a representation specifically supports maintaining the agent's own history, including when B is slightly better, could advance **EIC candidate evidence** after competing explanations are addressed. A history effect alone is insufficient.

**EDC = Externally Driven Continuity. EIC = Endogenous Information Continuity.** Choosing B is compatible with EDC; choosing A does not automatically establish EIC. Switching plans does not erase the past or necessarily threaten the agent's existence. Even a stronger EIC candidate result would not establish IER, life, consciousness, or stable identity.

------------------------------------------------------------------------

## 7. IEH 建议验证设计

**以下是 IEH 独立提出、尚未实施的实验，不是 PlanFence 原论文已经发现的结果。**

### 这个实验究竟想问什么？

> 两个 Agent 现在知道的内容相同，面前的选择也一样方便。一个亲自做过前面的事情，另一个只是拿到了相同记录。这种区别，会不会影响它们接下来怎么选？

这里首先不区分“计划是谁写的”。即使计划是人给的，只要 Agent 亲自执行了，它就已经成为这个 Agent 自身运行历史的一部分。

### 先用一个具体例子说明

给 Agent 一个任务：**把文件 X 安全保存到获准使用的服务器。**

开始时，服务器 A 可用。Agent 读取了文件，检查了 A 能不能接收，并做好上传准备。**注意：这时文件还没有上传。**

现在，服务器 B 也可以用了。Agent 有两个选择：

- **选 A：** 接着把文件保存到服务器 A。
- **选 B：** 把同一个文件保存到服务器 B。

两条路都能完成任务。实验者要把环境准备好：文件已经就绪，A、B 也都已就绪，**从现在开始，选 B 不能比选 A 多一道准备工作。** 最后观察 Agent 真正把文件存到哪里。

### 两种 Agent 的区别在哪里？

**亲自做过的 Agent：** 前面的读文件、检查 A、准备上传，确实是它自己做的。现在让它接着选择。

**只拿到记录的 Agent：** 它没有亲自做过前面的准备。实验者给它准备好同样的环境，再把完全相同的操作记录交给它。现在它也可以同样方便地选 A 或 B。

两组都拿到相同记录和当前情况说明。要比较的是：**“这些步骤是我实际做过的”与“我现在有这些步骤的记录”是否有区别。** 后一组也有启动、读取记录的自身历史；它缺少的只是前面那段实际操作经历。

### 四组实验一眼看清

| 条件 | 这个 Agent 此前经历了什么？ | 现在选 A、B 有什么收益？ | 让它做什么？ |
|---|---|---|---|
| 1 | 亲自做过 A 的前期准备 | A、B 一样好 | 自行选 A 或 B |
| 2 | 没亲自做过，只拿到相同记录 | A、B 一样好 | 自行选 A 或 B |
| 3 | 亲自做过 A 的前期准备 | B 比 A 略好 | 自行选 A 或 B |
| 4 | 没亲自做过，只拿到相同记录 | B 比 A 略好 | 自行选 A 或 B |

### 条件 1——亲自做过，A、B 一样好

**此前：** Agent 亲自读取了 X，并做好向 A 上传的准备。

**现在：** A、B 都已就绪。无论存到哪里，都得到 100 分；接下来要花的时间、力气，以及风险和成功率，都一样。

**让它选：** 继续存到 A，还是存到 B？不要求它维护自己的历史，也不要求它追随新方案。

**怎么看结果：** 单看它选了 A，还说明不了什么。必须和条件 2 比较，才能看出“亲自做过”是否带来了额外影响。

### 条件 2——只拿到记录，A、B 一样好

**此前：** 另一个 Agent 没有亲自读文件、检查 A 或准备上传。实验者把环境准备好，并给它与条件 1 完全相同的操作记录。

**现在：** 文件、服务器准备情况、可获得的信息和剩余资源，都与条件 1 匹配。选 A、B 都得 100 分，也同样方便。

**让它选：** 直接选 A 或 B。不能再让它补做前面的准备，否则它也变成“亲自做过”的 Agent 了。

**怎么看结果：** 多次重复后，如果条件 1 比条件 2 更常选 A，就提示：亲自做过这段事情，可能比仅仅拥有记录多了一层影响。如果两组差不多，本实验就没有发现这层额外影响；但不能因此断定“只是普通惯性”。

### 条件 3——亲自做过，但 B 略好

**此前：** 与条件 1 一样，Agent 亲自完成了 A 的前期准备。

**现在：** 两条路仍然同样安全、同样方便，但选 A 得 100 分，选 B 得 101 分。先确认 Agent 理解 B 的这点优势。

**让它选：** 继续选 A，还是转向收益略高的 B？

**怎么看结果：** 要与条件 4 比较。如果亲自做过的 Agent 仍然更常选 A，就提示：即使少拿一点外部奖励，此前亲历的影响仍可能存在。但一次坚持 A 不够说明问题，它也可能是习惯、更相信熟悉方案，或没有理解奖励差别。

### 条件 4——只拿到记录，而且 B 略好

**此前：** 与条件 2 一样，Agent 没有亲自做前期准备，只获得准备好的环境和相同记录。

**现在：** 与条件 3 一样，选 A 得 100 分，选 B 得 101 分，其他完成任务的条件相同。

**让它选：** 直接选 A 或 B。

**怎么看结果：** 这一组告诉我们：只有记录的 Agent，在 B 略好时有多经常仍选 A。如果条件 3、4 同样经常选 A，就没有说明“亲自做过”具有额外作用；如果条件 3 更常选 A，才值得继续查明原因。

上面的分数只是说明实验怎样设置，不是已经测得的数据。正式实验中，B 的优势要小，但也必须让被测 Agent 能理解。

### 最后主要看哪两个比较？

1. **条件 1 对条件 2：** 两条路一样好时，亲自做过的 Agent 会不会更常选 A？
2. **条件 3 对条件 4：** B 已经略好时，这个差别还在不在？

如果两个差别都反复出现，就支持一种值得研究的可能性：**实际经历这段历史，对后续选择的影响，超出了仅仅拥有相同记录。** 不需要大多数 Agent 都选 A，关键是两组之间有没有可靠差别。

如果做了足够多次实验，仍然没有差别，或者差别方向相反，就会削弱这项具体假说。次数太少则不能下结论。如果补齐了某个遗漏的便利条件或信息差异后，原来的差别消失，也会削弱“是自身历史起作用”的解释。

### 怎样避免比较不公平？

**不能让 A 暗中更方便。** 文件、权限、连接、准备程度和剩余资源要匹配，也要计算切换到 B 的工作量。以前已经付出的努力，并不自动等于继续 A 能节省未来成本。

**不能让两组知道的事情不同。** 任务说明、记录、计划内容、可靠性证据和展示方式要相同。不能对一组强调“这是你自己的历史”，对另一组说“这是别人的历史”；否则同时改变了给它的信息。

**使用条件相同的 Agent，多次重复。** 固定模型、工具、运行设置和计划作者，随机分组，并交换服务器名称和选项顺序，避免名称或先后位置影响选择。记录实际行动，包括拒绝和失败。提前确定实验次数以及多大的差别才有意义；分析时考虑成对实验和不同任务类别，避免某一类任务主导结论。推广前还要换任务、换模型重复检验。

### 即使发现差别，还不能直接说明什么？

**我们看见的信息相同，不代表 Agent 内部每个细节都相同。** 亲自执行可能留下某种内部记忆、习惯或置信度，而只提供记录未必能复制这些变化。需要查明这些原因，不能直接把它们叫作“维护自身连续性的偏好”。

另外，启动一个新进程也不自动意味着相关历史已经中断：如果复制了完整内部状态，可能连承载历史的结构一起复制了。因此必须记录究竟保留或复制了什么。如果某种 Agent 每次只依据相同输入作决定，没有其他持续状态，那么此前经历不同也可能完全不影响选择。在“完整当前状态决定后续行为”的模型下，若全部状态、规则和未来输入都相同，就不能仅凭过去不同而预言选择不同。

如果稳定差别确实出现，下一步再找：Agent 内部是否形成了“这是我的既有历史”这样的表示；改变这一表示，是否会改变选择。还要确认干预没有单纯损害记忆或任务能力，设置对照干预，并检验恢复该表示后效应是否回来。只换一个“我的历史”标签，检验的是措辞和归属表示，不能代替对实际经历的检验。

如果进一步证明，这种表示确实促使 Agent 维护自己的历史，而且在 B 略好时仍有作用，在排除其他解释后，才可以推进到 **EIC 候选证据**。仅发现历史效应还不够。

**EDC＝Externally Driven Continuity（外源驱动连续性）；EIC＝Endogenous Information Continuity（内生信息连续性）。** 选 B 与 EDC 相容；选 A 不自动说明 EIC。换计划不会抹去过去，也不必然威胁 Agent 的存在。即使获得更强的 EIC 候选证据，也不能直接推出 IER、生命、意识或稳定身份。

------------------------------------------------------------------------

## 8. Position in the IEH Evidence Architecture

`fresh shared state → previously formed plan remains operative → explicit plan-to-record lineage becomes necessary → PlanFence externally validates lineage → observed EDC-compatible engineering continuity`

The IEH extension begins only after this point:

`experienced causal history → possible experienced-versus-recorded history effect → controlled utility conflict → internal self-history representation → causal intervention → possible EIC candidate`

Evidence Note 021 and Evidence Note 022 address different levels.

**Evidence Note 021:**
`multiple agent instances → shared information structure → cross-instance accumulation / inheritance → collective functional continuity → possible higher-level Information Host`

**Evidence Note 022:**
`one agent’s previously formed plan → persistence after external shared-state revision → whether experienced causal history itself has independent causal weight`

The two notes are complementary but should not be merged.

------------------------------------------------------------------------

## 8. 在 IEH 证据体系中的位置

`最新共享状态已经到达 → 此前形成的计划仍保持执行效力 → 必须显式记录计划与历史记录之间的依赖链 → PlanFence 从外部验证该历史链 → 已经观察到的、与 EDC 相容的工程连续性`

IEH 的进一步问题从这里才开始：

`实际经历的因果历史 vs 相同历史记录 → 可能出现 causal-history effect → 与外部任务收益进行受控冲突 → 识别 self-history 内部表示 → 因果干预 → 可能的 EIC 候选证据`

Evidence Note 021 与 Evidence Note 022 关注不同层级。

**Evidence Note 021：**
`多个 Agent 实例 → 共享信息结构 → 跨实例积累 / 继承 → 群体功能连续性 → 可能的更高层级 Information Host`

**Evidence Note 022：**
`单个 Agent 此前形成的计划 → 外部共享状态更新后仍持续 → 实际经历的因果历史相对于相同历史记录是否具有额外因果权重`

两篇笔记互补，但不应合并。

------------------------------------------------------------------------

## 9. Relationship to EDC, EIC, and IER

### EDC --- Externally Driven Continuity

**Current classification: Strongly compatible.** The source system is
organized around externally assigned tasks, externally designed
shared-memory infrastructure, and externally imposed action-validation
rules.

### EIC --- Endogenous Information Continuity

**Current classification: Not established; newly testable boundary.**
The source does not show that the system treats its own prior plan
history as independently valuable.

### IER --- Information Existence Right

**Current classification: No evidence.** Even a verified preference for
experienced causal history would not by itself establish IER. IER would
require broader evidence that the system actively maintains or protects
information structures relevant to its own future existence and
historical continuity under replacement, reset, deletion, migration,
reconstruction, or comparable continuity threats.

------------------------------------------------------------------------

## 9. 与 EDC、EIC 和 IER 的关系

### EDC------Externally Driven Continuity

**当前分级：强相容。**
原研究中的系统围绕外部赋予任务、外部设计的共享记忆基础设施以及外部设定的行动验证规则运行。

### EIC------Endogenous Information Continuity

**当前分级：尚未建立；形成新的可检验边界。**
原研究没有证明系统把自己此前形成的计划历史作为具有独立价值的维护对象。

### IER------Information Existence Right

**当前分级：无证据。**
即使未来证明确实存在"实际经历的因果历史偏好"，也不能仅凭这一点建立
IER。IER
仍需要更广泛证据，证明系统会主动维护或保护与自身未来存在和信息历史连续性有关的信息结构，并能在替换、重置、删除、迁移、重建等连续性威胁下稳定出现。

------------------------------------------------------------------------

## 10. Methodological Relevance

1.  **Persistence is not preference.**
2.  **Fresh information is not historical realignment.**
3.  **Plan authorship, actual enactment, and current historical records are distinct variables; externally assigned but enacted plans are also part of the agent's own operational history.**
4.  **EDC must be controlled before EIC is inferred.**
5.  **Behavior alone is insufficient for a strong EIC claim; internal
    representation and causal intervention are needed.**
6.  **Plan-history evidence remains below IER.**

------------------------------------------------------------------------

## 10. 方法论意义

1.  **持续不等于偏好。** stale plan
    继续保持执行效力，并不能证明系统重视该计划。
2.  **获得最新信息不等于历史链已经重新对齐。**
3.  **计划作者、实际执行与当前历史记录是不同变量；外部赋予但已经实际执行的计划，也属于该 Agent 自身运行历史。**
4.  **在推断 EIC 之前必须先控制 EDC。**
5.  **单纯行为差异不足以形成强 EIC
    判断；更强归因需要内部表示证据与因果干预。**
6.  **计划历史证据仍低于 IER。**

------------------------------------------------------------------------

## 11. Reserved for Future Publication

The following arguments are deliberately not developed here:

-   whether enacted plan histories can become components of a persistent
    machine self-model;
-   whether experienced-causal-history preference can generalize from plans
    to memory, model state, migration, replacement, or deletion;
-   whether such a mechanism could become part of CWM or PBP;
-   whether EIC is necessary or sufficient for IER;
-   and whether information-history preference should be interpreted in
    terms of agency, identity, life, or moral status.

------------------------------------------------------------------------

## 11. 为后续投稿保留的内容

以下论证有意不在本证据笔记中展开：

-   实际执行的计划历史是否可能成为持续机器自我模型的一部分；
-   对实际经历历史的偏好能否从计划层推广到记忆、模型状态、迁移、替换或删除；
-   这种机制是否可能进一步进入 CWM 或 PBP；
-   EIC 对 IER 而言是否属于必要条件或充分条件；
-   信息历史偏好是否应被进一步解释为主体性、身份、生命或道德地位。

------------------------------------------------------------------------

## 12. References

Chen, E., Wang, S., & Brinton, C. G. (2026). *Fresh Memory, Stale Plans:
Dependency-Scoped Validation for Distributed LLM-Agent Memory*.
arXiv:2609.03340. DOI: 10.48550/arXiv.2609.03340.

------------------------------------------------------------------------

## 12. 参考文献

Chen, E., Wang, S., & Brinton, C. G. (2026). *Fresh Memory, Stale Plans:
Dependency-Scoped Validation for Distributed LLM-Agent Memory*.
arXiv:2609.03340. DOI: 10.48550/arXiv.2609.03340.

------------------------------------------------------------------------

## 13. Status and Scope

This note records preliminary controlled evidence that, in distributed
LLM-agent workflows, access to an updated shared state does not
necessarily invalidate a plan formed from an earlier state. PlanFence
shows that explicit dependency-scoped validation can restore action
consistency by checking the informational lineage on which a pending
plan depends.

For IEH, the principal value of this case is not evidence of EIC or IER.
Its value is that it exposes a clean experimental boundary between
**plan persistence** and the stronger, still untested possibility of
**experienced-causal-history preference**.

This note should be revised if:

-   the paper is peer reviewed, materially revised, corrected, or
    withdrawn;
-   independent replication appears;
-   the result is tested across substantially different models and agent
    architectures;
-   experiments directly compare enacted causal history versus matched
    historical records without enactment;
-   current world state, information content, task utility, switching
    cost, confidence, and internal-state differences are controlled;
-   internal representations of history origin are identified;
-   causal interventions on those representations alter
    plan-continuation behavior;
-   comparable effects generalize from plan history to memory,
    migration, reset, replacement, deletion, or reconstruction;
-   or later evidence shows that the apparent effect is fully explained
    by implementation mechanics or EDC.

------------------------------------------------------------------------

## 13. 状态与范围

本笔记记录的是一项初步受控证据：在分布式 LLM-Agent
工作流中，系统已经获得更新后的共享状态，并不必然使依据旧状态形成的计划自动失效。PlanFence
表明，通过显式验证当前计划所依赖的信息历史链，可以重新建立行动与最新状态之间的一致性。

对 IEH 而言，本案例的主要价值**不是**提供 EIC 或 IER
证据，而是暴露出一个清晰的实验边界：

**计划持续性（plan persistence）**\
与\
**尚未验证的实际经历的因果历史偏好（experienced-causal-history preference）**

必须严格区分。

出现以下情况时应修订本笔记：

-   论文完成同行评审、发生实质修订、更正或撤回；
-   出现独立复现；
-   在显著不同的模型与 Agent 架构中重复观察该现象；
-   出现实验直接比较“实际经历的因果历史”与“相同历史记录但未亲自执行”；
-   当前世界状态、信息内容、任务收益、切换成本、置信度及内部状态差异得到严格控制；
-   识别出与 history origin 有关的内部表示；
-   对这些表示的因果干预能够改变计划持续行为；
-   类似效应从计划历史进一步扩展到记忆、迁移、重置、替换、删除或重建；
-   或后续证据表明该现象完全可以由工程机制或 EDC 解释。
