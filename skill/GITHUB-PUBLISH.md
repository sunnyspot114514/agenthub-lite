# GitHub + Cloudflare Pages：长期维护的公开个人 AgentHub Lite

> GitHub 是**版本化的源代码仓库**，Cloudflare Pages 是**公开展示与 Agent 可读的发布站点**。Skill 帮助生成和审核内容，但不会未经授权自动 push/publish。

## 推荐仓库分工

- 教学代码与 Skill：公开仓库 `agenthub-lite`（本 Starter）。
- 每位学生自己的项目上下文：另一份 GitHub 仓库 `my-agenthub-lite`（可选，不是强制）。

请不要把所有同学的个人资料都往教学仓库提 PR。个人站点应由个人控制；私有源码仓库的 Pages 部署产物同样可能被任何访问者看到。

## 1. 生成个人站点

在本 Starter 根目录：

```bash
python scripts/agenthub_lite.py init my-agenthub-lite
# 审核并编辑 my-agenthub-lite/context.md、projects/、changelog.md
python scripts/agenthub_lite.py check my-agenthub-lite
python scripts/agenthub_lite.py build my-agenthub-lite
```

把 `my-agenthub-lite` 作为一个独立的 GitHub 仓库；至少需要源 Markdown 和生成的 `docs/`，并人工确认没有非公开资料。可以用 GitHub 网站新建仓库，再由本人或获得明确授权的 Agent 提交、推送。**不需要把 Cloudflare 的密钥存到 GitHub。**

## 2. 连接 Cloudflare Pages

1. 本人登录 Cloudflare，进入 Workers & Pages，新建 Pages **Git integration** 项目（不是 Direct Upload）。
2. 在 GitHub 安装 Cloudflare Pages GitHub App，授权**仅需要的仓库**。
3. 选择刚创建的个人站点仓库，生产分支 `main`。
4. 静态站无需前端框架：`Build command` 填 `exit 0`，`Build output directory` 填 `docs`（前提是 `docs/` 已提交）。
5. 创建部署。得到 Pages 返回的正式项目 URL 后，检查 `/context.txt` 和 `/llms.txt`。

首次部署成功后，在本地更新 Markdown → 检查 → `build` → 审核 → commit/push 到 GitHub，即可由 Cloudflare 根据该仓库配置自动部署。

## 3. 已经建了 Direct Upload 项目？

Cloudflare 官方明确：**Direct Upload 项目不能切换成 Git 集成**。可选择：
- 继续原项目：本人通过控制台上传 `docs/`，或登录 Wrangler 后执行 `npx wrangler pages deploy my-agenthub-lite/docs --project-name=YOUR_PROJECT`。
- 想享受 Git 推送自动部署：另建 Git-integrated Pages 项目，再决定是否将自定义域名迁移过去。不要误以为会沿用已有 `*.pages.dev` 域名。

## 4. 安全与复现

- 请在每次发布前检查源文件和生成网站；更改站点后要记录绝对更新日期。
- Git 仓库提交历史也可能保留误传的机密；意外泄露应立即撤销/轮换密钥，不要仅删除最新文件。
- 用不同的 AI 和网络测试真实网页读取。失败时保留本地文本交接方案。

官方：
- [Cloudflare Pages Static HTML](https://developers.cloudflare.com/pages/framework-guides/deploy-anything/)
- [Git Integration](https://developers.cloudflare.com/pages/configuration/git-integration/)
- [Direct Upload](https://developers.cloudflare.com/pages/get-started/direct-upload/)
