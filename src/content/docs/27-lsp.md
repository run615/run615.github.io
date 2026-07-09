---
title: 'LSP 服务器'
description: 'OpenCode 与你的 LSP 服务器集成。'
category: '配置'
order: 27
slug: 'lsp'
---

OpenCode 可以与语言服务器协议（LSP）服务器集成，将诊断信息作为 agent 的反馈。
* * *
## 内置支持
OpenCode 内置了多种适用于主流语言的 LSP 服务器：
LSP 服务器| 扩展名| 要求  
---|---|---  
astro| .astro| 为 Astro 项目自动安装  
bash| .sh, .bash, .zsh, .ksh| 自动安装 bash-language-server  
clangd| .c, .cpp, .cc, .cxx, .c++, .h, .hpp, .hh, .hxx, .h++| 为 C/C++ 项目自动安装  
csharp| .cs| 需要已安装 `.NET SDK`  
clojure-lsp| .clj, .cljs, .cljc, .edn| 需要 `clojure-lsp` 命令可用  
dart| .dart| 需要 `dart` 命令可用  
deno| .ts, .tsx, .js, .jsx, .mjs| 需要 `deno` 命令可用（自动检测 deno.json/deno.jsonc）  
elixir-ls| .ex, .exs| 需要 `elixir` 命令可用  
eslint| .ts, .tsx, .js, .jsx, .mjs, .cjs, .mts, .cts, .vue| 项目中需要 `eslint` 依赖  
fsharp| .fs, .fsi, .fsx, .fsscript| 需要已安装 `.NET SDK`  
gleam| .gleam| 需要 `gleam` 命令可用  
gopls| .go| 需要 `go` 命令可用  
hls| .hs, .lhs| 需要 `haskell-language-server-wrapper` 命令可用  
jdtls| .java| 需要已安装 `Java SDK (version 21+)`  
julials| .jl| 需要安装 `julia` and `LanguageServer.jl`  
kotlin-ls| .kt, .kts| 为 Kotlin 项目自动安装  
lua-ls| .lua| 为 Lua 项目自动安装  
nixd| .nix| 需要 `nixd` 命令可用  
ocaml-lsp| .ml, .mli| 需要 `ocamllsp` 命令可用  
oxlint| .ts, .tsx, .js, .jsx, .mjs, .cjs, .mts, .cts, .vue, .astro, .svelte| 项目中需要 `oxlint` 依赖  
php intelephense| .php| 为 PHP 项目自动安装  
prisma| .prisma| 需要 `prisma` 命令可用  
pyright| .py, .pyi| 需要已安装 `pyright` 依赖  
ruby-lsp (rubocop)| .rb, .rake, .gemspec, .ru| 需要 `ruby` 和 `gem` 命令可用  
rust| .rs| 需要 `rust-analyzer` 命令可用  
sourcekit-lsp| .swift, .objc, .objcpp| 需要已安装 `swift`（macOS 上为 `xcode`）  
svelte| .svelte| 为 Svelte 项目自动安装  
terraform| .tf, .tfvars| 从 GitHub releases 自动安装  
tinymist| .typ, .typc| 从 GitHub releases 自动安装  
typescript| .ts, .tsx, .js, .jsx, .mjs, .cjs, .mts, .cts| 项目中需要 `typescript` 依赖  
vue| .vue| 为 Vue 项目自动安装  
yaml-ls| .yaml, .yml| 自动安装 Red Hat yaml-language-server  
zls| .zig, .zon| 需要 `zig` 命令可用  
LSP 默认关闭。启用后，当检测到上述文件扩展名且满足相应要求时，服务器会启动。


<aside aria-label="注意" class="starlight-aside starlight-aside--note"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M12 11C11.7348 11 11.4804 11.1054 11.2929 11.2929C11.1054 11.4804 11 11.7348 11 12V16C11 16.2652 11.1054 16.5196 11.2929 16.7071C11.4804 16.8946 11.7348 17 12 17C12.2652 17 12.5196 16.8946 12.7071 16.7071C12.8946 16.5196 13 16.2652 13 16V12C13 11.7348 12.8946 11.4804 12.7071 11.2929C12.5196 11.1054 12.2652 11 12 11ZM12.38 7.08C12.1365 6.97998 11.8635 6.97998 11.62 7.08C11.4973 7.12759 11.3851 7.19896 11.29 7.29C11.2017 7.3872 11.1306 7.49882 11.08 7.62C11.024 7.73868 10.9966 7.86882 11 8C10.9992 8.13161 11.0245 8.26207 11.0742 8.38391C11.124 8.50574 11.1973 8.61656 11.29 8.71C11.3872 8.79833 11.4988 8.86936 11.62 8.92C11.7715 8.98224 11.936 9.00632 12.099 8.99011C12.2619 8.97391 12.4184 8.91792 12.5547 8.82707C12.691 8.73622 12.8029 8.61328 12.8805 8.46907C12.9582 8.32486 12.9992 8.16378 13 8C12.9963 7.73523 12.8927 7.48163 12.71 7.29C12.6149 7.19896 12.5028 7.12759 12.38 7.08ZM12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM12 20C10.4178 20 8.87104 19.5308 7.55544 18.6518C6.23985 17.7727 5.21447 16.5233 4.60897 15.0615C4.00347 13.5997 3.84504 11.9911 4.15372 10.4393C4.4624 8.88743 5.22433 7.46197 6.34315 6.34315C7.46197 5.22433 8.88743 4.4624 10.4393 4.15372C11.9911 3.84504 13.5997 4.00346 15.0615 4.60896C16.5233 5.21447 17.7727 6.23984 18.6518 7.55544C19.5308 8.87103 20 10.4177 20 12C20 14.1217 19.1572 16.1566 17.6569 17.6569C16.1566 19.1571 14.1217 20 12 20Z"></path></svg>注意</p><div class="starlight-aside__content"><p>你可以将 <code dir="auto">OPENCODE_DISABLE_LSP_DOWNLOAD</code> 环境变量设置为 <code dir="auto">true</code> 来禁用 LSP 服务器的自动下载。</p></div></aside>


* * *
## 工作原理
启用 LSP 且 opencode 打开文件时，它会：
  1. 将文件扩展名与所有已启用的 LSP 服务器进行匹配。
  2. 如果对应的 LSP 服务器尚未运行，则自动启动它。


* * *
## 最佳实践
LSP 可以通过语言服务器诊断帮助 agent 发现并修复问题。这对某些项目很有用，但并不总是带来净收益。
语言服务器可能与项目不同步、占用较多内存、随版本或项目表现不同，并拖慢 agent 工作流。在许多项目中，更好的做法是让 agent 直接运行 lint、typecheck 或其他诊断类 CLI 工具，这样错误会进入 agent 循环，同时避免这些权衡。将这些命令记录在 `AGENTS.md` 或 skills 等指令文件中，让 agent 知道该运行什么。当你的项目能从额外的语言服务器反馈中受益时再启用 LSP。
* * *
## 配置
你可以通过 opencode 配置文件中的 `lsp` 部分来启用并自定义 LSP 服务器。
要启用所有内置 LSP 服务器，请将 `lsp` 设置为 `true`。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"lsp"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#005CC5;--1:#79B8FF">true</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "lsp": true}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


使用对象可以在保持内置服务器启用的同时配置覆盖项或自定义服务器。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"lsp"</span><span style="--0:#24292E;--1:#E1E4E8">: {}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "lsp": {}}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


每个 LSP 服务器支持以下配置项：
属性| 类型| 描述  
---|---|---  
`disabled`| boolean| 设置为 `true` 可禁用该 LSP 服务器  
`command`| string[]| 启动 LSP 服务器的命令  
`extensions`| string[]| 该 LSP 服务器需要处理的文件扩展名  
`env`| object| 启动服务器时设置的环境变量  
`initialization`| object| 发送给 LSP 服务器的初始化选项  
下面来看一些示例。
* * *
### 环境变量
使用 `env` 属性在启动 LSP 服务器时设置环境变量：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"lsp"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"rust"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"env"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">        </span><span style="--0:#004ba0;--1:#81bcff">"RUST_LOG"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"debug"</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "lsp": {    "rust": {      "env": {        "RUST_LOG": "debug"      }    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### 初始化选项
使用 `initialization` 属性向 LSP 服务器传递初始化选项。这些是在 LSP `initialize` 请求期间发送的服务器特定设置：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"lsp"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"typescript"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"initialization"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">        </span><span style="--0:#004ba0;--1:#81bcff">"preferences"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">          </span><span style="--0:#004ba0;--1:#81bcff">"importModuleSpecifierPreference"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"relative"</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">        </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "lsp": {    "typescript": {      "initialization": {        "preferences": {          "importModuleSpecifierPreference": "relative"        }      }    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>

 

<aside aria-label="注意" class="starlight-aside starlight-aside--note"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M12 11C11.7348 11 11.4804 11.1054 11.2929 11.2929C11.1054 11.4804 11 11.7348 11 12V16C11 16.2652 11.1054 16.5196 11.2929 16.7071C11.4804 16.8946 11.7348 17 12 17C12.2652 17 12.5196 16.8946 12.7071 16.7071C12.8946 16.5196 13 16.2652 13 16V12C13 11.7348 12.8946 11.4804 12.7071 11.2929C12.5196 11.1054 12.2652 11 12 11ZM12.38 7.08C12.1365 6.97998 11.8635 6.97998 11.62 7.08C11.4973 7.12759 11.3851 7.19896 11.29 7.29C11.2017 7.3872 11.1306 7.49882 11.08 7.62C11.024 7.73868 10.9966 7.86882 11 8C10.9992 8.13161 11.0245 8.26207 11.0742 8.38391C11.124 8.50574 11.1973 8.61656 11.29 8.71C11.3872 8.79833 11.4988 8.86936 11.62 8.92C11.7715 8.98224 11.936 9.00632 12.099 8.99011C12.2619 8.97391 12.4184 8.91792 12.5547 8.82707C12.691 8.73622 12.8029 8.61328 12.8805 8.46907C12.9582 8.32486 12.9992 8.16378 13 8C12.9963 7.73523 12.8927 7.48163 12.71 7.29C12.6149 7.19896 12.5028 7.12759 12.38 7.08ZM12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM12 20C10.4178 20 8.87104 19.5308 7.55544 18.6518C6.23985 17.7727 5.21447 16.5233 4.60897 15.0615C4.00347 13.5997 3.84504 11.9911 4.15372 10.4393C4.4624 8.88743 5.22433 7.46197 6.34315 6.34315C7.46197 5.22433 8.88743 4.4624 10.4393 4.15372C11.9911 3.84504 13.5997 4.00346 15.0615 4.60896C16.5233 5.21447 17.7727 6.23984 18.6518 7.55544C19.5308 8.87103 20 10.4177 20 12C20 14.1217 19.1572 16.1566 17.6569 17.6569C16.1566 19.1571 14.1217 20 12 20Z"></path></svg>注意</p><div class="starlight-aside__content"><p>初始化选项因 LSP 服务器而异。请查阅你所使用的 LSP 服务器的文档以了解可用选项。</p></div></aside>


* * *
### 禁用 LSP 服务器
如果省略 `lsp`，所有 LSP 服务器都会被禁用。如果另一个配置启用了 LSP，可将 `lsp` 设置为 `false` 来禁用所有 LSP 服务器：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">  </span><span style="--0:#004ba0;--1:#81bcff">"lsp"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#004ba0;--1:#81bcff">false</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "lsp": false}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


要禁用**特定的** LSP 服务器，将 `disabled` 设置为 `true`：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"lsp"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"typescript"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"disabled"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#004ba0;--1:#81bcff">true</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "lsp": {    "typescript": {      "disabled": true    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### 自定义 LSP 服务器
你可以通过指定命令和文件扩展名来添加自定义 LSP 服务器：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"lsp"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">    </span><span style="--0:#004ba0;--1:#81bcff">"custom-lsp"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"command"</span><span style="--0:#24292E;--1:#E1E4E8">: [</span><span style="--0:#032F62;--1:#9ECBFF">"custom-lsp-server"</span><span style="--0:#24292E;--1:#E1E4E8">, </span><span style="--0:#032F62;--1:#9ECBFF">"--stdio"</span><span style="--0:#24292E;--1:#E1E4E8">],</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"extensions"</span><span style="--0:#24292E;--1:#E1E4E8">: [</span><span style="--0:#032F62;--1:#9ECBFF">".custom"</span><span style="--0:#24292E;--1:#E1E4E8">]</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "lsp": {    "custom-lsp": {      "command": ["custom-lsp-server", "--stdio"],      "extensions": [".custom"]    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
## 补充信息
### PHP Intelephense
PHP Intelephense 通过许可证密钥提供高级功能。你可以将许可证密钥单独放在以下路径的文本文件中：
  * macOS/Linux：`$HOME/intelephense/license.txt`
  * Windows：`%USERPROFILE%/intelephense/license.txt`


该文件应仅包含许可证密钥，不要添加其他任何内容。