# 背书请求邮件（可直接发送版）

> **你的 endorsement code：`Q8YMWW`**（arXiv 于 2026-10-23 发出，绑定 cs.RO）
> 背书链接：`https://arxiv.org/auth/endorse?x=Q8YMWW`
>
> 使用说明
> 1. 两封信已填好 code，**一次只发一封**。arXiv 官方明确禁止群发骚扰或反复催同一人。
> 2. 优先发**邮件 1（Yue Xie）**，其论文主题与你几乎同题，命中概率最高。
> 3. 每封都单独针对该作者的具体论文写，回复率远高于群发模板。
> 4. 发出后若 1-2 周无回应，再换下一位，**不要重复催同一人**。

---

## 重要：一次背书即可覆盖 cs.AI

arXiv 的背书是**按 endorsement category** 计的（官方："At least one positive endorsement is required per endorsement category"）。而 cs.RO 的背书域涵盖全部 41 个 cs.* 分类（你收到的邮件里列的那串：cs.AI、cs.AR、cs.CC、…、cs.RO、cs.SC、cs.SD、cs.SE、cs.SI、cs.SY）。

> **结论：`Q8YMWW` 一次背书同时解锁 cs.RO 与 cs.AI。**不需要为两个分类各要一次背书。

---

## 邮件 1：Yue Xie（最高优先级，先发这封）

**收件人获取**：
1. 打开 `https://arxiv.org/abs/2603.19582`
2. 页面底部点 **"Which authors of this paper are endorsers?"**（链接为 `/auth/show-endorsers/2603.19582`，**需登录**）
3. 确认列表中 **Yue Xie** 有背书资格
4. 同页 **"Submission history"** 下点作者旁的 `[view email]`（链接形如 `/show-email/<hash>/2603.19582`）

**已知信息**：Yue Xie 在 cs 域有效窗口内有 **17 篇**论文，满足"3 篇"门槛。论文《Evolving Embodied Intelligence》(2603.19582) 分类 cs.RO + cs.AI，2026-03-20 提交。

**主题**：

```
Endorsement request: arXiv submission on whether the robot's body acts as an algorithm (code + dataset open)
```

**正文**（可直接复制发送）：

```text
Dear Dr. Xie,

I am an independent researcher preparing a submission to arXiv (cs.RO, cross-listed
to cs.AI) and would be grateful if you could consider endorsing it.

Your work on "Evolving Embodied Intelligence" (arXiv:2603.19582) co-designs
morphology and behaviour through a GNN-driven loop, which asks precisely the
question my study approaches from the opposite direction: not how to optimise
a body for a task, but how much an agent's physical structure itself acts as
an algorithm that constrains and shapes the trajectory of open-ended
behavioural evolution.

My submission, "The Physical Riverbed Hypothesis: Structural Boundaries and
Cross-Hardware Validation of an Embodied Evolution System under Extreme
Constraints", reports a novelty-search-driven escape robot built from scratch
on two heterogeneous ESP32 platforms, deliberately consuming raw hardware
thermal noise as a system input. The main result is negative and I think it is
worth stating plainly: the weak hypothesis that specific sensor parameters
directly determine specific behaviours collapses into a Simpson
pseudo-correlation once environmental confounds are removed, and the strong
version of the hypothesis is explicitly falsified. What survives across
hardware and firmware versions is a set of structural signatures -- novelty
that rises then plateaus, a non-degenerating rule count, and chaos
constrained to left-wheel deceleration.

Because I am not affiliated with a university or research institute, I cannot
qualify through arXiv's institutional-email route and have to seek personal
endorsement. My endorsement code is:

    Q8YMWW

and the direct link is:

    https://arxiv.org/auth/endorse?x=Q8YMWW

All firmware, datasets and the full analysis pipeline are open and
reproducible, so you can inspect the work directly:

    https://github.com/xavercai/embodied-evolution-car

I am aware that endorsing carries no obligation to read the paper in detail;
I only ask that the work looks appropriate for the cs domain. If you would
prefer not to, please feel free to ignore this message -- no explanation is
needed, and I will simply look for another endorser.

Thank you for your time.

Best regards,
Jiyong Cai
Independent Researcher, Beijing, China
xavercai@outlook.com
```

---

## 邮件 2：Stefanos Nikolaidis（第一封无回应时发这封）

**收件人获取**：
1. 打开 `https://arxiv.org/abs/2603.12510`
2. 底部点 **"Which authors of this paper are endorsers?"**（`/auth/show-endorsers/2603.12510`，**需登录**）
3. 确认 **Stefanos Nikolaidis** 在列表中（他是该文第 12 位作者，**务必用底部链接确认资格**，不要只看作者栏）
4. 同页 "Submission history" 下点 `[view email]`

**已知信息**：Stefanos Nikolaidis 在 cs 域有效窗口内有 **39 篇**论文，满足门槛。论文《Red-Teaming Vision-Language-Action Models via Quality Diversity Prompt Generation for Robust Robot...》(2603.12510) 分类 cs.RO + cs.AI + cs.CL。

**主题**：

```
Endorsement request: arXiv submission on physical constraints as an algorithmic channel (code + dataset open)
```

**正文**（可直接复制发送）：

```text
Dear Dr. Nikolaidis,

I am an independent researcher preparing a submission to arXiv (cs.RO, cross-listed
to cs.AI) and would be grateful if you could consider endorsing it.

Your recent work on quality-diversity prompt generation for red-teaming
vision-language-action models (arXiv:2603.12510) resonates with the premise
my study tests: that the interaction between an agent's body, its environment
and a simple control law is where behaviour actually comes from -- and that
the body itself contributes far more to that outcome than is usually
acknowledged.

My submission, "The Physical Riverbed Hypothesis: Structural Boundaries and
Cross-Hardware Validation of an Embodied Evolution System under Extreme
Constraints", reports a novelty-search-driven escape robot built from scratch
on two heterogeneous ESP32 platforms under a strict "no-calibration,
no-filtering, no-PID" protocol, deliberately consuming raw hardware thermal
noise as a system input. The main finding is negative: the weak hypothesis
that specific sensor parameters directly determine specific behaviours
collapses into a Simpson pseudo-correlation once environmental confounds are
removed, and the strong form of the hypothesis is falsified. What generalises
across hardware and firmware versions is structural -- novelty that rises
then plateaus, a non-degenerating rule count, and chaos constrained to
left-wheel deceleration -- which I frame as the physical body acting as a
"riverbed" that constrains the parameter-evolution space through epistatic
effects.

Because I am not affiliated with a university or research institute, I cannot
qualify through arXiv's institutional-email route and have to seek personal
endorsement. My endorsement code is:

    Q8YMWW

and the direct link is:

    https://arxiv.org/auth/endorse?x=Q8YMWW

All firmware, datasets and the full analysis pipeline are open and
reproducible, so you can inspect the work directly:

    https://github.com/xavercai/embodied-evolution-car

I am aware that endorsing carries no obligation to read the paper in detail;
I only ask that the work looks appropriate for the cs domain. If you would
prefer not to, please feel free to ignore this message -- no explanation is
needed, and I will simply look for another endorser.

Thank you for your time.

Best regards,
Jiyong Cai
Independent Researcher, Beijing, China
xavercai@outlook.com
```

---

## 备选背书人（前三封都无回应时用）

以下同样满足"cs 域 3 篇"门槛，主题匹配度依次递减：

| 姓名 | 首选论文 | cs 域有效论文数 | 方向匹配 | 摘要页 |
|---|---|---|---|---|
| Stéphane Doncieux | 2604.22551 (QDTraj) | 21 | ★★★ QD 领域核心作者 | `arxiv.org/abs/2604.22551` |
| Mahdi Khoramshahi | 2604.22551 | 15 | ★★★ 群体机器人 + 行为发现 | 同上 |
| Connor Mattson | 2502.15937 | 11 | ★★★ novelty search + 群体机器人涌现行为 | `arxiv.org/abs/2502.15937` |
| Daniel S. Brown | 2502.15937 | 35 | ★★★ 同上 | 同上 |
| Faiz Ben Amar | 2604.22551 | 9 | ★★☆ 群体智能 | `arxiv.org/abs/2604.22551` |
| Alvaro Serra-Gomez | 2603.19582 | 9 | ★★☆ 进化计算 | `arxiv.org/abs/2603.19582` |
| Shuaiqun Pan | 2603.19582 | 7 | ★★☆ 同上 | 同上 |
| Minjune Hwang | 2603.12510 | 7 | ★★☆ 机器人学习 | `arxiv.org/abs/2603.12510` |
| Bryon Tjanaka | 2603.12510 | 10 | ★★☆ 具身智能 | 同上 |

> 邮件模板结构同上，只需替换称呼、论文引用与 code 段落即可。

---

## 通用提醒

| 事项 | 要求 |
|---|---|
| 发送数量 | 一次只发 1 封。arXiv 官方："it is inappropriate to email large numbers of potential endorsers at once, or to repeatedly email the same endorser" |
| 查邮箱方式 | 必须**登录** arXiv 后查看摘要页的 `[view email]`。未登录时 `/auth/show-endorsers/<id>` 返回 401 |
| 不要批量抓取 | arXiv 明确禁止短时间查看大量邮箱，可能导致**不可撤销的账号封禁**。手动、逐个查看 |
| 语言 | 英文。中文邮件在学术圈基本不会被回复 |
| 附件 | 官方建议可附投稿副本。附 `build\arxiv\arxiv_submission.tar.gz` 或 PDF 预览件 |
| 身份声明 | 必须写明"I am an independent researcher"——与论文署名一致，不是缺陷，无需隐瞒 |
| 拒绝出口 | 明确给出"可以拒绝、不必解释"，显著提高回复率 |
| 背书人要做的事 | 打开链接、填入 6 位 code、同意背书。**不需要审稿** |
| 后续 | 1-2 周无回应就换下一位，不要重复催同一人 |

## 若 4-6 位都无回应

arXiv 官方建议此时联系 arXiv 管理员（而非放弃）。可考虑的并行方案：

1. **先投期刊**——多数期刊不要求先上 arXiv，arXiv 预印本不是期刊投稿的前置条件。**这条最实际**
2. 通过 arXiv 用户支持门户说明情况（官方偶尔直接处理投递故障类问题，但不会豁免背书要求本身）
3. 换用 `cs.LG` 或 `cs.NE`（cs.NE = Neural and Evolutionary Computing，与"进化 + 行为"高度契合），但需调整主分类，影响论文曝光面
