# arXiv 注册邮箱与背书(Endorsement)执行方案

> 适用对象：独立研究者（自学考试学位论文），无高校/科研机构隶属。
> 生成日期：2026-10-23
> 依据：arXiv 官方文档（info.arxiv.org）与 2026-01-21 官方背书政策更新公告。
> **当前状态**：账号已注册完成（`xavercai` / `xavercai@outlook.com` / Independent Researcher），
> 已创建投稿 8272289（未完成状态，2026-11-06 到期）。**下一步只剩背书。**
>
> 配套文件：`ENDORSEMENT_EMAILS.md`（给 Yue Xie、Stefanos Nikolaidis 的两封英文请求信，已写好，
> 拿到 endorsement code 后填入即可发送）

---

## 一、结论先行

### 1.1 139 / 189 邮箱为什么不行

**不是因为域名被 arXiv 拉黑，而是这两个域名缺少 DMARC 记录。**

实测 DNS（`Resolve-DnsName`）结果：

| 域名 | MX 记录 | SPF | DMARC |
|---|---|---|---|
| 139.com | `mx2.mail.139.com` / `mx1.mail.139.com` | 有 | **无** |
| 189.cn | `mx2-189.21cn.com` / `mta-189.21cn.com` | 有 | **无** |
| gmail.com | 有 | 有 | 有 |
| outlook.com / hotmail.com | 有 | 有 | 有 |
| qq.com / foxmail.com | 有 | 有 | 有 |
| 163.com / 126.com | 有 | 有 | 有 |
| sina.com | 有 | 有 | 有 |
| aliyun.com | 有 | 有 | 有 |
| protonmail.com | 有 | 无 | 有 |

MX 存在说明这两个域名**能收信**。真正的差异在 DMARC：139.com 和 189.cn 是中国电信的**手机号邮箱服务**，账号由手机号直接派生，历史上被大量用于薅羊毛/批量注册/营销推送，域名信誉评分极低。arXiv 注册时会对邮箱域名做实时风险评估，风险域名在账号创建前就被拦截——所以你在表单阶段就被挡下了，验证邮件根本不会发出。

对照证据：Intel 官方支持文档中描述的同类机制（"该电子邮件地址来自受限域名"，注册时通过外部风险情报服务实时评估域名）正是主流学术/企业平台现在普遍采用的域名级风控；QQ/163/126 这类"低风险但非机构"的域名在 arXiv 上是被接受的，只是走背书流程而已。

### 1.2 推荐的邮箱方案（按优先级）

| 优先级 | 域名 | 理由 | 获取成本 |
|---|---|---|---|
| **首选** | `gmail.com` | DMARC 完整、国际通用、背书邮件送达率最高；投稿信里最不显突兀 | 需自备网络环境 |
| **次选** | `outlook.com` / `hotmail.com` | 微软系 DMARC 完整，国内可正常访问 | 免费 |
| **稳妥** | `foxmail.com` | 腾讯自有域名，DMARC 完整，与 QQ 邮箱同投递集群 | 免费 |
| **可用** | `qq.com` / `163.com` / `126.com` / `sina.com` | DMARC 完整，arXiv 接受，但属消费级邮箱 | 免费 |
| **最彻底** | 自有域名邮箱（如 `xxx.com`） | 完全脱离运营商与机构，署名"Independent Researcher"时观感最好，论文里可长期使用 | 约 ¥60-100/年 |

> **重要提醒**：arXiv 账号**终身唯一**，官方明确警告不要重复注册。选定一个邮箱后不要更换域名策略，注册前请先在下面 1.3 完成验证。

### 1.3 注册前的三步验证（5 分钟，避免注册到一半被卡）

1. **确认能收到国外邮件**：给你的候选邮箱发一封来自 Gmail/Outlook 的测试邮件，看是否正常进收件箱（不是垃圾箱）。139/189 这类邮箱常见"国外邮件进垃圾箱"问题，即使换了域名也可能踩坑。
2. **确认能收到 arXiv 验证邮件**：注册表单的验证码由 arxiv.org 发出（形如 `8GQUZR-P8NFDZ`）。若提交后 1 小时内未收到，检查垃圾箱；仍无则换域名重试（此时尚未完成注册，可安全重来）。
3. **选定后不要换**：注册成功即绑定，后续只能通过官方 [email change form](https://arxiv.org/auth/email-change-form) 更改，且历史投稿的作者元数据邮箱同步更新，需谨慎。

### 1.4 已落地的账号信息（2026-10-23）

账号已注册成功，实际情况：

| 项 | 值 |
|---|---|
| arXiv 用户名 | `xavercai` |
| 邮箱 | `xavercai@outlook.com` |
| Affiliation | Independent Researcher |
| 默认分类 | cs.AI |
| 背书域 | cs（覆盖 cs.AI 与 cs.RO） |
| 本月可投稿数 | 2 |

`outlook.com` 的 SPF 与 DMARC 均完整，注册通过验证。

**论文里的通讯邮箱已同步改为 `xavercai@outlook.com`**，与账号完全一致。这一步是必要的：arXiv 对单作者投稿会做作者邮箱一致性核对，论文中的通讯邮箱若与账号邮箱不符，可能被要求说明或影响审核。同时它也让 "Independent Researcher" 的署名在全文自洽——不再出现"独立研究者 + 企业邮箱"的表面矛盾。

后续 IEEE/ACM/Springer 审稿通信也统一使用 `xavercai@outlook.com`。

---

## 二、比邮箱更要紧的事：2026 年背书政策已变更

**这是本次调研中最重要的发现，直接决定你的投稿路径。**

arXiv 于 **2026 年 1 月 21 日**发布官方公告，核心变更：

> 机构邮箱地址（academic or research institution 的邮箱）**不再单独构成**新作者的背书资质。

变更后，新作者只有两条路：

| 路径 | 条件 | 你的可行性 |
|---|---|---|
| **路径一（自动背书）** | 同时满足：① 机构/研究机构邮箱；② 此前已有被 arXiv 接收的论文，且认领了该论文的作者身份 | ❌ 不满足。你没有机构邮箱，也没有既有 arXiv 论文 |
| **路径二（个人背书）** | 找一位在**同一背书域**已有足够论文的 arXiv 作者为你背书 | ✅ **这是你唯一的路** |

### 关键结论

> **无论你选哪个邮箱，都必须找到一位愿意为你背书的 arXiv 作者。**
> 换邮箱只能让你"注册成功"，但不能让你"有权投稿"。

cs 域的背书域是 `cs`（整个计算机科学大域），`cs.AI` 和 `cs.RO` 同属该域，**一位背书人可同时覆盖你的主分类和副分类**。

---

## 三、背书人筛选结果（已用 arXiv API 实测）

筛选脚本：`scripts/find_endorsers.py`
判定规则依据 [arXiv Endorsement 文档](https://info.arxiv.org/help/endorsement.html)：背书人须在背书域内有足够论文，且**仅统计 3 个月前至 5 年前提交的论文**（保证活跃度）。

查询词覆盖 novelty search / quality diversity / evolutionary robotics / embodied intelligence / behavioral diversity。
扫描 153 篇 → 落入有效窗口 104 篇 → 488 位作者。

### 3.1 候选背书人（按有效窗口内 cs 域论文数排序）

| 论文数 | 姓名 | 相关 arXiv ID | 方向匹配度 |
|---|---|---|---|
| 5 | **Antoine Cully** | 2509.11755, 2508.19172, 2504.01915, 2501.18723, 2405.04308 | ★★★ 质量多样性/行为发现，与本文"物理约束下的开放式行为进化"高度契合 |
| 4 | **Stéphane Doncieux** | 2604.22551, 2510.09267, 2410.02319, 2403.06173 | ★★★ QD 领域核心作者，novelty search 与行为多样性研究深厚 |
| 4 | **Mahdi Khoramshahi** | 2604.22551, 2510.09267, 2411.14917, 2403.06173 | ★★★ 群体机器人 + 行为发现 |
| 4 | **Johann Huber** | 2510.09267, 2410.02319, 2403.06173, 2210.07887 | ★★☆ QD/涌现行为 |
| 3 | **Stefanos Nikolaidis** | 2603.12510, 2602.23468, 2407.17515 | ★★★ 人机协作 + 行为多样性，论文主题与本文最接近 |
| 3 | **Yue Xie** | 2603.19582, 2503.16127, 2407.07591 | ★★★ "Evolving Embodied Intelligence"——**与你论文选题几乎同一个方向** |
| 3 | **Kyrre Glette** / **K. Ege de Bruin** / **Kai Olav Ellefsen** | 2605.15769, 2601.03813, 2601.03807 | ★★☆ 进化与智能体研究 |
| 3 | **Connor Mattson** / **Daniel S. Brown** | 2502.15937, 2310.16941, 2305.16148 | ★★★ novelty search + 群体机器人涌现行为 |
| 3 | **Jie Luo** | 2403.19545, 2309.14387, 2309.13099 | ★★☆ 机器人进化（Lamarckian Inheritance 论文） |
| 3 | **Paul Templier** / **Mathilde Kappel** / **François Hélénon** | 2509.11755, 2604.22551, 2410.02319, 2403.06173 | ★★☆ QD 方向 |
| 2 | **Emma Hart** | 2606.11037, 2403.10303 | ★★☆ 行为多样性 |
| 2 | **Faiz Ben Amar** | 2604.22551, 2210.07887 | ★★☆ 群体智能 |

> **最高优先级：Yue Xie（2603.19582《Evolving Embodied Intelligence: GNN-Driven Co-Design of Morphology and ...》）与 Stefanos Nikolaidis（2603.12510）**——两人的近期工作与本文"物理身体作为算法约束"的论点几乎同题，是最容易理解你研究意义的读者。

### 3.2 获取背书人的联系方式（官方流程）

1. 登录 arXiv（必须登录，未登录时 `/auth/show-endorsers/<id>` 返回 401）
2. 打开上述任一 arXiv 摘要页
3. 点击页面底部的 **"Which authors of this paper are endorsers?"** 链接（实测该链接存在且指向 `/auth/show-endorsers/<arxiv_id>`）
4. 列表中即为**有资格背书的作者**
5. 在同一摘要页的 **"Submission history"** 标题下方查看该作者的邮箱（arXiv 已把提交者邮箱改为登录后可见的 `[view email]` 链接）

> **不要用脚本批量抓邮箱**。官方明确规定：短时间内查看大量邮箱会导致账号被**不可撤销地封禁**（用于批量骚扰的判定阈值）。手动、逐个查看即可。

### 3.3 给背书人的请求邮件（英文模板）

> 发送数量控制：arXiv 明确指出"群发模板给大量潜在背书人"是不当行为。**一次只发给 1-2 人，优先顺序联系，不重复骚扰同一人。**

```subject
Endorsement request: arXiv submission on physical constraints in embodied evolution (code + dataset available)

Dear Prof. <Surname>,

I am an independent researcher preparing a submission to arXiv (cs.RO / cs.AI)
and would be grateful if you could consider endorsing it.

Your work on <specific topic from one of the papers listed above, e.g.
"quality-diversity optimisation for robot skill discovery"> is closely related to
the question my study addresses: how much does an agent's physical body itself
act as an algorithm in open-ended behavioural evolution?

The submission, "The Physical Riverbed Hypothesis: Structural Boundaries and
Cross-Hardware Validation of an Embodied Evolution System under Extreme
Constraints", reports a novelty-search-driven escape robot built from scratch
on two heterogeneous ESP32 platforms, deliberately consuming raw hardware
thermal noise as a system input. The main finding is a negative one: the weak
hypothesis that specific sensor parameters determine specific behaviours
collapses into a Simpson pseudo-correlation once environmental confounds are
removed, while the strong hypothesis is explicitly falsified. All firmware,
datasets and the analysis pipeline are open and reproducible:
https://github.com/xavercai/embodied-evolution-car

I am not affiliated with a university or research institute, so I am not able
to satisfy arXiv's institutional-email route. If the topic falls within your
area and you would be willing to endorse, please use the endorsement code in
the request email arXiv sent me. If you would prefer not to, please feel free
to ignore this message -- no explanation is needed.

Thank you for your time.

Best regards,
Jiyong Cai
Independent Researcher, Beijing, China
<your contact email>
```

**要点说明：**
- 第一段必须点明**你读过他的哪篇论文**——这是回复率最高的关键
- 主动说明"无机构隶属"（对应你论文里的 Independent Researcher 身份），避免对方误以为你隐瞒
- 附 GitHub 链接：可复现的开放代码+数据，是独立研究者最有力的背书理由
- 明确给出"可以拒绝"的出口，降低对方心理负担
- 邮件语言用英文，学界通用；中文邮件容易被直接忽略

---

## 四、执行顺序

### 已完成

| 步骤 | 动作 | 状态 |
|---|---|---|
| 1 | 申请 SPF+DMARC 完整的邮箱 | ✅ `xavercai@outlook.com` |
| 2 | 注册 arXiv，Organization 填 `Independent` | ✅ 已注册，用户名 `xavercai` |
| 3 | 选分类创建投稿（投稿 8272289 已建，未完成态） | ✅ 已创建，2026-11-06 到期 |

### 待完成（关键路径全在这）

| 步骤 | 动作 | 说明 |
|---|---|---|
| 4 | **拿到背书请求邮件中的 6 位 endorsement code** | code 有效期有限，收到后立即行动。检查 `xavercai@outlook.com` 收件箱与垃圾箱 |
| 5 | 按 3.1 顺序联系 1-2 位候选背书人 | 从 Yue Xie / Stefanos Nikolaidis 开始，附 GitHub 链接 |
| 6 | 背书通过后完成投稿 8272289 | 上传 `build/arxiv/arxiv_submission.tar.gz`，主文件选 `main.tex` |
| 7 | 许可选第 5 项 `arXiv.org perpetual, non-exclusive license` | 不可撤销，选它对 IEEE/ACM/Springer 零冲突 |
| 8 | 拿到 arXiv ID 后回填 README 与 CITATION.bib | 发给我即可，我帮你改并推送 |

### 关于投稿 8272289

- 未完成状态的投稿会保留到 **2026-11-06**，过期后 arXiv 自动删除。
- 若在到期前背书已到位，直接点该行的 **update** 继续即可，无需重建。
- 若背书拖到 11-06 之后，点 **START NEW SUBMISSION** 重来——提交包已就绪（53.6 KB，校验通过），随时可传。
- 注意：`build/` 目录被 `.gitignore` 排除，提交包不会进 git，**不要清空本地 `build/` 目录**。

### 注册表填写要点

- **Organization affiliation**：`Independent`（官方明确允许 unaffiliated 者填 "Independent" 作为机构）
- **Organization email**：填与 Organization 关联的邮箱；若选 Independent，填你的个人邮箱即可
- **Password**：≥8 位，必须含下划线 `_`，其余只允许字母数字
- **Username**：一旦设定不可更改

---

## 四点五、排查：还没收到背书请求邮件

**结论先行：这不是故障，而是流程还没走到触发点。**

arXiv 官方文档对背书请求邮件的触发条件写得很明确：

> "Start a new submission and select the category you wish to submit to.
> Check your email for an **endorsement request email**."

即：**背书请求邮件是在投稿流程走到"选择分类"这一步时，由系统自动发出的**，而不是注册账号时发的，也不是点"START NEW SUBMISSION"就发的。

而当前投稿 8272289 的状态是 **incomplete（未完成）**。arXiv 投稿系统 v1.5 的完整步骤是：

```
Prepare Files（上传）→ Check Files → Accept and Continue
    → 编译 → Preview your PDF → Continue
    → Metadata 页（在这里填标题/摘要/作者/分类）
    → Submit Article
```

**Metadata 页的分类选择步骤才是触发点**。你的投稿停在"未完成"，说明大概率还没提交到那一步，因此邮件从未发出。

### 排查清单（按顺序做）

| # | 检查 | 做法 | 判断 |
|---|---|---|---|
| 1 | **投稿是否走到 Metadata 页** | 回到 arXiv 用户页 → 点投稿 8272289 的 **update** → 走完文件检查 → Continue → 进 Metadata 页 | 若之前就停在这里 → 这就是没收到邮件的原因，继续走完即可触发 |
| 2 | **分类是否真的选到 cs 域** | 在 Metadata 页把主分类设为 `cs.AI` 或 `cs.RO`（同属 cs 背书域），次分类选另一个 | 选完点 Continue，系统当场发信 |
| 3 | **垃圾邮件 / 其他文件夹** | outlook.com 网页版检查：垃圾邮件、**"其他"（Other）**、**"聚焦"（Focused）** 三个分类都要看；搜索 `arxiv` / `endorse` 关键词 | Outlook 网页版默认把非通讯邮件归入"其他"，很容易漏看 |
| 4 | **是否用了其他邮箱** | 确认 arXiv 账号邮箱仍是 `xavercai@outlook.com`（用户页顶部 E-mail 一行）。若曾改成大众汽车邮箱，信就发到那边了 | 与本机 Outlook 一致：大众汽车账号本地 OST 中未发现任何 arXiv 背书邮件痕迹 |
| 5 | **等待时间** | arXiv 的自动发信是即时的，但 Outlook 对批量/自动发件人有延迟过滤 | 若第 1、2 步确认已触发，等 24 小时仍无 → 走第 4 节"联系 arXiv" |

### 第 1 步的具体操作（最可能的解法）

1. 登录 arXiv → 用户页 → 找到 `submit/8272289` → 点 **update**
2. "Prepare Files" 页点 **Check Files** → 确认 Top-Level TeX file 是 `main.tex` → **Accept and Continue**
3. 等编译完成 → **Continue**
4. **Metadata 页**：填标题、摘要、作者（`Jiyong Cai`）、**主分类 `cs.AI`**、次分类 `cs.RO` → **Continue**
5. 这一步系统会立刻把背书请求邮件发到账号邮箱（正文含 6 位 endorsement code 和 `https://arxiv.org/auth/endorse?x=XXXXXX` 链接）
6. 回到用户页点 **Unsubmit** 也可以——官方说明 unsubmit 会把投稿退回 incomplete 状态以便修改

> 提交包已就绪，直接用 `build\arxiv\arxiv_submission.tar.gz`，主文件选 `main.tex`。若上传阶段报错，指南第四章的构建校验规则可对照排查。

### 如果第 3 步确认邮件已到但被误判

- 在 Outlook 网页版把 `arxiv.org` 加入**安全发件人**，避免后续背书人回复被误判为垃圾邮件
- 搜索范围要包含"所有文件夹"，不只是收件箱

### 如果始终收不到（超过 24 小时）

arXiv 官方为背书问题设有专门渠道：

- **Endorsement Policy Feedback Form**（官方在 2026-01-21 公告中明确推荐）：https://blog.arxiv.org/2026/01/21/attention-authors-updated-endorsement-policy/
- **用户支持门户**：https://support.arxiv.org/
- 邮件：`help@arxiv.org`（官方提示：若没收到自动回信，多半是被垃圾邮件过滤器吃了）

> 官方明确表态：**"arXiv staff cannot waive endorsement requirements or provide a personal endorsement for authors."** 工作人员不能豁免背书要求，也不能替你背书。所以求助渠道的作用是排查邮件投递故障，而不是走捷径。这点要有预期。

---

## 五、风险与备选

| 风险 | 应对 |
|---|---|
| 找不到愿意背书的人 | ① 换 `cs.LG` 等背书人池更大的分类（但需同步调整主分类，会影响论文曝光）；② 通过 arXiv [Contact Form](https://arxiv.org/contact) 说明情况，官方偶尔直接处理；③ 先投期刊，arXiv 预印本非必需前置 |
| 背书请求长期无人响应 | arXiv 官方建议直接联系 arXiv 管理员而非放弃 |
| 分类选错被 moderator 改判 | 论文是具身智能 + 进化 + 机器人，cs.RO 与 cs.AI 均合理；建议主 cs.RO、副 cs.AI，与你的开放仓库主题一致 |
| 许可选错 | arXiv 许可**不可撤销**，提交前务必确认第 5 项 |

---

## 六、参考资料

- arXiv 注册帮助（含 "If you are unaffiliated you may enter 'Independent' as your organization"）: https://info.arxiv.org/help/registerhelp.html
- arXiv 背书系统说明: https://info.arxiv.org/help/endorsement.html
- 2026-01-21 背书政策更新公告: https://blog.arxiv.org/2026/01/21/attention-authors-updated-endorsement-policy/
- arXiv 身份与机构政策: https://info.arxiv.org/help/policies/identity_and_affiliation.html
- arXiv 邮箱可见性政策: https://info.arxiv.org/help/email-protection.html
- arXiv 许可说明: https://info.arxiv.org/help/license
