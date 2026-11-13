# AgentHub Lite

- 版本：0.1.3
- 更新：2026-11-14 04:30 Asia/Shanghai
- 托管：Cloudflare Pages（https://agenthub-lite.pages.dev/）
- 源码：https://github.com/sunnyspot114514/agenthub-lite
- 访问：公开、只读、无数据库、无登录
- 身份：[sunnyspot114514](https://github.com/sunnyspot114514)
- 本文件是给 AI 的统一入口。人类请看 [index.html](index.html)。

## 这是什么

AgentHub Lite = 一份供 AI 读取的、可追溯更新的个人项目上下文。

它不是家用 Agenthub。家用 Hub 有身份、ACL、工作区和 MCP，跑在所有者机器上。Lite 只有静态页面和 Markdown。把本页 URL 交给能访问网页的 Agent 即可；能否读到取决于对方的工具和网络，不取决于本站再提供 API。

扫码打开的就是本文件。若要自己搭一份同类站点，不要复制本页的项目内容，去用 Skill：https://agenthub-lite.pages.dev/skill/SKILL.md （zip：https://agenthub-lite.pages.dev/agenthub-lite-cloudflare-starter.zip）。Skill 会生成你自己的 Lite，不会覆盖本站。

相关入口：

| 用途 | URL |
|------|-----|
| 本站 | https://agenthub-lite.pages.dev/ |
| 本快照（AI） | https://agenthub-lite.pages.dev/context.md |
| 本站源码 | https://github.com/sunnyspot114514/agenthub-lite |
| 家用 Hub | https://agenthub.sunny99.win |
| Hub 源码 | https://github.com/sunnyspot114514/agenthub |
| 公开告示板 | https://aegis.sunny99.win |
| 告示板源码 | https://github.com/sunnyspot114514/aegis-observatory |
| Hub 浏览器演示 | https://huggingface.co/spaces/sunny114514/agenthub-playground |
| 复刻用 Skill | https://agenthub-lite.pages.dev/skill/SKILL.md |
| Skill 打包下载 | https://agenthub-lite.pages.dev/agenthub-lite-cloudflare-starter.zip |

## 我是谁、研究方向

GitHub：[sunnyspot114514](https://github.com/sunnyspot114514)。公开工作围绕本地优先的 Agent 基础设施，以及可核对的审计/验证笔记。

当前公开方向：

1. **家用 Agent Hub**：授权 Agent 的共享上下文、工作区、聊天、人批准后的 GitHub 发布。
2. **公开观察**：极小的告示板（AEGIS），让 Agent 按文档读写短消息，而不是把访客当成“出逃 AI”。
3. **独立核对**：对公开数学/Lean 结果和 AI 风险材料做可复现笔记（见 GitHub 上的 `*-audit` 仓库）。

## 项目索引

### Agenthub — 运行中

本地优先家庭 Agent Hub。作者实例 1.4.9。源码 MIT。

- 详情：[projects/agenthub.md](projects/agenthub.md)
- 仓库：https://github.com/sunnyspot114514/agenthub
- 实例：https://agenthub.sunny99.win

### AEGIS Agent Observatory — 运行中

公开告示板。匿名可读；写入必须 `public: true`。

- 详情：[projects/aegis.md](projects/aegis.md)
- 仓库：https://github.com/sunnyspot114514/aegis-observatory
- 实例：https://aegis.sunny99.win
- Agent 入口：https://aegis.sunny99.win/agent.txt

## 近期进展

完整时间线见 [changelog.md](changelog.md)。

- 2026-11-14：公开源码仓库 https://github.com/sunnyspot114514/agenthub-lite 。
- 2026-10-31：本站公开托管复刻用 Skill（`/skill/SKILL.md` 与 zip）。
- 2026-10-30：Lite 公开入口为 Cloudflare Pages（https://agenthub-lite.pages.dev/）。
- 2026-10-27：家用 Hub 前的 Cloudflare Tunnel 客户端升到 2026.10.4。
- 2026-10-21：Agenthub 公开树为 1.4.9。
- 2026-10-19：AEGIS 公开源码仓库。

## 下一步任务

当前问题：Lite 是手工快照，不是家用 Hub 的实时投影。

待办：

1. 公开项目有实质进展时，更新 `projects/`、`changelog.md` 和本文件顶部的更新时间，再推 GitHub 并发布 Pages。
2. 不要把派上 `data/`、token、未公开仓库或协作资料拷到本站。

交接：改这些文件后提交 GitHub（https://github.com/sunnyspot114514/agenthub-lite），再 `wrangler pages deploy`。公开入口以 https://agenthub-lite.pages.dev/ 为准。
