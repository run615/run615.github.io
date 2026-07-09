---
title: 'TUI'
description: '使用 OpenCode 终端用户界面。'
category: 'OpenCode 开发手册'
order: 9
slug: 'opencode/tui'
---

OpenCode 提供了一个交互式终端界面（TUI），用于配合 LLM 处理您的项目。
运行 OpenCode 即可启动当前目录的 TUI。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


或者您可以为指定的工作目录启动它。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">/path/to/project</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode /path/to/project" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


进入 TUI 后，您可以输入消息进行提示。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="text"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">Give me a quick summary of the codebase.</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="Give me a quick summary of the codebase." data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
## 文件引用
您可以使用 `@` 在消息中引用文件。这会在当前工作目录中进行模糊文件搜索。


<aside aria-label="提示" class="starlight-aside starlight-aside--tip"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path clip-rule="evenodd" d="M1.43909 8.85483L1.44039 8.85354L4.96668 5.33815C5.30653 4.99386 5.7685 4.79662 6.2524 4.78972L6.26553 4.78963L12.9014 4.78962L13.8479 3.84308C16.9187 0.772319 20.0546 0.770617 21.4678 0.975145C21.8617 1.02914 22.2271 1.21053 22.5083 1.4917C22.7894 1.77284 22.9708 2.13821 23.0248 2.53199C23.2294 3.94517 23.2278 7.08119 20.1569 10.1521L19.2107 11.0983V17.7338L19.2106 17.7469C19.2037 18.2308 19.0067 18.6933 18.6624 19.0331L15.1456 22.5608C14.9095 22.7966 14.6137 22.964 14.29 23.0449C13.9663 23.1259 13.6267 23.1174 13.3074 23.0204C12.9881 22.9235 12.7011 22.7417 12.4771 22.4944C12.2533 22.2473 12.1006 21.9441 12.0355 21.6171L11.1783 17.3417L6.65869 12.822L4.34847 12.3589L2.38351 11.965C2.05664 11.8998 1.75272 11.747 1.50564 11.5232C1.25835 11.2992 1.07653 11.0122 0.979561 10.6929C0.882595 10.3736 0.874125 10.034 0.955057 9.7103C1.03599 9.38659 1.20328 9.09092 1.43909 8.85483ZM6.8186 10.8724L2.94619 10.096L6.32006 6.73268H10.9583L6.8186 10.8724ZM15.2219 5.21703C17.681 2.75787 20.0783 2.75376 21.1124 2.8876C21.2462 3.92172 21.2421 6.31895 18.783 8.77812L12.0728 15.4883L8.51172 11.9272L15.2219 5.21703ZM13.9042 21.0538L13.1279 17.1811L17.2676 13.0414V17.68L13.9042 21.0538Z" fill-rule="evenodd"></path><path d="M9.31827 18.3446C9.45046 17.8529 9.17864 17.3369 8.68945 17.1724C8.56178 17.1294 8.43145 17.1145 8.30512 17.1243C8.10513 17.1398 7.91519 17.2172 7.76181 17.3434C7.62613 17.455 7.51905 17.6048 7.45893 17.7835C6.97634 19.2186 5.77062 19.9878 4.52406 20.4029C4.08525 20.549 3.6605 20.644 3.29471 20.7053C3.35607 20.3395 3.45098 19.9148 3.59711 19.476C4.01221 18.2294 4.78141 17.0237 6.21648 16.5411C6.39528 16.481 6.54504 16.3739 6.65665 16.2382C6.85126 16.0016 6.92988 15.678 6.84417 15.3647C6.83922 15.3466 6.83373 15.3286 6.82767 15.3106C6.74106 15.053 6.55701 14.8557 6.33037 14.7459C6.10949 14.6389 5.84816 14.615 5.59715 14.6994C5.47743 14.7397 5.36103 14.7831 5.24786 14.8294C3.22626 15.6569 2.2347 17.4173 1.75357 18.8621C1.49662 19.6337 1.36993 20.3554 1.30679 20.8818C1.27505 21.1464 1.25893 21.3654 1.25072 21.5213C1.24662 21.5993 1.24448 21.6618 1.24337 21.7066L1.243 21.7226L1.24235 21.7605L1.2422 21.7771L1.24217 21.7827L1.24217 21.7856C1.24217 22.3221 1.67703 22.7579 2.2137 22.7579L2.2155 22.7579L2.22337 22.7578L2.23956 22.7577C2.25293 22.7575 2.27096 22.7572 2.29338 22.7567C2.33821 22.7555 2.40073 22.7534 2.47876 22.7493C2.63466 22.7411 2.85361 22.725 3.11822 22.6932C3.64462 22.6301 4.36636 22.5034 5.13797 22.2464C6.58274 21.7653 8.3431 20.7738 9.17063 18.7522C9.21696 18.639 9.26037 18.5226 9.30064 18.4029C9.30716 18.3835 9.31304 18.364 9.31827 18.3446Z"></path></svg>提示</p><div class="starlight-aside__content"><p>您还可以使用 <code dir="auto">@</code> 来引用消息中的文件。</p></div></aside>

 

<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="text"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">How is auth handled in </span><mark><span style="--0:#24292e;--1:#e1e4e8">@packages/functions/src/api/index.ts</span></mark><span style="--0:#24292e;--1:#e1e4e8">?</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="How is auth handled in @packages/functions/src/api/index.ts?" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


文件的内容会自动添加到对话中。
* * *
## Bash 命令
以 `!` 开头的消息会作为 shell 命令执行。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#BF3441;--1:#F97583">!</span><span style="--0:#6F42C1;--1:#B392F0">ls</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#005CC5;--1:#79B8FF">-la</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="!ls -la" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


命令的输出会作为工具结果添加到对话中。
* * *
## 命令
使用 OpenCode TUI 时，您可以输入 `/` 后跟命令名称来快速执行操作。例如：


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/help</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/help" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


大多数命令还支持以 `ctrl+x` 作为前导键的快捷键，其中 `ctrl+x` 是默认前导键。[了解更多](/docs/keybinds)。
以下是所有可用的斜杠命令：
* * *
### connect
将提供商添加到 OpenCode。允许您从可用的提供商中选择并添加其 API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### compact
压缩当前会话。 _别名_ ：`/summarize`


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/compact</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/compact" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


**快捷键：** `ctrl+x c`
* * *
### details
切换工具执行详情的显示。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/details</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/details" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


**快捷键：** `ctrl+x d`
* * *
### editor
打开外部编辑器来编写消息。使用 `EDITOR` 环境变量中设置的编辑器。[了解更多](#editor-setup)。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/editor</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/editor" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


**快捷键：** `ctrl+x e`
* * *
### exit
退出 OpenCode。 _别名_ ：`/quit`、`/q`


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/exit</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/exit" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


**快捷键：** `ctrl+x q`
* * *
### export
将当前对话导出为 Markdown 并在默认编辑器中打开。使用 `EDITOR` 环境变量中设置的编辑器。[了解更多](#editor-setup)。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/export</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/export" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


**快捷键：** `ctrl+x x`
* * *
### help
显示帮助对话框。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/help</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/help" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


**快捷键：** `ctrl+x h`
* * *
### init
创建或更新 `AGENTS.md` 文件。[了解更多](/docs/rules)。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/init</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/init" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


**快捷键：** `ctrl+x i`
* * *
### models
列出可用模型。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


**快捷键：** `ctrl+x m`
* * *
### new
开始新的会话。 _别名_ ：`/clear`


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/new</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/new" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


**快捷键：** `ctrl+x n`
* * *
### redo
重做之前撤销的消息。仅在使用 `/undo` 后可用。


<aside aria-label="提示" class="starlight-aside starlight-aside--tip"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path clip-rule="evenodd" d="M1.43909 8.85483L1.44039 8.85354L4.96668 5.33815C5.30653 4.99386 5.7685 4.79662 6.2524 4.78972L6.26553 4.78963L12.9014 4.78962L13.8479 3.84308C16.9187 0.772319 20.0546 0.770617 21.4678 0.975145C21.8617 1.02914 22.2271 1.21053 22.5083 1.4917C22.7894 1.77284 22.9708 2.13821 23.0248 2.53199C23.2294 3.94517 23.2278 7.08119 20.1569 10.1521L19.2107 11.0983V17.7338L19.2106 17.7469C19.2037 18.2308 19.0067 18.6933 18.6624 19.0331L15.1456 22.5608C14.9095 22.7966 14.6137 22.964 14.29 23.0449C13.9663 23.1259 13.6267 23.1174 13.3074 23.0204C12.9881 22.9235 12.7011 22.7417 12.4771 22.4944C12.2533 22.2473 12.1006 21.9441 12.0355 21.6171L11.1783 17.3417L6.65869 12.822L4.34847 12.3589L2.38351 11.965C2.05664 11.8998 1.75272 11.747 1.50564 11.5232C1.25835 11.2992 1.07653 11.0122 0.979561 10.6929C0.882595 10.3736 0.874125 10.034 0.955057 9.7103C1.03599 9.38659 1.20328 9.09092 1.43909 8.85483ZM6.8186 10.8724L2.94619 10.096L6.32006 6.73268H10.9583L6.8186 10.8724ZM15.2219 5.21703C17.681 2.75787 20.0783 2.75376 21.1124 2.8876C21.2462 3.92172 21.2421 6.31895 18.783 8.77812L12.0728 15.4883L8.51172 11.9272L15.2219 5.21703ZM13.9042 21.0538L13.1279 17.1811L17.2676 13.0414V17.68L13.9042 21.0538Z" fill-rule="evenodd"></path><path d="M9.31827 18.3446C9.45046 17.8529 9.17864 17.3369 8.68945 17.1724C8.56178 17.1294 8.43145 17.1145 8.30512 17.1243C8.10513 17.1398 7.91519 17.2172 7.76181 17.3434C7.62613 17.455 7.51905 17.6048 7.45893 17.7835C6.97634 19.2186 5.77062 19.9878 4.52406 20.4029C4.08525 20.549 3.6605 20.644 3.29471 20.7053C3.35607 20.3395 3.45098 19.9148 3.59711 19.476C4.01221 18.2294 4.78141 17.0237 6.21648 16.5411C6.39528 16.481 6.54504 16.3739 6.65665 16.2382C6.85126 16.0016 6.92988 15.678 6.84417 15.3647C6.83922 15.3466 6.83373 15.3286 6.82767 15.3106C6.74106 15.053 6.55701 14.8557 6.33037 14.7459C6.10949 14.6389 5.84816 14.615 5.59715 14.6994C5.47743 14.7397 5.36103 14.7831 5.24786 14.8294C3.22626 15.6569 2.2347 17.4173 1.75357 18.8621C1.49662 19.6337 1.36993 20.3554 1.30679 20.8818C1.27505 21.1464 1.25893 21.3654 1.25072 21.5213C1.24662 21.5993 1.24448 21.6618 1.24337 21.7066L1.243 21.7226L1.24235 21.7605L1.2422 21.7771L1.24217 21.7827L1.24217 21.7856C1.24217 22.3221 1.67703 22.7579 2.2137 22.7579L2.2155 22.7579L2.22337 22.7578L2.23956 22.7577C2.25293 22.7575 2.27096 22.7572 2.29338 22.7567C2.33821 22.7555 2.40073 22.7534 2.47876 22.7493C2.63466 22.7411 2.85361 22.725 3.11822 22.6932C3.64462 22.6301 4.36636 22.5034 5.13797 22.2464C6.58274 21.7653 8.3431 20.7738 9.17063 18.7522C9.21696 18.639 9.26037 18.5226 9.30064 18.4029C9.30716 18.3835 9.31304 18.364 9.31827 18.3446Z"></path></svg>提示</p><div class="starlight-aside__content"><p>所有文件更改也会被恢复。</p></div></aside>


在内部，这使用 Git 来管理文件更改。因此您的项目**需要是一个 Git 仓库** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/redo</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/redo" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


**快捷键：** `ctrl+x r`
* * *
### sessions
列出会话并在会话之间切换。 _别名_ ：`/resume`、`/continue`


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/sessions</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/sessions" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


**快捷键：** `ctrl+x l`
* * *
### share
分享当前会话。[了解更多](/docs/share)。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/share</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/share" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


**快捷键：** `ctrl+x s`
* * *
### themes
列出可用主题。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/themes</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/themes" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


**快捷键：** `ctrl+x t`
* * *
### thinking
切换对话中思考/推理块的可见性。启用后，您可以看到支持扩展思考的模型的推理过程。


<aside aria-label="注意" class="starlight-aside starlight-aside--note"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M12 11C11.7348 11 11.4804 11.1054 11.2929 11.2929C11.1054 11.4804 11 11.7348 11 12V16C11 16.2652 11.1054 16.5196 11.2929 16.7071C11.4804 16.8946 11.7348 17 12 17C12.2652 17 12.5196 16.8946 12.7071 16.7071C12.8946 16.5196 13 16.2652 13 16V12C13 11.7348 12.8946 11.4804 12.7071 11.2929C12.5196 11.1054 12.2652 11 12 11ZM12.38 7.08C12.1365 6.97998 11.8635 6.97998 11.62 7.08C11.4973 7.12759 11.3851 7.19896 11.29 7.29C11.2017 7.3872 11.1306 7.49882 11.08 7.62C11.024 7.73868 10.9966 7.86882 11 8C10.9992 8.13161 11.0245 8.26207 11.0742 8.38391C11.124 8.50574 11.1973 8.61656 11.29 8.71C11.3872 8.79833 11.4988 8.86936 11.62 8.92C11.7715 8.98224 11.936 9.00632 12.099 8.99011C12.2619 8.97391 12.4184 8.91792 12.5547 8.82707C12.691 8.73622 12.8029 8.61328 12.8805 8.46907C12.9582 8.32486 12.9992 8.16378 13 8C12.9963 7.73523 12.8927 7.48163 12.71 7.29C12.6149 7.19896 12.5028 7.12759 12.38 7.08ZM12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM12 20C10.4178 20 8.87104 19.5308 7.55544 18.6518C6.23985 17.7727 5.21447 16.5233 4.60897 15.0615C4.00347 13.5997 3.84504 11.9911 4.15372 10.4393C4.4624 8.88743 5.22433 7.46197 6.34315 6.34315C7.46197 5.22433 8.88743 4.4624 10.4393 4.15372C11.9911 3.84504 13.5997 4.00346 15.0615 4.60896C16.5233 5.21447 17.7727 6.23984 18.6518 7.55544C19.5308 8.87103 20 10.4177 20 12C20 14.1217 19.1572 16.1566 17.6569 17.6569C16.1566 19.1571 14.1217 20 12 20Z"></path></svg>注意</p><div class="starlight-aside__content"><p>此命令仅控制思考块是否<strong>显示</strong> — 它不会启用或禁用模型的推理能力。要切换实际的推理能力，请使用 <code dir="auto">ctrl+t</code> 循环切换模型变体。</p></div></aside>

 

<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/thinking</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/thinking" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### undo
撤销对话中的最后一条消息。移除最近的用户消息、所有后续响应以及所有文件更改。


<aside aria-label="提示" class="starlight-aside starlight-aside--tip"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path clip-rule="evenodd" d="M1.43909 8.85483L1.44039 8.85354L4.96668 5.33815C5.30653 4.99386 5.7685 4.79662 6.2524 4.78972L6.26553 4.78963L12.9014 4.78962L13.8479 3.84308C16.9187 0.772319 20.0546 0.770617 21.4678 0.975145C21.8617 1.02914 22.2271 1.21053 22.5083 1.4917C22.7894 1.77284 22.9708 2.13821 23.0248 2.53199C23.2294 3.94517 23.2278 7.08119 20.1569 10.1521L19.2107 11.0983V17.7338L19.2106 17.7469C19.2037 18.2308 19.0067 18.6933 18.6624 19.0331L15.1456 22.5608C14.9095 22.7966 14.6137 22.964 14.29 23.0449C13.9663 23.1259 13.6267 23.1174 13.3074 23.0204C12.9881 22.9235 12.7011 22.7417 12.4771 22.4944C12.2533 22.2473 12.1006 21.9441 12.0355 21.6171L11.1783 17.3417L6.65869 12.822L4.34847 12.3589L2.38351 11.965C2.05664 11.8998 1.75272 11.747 1.50564 11.5232C1.25835 11.2992 1.07653 11.0122 0.979561 10.6929C0.882595 10.3736 0.874125 10.034 0.955057 9.7103C1.03599 9.38659 1.20328 9.09092 1.43909 8.85483ZM6.8186 10.8724L2.94619 10.096L6.32006 6.73268H10.9583L6.8186 10.8724ZM15.2219 5.21703C17.681 2.75787 20.0783 2.75376 21.1124 2.8876C21.2462 3.92172 21.2421 6.31895 18.783 8.77812L12.0728 15.4883L8.51172 11.9272L15.2219 5.21703ZM13.9042 21.0538L13.1279 17.1811L17.2676 13.0414V17.68L13.9042 21.0538Z" fill-rule="evenodd"></path><path d="M9.31827 18.3446C9.45046 17.8529 9.17864 17.3369 8.68945 17.1724C8.56178 17.1294 8.43145 17.1145 8.30512 17.1243C8.10513 17.1398 7.91519 17.2172 7.76181 17.3434C7.62613 17.455 7.51905 17.6048 7.45893 17.7835C6.97634 19.2186 5.77062 19.9878 4.52406 20.4029C4.08525 20.549 3.6605 20.644 3.29471 20.7053C3.35607 20.3395 3.45098 19.9148 3.59711 19.476C4.01221 18.2294 4.78141 17.0237 6.21648 16.5411C6.39528 16.481 6.54504 16.3739 6.65665 16.2382C6.85126 16.0016 6.92988 15.678 6.84417 15.3647C6.83922 15.3466 6.83373 15.3286 6.82767 15.3106C6.74106 15.053 6.55701 14.8557 6.33037 14.7459C6.10949 14.6389 5.84816 14.615 5.59715 14.6994C5.47743 14.7397 5.36103 14.7831 5.24786 14.8294C3.22626 15.6569 2.2347 17.4173 1.75357 18.8621C1.49662 19.6337 1.36993 20.3554 1.30679 20.8818C1.27505 21.1464 1.25893 21.3654 1.25072 21.5213C1.24662 21.5993 1.24448 21.6618 1.24337 21.7066L1.243 21.7226L1.24235 21.7605L1.2422 21.7771L1.24217 21.7827L1.24217 21.7856C1.24217 22.3221 1.67703 22.7579 2.2137 22.7579L2.2155 22.7579L2.22337 22.7578L2.23956 22.7577C2.25293 22.7575 2.27096 22.7572 2.29338 22.7567C2.33821 22.7555 2.40073 22.7534 2.47876 22.7493C2.63466 22.7411 2.85361 22.725 3.11822 22.6932C3.64462 22.6301 4.36636 22.5034 5.13797 22.2464C6.58274 21.7653 8.3431 20.7738 9.17063 18.7522C9.21696 18.639 9.26037 18.5226 9.30064 18.4029C9.30716 18.3835 9.31304 18.364 9.31827 18.3446Z"></path></svg>提示</p><div class="starlight-aside__content"><p>所做的任何文件更改也会被还原。</p></div></aside>


在内部，这使用 Git 来管理文件更改。因此您的项目**需要是一个 Git 仓库** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/undo</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/undo" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


**快捷键：** `ctrl+x u`
* * *
### unshare
取消分享当前会话。[了解更多](/docs/share#un-sharing)。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/unshare</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/unshare" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
## 编辑器设置
`/editor` 和 `/export` 命令都使用 `EDITOR` 环境变量中指定的编辑器。
**Linux/macOS:**

%%%PR_START_64ef58ea_PR_END%%%
要使其永久生效，请将其添加到您的 shell 配置文件中； `~/.bashrc`、`~/.zshrc` 等。

---

**Windows (CMD):**

%%%PR_START_f57420f4_PR_END%%%
要使其永久生效，请使用**系统属性** > **环境变量** 。

---

**Windows (PowerShell):**

%%%PR_START_52570a4b_PR_END%%%
要使其永久生效，请将其添加到您的 PowerShell 配置文件中。
常用的编辑器选项包括：
  * `code` \- Visual Studio Code
  * `cursor` \- Cursor
  * `windsurf` \- Windsurf
  * `nvim` \- Neovim 编辑器
  * `vim` \- Vim 编辑器
  * `nano` \- Nano 编辑器
  * `notepad` \- Notepad（Windows 记事本）
  * `subl` \- Sublime Text


<aside aria-label="注意" class="starlight-aside starlight-aside--note"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M12 11C11.7348 11 11.4804 11.1054 11.2929 11.2929C11.1054 11.4804 11 11.7348 11 12V16C11 16.2652 11.1054 16.5196 11.2929 16.7071C11.4804 16.8946 11.7348 17 12 17C12.2652 17 12.5196 16.8946 12.7071 16.7071C12.8946 16.5196 13 16.2652 13 16V12C13 11.7348 12.8946 11.4804 12.7071 11.2929C12.5196 11.1054 12.2652 11 12 11ZM12.38 7.08C12.1365 6.97998 11.8635 6.97998 11.62 7.08C11.4973 7.12759 11.3851 7.19896 11.29 7.29C11.2017 7.3872 11.1306 7.49882 11.08 7.62C11.024 7.73868 10.9966 7.86882 11 8C10.9992 8.13161 11.0245 8.26207 11.0742 8.38391C11.124 8.50574 11.1973 8.61656 11.29 8.71C11.3872 8.79833 11.4988 8.86936 11.62 8.92C11.7715 8.98224 11.936 9.00632 12.099 8.99011C12.2619 8.97391 12.4184 8.91792 12.5547 8.82707C12.691 8.73622 12.8029 8.61328 12.8805 8.46907C12.9582 8.32486 12.9992 8.16378 13 8C12.9963 7.73523 12.8927 7.48163 12.71 7.29C12.6149 7.19896 12.5028 7.12759 12.38 7.08ZM12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM12 20C10.4178 20 8.87104 19.5308 7.55544 18.6518C6.23985 17.7727 5.21447 16.5233 4.60897 15.0615C4.00347 13.5997 3.84504 11.9911 4.15372 10.4393C4.4624 8.88743 5.22433 7.46197 6.34315 6.34315C7.46197 5.22433 8.88743 4.4624 10.4393 4.15372C11.9911 3.84504 13.5997 4.00346 15.0615 4.60896C16.5233 5.21447 17.7727 6.23984 18.6518 7.55544C19.5308 8.87103 20 10.4177 20 12C20 14.1217 19.1572 16.1566 17.6569 17.6569C16.1566 19.1571 14.1217 20 12 20Z"></path></svg>注意</p><div class="starlight-aside__content"><p>某些编辑器（如 VS Code）需要以 <code dir="auto">--wait</code> 标志启动。</p></div></aside>


某些编辑器需要命令行参数才能以阻塞模式运行。`--wait` 标志使编辑器进程阻塞直到关闭。
* * *
## 配置
您可以通过 `tui.json`（或 `tui.jsonc`）自定义 TUI 行为。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">tui.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/tui.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"theme"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"opencode"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"leader_timeout"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#005CC5;--1:#79B8FF">2000</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"keybinds"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"leader"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"ctrl+x"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"command_list"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"ctrl+p"</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">},</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"scroll_speed"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#005CC5;--1:#79B8FF">3</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"scroll_acceleration"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"enabled"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#005CC5;--1:#79B8FF">false</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">},</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"diff_style"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"auto"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"mouse"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#005CC5;--1:#79B8FF">true</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"attention"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"enabled"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#005CC5;--1:#79B8FF">true</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"notifications"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#005CC5;--1:#79B8FF">true</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"sound"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#005CC5;--1:#79B8FF">true</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"volume"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#005CC5;--1:#79B8FF">0.4</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"sound_pack"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"opencode.default"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"sounds"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"error"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"./sounds/error.mp3"</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/tui.json",  "theme": "opencode",  "leader_timeout": 2000,  "keybinds": {    "leader": "ctrl+x",    "command_list": "ctrl+p"  },  "scroll_speed": 3,  "scroll_acceleration": {    "enabled": false  },  "diff_style": "auto",  "mouse": true,  "attention": {    "enabled": true,    "notifications": true,    "sound": true,    "volume": 0.4,    "sound_pack": "opencode.default",    "sounds": {      "error": "./sounds/error.mp3"    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


这与 `opencode.json` 是分开的；`opencode.json` 用于配置服务器和运行时行为。
`keybinds` 会与内置默认值合并，因此你只需要配置想要修改的快捷键。
### 选项
  * `theme` \- 设置 UI 主题。[了解更多](/docs/themes)。
  * `keybinds` \- 自定义键盘快捷键。[了解更多](/docs/keybinds)。
  * `leader_timeout` \- 控制按下 leader key 后 OpenCode 等待后续按键的时间。默认为 `2000`。
  * `scroll_acceleration.enabled` \- 启用 macOS 风格的滚动加速，让滚动更平滑自然。启用后，快速滚动时速度会增加，慢速移动时仍保持精确。**此设置优先于`scroll_speed`，启用时会覆盖它。**
  * `scroll_speed` \- 控制使用滚动命令时 TUI 的滚动速度（最小值：`0.001`，支持小数）。默认为 `3`。**注意：如果`scroll_acceleration.enabled` 设置为 `true`，则此设置会被忽略。**
  * `diff_style` \- 控制 diff 的显示方式。`"auto"` 会根据终端宽度自适应，`"stacked"` 始终显示单列布局。
  * `mouse` \- 在 TUI 中启用或禁用鼠标捕获（默认：`true`）。禁用后，终端原生的鼠标选择和滚动行为会保留下来。
  * `attention` \- 配置 TUI 桌面通知和声音。默认禁用。


使用 `OPENCODE_TUI_CONFIG` 可以加载自定义的 TUI 配置文件路径。
### Attention
当 OpenCode 需要你处理问题、批准权限请求、查看会话错误，或想告知会话已完成时，TUI 可以通过声音和桌面通知提醒你。设置 `attention.enabled` 后会启用这些提醒；内置事件触发时会播放声音。桌面通知只会在终端窗口未聚焦时发送，并且不会用于 subagent 事件。
  * `enabled` \- 开启 Attention 的所有通知和声音。默认为 `false`。
  * `notifications` \- 启用 Attention 后，允许 TUI 通过终端发送桌面通知。默认为 `true`。
  * `sound` \- 启用 Attention 后，允许播放提示音。默认为 `true`。
  * `volume` \- 默认提示音音量，范围从 `0` 到 `1`。默认为 `0.4`。
  * `sound_pack` \- 要使用的 sound pack ID。默认为 `opencode.default`。
  * `sounds` \- 为 `default`、`question`、`permission`、`error`、`done` 或 `subagent_done` 指定自定义声音文件。路径可以是绝对路径、`file://` URL，或相对于 `tui.json` 的路径。


* * *
## 自定义
您可以使用命令面板（`ctrl+x h` 或 `/help`）自定义 TUI 视图的各个方面。这些设置在重启后仍会保留。
* * *
#### 用户名显示
切换您的用户名是否显示在聊天消息中。通过以下方式访问：
  * 命令面板：搜索 “username” 或 “hide username”
  * 该设置会自动保存，并在各个 TUI 会话中保持记忆