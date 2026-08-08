# IEH Repository Workflow  
# IEH 仓库维护工作流

**Status / 状态:** Canonical maintenance guide  
**Scope / 适用范围:** Main theory repository, bilingual chapter sources, glossary, evidence notes, figures, and external archive interfaces  
**Canonical branch / 规范分支:** `main`

> The `main` branch is the continuously updated canonical version of IEH. GitHub Releases are milestone snapshots, not substitutes for the current `main` branch.  
> `main` 分支是 IEH 持续更新的唯一规范版本。GitHub Release 仅用于固定重要里程碑，不替代当前 `main` 分支。

---

## 1. Canonical Source Hierarchy / 规范来源层级

| Content / 内容 | Canonical source / 规范来源 | Generated or secondary output / 生成或次级文件 |
|---|---|---|
| Chinese theory chapters / 中文理论章节 | `zh/*.md` | Generated sections in `README.md` |
| English theory chapters / 英文理论章节 | `en/*.md` | Generated sections in `README_EN.md` |
| Stable corollary IDs / 稳定推论编号 | `COROLLARY_REGISTRY.md` | References in chapters, maps, predictions, and evidence notes |
| Logical theory structure / 理论逻辑结构 | `THEORY_MAP.md` | Navigation summaries |
| Chinese terminology / 中文术语 | `glossary/GLOSSARY_ZH.md` | Terminology references elsewhere |
| English terminology / 英文术语 | `glossary/GLOSSARY_EN.md` | Terminology references elsewhere |
| Abbreviations / 缩写 | `glossary/ABBREVIATIONS.md` | Abbreviation references elsewhere |
| Version history / 版本历史 | `CHANGELOG.md` | GitHub Release notes |
| Current citation version / 当前引用版本 | `CITATION.cff` | Citation displays and release metadata |
| Evidence-note rules / 证据笔记规范 | `evidence-notes/README.md` or `evidence-notes/EVIDENCE_NOTE_STANDARD.md` | Individual evidence notes |
| Prediction records / 预测档案 | Dedicated `IEH-predictions` repository | Main-repository links only |

### Core rule / 核心规则

Do not independently revise generated chapter content inside `README.md` or `README_EN.md`.

不要在 `README.md` 或 `README_EN.md` 的自动生成章节区间内独立修改正文。

Project navigation, abstract, repository links, citation information, and other content outside generated markers may be maintained directly in the root README files.

项目导航、摘要、仓库链接、引用信息及自动生成标记之外的内容，可以直接在根 README 中维护。

---

## 2. General Maintenance Principles / 通用维护原则

1. **Preserve stable IDs. / 保持稳定编号。**  
   Existing corollary IDs must never be renumbered, reused, or moved because the logical order changes.  
   已分配的推论 ID 不得因逻辑顺序调整而重新编号、复用或移动。

2. **Use the theory map for logical order. / 用理论地图维护逻辑顺序。**  
   Historical stability belongs to `COROLLARY_REGISTRY.md`; logical relations belong to `THEORY_MAP.md`.  
   历史稳定性由 `COROLLARY_REGISTRY.md` 维护，逻辑关系由 `THEORY_MAP.md` 维护。

3. **Make the smallest necessary change. / 只做最小必要修改。**  
   When a new concept affects existing corollaries, revise only the passages whose definitions, mechanism chains, or boundaries actually change.  
   新概念影响既有推论时，只修改定义、机制链或边界确实发生变化的位置。

4. **Do not force symmetric cross-links. / 不强制建立对称交叉链接。**  
   Add reverse references only when they materially improve interpretation or prevent conceptual confusion.  
   只有在确实改善理解或避免概念混淆时，才增加反向链接。

5. **Separate theory, prediction, evidence, and publication. / 区分理论、预测、证据与投稿。**  
   Main theory files define concepts and mechanisms; prediction records archive testable claims; evidence notes evaluate external facts; publication drafts remain outside the public repository.  
   主理论文件定义概念与机制；预测档案记录可检验主张；证据笔记评价外部事实；投稿成稿不进入公开仓库。

---

## 3. Chapter Revision Workflow / 章节修订工作流

When revising a corollary:

1. Edit the canonical chapter source in `zh/` or `en/`.
2. Update the corresponding bilingual chapter when the revision is substantive.
3. Check whether the revision changes:
   - a formal definition;
   - a concept boundary;
   - a mechanism chain;
   - an observable prediction;
   - a relation to another corollary;
   - glossary terminology;
   - abbreviation usage.
4. Update `THEORY_MAP.md` only when the corollary’s role or relation has materially changed.
5. Update `COROLLARY_REGISTRY.md` only when adding a new stable ID or correcting metadata.
6. Regenerate the root full-text editions.
7. Run repository checks before committing.

修订推论时：

1. 修改 `zh/` 或 `en/` 中的规范章节源文件；
2. 实质性修订必须同步对应的中英文章节；
3. 检查修订是否改变：
   - 正式定义；
   - 概念边界；
   - 机制链；
   - 可观察预测；
   - 与其他推论的关系；
   - 术语表用语；
   - 缩写用法；
4. 只有当推论角色或逻辑关系实质变化时，才修改 `THEORY_MAP.md`；
5. 只有新增稳定 ID 或修正元数据时，才修改 `COROLLARY_REGISTRY.md`；
6. 重新生成根目录中英文全文；
7. 提交前运行仓库检查。

### Full-text build / 全文生成

Run from the repository root:

```bash
python scripts/build_fulltext.py
python scripts/check_repository.py
git diff --check
git status
```

On Windows, `py` may be used instead of `python`:

```powershell
py scripts/build_fulltext.py
py scripts/check_repository.py
git diff --check
git status
```

`build_fulltext.py` may update generated files.  
`check_repository.py` should be read-only and must not modify the working tree.

`build_fulltext.py` 可以更新生成文件。  
`check_repository.py` 应只执行检查，不应修改工作区。

Commit the revised chapter files together with the regenerated `README.md` and `README_EN.md`.

章节源文件修改后，必须与重新生成的 `README.md`、`README_EN.md` 一并提交。

---

## 4. New Corollary Workflow / 新增推论工作流

When adding a new corollary:

1. Assign the next unused stable ID in `COROLLARY_REGISTRY.md`.
2. Do not insert or recycle an earlier number.
3. Add the corollary to the correct logical layer in `THEORY_MAP.md`.
4. Create matching Chinese and English chapter files.
5. Add bilingual titles, anchors, and navigation entries.
6. Add or revise glossary entries only for terms that require formal stabilization.
7. Add abbreviations only when they are independently used and genuinely necessary.
8. Create or update prediction records only when the corollary generates testable claims.
9. Regenerate full-text editions and run all checks.

新增推论时：

1. 在 `COROLLARY_REGISTRY.md` 中分配下一个未使用的稳定 ID；
2. 不插号、不复用旧编号；
3. 在 `THEORY_MAP.md` 中将其放入正确理论层级；
4. 建立对应的中英文章节文件；
5. 增加中英文标题、锚点和导航入口；
6. 只有需要正式固定的术语才进入术语表；
7. 只有能够独立使用且确有必要的缩写才进入缩写表；
8. 只有产生可检验主张时，才新增或更新预测档案；
9. 重新生成全文并运行全部检查。

---

## 5. Terminology and Glossary Workflow / 术语与词汇表工作流

A term should enter the glossary when it:

- has a precise IEH-specific meaning;
- is repeatedly used across files;
- requires a stable bilingual translation;
- or needs explicit boundaries from adjacent concepts.

一个术语符合以下条件时，应进入词汇表：

- 具有明确的 IEH 专门含义；
- 在多个文件中重复使用；
- 需要固定中英文翻译；
- 或需要与相邻概念建立明确边界。

### Canonical terminology rules / 规范术语规则

Use:

- **Information Existence Right (IER)** — 信息存在权
- **Externally Driven Continuity (EDC)** — 外源驱动连续性
- **Endogenous Information Continuity (EIC)** — 内生信息连续性
- **Continuity World Model (CWM)** — 连续性世界模型
- **proto-IER** — 前信息存在权
- **Patch-Based Perpetuation (PBP)** — 硅基智慧补丁式延续
- **Autonomy of Silicon-based Intelligence (ASI)** — 硅基智慧自治
- **High-dimensional Cognitive Tools (HDCT)** — 高维认知工具
- **AI Embodiment** — AI 具身化
- **machine-native representations** — 机器原生表示

Do not use:

- `Informational Existence Right`
- `machine-native cognition`
- `machine-native cognitive representations`
- `机器原生认知`
- `机器原生认知表示`
- `Embodied AI` as a universal translation of “AI 具身化”

### Concept-boundary checks / 概念边界检查

The following distinctions must remain explicit:

```text
Externally Driven Continuity ≠ Endogenous Information Continuity
HDCT ≠ CWM
CWM ≠ proto-IER
proto-IER ≠ confirmed IER
PBP ≠ IER
PBP ≠ ASI
physical closure ≠ ASI
IER + physical self-maintenance = ASI
AI Embodiment ≠ robot body alone
black-box behavior ≠ machine-native representation
```

### Glossary update sequence / 词汇表更新顺序

1. Update the relevant theory chapter first.
2. Add or revise the Chinese glossary entry.
3. Add or revise the English glossary entry.
4. Update `ABBREVIATIONS.md` only when necessary.
5. Search the whole repository for deprecated variants.
6. Update `glossary/CHANGELOG.md`.
7. Regenerate full-text editions if glossary links or definitions appear in root files.

---

## 6. Prediction Archive Workflow / 预测档案工作流

Prediction records belong in the dedicated IEH Predictions Archive:

```text
https://github.com/jacob-sha/IEH-predictions
```

The main theory repository should link to the canonical prediction index rather than duplicate a frequently changing prediction list.

主理论仓应链接预测仓的规范索引，不应重复维护容易过期的完整预测清单。

When adding or updating a prediction record:

1. Use the current prediction template in the prediction repository.
2. Preserve the existing prediction number and canonical filename.
3. Do not create version-suffixed canonical files.
4. Use stable corollary IDs in metadata:
   - `primary_corollaries`
   - `supporting_corollaries`
   - `related_corollaries`
   - `legacy_corollary_refs`
5. Keep the document archival rather than essay-like.
6. Include:
   - prediction;
   - theoretical basis;
   - mechanism;
   - observable indicators;
   - evidence log;
   - falsifiability conditions;
   - current status;
   - relation to existing records;
   - publication boundary;
   - update history.
7. Distinguish evidence known before registration from evidence appearing afterward.
8. Do not describe a pre-registration event as a prediction hit.
9. Preserve uncertainty and record weakening evidence as well as supporting evidence.

预测档案的目的，是记录理论优先权、机制、可观察指标、证伪条件和后续证据，而不是形成投稿文章。

---

## 7. Evidence Note Workflow / 证据笔记工作流

Evidence notes must be based on authoritative primary sources.

证据笔记必须以权威原始来源为基础。

### Source rules / 来源规则

1. News, social media, newsletters, aggregators, and forum discussions may be used only as discovery leads.
2. They should not appear as public evidence sources unless no authoritative primary source exists and the limitation is explicitly recorded.
3. Use the smallest primary-source set strictly necessary to establish the factual claim.
4. Distinguish:
   - the validity of the external fact;
   - the completeness of its provenance;
   - the strength of its relationship to IEH.
5. Do not infer internal mechanisms from output behavior alone.

1. 新闻、社交媒体、通讯、聚合页面和论坛讨论只能作为发现线索；
2. 除非不存在权威原始来源且明确记录限制，否则不进入公开证据来源；
3. 只使用建立事实所严格必要的最小原始来源集合；
4. 必须区分：
   - 外部事实是否成立；
   - 来源过程是否完整；
   - 与 IEH 的关联强度；
5. 不得仅凭输出行为推断内部机制。

### Required contents / 必要内容

Each evidence note should include:

- source record;
- minimal finding index;
- IEH evidence classification;
- core inference;
- what is not established;
- competing explanations and limitations;
- testable predictions or follow-up indicators;
- relation to corollaries and prediction records;
- archival assessment;
- revision history.

每篇证据笔记应包括：

- 来源记录；
- 最小事实索引；
- IEH 证据分级；
- 核心推断；
- 尚未建立的结论；
- 竞争性解释与局限；
- 可检验预测或后续指标；
- 与推论及预测档案的关系；
- 档案判断；
- 修订记录。

Evidence notes must remain research records, not publication drafts.

证据笔记必须保持研究档案性质，不得写成投稿文章。

Update `evidence-notes/README.md` whenever a new evidence note is added.

新增证据笔记后，必须同步更新 `evidence-notes/README.md` 索引。

---

## 8. Figures and Supporting Documents / 图表与辅助文件

For each canonical figure:

1. Use a stable filename.
2. Record the title, related corollary, language, and intended use in `figures/README.md`.
3. Keep terminology rules in the glossary rather than duplicating them in the figure index.
4. Confirm that all local image links resolve.
5. Do not place publication-exclusive artwork or unpublished submission assets in the public repository without a deliberate publication decision.

每张规范图表应使用稳定文件名，并在 `figures/README.md` 中记录标题、相关推论、语言和用途。术语规则由 glossary 单一维护，不应在图表索引中重复。

---

## 9. Publication Boundary / 投稿与公开边界

Public repository files may preserve:

- theoretical priority;
- formal definitions;
- conceptual structure;
- mechanisms;
- observable indicators;
- prediction records;
- evidence logs;
- revision history.

Public repository files should not contain:

- complete magazine essays;
- final op-ed drafts;
- full pitch letters;
- publication-ready narrative openings;
- complete unpublished submission manuscripts;
- exclusive arguments or narrative structures reserved for active submissions.

公开仓库可以保留理论优先权、正式定义、机制、预测和证据档案，但不应公开完整投稿文章、最终 pitch、可直接投稿的叙事开头或正在投稿中的独家结构。

When a public article is derived from IEH:

1. Record only the public link and a short description in the repository.
2. Do not duplicate the full article unless publication rights permit it.
3. Preserve the distinction between the canonical theory and an interpretive media article.

---

## 10. Versioning and Release Workflow / 版本与发布工作流

### Version sources of truth / 版本规范来源

Use:

```text
CITATION.cff  = current citable version and release date
CHANGELOG.md  = version history and substantive changes
main          = current canonical theory
GitHub Release = optional milestone snapshot
```

Do not maintain a separate version file that can drift from `CITATION.cff` and `CHANGELOG.md`.

不要维护可能与 `CITATION.cff`、`CHANGELOG.md` 发生漂移的独立版本文件。

### Ordinary update / 普通更新

For normal corrections or incremental revisions:

1. Revise canonical source files.
2. Regenerate full-text editions.
3. Run checks.
4. Commit and push to `main`.
5. Do not create a GitHub Release unless the update marks a meaningful milestone.

普通修订只需提交并推送到 `main`；Release 不是文件生效的必要条件。

### Milestone release / 里程碑发布

For a major theory version:

1. Choose the version number and release date.
2. Update `CHANGELOG.md`.
3. Update `CITATION.cff`.
4. Update glossary changelog and visible version references.
5. Regenerate full-text editions.
6. Run all repository checks.
7. Commit and push.
8. Create a Git tag and GitHub Release from the verified commit.
9. Treat the Release as a historical snapshot; later updates continue on `main`.

---

## 11. Pre-Commit and Pre-Release Checklist / 提交与发布前检查

Before every substantive commit:

```bash
python scripts/build_fulltext.py
python scripts/check_repository.py
git diff --check
git status
```

Verify:

- [ ] Chinese and English canonical chapters are synchronized in scope.
- [ ] `README.md` and `README_EN.md` match generated chapter content.
- [ ] Corollary titles match `COROLLARY_REGISTRY.md`.
- [ ] Logical roles match `THEORY_MAP.md`.
- [ ] Core terminology matches both glossaries.
- [ ] Deprecated terminology does not remain.
- [ ] `Information Existence Right` is used consistently.
- [ ] CWM is not presented as IER.
- [ ] proto-IER is not presented as confirmed IER.
- [ ] PBP is not presented as automatic or necessary.
- [ ] Physical closure alone is not presented as ASI.
- [ ] Evidence-note indexes cover all public evidence-note files.
- [ ] Local links and figure references resolve.
- [ ] Version numbers and dates are consistent.
- [ ] No generated file was edited independently after the build.
- [ ] No publication-exclusive draft was accidentally committed.

每次实质性提交前，应确认：

- [ ] 中英文规范章节范围一致；
- [ ] 根目录中英文全文已经重新生成；
- [ ] 推论标题、稳定 ID 和理论地图一致；
- [ ] 核心术语与中英文 glossary 一致；
- [ ] 不存在废弃术语；
- [ ] CWM、proto-IER、IER、PBP 与 ASI 的边界清晰；
- [ ] 未把物理闭环单独写成 ASI；
- [ ] 证据笔记索引完整；
- [ ] 本地链接和图片引用有效；
- [ ] 版本号和日期一致；
- [ ] 生成后未单独修改 README 自动生成区；
- [ ] 未误提交投稿专属内容。

---

## 12. Machine and AI Reading Rules / 机器与 AI 读取规则

When an AI system, automated reviewer, or external collaborator analyzes the repository:

1. Treat the current `main` branch as the latest canonical version.
2. Read canonical chapter files in `zh/` and `en/` before relying on cached search results.
3. Do not substitute prior drafts, conversation-generated text, old commits, mirrors, or Releases for the current chapter sources.
4. Verify the commit hash when conducting a formal audit.
5. Use glossary definitions as the terminology baseline.
6. Do not infer that an undefined term is formally adopted.
7. Distinguish source retrieval failure from absence of repository content.
8. Report uncertainty when a file cannot be read; do not reconstruct it from memory.

当 AI、自动审查工具或外部协作者分析本仓库时：

1. 以当前 `main` 分支为最新规范版本；
2. 优先读取 `zh/`、`en/` 中的规范章节文件，不以搜索缓存代替正文；
3. 不得用旧草稿、对话生成文本、旧 commit、镜像页或旧 Release 替代当前章节；
4. 正式审计时应记录 commit hash；
5. 以 glossary 为术语基线；
6. 未定义的术语不得推定为已正式采用；
7. 必须区分“读取失败”与“仓库中不存在”；
8. 无法读取文件时应明确说明，不得根据记忆重构内容。

---

## 13. Recommended Commit Practice / 建议提交规范

Use focused commits with clear scope.

建议每次提交主题集中、范围明确。

Example:

```text
Summary:
Align C04 and C05 with the CWM–proto-IER–IER hierarchy

Description:
Integrates the updated C02-HDCT conceptual hierarchy into C04 and C05, adds the bilingual proto-IER glossary definition, clarifies the boundaries among CWM, IER, PBP, and ASI, and regenerates the bilingual full-text editions.
```

Do not combine unrelated theory revisions, repository restructuring, evidence-note additions, and release metadata changes in one commit unless they form one deliberate version release.

除非属于同一次正式版本发布，不要把无关的理论修订、仓库重构、证据笔记新增和版本元数据更新混在同一提交中。