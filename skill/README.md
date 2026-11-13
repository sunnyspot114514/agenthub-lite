# AgentHub Lite · Cloudflare Pages 教学 Starter

> **一个链接，让不同 AI 读取同一份经本人审核的公开项目上下文。**

这是独立于完整 AgentHub 的**静态公开只读演示**。没有数据库、登录、自动记忆同步、MCP 写入、密钥或者后台 Agent。它特别适合 15 分钟演讲、大学生教学，以及用多个模型体验同一份项目交接资料。

## 两条路径，不强迫学生注册 GitHub

- **新手（推荐入门）**：让 AI 生成站点 → 人工审核 → Cloudflare Pages 控制台 Direct Upload → 把 URL 给另一个 Agent。详见 [`CLOUDFLARE-QUICKSTART.md`](CLOUDFLARE-QUICKSTART.md)。
- **长期维护**：在 GitHub 保存自己的站点源文件 → 用 Cloudflare Pages Git 集成自动部署已提交的 `docs/` → 将版本控制融入日常更新。详见 [`GITHUB-PUBLISH.md`](GITHUB-PUBLISH.md)。

学生不用提供手机号给 Agent、不用把密码或 Token 填进 Skill、不需要先学会服务器部署。Cloudflare 与 GitHub 账号由每位用户**自己**在官方站点注册、登录和授权。

## 本地一键生成（可由支持文件操作的 Agent 执行）

需要 Python 3.9+，不需要额外依赖：

```bash
python scripts/agenthub_lite.py init my-agenthub-lite
# 修改 my-agenthub-lite/context.md、my-agenthub-lite/projects/、my-agenthub-lite/changelog.md
python scripts/agenthub_lite.py check my-agenthub-lite
python scripts/agenthub_lite.py build my-agenthub-lite
python scripts/agenthub_lite.py serve my-agenthub-lite
```

输出的 `my-agenthub-lite/docs/` 可直接上传 Pages，包含 `index.html`、`context.md`、`context.txt`、`llms.txt`、项目文档以及机器索引。**浏览器能打开页面不代表每个 AI 都能读取；请用新会话分别测试。**

## 给 AI 安装 Skill

将整个本仓库（含 `SKILL.md`、`scripts/`、`assets/`）放入支持 Agent Skills 的项目技能目录，例如 Codex 的 `.agents/skills/agenthub-lite/`。若对应工具支持从 GitHub 安装 Skill，待仓库发布后可通过其安装器安装；普通聊天 AI 可直接使用 [`NO-SKILL-PROMPT.md`](NO-SKILL-PROMPT.md)。

然后告诉 Agent：

> 使用 AgentHub Lite Skill，把我明确允许公开的资料整理成一个供其他 AI 读取的个人项目站点，先让我审核；然后指导我通过 Cloudflare Pages 发布。不要自动把任何私人文件、聊天记录或密钥上传到网上。

## 目录

```text
SKILL.md                    Agent 标准技能描述
CLOUDFLARE-QUICKSTART.md    不依赖 GitHub 的学生版教程
GITHUB-PUBLISH.md           GitHub 自动部署教程
NO-SKILL-PROMPT.md          只有普通聊天 AI 也能尝试
TALK-DEMO.md                现场演示和备用方案
scripts/agenthub_lite.py    纯 Python 本地构建器
assets/                     可填写的 Markdown 模板
examples/student-demo/      虚构学生公开示例
references/cloudflare-pages.md 官方说明摘要
```

`examples/student-demo/docs/` 是演示用虚构资料，不能误当成自己的个人站点。生成站点需要审查源 Markdown 和 `docs/` 内所有文件。

## 使用边界

- 站点内容**面向所有人公开**，不要放任何私有或敏感信息；自动扫描只是辅助。
- 时间戳是「上次确认/生成时间」，不是实时状态或自动同步承诺。
- Cloudflare Pages 默认子域名通常是长期项目入口，但**中国大陆可访问性需要以实际网络实测为准**，不可保证三网始终可用。
- 现有 Direct Upload Pages 项目不能原地切换成 Git 集成项目；想用 Git 自动部署，需要新建 Git-integrated Pages 项目。
- 本仓库不替你创建 Cloudflare/GitHub 账号、不保存凭据、不执行公网发布；公开推送和授权需用户确认。

License: MIT。官方文档链接见 [`references/cloudflare-pages.md`](references/cloudflare-pages.md)。
