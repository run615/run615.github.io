---
title: 简介'
description: '开始使用 OpenCode。'
category: 'OpenCode 开发手册'
order: 1
slug: 'opencode/intro'
---

[**OpenCode**](https://opencode.ai/) 是一个开源的 AI 编码代理。它提供终端界面、桌面应用和 IDE 扩展等多种使用方式。
让我们开始吧。
* * *
#### 前提条件
要在终端中使用 OpenCode，你需要：
  1. 一款现代终端模拟器，例如：
     * [WezTerm](https://wezterm.org)，跨平台
     * [Alacritty](https://alacritty.org)，跨平台
     * [Ghostty](https://ghostty.org)，Linux 和 macOS
     * [Kitty](https://sw.kovidgoyal.net/kitty/)，Linux 和 macOS
  2. 你想使用的 LLM 提供商的 API 密钥。


* * *
## 安装
安装 OpenCode 最简单的方法是通过安装脚本。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">curl</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#005CC5;--1:#79B8FF">-fsSL</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">https://opencode.ai/install</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#BF3441;--1:#F97583">|</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#6F42C1;--1:#B392F0">bash</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="curl -fsSL https://opencode.ai/install | bash" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


你也可以使用以下方式安装：
  * **使用 Node.js**
**npm:**

%%%PR_START_e00e22c7_PR_END%%%

---

**Bun:**

%%%PR_START_609f80bb_PR_END%%%

---

**pnpm:**

%%%PR_START_dd6aa15c_PR_END%%%

---

**Yarn:**

%%%PR_START_512d6a96_PR_END%%%
  * **在 macOS 和 Linux 上使用 Homebrew**


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">brew</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">install</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">anomalyco/tap/opencode</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="brew install anomalyco/tap/opencode" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


> 我们推荐使用 OpenCode tap 以获取最新版本。官方的 `brew install opencode` formula 由 Homebrew 团队维护，更新频率较低。
  * **在 Arch Linux 上安装**


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">sudo</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">pacman</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#005CC5;--1:#79B8FF">-S</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">opencode</span><span style="--0:#24292E;--1:#E1E4E8">           </span><span style="--0:#616972;--1:#99A0A6"># Arch Linux (Stable)</span></div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">paru</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#005CC5;--1:#79B8FF">-S</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">opencode-bin</span><span style="--0:#24292E;--1:#E1E4E8">              </span><span style="--0:#616972;--1:#99A0A6"># Arch Linux (Latest from AUR)</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="sudo pacman -S opencode           # Arch Linux (Stable)paru -S opencode-bin              # Arch Linux (Latest from AUR)" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


#### Windows


<aside aria-label="推荐：使用 WSL" class="starlight-aside starlight-aside--tip"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path clip-rule="evenodd" d="M1.43909 8.85483L1.44039 8.85354L4.96668 5.33815C5.30653 4.99386 5.7685 4.79662 6.2524 4.78972L6.26553 4.78963L12.9014 4.78962L13.8479 3.84308C16.9187 0.772319 20.0546 0.770617 21.4678 0.975145C21.8617 1.02914 22.2271 1.21053 22.5083 1.4917C22.7894 1.77284 22.9708 2.13821 23.0248 2.53199C23.2294 3.94517 23.2278 7.08119 20.1569 10.1521L19.2107 11.0983V17.7338L19.2106 17.7469C19.2037 18.2308 19.0067 18.6933 18.6624 19.0331L15.1456 22.5608C14.9095 22.7966 14.6137 22.964 14.29 23.0449C13.9663 23.1259 13.6267 23.1174 13.3074 23.0204C12.9881 22.9235 12.7011 22.7417 12.4771 22.4944C12.2533 22.2473 12.1006 21.9441 12.0355 21.6171L11.1783 17.3417L6.65869 12.822L4.34847 12.3589L2.38351 11.965C2.05664 11.8998 1.75272 11.747 1.50564 11.5232C1.25835 11.2992 1.07653 11.0122 0.979561 10.6929C0.882595 10.3736 0.874125 10.034 0.955057 9.7103C1.03599 9.38659 1.20328 9.09092 1.43909 8.85483ZM6.8186 10.8724L2.94619 10.096L6.32006 6.73268H10.9583L6.8186 10.8724ZM15.2219 5.21703C17.681 2.75787 20.0783 2.75376 21.1124 2.8876C21.2462 3.92172 21.2421 6.31895 18.783 8.77812L12.0728 15.4883L8.51172 11.9272L15.2219 5.21703ZM13.9042 21.0538L13.1279 17.1811L17.2676 13.0414V17.68L13.9042 21.0538Z" fill-rule="evenodd"></path><path d="M9.31827 18.3446C9.45046 17.8529 9.17864 17.3369 8.68945 17.1724C8.56178 17.1294 8.43145 17.1145 8.30512 17.1243C8.10513 17.1398 7.91519 17.2172 7.76181 17.3434C7.62613 17.455 7.51905 17.6048 7.45893 17.7835C6.97634 19.2186 5.77062 19.9878 4.52406 20.4029C4.08525 20.549 3.6605 20.644 3.29471 20.7053C3.35607 20.3395 3.45098 19.9148 3.59711 19.476C4.01221 18.2294 4.78141 17.0237 6.21648 16.5411C6.39528 16.481 6.54504 16.3739 6.65665 16.2382C6.85126 16.0016 6.92988 15.678 6.84417 15.3647C6.83922 15.3466 6.83373 15.3286 6.82767 15.3106C6.74106 15.053 6.55701 14.8557 6.33037 14.7459C6.10949 14.6389 5.84816 14.615 5.59715 14.6994C5.47743 14.7397 5.36103 14.7831 5.24786 14.8294C3.22626 15.6569 2.2347 17.4173 1.75357 18.8621C1.49662 19.6337 1.36993 20.3554 1.30679 20.8818C1.27505 21.1464 1.25893 21.3654 1.25072 21.5213C1.24662 21.5993 1.24448 21.6618 1.24337 21.7066L1.243 21.7226L1.24235 21.7605L1.2422 21.7771L1.24217 21.7827L1.24217 21.7856C1.24217 22.3221 1.67703 22.7579 2.2137 22.7579L2.2155 22.7579L2.22337 22.7578L2.23956 22.7577C2.25293 22.7575 2.27096 22.7572 2.29338 22.7567C2.33821 22.7555 2.40073 22.7534 2.47876 22.7493C2.63466 22.7411 2.85361 22.725 3.11822 22.6932C3.64462 22.6301 4.36636 22.5034 5.13797 22.2464C6.58274 21.7653 8.3431 20.7738 9.17063 18.7522C9.21696 18.639 9.26037 18.5226 9.30064 18.4029C9.30716 18.3835 9.31304 18.364 9.31827 18.3446Z"></path></svg>推荐：使用 WSL</p><div class="starlight-aside__content"><p>为了在 Windows 上获得最佳体验，我们推荐使用 <a href="/docs/windows-wsl">Windows Subsystem for Linux (WSL)</a>。它提供更好的性能，并完全兼容 OpenCode 的所有功能。</p></div></aside>


  * **使用 Chocolatey**


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">choco</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">install</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">opencode</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="choco install opencode" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  * **使用 Scoop**


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">scoop</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">install</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">opencode</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="scoop install opencode" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  * **使用 NPM**


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">npm</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">install</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#005CC5;--1:#79B8FF">-g</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">opencode-ai</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="npm install -g opencode-ai" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  * **使用 Mise**


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">mise</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">use</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#005CC5;--1:#79B8FF">-g</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">github:anomalyco/opencode</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="mise use -g github:anomalyco/opencode" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  * **使用 Docker**


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">docker</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">run</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#005CC5;--1:#79B8FF">-it</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#005CC5;--1:#79B8FF">--rm</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">ghcr.io/anomalyco/opencode</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="docker run -it --rm ghcr.io/anomalyco/opencode" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


在 Windows 上通过 Bun 安装 OpenCode 的支持目前正在开发中。
你也可以从 [Releases](https://github.com/anomalyco/opencode/releases) 页面直接下载二进制文件。
* * *
## 配置
通过 OpenCode，你可以配置 API 密钥来使用任意 LLM 提供商。
如果你刚开始接触 LLM 提供商，我们推荐使用 [OpenCode Zen](/docs/zen)。这是一组经过 OpenCode 团队测试和验证的精选模型。
  1. 在 TUI 中运行 `/connect` 命令，选择 opencode，然后前往 [opencode.ai/auth](https://opencode.ai/auth)。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  2. 登录并添加账单信息，然后复制你的 API 密钥。
  3. 粘贴你的 API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


你也可以选择其他提供商。[了解更多](/docs/providers#directory)。
* * *
## 初始化
配置好提供商后，导航到你想要处理的项目目录。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#005CC5;--1:#79B8FF">cd</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">/path/to/project</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="cd /path/to/project" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


然后运行 OpenCode。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">opencode</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="opencode" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


接下来，运行以下命令为项目初始化 OpenCode。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/init</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/init" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


OpenCode 会分析你的项目并在项目根目录创建一个 `AGENTS.md` 文件。


<aside aria-label="提示" class="starlight-aside starlight-aside--tip"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path clip-rule="evenodd" d="M1.43909 8.85483L1.44039 8.85354L4.96668 5.33815C5.30653 4.99386 5.7685 4.79662 6.2524 4.78972L6.26553 4.78963L12.9014 4.78962L13.8479 3.84308C16.9187 0.772319 20.0546 0.770617 21.4678 0.975145C21.8617 1.02914 22.2271 1.21053 22.5083 1.4917C22.7894 1.77284 22.9708 2.13821 23.0248 2.53199C23.2294 3.94517 23.2278 7.08119 20.1569 10.1521L19.2107 11.0983V17.7338L19.2106 17.7469C19.2037 18.2308 19.0067 18.6933 18.6624 19.0331L15.1456 22.5608C14.9095 22.7966 14.6137 22.964 14.29 23.0449C13.9663 23.1259 13.6267 23.1174 13.3074 23.0204C12.9881 22.9235 12.7011 22.7417 12.4771 22.4944C12.2533 22.2473 12.1006 21.9441 12.0355 21.6171L11.1783 17.3417L6.65869 12.822L4.34847 12.3589L2.38351 11.965C2.05664 11.8998 1.75272 11.747 1.50564 11.5232C1.25835 11.2992 1.07653 11.0122 0.979561 10.6929C0.882595 10.3736 0.874125 10.034 0.955057 9.7103C1.03599 9.38659 1.20328 9.09092 1.43909 8.85483ZM6.8186 10.8724L2.94619 10.096L6.32006 6.73268H10.9583L6.8186 10.8724ZM15.2219 5.21703C17.681 2.75787 20.0783 2.75376 21.1124 2.8876C21.2462 3.92172 21.2421 6.31895 18.783 8.77812L12.0728 15.4883L8.51172 11.9272L15.2219 5.21703ZM13.9042 21.0538L13.1279 17.1811L17.2676 13.0414V17.68L13.9042 21.0538Z" fill-rule="evenodd"></path><path d="M9.31827 18.3446C9.45046 17.8529 9.17864 17.3369 8.68945 17.1724C8.56178 17.1294 8.43145 17.1145 8.30512 17.1243C8.10513 17.1398 7.91519 17.2172 7.76181 17.3434C7.62613 17.455 7.51905 17.6048 7.45893 17.7835C6.97634 19.2186 5.77062 19.9878 4.52406 20.4029C4.08525 20.549 3.6605 20.644 3.29471 20.7053C3.35607 20.3395 3.45098 19.9148 3.59711 19.476C4.01221 18.2294 4.78141 17.0237 6.21648 16.5411C6.39528 16.481 6.54504 16.3739 6.65665 16.2382C6.85126 16.0016 6.92988 15.678 6.84417 15.3647C6.83922 15.3466 6.83373 15.3286 6.82767 15.3106C6.74106 15.053 6.55701 14.8557 6.33037 14.7459C6.10949 14.6389 5.84816 14.615 5.59715 14.6994C5.47743 14.7397 5.36103 14.7831 5.24786 14.8294C3.22626 15.6569 2.2347 17.4173 1.75357 18.8621C1.49662 19.6337 1.36993 20.3554 1.30679 20.8818C1.27505 21.1464 1.25893 21.3654 1.25072 21.5213C1.24662 21.5993 1.24448 21.6618 1.24337 21.7066L1.243 21.7226L1.24235 21.7605L1.2422 21.7771L1.24217 21.7827L1.24217 21.7856C1.24217 22.3221 1.67703 22.7579 2.2137 22.7579L2.2155 22.7579L2.22337 22.7578L2.23956 22.7577C2.25293 22.7575 2.27096 22.7572 2.29338 22.7567C2.33821 22.7555 2.40073 22.7534 2.47876 22.7493C2.63466 22.7411 2.85361 22.725 3.11822 22.6932C3.64462 22.6301 4.36636 22.5034 5.13797 22.2464C6.58274 21.7653 8.3431 20.7738 9.17063 18.7522C9.21696 18.639 9.26037 18.5226 9.30064 18.4029C9.30716 18.3835 9.31304 18.364 9.31827 18.3446Z"></path></svg>提示</p><div class="starlight-aside__content"><p>你应该将项目的 <code dir="auto">AGENTS.md</code> 文件提交到 Git。</p></div></aside>


这有助于 OpenCode 理解项目结构和编码规范。
* * *
## 使用
现在你已经准备好使用 OpenCode 来处理项目了，尽管提问吧！
如果你是第一次使用 AI 编码代理，以下示例可能会对你有所帮助。
* * *
### 提问
你可以让 OpenCode 为你讲解代码库。


<aside aria-label="提示" class="starlight-aside starlight-aside--tip"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path clip-rule="evenodd" d="M1.43909 8.85483L1.44039 8.85354L4.96668 5.33815C5.30653 4.99386 5.7685 4.79662 6.2524 4.78972L6.26553 4.78963L12.9014 4.78962L13.8479 3.84308C16.9187 0.772319 20.0546 0.770617 21.4678 0.975145C21.8617 1.02914 22.2271 1.21053 22.5083 1.4917C22.7894 1.77284 22.9708 2.13821 23.0248 2.53199C23.2294 3.94517 23.2278 7.08119 20.1569 10.1521L19.2107 11.0983V17.7338L19.2106 17.7469C19.2037 18.2308 19.0067 18.6933 18.6624 19.0331L15.1456 22.5608C14.9095 22.7966 14.6137 22.964 14.29 23.0449C13.9663 23.1259 13.6267 23.1174 13.3074 23.0204C12.9881 22.9235 12.7011 22.7417 12.4771 22.4944C12.2533 22.2473 12.1006 21.9441 12.0355 21.6171L11.1783 17.3417L6.65869 12.822L4.34847 12.3589L2.38351 11.965C2.05664 11.8998 1.75272 11.747 1.50564 11.5232C1.25835 11.2992 1.07653 11.0122 0.979561 10.6929C0.882595 10.3736 0.874125 10.034 0.955057 9.7103C1.03599 9.38659 1.20328 9.09092 1.43909 8.85483ZM6.8186 10.8724L2.94619 10.096L6.32006 6.73268H10.9583L6.8186 10.8724ZM15.2219 5.21703C17.681 2.75787 20.0783 2.75376 21.1124 2.8876C21.2462 3.92172 21.2421 6.31895 18.783 8.77812L12.0728 15.4883L8.51172 11.9272L15.2219 5.21703ZM13.9042 21.0538L13.1279 17.1811L17.2676 13.0414V17.68L13.9042 21.0538Z" fill-rule="evenodd"></path><path d="M9.31827 18.3446C9.45046 17.8529 9.17864 17.3369 8.68945 17.1724C8.56178 17.1294 8.43145 17.1145 8.30512 17.1243C8.10513 17.1398 7.91519 17.2172 7.76181 17.3434C7.62613 17.455 7.51905 17.6048 7.45893 17.7835C6.97634 19.2186 5.77062 19.9878 4.52406 20.4029C4.08525 20.549 3.6605 20.644 3.29471 20.7053C3.35607 20.3395 3.45098 19.9148 3.59711 19.476C4.01221 18.2294 4.78141 17.0237 6.21648 16.5411C6.39528 16.481 6.54504 16.3739 6.65665 16.2382C6.85126 16.0016 6.92988 15.678 6.84417 15.3647C6.83922 15.3466 6.83373 15.3286 6.82767 15.3106C6.74106 15.053 6.55701 14.8557 6.33037 14.7459C6.10949 14.6389 5.84816 14.615 5.59715 14.6994C5.47743 14.7397 5.36103 14.7831 5.24786 14.8294C3.22626 15.6569 2.2347 17.4173 1.75357 18.8621C1.49662 19.6337 1.36993 20.3554 1.30679 20.8818C1.27505 21.1464 1.25893 21.3654 1.25072 21.5213C1.24662 21.5993 1.24448 21.6618 1.24337 21.7066L1.243 21.7226L1.24235 21.7605L1.2422 21.7771L1.24217 21.7827L1.24217 21.7856C1.24217 22.3221 1.67703 22.7579 2.2137 22.7579L2.2155 22.7579L2.22337 22.7578L2.23956 22.7577C2.25293 22.7575 2.27096 22.7572 2.29338 22.7567C2.33821 22.7555 2.40073 22.7534 2.47876 22.7493C2.63466 22.7411 2.85361 22.725 3.11822 22.6932C3.64462 22.6301 4.36636 22.5034 5.13797 22.2464C6.58274 21.7653 8.3431 20.7738 9.17063 18.7522C9.21696 18.639 9.26037 18.5226 9.30064 18.4029C9.30716 18.3835 9.31304 18.364 9.31827 18.3446Z"></path></svg>提示</p><div class="starlight-aside__content"><p>使用 <code dir="auto">@</code> 键可以模糊搜索项目中的文件。</p></div></aside>

 

<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">How is authentication handled in </span><mark><span style="--0:#24292e;--1:#e1e4e8">@packages/functions/src/api/index.ts</span></mark></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="How is authentication handled in @packages/functions/src/api/index.ts" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


当你遇到不熟悉的代码时，这个功能非常有用。
* * *
### 添加功能
你可以让 OpenCode 为项目添加新功能。不过我们建议先让它制定一个计划。
  1. **制定计划**
OpenCode 有一个 _计划模式_ ，该模式下它不会进行任何修改，而是建议 _如何_ 实现该功能。
使用 **Tab** 键切换到计划模式。你会在右下角看到模式指示器。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">&lt;TAB&gt;</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="&lt;TAB&gt;" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


接下来描述你希望它做什么。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">When a user deletes a note, we'd like to flag it as deleted in the database.</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">Then create a screen that shows all the recently deleted notes.</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">From this screen, the user can undelete a note or permanently delete it.</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="When a user deletes a note, we'd like to flag it as deleted in the database.Then create a screen that shows all the recently deleted notes.From this screen, the user can undelete a note or permanently delete it." data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


你需要提供足够的细节，让 OpenCode 理解你的需求。可以把它当作团队中的一名初级开发者来沟通。


<aside aria-label="提示" class="starlight-aside starlight-aside--tip"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path clip-rule="evenodd" d="M1.43909 8.85483L1.44039 8.85354L4.96668 5.33815C5.30653 4.99386 5.7685 4.79662 6.2524 4.78972L6.26553 4.78963L12.9014 4.78962L13.8479 3.84308C16.9187 0.772319 20.0546 0.770617 21.4678 0.975145C21.8617 1.02914 22.2271 1.21053 22.5083 1.4917C22.7894 1.77284 22.9708 2.13821 23.0248 2.53199C23.2294 3.94517 23.2278 7.08119 20.1569 10.1521L19.2107 11.0983V17.7338L19.2106 17.7469C19.2037 18.2308 19.0067 18.6933 18.6624 19.0331L15.1456 22.5608C14.9095 22.7966 14.6137 22.964 14.29 23.0449C13.9663 23.1259 13.6267 23.1174 13.3074 23.0204C12.9881 22.9235 12.7011 22.7417 12.4771 22.4944C12.2533 22.2473 12.1006 21.9441 12.0355 21.6171L11.1783 17.3417L6.65869 12.822L4.34847 12.3589L2.38351 11.965C2.05664 11.8998 1.75272 11.747 1.50564 11.5232C1.25835 11.2992 1.07653 11.0122 0.979561 10.6929C0.882595 10.3736 0.874125 10.034 0.955057 9.7103C1.03599 9.38659 1.20328 9.09092 1.43909 8.85483ZM6.8186 10.8724L2.94619 10.096L6.32006 6.73268H10.9583L6.8186 10.8724ZM15.2219 5.21703C17.681 2.75787 20.0783 2.75376 21.1124 2.8876C21.2462 3.92172 21.2421 6.31895 18.783 8.77812L12.0728 15.4883L8.51172 11.9272L15.2219 5.21703ZM13.9042 21.0538L13.1279 17.1811L17.2676 13.0414V17.68L13.9042 21.0538Z" fill-rule="evenodd"></path><path d="M9.31827 18.3446C9.45046 17.8529 9.17864 17.3369 8.68945 17.1724C8.56178 17.1294 8.43145 17.1145 8.30512 17.1243C8.10513 17.1398 7.91519 17.2172 7.76181 17.3434C7.62613 17.455 7.51905 17.6048 7.45893 17.7835C6.97634 19.2186 5.77062 19.9878 4.52406 20.4029C4.08525 20.549 3.6605 20.644 3.29471 20.7053C3.35607 20.3395 3.45098 19.9148 3.59711 19.476C4.01221 18.2294 4.78141 17.0237 6.21648 16.5411C6.39528 16.481 6.54504 16.3739 6.65665 16.2382C6.85126 16.0016 6.92988 15.678 6.84417 15.3647C6.83922 15.3466 6.83373 15.3286 6.82767 15.3106C6.74106 15.053 6.55701 14.8557 6.33037 14.7459C6.10949 14.6389 5.84816 14.615 5.59715 14.6994C5.47743 14.7397 5.36103 14.7831 5.24786 14.8294C3.22626 15.6569 2.2347 17.4173 1.75357 18.8621C1.49662 19.6337 1.36993 20.3554 1.30679 20.8818C1.27505 21.1464 1.25893 21.3654 1.25072 21.5213C1.24662 21.5993 1.24448 21.6618 1.24337 21.7066L1.243 21.7226L1.24235 21.7605L1.2422 21.7771L1.24217 21.7827L1.24217 21.7856C1.24217 22.3221 1.67703 22.7579 2.2137 22.7579L2.2155 22.7579L2.22337 22.7578L2.23956 22.7577C2.25293 22.7575 2.27096 22.7572 2.29338 22.7567C2.33821 22.7555 2.40073 22.7534 2.47876 22.7493C2.63466 22.7411 2.85361 22.725 3.11822 22.6932C3.64462 22.6301 4.36636 22.5034 5.13797 22.2464C6.58274 21.7653 8.3431 20.7738 9.17063 18.7522C9.21696 18.639 9.26037 18.5226 9.30064 18.4029C9.30716 18.3835 9.31304 18.364 9.31827 18.3446Z"></path></svg>提示</p><div class="starlight-aside__content"><p>为 OpenCode 提供充足的上下文和示例，帮助它理解你的需求。</p></div></aside>


  2. **迭代计划**
当它给出计划后，你可以提供反馈或补充更多细节。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">We'd like to design this new screen using a design I've used before.</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">[Image #1] Take a look at this image and use it as a reference.</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="We'd like to design this new screen using a design I've used before.[Image #1] Take a look at this image and use it as a reference." data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>

 

<aside aria-label="提示" class="starlight-aside starlight-aside--tip"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path clip-rule="evenodd" d="M1.43909 8.85483L1.44039 8.85354L4.96668 5.33815C5.30653 4.99386 5.7685 4.79662 6.2524 4.78972L6.26553 4.78963L12.9014 4.78962L13.8479 3.84308C16.9187 0.772319 20.0546 0.770617 21.4678 0.975145C21.8617 1.02914 22.2271 1.21053 22.5083 1.4917C22.7894 1.77284 22.9708 2.13821 23.0248 2.53199C23.2294 3.94517 23.2278 7.08119 20.1569 10.1521L19.2107 11.0983V17.7338L19.2106 17.7469C19.2037 18.2308 19.0067 18.6933 18.6624 19.0331L15.1456 22.5608C14.9095 22.7966 14.6137 22.964 14.29 23.0449C13.9663 23.1259 13.6267 23.1174 13.3074 23.0204C12.9881 22.9235 12.7011 22.7417 12.4771 22.4944C12.2533 22.2473 12.1006 21.9441 12.0355 21.6171L11.1783 17.3417L6.65869 12.822L4.34847 12.3589L2.38351 11.965C2.05664 11.8998 1.75272 11.747 1.50564 11.5232C1.25835 11.2992 1.07653 11.0122 0.979561 10.6929C0.882595 10.3736 0.874125 10.034 0.955057 9.7103C1.03599 9.38659 1.20328 9.09092 1.43909 8.85483ZM6.8186 10.8724L2.94619 10.096L6.32006 6.73268H10.9583L6.8186 10.8724ZM15.2219 5.21703C17.681 2.75787 20.0783 2.75376 21.1124 2.8876C21.2462 3.92172 21.2421 6.31895 18.783 8.77812L12.0728 15.4883L8.51172 11.9272L15.2219 5.21703ZM13.9042 21.0538L13.1279 17.1811L17.2676 13.0414V17.68L13.9042 21.0538Z" fill-rule="evenodd"></path><path d="M9.31827 18.3446C9.45046 17.8529 9.17864 17.3369 8.68945 17.1724C8.56178 17.1294 8.43145 17.1145 8.30512 17.1243C8.10513 17.1398 7.91519 17.2172 7.76181 17.3434C7.62613 17.455 7.51905 17.6048 7.45893 17.7835C6.97634 19.2186 5.77062 19.9878 4.52406 20.4029C4.08525 20.549 3.6605 20.644 3.29471 20.7053C3.35607 20.3395 3.45098 19.9148 3.59711 19.476C4.01221 18.2294 4.78141 17.0237 6.21648 16.5411C6.39528 16.481 6.54504 16.3739 6.65665 16.2382C6.85126 16.0016 6.92988 15.678 6.84417 15.3647C6.83922 15.3466 6.83373 15.3286 6.82767 15.3106C6.74106 15.053 6.55701 14.8557 6.33037 14.7459C6.10949 14.6389 5.84816 14.615 5.59715 14.6994C5.47743 14.7397 5.36103 14.7831 5.24786 14.8294C3.22626 15.6569 2.2347 17.4173 1.75357 18.8621C1.49662 19.6337 1.36993 20.3554 1.30679 20.8818C1.27505 21.1464 1.25893 21.3654 1.25072 21.5213C1.24662 21.5993 1.24448 21.6618 1.24337 21.7066L1.243 21.7226L1.24235 21.7605L1.2422 21.7771L1.24217 21.7827L1.24217 21.7856C1.24217 22.3221 1.67703 22.7579 2.2137 22.7579L2.2155 22.7579L2.22337 22.7578L2.23956 22.7577C2.25293 22.7575 2.27096 22.7572 2.29338 22.7567C2.33821 22.7555 2.40073 22.7534 2.47876 22.7493C2.63466 22.7411 2.85361 22.725 3.11822 22.6932C3.64462 22.6301 4.36636 22.5034 5.13797 22.2464C6.58274 21.7653 8.3431 20.7738 9.17063 18.7522C9.21696 18.639 9.26037 18.5226 9.30064 18.4029C9.30716 18.3835 9.31304 18.364 9.31827 18.3446Z"></path></svg>提示</p><div class="starlight-aside__content"><p>将图片拖放到终端中即可将其添加到提示词中。</p></div></aside>


OpenCode 可以扫描你提供的图片并将其添加到提示词中。只需将图片拖放到终端窗口即可。
  3. **构建功能**
当你对计划满意后，再次按 **Tab** 键切换回 _构建模式_ 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">&lt;TAB&gt;</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="&lt;TAB&gt;" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


然后让它开始实施。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">Sounds</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">good!</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">Go</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">ahead</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">and</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">make</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">the</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">changes.</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="Sounds good! Go ahead and make the changes." data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### 直接修改
对于比较简单的修改，你可以直接让 OpenCode 实施，无需先审查计划。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">We need to add authentication to the /settings route. Take a look at how this is</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">handled in the /notes route in </span><mark><span style="--0:#24292e;--1:#e1e4e8">@packages/functions/src/notes.ts</span></mark><span style="--0:#24292e;--1:#e1e4e8"> and implement</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">the same logic in </span><mark><span style="--0:#24292e;--1:#e1e4e8">@packages/functions/src/settings.ts</span></mark></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="We need to add authentication to the /settings route. Take a look at how this ishandled in the /notes route in @packages/functions/src/notes.ts and implementthe same logic in @packages/functions/src/settings.ts" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


请确保提供足够的细节，以便 OpenCode 做出正确的修改。
* * *
### 撤销修改
假设你让 OpenCode 做了一些修改。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">Can you refactor the function in </span><mark><span style="--0:#24292e;--1:#e1e4e8">@packages/functions/src/api/index.ts</span></mark><span style="--0:#24292e;--1:#e1e4e8">?</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="Can you refactor the function in @packages/functions/src/api/index.ts?" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


但你发现结果不是你想要的。你**可以使用** `/undo` 命令来撤销修改。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/undo</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/undo" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


OpenCode 会还原所做的修改，并重新显示你之前的消息。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">Can you refactor the function in </span><mark><span style="--0:#24292e;--1:#e1e4e8">@packages/functions/src/api/index.ts</span></mark><span style="--0:#24292e;--1:#e1e4e8">?</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="Can you refactor the function in @packages/functions/src/api/index.ts?" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


你可以调整提示词，让 OpenCode 重新尝试。


<aside aria-label="提示" class="starlight-aside starlight-aside--tip"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path clip-rule="evenodd" d="M1.43909 8.85483L1.44039 8.85354L4.96668 5.33815C5.30653 4.99386 5.7685 4.79662 6.2524 4.78972L6.26553 4.78963L12.9014 4.78962L13.8479 3.84308C16.9187 0.772319 20.0546 0.770617 21.4678 0.975145C21.8617 1.02914 22.2271 1.21053 22.5083 1.4917C22.7894 1.77284 22.9708 2.13821 23.0248 2.53199C23.2294 3.94517 23.2278 7.08119 20.1569 10.1521L19.2107 11.0983V17.7338L19.2106 17.7469C19.2037 18.2308 19.0067 18.6933 18.6624 19.0331L15.1456 22.5608C14.9095 22.7966 14.6137 22.964 14.29 23.0449C13.9663 23.1259 13.6267 23.1174 13.3074 23.0204C12.9881 22.9235 12.7011 22.7417 12.4771 22.4944C12.2533 22.2473 12.1006 21.9441 12.0355 21.6171L11.1783 17.3417L6.65869 12.822L4.34847 12.3589L2.38351 11.965C2.05664 11.8998 1.75272 11.747 1.50564 11.5232C1.25835 11.2992 1.07653 11.0122 0.979561 10.6929C0.882595 10.3736 0.874125 10.034 0.955057 9.7103C1.03599 9.38659 1.20328 9.09092 1.43909 8.85483ZM6.8186 10.8724L2.94619 10.096L6.32006 6.73268H10.9583L6.8186 10.8724ZM15.2219 5.21703C17.681 2.75787 20.0783 2.75376 21.1124 2.8876C21.2462 3.92172 21.2421 6.31895 18.783 8.77812L12.0728 15.4883L8.51172 11.9272L15.2219 5.21703ZM13.9042 21.0538L13.1279 17.1811L17.2676 13.0414V17.68L13.9042 21.0538Z" fill-rule="evenodd"></path><path d="M9.31827 18.3446C9.45046 17.8529 9.17864 17.3369 8.68945 17.1724C8.56178 17.1294 8.43145 17.1145 8.30512 17.1243C8.10513 17.1398 7.91519 17.2172 7.76181 17.3434C7.62613 17.455 7.51905 17.6048 7.45893 17.7835C6.97634 19.2186 5.77062 19.9878 4.52406 20.4029C4.08525 20.549 3.6605 20.644 3.29471 20.7053C3.35607 20.3395 3.45098 19.9148 3.59711 19.476C4.01221 18.2294 4.78141 17.0237 6.21648 16.5411C6.39528 16.481 6.54504 16.3739 6.65665 16.2382C6.85126 16.0016 6.92988 15.678 6.84417 15.3647C6.83922 15.3466 6.83373 15.3286 6.82767 15.3106C6.74106 15.053 6.55701 14.8557 6.33037 14.7459C6.10949 14.6389 5.84816 14.615 5.59715 14.6994C5.47743 14.7397 5.36103 14.7831 5.24786 14.8294C3.22626 15.6569 2.2347 17.4173 1.75357 18.8621C1.49662 19.6337 1.36993 20.3554 1.30679 20.8818C1.27505 21.1464 1.25893 21.3654 1.25072 21.5213C1.24662 21.5993 1.24448 21.6618 1.24337 21.7066L1.243 21.7226L1.24235 21.7605L1.2422 21.7771L1.24217 21.7827L1.24217 21.7856C1.24217 22.3221 1.67703 22.7579 2.2137 22.7579L2.2155 22.7579L2.22337 22.7578L2.23956 22.7577C2.25293 22.7575 2.27096 22.7572 2.29338 22.7567C2.33821 22.7555 2.40073 22.7534 2.47876 22.7493C2.63466 22.7411 2.85361 22.725 3.11822 22.6932C3.64462 22.6301 4.36636 22.5034 5.13797 22.2464C6.58274 21.7653 8.3431 20.7738 9.17063 18.7522C9.21696 18.639 9.26037 18.5226 9.30064 18.4029C9.30716 18.3835 9.31304 18.364 9.31827 18.3446Z"></path></svg>提示</p><div class="starlight-aside__content"><p>你可以多次运行 <code dir="auto">/undo</code> 来撤销多次修改。</p></div></aside>


你也**可以使用** `/redo` 命令来重做修改。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/redo</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/redo" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
## 分享
你与 OpenCode 的对话可以[与团队分享](/docs/share)。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">/share</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/share" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


这会生成当前对话的链接并复制到剪贴板。


<aside aria-label="注意" class="starlight-aside starlight-aside--note"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M12 11C11.7348 11 11.4804 11.1054 11.2929 11.2929C11.1054 11.4804 11 11.7348 11 12V16C11 16.2652 11.1054 16.5196 11.2929 16.7071C11.4804 16.8946 11.7348 17 12 17C12.2652 17 12.5196 16.8946 12.7071 16.7071C12.8946 16.5196 13 16.2652 13 16V12C13 11.7348 12.8946 11.4804 12.7071 11.2929C12.5196 11.1054 12.2652 11 12 11ZM12.38 7.08C12.1365 6.97998 11.8635 6.97998 11.62 7.08C11.4973 7.12759 11.3851 7.19896 11.29 7.29C11.2017 7.3872 11.1306 7.49882 11.08 7.62C11.024 7.73868 10.9966 7.86882 11 8C10.9992 8.13161 11.0245 8.26207 11.0742 8.38391C11.124 8.50574 11.1973 8.61656 11.29 8.71C11.3872 8.79833 11.4988 8.86936 11.62 8.92C11.7715 8.98224 11.936 9.00632 12.099 8.99011C12.2619 8.97391 12.4184 8.91792 12.5547 8.82707C12.691 8.73622 12.8029 8.61328 12.8805 8.46907C12.9582 8.32486 12.9992 8.16378 13 8C12.9963 7.73523 12.8927 7.48163 12.71 7.29C12.6149 7.19896 12.5028 7.12759 12.38 7.08ZM12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM12 20C10.4178 20 8.87104 19.5308 7.55544 18.6518C6.23985 17.7727 5.21447 16.5233 4.60897 15.0615C4.00347 13.5997 3.84504 11.9911 4.15372 10.4393C4.4624 8.88743 5.22433 7.46197 6.34315 6.34315C7.46197 5.22433 8.88743 4.4624 10.4393 4.15372C11.9911 3.84504 13.5997 4.00346 15.0615 4.60896C16.5233 5.21447 17.7727 6.23984 18.6518 7.55544C19.5308 8.87103 20 10.4177 20 12C20 14.1217 19.1572 16.1566 17.6569 17.6569C16.1566 19.1571 14.1217 20 12 20Z"></path></svg>注意</p><div class="starlight-aside__content"><p>对话默认不会被分享。</p></div></aside>


这是一个与 OpenCode 的[示例对话](https://opencode.ai/s/4XP1fce5)。
* * *
## 个性化
以上就是全部内容！你现在已经是 OpenCode 的使用高手了。
要让它更符合你的习惯，我们推荐[选择一个主题](/docs/themes)、[自定义快捷键](/docs/keybinds)、[配置代码格式化工具](/docs/formatters)、[创建自定义命令](/docs/commands)，或者探索 [OpenCode 配置](/docs/config)。