---
title: 'CLI'
description: 'OpenCode CLI 选项和命令。'
category: 'OpenCode 开发手册'
order: 10
slug: 'opencode/cli'
---

OpenCode CLI 在不带任何参数运行时，默认启动 [TUI](/docs/tui)。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


但它也接受本页面中记录的命令，使您可以通过编程方式与 OpenCode 进行交互。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">run</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">"Explain how closures work in JavaScript"</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='opencode run "Explain how closures work in JavaScript"' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### tui
启动 OpenCode 终端用户界面。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> [project]</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode [project]" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


#### 标志
标志| 简写| 描述  
---|---|---  
`--continue`| `-c`| 继续上一个会话  
`--session`| `-s`| 要继续的会话 ID  
`--fork`| | 继续时分叉会话（与 `--continue` 或 `--session` 配合使用）  
`--prompt`| | 要使用的提示词  
`--model`| `-m`| 要使用的模型，格式为 provider/model  
`--agent`| | 要使用的代理  
`--port`| | 监听端口  
`--hostname`| | 监听主机名  
* * *
## 命令
OpenCode CLI 还提供以下命令。
* * *
### agent
管理 OpenCode 的代理。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">agent</span><span style="--0:#24292E;--1:#E1E4E8"> [command]</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode agent [command]" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### attach
将终端连接到已通过 `serve` 或 `web` 命令启动的 OpenCode 后端服务器。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">attach</span><span style="--0:#24292E;--1:#E1E4E8"> [url]</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode attach [url]" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


这允许将 TUI 与远程 OpenCode 后端配合使用。例如：


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#616972;--1:#99A0A6"># Start the backend server for web/mobile access</span></div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">web</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#005CC5;--1:#79B8FF">--port</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#005CC5;--1:#79B8FF">4096</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#005CC5;--1:#79B8FF">--hostname</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#005CC5;--1:#79B8FF">0.0.0.0</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#616972;--1:#99A0A6"># In another terminal, attach the TUI to the running backend</span></div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">attach</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">http://10.20.30.40:4096</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode web --port 4096 --hostname 0.0.0.0opencode attach http://10.20.30.40:4096" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


#### 标志
标志| 简写| 描述  
---|---|---  
`--dir`| | 启动 TUI 的工作目录  
`--continue`| `-c`| 继续上一个会话  
`--session`| `-s`| 要继续的会话 ID  
`--fork`| | 继续时派生会话（与 `--continue` 或 `--session` 一起使用）  
`--password`| `-p`| 基本认证密码（默认使用 `OPENCODE_SERVER_PASSWORD`）  
`--username`| `-u`| 基本认证用户名（默认使用 `OPENCODE_SERVER_USERNAME` 或 `opencode`）  
* * *
#### create
使用自定义配置创建新的代理。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">agent</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">create</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode agent create" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


此命令将引导您使用自定义系统提示词和工具配置来创建新的代理。
* * *
#### list
列出所有可用的代理。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">agent</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">list</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode agent list" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### auth
管理提供商的凭据和登录信息的命令。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">auth</span><span style="--0:#24292E;--1:#E1E4E8"> [command]</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode auth [command]" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
#### login
OpenCode 基于 [Models.dev](https://models.dev) 的提供商列表运行，因此您可以使用 `opencode auth login` 为任何想要使用的提供商配置 API 密钥。密钥存储在 `~/.local/share/opencode/auth.json` 中。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">auth</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">login</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode auth login" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


OpenCode 启动时会从凭据文件加载提供商信息，同时也会加载环境变量或项目中 `.env` 文件中定义的密钥。
* * *
#### list
列出凭据文件中存储的所有已认证提供商。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">auth</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">list</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode auth list" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


或使用简写版本。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">auth</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">ls</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode auth ls" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
#### logout
从凭据文件中清除提供商信息以完成登出。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">auth</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">logout</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode auth logout" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### github
管理用于仓库自动化的 GitHub 代理。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">github</span><span style="--0:#24292E;--1:#E1E4E8"> [command]</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode github [command]" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
#### install
在您的仓库中安装 GitHub 代理。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">github</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">install</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode github install" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


此命令会设置必要的 GitHub Actions 工作流并引导您完成配置过程。[了解更多](/docs/github)。
* * *
#### run
运行 GitHub 代理。通常在 GitHub Actions 中使用。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">github</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">run</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode github run" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


##### 标志
标志| 描述  
---|---  
`--event`| 用于运行代理的 GitHub 模拟事件  
`--token`| GitHub 个人访问令牌  
* * *
### mcp
管理 Model Context Protocol 服务器。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">mcp</span><span style="--0:#24292E;--1:#E1E4E8"> [command]</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode mcp [command]" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
#### add
将 MCP 服务器添加到您的配置中。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">mcp</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">add</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode mcp add" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


此命令将引导您添加本地或远程 MCP 服务器。
* * *
#### list
列出所有已配置的 MCP 服务器及其连接状态。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">mcp</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">list</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode mcp list" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


或使用简写版本。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">mcp</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">ls</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode mcp ls" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
#### auth
对支持 OAuth 的 MCP 服务器进行认证。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">mcp</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">auth</span><span style="--0:#24292E;--1:#E1E4E8"> [name]</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode mcp auth [name]" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


如果您不提供服务器名称，系统将提示您从可用的支持 OAuth 的服务器中进行选择。
您还可以列出支持 OAuth 的服务器及其认证状态。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">mcp</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">auth</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">list</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode mcp auth list" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


或使用简写版本。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">mcp</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">auth</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">ls</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode mcp auth ls" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
#### logout
移除 MCP 服务器的 OAuth 凭据。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">mcp</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">logout</span><span style="--0:#24292E;--1:#E1E4E8"> [name]</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode mcp logout [name]" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
#### debug
调试 MCP 服务器的 OAuth 连接问题。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">mcp</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">debug</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">&lt;name&gt;</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode mcp debug &lt;name&gt;" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### models
列出已配置提供商的所有可用模型。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">models</span><span style="--0:#24292E;--1:#E1E4E8"> [provider]</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode models [provider]" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


此命令以 `provider/model` 的格式显示所有已配置提供商中可用的模型。
这对于确定在[配置文件](/docs/config/)中使用的确切模型名称非常有用。
您可以选择传入提供商 ID 来按提供商筛选模型。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">models</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">anthropic</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode models anthropic" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


#### 标志
标志| 描述  
---|---  
`--refresh`| 从 models.dev 刷新模型缓存  
`--verbose`| 使用更详细的模型输出（包含费用等元数据）  
使用 `--refresh` 标志可以更新缓存的模型列表。当提供商新增了模型并且您希望在 OpenCode 中看到它们时，此功能非常有用。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">models</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#005CC5;--1:#79B8FF">--refresh</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode models --refresh" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### run
以非交互模式运行 OpenCode，直接传入提示词。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">run</span><span style="--0:#24292E;--1:#E1E4E8"> [message..]</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode run [message..]" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


这对于脚本编写、自动化或无需启动完整 TUI 即可快速获取答案的场景非常有用。例如：


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><mark><span style="--0:#5c37a0;--1:#c5acf4">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">run</span></mark><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">Explain</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">the</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">use</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">of</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">context</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">in</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">Go</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode run Explain the use of context in Go" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


您还可以连接到正在运行的 `opencode serve` 实例，以避免每次运行时 MCP 服务器的冷启动时间：


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#616972;--1:#99A0A6"># Start a headless server in one terminal</span></div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">serve</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#616972;--1:#99A0A6"># In another terminal, run commands that attach to it</span></div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">run</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#005CC5;--1:#79B8FF">--attach</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">http://localhost:4096</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">"Explain async/await in JavaScript"</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='opencode serveopencode run --attach http://localhost:4096 "Explain async/await in JavaScript"' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


#### 标志
标志| 简写| 描述  
---|---|---  
`--command`| | 要运行的命令，使用 message 作为参数  
`--continue`| `-c`| 继续上一个会话  
`--session`| `-s`| 要继续的会话 ID  
`--fork`| | 继续时分叉会话（与 `--continue` 或 `--session` 配合使用）  
`--share`| | 分享会话  
`--model`| `-m`| 要使用的模型，格式为 provider/model  
`--agent`| | 要使用的代理  
`--file`| `-f`| 附加到消息的文件  
`--format`| | 格式：default（格式化输出）或 json（原始 JSON 事件）  
`--title`| | 会话标题（未提供值时使用截断的提示词）  
`--attach`| | 连接到正在运行的 opencode 服务器（例如 [http://localhost:4096）](http://localhost:4096%EF%BC%89)  
`--password`| `-p`| 基本认证密码（默认使用 `OPENCODE_SERVER_PASSWORD`）  
`--username`| `-u`| 基本认证用户名（默认使用 `OPENCODE_SERVER_USERNAME` 或 `opencode`）  
`--dir`| | 运行目录，或附加时远程服务器上的路径  
`--variant`| | 模型变体（特定于提供商的推理级别）  
`--thinking`| | 显示思考块  
`--port`| | 本地服务器端口（默认为随机端口）  
* * *
### serve
启动无界面的 OpenCode 服务器以提供 API 访问。查看[服务器文档](/docs/server)了解完整的 HTTP 接口。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">serve</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode serve" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


此命令启动一个 HTTP 服务器，提供对 OpenCode 功能的 API 访问，无需 TUI 界面。设置 `OPENCODE_SERVER_PASSWORD` 可启用 HTTP 基本认证（用户名默认为 `opencode`）。
#### 标志
标志| 描述  
---|---  
`--port`| 监听端口  
`--hostname`| 监听主机名  
`--mdns`| 启用 mDNS 发现  
`--cors`| 允许 CORS 的额外浏览器来源  
* * *
### session
管理 OpenCode 会话。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">session</span><span style="--0:#24292E;--1:#E1E4E8"> [command]</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode session [command]" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
#### list
列出所有 OpenCode 会话。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">session</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">list</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode session list" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


##### 标志
标志| 简写| 描述  
---|---|---  
`--max-count`| `-n`| 限制为最近 N 个会话  
`--format`| | 输出格式：table 或 json（默认 table）  
* * *
### stats
显示 OpenCode 会话的 Token 用量和费用统计信息。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">stats</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode stats" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


#### 标志
标志| 描述  
---|---  
`--days`| 显示最近 N 天的统计信息（默认为所有时间）  
`--tools`| 显示的工具数量（默认为全部）  
`--models`| 显示模型用量明细（默认隐藏）。传入数字可显示前 N 个  
`--project`| 按项目筛选（默认为所有项目，传入空字符串表示当前项目）  
* * *
### export
将会话数据导出为 JSON。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">export</span><span style="--0:#24292E;--1:#E1E4E8"> [sessionID]</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode export [sessionID]" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


如果您不提供会话 ID，系统将提示您从可用的会话中进行选择。
* * *
### import
从 JSON 文件或 OpenCode 分享链接导入会话数据。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">import</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">&lt;file&gt;</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode import &lt;file&gt;" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


您可以从本地文件或 OpenCode 分享链接导入。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">import</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">session.json</span></div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">import</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">https://opncd.ai/s/abc123</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode import session.jsonopencode import https://opncd.ai/s/abc123" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### web
启动带有 Web 界面的无界面 OpenCode 服务器。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">web</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode web" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


此命令启动一个 HTTP 服务器并打开浏览器，通过 Web 界面访问 OpenCode。设置 `OPENCODE_SERVER_PASSWORD` 可启用 HTTP 基本认证（用户名默认为 `opencode`）。
#### 标志
标志| 描述  
---|---  
`--port`| 监听端口  
`--hostname`| 监听主机名  
`--mdns`| 启用 mDNS 发现  
`--cors`| 允许 CORS 的额外浏览器来源  
* * *
### acp
启动 ACP（Agent Client Protocol）服务器。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">acp</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode acp" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


此命令启动一个通过 stdin/stdout 使用 nd-JSON 进行通信的 ACP 服务器。
#### 标志
标志| 描述  
---|---  
`--cwd`| 工作目录  
`--port`| 监听端口  
`--hostname`| 监听主机名  
* * *
### uninstall
卸载 OpenCode 并删除所有相关文件。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">uninstall</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode uninstall" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


#### 标志
标志| 简写| 描述  
---|---|---  
`--keep-config`| `-c`| 保留配置文件  
`--keep-data`| `-d`| 保留会话数据和快照  
`--dry-run`| | 显示将被删除的内容但不实际删除  
`--force`| `-f`| 跳过确认提示  
* * *
### upgrade
将 OpenCode 更新到最新版本或指定版本。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">upgrade</span><span style="--0:#24292E;--1:#E1E4E8"> [target]</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode upgrade [target]" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


更新到最新版本。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">upgrade</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode upgrade" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


更新到指定版本。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">upgrade</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">v0.1.48</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode upgrade v0.1.48" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


#### 标志
标志| 简写| 描述  
---|---|---  
`--method`| `-m`| 使用的安装方式：curl、npm、pnpm、bun、brew  
* * *
## 全局标志
OpenCode CLI 接受以下全局标志。
标志| 简写| 描述  
---|---|---  
`--help`| `-h`| 显示帮助信息  
`--version`| `-v`| 打印版本号  
`--print-logs`| | 将日志输出到 stderr  
`--log-level`| | 日志级别（DEBUG、INFO、WARN、ERROR）  
* * *
## 环境变量
OpenCode 可以通过环境变量进行配置。
变量| 类型| 描述  
---|---|---  
`OPENCODE_AUTO_SHARE`| boolean| 自动分享会话  
`OPENCODE_GIT_BASH_PATH`| string| Windows 上 Git Bash 可执行文件的路径  
`OPENCODE_CONFIG`| string| 配置文件路径  
`OPENCODE_TUI_CONFIG`| string| TUI 配置文件路径  
`OPENCODE_CONFIG_DIR`| string| 配置目录路径  
`OPENCODE_CONFIG_CONTENT`| string| 内联 JSON 配置内容  
`OPENCODE_DISABLE_AUTOUPDATE`| boolean| 禁用自动更新检查  
`OPENCODE_DISABLE_PRUNE`| boolean| 禁用旧数据清理  
`OPENCODE_DISABLE_TERMINAL_TITLE`| boolean| 禁用自动终端标题更新  
`OPENCODE_PERMISSION`| string| 内联 JSON 权限配置  
`OPENCODE_DISABLE_DEFAULT_PLUGINS`| boolean| 禁用默认插件  
`OPENCODE_DISABLE_LSP_DOWNLOAD`| boolean| 禁用 LSP 服务器自动下载  
`OPENCODE_ENABLE_EXPERIMENTAL_MODELS`| boolean| 启用实验性模型  
`OPENCODE_DISABLE_AUTOCOMPACT`| boolean| 禁用自动上下文压缩  
`OPENCODE_DISABLE_CLAUDE_CODE`| boolean| 禁用读取 `.claude`（提示词 + 技能）  
`OPENCODE_DISABLE_CLAUDE_CODE_PROMPT`| boolean| 禁用读取 `~/.claude/CLAUDE.md`  
`OPENCODE_DISABLE_CLAUDE_CODE_SKILLS`| boolean| 禁用加载 `.claude/skills`  
`OPENCODE_DISABLE_MODELS_FETCH`| boolean| 禁用从远程源获取模型  
`OPENCODE_FAKE_VCS`| string| 用于测试目的的模拟 VCS 提供商  
`OPENCODE_CLIENT`| string| 客户端标识符（默认为 `cli`）  
`OPENCODE_ENABLE_EXA`| boolean| 启用 Exa 网络搜索工具  
`OPENCODE_SERVER_PASSWORD`| string| 为 `serve`/`web` 启用基本认证  
`OPENCODE_SERVER_USERNAME`| string| 覆盖基本认证用户名（默认为 `opencode`）  
`OPENCODE_MODELS_URL`| string| 自定义模型配置获取 URL  
* * *
### 实验性功能
这些环境变量用于启用可能会更改或移除的实验性功能。
变量| 类型| 描述  
---|---|---  
`OPENCODE_EXPERIMENTAL`| boolean| 启用受总开关控制的实验性功能  
`OPENCODE_EXPERIMENTAL_ICON_DISCOVERY`| boolean| 启用图标发现  
`OPENCODE_EXPERIMENTAL_DISABLE_COPY_ON_SELECT`| boolean| 禁用 TUI 中的选中即复制  
`OPENCODE_EXPERIMENTAL_BASH_DEFAULT_TIMEOUT_MS`| number| bash 命令的默认超时时间（毫秒）  
`OPENCODE_EXPERIMENTAL_OUTPUT_TOKEN_MAX`| number| LLM 响应的最大输出 Token 数  
`OPENCODE_EXPERIMENTAL_FILEWATCHER`| boolean| 启用整个目录的文件监听器  
`OPENCODE_EXPERIMENTAL_OXFMT`| boolean| 启用 oxfmt 格式化器  
`OPENCODE_EXPERIMENTAL_LSP_TOOL`| boolean| 启用实验性 LSP 工具  
`OPENCODE_EXPERIMENTAL_DISABLE_FILEWATCHER`| boolean| 禁用文件监听器  
`OPENCODE_EXPERIMENTAL_EXA`| boolean| 启用实验性 Exa 功能  
`OPENCODE_EXPERIMENTAL_LSP_TY`| boolean| 为 python 文件启用 TY LSP  
`OPENCODE_EXPERIMENTAL_PLAN_MODE`| boolean| 启用计划模式  
`OPENCODE_EXPERIMENTAL_BACKGROUND_SUBAGENTS`| boolean| 启用后台子代理任务  
`OPENCODE_EXPERIMENTAL_EVENT_SYSTEM`| boolean| 启用实验性事件系统  
`OPENCODE_EXPERIMENTAL_NATIVE_LLM`| boolean| 启用原生 LLM 请求路径  
`OPENCODE_EXPERIMENTAL_PARALLEL`| boolean| 启用并行 Web 搜索执行  
`OPENCODE_EXPERIMENTAL_SCOUT`| boolean| 启用 Scout 子代理  
`OPENCODE_EXPERIMENTAL_WORKSPACES`| boolean| 启用工作区支持