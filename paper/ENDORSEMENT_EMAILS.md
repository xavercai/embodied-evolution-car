# 背书请求邮件（针对两位最高优先级候选背书人）

> 使用说明
> 1. 等 arXiv 背书请求邮件到达后，从正文取出 6 位 endorsement code 与 `https://arxiv.org/auth/endorse?x=XXXXXX` 链接。
> 2. 下面两封各填入对应的 code 与链接，**一次只发一封**。arXiv 明确禁止群发模板骚扰。
> 3. 每封都单独针对该作者的具体论文写，回复率远高于群发。
> 4. 发出后若 1-2 周无回应，再换下一位，**不要重复催同一人**。

---

## 邮件 1：Yue Xie（最高优先级）

**收件人获取**：arXiv 摘要页 `https://arxiv.org/abs/2603.19582` → 底部 "Which authors of this paper are endorsers?" → 列表中确认该作者有背书资格 → 同页 "Submission history" 下点 `[view email]`

**主题**：

```
Endorsement request: arXiv submission on whether the robot's body acts as an algorithm (code + dataset open)
```

**正文**：

```text
Dear Dr. Xie,

I am an independent researcher preparing a submission to arXiv (cs.AI / cs.RO)
and would be grateful if you could consider endorsing it.

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
endorsement. The endorsement code I was issued is:

    <ENDORSEMENT CODE>

and the direct link is:

    <https://arxiv.org/auth/endorse?x=XXXXXX>

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

## 邮件 2：Stefanos Nikolaidis

**收件人获取**：`https://arxiv.org/abs/2603.12510` → "Which authors of this paper are endorsers?" → "Submission history" 下的 `[view email]`

**主题**：

```
Endorsement request: arXiv submission on physical constraints as an algorithmic channel (code + dataset open)
```

**正文**：

```text
Dear Dr. Nikolaidis,

I am an independent researcher preparing a submission to arXiv (cs.AI / cs.RO)
and would be grateful if you could consider endorsing it.

Your recent work on behavioural diversity and the design of agents that
engage with people (arXiv:2603.12510 and related) resonates with the premise
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
endorsement. The endorsement code I was issued is:

    <ENDORSEMENT CODE>

and the direct link is:

    <https://arxiv.org/auth/endorse?x=XXXXXX>

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

## 通用提醒（两封信都适用）

| 事项 | 要求 |
|---|---|
| 发送数量 | 一次只发 1 封。arXiv 官方明确："it is inappropriate to email large numbers of potential endorsers at once, or to repeatedly email the same endorser" |
| 语言 | 英文。中文邮件在学术圈基本不会被回复 |
| 附件 | 官方建议附上投稿副本。可附 `build\arxiv\arxiv_submission.tar.gz` 或 PDF 预览件 |
| 身份声明 | 必须写明"I am an independent researcher" / 无机构隶属——这与论文署名一致，不是缺陷，无需隐瞒 |
| 拒绝出口 | 明确给出"可以拒绝、不必解释"的出口，显著提高回复率 |
| 背书人收到的东西 | 背书人点链接后看到的是官方表单，只需填入 6 位 code 并选择是否同意背书，**不需要他们审稿** |
| 后续 | 若 1-2 周无回应，换下一位候选（见 `ARXIV_SUBMISSION_GUIDE.md` 3.1 节的完整名单），不要重复催同一人 |

## 若 4-6 位都无回应

arXiv 官方建议此时联系 arXiv 管理员（而非放弃）。同时可考虑：

1. 换一个背书人池更大的分类（`cs.LG`），但需相应调整主分类，会影响论文曝光面
2. 先投期刊 —— 多数期刊不要求先上 arXiv，arXiv 预印本不是期刊投稿的前置条件
3. 通过 arXiv 用户支持门户说明情况，官方偶尔会直接处理投递故障类问题（但不会豁免背书要求本身）
