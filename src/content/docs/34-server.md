---
title: '服务器'
description: '通过 HTTP 与 opencode 服务器交互。'
category: '开发'
order: 34
slug: 'server'
---

`opencode serve` 命令运行一个无界面的 HTTP 服务器，暴露一个 OpenAPI 端点供 opencode 客户端使用。
* * *
### 用法


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">serve</span><span style="--0:#24292E;--1:#E1E4E8"> [--port </span><span style="--0:#032F62;--1:#9ECBFF">&lt;number&gt;]</span><span style="--0:#24292E;--1:#E1E4E8"> [--hostname </span><span style="--0:#032F62;--1:#9ECBFF">&lt;string&gt;]</span><span style="--0:#24292E;--1:#E1E4E8"> [--cors </span><span style="--0:#032F62;--1:#9ECBFF">&lt;origin&gt;]</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode serve [--port &lt;number&gt;] [--hostname &lt;string&gt;] [--cors &lt;origin&gt;]" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


#### 选项
标志| 描述| 默认值  
---|---|---  
`--port`| 监听端口| `4096`  
`--hostname`| 监听的主机名| `127.0.0.1`  
`--mdns`| 启用 mDNS 发现| `false`  
`--mdns-domain`| mDNS 服务的自定义域名| `opencode.local`  
`--cors`| 额外允许的浏览器来源| `[]`  
`--cors` 可以多次传递：


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">serve</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#005CC5;--1:#79B8FF">--cors</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">http://localhost:5173</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#005CC5;--1:#79B8FF">--cors</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">https://app.example.com</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode serve --cors http://localhost:5173 --cors https://app.example.com" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### 认证
设置 `OPENCODE_SERVER_PASSWORD` 以使用 HTTP 基本认证保护服务器。用户名默认为 `opencode`，也可以设置 `OPENCODE_SERVER_USERNAME` 来覆盖它。这适用于 `opencode serve` 和 `opencode web`。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">OPENCODE_SERVER_PASSWORD</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#032F62;--1:#9ECBFF">your-password</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">serve</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="OPENCODE_SERVER_PASSWORD=your-password opencode serve" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### 工作原理
当你运行 `opencode` 时，它会启动一个 TUI 和一个服务器。TUI 是与服务器通信的客户端。服务器暴露一个 OpenAPI 3.1 规范端点。该端点也用于生成 [SDK](/docs/sdk)。


<aside aria-label="提示" class="starlight-aside starlight-aside--tip"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path clip-rule="evenodd" d="M1.43909 8.85483L1.44039 8.85354L4.96668 5.33815C5.30653 4.99386 5.7685 4.79662 6.2524 4.78972L6.26553 4.78963L12.9014 4.78962L13.8479 3.84308C16.9187 0.772319 20.0546 0.770617 21.4678 0.975145C21.8617 1.02914 22.2271 1.21053 22.5083 1.4917C22.7894 1.77284 22.9708 2.13821 23.0248 2.53199C23.2294 3.94517 23.2278 7.08119 20.1569 10.1521L19.2107 11.0983V17.7338L19.2106 17.7469C19.2037 18.2308 19.0067 18.6933 18.6624 19.0331L15.1456 22.5608C14.9095 22.7966 14.6137 22.964 14.29 23.0449C13.9663 23.1259 13.6267 23.1174 13.3074 23.0204C12.9881 22.9235 12.7011 22.7417 12.4771 22.4944C12.2533 22.2473 12.1006 21.9441 12.0355 21.6171L11.1783 17.3417L6.65869 12.822L4.34847 12.3589L2.38351 11.965C2.05664 11.8998 1.75272 11.747 1.50564 11.5232C1.25835 11.2992 1.07653 11.0122 0.979561 10.6929C0.882595 10.3736 0.874125 10.034 0.955057 9.7103C1.03599 9.38659 1.20328 9.09092 1.43909 8.85483ZM6.8186 10.8724L2.94619 10.096L6.32006 6.73268H10.9583L6.8186 10.8724ZM15.2219 5.21703C17.681 2.75787 20.0783 2.75376 21.1124 2.8876C21.2462 3.92172 21.2421 6.31895 18.783 8.77812L12.0728 15.4883L8.51172 11.9272L15.2219 5.21703ZM13.9042 21.0538L13.1279 17.1811L17.2676 13.0414V17.68L13.9042 21.0538Z" fill-rule="evenodd"></path><path d="M9.31827 18.3446C9.45046 17.8529 9.17864 17.3369 8.68945 17.1724C8.56178 17.1294 8.43145 17.1145 8.30512 17.1243C8.10513 17.1398 7.91519 17.2172 7.76181 17.3434C7.62613 17.455 7.51905 17.6048 7.45893 17.7835C6.97634 19.2186 5.77062 19.9878 4.52406 20.4029C4.08525 20.549 3.6605 20.644 3.29471 20.7053C3.35607 20.3395 3.45098 19.9148 3.59711 19.476C4.01221 18.2294 4.78141 17.0237 6.21648 16.5411C6.39528 16.481 6.54504 16.3739 6.65665 16.2382C6.85126 16.0016 6.92988 15.678 6.84417 15.3647C6.83922 15.3466 6.83373 15.3286 6.82767 15.3106C6.74106 15.053 6.55701 14.8557 6.33037 14.7459C6.10949 14.6389 5.84816 14.615 5.59715 14.6994C5.47743 14.7397 5.36103 14.7831 5.24786 14.8294C3.22626 15.6569 2.2347 17.4173 1.75357 18.8621C1.49662 19.6337 1.36993 20.3554 1.30679 20.8818C1.27505 21.1464 1.25893 21.3654 1.25072 21.5213C1.24662 21.5993 1.24448 21.6618 1.24337 21.7066L1.243 21.7226L1.24235 21.7605L1.2422 21.7771L1.24217 21.7827L1.24217 21.7856C1.24217 22.3221 1.67703 22.7579 2.2137 22.7579L2.2155 22.7579L2.22337 22.7578L2.23956 22.7577C2.25293 22.7575 2.27096 22.7572 2.29338 22.7567C2.33821 22.7555 2.40073 22.7534 2.47876 22.7493C2.63466 22.7411 2.85361 22.725 3.11822 22.6932C3.64462 22.6301 4.36636 22.5034 5.13797 22.2464C6.58274 21.7653 8.3431 20.7738 9.17063 18.7522C9.21696 18.639 9.26037 18.5226 9.30064 18.4029C9.30716 18.3835 9.31304 18.364 9.31827 18.3446Z"></path></svg>提示</p><div class="starlight-aside__content"><p>使用 opencode 服务器以编程方式与 opencode 交互。</p></div></aside>


这种架构让 opencode 支持多个客户端，并允许你以编程方式与 opencode 交互。
你可以运行 `opencode serve` 来启动一个独立的服务器。如果你已经在运行 opencode TUI，`opencode serve` 会启动一个新的服务器。
* * *
#### 连接到现有服务器
当你启动 TUI 时，它会随机分配端口和主机名。你也可以传入 `--hostname` 和 `--port` [标志](/docs/cli)，然后用它来连接对应的服务器。
[`/tui`](#tui) 端点可用于通过服务器驱动 TUI。例如，你可以预填充或运行一个提示词。此方式被 OpenCode [IDE](/docs/ide) 插件所使用。
* * *
## 规范
服务器发布了一个 OpenAPI 3.1 规范，可在以下地址查看：


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="plaintext"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">http://&lt;hostname&gt;:&lt;port&gt;/doc</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="http://&lt;hostname&gt;:&lt;port&gt;/doc" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


例如，`http://localhost:4096/doc`。使用该规范可以生成客户端或检查请求和响应类型，也可以在 Swagger 浏览器中查看。
* * *
## API
opencode 服务器暴露以下 API。
* * *
### 全局
方法| 路径| 描述| 响应  
---|---|---|---  
`GET`| `/global/health`| 获取服务器健康状态和版本| `{ healthy: true, version: string }`  
`GET`| `/global/event`| 获取全局事件（SSE 流）| 事件流  
* * *
### 项目
方法| 路径| 描述| 响应  
---|---|---|---  
`GET`| `/project`| 列出所有项目| [`Project[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/project/current`| 获取当前项目| [`Project`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
* * *
### 路径和 VCS
方法| 路径| 描述| 响应  
---|---|---|---  
`GET`| `/path`| 获取当前路径| [`Path`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/vcs`| 获取当前项目的 VCS 信息| [`VcsInfo`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
* * *
### 实例
方法| 路径| 描述| 响应  
---|---|---|---  
`POST`| `/instance/dispose`| 销毁当前实例| `boolean`  
* * *
### 配置
方法| 路径| 描述| 响应  
---|---|---|---  
`GET`| `/config`| 获取配置信息| [`Config`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`PATCH`| `/config`| 更新配置| [`Config`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/config/providers`| 列出提供商和默认模型| `{ providers: `[Provider[]](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, default: { [key: string]: string } }`  
* * *
### 提供商
方法| 路径| 描述| 响应  
---|---|---|---  
`GET`| `/provider`| 列出所有提供商| `{ all: `[Provider[]](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, default: {...}, connected: string[] }`  
`GET`| `/provider/auth`| 获取提供商认证方式| `{ [providerID: string]: `[ProviderAuthMethod[]](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)` }`  
`POST`| `/provider/{id}/oauth/authorize`| 使用 OAuth 授权提供商| [`ProviderAuthAuthorization`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`POST`| `/provider/{id}/oauth/callback`| 处理提供商的 OAuth 回调| `boolean`  
* * *
### 会话
方法| 路径| 描述| 说明  
---|---|---|---  
`GET`| `/session`| 列出所有会话| 返回 [`Session[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`POST`| `/session`| 创建新会话| 请求体：`{ parentID?, title? }`，返回 [`Session`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/session/status`| 获取所有会话的状态| 返回 `{ [sessionID: string]: `[SessionStatus](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)` }`  
`GET`| `/session/:id`| 获取会话详情| 返回 [`Session`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`DELETE`| `/session/:id`| 删除会话及其所有数据| 返回 `boolean`  
`PATCH`| `/session/:id`| 更新会话属性| 请求体：`{ title? }`，返回 [`Session`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/session/:id/children`| 获取会话的子会话| 返回 [`Session[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/session/:id/todo`| 获取会话的待办事项列表| 返回 [`Todo[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`POST`| `/session/:id/init`| 分析应用并创建 `AGENTS.md`| 请求体：`{ messageID, providerID, modelID }`，返回 `boolean`  
`POST`| `/session/:id/fork`| 在某条消息处分叉现有会话| 请求体：`{ messageID? }`，返回 [`Session`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`POST`| `/session/:id/abort`| 中止正在运行的会话| 返回 `boolean`  
`POST`| `/session/:id/share`| 分享会话| 返回 [`Session`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`DELETE`| `/session/:id/share`| 取消分享会话| 返回 [`Session`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/session/:id/diff`| 获取本次会话的差异| 查询参数：`messageID?`，返回 [`FileDiff[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`POST`| `/session/:id/summarize`| 总结会话| 请求体：`{ providerID, modelID }`，返回 `boolean`  
`POST`| `/session/:id/revert`| 回退消息| 请求体：`{ messageID, partID? }`，返回 `boolean`  
`POST`| `/session/:id/unrevert`| 恢复所有已回退的消息| 返回 `boolean`  
`POST`| `/session/:id/permissions/:permissionID`| 响应权限请求| 请求体：`{ response, remember? }`，返回 `boolean`  
* * *
### 消息
方法| 路径| 描述| 说明  
---|---|---|---  
`GET`| `/session/:id/message`| 列出会话中的消息| 查询参数：`limit?`，返回 `{ info: `[Message](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, parts: `[Part[]](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`}[]`  
`POST`| `/session/:id/message`| 发送消息并等待响应| 请求体：`{ messageID?, model?, agent?, noReply?, system?, tools?, parts }`，返回 `{ info: `[Message](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, parts: `[Part[]](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`}`  
`GET`| `/session/:id/message/:messageID`| 获取消息详情| 返回 `{ info: `[Message](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, parts: `[Part[]](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`}`  
`POST`| `/session/:id/prompt_async`| 异步发送消息（不等待响应）| 请求体：与 `/session/:id/message` 相同，返回 `204 No Content`  
`POST`| `/session/:id/command`| 执行斜杠命令| 请求体：`{ messageID?, agent?, model?, command, arguments }`，返回 `{ info: `[Message](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, parts: `[Part[]](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`}`  
`POST`| `/session/:id/shell`| 运行 shell 命令| 请求体：`{ agent, model?, command }`，返回 `{ info: `[Message](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, parts: `[Part[]](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`}`  
* * *
### 命令
方法| 路径| 描述| 响应  
---|---|---|---  
`GET`| `/command`| 列出所有命令| [`Command[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
* * *
### 文件
方法| 路径| 描述| 响应  
---|---|---|---  
`GET`| `/find?pattern=<pat>`| 在文件中搜索文本| 包含 `path`、`lines`、`line_number`、`absolute_offset`、`submatches` 的匹配对象数组  
`GET`| `/find/file?query=<q>`| 按名称查找文件和目录| `string[]`（路径）  
`GET`| `/find/symbol?query=<q>`| 查找工作区符号| [`Symbol[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/file?path=<path>`| 列出文件和目录| [`FileNode[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/file/content?path=<p>`| 读取文件| [`FileContent`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/file/status`| 获取已跟踪文件的状态| [`File[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
#### `/find/file` 查询参数
  * `query`（必需）— 搜索字符串（模糊匹配）
  * `type`（可选）— 将结果限制为 `"file"` 或 `"directory"`
  * `directory`（可选）— 覆盖搜索的项目根目录
  * `limit`（可选）— 最大结果数（1–200）
  * `dirs`（可选）— 旧版标志（`"false"` 仅返回文件）


* * *
### 工具（实验性）
方法| 路径| 描述| 响应  
---|---|---|---  
`GET`| `/experimental/tool/ids`| 列出所有工具 ID| [`ToolIDs`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/experimental/tool?provider=<p>&model=<m>`| 列出指定模型的工具及其 JSON Schema| [`ToolList`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
* * *
### LSP、格式化器和 MCP
方法| 路径| 描述| 响应  
---|---|---|---  
`GET`| `/lsp`| 获取 LSP 服务器状态| [`LSPStatus[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/formatter`| 获取格式化器状态| [`FormatterStatus[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/mcp`| 获取 MCP 服务器状态| `{ [name: string]: `[MCPStatus](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)` }`  
`POST`| `/mcp`| 动态添加 MCP 服务器| 请求体：`{ name, config }`，返回 MCP 状态对象  
* * *
### 代理
方法| 路径| 描述| 响应  
---|---|---|---  
`GET`| `/agent`| 列出所有可用的代理| [`Agent[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
* * *
### 日志
方法| 路径| 描述| 响应  
---|---|---|---  
`POST`| `/log`| 写入日志条目。请求体：`{ service, level, message, extra? }`| `boolean`  
* * *
### TUI
方法| 路径| 描述| 响应  
---|---|---|---  
`POST`| `/tui/append-prompt`| 向提示词追加文本| `boolean`  
`POST`| `/tui/open-help`| 打开帮助对话框| `boolean`  
`POST`| `/tui/open-sessions`| 打开会话选择器| `boolean`  
`POST`| `/tui/open-themes`| 打开主题选择器| `boolean`  
`POST`| `/tui/open-models`| 打开模型选择器| `boolean`  
`POST`| `/tui/submit-prompt`| 提交当前提示词| `boolean`  
`POST`| `/tui/clear-prompt`| 清除提示词| `boolean`  
`POST`| `/tui/execute-command`| 执行命令（`{ command }`）| `boolean`  
`POST`| `/tui/show-toast`| 显示提示消息（`{ title?, message, variant }`）| `boolean`  
`GET`| `/tui/control/next`| 等待下一个控制请求| 控制请求对象  
`POST`| `/tui/control/response`| 响应控制请求（`{ body }`）| `boolean`  
* * *
### 认证
方法| 路径| 描述| 响应  
---|---|---|---  
`PUT`| `/auth/:id`| 设置认证凭据。请求体必须匹配提供商的数据结构| `boolean`  
* * *
### 事件
方法| 路径| 描述| 响应  
---|---|---|---  
`GET`| `/event`| 服务器发送事件流。第一个事件是 `server.connected`，之后是总线事件| 服务器发送事件流  
* * *
### 文档
方法| 路径| 描述| 响应  
---|---|---|---  
`GET`| `/doc`| OpenAPI 3.1 规范| 包含 OpenAPI 规范的 HTML 页面