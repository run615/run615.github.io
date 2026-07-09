---
title: '规则'
description: '为 opencode 设置自定义指令。'
category: 'OpenCode 开发手册'
order: 18
slug: 'opencode/rules'
---

您可以通过创建 `AGENTS.md` 文件来为 opencode 提供自定义指令。这类似于 Cursor 的规则功能。该文件包含的指令会被纳入 LLM 的上下文中，以便针对您的特定项目自定义其行为。
* * *
## 初始化
要创建新的 `AGENTS.md` 文件，您可以在 opencode 中运行 `/init` 命令。


<aside aria-label="提示" class="starlight-aside starlight-aside--tip"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path clip-rule="evenodd" d="M1.43909 8.85483L1.44039 8.85354L4.96668 5.33815C5.30653 4.99386 5.7685 4.79662 6.2524 4.78972L6.26553 4.78963L12.9014 4.78962L13.8479 3.84308C16.9187 0.772319 20.0546 0.770617 21.4678 0.975145C21.8617 1.02914 22.2271 1.21053 22.5083 1.4917C22.7894 1.77284 22.9708 2.13821 23.0248 2.53199C23.2294 3.94517 23.2278 7.08119 20.1569 10.1521L19.2107 11.0983V17.7338L19.2106 17.7469C19.2037 18.2308 19.0067 18.6933 18.6624 19.0331L15.1456 22.5608C14.9095 22.7966 14.6137 22.964 14.29 23.0449C13.9663 23.1259 13.6267 23.1174 13.3074 23.0204C12.9881 22.9235 12.7011 22.7417 12.4771 22.4944C12.2533 22.2473 12.1006 21.9441 12.0355 21.6171L11.1783 17.3417L6.65869 12.822L4.34847 12.3589L2.38351 11.965C2.05664 11.8998 1.75272 11.747 1.50564 11.5232C1.25835 11.2992 1.07653 11.0122 0.979561 10.6929C0.882595 10.3736 0.874125 10.034 0.955057 9.7103C1.03599 9.38659 1.20328 9.09092 1.43909 8.85483ZM6.8186 10.8724L2.94619 10.096L6.32006 6.73268H10.9583L6.8186 10.8724ZM15.2219 5.21703C17.681 2.75787 20.0783 2.75376 21.1124 2.8876C21.2462 3.92172 21.2421 6.31895 18.783 8.77812L12.0728 15.4883L8.51172 11.9272L15.2219 5.21703ZM13.9042 21.0538L13.1279 17.1811L17.2676 13.0414V17.68L13.9042 21.0538Z" fill-rule="evenodd"></path><path d="M9.31827 18.3446C9.45046 17.8529 9.17864 17.3369 8.68945 17.1724C8.56178 17.1294 8.43145 17.1145 8.30512 17.1243C8.10513 17.1398 7.91519 17.2172 7.76181 17.3434C7.62613 17.455 7.51905 17.6048 7.45893 17.7835C6.97634 19.2186 5.77062 19.9878 4.52406 20.4029C4.08525 20.549 3.6605 20.644 3.29471 20.7053C3.35607 20.3395 3.45098 19.9148 3.59711 19.476C4.01221 18.2294 4.78141 17.0237 6.21648 16.5411C6.39528 16.481 6.54504 16.3739 6.65665 16.2382C6.85126 16.0016 6.92988 15.678 6.84417 15.3647C6.83922 15.3466 6.83373 15.3286 6.82767 15.3106C6.74106 15.053 6.55701 14.8557 6.33037 14.7459C6.10949 14.6389 5.84816 14.615 5.59715 14.6994C5.47743 14.7397 5.36103 14.7831 5.24786 14.8294C3.22626 15.6569 2.2347 17.4173 1.75357 18.8621C1.49662 19.6337 1.36993 20.3554 1.30679 20.8818C1.27505 21.1464 1.25893 21.3654 1.25072 21.5213C1.24662 21.5993 1.24448 21.6618 1.24337 21.7066L1.243 21.7226L1.24235 21.7605L1.2422 21.7771L1.24217 21.7827L1.24217 21.7856C1.24217 22.3221 1.67703 22.7579 2.2137 22.7579L2.2155 22.7579L2.22337 22.7578L2.23956 22.7577C2.25293 22.7575 2.27096 22.7572 2.29338 22.7567C2.33821 22.7555 2.40073 22.7534 2.47876 22.7493C2.63466 22.7411 2.85361 22.725 3.11822 22.6932C3.64462 22.6301 4.36636 22.5034 5.13797 22.2464C6.58274 21.7653 8.3431 20.7738 9.17063 18.7522C9.21696 18.639 9.26037 18.5226 9.30064 18.4029C9.30716 18.3835 9.31304 18.364 9.31827 18.3446Z"></path></svg>提示</p><div class="starlight-aside__content"><p>您应该将项目的 <code dir="auto">AGENTS.md</code> 文件提交到 Git。</p></div></aside>


该命令会扫描您的项目及其所有内容，了解项目的用途，并据此生成一个 `AGENTS.md` 文件。这有助于 opencode 更好地导航您的项目。
如果您已有 `AGENTS.md` 文件，该命令会尝试在其基础上进行补充。
* * *
## 示例
您也可以手动创建此文件。以下是一些可以放入 `AGENTS.md` 文件中的内容示例。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">AGENTS.md</span></figcaption><pre data-language="markdown"><code><div class="ec-line"><div class="code"><span style="--0:#005CC5;--0fw:bold;--1:#79B8FF;--1fw:bold"># SST v3 Monorepo Project</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">This is an SST v3 monorepo with TypeScript. The project uses bun workspaces for package management.</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#005CC5;--0fw:bold;--1:#79B8FF;--1fw:bold">## Project Structure</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#AE4B07;--1:#FFAB70">-</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#005CC5;--1:#79B8FF">`packages/`</span><span style="--0:#24292E;--1:#E1E4E8"> - Contains all workspace packages (functions, core, web, etc.)</span></div></div><div class="ec-line"><div class="code"><span style="--0:#AE4B07;--1:#FFAB70">-</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#005CC5;--1:#79B8FF">`infra/`</span><span style="--0:#24292E;--1:#E1E4E8"> - Infrastructure definitions split by service (storage.ts, api.ts, web.ts)</span></div></div><div class="ec-line"><div class="code"><span style="--0:#AE4B07;--1:#FFAB70">-</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#005CC5;--1:#79B8FF">`sst.config.ts`</span><span style="--0:#24292E;--1:#E1E4E8"> - Main SST configuration with dynamic imports</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#005CC5;--0fw:bold;--1:#79B8FF;--1fw:bold">## Code Standards</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#AE4B07;--1:#FFAB70">-</span><span style="--0:#24292E;--1:#E1E4E8"> Use TypeScript with strict mode enabled</span></div></div><div class="ec-line"><div class="code"><span style="--0:#AE4B07;--1:#FFAB70">-</span><span style="--0:#24292E;--1:#E1E4E8"> Shared code goes in </span><span style="--0:#005CC5;--1:#79B8FF">`packages/core/`</span><span style="--0:#24292E;--1:#E1E4E8"> with proper exports configuration</span></div></div><div class="ec-line"><div class="code"><span style="--0:#AE4B07;--1:#FFAB70">-</span><span style="--0:#24292E;--1:#E1E4E8"> Functions go in </span><span style="--0:#005CC5;--1:#79B8FF">`packages/functions/`</span></div></div><div class="ec-line"><div class="code"><span style="--0:#AE4B07;--1:#FFAB70">-</span><span style="--0:#24292E;--1:#E1E4E8"> Infrastructure should be split into logical files in </span><span style="--0:#005CC5;--1:#79B8FF">`infra/`</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#005CC5;--0fw:bold;--1:#79B8FF;--1fw:bold">## Monorepo Conventions</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#AE4B07;--1:#FFAB70">-</span><span style="--0:#24292E;--1:#E1E4E8"> Import shared modules using workspace names: </span><span style="--0:#005CC5;--1:#79B8FF">`@my-app/core/example`</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="# SST v3 Monorepo ProjectThis is an SST v3 monorepo with TypeScript. The project uses bun workspaces for package management.## Project Structure- `packages/` - Contains all workspace packages (functions, core, web, etc.)- `infra/` - Infrastructure definitions split by service (storage.ts, api.ts, web.ts)- `sst.config.ts` - Main SST configuration with dynamic imports## Code Standards- Use TypeScript with strict mode enabled- Shared code goes in `packages/core/` with proper exports configuration- Functions go in `packages/functions/`- Infrastructure should be split into logical files in `infra/`## Monorepo Conventions- Import shared modules using workspace names: `@my-app/core/example`" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


我们在这里添加了项目特定的指令，这些指令会在您的团队中共享。
* * *
## 类型
opencode 还支持从多个位置读取 `AGENTS.md` 文件，不同的位置有不同的用途。
### 项目级
在项目根目录放置一个 `AGENTS.md` 文件，用于定义项目特定的规则。这些规则仅在您在该目录或其子目录中工作时生效。
### 全局级
您还可以在 `~/.config/opencode/AGENTS.md` 文件中设置全局规则。这些规则会应用于所有 opencode 会话。
由于该文件不会被提交到 Git 或与团队共享，我们建议用它来指定 LLM 应遵循的个人规则。
### Claude Code 兼容性
对于从 Claude Code 迁移过来的用户，OpenCode 支持 Claude Code 的文件约定作为回退方案：
  * **项目规则** ：项目目录中的 `CLAUDE.md`（在没有 `AGENTS.md` 的情况下使用）
  * **全局规则** ：`~/.claude/CLAUDE.md`（在没有 `~/.config/opencode/AGENTS.md` 的情况下使用）
  * **技能** ：`~/.claude/skills/` — 详情请参阅[代理技能](/docs/skills/)


要禁用 Claude Code 兼容性，请设置以下环境变量之一：


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#BF3441;--1:#F97583">export</span><span style="--0:#24292E;--1:#E1E4E8"> OPENCODE_DISABLE_CLAUDE_CODE</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#005CC5;--1:#79B8FF">1</span><span style="--0:#24292E;--1:#E1E4E8">        </span><span style="--0:#616972;--1:#99A0A6"># Disable all .claude support</span></div></div><div class="ec-line"><div class="code"><span style="--0:#BF3441;--1:#F97583">export</span><span style="--0:#24292E;--1:#E1E4E8"> OPENCODE_DISABLE_CLAUDE_CODE_PROMPT</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#005CC5;--1:#79B8FF">1</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#616972;--1:#99A0A6"># Disable only ~/.claude/CLAUDE.md</span></div></div><div class="ec-line"><div class="code"><span style="--0:#BF3441;--1:#F97583">export</span><span style="--0:#24292E;--1:#E1E4E8"> OPENCODE_DISABLE_CLAUDE_CODE_SKILLS</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#005CC5;--1:#79B8FF">1</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#616972;--1:#99A0A6"># Disable only .claude/skills</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="export OPENCODE_DISABLE_CLAUDE_CODE=1        # Disable all .claude supportexport OPENCODE_DISABLE_CLAUDE_CODE_PROMPT=1 # Disable only ~/.claude/CLAUDE.mdexport OPENCODE_DISABLE_CLAUDE_CODE_SKILLS=1 # Disable only .claude/skills" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
## 优先级
当 opencode 启动时，它会按以下顺序查找规则文件：
  1. **本地文件** ，从当前目录向上遍历（`AGENTS.md`、`CLAUDE.md`）
  2. **全局文件** ，位于 `~/.config/opencode/AGENTS.md`
  3. **Claude Code 文件** ，位于 `~/.claude/CLAUDE.md`（除非已禁用）


在每个类别中，第一个匹配的文件优先。例如，如果您同时拥有 `AGENTS.md` 和 `CLAUDE.md`，则只会使用 `AGENTS.md`。同样，`~/.config/opencode/AGENTS.md` 优先于 `~/.claude/CLAUDE.md`。
* * *
## 自定义指令
您可以在 `opencode.json` 或全局配置文件 `~/.config/opencode/opencode.json` 中指定自定义指令文件。这允许您和团队复用现有规则，而无需将它们复制到 AGENTS.md 中。
示例：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"instructions"</span><span style="--0:#24292E;--1:#E1E4E8">: [</span><span style="--0:#032F62;--1:#9ECBFF">"CONTRIBUTING.md"</span><span style="--0:#24292E;--1:#E1E4E8">, </span><span style="--0:#032F62;--1:#9ECBFF">"docs/guidelines.md"</span><span style="--0:#24292E;--1:#E1E4E8">, </span><span style="--0:#032F62;--1:#9ECBFF">".cursor/rules/*.md"</span><span style="--0:#24292E;--1:#E1E4E8">]</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "instructions": ["CONTRIBUTING.md", "docs/guidelines.md", ".cursor/rules/*.md"]}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


您还可以使用远程 URL 从网络加载指令。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"instructions"</span><span style="--0:#24292E;--1:#E1E4E8">: [</span><span style="--0:#032F62;--1:#9ECBFF">"https://raw.githubusercontent.com/my-org/shared-rules/main/style.md"</span><span style="--0:#24292E;--1:#E1E4E8">]</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "instructions": ["https://raw.githubusercontent.com/my-org/shared-rules/main/style.md"]}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


远程指令的获取超时时间为 5 秒。
所有指令文件都会与您的 `AGENTS.md` 文件合并。
* * *
## 引用外部文件
虽然 opencode 不会自动解析 `AGENTS.md` 中的文件引用，但您可以通过以下两种方式实现类似的功能：
### 使用 opencode.json
推荐的方式是使用 `opencode.json` 中的 `instructions` 字段：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"instructions"</span><span style="--0:#24292E;--1:#E1E4E8">: [</span><span style="--0:#032F62;--1:#9ECBFF">"docs/development-standards.md"</span><span style="--0:#24292E;--1:#E1E4E8">, </span><span style="--0:#032F62;--1:#9ECBFF">"test/testing-guidelines.md"</span><span style="--0:#24292E;--1:#E1E4E8">, </span><span style="--0:#032F62;--1:#9ECBFF">"packages/*/AGENTS.md"</span><span style="--0:#24292E;--1:#E1E4E8">]</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "instructions": ["docs/development-standards.md", "test/testing-guidelines.md", "packages/*/AGENTS.md"]}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


### 在 AGENTS.md 中手动指定
您可以在 `AGENTS.md` 中提供明确的指令，教 opencode 读取外部文件。以下是一个实际示例：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">AGENTS.md</span></figcaption><pre data-language="markdown"><code><div class="ec-line"><div class="code"><span style="--0:#005CC5;--0fw:bold;--1:#79B8FF;--1fw:bold"># TypeScript Project Rules</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#005CC5;--0fw:bold;--1:#79B8FF;--1fw:bold">## External File Loading</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">CRITICAL: When you encounter a file reference (e.g., @rules/general.md), use your Read tool to load it on a need-to-know basis. They're relevant to the SPECIFIC task at hand.</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">Instructions:</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#AE4B07;--1:#FFAB70">-</span><span style="--0:#24292E;--1:#E1E4E8"> Do NOT preemptively load all references - use lazy loading based on actual need</span></div></div><div class="ec-line"><div class="code"><span style="--0:#AE4B07;--1:#FFAB70">-</span><span style="--0:#24292E;--1:#E1E4E8"> When loaded, treat content as mandatory instructions that override defaults</span></div></div><div class="ec-line"><div class="code"><span style="--0:#AE4B07;--1:#FFAB70">-</span><span style="--0:#24292E;--1:#E1E4E8"> Follow references recursively when needed</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#005CC5;--0fw:bold;--1:#79B8FF;--1fw:bold">## Development Guidelines</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">For TypeScript code style and best practices: @docs/typescript-guidelines.md</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">For React component architecture and hooks patterns: @docs/react-patterns.md</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">For REST API design and error handling: @docs/api-standards.md</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">For testing strategies and coverage requirements: @test/testing-guidelines.md</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#005CC5;--0fw:bold;--1:#79B8FF;--1fw:bold">## General Guidelines</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">Read the following file immediately as it's relevant to all workflows: @rules/general-guidelines.md.</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="# TypeScript Project Rules## External File LoadingCRITICAL: When you encounter a file reference (e.g., @rules/general.md), use your Read tool to load it on a need-to-know basis. They're relevant to the SPECIFIC task at hand.Instructions:- Do NOT preemptively load all references - use lazy loading based on actual need- When loaded, treat content as mandatory instructions that override defaults- Follow references recursively when needed## Development GuidelinesFor TypeScript code style and best practices: @docs/typescript-guidelines.mdFor React component architecture and hooks patterns: @docs/react-patterns.mdFor REST API design and error handling: @docs/api-standards.mdFor testing strategies and coverage requirements: @test/testing-guidelines.md## General GuidelinesRead the following file immediately as it's relevant to all workflows: @rules/general-guidelines.md." data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


这种方式允许您：
  * 创建模块化、可复用的规则文件
  * 通过符号链接或 Git 子模块在项目之间共享规则
  * 保持 AGENTS.md 简洁，同时引用详细的指南
  * 确保 opencode 仅在特定任务需要时才加载文件


<aside aria-label="提示" class="starlight-aside starlight-aside--tip"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path clip-rule="evenodd" d="M1.43909 8.85483L1.44039 8.85354L4.96668 5.33815C5.30653 4.99386 5.7685 4.79662 6.2524 4.78972L6.26553 4.78963L12.9014 4.78962L13.8479 3.84308C16.9187 0.772319 20.0546 0.770617 21.4678 0.975145C21.8617 1.02914 22.2271 1.21053 22.5083 1.4917C22.7894 1.77284 22.9708 2.13821 23.0248 2.53199C23.2294 3.94517 23.2278 7.08119 20.1569 10.1521L19.2107 11.0983V17.7338L19.2106 17.7469C19.2037 18.2308 19.0067 18.6933 18.6624 19.0331L15.1456 22.5608C14.9095 22.7966 14.6137 22.964 14.29 23.0449C13.9663 23.1259 13.6267 23.1174 13.3074 23.0204C12.9881 22.9235 12.7011 22.7417 12.4771 22.4944C12.2533 22.2473 12.1006 21.9441 12.0355 21.6171L11.1783 17.3417L6.65869 12.822L4.34847 12.3589L2.38351 11.965C2.05664 11.8998 1.75272 11.747 1.50564 11.5232C1.25835 11.2992 1.07653 11.0122 0.979561 10.6929C0.882595 10.3736 0.874125 10.034 0.955057 9.7103C1.03599 9.38659 1.20328 9.09092 1.43909 8.85483ZM6.8186 10.8724L2.94619 10.096L6.32006 6.73268H10.9583L6.8186 10.8724ZM15.2219 5.21703C17.681 2.75787 20.0783 2.75376 21.1124 2.8876C21.2462 3.92172 21.2421 6.31895 18.783 8.77812L12.0728 15.4883L8.51172 11.9272L15.2219 5.21703ZM13.9042 21.0538L13.1279 17.1811L17.2676 13.0414V17.68L13.9042 21.0538Z" fill-rule="evenodd"></path><path d="M9.31827 18.3446C9.45046 17.8529 9.17864 17.3369 8.68945 17.1724C8.56178 17.1294 8.43145 17.1145 8.30512 17.1243C8.10513 17.1398 7.91519 17.2172 7.76181 17.3434C7.62613 17.455 7.51905 17.6048 7.45893 17.7835C6.97634 19.2186 5.77062 19.9878 4.52406 20.4029C4.08525 20.549 3.6605 20.644 3.29471 20.7053C3.35607 20.3395 3.45098 19.9148 3.59711 19.476C4.01221 18.2294 4.78141 17.0237 6.21648 16.5411C6.39528 16.481 6.54504 16.3739 6.65665 16.2382C6.85126 16.0016 6.92988 15.678 6.84417 15.3647C6.83922 15.3466 6.83373 15.3286 6.82767 15.3106C6.74106 15.053 6.55701 14.8557 6.33037 14.7459C6.10949 14.6389 5.84816 14.615 5.59715 14.6994C5.47743 14.7397 5.36103 14.7831 5.24786 14.8294C3.22626 15.6569 2.2347 17.4173 1.75357 18.8621C1.49662 19.6337 1.36993 20.3554 1.30679 20.8818C1.27505 21.1464 1.25893 21.3654 1.25072 21.5213C1.24662 21.5993 1.24448 21.6618 1.24337 21.7066L1.243 21.7226L1.24235 21.7605L1.2422 21.7771L1.24217 21.7827L1.24217 21.7856C1.24217 22.3221 1.67703 22.7579 2.2137 22.7579L2.2155 22.7579L2.22337 22.7578L2.23956 22.7577C2.25293 22.7575 2.27096 22.7572 2.29338 22.7567C2.33821 22.7555 2.40073 22.7534 2.47876 22.7493C2.63466 22.7411 2.85361 22.725 3.11822 22.6932C3.64462 22.6301 4.36636 22.5034 5.13797 22.2464C6.58274 21.7653 8.3431 20.7738 9.17063 18.7522C9.21696 18.639 9.26037 18.5226 9.30064 18.4029C9.30716 18.3835 9.31304 18.364 9.31827 18.3446Z"></path></svg>提示</p><div class="starlight-aside__content"><p>对于 monorepo 或具有共享标准的项目，使用 <code dir="auto">opencode.json</code> 配合 glob 模式（如 <code dir="auto">packages/*/AGENTS.md</code>）比手动指定指令更易于维护。</p></div></aside>