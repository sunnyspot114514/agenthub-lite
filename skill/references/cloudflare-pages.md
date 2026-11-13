# Cloudflare Pages 官方依据（2026-10-30）

- 静态网站 Git 集成、`exit 0` 和自定义构建输出路径（如 `docs`）：https://developers.cloudflare.com/pages/framework-guides/deploy-anything/
- 与 GitHub/GitLab 连接、推送后自动部署：https://developers.cloudflare.com/pages/get-started/git-integration/
- GitHub App 授权范围及建议只选必要仓库：https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/
- Direct Upload 支持拖拽文件夹/ZIP 或 Wrangler；**Direct Upload 无法原地切换 Git 集成**：https://developers.cloudflare.com/pages/get-started/direct-upload/
- Wrangler OAuth 登录（用户浏览器确认）：https://developers.cloudflare.com/workers/wrangler/commands/general/
- Wrangler Pages 命令：https://developers.cloudflare.com/workers/wrangler/commands/pages/
- Agent Skills 开放规范：https://agentskills.io/specification

**部署限制：** Cloudflare Pages 的海外全球网络不等于中国大陆专用网络。默认 `*.pages.dev` 是网站项目地址，而非保证国内三网或所有 Agent 的稳定访问服务。实际可用性请用校园网、手机数据及模型网页工具多次实测。

**账号边界：** 用户自己注册/登录 Cloudflare 与 GitHub；Agent 只在得到用户明确许可后执行上传或 Git 写入；不请求口令/验证码/Token，也不把凭据写入文本。
