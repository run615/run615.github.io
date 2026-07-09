---
title: 'Zen'
description: '由 OpenCode 提供的精选模型列表。'
category: 'OpenCode 开发手册'
order: 13
slug: 'opencode/zen'
---

OpenCode Zen 是由 OpenCode 团队提供的一组经过测试和验证的模型。
Zen 的工作方式与 OpenCode 中的任何其他提供商相同。你登录 OpenCode Zen 并获取 API 密钥。它是**完全可选的** ，即使不用它，你也可以照常使用 OpenCode。
* * *
## 背景
现在市面上有大量模型，但其中只有少数模型适合作为编码代理使用。此外，大多数提供商的配置方式差异很大，因此你获得的性能和质量也会非常不同。


<aside aria-label="提示" class="starlight-aside starlight-aside--tip"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path clip-rule="evenodd" d="M1.43909 8.85483L1.44039 8.85354L4.96668 5.33815C5.30653 4.99386 5.7685 4.79662 6.2524 4.78972L6.26553 4.78963L12.9014 4.78962L13.8479 3.84308C16.9187 0.772319 20.0546 0.770617 21.4678 0.975145C21.8617 1.02914 22.2271 1.21053 22.5083 1.4917C22.7894 1.77284 22.9708 2.13821 23.0248 2.53199C23.2294 3.94517 23.2278 7.08119 20.1569 10.1521L19.2107 11.0983V17.7338L19.2106 17.7469C19.2037 18.2308 19.0067 18.6933 18.6624 19.0331L15.1456 22.5608C14.9095 22.7966 14.6137 22.964 14.29 23.0449C13.9663 23.1259 13.6267 23.1174 13.3074 23.0204C12.9881 22.9235 12.7011 22.7417 12.4771 22.4944C12.2533 22.2473 12.1006 21.9441 12.0355 21.6171L11.1783 17.3417L6.65869 12.822L4.34847 12.3589L2.38351 11.965C2.05664 11.8998 1.75272 11.747 1.50564 11.5232C1.25835 11.2992 1.07653 11.0122 0.979561 10.6929C0.882595 10.3736 0.874125 10.034 0.955057 9.7103C1.03599 9.38659 1.20328 9.09092 1.43909 8.85483ZM6.8186 10.8724L2.94619 10.096L6.32006 6.73268H10.9583L6.8186 10.8724ZM15.2219 5.21703C17.681 2.75787 20.0783 2.75376 21.1124 2.8876C21.2462 3.92172 21.2421 6.31895 18.783 8.77812L12.0728 15.4883L8.51172 11.9272L15.2219 5.21703ZM13.9042 21.0538L13.1279 17.1811L17.2676 13.0414V17.68L13.9042 21.0538Z" fill-rule="evenodd"></path><path d="M9.31827 18.3446C9.45046 17.8529 9.17864 17.3369 8.68945 17.1724C8.56178 17.1294 8.43145 17.1145 8.30512 17.1243C8.10513 17.1398 7.91519 17.2172 7.76181 17.3434C7.62613 17.455 7.51905 17.6048 7.45893 17.7835C6.97634 19.2186 5.77062 19.9878 4.52406 20.4029C4.08525 20.549 3.6605 20.644 3.29471 20.7053C3.35607 20.3395 3.45098 19.9148 3.59711 19.476C4.01221 18.2294 4.78141 17.0237 6.21648 16.5411C6.39528 16.481 6.54504 16.3739 6.65665 16.2382C6.85126 16.0016 6.92988 15.678 6.84417 15.3647C6.83922 15.3466 6.83373 15.3286 6.82767 15.3106C6.74106 15.053 6.55701 14.8557 6.33037 14.7459C6.10949 14.6389 5.84816 14.615 5.59715 14.6994C5.47743 14.7397 5.36103 14.7831 5.24786 14.8294C3.22626 15.6569 2.2347 17.4173 1.75357 18.8621C1.49662 19.6337 1.36993 20.3554 1.30679 20.8818C1.27505 21.1464 1.25893 21.3654 1.25072 21.5213C1.24662 21.5993 1.24448 21.6618 1.24337 21.7066L1.243 21.7226L1.24235 21.7605L1.2422 21.7771L1.24217 21.7827L1.24217 21.7856C1.24217 22.3221 1.67703 22.7579 2.2137 22.7579L2.2155 22.7579L2.22337 22.7578L2.23956 22.7577C2.25293 22.7575 2.27096 22.7572 2.29338 22.7567C2.33821 22.7555 2.40073 22.7534 2.47876 22.7493C2.63466 22.7411 2.85361 22.725 3.11822 22.6932C3.64462 22.6301 4.36636 22.5034 5.13797 22.2464C6.58274 21.7653 8.3431 20.7738 9.17063 18.7522C9.21696 18.639 9.26037 18.5226 9.30064 18.4029C9.30716 18.3835 9.31304 18.364 9.31827 18.3446Z"></path></svg>提示</p><div class="starlight-aside__content"><p>我们测试了一组与 OpenCode 配合良好的精选模型和提供商。</p></div></aside>


所以，如果你通过 OpenRouter 之类的服务使用模型，你无法确定自己拿到的是否是目标模型的最佳版本。
为了解决这个问题，我们做了几件事：
  1. 我们测试了一组选定的模型，并与它们的团队讨论了如何以最佳方式运行这些模型。
  2. 然后我们与几家提供商合作，确保这些模型被正确提供。
  3. 最后，我们对模型和提供商的组合进行了基准测试，并整理出了一份我们认为值得推荐的列表。


OpenCode Zen 是一个 AI 网关，让你可以访问这些模型。
* * *
## 工作原理
OpenCode Zen 的工作方式与 OpenCode 中的任何其他提供商相同。
  1. 登录 **[OpenCode Zen](https://opencode.ai/auth)** ，添加你的账单信息，然后复制你的 API 密钥。
  2. 在 TUI 中运行 `/connect` 命令，选择 OpenCode Zen，然后粘贴你的 API 密钥。
  3. 在 TUI 中运行 `/models`，查看我们推荐的模型列表。


你按请求付费，也可以向账户充值。
* * *
## 端点
你也可以通过以下 API 端点访问我们的模型。
模型| 模型 ID| 端点| AI SDK 包  
---|---|---|---  
GPT 5.5| gpt-5.5| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5.5 Pro| gpt-5.5-pro| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5.4| gpt-5.4| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5.4 Pro| gpt-5.4-pro| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5.4 Mini| gpt-5.4-mini| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5.4 Nano| gpt-5.4-nano| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5.3 Codex| gpt-5.3-codex| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5.3 Codex Spark| gpt-5.3-codex-spark| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5.2| gpt-5.2| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5.2 Codex| gpt-5.2-codex| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5.1| gpt-5.1| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5.1 Codex| gpt-5.1-codex| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5.1 Codex Max| gpt-5.1-codex-max| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5.1 Codex Mini| gpt-5.1-codex-mini| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5| gpt-5| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5 Codex| gpt-5-codex| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5 Nano| gpt-5-nano| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
Claude Fable 5| claude-fable-5| `https://opencode.ai/zen/v1/messages`| `@ai-sdk/anthropic`  
Claude Opus 4.8| claude-opus-4-8| `https://opencode.ai/zen/v1/messages`| `@ai-sdk/anthropic`  
Claude Opus 4.7| claude-opus-4-7| `https://opencode.ai/zen/v1/messages`| `@ai-sdk/anthropic`  
Claude Opus 4.6| claude-opus-4-6| `https://opencode.ai/zen/v1/messages`| `@ai-sdk/anthropic`  
Claude Opus 4.5| claude-opus-4-5| `https://opencode.ai/zen/v1/messages`| `@ai-sdk/anthropic`  
Claude Sonnet 5| claude-sonnet-5| `https://opencode.ai/zen/v1/messages`| `@ai-sdk/anthropic`  
Claude Sonnet 4.6| claude-sonnet-4-6| `https://opencode.ai/zen/v1/messages`| `@ai-sdk/anthropic`  
Claude Sonnet 4.5| claude-sonnet-4-5| `https://opencode.ai/zen/v1/messages`| `@ai-sdk/anthropic`  
Claude Haiku 4.5| claude-haiku-4-5| `https://opencode.ai/zen/v1/messages`| `@ai-sdk/anthropic`  
Gemini 3.5 Flash| gemini-3.5-flash| `https://opencode.ai/zen/v1/models/gemini-3.5-flash`| `@ai-sdk/google`  
Gemini 3.1 Pro| gemini-3.1-pro| `https://opencode.ai/zen/v1/models/gemini-3.1-pro`| `@ai-sdk/google`  
Gemini 3 Flash| gemini-3-flash| `https://opencode.ai/zen/v1/models/gemini-3-flash`| `@ai-sdk/google`  
Qwen3.7 Max| qwen3.7-max| `https://opencode.ai/zen/v1/messages`| `@ai-sdk/anthropic`  
Qwen3.7 Plus| qwen3.7-plus| `https://opencode.ai/zen/v1/messages`| `@ai-sdk/anthropic`  
Qwen3.6 Plus| qwen3.6-plus| `https://opencode.ai/zen/v1/messages`| `@ai-sdk/anthropic`  
Qwen3.5 Plus| qwen3.5-plus| `https://opencode.ai/zen/v1/messages`| `@ai-sdk/anthropic`  
DeepSeek V4 Pro| deepseek-v4-pro| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
DeepSeek V4 Flash| deepseek-v4-flash| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
MiniMax M3| minimax-m3| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
MiniMax M2.7| minimax-m2.7| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
MiniMax M2.5| minimax-m2.5| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
GLM 5.2| glm-5.2| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
GLM 5.1| glm-5.1| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
GLM 5| glm-5| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
Kimi K2.5| kimi-k2.5| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
Kimi K2.6| kimi-k2.6| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
Kimi K2.7 Code| kimi-k2.7-code| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
Grok 4.5| grok-4.5| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
Grok Build 0.1| grok-build-0.1| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
Big Pickle| big-pickle| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
MiMo-V2.5 Free| mimo-v2.5-free| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
North Mini Code Free| north-mini-code-free| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
Nemotron 3 Ultra Free| nemotron-3-ultra-free| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
DeepSeek V4 Flash Free| deepseek-v4-flash-free| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
在你的 OpenCode 配置中，[模型 ID](/docs/config/#models) 使用 `opencode/<model-id>` 格式。例如，对于 GPT 5.5，你需要在配置中使用 `opencode/gpt-5.5`。
* * *
### 模型
你可以从以下地址获取可用模型及其元数据的完整列表：


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="plaintext"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">https://opencode.ai/zen/v1/models</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="https://opencode.ai/zen/v1/models" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
## 定价
我们支持按量付费模式。以下是**每 1M tokens** 的价格。
模型| 输入| 输出| 缓存读取| 缓存写入  
---|---|---|---|---  
Big Pickle| Free| Free| Free| -  
DeepSeek V4 Flash Free| Free| Free| Free| -  
MiMo-V2.5 Free| Free| Free| Free| -  
North Mini Code Free| Free| Free| Free| -  
Nemotron 3 Ultra Free| Free| Free| Free| -  
MiniMax M3| $0.30| $1.20| $0.06| -  
MiniMax M2.7| $0.30| $1.20| $0.06| -  
MiniMax M2.5| $0.30| $1.20| $0.06| -  
GLM 5.2| $1.40| $4.40| $0.26| -  
GLM 5.1| $1.40| $4.40| $0.26| -  
GLM 5| $1.00| $3.20| $0.20| -  
Kimi K2.7 Code| $0.95| $4.00| $0.19| -  
Kimi K2.6| $0.95| $4.00| $0.16| -  
Kimi K2.5| $0.60| $3.00| $0.10| -  
Qwen3.7 Max| $2.50| $7.50| $0.50| $3.125  
Qwen3.7 Plus| $0.40| $1.60| $0.04| $0.50  
Qwen3.6 Plus| $0.50| $3.00| $0.05| $0.625  
Qwen3.5 Plus| $0.20| $1.20| $0.02| $0.25  
DeepSeek V4 Pro| $1.74| $3.48| $0.145| -  
DeepSeek V4 Flash| $0.14| $0.28| $0.028| -  
Grok 4.5 (≤ 200K tokens)| $2.00| $6.00| $0.50| -  
Grok 4.5 (> 200K tokens)| $4.00| $12.00| $1.00| -  
Grok Build 0.1| $1.00| $2.00| $0.20| -  
Claude Fable 5| $10.00| $50.00| $1.00| $12.50  
Claude Opus 4.8| $5.00| $25.00| $0.50| $6.25  
Claude Opus 4.7| $5.00| $25.00| $0.50| $6.25  
Claude Opus 4.6| $5.00| $25.00| $0.50| $6.25  
Claude Opus 4.5| $5.00| $25.00| $0.50| $6.25  
Claude Sonnet 5| $2.00| $10.00| $0.20| $2.50  
Claude Sonnet 4.6| $3.00| $15.00| $0.30| $3.75  
Claude Sonnet 4.5 (≤ 200K tokens)| $3.00| $15.00| $0.30| $3.75  
Claude Sonnet 4.5 (> 200K tokens)| $6.00| $22.50| $0.60| $7.50  
Claude Haiku 4.5| $1.00| $5.00| $0.10| $1.25  
Gemini 3.5 Flash| $1.50| $9.00| $0.15| -  
Gemini 3.1 Pro (≤ 200K tokens)| $2.00| $12.00| $0.20| -  
Gemini 3.1 Pro (> 200K tokens)| $4.00| $18.00| $0.40| -  
Gemini 3 Flash| $0.50| $3.00| $0.05| -  
GPT 5.5 (≤ 272K tokens)| $5.00| $30.00| $0.50| -  
GPT 5.5 (> 272K tokens)| $10.00| $45.00| $1.00| -  
GPT 5.5 Pro| $30.00| $180.00| $30.00| -  
GPT 5.4 (≤ 272K tokens)| $2.50| $15.00| $0.25| -  
GPT 5.4 (> 272K tokens)| $5.00| $22.50| $0.50| -  
GPT 5.4 Pro| $30.00| $180.00| $30.00| -  
GPT 5.4 Mini| $0.75| $4.50| $0.075| -  
GPT 5.4 Nano| $0.20| $1.25| $0.02| -  
GPT 5.3 Codex Spark| $1.75| $14.00| $0.175| -  
GPT 5.3 Codex| $1.75| $14.00| $0.175| -  
GPT 5.2| $1.75| $14.00| $0.175| -  
GPT 5.2 Codex| $1.75| $14.00| $0.175| -  
GPT 5.1| $1.07| $8.50| $0.107| -  
GPT 5.1 Codex| $1.07| $8.50| $0.107| -  
GPT 5.1 Codex Max| $1.25| $10.00| $0.125| -  
GPT 5.1 Codex Mini| $0.25| $2.00| $0.025| -  
GPT 5| $1.07| $8.50| $0.107| -  
GPT 5 Codex| $1.07| $8.50| $0.107| -  
GPT 5 Nano| $0.05| $0.40| $0.005| -  
你可能会在使用记录中看到 _Claude Haiku 3.5_ 。这是一个[低成本模型](/docs/config/#models)，用于生成会话标题。


<aside aria-label="注意" class="starlight-aside starlight-aside--note"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M12 11C11.7348 11 11.4804 11.1054 11.2929 11.2929C11.1054 11.4804 11 11.7348 11 12V16C11 16.2652 11.1054 16.5196 11.2929 16.7071C11.4804 16.8946 11.7348 17 12 17C12.2652 17 12.5196 16.8946 12.7071 16.7071C12.8946 16.5196 13 16.2652 13 16V12C13 11.7348 12.8946 11.4804 12.7071 11.2929C12.5196 11.1054 12.2652 11 12 11ZM12.38 7.08C12.1365 6.97998 11.8635 6.97998 11.62 7.08C11.4973 7.12759 11.3851 7.19896 11.29 7.29C11.2017 7.3872 11.1306 7.49882 11.08 7.62C11.024 7.73868 10.9966 7.86882 11 8C10.9992 8.13161 11.0245 8.26207 11.0742 8.38391C11.124 8.50574 11.1973 8.61656 11.29 8.71C11.3872 8.79833 11.4988 8.86936 11.62 8.92C11.7715 8.98224 11.936 9.00632 12.099 8.99011C12.2619 8.97391 12.4184 8.91792 12.5547 8.82707C12.691 8.73622 12.8029 8.61328 12.8805 8.46907C12.9582 8.32486 12.9992 8.16378 13 8C12.9963 7.73523 12.8927 7.48163 12.71 7.29C12.6149 7.19896 12.5028 7.12759 12.38 7.08ZM12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM12 20C10.4178 20 8.87104 19.5308 7.55544 18.6518C6.23985 17.7727 5.21447 16.5233 4.60897 15.0615C4.00347 13.5997 3.84504 11.9911 4.15372 10.4393C4.4624 8.88743 5.22433 7.46197 6.34315 6.34315C7.46197 5.22433 8.88743 4.4624 10.4393 4.15372C11.9911 3.84504 13.5997 4.00346 15.0615 4.60896C16.5233 5.21447 17.7727 6.23984 18.6518 7.55544C19.5308 8.87103 20 10.4177 20 12C20 14.1217 19.1572 16.1566 17.6569 17.6569C16.1566 19.1571 14.1217 20 12 20Z"></path></svg>注意</p><div class="starlight-aside__content"><p>信用卡手续费按成本转嫁（每笔交易 4.4% + $0.30）；除此之外我们不会额外收费。</p></div></aside>


免费模型：
  * DeepSeek V4 Flash Free 目前在 OpenCode 上限时免费提供。团队正在利用这段时间收集反馈并改进模型。
  * MiMo-V2.5 Free 目前在 OpenCode 上限时免费提供。团队正在利用这段时间收集反馈并改进模型。
  * North Mini Code Free 目前在 OpenCode 上限时免费提供。团队正在利用这段时间收集反馈并改进模型。
  * Nemotron 3 Ultra Free 目前在 OpenCode 上限时免费提供。团队正在利用这段时间收集反馈并改进模型。
  * Big Pickle 是一个隐身模型，目前在 OpenCode 上限时免费提供。团队正在利用这段时间收集反馈并改进模型。


如果你有任何问题，请[联系我们](mailto:help@anoma.ly)。
* * *
### 自动充值
如果你的余额低于 $5，Zen 将自动充值 $20。
你可以更改自动充值金额，也可以完全禁用自动充值。
* * *
### 月度限额
你还可以为整个工作区以及团队中的每位成员设置月度使用限额。
例如，假设你将月度使用限额设置为 $20，那么 Zen 在一个月内的使用金额不会超过 $20。但如果你启用了自动充值，当余额低于 $5 时，Zen 最终向你收取的金额可能会超过 $20。
* * *
### 已弃用模型
模型| 弃用日期  
---|---  
GPT 5.2 Codex| July 23, 2026  
GPT 5.1 Codex| July 23, 2026  
GPT 5.1 Codex Max| July 23, 2026  
GPT 5.1 Codex Mini| July 23, 2026  
GPT 5 Codex| July 23, 2026  
Claude Opus 4.1| August 5, 2026  
Claude Sonnet 4| June 15, 2026  
Claude Haiku 3.5| February 16, 2026  
Gemini 3 Pro| March 9, 2026  
MiniMax M2.5| August 5, 2026  
MiniMax M2.1| March 15, 2026  
GLM 5| May 14, 2026  
GLM 4.7| March 15, 2026  
GLM 4.6| March 15, 2026  
Kimi K2.5| August 5, 2026  
Kimi K2 Thinking| March 6, 2026  
Kimi K2| March 6, 2026  
Qwen3 Coder 480B| February 6, 2026  
* * *
## 隐私
我们所有模型都托管在 US。我们的提供商遵循零保留政策，不会将你的数据用于模型训练，但以下情况除外：
  * Big Pickle：在免费期间，收集的数据可能会被用于改进模型。
  * DeepSeek V4 Flash Free：在免费期间，收集的数据可能会被用于改进模型。
  * MiMo-V2.5 Free：在免费期间，收集的数据可能会被用于改进模型。
  * North Mini Code Free：免费期间，所收集的数据可能会被保留并用于改进模型。请勿提交个人或机密数据。请参阅我们的[使用条款](https://cohere.com/terms-of-use)和[隐私政策](https://cohere.com/privacy)。
  * Nemotron 3 Ultra Free（NVIDIA 免费端点）：仅供试用 — 请勿提交个人或机密数据。出于安全目的以及为改进 NVIDIA 产品和服务，系统会记录你的使用情况。出于改进目的而记录的会话数据不会与你的身份或任何持久标识符相关联。有关我们数据处理实践的更多信息，请参阅我们的[隐私政策](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf)。与此端点进行交互，即表示你同意我们收集、记录和使用此类信息，并同意 [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf)。
  * OpenAI APIs：请求会根据 [OpenAI’s Data Policies](https://platform.openai.com/docs/guides/your-data) 保留 30 天。
  * Anthropic APIs：请求会根据 [Anthropic’s Data Policies](https://docs.anthropic.com/en/docs/claude-code/data-usage) 保留 30 天。


* * *
## 团队
Zen 也非常适合团队使用。你可以邀请队友、分配角色、管理团队使用的模型，等等。


<aside aria-label="注意" class="starlight-aside starlight-aside--note"><p aria-hidden="true" class="starlight-aside__title"><svg class="starlight-aside__icon" fill="currentColor" height="16" viewBox="0 0 24 24" width="16"><path d="M12 11C11.7348 11 11.4804 11.1054 11.2929 11.2929C11.1054 11.4804 11 11.7348 11 12V16C11 16.2652 11.1054 16.5196 11.2929 16.7071C11.4804 16.8946 11.7348 17 12 17C12.2652 17 12.5196 16.8946 12.7071 16.7071C12.8946 16.5196 13 16.2652 13 16V12C13 11.7348 12.8946 11.4804 12.7071 11.2929C12.5196 11.1054 12.2652 11 12 11ZM12.38 7.08C12.1365 6.97998 11.8635 6.97998 11.62 7.08C11.4973 7.12759 11.3851 7.19896 11.29 7.29C11.2017 7.3872 11.1306 7.49882 11.08 7.62C11.024 7.73868 10.9966 7.86882 11 8C10.9992 8.13161 11.0245 8.26207 11.0742 8.38391C11.124 8.50574 11.1973 8.61656 11.29 8.71C11.3872 8.79833 11.4988 8.86936 11.62 8.92C11.7715 8.98224 11.936 9.00632 12.099 8.99011C12.2619 8.97391 12.4184 8.91792 12.5547 8.82707C12.691 8.73622 12.8029 8.61328 12.8805 8.46907C12.9582 8.32486 12.9992 8.16378 13 8C12.9963 7.73523 12.8927 7.48163 12.71 7.29C12.6149 7.19896 12.5028 7.12759 12.38 7.08ZM12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 10.6868 21.7413 9.38642 21.2388 8.17317C20.7363 6.95991 19.9997 5.85752 19.0711 4.92893C18.1425 4.00035 17.0401 3.26375 15.8268 2.7612C14.6136 2.25866 13.3132 2 12 2ZM12 20C10.4178 20 8.87104 19.5308 7.55544 18.6518C6.23985 17.7727 5.21447 16.5233 4.60897 15.0615C4.00347 13.5997 3.84504 11.9911 4.15372 10.4393C4.4624 8.88743 5.22433 7.46197 6.34315 6.34315C7.46197 5.22433 8.88743 4.4624 10.4393 4.15372C11.9911 3.84504 13.5997 4.00346 15.0615 4.60896C16.5233 5.21447 17.7727 6.23984 18.6518 7.55544C19.5308 8.87103 20 10.4177 20 12C20 14.1217 19.1572 16.1566 17.6569 17.6569C16.1566 19.1571 14.1217 20 12 20Z"></path></svg>注意</p><div class="starlight-aside__content"><p>作为测试版的一部分，工作区目前对团队免费开放。</p></div></aside>


作为测试版的一部分，团队目前可以免费管理工作区。我们很快会分享更多定价细节。
* * *
### 角色
你可以邀请队友加入工作区并分配角色：
  * **Admin** ：管理模型、成员、API 密钥和账单
  * **Member** ：仅管理自己的 API 密钥


Admin 还可以为每位成员设置月度支出限额，以便控制成本。
* * *
### 模型访问
Admin 可以为工作区启用或禁用特定模型。向已禁用模型发出的请求会返回错误。
这在你想禁用会收集数据的模型时很有用。
* * *
### 自带密钥
你可以使用自己的 OpenAI 或 Anthropic API 密钥，同时仍然访问 Zen 中的其他模型。
当你使用自己的密钥时，tokens 由提供商直接计费，而不是由 Zen 计费。
例如，你的组织可能已经拥有 OpenAI 或 Anthropic 的密钥，并且你想使用它，而不是使用 Zen 提供的密钥。
* * *
## 目标
我们创建 OpenCode Zen，是为了：
  1. 为编码代理**基准测试** 最佳模型和提供商。
  2. 提供**最高质量** 的选项，而不是降低性能或路由到更便宜的提供商。
  3. 通过按成本销售来传递任何**降价** ；因此唯一的加价只是为了覆盖我们的处理费用。
  4. 保持**无锁定** ，允许你将它与任何其他编码代理一起使用。同时也始终允许你在 OpenCode 中使用任何其他提供商。