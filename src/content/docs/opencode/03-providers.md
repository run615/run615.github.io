---
title: '提供商'
description: '在 OpenCode 中使用任意 LLM 提供商。'
category: 'OpenCode 开发手册'
order: 3
slug: 'opencode/providers'
---

OpenCode 使用 [AI SDK](https://ai-sdk.dev/) 和 [Models.dev](https://models.dev)，支持 **75+ LLM 提供商** ，同时也支持运行本地模型。
要添加提供商，你需要：
  1. 使用 `/connect` 命令添加提供商的 API 密钥。
  2. 在 OpenCode 配置中设置该提供商。


* * *
### 凭据
使用 `/connect` 命令添加提供商的 API 密钥后，凭据会存储在 `~/.local/share/opencode/auth.json` 中。
* * *
### 配置
你可以通过 OpenCode 配置中的 `provider` 部分来自定义提供商。
* * *
#### 自定义 Base URL
你可以通过设置 `baseURL` 选项来自定义任何提供商的 Base URL。这在使用代理服务或自定义端点时非常有用。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"provider"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"anthropic"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"options"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">        </span><span style="--0:#004ba0;--1:#81bcff">"baseURL"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://api.anthropic.com/v1"</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "provider": {    "anthropic": {      "options": {        "baseURL": "https://api.anthropic.com/v1"      }    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
## OpenCode Zen
OpenCode Zen 是由 OpenCode 团队提供的模型列表，这些模型已经过测试和验证，能够与 OpenCode 良好配合使用。[了解更多](/docs/zen)。


<aside aria-label="提示" class="starlight-aside starlight-aside--tip"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path clip-rule="evenodd" d="M1.43909 8.85483L1.44039 8.85354L4.96668 5.33815C5.30653 4.99386 5.7685 4.79662 6.2524 4.78972L6.26553 4.78963L12.9014 4.78962L13.8479 3.84308C16.9187 0.772319 20.0546 0.770617 21.4678 0.975145C21.8617 1.02914 22.2271 1.21053 22.5083 1.4917C22.7894 1.77284 22.9708 2.13821 23.0248 2.53199C23.2294 3.94517 23.2278 7.08119 20.1569 10.1521L19.2107 11.0983V17.7338L19.2106 17.7469C19.2037 18.2308 19.0067 18.6933 18.6624 19.0331L15.1456 22.5608C14.9095 22.7966 14.6137 22.964 14.29 23.0449C13.9663 23.1259 13.6267 23.1174 13.3074 23.0204C12.9881 22.9235 12.7011 22.7417 12.4771 22.4944C12.2533 22.2473 12.1006 21.9441 12.0355 21.6171L11.1783 17.3417L6.65869 12.822L4.34847 12.3589L2.38351 11.965C2.05664 11.8998 1.75272 11.747 1.50564 11.5232C1.25835 11.2992 1.07653 11.0122 0.979561 10.6929C0.882595 10.3736 0.874125 10.034 0.955057 9.7103C1.03599 9.38659 1.20328 9.09092 1.43909 8.85483ZM6.8186 10.8724L2.94619 10.096L6.32006 6.73268H10.9583L6.8186 10.8724ZM15.2219 5.21703C17.681 2.75787 20.0783 2.75376 21.1124 2.8876C21.2462 3.92172 21.2421 6.31895 18.783 8.77812L12.0728 15.4883L8.51172 11.9272L15.2219 5.21703ZM13.9042 21.0538L13.1279 17.1811L17.2676 13.0414V17.68L13.9042 21.0538Z" fill-rule="evenodd"></path><path d="M9.31827 18.3446C9.45046 17.8529 9.17864 17.3369 8.68945 17.1724C8.56178 17.1294 8.43145 17.1145 8.30512 17.1243C8.10513 17.1398 7.91519 17.2172 7.76181 17.3434C7.62613 17.455 7.51905 17.6048 7.45893 17.7835C6.97634 19.2186 5.77062 19.9878 4.52406 20.4029C4.08525 20.549 3.6605 20.644 3.29471 20.7053C3.35607 20.3395 3.45098 19.9148 3.59711 19.476C4.01221 18.2294 4.78141 17.0237 6.21648 16.5411C6.39528 16.481 6.54504 16.3739 6.65665 16.2382C6.85126 16.0016 6.92988 15.678 6.84417 15.3647C6.83922 15.3466 6.83373 15.3286 6.82767 15.3106C6.74106 15.053 6.55701 14.8557 6.33037 14.7459C6.10949 14.6389 5.84816 14.615 5.59715 14.6994C5.47743 14.7397 5.36103 14.7831 5.24786 14.8294C3.22626 15.6569 2.2347 17.4173 1.75357 18.8621C1.49662 19.6337 1.36993 20.3554 1.30679 20.8818C1.27505 21.1464 1.25893 21.3654 1.25072 21.5213C1.24662 21.5993 1.24448 21.6618 1.24337 21.7066L1.243 21.7226L1.24235 21.7605L1.2422 21.7771L1.24217 21.7827L1.24217 21.7856C1.24217 22.3221 1.67703 22.7579 2.2137 22.7579L2.2155 22.7579L2.22337 22.7578L2.23956 22.7577C2.25293 22.7575 2.27096 22.7572 2.29338 22.7567C2.33821 22.7555 2.40073 22.7534 2.47876 22.7493C2.63466 22.7411 2.85361 22.725 3.11822 22.6932C3.64462 22.6301 4.36636 22.5034 5.13797 22.2464C6.58274 21.7653 8.3431 20.7738 9.17063 18.7522C9.21696 18.639 9.26037 18.5226 9.30064 18.4029C9.30716 18.3835 9.31304 18.364 9.31827 18.3446Z"></path></svg>提示</p><div class="starlight-aside__content"><p>如果你是新用户，我们建议从 OpenCode Zen 开始。</p></div></aside>


  1. 在 TUI 中执行 `/connect` 命令，选择 opencode，然后前往 [opencode.ai/auth](https://opencode.ai/auth)。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  2. 登录后添加账单信息，然后复制你的 API 密钥。
  3. 粘贴你的 API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 在 TUI 中执行 `/models` 查看我们推荐的模型列表。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


它的使用方式与 OpenCode 中的其他提供商完全相同，且完全可选。
* * *
## 目录
下面我们来详细了解一些提供商。如果你想将某个提供商添加到列表中，欢迎提交 PR。


<aside aria-label="注意" class="starlight-aside starlight-aside--note"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M12 11C11.7348 11 11.4804 11.1054 11.2929 11.2929C11.1054 11.4804 11 11.7348 11 12V16C11 16.2652 11.1054 16.5196 11.2929 16.7071C11.4804 16.8946 11.7348 17 12 17C12.2652 17 12.5196 16.8946 12.7071 16.7071C12.8946 16.5196 13 16.2652 13 16V12C13 11.7348 12.8946 11.4804 12.7071 11.2929C12.5196 11.1054 12.2652 11 12 11ZM12.38 7.08C12.1365 6.97998 11.8635 6.97998 11.62 7.08C11.4973 7.12759 11.3851 7.19896 11.29 7.29C11.2017 7.3872 11.1306 7.49882 11.08 7.62C11.024 7.73868 10.9966 7.86882 11 8C10.9992 8.13161 11.0245 8.26207 11.0742 8.38391C11.124 8.50574 11.1973 8.61656 11.29 8.71C11.3872 8.79833 11.4988 8.86936 11.62 8.92C11.7715 8.98224 11.936 9.00632 12.099 8.99011C12.2619 8.97391 12.4184 8.91792 12.5547 8.82707C12.691 8.73622 12.8029 8.61328 12.8805 8.46907C12.9582 8.32486 12.9992 8.16378 13 8C12.9963 7.73523 12.8927 7.48163 12.71 7.29C12.6149 7.19896 12.5028 7.12759 12.38 7.08ZM12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM12 20C10.4178 20 8.87104 19.5308 7.55544 18.6518C6.23985 17.7727 5.21447 16.5233 4.60897 15.0615C4.00347 13.5997 3.84504 11.9911 4.15372 10.4393C4.4624 8.88743 5.22433 7.46197 6.34315 6.34315C7.46197 5.22433 8.88743 4.4624 10.4393 4.15372C11.9911 3.84504 13.5997 4.00346 15.0615 4.60896C16.5233 5.21447 17.7727 6.23984 18.6518 7.55544C19.5308 8.87103 20 10.4177 20 12C20 14.1217 19.1572 16.1566 17.6569 17.6569C16.1566 19.1571 14.1217 20 12 20Z"></path></svg>注意</p><div class="starlight-aside__content"><p>没有看到你想要的提供商？欢迎提交 PR。</p></div></aside>


* * *
### 302.AI
  1. 前往 [302.AI 控制台](https://302.ai/)，创建账户并生成 API 密钥。
  2. 执行 `/connect` 命令并搜索 **302.AI** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入你的 302.AI API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择模型。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### Amazon Bedrock
要在 OpenCode 中使用 Amazon Bedrock：
  1. 前往 Amazon Bedrock 控制台中的**模型目录** ，申请访问你想要使用的模型。


<aside aria-label="提示" class="starlight-aside starlight-aside--tip"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path clip-rule="evenodd" d="M1.43909 8.85483L1.44039 8.85354L4.96668 5.33815C5.30653 4.99386 5.7685 4.79662 6.2524 4.78972L6.26553 4.78963L12.9014 4.78962L13.8479 3.84308C16.9187 0.772319 20.0546 0.770617 21.4678 0.975145C21.8617 1.02914 22.2271 1.21053 22.5083 1.4917C22.7894 1.77284 22.9708 2.13821 23.0248 2.53199C23.2294 3.94517 23.2278 7.08119 20.1569 10.1521L19.2107 11.0983V17.7338L19.2106 17.7469C19.2037 18.2308 19.0067 18.6933 18.6624 19.0331L15.1456 22.5608C14.9095 22.7966 14.6137 22.964 14.29 23.0449C13.9663 23.1259 13.6267 23.1174 13.3074 23.0204C12.9881 22.9235 12.7011 22.7417 12.4771 22.4944C12.2533 22.2473 12.1006 21.9441 12.0355 21.6171L11.1783 17.3417L6.65869 12.822L4.34847 12.3589L2.38351 11.965C2.05664 11.8998 1.75272 11.747 1.50564 11.5232C1.25835 11.2992 1.07653 11.0122 0.979561 10.6929C0.882595 10.3736 0.874125 10.034 0.955057 9.7103C1.03599 9.38659 1.20328 9.09092 1.43909 8.85483ZM6.8186 10.8724L2.94619 10.096L6.32006 6.73268H10.9583L6.8186 10.8724ZM15.2219 5.21703C17.681 2.75787 20.0783 2.75376 21.1124 2.8876C21.2462 3.92172 21.2421 6.31895 18.783 8.77812L12.0728 15.4883L8.51172 11.9272L15.2219 5.21703ZM13.9042 21.0538L13.1279 17.1811L17.2676 13.0414V17.68L13.9042 21.0538Z" fill-rule="evenodd"></path><path d="M9.31827 18.3446C9.45046 17.8529 9.17864 17.3369 8.68945 17.1724C8.56178 17.1294 8.43145 17.1145 8.30512 17.1243C8.10513 17.1398 7.91519 17.2172 7.76181 17.3434C7.62613 17.455 7.51905 17.6048 7.45893 17.7835C6.97634 19.2186 5.77062 19.9878 4.52406 20.4029C4.08525 20.549 3.6605 20.644 3.29471 20.7053C3.35607 20.3395 3.45098 19.9148 3.59711 19.476C4.01221 18.2294 4.78141 17.0237 6.21648 16.5411C6.39528 16.481 6.54504 16.3739 6.65665 16.2382C6.85126 16.0016 6.92988 15.678 6.84417 15.3647C6.83922 15.3466 6.83373 15.3286 6.82767 15.3106C6.74106 15.053 6.55701 14.8557 6.33037 14.7459C6.10949 14.6389 5.84816 14.615 5.59715 14.6994C5.47743 14.7397 5.36103 14.7831 5.24786 14.8294C3.22626 15.6569 2.2347 17.4173 1.75357 18.8621C1.49662 19.6337 1.36993 20.3554 1.30679 20.8818C1.27505 21.1464 1.25893 21.3654 1.25072 21.5213C1.24662 21.5993 1.24448 21.6618 1.24337 21.7066L1.243 21.7226L1.24235 21.7605L1.2422 21.7771L1.24217 21.7827L1.24217 21.7856C1.24217 22.3221 1.67703 22.7579 2.2137 22.7579L2.2155 22.7579L2.22337 22.7578L2.23956 22.7577C2.25293 22.7575 2.27096 22.7572 2.29338 22.7567C2.33821 22.7555 2.40073 22.7534 2.47876 22.7493C2.63466 22.7411 2.85361 22.725 3.11822 22.6932C3.64462 22.6301 4.36636 22.5034 5.13797 22.2464C6.58274 21.7653 8.3431 20.7738 9.17063 18.7522C9.21696 18.639 9.26037 18.5226 9.30064 18.4029C9.30716 18.3835 9.31304 18.364 9.31827 18.3446Z"></path></svg>提示</p><div class="starlight-aside__content"><p>你需要先在 Amazon Bedrock 中获得对目标模型的访问权限。</p></div></aside>


  2. 使用以下方法之一**配置身份验证** ：
* * *
#### 环境变量（快速上手）
运行 opencode 时设置以下环境变量之一：


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#616972;--1:#99A0A6"># Option 1: Using AWS access keys</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">AWS_ACCESS_KEY_ID</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#032F62;--1:#9ECBFF">XXX</span><span style="--0:#24292E;--1:#E1E4E8"> AWS_SECRET_ACCESS_KEY</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#032F62;--1:#9ECBFF">YYY</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#6F42C1;--1:#B392F0">opencode</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#616972;--1:#99A0A6"># Option 2: Using named AWS profile</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">AWS_PROFILE</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#032F62;--1:#9ECBFF">my-profile</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#6F42C1;--1:#B392F0">opencode</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#616972;--1:#99A0A6"># Option 3: Using Bedrock bearer token</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">AWS_BEARER_TOKEN_BEDROCK</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#032F62;--1:#9ECBFF">XXX</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#6F42C1;--1:#B392F0">opencode</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="AWS_ACCESS_KEY_ID=XXX AWS_SECRET_ACCESS_KEY=YYY opencodeAWS_PROFILE=my-profile opencodeAWS_BEARER_TOKEN_BEDROCK=XXX opencode" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


或者将它们添加到你的 bash 配置文件中：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">~/.bash_profile</span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#BF3441;--1:#F97583">export</span><span style="--0:#24292E;--1:#E1E4E8"> AWS_PROFILE</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#24292E;--1:#E1E4E8">my-dev-profile</span></div></div><div class="ec-line"><div class="code"><span style="--0:#BF3441;--1:#F97583">export</span><span style="--0:#24292E;--1:#E1E4E8"> AWS_REGION</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#24292E;--1:#E1E4E8">us-east-1</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="export AWS_PROFILE=my-dev-profileexport AWS_REGION=us-east-1" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
#### 配置文件（推荐）
如需项目级别或持久化的配置，请使用 `opencode.json`：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"provider"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"amazon-bedrock"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"options"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#005CC5;--1:#79B8FF">"region"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"us-east-1"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#005CC5;--1:#79B8FF">"profile"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"my-aws-profile"</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "provider": {    "amazon-bedrock": {      "options": {        "region": "us-east-1",        "profile": "my-aws-profile"      }    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


**可用选项：**
     * `region` \- AWS 区域（例如 `us-east-1`、`eu-west-1`）
     * `profile` \- `~/.aws/credentials` 中的 AWS 命名配置文件
     * `endpoint` \- VPC 端点的自定义端点 URL（通用 `baseURL` 选项的别名）


<aside aria-label="提示" class="starlight-aside starlight-aside--tip"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path clip-rule="evenodd" d="M1.43909 8.85483L1.44039 8.85354L4.96668 5.33815C5.30653 4.99386 5.7685 4.79662 6.2524 4.78972L6.26553 4.78963L12.9014 4.78962L13.8479 3.84308C16.9187 0.772319 20.0546 0.770617 21.4678 0.975145C21.8617 1.02914 22.2271 1.21053 22.5083 1.4917C22.7894 1.77284 22.9708 2.13821 23.0248 2.53199C23.2294 3.94517 23.2278 7.08119 20.1569 10.1521L19.2107 11.0983V17.7338L19.2106 17.7469C19.2037 18.2308 19.0067 18.6933 18.6624 19.0331L15.1456 22.5608C14.9095 22.7966 14.6137 22.964 14.29 23.0449C13.9663 23.1259 13.6267 23.1174 13.3074 23.0204C12.9881 22.9235 12.7011 22.7417 12.4771 22.4944C12.2533 22.2473 12.1006 21.9441 12.0355 21.6171L11.1783 17.3417L6.65869 12.822L4.34847 12.3589L2.38351 11.965C2.05664 11.8998 1.75272 11.747 1.50564 11.5232C1.25835 11.2992 1.07653 11.0122 0.979561 10.6929C0.882595 10.3736 0.874125 10.034 0.955057 9.7103C1.03599 9.38659 1.20328 9.09092 1.43909 8.85483ZM6.8186 10.8724L2.94619 10.096L6.32006 6.73268H10.9583L6.8186 10.8724ZM15.2219 5.21703C17.681 2.75787 20.0783 2.75376 21.1124 2.8876C21.2462 3.92172 21.2421 6.31895 18.783 8.77812L12.0728 15.4883L8.51172 11.9272L15.2219 5.21703ZM13.9042 21.0538L13.1279 17.1811L17.2676 13.0414V17.68L13.9042 21.0538Z" fill-rule="evenodd"></path><path d="M9.31827 18.3446C9.45046 17.8529 9.17864 17.3369 8.68945 17.1724C8.56178 17.1294 8.43145 17.1145 8.30512 17.1243C8.10513 17.1398 7.91519 17.2172 7.76181 17.3434C7.62613 17.455 7.51905 17.6048 7.45893 17.7835C6.97634 19.2186 5.77062 19.9878 4.52406 20.4029C4.08525 20.549 3.6605 20.644 3.29471 20.7053C3.35607 20.3395 3.45098 19.9148 3.59711 19.476C4.01221 18.2294 4.78141 17.0237 6.21648 16.5411C6.39528 16.481 6.54504 16.3739 6.65665 16.2382C6.85126 16.0016 6.92988 15.678 6.84417 15.3647C6.83922 15.3466 6.83373 15.3286 6.82767 15.3106C6.74106 15.053 6.55701 14.8557 6.33037 14.7459C6.10949 14.6389 5.84816 14.615 5.59715 14.6994C5.47743 14.7397 5.36103 14.7831 5.24786 14.8294C3.22626 15.6569 2.2347 17.4173 1.75357 18.8621C1.49662 19.6337 1.36993 20.3554 1.30679 20.8818C1.27505 21.1464 1.25893 21.3654 1.25072 21.5213C1.24662 21.5993 1.24448 21.6618 1.24337 21.7066L1.243 21.7226L1.24235 21.7605L1.2422 21.7771L1.24217 21.7827L1.24217 21.7856C1.24217 22.3221 1.67703 22.7579 2.2137 22.7579L2.2155 22.7579L2.22337 22.7578L2.23956 22.7577C2.25293 22.7575 2.27096 22.7572 2.29338 22.7567C2.33821 22.7555 2.40073 22.7534 2.47876 22.7493C2.63466 22.7411 2.85361 22.725 3.11822 22.6932C3.64462 22.6301 4.36636 22.5034 5.13797 22.2464C6.58274 21.7653 8.3431 20.7738 9.17063 18.7522C9.21696 18.639 9.26037 18.5226 9.30064 18.4029C9.30716 18.3835 9.31304 18.364 9.31827 18.3446Z"></path></svg>提示</p><div class="starlight-aside__content"><p>配置文件中的选项优先级高于环境变量。</p></div></aside>


* * *
#### 进阶：VPC 端点
如果你使用 Bedrock 的 VPC 端点：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"provider"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"amazon-bedrock"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"options"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#005CC5;--1:#79B8FF">"region"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"us-east-1"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#005CC5;--1:#79B8FF">"profile"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"production"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#005CC5;--1:#79B8FF">"endpoint"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://bedrock-runtime.us-east-1.vpce-xxxxx.amazonaws.com"</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "provider": {    "amazon-bedrock": {      "options": {        "region": "us-east-1",        "profile": "production",        "endpoint": "https://bedrock-runtime.us-east-1.vpce-xxxxx.amazonaws.com"      }    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>

 

<aside aria-label="注意" class="starlight-aside starlight-aside--note"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M12 11C11.7348 11 11.4804 11.1054 11.2929 11.2929C11.1054 11.4804 11 11.7348 11 12V16C11 16.2652 11.1054 16.5196 11.2929 16.7071C11.4804 16.8946 11.7348 17 12 17C12.2652 17 12.5196 16.8946 12.7071 16.7071C12.8946 16.5196 13 16.2652 13 16V12C13 11.7348 12.8946 11.4804 12.7071 11.2929C12.5196 11.1054 12.2652 11 12 11ZM12.38 7.08C12.1365 6.97998 11.8635 6.97998 11.62 7.08C11.4973 7.12759 11.3851 7.19896 11.29 7.29C11.2017 7.3872 11.1306 7.49882 11.08 7.62C11.024 7.73868 10.9966 7.86882 11 8C10.9992 8.13161 11.0245 8.26207 11.0742 8.38391C11.124 8.50574 11.1973 8.61656 11.29 8.71C11.3872 8.79833 11.4988 8.86936 11.62 8.92C11.7715 8.98224 11.936 9.00632 12.099 8.99011C12.2619 8.97391 12.4184 8.91792 12.5547 8.82707C12.691 8.73622 12.8029 8.61328 12.8805 8.46907C12.9582 8.32486 12.9992 8.16378 13 8C12.9963 7.73523 12.8927 7.48163 12.71 7.29C12.6149 7.19896 12.5028 7.12759 12.38 7.08ZM12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM12 20C10.4178 20 8.87104 19.5308 7.55544 18.6518C6.23985 17.7727 5.21447 16.5233 4.60897 15.0615C4.00347 13.5997 3.84504 11.9911 4.15372 10.4393C4.4624 8.88743 5.22433 7.46197 6.34315 6.34315C7.46197 5.22433 8.88743 4.4624 10.4393 4.15372C11.9911 3.84504 13.5997 4.00346 15.0615 4.60896C16.5233 5.21447 17.7727 6.23984 18.6518 7.55544C19.5308 8.87103 20 10.4177 20 12C20 14.1217 19.1572 16.1566 17.6569 17.6569C16.1566 19.1571 14.1217 20 12 20Z"></path></svg>注意</p><div class="starlight-aside__content"><p><code dir="auto">endpoint</code> 选项是通用 <code dir="auto">baseURL</code> 选项的别名，使用了 AWS 特有的术语。如果同时指定了 <code dir="auto">endpoint</code> 和 <code dir="auto">baseURL</code>，则 <code dir="auto">endpoint</code> 优先。</p></div></aside>


* * *
#### 认证方式
     * **`AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY`**：在 AWS 控制台中创建 IAM 用户并生成访问密钥
     * **`AWS_PROFILE`** ：使用 `~/.aws/credentials` 中的命名配置文件。需要先通过 `aws configure --profile my-profile` 或 `aws sso login` 进行配置
     * **`AWS_BEARER_TOKEN_BEDROCK`** ：从 Amazon Bedrock 控制台生成长期 API 密钥
     * **`AWS_WEB_IDENTITY_TOKEN_FILE` / `AWS_ROLE_ARN`**：适用于 EKS IRSA（服务账户的 IAM 角色）或其他支持 OIDC 联合的 Kubernetes 环境。使用服务账户注解时，Kubernetes 会自动注入这些环境变量。
* * *
#### 认证优先级
Amazon Bedrock 使用以下认证优先级：
     1. **Bearer Token** \- `AWS_BEARER_TOKEN_BEDROCK` 环境变量或通过 `/connect` 命令获取的 Token
     2. **AWS 凭证链** \- 配置文件、访问密钥、共享凭证、IAM 角色、Web Identity Token（EKS IRSA）、实例元数据


<aside aria-label="注意" class="starlight-aside starlight-aside--note"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M12 11C11.7348 11 11.4804 11.1054 11.2929 11.2929C11.1054 11.4804 11 11.7348 11 12V16C11 16.2652 11.1054 16.5196 11.2929 16.7071C11.4804 16.8946 11.7348 17 12 17C12.2652 17 12.5196 16.8946 12.7071 16.7071C12.8946 16.5196 13 16.2652 13 16V12C13 11.7348 12.8946 11.4804 12.7071 11.2929C12.5196 11.1054 12.2652 11 12 11ZM12.38 7.08C12.1365 6.97998 11.8635 6.97998 11.62 7.08C11.4973 7.12759 11.3851 7.19896 11.29 7.29C11.2017 7.3872 11.1306 7.49882 11.08 7.62C11.024 7.73868 10.9966 7.86882 11 8C10.9992 8.13161 11.0245 8.26207 11.0742 8.38391C11.124 8.50574 11.1973 8.61656 11.29 8.71C11.3872 8.79833 11.4988 8.86936 11.62 8.92C11.7715 8.98224 11.936 9.00632 12.099 8.99011C12.2619 8.97391 12.4184 8.91792 12.5547 8.82707C12.691 8.73622 12.8029 8.61328 12.8805 8.46907C12.9582 8.32486 12.9992 8.16378 13 8C12.9963 7.73523 12.8927 7.48163 12.71 7.29C12.6149 7.19896 12.5028 7.12759 12.38 7.08ZM12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM12 20C10.4178 20 8.87104 19.5308 7.55544 18.6518C6.23985 17.7727 5.21447 16.5233 4.60897 15.0615C4.00347 13.5997 3.84504 11.9911 4.15372 10.4393C4.4624 8.88743 5.22433 7.46197 6.34315 6.34315C7.46197 5.22433 8.88743 4.4624 10.4393 4.15372C11.9911 3.84504 13.5997 4.00346 15.0615 4.60896C16.5233 5.21447 17.7727 6.23984 18.6518 7.55544C19.5308 8.87103 20 10.4177 20 12C20 14.1217 19.1572 16.1566 17.6569 17.6569C16.1566 19.1571 14.1217 20 12 20Z"></path></svg>注意</p><div class="starlight-aside__content"><p>当设置了 Bearer Token（通过 <code dir="auto">/connect</code> 或 <code dir="auto">AWS_BEARER_TOKEN_BEDROCK</code>）时，它的优先级高于所有 AWS 凭证方式，包括已配置的配置文件。</p></div></aside>


  3. 执行 `/models` 命令选择你想要的模型。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


<aside aria-label="注意" class="starlight-aside starlight-aside--note"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M12 11C11.7348 11 11.4804 11.1054 11.2929 11.2929C11.1054 11.4804 11 11.7348 11 12V16C11 16.2652 11.1054 16.5196 11.2929 16.7071C11.4804 16.8946 11.7348 17 12 17C12.2652 17 12.5196 16.8946 12.7071 16.7071C12.8946 16.5196 13 16.2652 13 16V12C13 11.7348 12.8946 11.4804 12.7071 11.2929C12.5196 11.1054 12.2652 11 12 11ZM12.38 7.08C12.1365 6.97998 11.8635 6.97998 11.62 7.08C11.4973 7.12759 11.3851 7.19896 11.29 7.29C11.2017 7.3872 11.1306 7.49882 11.08 7.62C11.024 7.73868 10.9966 7.86882 11 8C10.9992 8.13161 11.0245 8.26207 11.0742 8.38391C11.124 8.50574 11.1973 8.61656 11.29 8.71C11.3872 8.79833 11.4988 8.86936 11.62 8.92C11.7715 8.98224 11.936 9.00632 12.099 8.99011C12.2619 8.97391 12.4184 8.91792 12.5547 8.82707C12.691 8.73622 12.8029 8.61328 12.8805 8.46907C12.9582 8.32486 12.9992 8.16378 13 8C12.9963 7.73523 12.8927 7.48163 12.71 7.29C12.6149 7.19896 12.5028 7.12759 12.38 7.08ZM12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM12 20C10.4178 20 8.87104 19.5308 7.55544 18.6518C6.23985 17.7727 5.21447 16.5233 4.60897 15.0615C4.00347 13.5997 3.84504 11.9911 4.15372 10.4393C4.4624 8.88743 5.22433 7.46197 6.34315 6.34315C7.46197 5.22433 8.88743 4.4624 10.4393 4.15372C11.9911 3.84504 13.5997 4.00346 15.0615 4.60896C16.5233 5.21447 17.7727 6.23984 18.6518 7.55544C19.5308 8.87103 20 10.4177 20 12C20 14.1217 19.1572 16.1566 17.6569 17.6569C16.1566 19.1571 14.1217 20 12 20Z"></path></svg>注意</p><div class="starlight-aside__content"><p>对于自定义推理配置文件，请在 key 中使用模型名称和提供商名称，并将 <code dir="auto">id</code> 属性设置为 ARN。这可以确保正确的缓存行为：</p><div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"provider"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"amazon-bedrock"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#616972;--1:#99A0A6">// ...</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"models"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#005CC5;--1:#79B8FF">"anthropic-claude-sonnet-4.5"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">          </span><span style="--0:#005CC5;--1:#79B8FF">"id"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"arn:aws:bedrock:us-east-1:xxx:application-inference-profile/yyy"</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">        </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "provider": {    "amazon-bedrock": {      // ...      "models": {        "anthropic-claude-sonnet-4.5": {          "id": "arn:aws:bedrock:us-east-1:xxx:application-inference-profile/yyy"        }      }    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div></div></aside>


* * *
### Anthropic
  1. 注册完成后，执行 `/connect` 命令并选择 Anthropic。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  2. 你可以选择 **Claude Pro/Max** 选项，浏览器会自动打开并要求你进行身份验证。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ Select auth method</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│ Claude Pro/Max</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│ Create an API Key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│ Manually enter API Key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ Select auth method││ Claude Pro/Max│ Create an API Key│ Manually enter API Key└" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 现在使用 `/models` 命令即可看到所有 Anthropic 模型。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


在 OpenCode 中使用 Claude Pro/Max 订阅不是 [Anthropic](https://anthropic.com) 官方支持的用法。
##### 使用 API 密钥
如果你没有 Pro/Max 订阅，也可以选择 **Create an API Key** 。浏览器会自动打开并要求你登录 Anthropic，然后会提供一个代码供你粘贴到终端中。
如果你已经有 API 密钥，可以选择 **Manually enter API Key** 并将其粘贴到终端中。
* * *
### Atomic Chat
你可以通过 [Atomic Chat](https://atomic.chat) 配置 opencode 以使用本地模型。Atomic Chat 是一款桌面应用程序，它在 OpenAI 兼容的 API 服务器后面运行本地 LLM（默认端点 `http://127.0.0.1:1337/v1`）。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"provider"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"</span><mark><span style="--0:#004ba0;--1:#81bcff">atomic-chat</span></mark><span style="--0:#005CC5;--1:#79B8FF">"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"npm"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"@ai-sdk/openai-compatible"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"name"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"Atomic Chat (local)"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"options"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">        </span><span style="--0:#004ba0;--1:#81bcff">"baseURL"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"http://127.0.0.1:1337/v1"</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">},</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"models"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">        </span><span style="--0:#004ba0;--1:#81bcff">"&lt;your-model-id&gt;"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">          </span><span style="--0:#004ba0;--1:#81bcff">"name"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"&lt;your-model-name&gt;"</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">        </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "provider": {    "atomic-chat": {      "npm": "@ai-sdk/openai-compatible",      "name": "Atomic Chat (local)",      "options": {        "baseURL": "http://127.0.0.1:1337/v1"      },      "models": {        "&lt;your-model-id&gt;": {          "name": "&lt;your-model-name&gt;"        }      }    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


在此示例中：
  * `atomic-chat` 是自定义的提供商 ID。可以是任何你想要的字符串。
  * `npm` 指定此提供商使用的包。这里使用 `@ai-sdk/openai-compatible` 来连接任何 OpenAI 兼容的 API。
  * `name` 是提供商在界面中显示的名称。
  * `options.baseURL` 是本地服务器的端点。根据你的 Atomic Chat 设置修改主机和端口。
  * `models` 是模型 ID 到其显示名称的映射。每个 ID 必须与 `GET /v1/models` 返回的 `id` 匹配——运行 `curl http://127.0.0.1:1337/v1/models` 可列出 Atomic Chat 当前已加载的 ID。


<aside aria-label="提示" class="starlight-aside starlight-aside--tip"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path clip-rule="evenodd" d="M1.43909 8.85483L1.44039 8.85354L4.96668 5.33815C5.30653 4.99386 5.7685 4.79662 6.2524 4.78972L6.26553 4.78963L12.9014 4.78962L13.8479 3.84308C16.9187 0.772319 20.0546 0.770617 21.4678 0.975145C21.8617 1.02914 22.2271 1.21053 22.5083 1.4917C22.7894 1.77284 22.9708 2.13821 23.0248 2.53199C23.2294 3.94517 23.2278 7.08119 20.1569 10.1521L19.2107 11.0983V17.7338L19.2106 17.7469C19.2037 18.2308 19.0067 18.6933 18.6624 19.0331L15.1456 22.5608C14.9095 22.7966 14.6137 22.964 14.29 23.0449C13.9663 23.1259 13.6267 23.1174 13.3074 23.0204C12.9881 22.9235 12.7011 22.7417 12.4771 22.4944C12.2533 22.2473 12.1006 21.9441 12.0355 21.6171L11.1783 17.3417L6.65869 12.822L4.34847 12.3589L2.38351 11.965C2.05664 11.8998 1.75272 11.747 1.50564 11.5232C1.25835 11.2992 1.07653 11.0122 0.979561 10.6929C0.882595 10.3736 0.874125 10.034 0.955057 9.7103C1.03599 9.38659 1.20328 9.09092 1.43909 8.85483ZM6.8186 10.8724L2.94619 10.096L6.32006 6.73268H10.9583L6.8186 10.8724ZM15.2219 5.21703C17.681 2.75787 20.0783 2.75376 21.1124 2.8876C21.2462 3.92172 21.2421 6.31895 18.783 8.77812L12.0728 15.4883L8.51172 11.9272L15.2219 5.21703ZM13.9042 21.0538L13.1279 17.1811L17.2676 13.0414V17.68L13.9042 21.0538Z" fill-rule="evenodd"></path><path d="M9.31827 18.3446C9.45046 17.8529 9.17864 17.3369 8.68945 17.1724C8.56178 17.1294 8.43145 17.1145 8.30512 17.1243C8.10513 17.1398 7.91519 17.2172 7.76181 17.3434C7.62613 17.455 7.51905 17.6048 7.45893 17.7835C6.97634 19.2186 5.77062 19.9878 4.52406 20.4029C4.08525 20.549 3.6605 20.644 3.29471 20.7053C3.35607 20.3395 3.45098 19.9148 3.59711 19.476C4.01221 18.2294 4.78141 17.0237 6.21648 16.5411C6.39528 16.481 6.54504 16.3739 6.65665 16.2382C6.85126 16.0016 6.92988 15.678 6.84417 15.3647C6.83922 15.3466 6.83373 15.3286 6.82767 15.3106C6.74106 15.053 6.55701 14.8557 6.33037 14.7459C6.10949 14.6389 5.84816 14.615 5.59715 14.6994C5.47743 14.7397 5.36103 14.7831 5.24786 14.8294C3.22626 15.6569 2.2347 17.4173 1.75357 18.8621C1.49662 19.6337 1.36993 20.3554 1.30679 20.8818C1.27505 21.1464 1.25893 21.3654 1.25072 21.5213C1.24662 21.5993 1.24448 21.6618 1.24337 21.7066L1.243 21.7226L1.24235 21.7605L1.2422 21.7771L1.24217 21.7827L1.24217 21.7856C1.24217 22.3221 1.67703 22.7579 2.2137 22.7579L2.2155 22.7579L2.22337 22.7578L2.23956 22.7577C2.25293 22.7575 2.27096 22.7572 2.29338 22.7567C2.33821 22.7555 2.40073 22.7534 2.47876 22.7493C2.63466 22.7411 2.85361 22.725 3.11822 22.6932C3.64462 22.6301 4.36636 22.5034 5.13797 22.2464C6.58274 21.7653 8.3431 20.7738 9.17063 18.7522C9.21696 18.639 9.26037 18.5226 9.30064 18.4029C9.30716 18.3835 9.31304 18.364 9.31827 18.3446Z"></path></svg>提示</p><div class="starlight-aside__content"><p>如果工具调用工作不佳，请选择一个对 tool calling 支持较好的已加载模型（例如 Qwen-Coder 或 DeepSeek-Coder 的变体）。</p></div></aside>


* * *
### Azure OpenAI


<aside aria-label="注意" class="starlight-aside starlight-aside--note"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M12 11C11.7348 11 11.4804 11.1054 11.2929 11.2929C11.1054 11.4804 11 11.7348 11 12V16C11 16.2652 11.1054 16.5196 11.2929 16.7071C11.4804 16.8946 11.7348 17 12 17C12.2652 17 12.5196 16.8946 12.7071 16.7071C12.8946 16.5196 13 16.2652 13 16V12C13 11.7348 12.8946 11.4804 12.7071 11.2929C12.5196 11.1054 12.2652 11 12 11ZM12.38 7.08C12.1365 6.97998 11.8635 6.97998 11.62 7.08C11.4973 7.12759 11.3851 7.19896 11.29 7.29C11.2017 7.3872 11.1306 7.49882 11.08 7.62C11.024 7.73868 10.9966 7.86882 11 8C10.9992 8.13161 11.0245 8.26207 11.0742 8.38391C11.124 8.50574 11.1973 8.61656 11.29 8.71C11.3872 8.79833 11.4988 8.86936 11.62 8.92C11.7715 8.98224 11.936 9.00632 12.099 8.99011C12.2619 8.97391 12.4184 8.91792 12.5547 8.82707C12.691 8.73622 12.8029 8.61328 12.8805 8.46907C12.9582 8.32486 12.9992 8.16378 13 8C12.9963 7.73523 12.8927 7.48163 12.71 7.29C12.6149 7.19896 12.5028 7.12759 12.38 7.08ZM12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM12 20C10.4178 20 8.87104 19.5308 7.55544 18.6518C6.23985 17.7727 5.21447 16.5233 4.60897 15.0615C4.00347 13.5997 3.84504 11.9911 4.15372 10.4393C4.4624 8.88743 5.22433 7.46197 6.34315 6.34315C7.46197 5.22433 8.88743 4.4624 10.4393 4.15372C11.9911 3.84504 13.5997 4.00346 15.0615 4.60896C16.5233 5.21447 17.7727 6.23984 18.6518 7.55544C19.5308 8.87103 20 10.4177 20 12C20 14.1217 19.1572 16.1566 17.6569 17.6569C16.1566 19.1571 14.1217 20 12 20Z"></path></svg>注意</p><div class="starlight-aside__content"><p>如果遇到 “I’m sorry, but I cannot assist with that request” 错误，请尝试将 Azure 资源中的内容过滤器从 <strong>DefaultV2</strong> 更改为 <strong>Default</strong>。</p></div></aside>


  1. 前往 [Azure 门户](https://portal.azure.com/)并创建 **Azure OpenAI** 资源。你需要：
     * **资源名称** ：这会成为你的 API 端点的一部分（`https://RESOURCE_NAME.openai.azure.com/`）
     * **API 密钥** ：资源中的 `KEY 1` 或 `KEY 2`
  2. 前往 [Azure AI Foundry](https://ai.azure.com/) 并部署一个模型。


<aside aria-label="注意" class="starlight-aside starlight-aside--note"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M12 11C11.7348 11 11.4804 11.1054 11.2929 11.2929C11.1054 11.4804 11 11.7348 11 12V16C11 16.2652 11.1054 16.5196 11.2929 16.7071C11.4804 16.8946 11.7348 17 12 17C12.2652 17 12.5196 16.8946 12.7071 16.7071C12.8946 16.5196 13 16.2652 13 16V12C13 11.7348 12.8946 11.4804 12.7071 11.2929C12.5196 11.1054 12.2652 11 12 11ZM12.38 7.08C12.1365 6.97998 11.8635 6.97998 11.62 7.08C11.4973 7.12759 11.3851 7.19896 11.29 7.29C11.2017 7.3872 11.1306 7.49882 11.08 7.62C11.024 7.73868 10.9966 7.86882 11 8C10.9992 8.13161 11.0245 8.26207 11.0742 8.38391C11.124 8.50574 11.1973 8.61656 11.29 8.71C11.3872 8.79833 11.4988 8.86936 11.62 8.92C11.7715 8.98224 11.936 9.00632 12.099 8.99011C12.2619 8.97391 12.4184 8.91792 12.5547 8.82707C12.691 8.73622 12.8029 8.61328 12.8805 8.46907C12.9582 8.32486 12.9992 8.16378 13 8C12.9963 7.73523 12.8927 7.48163 12.71 7.29C12.6149 7.19896 12.5028 7.12759 12.38 7.08ZM12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM12 20C10.4178 20 8.87104 19.5308 7.55544 18.6518C6.23985 17.7727 5.21447 16.5233 4.60897 15.0615C4.00347 13.5997 3.84504 11.9911 4.15372 10.4393C4.4624 8.88743 5.22433 7.46197 6.34315 6.34315C7.46197 5.22433 8.88743 4.4624 10.4393 4.15372C11.9911 3.84504 13.5997 4.00346 15.0615 4.60896C16.5233 5.21447 17.7727 6.23984 18.6518 7.55544C19.5308 8.87103 20 10.4177 20 12C20 14.1217 19.1572 16.1566 17.6569 17.6569C16.1566 19.1571 14.1217 20 12 20Z"></path></svg>注意</p><div class="starlight-aside__content"><p>部署名称必须与模型名称一致，OpenCode 才能正常工作。</p></div></aside>


  3. 执行 `/connect` 命令并搜索 **Azure** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 输入你的 API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  5. 将资源名称设置为环境变量：


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">AZURE_RESOURCE_NAME</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#032F62;--1:#9ECBFF">XXX</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#6F42C1;--1:#B392F0">opencode</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="AZURE_RESOURCE_NAME=XXX opencode" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


或者添加到你的 bash 配置文件中：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">~/.bash_profile</span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#BF3441;--1:#F97583">export</span><span style="--0:#24292E;--1:#E1E4E8"> AZURE_RESOURCE_NAME</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#24292E;--1:#E1E4E8">XXX</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="export AZURE_RESOURCE_NAME=XXX" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  6. 执行 `/models` 命令选择你已部署的模型。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### Azure Cognitive Services
  1. 前往 [Azure 门户](https://portal.azure.com/)并创建 **Azure OpenAI** 资源。你需要：
     * **资源名称** ：这会成为你的 API 端点的一部分（`https://AZURE_COGNITIVE_SERVICES_RESOURCE_NAME.cognitiveservices.azure.com/`）
     * **API 密钥** ：资源中的 `KEY 1` 或 `KEY 2`
  2. 前往 [Azure AI Foundry](https://ai.azure.com/) 并部署一个模型。


<aside aria-label="注意" class="starlight-aside starlight-aside--note"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M12 11C11.7348 11 11.4804 11.1054 11.2929 11.2929C11.1054 11.4804 11 11.7348 11 12V16C11 16.2652 11.1054 16.5196 11.2929 16.7071C11.4804 16.8946 11.7348 17 12 17C12.2652 17 12.5196 16.8946 12.7071 16.7071C12.8946 16.5196 13 16.2652 13 16V12C13 11.7348 12.8946 11.4804 12.7071 11.2929C12.5196 11.1054 12.2652 11 12 11ZM12.38 7.08C12.1365 6.97998 11.8635 6.97998 11.62 7.08C11.4973 7.12759 11.3851 7.19896 11.29 7.29C11.2017 7.3872 11.1306 7.49882 11.08 7.62C11.024 7.73868 10.9966 7.86882 11 8C10.9992 8.13161 11.0245 8.26207 11.0742 8.38391C11.124 8.50574 11.1973 8.61656 11.29 8.71C11.3872 8.79833 11.4988 8.86936 11.62 8.92C11.7715 8.98224 11.936 9.00632 12.099 8.99011C12.2619 8.97391 12.4184 8.91792 12.5547 8.82707C12.691 8.73622 12.8029 8.61328 12.8805 8.46907C12.9582 8.32486 12.9992 8.16378 13 8C12.9963 7.73523 12.8927 7.48163 12.71 7.29C12.6149 7.19896 12.5028 7.12759 12.38 7.08ZM12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM12 20C10.4178 20 8.87104 19.5308 7.55544 18.6518C6.23985 17.7727 5.21447 16.5233 4.60897 15.0615C4.00347 13.5997 3.84504 11.9911 4.15372 10.4393C4.4624 8.88743 5.22433 7.46197 6.34315 6.34315C7.46197 5.22433 8.88743 4.4624 10.4393 4.15372C11.9911 3.84504 13.5997 4.00346 15.0615 4.60896C16.5233 5.21447 17.7727 6.23984 18.6518 7.55544C19.5308 8.87103 20 10.4177 20 12C20 14.1217 19.1572 16.1566 17.6569 17.6569C16.1566 19.1571 14.1217 20 12 20Z"></path></svg>注意</p><div class="starlight-aside__content"><p>部署名称必须与模型名称一致，OpenCode 才能正常工作。</p></div></aside>


  3. 执行 `/connect` 命令并搜索 **Azure Cognitive Services** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 输入你的 API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  5. 将资源名称设置为环境变量：


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">AZURE_COGNITIVE_SERVICES_RESOURCE_NAME</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#032F62;--1:#9ECBFF">XXX</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#6F42C1;--1:#B392F0">opencode</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="AZURE_COGNITIVE_SERVICES_RESOURCE_NAME=XXX opencode" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


或者添加到你的 bash 配置文件中：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">~/.bash_profile</span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#BF3441;--1:#F97583">export</span><span style="--0:#24292E;--1:#E1E4E8"> AZURE_COGNITIVE_SERVICES_RESOURCE_NAME</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#24292E;--1:#E1E4E8">XXX</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="export AZURE_COGNITIVE_SERVICES_RESOURCE_NAME=XXX" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  6. 执行 `/models` 命令选择你已部署的模型。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### Baseten
  1. 前往 [Baseten](https://app.baseten.co/)，创建账户并生成 API 密钥。
  2. 执行 `/connect` 命令并搜索 **Baseten** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入你的 Baseten API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择模型。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### Cerebras
  1. 前往 [Cerebras 控制台](https://inference.cerebras.ai/)，创建账户并生成 API 密钥。
  2. 执行 `/connect` 命令并搜索 **Cerebras** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入你的 Cerebras API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择模型，例如 _Qwen 3 Coder 480B_ 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### Cloudflare AI Gateway
Cloudflare AI Gateway 允许你通过统一端点访问来自 OpenAI、Anthropic、Workers AI 等提供商的模型。通过 [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/)，你无需为每个提供商单独准备 API 密钥。
  1. 前往 [Cloudflare 仪表盘](https://dash.cloudflare.com/)，导航到 **AI** > **AI Gateway** ，创建一个新的网关。
  2. 将你的 Account ID 和 Gateway ID 设置为环境变量。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">~/.bash_profile</span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#BF3441;--1:#F97583">export</span><span style="--0:#24292E;--1:#E1E4E8"> CLOUDFLARE_ACCOUNT_ID</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#24292E;--1:#E1E4E8">your-32-character-account-id</span></div></div><div class="ec-line"><div class="code"><span style="--0:#BF3441;--1:#F97583">export</span><span style="--0:#24292E;--1:#E1E4E8"> CLOUDFLARE_GATEWAY_ID</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#24292E;--1:#E1E4E8">your-gateway-id</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="export CLOUDFLARE_ACCOUNT_ID=your-32-character-account-idexport CLOUDFLARE_GATEWAY_ID=your-gateway-id" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 执行 `/connect` 命令并搜索 **Cloudflare AI Gateway** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 输入你的 Cloudflare API Token。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


或者将其设置为环境变量。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">~/.bash_profile</span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#BF3441;--1:#F97583">export</span><span style="--0:#24292E;--1:#E1E4E8"> CLOUDFLARE_API_TOKEN</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#24292E;--1:#E1E4E8">your-api-token</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="export CLOUDFLARE_API_TOKEN=your-api-token" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  5. 执行 `/models` 命令选择模型。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


你也可以通过 OpenCode 配置添加模型。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"provider"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"cloudflare-ai-gateway"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"models"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#005CC5;--1:#79B8FF">"openai/gpt-4o"</span><span style="--0:#24292E;--1:#E1E4E8">: {},</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#005CC5;--1:#79B8FF">"anthropic/claude-sonnet-4"</span><span style="--0:#24292E;--1:#E1E4E8">: {}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "provider": {    "cloudflare-ai-gateway": {      "models": {        "openai/gpt-4o": {},        "anthropic/claude-sonnet-4": {}      }    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### Cortecs
  1. 前往 [Cortecs 控制台](https://cortecs.ai/)，创建账户并生成 API 密钥。
  2. 执行 `/connect` 命令并搜索 **Cortecs** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入你的 Cortecs API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择模型，例如 _Kimi K2 Instruct_ 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### DeepSeek
  1. 前往 [DeepSeek 控制台](https://platform.deepseek.com/)，创建账户并点击 **Create new API key** 。
  2. 执行 `/connect` 命令并搜索 **DeepSeek** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入你的 DeepSeek API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择 DeepSeek 模型，例如 _DeepSeek V4 Pro_ 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### Deep Infra
  1. 前往 [Deep Infra 仪表盘](https://deepinfra.com/dash)，创建账户并生成 API 密钥。
  2. 执行 `/connect` 命令并搜索 **Deep Infra** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入你的 Deep Infra API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择模型。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### FrogBot
  1. 前往 [FrogBot 仪表盘](https://app.frogbot.ai/signup)，创建账户并生成 API 密钥。
  2. 执行 `/connect` 命令并搜索 **FrogBot** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入你的 FrogBot API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择模型。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### Fireworks AI
  1. 前往 [Fireworks AI 控制台](https://app.fireworks.ai/)，创建账户并点击 **Create API Key** 。
  2. 执行 `/connect` 命令并搜索 **Fireworks AI** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入你的 Fireworks AI API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择模型，例如 _Kimi K2 Instruct_ 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### GitLab Duo
GitLab Duo 通过 GitLab 的 Anthropic 代理提供具有原生工具调用能力的 AI 驱动的代理聊天。
  1. 执行 `/connect` 命令并选择 GitLab。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  2. 选择你的身份验证方式：


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ Select auth method</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│ OAuth (Recommended)</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│ Personal Access Token</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ Select auth method││ OAuth (Recommended)│ Personal Access Token└" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


#### 使用 OAuth（推荐）
选择 **OAuth** ，浏览器会自动打开进行授权。
#### 使用个人访问令牌
     1. 前往 [GitLab 用户设置 > Access Tokens](https://gitlab.com/-/user_settings/personal_access_tokens)
     2. 点击 **Add new token**
     3. 名称填写 `OpenCode`，范围选择 `api`
     4. 复制令牌（以 `glpat-` 开头）
     5. 在终端中输入该令牌
  3. 执行 `/models` 命令查看可用模型。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


提供三个基于 Claude 的模型：
     * **duo-chat-haiku-4-5** （默认）- 快速响应，适合简单任务
     * **duo-chat-sonnet-4-5** \- 性能均衡，适合大多数工作流
     * **duo-chat-opus-4-5** \- 最强大，适合复杂分析


<aside aria-label="注意" class="starlight-aside starlight-aside--note"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M12 11C11.7348 11 11.4804 11.1054 11.2929 11.2929C11.1054 11.4804 11 11.7348 11 12V16C11 16.2652 11.1054 16.5196 11.2929 16.7071C11.4804 16.8946 11.7348 17 12 17C12.2652 17 12.5196 16.8946 12.7071 16.7071C12.8946 16.5196 13 16.2652 13 16V12C13 11.7348 12.8946 11.4804 12.7071 11.2929C12.5196 11.1054 12.2652 11 12 11ZM12.38 7.08C12.1365 6.97998 11.8635 6.97998 11.62 7.08C11.4973 7.12759 11.3851 7.19896 11.29 7.29C11.2017 7.3872 11.1306 7.49882 11.08 7.62C11.024 7.73868 10.9966 7.86882 11 8C10.9992 8.13161 11.0245 8.26207 11.0742 8.38391C11.124 8.50574 11.1973 8.61656 11.29 8.71C11.3872 8.79833 11.4988 8.86936 11.62 8.92C11.7715 8.98224 11.936 9.00632 12.099 8.99011C12.2619 8.97391 12.4184 8.91792 12.5547 8.82707C12.691 8.73622 12.8029 8.61328 12.8805 8.46907C12.9582 8.32486 12.9992 8.16378 13 8C12.9963 7.73523 12.8927 7.48163 12.71 7.29C12.6149 7.19896 12.5028 7.12759 12.38 7.08ZM12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM12 20C10.4178 20 8.87104 19.5308 7.55544 18.6518C6.23985 17.7727 5.21447 16.5233 4.60897 15.0615C4.00347 13.5997 3.84504 11.9911 4.15372 10.4393C4.4624 8.88743 5.22433 7.46197 6.34315 6.34315C7.46197 5.22433 8.88743 4.4624 10.4393 4.15372C11.9911 3.84504 13.5997 4.00346 15.0615 4.60896C16.5233 5.21447 17.7727 6.23984 18.6518 7.55544C19.5308 8.87103 20 10.4177 20 12C20 14.1217 19.1572 16.1566 17.6569 17.6569C16.1566 19.1571 14.1217 20 12 20Z"></path></svg>注意</p><div class="starlight-aside__content"><p>你也可以通过指定 <code dir="auto">GITLAB_TOKEN</code> 环境变量来避免将令牌存储在 OpenCode 的认证存储中。</p></div></aside>


##### 自托管 GitLab


<aside aria-label="合规说明" class="starlight-aside starlight-aside--note"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M12 11C11.7348 11 11.4804 11.1054 11.2929 11.2929C11.1054 11.4804 11 11.7348 11 12V16C11 16.2652 11.1054 16.5196 11.2929 16.7071C11.4804 16.8946 11.7348 17 12 17C12.2652 17 12.5196 16.8946 12.7071 16.7071C12.8946 16.5196 13 16.2652 13 16V12C13 11.7348 12.8946 11.4804 12.7071 11.2929C12.5196 11.1054 12.2652 11 12 11ZM12.38 7.08C12.1365 6.97998 11.8635 6.97998 11.62 7.08C11.4973 7.12759 11.3851 7.19896 11.29 7.29C11.2017 7.3872 11.1306 7.49882 11.08 7.62C11.024 7.73868 10.9966 7.86882 11 8C10.9992 8.13161 11.0245 8.26207 11.0742 8.38391C11.124 8.50574 11.1973 8.61656 11.29 8.71C11.3872 8.79833 11.4988 8.86936 11.62 8.92C11.7715 8.98224 11.936 9.00632 12.099 8.99011C12.2619 8.97391 12.4184 8.91792 12.5547 8.82707C12.691 8.73622 12.8029 8.61328 12.8805 8.46907C12.9582 8.32486 12.9992 8.16378 13 8C12.9963 7.73523 12.8927 7.48163 12.71 7.29C12.6149 7.19896 12.5028 7.12759 12.38 7.08ZM12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM12 20C10.4178 20 8.87104 19.5308 7.55544 18.6518C6.23985 17.7727 5.21447 16.5233 4.60897 15.0615C4.00347 13.5997 3.84504 11.9911 4.15372 10.4393C4.4624 8.88743 5.22433 7.46197 6.34315 6.34315C7.46197 5.22433 8.88743 4.4624 10.4393 4.15372C11.9911 3.84504 13.5997 4.00346 15.0615 4.60896C16.5233 5.21447 17.7727 6.23984 18.6518 7.55544C19.5308 8.87103 20 10.4177 20 12C20 14.1217 19.1572 16.1566 17.6569 17.6569C16.1566 19.1571 14.1217 20 12 20Z"></path></svg>合规说明</p><div class="starlight-aside__content"><p>OpenCode 会使用一个小模型来执行部分 AI 任务，例如生成会话标题。默认情况下使用由 Zen 托管的 gpt-5-nano。如果你需要让 OpenCode 仅使用你自己的 GitLab 托管实例，请在 <code dir="auto">opencode.json</code> 文件中添加以下内容。同时建议禁用会话共享。</p><div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"small_model"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"gitlab/duo-chat-haiku-4-5"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"share"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"disabled"</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "small_model": "gitlab/duo-chat-haiku-4-5",  "share": "disabled"}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div></div></aside>


对于自托管 GitLab 实例：


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#BF3441;--1:#F97583">export</span><span style="--0:#24292E;--1:#E1E4E8"> GITLAB_INSTANCE_URL</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#24292E;--1:#E1E4E8">https://gitlab.company.com</span></div></div><div class="ec-line"><div class="code"><span style="--0:#BF3441;--1:#F97583">export</span><span style="--0:#24292E;--1:#E1E4E8"> GITLAB_TOKEN</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#24292E;--1:#E1E4E8">glpat-...</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="export GITLAB_INSTANCE_URL=https://gitlab.company.comexport GITLAB_TOKEN=glpat-..." data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


如果你的实例运行了自定义 AI Gateway：


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">GITLAB_AI_GATEWAY_URL</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#032F62;--1:#9ECBFF">https://ai-gateway.company.com</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="GITLAB_AI_GATEWAY_URL=https://ai-gateway.company.com" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


或者添加到你的 bash 配置文件中：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">~/.bash_profile</span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#BF3441;--1:#F97583">export</span><span style="--0:#24292E;--1:#E1E4E8"> GITLAB_INSTANCE_URL</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#24292E;--1:#E1E4E8">https://gitlab.company.com</span></div></div><div class="ec-line"><div class="code"><span style="--0:#BF3441;--1:#F97583">export</span><span style="--0:#24292E;--1:#E1E4E8"> GITLAB_AI_GATEWAY_URL</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#24292E;--1:#E1E4E8">https://ai-gateway.company.com</span></div></div><div class="ec-line"><div class="code"><span style="--0:#BF3441;--1:#F97583">export</span><span style="--0:#24292E;--1:#E1E4E8"> GITLAB_TOKEN</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#24292E;--1:#E1E4E8">glpat-...</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="export GITLAB_INSTANCE_URL=https://gitlab.company.comexport GITLAB_AI_GATEWAY_URL=https://ai-gateway.company.comexport GITLAB_TOKEN=glpat-..." data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>

 

<aside aria-label="注意" class="starlight-aside starlight-aside--note"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M12 11C11.7348 11 11.4804 11.1054 11.2929 11.2929C11.1054 11.4804 11 11.7348 11 12V16C11 16.2652 11.1054 16.5196 11.2929 16.7071C11.4804 16.8946 11.7348 17 12 17C12.2652 17 12.5196 16.8946 12.7071 16.7071C12.8946 16.5196 13 16.2652 13 16V12C13 11.7348 12.8946 11.4804 12.7071 11.2929C12.5196 11.1054 12.2652 11 12 11ZM12.38 7.08C12.1365 6.97998 11.8635 6.97998 11.62 7.08C11.4973 7.12759 11.3851 7.19896 11.29 7.29C11.2017 7.3872 11.1306 7.49882 11.08 7.62C11.024 7.73868 10.9966 7.86882 11 8C10.9992 8.13161 11.0245 8.26207 11.0742 8.38391C11.124 8.50574 11.1973 8.61656 11.29 8.71C11.3872 8.79833 11.4988 8.86936 11.62 8.92C11.7715 8.98224 11.936 9.00632 12.099 8.99011C12.2619 8.97391 12.4184 8.91792 12.5547 8.82707C12.691 8.73622 12.8029 8.61328 12.8805 8.46907C12.9582 8.32486 12.9992 8.16378 13 8C12.9963 7.73523 12.8927 7.48163 12.71 7.29C12.6149 7.19896 12.5028 7.12759 12.38 7.08ZM12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM12 20C10.4178 20 8.87104 19.5308 7.55544 18.6518C6.23985 17.7727 5.21447 16.5233 4.60897 15.0615C4.00347 13.5997 3.84504 11.9911 4.15372 10.4393C4.4624 8.88743 5.22433 7.46197 6.34315 6.34315C7.46197 5.22433 8.88743 4.4624 10.4393 4.15372C11.9911 3.84504 13.5997 4.00346 15.0615 4.60896C16.5233 5.21447 17.7727 6.23984 18.6518 7.55544C19.5308 8.87103 20 10.4177 20 12C20 14.1217 19.1572 16.1566 17.6569 17.6569C16.1566 19.1571 14.1217 20 12 20Z"></path></svg>注意</p><div class="starlight-aside__content"><p>你的 GitLab 管理员必须启用以下功能：</p><ol>
<li>为用户、群组或实例启用 <a href="https://docs.gitlab.com/user/duo_agent_platform/turn_on_off/">Duo Agent Platform</a></li>
<li>功能标志（通过 Rails 控制台）：
<ul>
<li><code dir="auto">agent_platform_claude_code</code></li>
<li><code dir="auto">third_party_agents_enabled</code></li>
</ul>
</li>
</ol></div></aside>


##### 自托管实例的 OAuth
要在自托管实例上使用 OAuth，你需要创建一个新应用（设置 → 应用），回调 URL 设置为 `http://127.0.0.1:8080/callback`，并选择以下范围：
  * api（代表你访问 API）
  * read_user（读取你的个人信息）
  * read_repository（允许对仓库进行只读访问）


然后将应用 ID 导出为环境变量：


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#BF3441;--1:#F97583">export</span><span style="--0:#24292E;--1:#E1E4E8"> GITLAB_OAUTH_CLIENT_ID</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#24292E;--1:#E1E4E8">your_application_id_here</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="export GITLAB_OAUTH_CLIENT_ID=your_application_id_here" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


更多文档请参阅 [opencode-gitlab-auth](https://www.npmjs.com/package/opencode-gitlab-auth) 主页。
##### 配置
通过 `opencode.json` 进行自定义配置：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"provider"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"gitlab"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"options"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#005CC5;--1:#79B8FF">"instanceUrl"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://gitlab.com"</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "provider": {    "gitlab": {      "options": {        "instanceUrl": "https://gitlab.com"      }    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


##### GitLab API 工具（可选，但强烈推荐）
要访问 GitLab 工具（合并请求、Issue、流水线、CI/CD 等）：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"plugin"</span><span style="--0:#24292E;--1:#E1E4E8">: [</span><span style="--0:#032F62;--1:#9ECBFF">"opencode-gitlab-plugin"</span><span style="--0:#24292E;--1:#E1E4E8">]</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "plugin": ["opencode-gitlab-plugin"]}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


该插件提供全面的 GitLab 仓库管理功能，包括 MR 审查、Issue 跟踪、流水线监控等。
* * *
### GitHub Copilot
要在 OpenCode 中使用你的 GitHub Copilot 订阅：


<aside aria-label="注意" class="starlight-aside starlight-aside--note"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M12 11C11.7348 11 11.4804 11.1054 11.2929 11.2929C11.1054 11.4804 11 11.7348 11 12V16C11 16.2652 11.1054 16.5196 11.2929 16.7071C11.4804 16.8946 11.7348 17 12 17C12.2652 17 12.5196 16.8946 12.7071 16.7071C12.8946 16.5196 13 16.2652 13 16V12C13 11.7348 12.8946 11.4804 12.7071 11.2929C12.5196 11.1054 12.2652 11 12 11ZM12.38 7.08C12.1365 6.97998 11.8635 6.97998 11.62 7.08C11.4973 7.12759 11.3851 7.19896 11.29 7.29C11.2017 7.3872 11.1306 7.49882 11.08 7.62C11.024 7.73868 10.9966 7.86882 11 8C10.9992 8.13161 11.0245 8.26207 11.0742 8.38391C11.124 8.50574 11.1973 8.61656 11.29 8.71C11.3872 8.79833 11.4988 8.86936 11.62 8.92C11.7715 8.98224 11.936 9.00632 12.099 8.99011C12.2619 8.97391 12.4184 8.91792 12.5547 8.82707C12.691 8.73622 12.8029 8.61328 12.8805 8.46907C12.9582 8.32486 12.9992 8.16378 13 8C12.9963 7.73523 12.8927 7.48163 12.71 7.29C12.6149 7.19896 12.5028 7.12759 12.38 7.08ZM12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM12 20C10.4178 20 8.87104 19.5308 7.55544 18.6518C6.23985 17.7727 5.21447 16.5233 4.60897 15.0615C4.00347 13.5997 3.84504 11.9911 4.15372 10.4393C4.4624 8.88743 5.22433 7.46197 6.34315 6.34315C7.46197 5.22433 8.88743 4.4624 10.4393 4.15372C11.9911 3.84504 13.5997 4.00346 15.0615 4.60896C16.5233 5.21447 17.7727 6.23984 18.6518 7.55544C19.5308 8.87103 20 10.4177 20 12C20 14.1217 19.1572 16.1566 17.6569 17.6569C16.1566 19.1571 14.1217 20 12 20Z"></path></svg>注意</p><div class="starlight-aside__content"><p>部分模型可能需要 <a href="https://github.com/features/copilot/plans">Pro+ 订阅</a>才能使用。</p></div></aside>


  1. 执行 `/connect` 命令并搜索 GitHub Copilot。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  2. 前往 [github.com/login/device](https://github.com/login/device) 并输入验证码。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ Login with GitHub Copilot</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│ https://github.com/login/device</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│ Enter code: 8F43-6FCF</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ Waiting for authorization...</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ Login with GitHub Copilot││ https://github.com/login/device││ Enter code: 8F43-6FCF│└ Waiting for authorization..." data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 现在执行 `/models` 命令选择你想要的模型。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### Google Vertex AI
要在 OpenCode 中使用 Google Vertex AI：
  1. 前往 Google Cloud Console 中的**模型花园** ，查看你所在区域可用的模型。


<aside aria-label="注意" class="starlight-aside starlight-aside--note"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M12 11C11.7348 11 11.4804 11.1054 11.2929 11.2929C11.1054 11.4804 11 11.7348 11 12V16C11 16.2652 11.1054 16.5196 11.2929 16.7071C11.4804 16.8946 11.7348 17 12 17C12.2652 17 12.5196 16.8946 12.7071 16.7071C12.8946 16.5196 13 16.2652 13 16V12C13 11.7348 12.8946 11.4804 12.7071 11.2929C12.5196 11.1054 12.2652 11 12 11ZM12.38 7.08C12.1365 6.97998 11.8635 6.97998 11.62 7.08C11.4973 7.12759 11.3851 7.19896 11.29 7.29C11.2017 7.3872 11.1306 7.49882 11.08 7.62C11.024 7.73868 10.9966 7.86882 11 8C10.9992 8.13161 11.0245 8.26207 11.0742 8.38391C11.124 8.50574 11.1973 8.61656 11.29 8.71C11.3872 8.79833 11.4988 8.86936 11.62 8.92C11.7715 8.98224 11.936 9.00632 12.099 8.99011C12.2619 8.97391 12.4184 8.91792 12.5547 8.82707C12.691 8.73622 12.8029 8.61328 12.8805 8.46907C12.9582 8.32486 12.9992 8.16378 13 8C12.9963 7.73523 12.8927 7.48163 12.71 7.29C12.6149 7.19896 12.5028 7.12759 12.38 7.08ZM12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM12 20C10.4178 20 8.87104 19.5308 7.55544 18.6518C6.23985 17.7727 5.21447 16.5233 4.60897 15.0615C4.00347 13.5997 3.84504 11.9911 4.15372 10.4393C4.4624 8.88743 5.22433 7.46197 6.34315 6.34315C7.46197 5.22433 8.88743 4.4624 10.4393 4.15372C11.9911 3.84504 13.5997 4.00346 15.0615 4.60896C16.5233 5.21447 17.7727 6.23984 18.6518 7.55544C19.5308 8.87103 20 10.4177 20 12C20 14.1217 19.1572 16.1566 17.6569 17.6569C16.1566 19.1571 14.1217 20 12 20Z"></path></svg>注意</p><div class="starlight-aside__content"><p>你需要一个启用了 Vertex AI API 的 Google Cloud 项目。</p></div></aside>


  2. 设置所需的环境变量：
     * `GOOGLE_CLOUD_PROJECT`：你的 Google Cloud 项目 ID
     * `VERTEX_LOCATION`（可选）：Vertex AI 的区域（默认为 `global`）
     * 身份验证（选择其一）： 
       * `GOOGLE_APPLICATION_CREDENTIALS`：服务账户 JSON 密钥文件的路径
       * 使用 gcloud CLI 进行身份验证：`gcloud auth application-default login`
在运行 opencode 时设置：


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">GOOGLE_APPLICATION_CREDENTIALS</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#032F62;--1:#9ECBFF">/path/to/service-account.json</span><span style="--0:#24292E;--1:#E1E4E8"> GOOGLE_CLOUD_PROJECT</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#032F62;--1:#9ECBFF">your-project-id</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#6F42C1;--1:#B392F0">opencode</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json GOOGLE_CLOUD_PROJECT=your-project-id opencode" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


或者添加到你的 bash 配置文件中：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">~/.bash_profile</span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#BF3441;--1:#F97583">export</span><span style="--0:#24292E;--1:#E1E4E8"> GOOGLE_APPLICATION_CREDENTIALS</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#24292E;--1:#E1E4E8">/path/to/service-account.json</span></div></div><div class="ec-line"><div class="code"><span style="--0:#BF3441;--1:#F97583">export</span><span style="--0:#24292E;--1:#E1E4E8"> GOOGLE_CLOUD_PROJECT</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#24292E;--1:#E1E4E8">your-project-id</span></div></div><div class="ec-line"><div class="code"><span style="--0:#BF3441;--1:#F97583">export</span><span style="--0:#24292E;--1:#E1E4E8"> VERTEX_LOCATION</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#24292E;--1:#E1E4E8">global</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.jsonexport GOOGLE_CLOUD_PROJECT=your-project-idexport VERTEX_LOCATION=global" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


<aside aria-label="提示" class="starlight-aside starlight-aside--tip"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path clip-rule="evenodd" d="M1.43909 8.85483L1.44039 8.85354L4.96668 5.33815C5.30653 4.99386 5.7685 4.79662 6.2524 4.78972L6.26553 4.78963L12.9014 4.78962L13.8479 3.84308C16.9187 0.772319 20.0546 0.770617 21.4678 0.975145C21.8617 1.02914 22.2271 1.21053 22.5083 1.4917C22.7894 1.77284 22.9708 2.13821 23.0248 2.53199C23.2294 3.94517 23.2278 7.08119 20.1569 10.1521L19.2107 11.0983V17.7338L19.2106 17.7469C19.2037 18.2308 19.0067 18.6933 18.6624 19.0331L15.1456 22.5608C14.9095 22.7966 14.6137 22.964 14.29 23.0449C13.9663 23.1259 13.6267 23.1174 13.3074 23.0204C12.9881 22.9235 12.7011 22.7417 12.4771 22.4944C12.2533 22.2473 12.1006 21.9441 12.0355 21.6171L11.1783 17.3417L6.65869 12.822L4.34847 12.3589L2.38351 11.965C2.05664 11.8998 1.75272 11.747 1.50564 11.5232C1.25835 11.2992 1.07653 11.0122 0.979561 10.6929C0.882595 10.3736 0.874125 10.034 0.955057 9.7103C1.03599 9.38659 1.20328 9.09092 1.43909 8.85483ZM6.8186 10.8724L2.94619 10.096L6.32006 6.73268H10.9583L6.8186 10.8724ZM15.2219 5.21703C17.681 2.75787 20.0783 2.75376 21.1124 2.8876C21.2462 3.92172 21.2421 6.31895 18.783 8.77812L12.0728 15.4883L8.51172 11.9272L15.2219 5.21703ZM13.9042 21.0538L13.1279 17.1811L17.2676 13.0414V17.68L13.9042 21.0538Z" fill-rule="evenodd"></path><path d="M9.31827 18.3446C9.45046 17.8529 9.17864 17.3369 8.68945 17.1724C8.56178 17.1294 8.43145 17.1145 8.30512 17.1243C8.10513 17.1398 7.91519 17.2172 7.76181 17.3434C7.62613 17.455 7.51905 17.6048 7.45893 17.7835C6.97634 19.2186 5.77062 19.9878 4.52406 20.4029C4.08525 20.549 3.6605 20.644 3.29471 20.7053C3.35607 20.3395 3.45098 19.9148 3.59711 19.476C4.01221 18.2294 4.78141 17.0237 6.21648 16.5411C6.39528 16.481 6.54504 16.3739 6.65665 16.2382C6.85126 16.0016 6.92988 15.678 6.84417 15.3647C6.83922 15.3466 6.83373 15.3286 6.82767 15.3106C6.74106 15.053 6.55701 14.8557 6.33037 14.7459C6.10949 14.6389 5.84816 14.615 5.59715 14.6994C5.47743 14.7397 5.36103 14.7831 5.24786 14.8294C3.22626 15.6569 2.2347 17.4173 1.75357 18.8621C1.49662 19.6337 1.36993 20.3554 1.30679 20.8818C1.27505 21.1464 1.25893 21.3654 1.25072 21.5213C1.24662 21.5993 1.24448 21.6618 1.24337 21.7066L1.243 21.7226L1.24235 21.7605L1.2422 21.7771L1.24217 21.7827L1.24217 21.7856C1.24217 22.3221 1.67703 22.7579 2.2137 22.7579L2.2155 22.7579L2.22337 22.7578L2.23956 22.7577C2.25293 22.7575 2.27096 22.7572 2.29338 22.7567C2.33821 22.7555 2.40073 22.7534 2.47876 22.7493C2.63466 22.7411 2.85361 22.725 3.11822 22.6932C3.64462 22.6301 4.36636 22.5034 5.13797 22.2464C6.58274 21.7653 8.3431 20.7738 9.17063 18.7522C9.21696 18.639 9.26037 18.5226 9.30064 18.4029C9.30716 18.3835 9.31304 18.364 9.31827 18.3446Z"></path></svg>提示</p><div class="starlight-aside__content"><p><code dir="auto">global</code> 区域可以提高可用性并减少错误，且不会产生额外费用。如果有数据驻留需求，请使用区域端点（例如 <code dir="auto">us-central1</code>）。<a href="https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-partner-models#regional_and_global_endpoints">了解更多</a></p></div></aside>


  3. 执行 `/models` 命令选择你想要的模型。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### Groq
  1. 前往 [Groq 控制台](https://console.groq.com/)，点击 **Create API Key** 并复制密钥。
  2. 执行 `/connect` 命令并搜索 Groq。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入该提供商的 API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择你想要的模型。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### Hugging Face
[Hugging Face Inference Providers](https://huggingface.co/docs/inference-providers) 提供对由 17+ 提供商支持的开放模型的访问。
  1. 前往 [Hugging Face 设置](https://huggingface.co/settings/tokens/new?ownUserPermissions=inference.serverless.write&tokenType=fineGrained)，创建一个具有调用 Inference Providers 权限的令牌。
  2. 执行 `/connect` 命令并搜索 **Hugging Face** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入你的 Hugging Face 令牌。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择模型，例如 _Kimi-K2-Instruct_ 或 _GLM-4.6_ 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### Helicone
[Helicone](https://helicone.ai) 是一个 LLM 可观测性平台，为你的 AI 应用提供日志记录、监控和分析功能。Helicone AI Gateway 会根据模型自动将请求路由到对应的提供商。
  1. 前往 [Helicone](https://helicone.ai)，创建账户并在仪表盘中生成 API 密钥。
  2. 执行 `/connect` 命令并搜索 **Helicone** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入你的 Helicone API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择模型。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


如需了解更多提供商以及缓存、速率限制等高级功能，请查阅 [Helicone 文档](https://docs.helicone.ai)。
#### 可选配置
如果 Helicone 的某些功能或模型未通过 OpenCode 自动配置，你随时可以手动配置。
[Helicone 模型目录](https://helicone.ai/models)中可以找到你需要添加的模型 ID。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">~/.config/opencode/opencode.jsonc</span></figcaption><pre data-language="jsonc"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"provider"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"helicone"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"npm"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"@ai-sdk/openai-compatible"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"name"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"Helicone"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"options"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#005CC5;--1:#79B8FF">"baseURL"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://ai-gateway.helicone.ai"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">},</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"models"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#005CC5;--1:#79B8FF">"gpt-4o"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">          </span><span style="--0:#616972;--1:#99A0A6">// Model ID (from Helicone's model directory page)</span></div></div><div class="ec-line"><div class="code"><span class="indent">          </span><span style="--0:#005CC5;--1:#79B8FF">"name"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"GPT-4o"</span><span style="--0:#24292E;--1:#E1E4E8">, </span><span style="--0:#616972;--1:#99A0A6">// Your own custom name for the model</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">        </span></span><span style="--0:#24292E;--1:#E1E4E8">},</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#005CC5;--1:#79B8FF">"claude-sonnet-4-20250514"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">          </span><span style="--0:#005CC5;--1:#79B8FF">"name"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"Claude Sonnet 4"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">        </span></span><span style="--0:#24292E;--1:#E1E4E8">},</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">},</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">},</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">},</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="{  &quot;$schema&quot;: &quot;https://opencode.ai/config.json&quot;,  &quot;provider&quot;: {    &quot;helicone&quot;: {      &quot;npm&quot;: &quot;@ai-sdk/openai-compatible&quot;,      &quot;name&quot;: &quot;Helicone&quot;,      &quot;options&quot;: {        &quot;baseURL&quot;: &quot;https://ai-gateway.helicone.ai&quot;,      },      &quot;models&quot;: {        &quot;gpt-4o&quot;: {          // Model ID (from Helicone's model directory page)          &quot;name&quot;: &quot;GPT-4o&quot;, // Your own custom name for the model        },        &quot;claude-sonnet-4-20250514&quot;: {          &quot;name&quot;: &quot;Claude Sonnet 4&quot;,        },      },    },  },}" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


#### 自定义请求头
Helicone 支持用于缓存、用户跟踪和会话管理等功能的自定义请求头。使用 `options.headers` 将它们添加到提供商配置中：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">~/.config/opencode/opencode.jsonc</span></figcaption><pre data-language="jsonc"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"provider"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"helicone"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"npm"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"@ai-sdk/openai-compatible"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"name"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"Helicone"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"options"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#005CC5;--1:#79B8FF">"baseURL"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://ai-gateway.helicone.ai"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#005CC5;--1:#79B8FF">"headers"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">          </span><span style="--0:#005CC5;--1:#79B8FF">"Helicone-Cache-Enabled"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"true"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">          </span><span style="--0:#005CC5;--1:#79B8FF">"Helicone-User-Id"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"opencode"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">        </span></span><span style="--0:#24292E;--1:#E1E4E8">},</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">},</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">},</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">},</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "provider": {    "helicone": {      "npm": "@ai-sdk/openai-compatible",      "name": "Helicone",      "options": {        "baseURL": "https://ai-gateway.helicone.ai",        "headers": {          "Helicone-Cache-Enabled": "true",          "Helicone-User-Id": "opencode",        },      },    },  },}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


##### 会话跟踪
Helicone 的 [Sessions](https://docs.helicone.ai/features/sessions) 功能允许你将相关的 LLM 请求归为一组。使用 [opencode-helicone-session](https://github.com/H2Shami/opencode-helicone-session) 插件可以自动将每个 OpenCode 对话记录为 Helicone 中的一个会话。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">npm</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">install</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#005CC5;--1:#79B8FF">-g</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">opencode-helicone-session</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="npm install -g opencode-helicone-session" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


将其添加到配置中。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"plugin"</span><span style="--0:#24292E;--1:#E1E4E8">: [</span><span style="--0:#032F62;--1:#9ECBFF">"opencode-helicone-session"</span><span style="--0:#24292E;--1:#E1E4E8">]</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "plugin": ["opencode-helicone-session"]}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


该插件会在你的请求中注入 `Helicone-Session-Id` 和 `Helicone-Session-Name` 请求头。在 Helicone 的 Sessions 页面中，你可以看到每个 OpenCode 对话都作为独立的会话列出。
##### 常用 Helicone 请求头
请求头| 描述  
---|---  
`Helicone-Cache-Enabled`| 启用响应缓存（`true`/`false`）  
`Helicone-User-Id`| 按用户跟踪指标  
`Helicone-Property-[Name]`| 添加自定义属性（例如 `Helicone-Property-Environment`）  
`Helicone-Prompt-Id`| 将请求与提示词版本关联  
有关所有可用请求头，请参阅 [Helicone Header Directory](https://docs.helicone.ai/helicone-headers/header-directory)。
* * *
### llama.cpp
你可以通过 [llama.cpp](https://github.com/ggml-org/llama.cpp) 的 llama-server 工具配置 OpenCode 使用本地模型。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"provider"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"</span><mark><span style="--0:#004ba0;--1:#81bcff">llama.cpp</span></mark><span style="--0:#005CC5;--1:#79B8FF">"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"npm"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"@ai-sdk/openai-compatible"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"name"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"llama-server (local)"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"options"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">        </span><span style="--0:#004ba0;--1:#81bcff">"baseURL"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"http://127.0.0.1:8080/v1"</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">},</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"models"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">        </span><span style="--0:#004ba0;--1:#81bcff">"qwen3-coder:a3b"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">          </span><span style="--0:#004ba0;--1:#81bcff">"name"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"Qwen3-Coder: a3b-30b (local)"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">          </span><span style="--0:#004ba0;--1:#81bcff">"limit"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">            </span><span style="--0:#004ba0;--1:#81bcff">"context"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#004ba0;--1:#81bcff">128000</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">            </span><span style="--0:#004ba0;--1:#81bcff">"output"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#004ba0;--1:#81bcff">65536</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">          </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">        </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "provider": {    "llama.cpp": {      "npm": "@ai-sdk/openai-compatible",      "name": "llama-server (local)",      "options": {        "baseURL": "http://127.0.0.1:8080/v1"      },      "models": {        "qwen3-coder:a3b": {          "name": "Qwen3-Coder: a3b-30b (local)",          "limit": {            "context": 128000,            "output": 65536          }        }      }    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


在这个示例中：
  * `llama.cpp` 是自定义的提供商 ID，可以是任意字符串。
  * `npm` 指定该提供商使用的包。这里使用 `@ai-sdk/openai-compatible` 来兼容任何 OpenAI 兼容的 API。
  * `name` 是该提供商在 UI 中显示的名称。
  * `options.baseURL` 是本地服务器的端点地址。
  * `models` 是模型 ID 到其配置的映射。模型名称会显示在模型选择列表中。


* * *
### IO.NET
IO.NET 提供 17 个针对不同用例优化的模型：
  1. 前往 [IO.NET 控制台](https://ai.io.net/)，创建账户并生成 API 密钥。
  2. 执行 `/connect` 命令并搜索 **IO.NET** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入你的 IO.NET API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择模型。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### LM Studio
你可以通过 LM Studio 配置 OpenCode 使用本地模型。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"provider"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"</span><mark><span style="--0:#004ba0;--1:#81bcff">lmstudio</span></mark><span style="--0:#005CC5;--1:#79B8FF">"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"npm"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"@ai-sdk/openai-compatible"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"name"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"LM Studio (local)"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"options"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">        </span><span style="--0:#004ba0;--1:#81bcff">"baseURL"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"http://127.0.0.1:1234/v1"</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">},</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"models"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">        </span><span style="--0:#004ba0;--1:#81bcff">"google/gemma-3n-e4b"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">          </span><span style="--0:#004ba0;--1:#81bcff">"name"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"Gemma 3n-e4b (local)"</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">        </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "provider": {    "lmstudio": {      "npm": "@ai-sdk/openai-compatible",      "name": "LM Studio (local)",      "options": {        "baseURL": "http://127.0.0.1:1234/v1"      },      "models": {        "google/gemma-3n-e4b": {          "name": "Gemma 3n-e4b (local)"        }      }    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


在这个示例中：
  * `lmstudio` 是自定义的提供商 ID，可以是任意字符串。
  * `npm` 指定该提供商使用的包。这里使用 `@ai-sdk/openai-compatible` 来兼容任何 OpenAI 兼容的 API。
  * `name` 是该提供商在 UI 中显示的名称。
  * `options.baseURL` 是本地服务器的端点地址。
  * `models` 是模型 ID 到其配置的映射。模型名称会显示在模型选择列表中。


* * *
### Moonshot AI
要使用 Moonshot AI 的 Kimi K2：
  1. 前往 [Moonshot AI 控制台](https://platform.moonshot.ai/console)，创建账户并点击 **Create API key** 。
  2. 执行 `/connect` 命令并搜索 **Moonshot AI** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入你的 Moonshot API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择 _Kimi K2_ 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### MiniMax
  1. 前往 [MiniMax API 控制台](https://platform.minimax.io/login)，创建账户并生成 API 密钥。
  2. 执行 `/connect` 命令并搜索 **MiniMax** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入你的 MiniMax API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择模型，例如 _M2.1_ 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### Nebius Token Factory
  1. 前往 [Nebius Token Factory 控制台](https://tokenfactory.nebius.com/)，创建账户并点击 **Add Key** 。
  2. 执行 `/connect` 命令并搜索 **Nebius Token Factory** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入你的 Nebius Token Factory API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择模型，例如 _Kimi K2 Instruct_ 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### Ollama
你可以通过 Ollama 配置 OpenCode 使用本地模型。


<aside aria-label="提示" class="starlight-aside starlight-aside--tip"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path clip-rule="evenodd" d="M1.43909 8.85483L1.44039 8.85354L4.96668 5.33815C5.30653 4.99386 5.7685 4.79662 6.2524 4.78972L6.26553 4.78963L12.9014 4.78962L13.8479 3.84308C16.9187 0.772319 20.0546 0.770617 21.4678 0.975145C21.8617 1.02914 22.2271 1.21053 22.5083 1.4917C22.7894 1.77284 22.9708 2.13821 23.0248 2.53199C23.2294 3.94517 23.2278 7.08119 20.1569 10.1521L19.2107 11.0983V17.7338L19.2106 17.7469C19.2037 18.2308 19.0067 18.6933 18.6624 19.0331L15.1456 22.5608C14.9095 22.7966 14.6137 22.964 14.29 23.0449C13.9663 23.1259 13.6267 23.1174 13.3074 23.0204C12.9881 22.9235 12.7011 22.7417 12.4771 22.4944C12.2533 22.2473 12.1006 21.9441 12.0355 21.6171L11.1783 17.3417L6.65869 12.822L4.34847 12.3589L2.38351 11.965C2.05664 11.8998 1.75272 11.747 1.50564 11.5232C1.25835 11.2992 1.07653 11.0122 0.979561 10.6929C0.882595 10.3736 0.874125 10.034 0.955057 9.7103C1.03599 9.38659 1.20328 9.09092 1.43909 8.85483ZM6.8186 10.8724L2.94619 10.096L6.32006 6.73268H10.9583L6.8186 10.8724ZM15.2219 5.21703C17.681 2.75787 20.0783 2.75376 21.1124 2.8876C21.2462 3.92172 21.2421 6.31895 18.783 8.77812L12.0728 15.4883L8.51172 11.9272L15.2219 5.21703ZM13.9042 21.0538L13.1279 17.1811L17.2676 13.0414V17.68L13.9042 21.0538Z" fill-rule="evenodd"></path><path d="M9.31827 18.3446C9.45046 17.8529 9.17864 17.3369 8.68945 17.1724C8.56178 17.1294 8.43145 17.1145 8.30512 17.1243C8.10513 17.1398 7.91519 17.2172 7.76181 17.3434C7.62613 17.455 7.51905 17.6048 7.45893 17.7835C6.97634 19.2186 5.77062 19.9878 4.52406 20.4029C4.08525 20.549 3.6605 20.644 3.29471 20.7053C3.35607 20.3395 3.45098 19.9148 3.59711 19.476C4.01221 18.2294 4.78141 17.0237 6.21648 16.5411C6.39528 16.481 6.54504 16.3739 6.65665 16.2382C6.85126 16.0016 6.92988 15.678 6.84417 15.3647C6.83922 15.3466 6.83373 15.3286 6.82767 15.3106C6.74106 15.053 6.55701 14.8557 6.33037 14.7459C6.10949 14.6389 5.84816 14.615 5.59715 14.6994C5.47743 14.7397 5.36103 14.7831 5.24786 14.8294C3.22626 15.6569 2.2347 17.4173 1.75357 18.8621C1.49662 19.6337 1.36993 20.3554 1.30679 20.8818C1.27505 21.1464 1.25893 21.3654 1.25072 21.5213C1.24662 21.5993 1.24448 21.6618 1.24337 21.7066L1.243 21.7226L1.24235 21.7605L1.2422 21.7771L1.24217 21.7827L1.24217 21.7856C1.24217 22.3221 1.67703 22.7579 2.2137 22.7579L2.2155 22.7579L2.22337 22.7578L2.23956 22.7577C2.25293 22.7575 2.27096 22.7572 2.29338 22.7567C2.33821 22.7555 2.40073 22.7534 2.47876 22.7493C2.63466 22.7411 2.85361 22.725 3.11822 22.6932C3.64462 22.6301 4.36636 22.5034 5.13797 22.2464C6.58274 21.7653 8.3431 20.7738 9.17063 18.7522C9.21696 18.639 9.26037 18.5226 9.30064 18.4029C9.30716 18.3835 9.31304 18.364 9.31827 18.3446Z"></path></svg>提示</p><div class="starlight-aside__content"><p>Ollama 可以自动为 OpenCode 进行配置。详见 <a href="https://docs.ollama.com/integrations/opencode">Ollama 集成文档</a>。</p></div></aside>

 

<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"provider"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"</span><mark><span style="--0:#004ba0;--1:#81bcff">ollama</span></mark><span style="--0:#005CC5;--1:#79B8FF">"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"npm"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"@ai-sdk/openai-compatible"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"name"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"Ollama (local)"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"options"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">        </span><span style="--0:#004ba0;--1:#81bcff">"baseURL"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"http://localhost:11434/v1"</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">},</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"models"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">        </span><span style="--0:#004ba0;--1:#81bcff">"llama2"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">          </span><span style="--0:#004ba0;--1:#81bcff">"name"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"Llama 2"</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">        </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "provider": {    "ollama": {      "npm": "@ai-sdk/openai-compatible",      "name": "Ollama (local)",      "options": {        "baseURL": "http://localhost:11434/v1"      },      "models": {        "llama2": {          "name": "Llama 2"        }      }    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


在这个示例中：
  * `ollama` 是自定义的提供商 ID，可以是任意字符串。
  * `npm` 指定该提供商使用的包。这里使用 `@ai-sdk/openai-compatible` 来兼容任何 OpenAI 兼容的 API。
  * `name` 是该提供商在 UI 中显示的名称。
  * `options.baseURL` 是本地服务器的端点地址。
  * `models` 是模型 ID 到其配置的映射。模型名称会显示在模型选择列表中。


<aside aria-label="提示" class="starlight-aside starlight-aside--tip"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path clip-rule="evenodd" d="M1.43909 8.85483L1.44039 8.85354L4.96668 5.33815C5.30653 4.99386 5.7685 4.79662 6.2524 4.78972L6.26553 4.78963L12.9014 4.78962L13.8479 3.84308C16.9187 0.772319 20.0546 0.770617 21.4678 0.975145C21.8617 1.02914 22.2271 1.21053 22.5083 1.4917C22.7894 1.77284 22.9708 2.13821 23.0248 2.53199C23.2294 3.94517 23.2278 7.08119 20.1569 10.1521L19.2107 11.0983V17.7338L19.2106 17.7469C19.2037 18.2308 19.0067 18.6933 18.6624 19.0331L15.1456 22.5608C14.9095 22.7966 14.6137 22.964 14.29 23.0449C13.9663 23.1259 13.6267 23.1174 13.3074 23.0204C12.9881 22.9235 12.7011 22.7417 12.4771 22.4944C12.2533 22.2473 12.1006 21.9441 12.0355 21.6171L11.1783 17.3417L6.65869 12.822L4.34847 12.3589L2.38351 11.965C2.05664 11.8998 1.75272 11.747 1.50564 11.5232C1.25835 11.2992 1.07653 11.0122 0.979561 10.6929C0.882595 10.3736 0.874125 10.034 0.955057 9.7103C1.03599 9.38659 1.20328 9.09092 1.43909 8.85483ZM6.8186 10.8724L2.94619 10.096L6.32006 6.73268H10.9583L6.8186 10.8724ZM15.2219 5.21703C17.681 2.75787 20.0783 2.75376 21.1124 2.8876C21.2462 3.92172 21.2421 6.31895 18.783 8.77812L12.0728 15.4883L8.51172 11.9272L15.2219 5.21703ZM13.9042 21.0538L13.1279 17.1811L17.2676 13.0414V17.68L13.9042 21.0538Z" fill-rule="evenodd"></path><path d="M9.31827 18.3446C9.45046 17.8529 9.17864 17.3369 8.68945 17.1724C8.56178 17.1294 8.43145 17.1145 8.30512 17.1243C8.10513 17.1398 7.91519 17.2172 7.76181 17.3434C7.62613 17.455 7.51905 17.6048 7.45893 17.7835C6.97634 19.2186 5.77062 19.9878 4.52406 20.4029C4.08525 20.549 3.6605 20.644 3.29471 20.7053C3.35607 20.3395 3.45098 19.9148 3.59711 19.476C4.01221 18.2294 4.78141 17.0237 6.21648 16.5411C6.39528 16.481 6.54504 16.3739 6.65665 16.2382C6.85126 16.0016 6.92988 15.678 6.84417 15.3647C6.83922 15.3466 6.83373 15.3286 6.82767 15.3106C6.74106 15.053 6.55701 14.8557 6.33037 14.7459C6.10949 14.6389 5.84816 14.615 5.59715 14.6994C5.47743 14.7397 5.36103 14.7831 5.24786 14.8294C3.22626 15.6569 2.2347 17.4173 1.75357 18.8621C1.49662 19.6337 1.36993 20.3554 1.30679 20.8818C1.27505 21.1464 1.25893 21.3654 1.25072 21.5213C1.24662 21.5993 1.24448 21.6618 1.24337 21.7066L1.243 21.7226L1.24235 21.7605L1.2422 21.7771L1.24217 21.7827L1.24217 21.7856C1.24217 22.3221 1.67703 22.7579 2.2137 22.7579L2.2155 22.7579L2.22337 22.7578L2.23956 22.7577C2.25293 22.7575 2.27096 22.7572 2.29338 22.7567C2.33821 22.7555 2.40073 22.7534 2.47876 22.7493C2.63466 22.7411 2.85361 22.725 3.11822 22.6932C3.64462 22.6301 4.36636 22.5034 5.13797 22.2464C6.58274 21.7653 8.3431 20.7738 9.17063 18.7522C9.21696 18.639 9.26037 18.5226 9.30064 18.4029C9.30716 18.3835 9.31304 18.364 9.31827 18.3446Z"></path></svg>提示</p><div class="starlight-aside__content"><p>如果工具调用不工作，请尝试增大 Ollama 中的 <code dir="auto">num_ctx</code> 值。建议从 16k - 32k 左右开始。</p></div></aside>


* * *
### Ollama Cloud
要在 OpenCode 中使用 Ollama Cloud：
  1. 前往 [https://ollama.com/](https://ollama.com/) 登录或创建账户。
  2. 导航到 **Settings** > **Keys** ，点击 **Add API Key** 生成新的 API 密钥。
  3. 复制 API 密钥以便在 OpenCode 中使用。
  4. 执行 `/connect` 命令并搜索 **Ollama Cloud** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  5. 输入你的 Ollama Cloud API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  6. **重要** ：在 OpenCode 中使用云端模型之前，必须先将模型信息拉取到本地：


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">ollama</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">pull</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">gpt-oss:20b-cloud</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="ollama pull gpt-oss:20b-cloud" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  7. 执行 `/models` 命令选择你的 Ollama Cloud 模型。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### OpenAI
我们建议注册 [ChatGPT Plus 或 Pro](https://chatgpt.com/pricing)。
  1. 注册完成后，执行 `/connect` 命令并选择 OpenAI。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  2. 你可以选择 **ChatGPT Plus/Pro** 选项，浏览器会自动打开并要求你进行身份验证。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ Select auth method</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│ ChatGPT Plus/Pro</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│ Manually enter API Key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ Select auth method││ ChatGPT Plus/Pro│ Manually enter API Key└" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 现在使用 `/models` 命令即可看到所有 OpenAI 模型。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


##### 使用 API 密钥
如果你已经有 API 密钥，可以选择 **Manually enter API Key** 并将其粘贴到终端中。
* * *
### OpenCode Zen
OpenCode Zen 是由 OpenCode 团队提供的经过测试和验证的模型列表。[了解更多](/docs/zen)。
  1. 登录 **[OpenCode Zen](https://opencode.ai/auth)** 并点击 **Create API Key** 。
  2. 执行 `/connect` 命令并搜索 **OpenCode Zen** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入你的 OpenCode API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择模型，例如 _Qwen 3 Coder 480B_ 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### OpenRouter
  1. 前往 [OpenRouter 仪表盘](https://openrouter.ai/settings/keys)，点击 **Create API Key** 并复制密钥。
  2. 执行 `/connect` 命令并搜索 OpenRouter。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入该提供商的 API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 默认已预加载了许多 OpenRouter 模型，执行 `/models` 命令选择你想要的模型。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


你也可以通过 OpenCode 配置添加更多模型。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"provider"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"openrouter"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"models"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">        </span><span style="--0:#004ba0;--1:#81bcff">"somecoolnewmodel"</span><span style="--0:#24292E;--1:#E1E4E8">: {}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "provider": {    "openrouter": {      "models": {        "somecoolnewmodel": {}      }    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  5. 你还可以通过 OpenCode 配置自定义模型。以下是指定提供商的示例：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"provider"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"openrouter"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"models"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#005CC5;--1:#79B8FF">"moonshotai/kimi-k2"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">          </span><span style="--0:#005CC5;--1:#79B8FF">"options"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">            </span><span style="--0:#005CC5;--1:#79B8FF">"provider"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">              </span><span style="--0:#005CC5;--1:#79B8FF">"order"</span><span style="--0:#24292E;--1:#E1E4E8">: [</span><span style="--0:#032F62;--1:#9ECBFF">"baseten"</span><span style="--0:#24292E;--1:#E1E4E8">],</span></div></div><div class="ec-line"><div class="code"><span class="indent">              </span><span style="--0:#005CC5;--1:#79B8FF">"allow_fallbacks"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#005CC5;--1:#79B8FF">false</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">            </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">          </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">        </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "provider": {    "openrouter": {      "models": {        "moonshotai/kimi-k2": {          "options": {            "provider": {              "order": ["baseten"],              "allow_fallbacks": false            }          }        }      }    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### SAP AI Core
SAP AI Core 通过统一平台提供对来自 OpenAI、Anthropic、Google、Amazon、Meta、Mistral 和 AI21 的 40+ 模型的访问。
  1. 前往 [SAP BTP Cockpit](https://account.hana.ondemand.com/)，导航到你的 SAP AI Core 服务实例，并创建服务密钥。


<aside aria-label="提示" class="starlight-aside starlight-aside--tip"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path clip-rule="evenodd" d="M1.43909 8.85483L1.44039 8.85354L4.96668 5.33815C5.30653 4.99386 5.7685 4.79662 6.2524 4.78972L6.26553 4.78963L12.9014 4.78962L13.8479 3.84308C16.9187 0.772319 20.0546 0.770617 21.4678 0.975145C21.8617 1.02914 22.2271 1.21053 22.5083 1.4917C22.7894 1.77284 22.9708 2.13821 23.0248 2.53199C23.2294 3.94517 23.2278 7.08119 20.1569 10.1521L19.2107 11.0983V17.7338L19.2106 17.7469C19.2037 18.2308 19.0067 18.6933 18.6624 19.0331L15.1456 22.5608C14.9095 22.7966 14.6137 22.964 14.29 23.0449C13.9663 23.1259 13.6267 23.1174 13.3074 23.0204C12.9881 22.9235 12.7011 22.7417 12.4771 22.4944C12.2533 22.2473 12.1006 21.9441 12.0355 21.6171L11.1783 17.3417L6.65869 12.822L4.34847 12.3589L2.38351 11.965C2.05664 11.8998 1.75272 11.747 1.50564 11.5232C1.25835 11.2992 1.07653 11.0122 0.979561 10.6929C0.882595 10.3736 0.874125 10.034 0.955057 9.7103C1.03599 9.38659 1.20328 9.09092 1.43909 8.85483ZM6.8186 10.8724L2.94619 10.096L6.32006 6.73268H10.9583L6.8186 10.8724ZM15.2219 5.21703C17.681 2.75787 20.0783 2.75376 21.1124 2.8876C21.2462 3.92172 21.2421 6.31895 18.783 8.77812L12.0728 15.4883L8.51172 11.9272L15.2219 5.21703ZM13.9042 21.0538L13.1279 17.1811L17.2676 13.0414V17.68L13.9042 21.0538Z" fill-rule="evenodd"></path><path d="M9.31827 18.3446C9.45046 17.8529 9.17864 17.3369 8.68945 17.1724C8.56178 17.1294 8.43145 17.1145 8.30512 17.1243C8.10513 17.1398 7.91519 17.2172 7.76181 17.3434C7.62613 17.455 7.51905 17.6048 7.45893 17.7835C6.97634 19.2186 5.77062 19.9878 4.52406 20.4029C4.08525 20.549 3.6605 20.644 3.29471 20.7053C3.35607 20.3395 3.45098 19.9148 3.59711 19.476C4.01221 18.2294 4.78141 17.0237 6.21648 16.5411C6.39528 16.481 6.54504 16.3739 6.65665 16.2382C6.85126 16.0016 6.92988 15.678 6.84417 15.3647C6.83922 15.3466 6.83373 15.3286 6.82767 15.3106C6.74106 15.053 6.55701 14.8557 6.33037 14.7459C6.10949 14.6389 5.84816 14.615 5.59715 14.6994C5.47743 14.7397 5.36103 14.7831 5.24786 14.8294C3.22626 15.6569 2.2347 17.4173 1.75357 18.8621C1.49662 19.6337 1.36993 20.3554 1.30679 20.8818C1.27505 21.1464 1.25893 21.3654 1.25072 21.5213C1.24662 21.5993 1.24448 21.6618 1.24337 21.7066L1.243 21.7226L1.24235 21.7605L1.2422 21.7771L1.24217 21.7827L1.24217 21.7856C1.24217 22.3221 1.67703 22.7579 2.2137 22.7579L2.2155 22.7579L2.22337 22.7578L2.23956 22.7577C2.25293 22.7575 2.27096 22.7572 2.29338 22.7567C2.33821 22.7555 2.40073 22.7534 2.47876 22.7493C2.63466 22.7411 2.85361 22.725 3.11822 22.6932C3.64462 22.6301 4.36636 22.5034 5.13797 22.2464C6.58274 21.7653 8.3431 20.7738 9.17063 18.7522C9.21696 18.639 9.26037 18.5226 9.30064 18.4029C9.30716 18.3835 9.31304 18.364 9.31827 18.3446Z"></path></svg>提示</p><div class="starlight-aside__content"><p>服务密钥是一个包含 <code dir="auto">clientid</code>、<code dir="auto">clientsecret</code>、<code dir="auto">url</code> 和 <code dir="auto">serviceurls.AI_API_URL</code> 的 JSON 对象。你可以在 BTP Cockpit 的 <strong>Services</strong> &gt; <strong>Instances and Subscriptions</strong> 下找到你的 AI Core 实例。</p></div></aside>


  2. 执行 `/connect` 命令并搜索 **SAP AI Core** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入你的服务密钥 JSON。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ Service key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ Service key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


或者设置 `AICORE_SERVICE_KEY` 环境变量：


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">AICORE_SERVICE_KEY</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#032F62;--1:#9ECBFF">'{"clientid":"...","clientsecret":"...","url":"...","serviceurls":{"AI_API_URL":"..."}}'</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#6F42C1;--1:#B392F0">opencode</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="AICORE_SERVICE_KEY='{&quot;clientid&quot;:&quot;...&quot;,&quot;clientsecret&quot;:&quot;...&quot;,&quot;url&quot;:&quot;...&quot;,&quot;serviceurls&quot;:{&quot;AI_API_URL&quot;:&quot;...&quot;}}' opencode" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


或者添加到你的 bash 配置文件中：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">~/.bash_profile</span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#BF3441;--1:#F97583">export</span><span style="--0:#24292E;--1:#E1E4E8"> AICORE_SERVICE_KEY</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#032F62;--1:#9ECBFF">'{"clientid":"...","clientsecret":"...","url":"...","serviceurls":{"AI_API_URL":"..."}}'</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="export AICORE_SERVICE_KEY='{&quot;clientid&quot;:&quot;...&quot;,&quot;clientsecret&quot;:&quot;...&quot;,&quot;url&quot;:&quot;...&quot;,&quot;serviceurls&quot;:{&quot;AI_API_URL&quot;:&quot;...&quot;}}'" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 可选：设置部署 ID 和资源组：


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">AICORE_DEPLOYMENT_ID</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#032F62;--1:#9ECBFF">your-deployment-id</span><span style="--0:#24292E;--1:#E1E4E8"> AICORE_RESOURCE_GROUP</span><span style="--0:#BF3441;--1:#F97583">=</span><span style="--0:#032F62;--1:#9ECBFF">your-resource-group</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#6F42C1;--1:#B392F0">opencode</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="AICORE_DEPLOYMENT_ID=your-deployment-id AICORE_RESOURCE_GROUP=your-resource-group opencode" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>

 

<aside aria-label="注意" class="starlight-aside starlight-aside--note"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M12 11C11.7348 11 11.4804 11.1054 11.2929 11.2929C11.1054 11.4804 11 11.7348 11 12V16C11 16.2652 11.1054 16.5196 11.2929 16.7071C11.4804 16.8946 11.7348 17 12 17C12.2652 17 12.5196 16.8946 12.7071 16.7071C12.8946 16.5196 13 16.2652 13 16V12C13 11.7348 12.8946 11.4804 12.7071 11.2929C12.5196 11.1054 12.2652 11 12 11ZM12.38 7.08C12.1365 6.97998 11.8635 6.97998 11.62 7.08C11.4973 7.12759 11.3851 7.19896 11.29 7.29C11.2017 7.3872 11.1306 7.49882 11.08 7.62C11.024 7.73868 10.9966 7.86882 11 8C10.9992 8.13161 11.0245 8.26207 11.0742 8.38391C11.124 8.50574 11.1973 8.61656 11.29 8.71C11.3872 8.79833 11.4988 8.86936 11.62 8.92C11.7715 8.98224 11.936 9.00632 12.099 8.99011C12.2619 8.97391 12.4184 8.91792 12.5547 8.82707C12.691 8.73622 12.8029 8.61328 12.8805 8.46907C12.9582 8.32486 12.9992 8.16378 13 8C12.9963 7.73523 12.8927 7.48163 12.71 7.29C12.6149 7.19896 12.5028 7.12759 12.38 7.08ZM12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM12 20C10.4178 20 8.87104 19.5308 7.55544 18.6518C6.23985 17.7727 5.21447 16.5233 4.60897 15.0615C4.00347 13.5997 3.84504 11.9911 4.15372 10.4393C4.4624 8.88743 5.22433 7.46197 6.34315 6.34315C7.46197 5.22433 8.88743 4.4624 10.4393 4.15372C11.9911 3.84504 13.5997 4.00346 15.0615 4.60896C16.5233 5.21447 17.7727 6.23984 18.6518 7.55544C19.5308 8.87103 20 10.4177 20 12C20 14.1217 19.1572 16.1566 17.6569 17.6569C16.1566 19.1571 14.1217 20 12 20Z"></path></svg>注意</p><div class="starlight-aside__content"><p>这些设置是可选的，应根据你的 SAP AI Core 配置进行设置。</p></div></aside>


  5. 执行 `/models` 命令从 40+ 个可用模型中进行选择。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### STACKIT
STACKIT AI Model Serving 提供完全托管的主权托管环境，专注于 Llama、Mistral 和 Qwen 等大语言模型，在欧洲基础设施上实现最大程度的数据主权。
  1. 前往 [STACKIT Portal](https://portal.stackit.cloud)，导航到 **AI Model Serving** ，为你的项目创建认证令牌。


<aside aria-label="提示" class="starlight-aside starlight-aside--tip"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path clip-rule="evenodd" d="M1.43909 8.85483L1.44039 8.85354L4.96668 5.33815C5.30653 4.99386 5.7685 4.79662 6.2524 4.78972L6.26553 4.78963L12.9014 4.78962L13.8479 3.84308C16.9187 0.772319 20.0546 0.770617 21.4678 0.975145C21.8617 1.02914 22.2271 1.21053 22.5083 1.4917C22.7894 1.77284 22.9708 2.13821 23.0248 2.53199C23.2294 3.94517 23.2278 7.08119 20.1569 10.1521L19.2107 11.0983V17.7338L19.2106 17.7469C19.2037 18.2308 19.0067 18.6933 18.6624 19.0331L15.1456 22.5608C14.9095 22.7966 14.6137 22.964 14.29 23.0449C13.9663 23.1259 13.6267 23.1174 13.3074 23.0204C12.9881 22.9235 12.7011 22.7417 12.4771 22.4944C12.2533 22.2473 12.1006 21.9441 12.0355 21.6171L11.1783 17.3417L6.65869 12.822L4.34847 12.3589L2.38351 11.965C2.05664 11.8998 1.75272 11.747 1.50564 11.5232C1.25835 11.2992 1.07653 11.0122 0.979561 10.6929C0.882595 10.3736 0.874125 10.034 0.955057 9.7103C1.03599 9.38659 1.20328 9.09092 1.43909 8.85483ZM6.8186 10.8724L2.94619 10.096L6.32006 6.73268H10.9583L6.8186 10.8724ZM15.2219 5.21703C17.681 2.75787 20.0783 2.75376 21.1124 2.8876C21.2462 3.92172 21.2421 6.31895 18.783 8.77812L12.0728 15.4883L8.51172 11.9272L15.2219 5.21703ZM13.9042 21.0538L13.1279 17.1811L17.2676 13.0414V17.68L13.9042 21.0538Z" fill-rule="evenodd"></path><path d="M9.31827 18.3446C9.45046 17.8529 9.17864 17.3369 8.68945 17.1724C8.56178 17.1294 8.43145 17.1145 8.30512 17.1243C8.10513 17.1398 7.91519 17.2172 7.76181 17.3434C7.62613 17.455 7.51905 17.6048 7.45893 17.7835C6.97634 19.2186 5.77062 19.9878 4.52406 20.4029C4.08525 20.549 3.6605 20.644 3.29471 20.7053C3.35607 20.3395 3.45098 19.9148 3.59711 19.476C4.01221 18.2294 4.78141 17.0237 6.21648 16.5411C6.39528 16.481 6.54504 16.3739 6.65665 16.2382C6.85126 16.0016 6.92988 15.678 6.84417 15.3647C6.83922 15.3466 6.83373 15.3286 6.82767 15.3106C6.74106 15.053 6.55701 14.8557 6.33037 14.7459C6.10949 14.6389 5.84816 14.615 5.59715 14.6994C5.47743 14.7397 5.36103 14.7831 5.24786 14.8294C3.22626 15.6569 2.2347 17.4173 1.75357 18.8621C1.49662 19.6337 1.36993 20.3554 1.30679 20.8818C1.27505 21.1464 1.25893 21.3654 1.25072 21.5213C1.24662 21.5993 1.24448 21.6618 1.24337 21.7066L1.243 21.7226L1.24235 21.7605L1.2422 21.7771L1.24217 21.7827L1.24217 21.7856C1.24217 22.3221 1.67703 22.7579 2.2137 22.7579L2.2155 22.7579L2.22337 22.7578L2.23956 22.7577C2.25293 22.7575 2.27096 22.7572 2.29338 22.7567C2.33821 22.7555 2.40073 22.7534 2.47876 22.7493C2.63466 22.7411 2.85361 22.725 3.11822 22.6932C3.64462 22.6301 4.36636 22.5034 5.13797 22.2464C6.58274 21.7653 8.3431 20.7738 9.17063 18.7522C9.21696 18.639 9.26037 18.5226 9.30064 18.4029C9.30716 18.3835 9.31304 18.364 9.31827 18.3446Z"></path></svg>提示</p><div class="starlight-aside__content"><p>你需要先拥有 STACKIT 客户账户、用户账户和项目，才能创建认证令牌。</p></div></aside>


  2. 执行 `/connect` 命令并搜索 **STACKIT** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入你的 STACKIT AI Model Serving 认证令牌。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择模型，例如 _Qwen3-VL 235B_ 或 _Llama 3.3 70B_ 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### OVHcloud AI Endpoints
  1. 前往 [OVHcloud 管理面板](https://ovh.com/manager)。导航到 `Public Cloud` 部分，`AI & Machine Learning` > `AI Endpoints`，在 `API Keys` 标签页中点击 **Create a new API key** 。
  2. 执行 `/connect` 命令并搜索 **OVHcloud AI Endpoints** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入你的 OVHcloud AI Endpoints API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择模型，例如 _gpt-oss-120b_ 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### Scaleway
要在 OpenCode 中使用 [Scaleway Generative APIs](https://www.scaleway.com/en/docs/generative-apis/)：
  1. 前往 [Scaleway Console IAM 设置](https://console.scaleway.com/iam/api-keys)生成新的 API 密钥。
  2. 执行 `/connect` 命令并搜索 **Scaleway** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入你的 Scaleway API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择模型，例如 _devstral-2-123b-instruct-2512_ 或 _gpt-oss-120b_ 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### Together AI
  1. 前往 [Together AI 控制台](https://api.together.ai)，创建账户并点击 **Add Key** 。
  2. 执行 `/connect` 命令并搜索 **Together AI** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入你的 Together AI API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择模型，例如 _Kimi K2 Instruct_ 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### Venice AI
  1. 前往 [Venice AI 控制台](https://venice.ai)，创建账户并生成 API 密钥。
  2. 执行 `/connect` 命令并搜索 **Venice AI** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入你的 Venice AI API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择模型，例如 _Llama 3.3 70B_ 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### Vercel AI Gateway
Vercel AI Gateway 允许你通过统一端点访问来自 OpenAI、Anthropic、Google、xAI 等提供商的模型。模型按原价提供，不额外加价。
  1. 前往 [Vercel 仪表盘](https://vercel.com/)，导航到 **AI Gateway** 标签页，点击 **API keys** 创建新的 API 密钥。
  2. 执行 `/connect` 命令并搜索 **Vercel AI Gateway** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入你的 Vercel AI Gateway API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择模型。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


你也可以通过 OpenCode 配置自定义模型。以下是指定提供商路由顺序的示例。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"provider"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"vercel"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"models"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#005CC5;--1:#79B8FF">"anthropic/claude-sonnet-4"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">          </span><span style="--0:#005CC5;--1:#79B8FF">"options"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">            </span><span style="--0:#005CC5;--1:#79B8FF">"order"</span><span style="--0:#24292E;--1:#E1E4E8">: [</span><span style="--0:#032F62;--1:#9ECBFF">"anthropic"</span><span style="--0:#24292E;--1:#E1E4E8">, </span><span style="--0:#032F62;--1:#9ECBFF">"vertex"</span><span style="--0:#24292E;--1:#E1E4E8">]</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">          </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">        </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "provider": {    "vercel": {      "models": {        "anthropic/claude-sonnet-4": {          "options": {            "order": ["anthropic", "vertex"]          }        }      }    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


一些常用的路由选项：
选项| 描述  
---|---  
`order`| 提供商尝试顺序  
`only`| 限制为特定提供商  
`zeroDataRetention`| 仅使用具有零数据留存策略的提供商  
* * *
### xAI
  1. 前往 [xAI 控制台](https://console.x.ai/)，创建账户并生成 API 密钥。
  2. 执行 `/connect` 命令并搜索 **xAI** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入你的 xAI API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择模型，例如 _Grok Beta_ 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### Z.AI
  1. 前往 [Z.AI API 控制台](https://z.ai/manage-apikey/apikey-list)，创建账户并点击 **Create a new API key** 。
  2. 执行 `/connect` 命令并搜索 **Z.AI** 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


如果你订阅了 **GLM Coding Plan** ，请选择 **Z.AI Coding Plan** 。
  3. 输入你的 Z.AI API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 执行 `/models` 命令选择模型，例如 _GLM-4.7_ 。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### ZenMux
  1. 前往 [ZenMux 仪表盘](https://zenmux.ai/settings/keys)，点击 **Create API Key** 并复制密钥。
  2. 执行 `/connect` 命令并搜索 ZenMux。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/connect</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/connect" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  3. 输入该提供商的 API 密钥。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">┌ API key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">└ enter</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="┌ API key││└ enter" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 默认已预加载了许多 ZenMux 模型，执行 `/models` 命令选择你想要的模型。


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="txt"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


你也可以通过 OpenCode 配置添加更多模型。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"provider"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"zenmux"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"models"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">        </span><span style="--0:#004ba0;--1:#81bcff">"somecoolnewmodel"</span><span style="--0:#24292E;--1:#E1E4E8">: {}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "provider": {    "zenmux": {      "models": {        "somecoolnewmodel": {}      }    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
## 自定义提供商
要添加 `/connect` 命令中未列出的任何 **OpenAI 兼容** 提供商：


<aside aria-label="提示" class="starlight-aside starlight-aside--tip"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path clip-rule="evenodd" d="M1.43909 8.85483L1.44039 8.85354L4.96668 5.33815C5.30653 4.99386 5.7685 4.79662 6.2524 4.78972L6.26553 4.78963L12.9014 4.78962L13.8479 3.84308C16.9187 0.772319 20.0546 0.770617 21.4678 0.975145C21.8617 1.02914 22.2271 1.21053 22.5083 1.4917C22.7894 1.77284 22.9708 2.13821 23.0248 2.53199C23.2294 3.94517 23.2278 7.08119 20.1569 10.1521L19.2107 11.0983V17.7338L19.2106 17.7469C19.2037 18.2308 19.0067 18.6933 18.6624 19.0331L15.1456 22.5608C14.9095 22.7966 14.6137 22.964 14.29 23.0449C13.9663 23.1259 13.6267 23.1174 13.3074 23.0204C12.9881 22.9235 12.7011 22.7417 12.4771 22.4944C12.2533 22.2473 12.1006 21.9441 12.0355 21.6171L11.1783 17.3417L6.65869 12.822L4.34847 12.3589L2.38351 11.965C2.05664 11.8998 1.75272 11.747 1.50564 11.5232C1.25835 11.2992 1.07653 11.0122 0.979561 10.6929C0.882595 10.3736 0.874125 10.034 0.955057 9.7103C1.03599 9.38659 1.20328 9.09092 1.43909 8.85483ZM6.8186 10.8724L2.94619 10.096L6.32006 6.73268H10.9583L6.8186 10.8724ZM15.2219 5.21703C17.681 2.75787 20.0783 2.75376 21.1124 2.8876C21.2462 3.92172 21.2421 6.31895 18.783 8.77812L12.0728 15.4883L8.51172 11.9272L15.2219 5.21703ZM13.9042 21.0538L13.1279 17.1811L17.2676 13.0414V17.68L13.9042 21.0538Z" fill-rule="evenodd"></path><path d="M9.31827 18.3446C9.45046 17.8529 9.17864 17.3369 8.68945 17.1724C8.56178 17.1294 8.43145 17.1145 8.30512 17.1243C8.10513 17.1398 7.91519 17.2172 7.76181 17.3434C7.62613 17.455 7.51905 17.6048 7.45893 17.7835C6.97634 19.2186 5.77062 19.9878 4.52406 20.4029C4.08525 20.549 3.6605 20.644 3.29471 20.7053C3.35607 20.3395 3.45098 19.9148 3.59711 19.476C4.01221 18.2294 4.78141 17.0237 6.21648 16.5411C6.39528 16.481 6.54504 16.3739 6.65665 16.2382C6.85126 16.0016 6.92988 15.678 6.84417 15.3647C6.83922 15.3466 6.83373 15.3286 6.82767 15.3106C6.74106 15.053 6.55701 14.8557 6.33037 14.7459C6.10949 14.6389 5.84816 14.615 5.59715 14.6994C5.47743 14.7397 5.36103 14.7831 5.24786 14.8294C3.22626 15.6569 2.2347 17.4173 1.75357 18.8621C1.49662 19.6337 1.36993 20.3554 1.30679 20.8818C1.27505 21.1464 1.25893 21.3654 1.25072 21.5213C1.24662 21.5993 1.24448 21.6618 1.24337 21.7066L1.243 21.7226L1.24235 21.7605L1.2422 21.7771L1.24217 21.7827L1.24217 21.7856C1.24217 22.3221 1.67703 22.7579 2.2137 22.7579L2.2155 22.7579L2.22337 22.7578L2.23956 22.7577C2.25293 22.7575 2.27096 22.7572 2.29338 22.7567C2.33821 22.7555 2.40073 22.7534 2.47876 22.7493C2.63466 22.7411 2.85361 22.725 3.11822 22.6932C3.64462 22.6301 4.36636 22.5034 5.13797 22.2464C6.58274 21.7653 8.3431 20.7738 9.17063 18.7522C9.21696 18.639 9.26037 18.5226 9.30064 18.4029C9.30716 18.3835 9.31304 18.364 9.31827 18.3446Z"></path></svg>提示</p><div class="starlight-aside__content"><p>你可以在 OpenCode 中使用任何 OpenAI 兼容的提供商。大多数现代 AI 提供商都提供 OpenAI 兼容的 API。</p></div></aside>


  1. 执行 `/connect` 命令，向下滚动到 **Other** 。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">$</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">/connect</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">┌</span><span style="--0:#24292E;--1:#E1E4E8">  </span><span style="--0:#032F62;--1:#9ECBFF">Add</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">credential</span></div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">◆</span><span style="--0:#24292E;--1:#E1E4E8">  </span><span style="--0:#032F62;--1:#9ECBFF">Select</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">provider</span></div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">│</span><span style="--0:#24292E;--1:#E1E4E8">  </span><span style="--0:#032F62;--1:#9ECBFF">...</span></div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">│</span><span style="--0:#24292E;--1:#E1E4E8">  </span><span style="--0:#032F62;--1:#9ECBFF">●</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">Other</span></div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">└</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="$ /connect┌  Add credential│◆  Select provider│  ...│  ● Other└" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  2. 输入该提供商的唯一 ID。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">$</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">/connect</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">┌</span><span style="--0:#24292E;--1:#E1E4E8">  </span><span style="--0:#032F62;--1:#9ECBFF">Add</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">credential</span></div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">◇</span><span style="--0:#24292E;--1:#E1E4E8">  </span><span style="--0:#032F62;--1:#9ECBFF">Enter</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">provider</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">id</span></div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">│</span><span style="--0:#24292E;--1:#E1E4E8">  </span><span style="--0:#032F62;--1:#9ECBFF">myprovider</span></div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">└</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="$ /connect┌  Add credential│◇  Enter provider id│  myprovider└" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>

 

<aside aria-label="注意" class="starlight-aside starlight-aside--note"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M12 11C11.7348 11 11.4804 11.1054 11.2929 11.2929C11.1054 11.4804 11 11.7348 11 12V16C11 16.2652 11.1054 16.5196 11.2929 16.7071C11.4804 16.8946 11.7348 17 12 17C12.2652 17 12.5196 16.8946 12.7071 16.7071C12.8946 16.5196 13 16.2652 13 16V12C13 11.7348 12.8946 11.4804 12.7071 11.2929C12.5196 11.1054 12.2652 11 12 11ZM12.38 7.08C12.1365 6.97998 11.8635 6.97998 11.62 7.08C11.4973 7.12759 11.3851 7.19896 11.29 7.29C11.2017 7.3872 11.1306 7.49882 11.08 7.62C11.024 7.73868 10.9966 7.86882 11 8C10.9992 8.13161 11.0245 8.26207 11.0742 8.38391C11.124 8.50574 11.1973 8.61656 11.29 8.71C11.3872 8.79833 11.4988 8.86936 11.62 8.92C11.7715 8.98224 11.936 9.00632 12.099 8.99011C12.2619 8.97391 12.4184 8.91792 12.5547 8.82707C12.691 8.73622 12.8029 8.61328 12.8805 8.46907C12.9582 8.32486 12.9992 8.16378 13 8C12.9963 7.73523 12.8927 7.48163 12.71 7.29C12.6149 7.19896 12.5028 7.12759 12.38 7.08ZM12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM12 20C10.4178 20 8.87104 19.5308 7.55544 18.6518C6.23985 17.7727 5.21447 16.5233 4.60897 15.0615C4.00347 13.5997 3.84504 11.9911 4.15372 10.4393C4.4624 8.88743 5.22433 7.46197 6.34315 6.34315C7.46197 5.22433 8.88743 4.4624 10.4393 4.15372C11.9911 3.84504 13.5997 4.00346 15.0615 4.60896C16.5233 5.21447 17.7727 6.23984 18.6518 7.55544C19.5308 8.87103 20 10.4177 20 12C20 14.1217 19.1572 16.1566 17.6569 17.6569C16.1566 19.1571 14.1217 20 12 20Z"></path></svg>注意</p><div class="starlight-aside__content"><p>请选择一个容易记住的 ID，你将在配置文件中使用它。</p></div></aside>


  3. 输入该提供商的 API 密钥。


<div class="expressive-code"><figure class="frame is-terminal not-content"><figcaption class="header"><span class="title"></span></figcaption><pre data-language="bash"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">$</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">/connect</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">┌</span><span style="--0:#24292E;--1:#E1E4E8">  </span><span style="--0:#032F62;--1:#9ECBFF">Add</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">credential</span></div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">▲</span><span style="--0:#24292E;--1:#E1E4E8">  </span><span style="--0:#032F62;--1:#9ECBFF">This</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">only</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">stores</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">a</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">credential</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">for</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">myprovider</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">-</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">you</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">will</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">need</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">to</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">configure</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">it</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">in</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">opencode.json,</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">check</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">the</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">docs</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">for</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">examples.</span></div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">│</span></div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">◇</span><span style="--0:#24292E;--1:#E1E4E8">  </span><span style="--0:#032F62;--1:#9ECBFF">Enter</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">your</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">API</span><span style="--0:#24292E;--1:#E1E4E8"> </span><span style="--0:#032F62;--1:#9ECBFF">key</span></div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">│</span><span style="--0:#24292E;--1:#E1E4E8">  </span><span style="--0:#032F62;--1:#9ECBFF">sk-...</span></div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">└</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="$ /connect┌  Add credential│▲  This only stores a credential for myprovider - you will need to configure it in opencode.json, check the docs for examples.│◇  Enter your API key│  sk-...└" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


  4. 在项目目录中创建或更新 `opencode.json` 文件：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"provider"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><mark><span style="--0:#004ba0;--1:#81bcff">"myprovider"</span></mark><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"npm"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"@ai-sdk/openai-compatible"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"name"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"My AI ProviderDisplay Name"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"options"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">        </span><span style="--0:#004ba0;--1:#81bcff">"baseURL"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://api.myprovider.com/v1"</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">},</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">      </span><span style="--0:#004ba0;--1:#81bcff">"models"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">        </span><span style="--0:#004ba0;--1:#81bcff">"my-model-name"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">          </span><span style="--0:#004ba0;--1:#81bcff">"name"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"My Model Display Name"</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">        </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "provider": {    "myprovider": {      "npm": "@ai-sdk/openai-compatible",      "name": "My AI ProviderDisplay Name",      "options": {        "baseURL": "https://api.myprovider.com/v1"      },      "models": {        "my-model-name": {          "name": "My Model Display Name"        }      }    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


以下是配置选项说明：
     * **npm** ：要使用的 AI SDK 包，对于 OpenAI 兼容的提供商使用 `@ai-sdk/openai-compatible`（适用于 `/v1/chat/completions`）。如果你的提供商/模型走 `/v1/responses`，请使用 `@ai-sdk/openai`。
     * **name** ：在 UI 中显示的名称。
     * **models** ：可用模型。
     * **options.baseURL** ：API 端点 URL。
     * **options.apiKey** ：可选，如果不使用 auth 认证，可直接设置 API 密钥。
     * **options.headers** ：可选，设置自定义请求头。
更多高级选项请参见下面的示例。
  5. 执行 `/models` 命令，你自定义的提供商和模型将出现在选择列表中。


* * *
##### 示例
以下是设置 `apiKey`、`headers` 和模型 `limit` 选项的示例。


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"provider"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"myprovider"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"npm"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"@ai-sdk/openai-compatible"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"name"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"My AI ProviderDisplay Name"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"options"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#005CC5;--1:#79B8FF">"baseURL"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://api.myprovider.com/v1"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">        </span><span style="--0:#004ba0;--1:#81bcff">"apiKey"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"{env:ANTHROPIC_API_KEY}"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#005CC5;--1:#79B8FF">"headers"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">          </span><span style="--0:#004ba0;--1:#81bcff">"Authorization"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"Bearer custom-token"</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">        </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">},</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"models"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#005CC5;--1:#79B8FF">"my-model-name"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">          </span><span style="--0:#005CC5;--1:#79B8FF">"name"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"My Model Display Name"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">          </span><span style="--0:#004ba0;--1:#81bcff">"limit"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">            </span><span style="--0:#004ba0;--1:#81bcff">"context"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#004ba0;--1:#81bcff">200000</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent">            </span><span style="--0:#004ba0;--1:#81bcff">"output"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#004ba0;--1:#81bcff">65536</span></div></div><div class="ec-line highlight mark"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">          </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">        </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "provider": {    "myprovider": {      "npm": "@ai-sdk/openai-compatible",      "name": "My AI ProviderDisplay Name",      "options": {        "baseURL": "https://api.myprovider.com/v1",        "apiKey": "{env:ANTHROPIC_API_KEY}",        "headers": {          "Authorization": "Bearer custom-token"        }      },      "models": {        "my-model-name": {          "name": "My Model Display Name",          "limit": {            "context": 200000,            "output": 65536          }        }      }    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


配置详情：
  * **apiKey** ：使用 `env` 变量语法设置，[了解更多](/docs/config#env-vars)。
  * **headers** ：随每个请求发送的自定义请求头。
  * **limit.context** ：模型接受的最大输入 Token 数。
  * **limit.output** ：模型可生成的最大 Token 数。


`limit` 字段让 OpenCode 了解你还剩余多少上下文空间。标准提供商会自动从 models.dev 拉取这些信息。
* * *
## 故障排除
如果你在配置提供商时遇到问题，请检查以下几点：
  1. **检查认证设置** ：运行 `opencode auth list` 查看该提供商的凭据是否已添加到配置中。
这不适用于 Amazon Bedrock 等依赖环境变量进行认证的提供商。
  2. 对于自定义提供商，请检查 OpenCode 配置并确认：
     * `/connect` 命令中使用的提供商 ID 与 OpenCode 配置中的 ID 一致。
     * 使用了正确的 npm 包。例如，Cerebras 应使用 `@ai-sdk/cerebras`。对于其他所有 OpenAI 兼容的提供商，使用 `@ai-sdk/openai-compatible`（`/v1/chat/completions`）；如果模型走 `/v1/responses`，请使用 `@ai-sdk/openai`。同一 provider 混用时，可在模型下设置 `provider.npm` 覆盖默认值。
     * `options.baseURL` 字段中的 API 端点地址正确。