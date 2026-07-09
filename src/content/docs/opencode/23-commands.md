---
title: 命令'
description: '为重复任务创建自定义命令。'
category: 'OpenCode 开发手册'
order: 23
slug: 'opencode/commands'
---

自定义命令允许你指定一个提示词，当在 TUI 中执行该命令时会运行这个提示词。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/my-command</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/my-command" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


自定义命令是 `/init`、`/undo`、`/redo`、`/share`、`/help` 等内置命令之外的补充。[了解更多](/docs/tui#commands)。
* * *
## 创建命令文件
在 `commands/` 目录中创建 markdown 文件来定义自定义命令。
创建 `.opencode/commands/test.md`：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">.opencode/commands/test.md</span></figcaption><pre data-language="md"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">---</span></div></div><div class="ec-line"><div class="code"><span style="--0:#1E7734;--1:#85E89D">description</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">Run tests with coverage</span></div></div><div class="ec-line"><div class="code"><span style="--0:#1E7734;--1:#85E89D">agent</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">build</span></div></div><div class="ec-line"><div class="code"><span style="--0:#1E7734;--1:#85E89D">model</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">anthropic/claude-3-5-sonnet-20241022</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">---</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">Run the full test suite with coverage report and show any failures.</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">Focus on the failing tests and suggest fixes.</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="---description: Run tests with coverageagent: buildmodel: anthropic/claude-3-5-sonnet-20241022---Run the full test suite with coverage report and show any failures.Focus on the failing tests and suggest fixes." data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


frontmatter 定义命令属性，内容则成为模板。
通过输入 `/` 后跟命令名称来使用该命令。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">"/test"</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='"/test"' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
## 配置
你可以通过 OpenCode 配置或在 `commands/` 目录中创建 markdown 文件来添加自定义命令。
* * *
### JSON
在 OpenCode [配置](/docs/config)中使用 `command` 选项：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.jsonc</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"command"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">    </span><span style="--0:#494f56;--1:#b4b9be">// This becomes the name of the command</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">    </span><span style="--0:#004ba0;--1:#81bcff">"test"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#494f56;--1:#b4b9be">// This is the prompt that will be sent to the LLM</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"template"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"Run the full test suite with coverage report and show any failures.</span><span style="--0:#004ba0;--1:#81bcff">\n</span><span style="--0:#032F62;--1:#9ECBFF">Focus on the failing tests and suggest fixes."</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#494f56;--1:#b4b9be">// This is shown as the description in the TUI</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"description"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"Run tests with coverage"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"agent"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"build"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"model"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"anthropic/claude-3-5-sonnet-20241022"</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "command": {    // This becomes the name of the command    "test": {      // This is the prompt that will be sent to the LLM      "template": "Run the full test suite with coverage report and show any failures.\nFocus on the failing tests and suggest fixes.",      // This is shown as the description in the TUI      "description": "Run tests with coverage",      "agent": "build",      "model": "anthropic/claude-3-5-sonnet-20241022"    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


现在你可以在 TUI 中运行这个命令：


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/test</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/test" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### Markdown
你还可以使用 markdown 文件定义命令。将它们放在：
  * 全局：`~/.config/opencode/commands/`
  * 项目级：`.opencode/commands/`


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">~/.config/opencode/commands/test.md</span></figcaption><pre data-language="markdown"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">---</span></div></div><div class="ec-line"><div class="code"><span style="--0:#1E7734;--1:#85E89D">description</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">Run tests with coverage</span></div></div><div class="ec-line"><div class="code"><span style="--0:#1E7734;--1:#85E89D">agent</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">build</span></div></div><div class="ec-line"><div class="code"><span style="--0:#1E7734;--1:#85E89D">model</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">anthropic/claude-3-5-sonnet-20241022</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">---</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">Run the full test suite with coverage report and show any failures.</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">Focus on the failing tests and suggest fixes.</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="---description: Run tests with coverageagent: buildmodel: anthropic/claude-3-5-sonnet-20241022---Run the full test suite with coverage report and show any failures.Focus on the failing tests and suggest fixes." data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


markdown 文件名即为命令名。例如，`test.md` 允许你运行：


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/test</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/test" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
## 提示词配置
自定义命令的提示词支持多种特殊占位符和语法。
* * *
### 参数
使用 `$ARGUMENTS` 占位符向命令传递参数。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">.opencode/commands/component.md</span></figcaption><pre data-language="md"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">---</span></div></div><div class="ec-line"><div class="code"><span style="--0:#1E7734;--1:#85E89D">description</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">Create a new component</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">---</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">Create a new React component named $ARGUMENTS with TypeScript support.</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">Include proper typing and basic structure.</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="---description: Create a new component---Create a new React component named $ARGUMENTS with TypeScript support.Include proper typing and basic structure." data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


带参数运行命令：


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/component</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">Button</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/component Button" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


`$ARGUMENTS` 将被替换为 `Button`。
你还可以使用位置参数访问各个参数：
  * `$1` \- 第一个参数
  * `$2` \- 第二个参数
  * `$3` \- 第三个参数
  * 以此类推…


例如：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">.opencode/commands/create-file.md</span></figcaption><pre data-language="md"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">---</span></div></div><div class="ec-line"><div class="code"><span style="--0:#1E7734;--1:#85E89D">description</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">Create a new file with content</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">---</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">Create a file named $1 in the directory $2</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">with the following content: $3</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="---description: Create a new file with content---Create a file named $1 in the directory $2with the following content: $3" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


运行命令：


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/create-file</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">config.json</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">src</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">"{ </span><span style="--0:#005CC5;--1:#79B8FF">\"</span><span style="--0:#032F62;--1:#9ECBFF">key</span><span style="--0:#005CC5;--1:#79B8FF">\"</span><span style="--0:#032F62;--1:#9ECBFF">: </span><span style="--0:#005CC5;--1:#79B8FF">\"</span><span style="--0:#032F62;--1:#9ECBFF">value</span><span style="--0:#005CC5;--1:#79B8FF">\"</span><span style="--0:#032F62;--1:#9ECBFF"> }"</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='/create-file config.json src "{ \"key\": \"value\" }"' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


替换结果为：
  * `$1` 替换为 `config.json`
  * `$2` 替换为 `src`
  * `$3` 替换为 `{ "key": "value" }`


* * *
### Shell 输出
使用 _!`command`_ 将 [bash 命令](/docs/tui#bash-commands)输出注入到提示词中。
例如，创建一个分析测试覆盖率的自定义命令：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">.opencode/commands/analyze-coverage.md</span></figcaption><pre data-language="md"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">---</span></div></div><div class="ec-line"><div class="code"><span style="--0:#1E7734;--1:#85E89D">description</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">Analyze test coverage</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">---</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">Here are the current test results:</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">!</span><span style="--0:#005CC5;--1:#79B8FF">`npm test`</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">Based on these results, suggest improvements to increase coverage.</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="---description: Analyze test coverage---Here are the current test results:!`npm test`Based on these results, suggest improvements to increase coverage." data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


或者查看最近的更改：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">.opencode/commands/review-changes.md</span></figcaption><pre data-language="md"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">---</span></div></div><div class="ec-line"><div class="code"><span style="--0:#1E7734;--1:#85E89D">description</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">Review recent changes</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">---</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">Recent git commits:</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">!</span><span style="--0:#005CC5;--1:#79B8FF">`git log --oneline -10`</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">Review these changes and suggest any improvements.</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="---description: Review recent changes---Recent git commits:!`git log --oneline -10`Review these changes and suggest any improvements." data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


命令在项目的根目录中运行，其输出会成为提示词的一部分。
* * *
### 文件引用
使用 `@` 后跟文件名在命令中引用文件。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">.opencode/commands/review-component.md</span></figcaption><pre data-language="md"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">---</span></div></div><div class="ec-line"><div class="code"><span style="--0:#1E7734;--1:#85E89D">description</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">Review component</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">---</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">Review the component in @src/components/Button.tsx.</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">Check for performance issues and suggest improvements.</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="---description: Review component---Review the component in @src/components/Button.tsx.Check for performance issues and suggest improvements." data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


文件内容会自动包含在提示词中。
* * *
## 选项
让我们详细了解各配置选项。
* * *
### Template
`template` 选项定义执行命令时发送给 LLM 的提示词。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"command"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"test"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"template"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"Run the full test suite with coverage report and show any failures.</span><span style="--0:#005CC5;--1:#79B8FF">\n</span><span style="--0:#032F62;--1:#9ECBFF">Focus on the failing tests and suggest fixes."</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "command": {    "test": {      "template": "Run the full test suite with coverage report and show any failures.\nFocus on the failing tests and suggest fixes."    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


这是一个**必需的** 配置选项。
* * *
### Description
使用 `description` 选项提供命令功能的简要描述。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"command"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"test"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"description"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"Run tests with coverage"</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "command": {    "test": {      "description": "Run tests with coverage"    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


当你输入命令时，这将在 TUI 中显示为描述。
* * *
### Agent
使用 `agent` 配置可选地指定由哪个[代理](/docs/agents)执行此命令。 如果这是一个[子代理](/docs/agents/#subagents)，该命令默认会触发子代理调用。 要禁用此行为，请将 `subtask` 设置为 `false`。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"command"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"review"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"agent"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"plan"</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "command": {    "review": {      "agent": "plan"    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


这是一个**可选的** 配置选项。如果未指定，默认使用你当前的代理。
* * *
### Subtask
使用 `subtask` 布尔值强制命令触发[子代理](/docs/agents/#subagents)调用。 如果你希望命令不污染主要上下文，这会很有用，它会**强制** 代理作为子代理运行， 即使[代理](/docs/agents)配置中的 `mode` 设置为 `primary`。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"command"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"analyze"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"subtask"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#005CC5;--1:#79B8FF">true</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "command": {    "analyze": {      "subtask": true    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


这是一个**可选的** 配置选项。
* * *
### Model
使用 `model` 配置覆盖此命令的默认模型。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"command"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"analyze"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"model"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"anthropic/claude-3-5-sonnet-20241022"</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "command": {    "analyze": {      "model": "anthropic/claude-3-5-sonnet-20241022"    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


这是一个**可选的** 配置选项。
* * *
## 内置命令
opencode 包含多个内置命令，如 `/init`、`/undo`、`/redo`、`/share`、`/help`；[了解更多](/docs/tui#commands)。


<aside aria-label="注意" class="starlight-aside starlight-aside--note"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M12 11C11.7348 11 11.4804 11.1054 11.2929 11.2929C11.1054 11.4804 11 11.7348 11 12V16C11 16.2652 11.1054 16.5196 11.2929 16.7071C11.4804 16.8946 11.7348 17 12 17C12.2652 17 12.5196 16.8946 12.7071 16.7071C12.8946 16.5196 13 16.2652 13 16V12C13 11.7348 12.8946 11.4804 12.7071 11.2929C12.5196 11.1054 12.2652 11 12 11ZM12.38 7.08C12.1365 6.97998 11.8635 6.97998 11.62 7.08C11.4973 7.12759 11.3851 7.19896 11.29 7.29C11.2017 7.3872 11.1306 7.49882 11.08 7.62C11.024 7.73868 10.9966 7.86882 11 8C10.9992 8.13161 11.0245 8.26207 11.0742 8.38391C11.124 8.50574 11.1973 8.61656 11.29 8.71C11.3872 8.79833 11.4988 8.86936 11.62 8.92C11.7715 8.98224 11.936 9.00632 12.099 8.99011C12.2619 8.97391 12.4184 8.91792 12.5547 8.82707C12.691 8.73622 12.8029 8.61328 12.8805 8.46907C12.9582 8.32486 12.9992 8.16378 13 8C12.9963 7.73523 12.8927 7.48163 12.71 7.29C12.6149 7.19896 12.5028 7.12759 12.38 7.08ZM12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM12 20C10.4178 20 8.87104 19.5308 7.55544 18.6518C6.23985 17.7727 5.21447 16.5233 4.60897 15.0615C4.00347 13.5997 3.84504 11.9911 4.15372 10.4393C4.4624 8.88743 5.22433 7.46197 6.34315 6.34315C7.46197 5.22433 8.88743 4.4624 10.4393 4.15372C11.9911 3.84504 13.5997 4.00346 15.0615 4.60896C16.5233 5.21447 17.7727 6.23984 18.6518 7.55544C19.5308 8.87103 20 10.4177 20 12C20 14.1217 19.1572 16.1566 17.6569 17.6569C16.1566 19.1571 14.1217 20 12 20Z"></path></svg>注意</p><div class="starlight-aside__content"><p>自定义命令可以覆盖内置命令。</p></div></aside>


如果你定义了同名的自定义命令，它将覆盖内置命令。