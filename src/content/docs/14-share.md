---
title: '分享'
description: '分享您的 OpenCode 对话。'
category: '使用'
order: 14
slug: 'share'
---

OpenCode 的分享功能允许您创建指向 OpenCode 对话的公开链接，方便与团队成员协作或向他人寻求帮助。


<aside aria-label="注意" class="starlight-aside starlight-aside--note"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M12 11C11.7348 11 11.4804 11.1054 11.2929 11.2929C11.1054 11.4804 11 11.7348 11 12V16C11 16.2652 11.1054 16.5196 11.2929 16.7071C11.4804 16.8946 11.7348 17 12 17C12.2652 17 12.5196 16.8946 12.7071 16.7071C12.8946 16.5196 13 16.2652 13 16V12C13 11.7348 12.8946 11.4804 12.7071 11.2929C12.5196 11.1054 12.2652 11 12 11ZM12.38 7.08C12.1365 6.97998 11.8635 6.97998 11.62 7.08C11.4973 7.12759 11.3851 7.19896 11.29 7.29C11.2017 7.3872 11.1306 7.49882 11.08 7.62C11.024 7.73868 10.9966 7.86882 11 8C10.9992 8.13161 11.0245 8.26207 11.0742 8.38391C11.124 8.50574 11.1973 8.61656 11.29 8.71C11.3872 8.79833 11.4988 8.86936 11.62 8.92C11.7715 8.98224 11.936 9.00632 12.099 8.99011C12.2619 8.97391 12.4184 8.91792 12.5547 8.82707C12.691 8.73622 12.8029 8.61328 12.8805 8.46907C12.9582 8.32486 12.9992 8.16378 13 8C12.9963 7.73523 12.8927 7.48163 12.71 7.29C12.6149 7.19896 12.5028 7.12759 12.38 7.08ZM12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM12 20C10.4178 20 8.87104 19.5308 7.55544 18.6518C6.23985 17.7727 5.21447 16.5233 4.60897 15.0615C4.00347 13.5997 3.84504 11.9911 4.15372 10.4393C4.4624 8.88743 5.22433 7.46197 6.34315 6.34315C7.46197 5.22433 8.88743 4.4624 10.4393 4.15372C11.9911 3.84504 13.5997 4.00346 15.0615 4.60896C16.5233 5.21447 17.7727 6.23984 18.6518 7.55544C19.5308 8.87103 20 10.4177 20 12C20 14.1217 19.1572 16.1566 17.6569 17.6569C16.1566 19.1571 14.1217 20 12 20Z"></path></svg>注意</p><div class="starlight-aside__content"><p>共享的对话对任何拥有链接的人都是公开可访问的。</p></div></aside>


* * *
## 工作原理
当您分享一段对话时，OpenCode 会：
  1. 为您的会话创建一个唯一的公开 URL
  2. 将您的对话历史同步到我们的服务器
  3. 通过可分享的链接使对话可访问 — `opncd.ai/s/<share-id>`


* * *
## 分享模式
OpenCode 支持三种分享模式，用于控制对话的共享方式：
* * *
### 手动模式（默认）
默认情况下，OpenCode 使用手动分享模式。会话不会自动共享，但您可以使用 `/share` 命令手动分享：


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="plaintext"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/share</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/share" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


这将生成一个唯一的 URL 并复制到您的剪贴板。
要在[配置文件](/docs/config)中显式设置手动模式：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"share"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"manual"</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "share": "manual"}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
### 自动分享
您可以在[配置文件](/docs/config)中将 `share` 选项设置为 `"auto"`，为所有新对话启用自动分享：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"share"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"auto"</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "share": "auto"}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


启用自动分享后，每个新对话都会自动共享并生成链接。
* * *
### 禁用
您可以在[配置文件](/docs/config)中将 `share` 选项设置为 `"disabled"`，完全禁用分享功能：


<div class="expressive-code"><figure class="frame has-title not-content"><figcaption class="header"><span class="title">opencode.json</span></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"$schema"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"https://opencode.ai/config.json"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"share"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"disabled"</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "$schema": "https://opencode.ai/config.json",  "share": "disabled"}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


要在团队中对特定项目强制执行此设置，请将其添加到项目的 `opencode.json` 文件中并提交到 Git。
* * *
## 取消分享
要停止分享对话并将其从公开访问中移除：


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="plaintext"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">/unshare</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="/unshare" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


这将移除分享链接并删除与该对话相关的数据。
* * *
## 隐私
分享对话时需要注意以下几点。
* * *
### 数据留存
共享的对话在您明确取消分享之前将一直保持可访问状态。这包括：
  * 完整的对话历史
  * 所有消息和回复
  * 会话元数据


* * *
### 建议
  * 仅分享不包含敏感信息的对话。
  * 分享前请检查对话内容。
  * 协作完成后请取消分享。
  * 避免分享包含专有代码或机密数据的对话。
  * 对于敏感项目，请完全禁用分享功能。


* * *
## 企业版
对于企业部署，分享功能可以：
  * 出于安全合规考虑**完全禁用**
  * **限制** 为仅通过 SSO 身份验证的用户可用
  * **自托管** 在您自己的基础设施上


[了解更多](/docs/enterprise)关于在您的组织中使用 OpenCode 的信息。