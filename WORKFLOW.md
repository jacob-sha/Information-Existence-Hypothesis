# IEH Workflow

## 1. New Corollary Workflow

When adding a new IEH corollary:

1. Assign the next stable corollary ID in `COROLLARY_REGISTRY.md`.
2. Add the corollary to the appropriate layer in `THEORY_MAP.md`.
3. Create a draft or placeholder file only when needed.
4. Avoid publication-ready prose in public draft files.
5. If the corollary generates testable predictions, create or update prediction records in `IEH-predictions`.
6. Use stable IDs in prediction metadata.
7. Preserve publication and copyright boundaries for future submissions.

## 2. Prediction Record Workflow

When adding or updating a prediction record:

1. Use `PREDICTION_TEMPLATE.md`.
2. Add stable corollary IDs.
3. Use `primary_corollaries`, `supporting_corollaries`, `related_corollaries`, and `legacy_corollary_refs`.
4. Keep the document archival, not essay-like.
5. Record observable indicators and evidence logs.
6. Avoid polished article openings, full pitches, or publication-ready argument flow.

## 3. Publication Boundary

Public repository documents preserve:

- theoretical priority;
- conceptual structure;
- mechanisms;
- observable indicators;
- evidence logs.

They should not contain:

- complete media essays;
- final op-ed drafts;
- full pitch letters;
- polished magazine-style openings;
- long narrative passages that can be directly reused in submissions

---

# IEH 工作流

本文件用于规范 Information Existence Hypothesis（IEH）主仓、预测仓、证据笔记和未来投稿之间的协作流程。

核心目标是：

- 保持推论编号稳定；
- 保持理论地图清晰；
- 保持预测文档可追踪；
- 保护未来投稿的首发权、独家权和版权边界；
- 避免公开仓库内容过度接近投稿成稿。

---

## 一、新增推论工作流

新增 IEH 推论时，应遵循以下步骤：

1. 在 `COROLLARY_REGISTRY.md` 中分配下一个稳定推论 ID。
2. 不要重新编号已有推论。
3. 在 `THEORY_MAP.md` 中将新推论放入合适的理论层级。
4. 如果全文尚未准备好，只建立 Draft 或 Placeholder 文件。
5. 公开草案中避免使用接近投稿成稿的表达。
6. 如果该推论产生可验证预测，则在 `IEH-predictions` 中新增或更新预测文档。
7. 预测文档元信息中必须使用稳定推论 ID。
8. 保留未来投稿与版权边界，避免影响首发权、独家投稿或后续英文 / 中文改写。

---

## 二、推论编号规则

IEH 推论编号采用稳定编号制度。

推论编号一经分配，即应保持稳定。

不应：

- 重新编号；
- 插队编号；
- 复用旧编号；
- 因逻辑顺序变化而移动编号。

理论逻辑顺序通过 `THEORY_MAP.md` 维护，而不是通过重新编号维护。

例如：

- `C06-SPP` 可以属于 Pre-ASI 人类文明重构层；
- `C12-GOV` 虽然后出现，但可以在理论地图中排在战争和教育之前；
- `C13-WAR` 和 `C14-EDU` 可以在逻辑上与 `C06-SPP` 构成同一 Pre-ASI 层。

核心规则：

> 推论编号用于历史稳定性，理论地图用于逻辑顺序。

---

## 三、预测文档工作流

新增或更新预测文档时，应遵循以下步骤：

1. 使用预测仓中的 `PREDICTION_TEMPLATE.md`。
2. 使用稳定推论 ID。
3. 使用以下字段建立多对多映射：
   - `primary_corollaries`
   - `supporting_corollaries`
   - `related_corollaries`
   - `legacy_corollary_refs`
4. 保持预测文档档案化，而不是文章化。
5. 明确写出预测机制、可观测指标和证伪条件。
6. 持续更新证据日志。
7. 避免媒体化开头、完整 pitch、完整案例展开或投稿成稿式论证。

预测文档的目的不是发表文章，而是记录：

- 理论优先权；
- 预测结构；
- 可观测指标；
- 证据日志；
- 状态变化；
- 与 IEH 推论的映射关系。

---

## 四、预测映射规则

一个预测可以对应多个推论，不应强行绑定到单一推论。

推荐结构：

- `primary_corollaries`：该预测最直接验证或呈现的推论；
- `supporting_corollaries`：为该预测提供支持机制的推论；
- `related_corollaries`：概念上相关但不是核心验证对象的推论；
- `legacy_corollary_refs`：旧版本中的罗马数字、中文序号或旧标题引用。

旧引用，例如“推论六”“Corollary VI”或旧概念名称，仍然有效。

但新预测文档应同时加入稳定 ID，例如：

- `C06-SPP`
- `C12-GOV`
- `C13-WAR`
- `C14-EDU`

---

## 五、证据笔记工作流

新增证据笔记时，应遵循以下原则：

1. 证据笔记应记录外部研究、新闻事件、技术进展或现实案例。
2. 证据笔记应说明其与 IEH 的关系。
3. 证据笔记不应被写成完整评论文章。
4. 证据笔记应尽量引用来源、日期和相关推论 ID。


---

## 4. Canonical Text and Full-text Build Workflow

The chapter collections are the canonical source for substantive revision:

```text
zh/*.md  = canonical Chinese chapters
en/*.md  = canonical English chapters
```

The root full-text editions are generated from those chapters:

```text
README.md     = generated Chinese full text
README_EN.md  = generated English full text
```

After revising a chapter, run:

```bash
python scripts/build_fulltext.py
python scripts/check_repository.py
```

Do not independently edit generated chapter content inside the root README files. Front matter, project navigation, abstract, project extensions, terminology links, and appendices may be maintained in the root files outside the generated markers.

Before each release, verify:

- chapter titles match `COROLLARY_REGISTRY.md`;
- core terminology matches the bilingual glossary;
- every ASI reference follows the canonical definition: IER + physical self-maintenance;
- highly autonomous operation without IER is not described as ASI;
- Chinese and English chapter collections contain the same chapter set;
- root full-text editions are synchronized with chapter files;
- local links and figure references resolve;
- version and release dates are consistent across metadata files.

---

## 四、规范正文与全文生成工作流

正文修订以分章节文件为规范来源：

```text
zh/*.md  = 中文规范章节
en/*.md  = 英文规范章节
```

根目录全文由章节文件生成：

```text
README.md     = 自动生成的中文全文
README_EN.md  = 自动生成的英文全文
```

完成章节修改后运行：

```bash
python scripts/build_fulltext.py
python scripts/check_repository.py
```

不要在根目录 README 的自动生成区间内单独修改章节正文。项目导航、摘要、项目扩展、术语链接和附录等位于自动生成标记之外的内容，可以继续在根文件中维护。

每次发布前应确认：

- 章节标题与 `COROLLARY_REGISTRY.md` 一致；
- 核心术语与中英文 GLOSSARY 一致；
- 所有 ASI 表述均遵循“IER + 物理自我维持能力”的定稿定义；
- 未形成 IER 的高度自主运行能力不得表述为 ASI；
- 中英文目录包含相同的章节集合；
- 根目录全文与章节文件同步；
- 本地链接和图片引用有效；
- 各元数据文件中的版本号与发布日期一致。
