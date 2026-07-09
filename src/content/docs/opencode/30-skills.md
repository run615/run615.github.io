---
title: 代理技能'
description: '通过 SKILL.md 定义可复用的行为'
category: 'OpenCode 开发手册'
order: 30
slug: 'opencode/skills'
---

代理技能让 OpenCode 能够从你的仓库或主目录中发现可复用的指令。 技能通过原生的 `skill` 工具按需加载——代理可以查看可用技能，并在需要时加载完整内容。
* * *
## 放置文件
为每个技能名称创建一个文件夹，并在其中放入 `SKILL.md`。 OpenCode 会搜索以下位置：
  * 项目配置：`.opencode/skills/<name>/SKILL.md`
  * 全局配置：`~/.config/opencode/skills/<name>/SKILL.md`
  * 项目 Claude 兼容：`.claude/skills/<name>/SKILL.md`
  * 全局 Claude 兼容：`~/.claude/skills/<name>/SKILL.md`
  * 项目代理兼容：`.agents/skills/<name>/SKILL.md`
  * 全局代理兼容：`~/.agents/skills/<name>/SKILL.md`


* * *
## 了解发现机制
对于项目本地路径，OpenCode 会从当前工作目录向上遍历，直到到达 git 工作树根目录。 在此过程中，它会加载 `.opencode/` 中所有匹配的 `skills/*/SKILL.md`，以及匹配的 `.claude/skills/*/SKILL.md` 或 `.agents/skills/*/SKILL.md`。
全局定义也会从 `~/.config/opencode/skills/*/SKILL.md`、`~/.claude/skills/*/SKILL.md` 和 `~/.agents/skills/*/SKILL.md` 中加载。
* * *
## 编写 frontmatter
每个 `SKILL.md` 必须以 YAML frontmatter 开头。 仅识别以下字段：
  * `name`（必填）
  * `description`（必填）
  * `license`（可选）
  * `compatibility`（可选）
  * `metadata`（可选，字符串到字符串的映射）


未知的 frontmatter 字段会被忽略。
* * *
## 验证名称
`name` 必须满足：
  * 长度为 1–64 个字符
  * 仅包含小写字母和数字，可用单个连字符分隔
  * 不以 `-` 开头或结尾
  * 不包含连续的 `--`
  * 与包含 `SKILL.md` 的目录名称一致


等效的正则表达式：


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="text"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">^[a-z0-9]+(-[a-z0-9]+)*$</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="^[a-z0-9]+(-[a-z0-9]+)*$" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
## 遵循长度规则
`description` 必须为 1-1024 个字符。 请保持描述足够具体，以便代理能够正确选择。
* * *
## 使用示例
创建 `.opencode/skills/git-release/SKILL.md`，内容如下：


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="markdown"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">---</span></div></div><div class="ec-line"><div class="code"><span style="--0:#1E7734;--1:#85E89D">name</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">git-release</span></div></div><div class="ec-line"><div class="code"><span style="--0:#1E7734;--1:#85E89D">description</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">Create consistent releases and changelogs</span></div></div><div class="ec-line"><div class="code"><span style="--0:#1E7734;--1:#85E89D">license</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">MIT</span></div></div><div class="ec-line"><div class="code"><span style="--0:#1E7734;--1:#85E89D">compatibility</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">opencode</span></div></div><div class="ec-line"><div class="code"><span style="--0:#1E7734;--1:#85E89D">metadata</span><span style="--0:#24292E;--1:#E1E4E8">:</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#1E7734;--1:#85E89D">audience</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">maintainers</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#1E7734;--1:#85E89D">workflow</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">github</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">---</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#005CC5;--0fw:bold;--1:#79B8FF;--1fw:bold">## What I do</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#AE4B07;--1:#FFAB70">-</span><span style="--0:#24292E;--1:#E1E4E8"> Draft release notes from merged PRs</span></div></div><div class="ec-line"><div class="code"><span style="--0:#AE4B07;--1:#FFAB70">-</span><span style="--0:#24292E;--1:#E1E4E8"> Propose a version bump</span></div></div><div class="ec-line"><div class="code"><span style="--0:#AE4B07;--1:#FFAB70">-</span><span style="--0:#24292E;--1:#E1E4E8"> Provide a copy-pasteable </span><span style="--0:#005CC5;--1:#79B8FF">`gh release create`</span><span style="--0:#24292E;--1:#E1E4E8"> command</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#005CC5;--0fw:bold;--1:#79B8FF;--1fw:bold">## When to use me</span></div></div><div class="ec-line"><div class="code">
</div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">Use this when you are preparing a tagged release.</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">Ask clarifying questions if the target versioning scheme is unclear.</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="---name: git-releasedescription: Create consistent releases and changelogslicense: MITcompatibility: opencodemetadata:  audience: maintainers  workflow: github---## What I do- Draft release notes from merged PRs- Propose a version bump- Provide a copy-pasteable `gh release create` command## When to use meUse this when you are preparing a tagged release.Ask clarifying questions if the target versioning scheme is unclear." data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
## 识别工具描述
OpenCode 会在 `skill` 工具描述中列出可用技能。 每个条目包含技能名称和描述：


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="xml"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">&lt;</span><span style="--0:#1E7734;--1:#85E89D">available_skills</span><span style="--0:#24292E;--1:#E1E4E8">&gt;</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">&lt;</span><span style="--0:#1E7734;--1:#85E89D">skill</span><span style="--0:#24292E;--1:#E1E4E8">&gt;</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">&lt;</span><span style="--0:#1E7734;--1:#85E89D">name</span><span style="--0:#24292E;--1:#E1E4E8">&gt;git-release&lt;/</span><span style="--0:#1E7734;--1:#85E89D">name</span><span style="--0:#24292E;--1:#E1E4E8">&gt;</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">&lt;</span><span style="--0:#1E7734;--1:#85E89D">description</span><span style="--0:#24292E;--1:#E1E4E8">&gt;Create consistent releases and changelogs&lt;/</span><span style="--0:#1E7734;--1:#85E89D">description</span><span style="--0:#24292E;--1:#E1E4E8">&gt;</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">&lt;/</span><span style="--0:#1E7734;--1:#85E89D">skill</span><span style="--0:#24292E;--1:#E1E4E8">&gt;</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">&lt;/</span><span style="--0:#1E7734;--1:#85E89D">available_skills</span><span style="--0:#24292E;--1:#E1E4E8">&gt;</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="&lt;available_skills&gt;  &lt;skill&gt;    &lt;name&gt;git-release&lt;/name&gt;    &lt;description&gt;Create consistent releases and changelogs&lt;/description&gt;  &lt;/skill&gt;&lt;/available_skills&gt;" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


代理通过调用工具来加载技能：


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="plaintext"><code><div class="ec-line"><div class="code"><span style="--0:#24292e;--1:#e1e4e8">skill({ name: "git-release" })</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='skill({ name: "git-release" })' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
## 配置权限
在 `opencode.json` 中使用基于模式的权限来控制代理可以访问哪些技能：


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"permission"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"skill"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"*"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"allow"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"pr-review"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"allow"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"internal-*"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"deny"</span><span style="--0:#24292E;--1:#E1E4E8">,</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"experimental-*"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"ask"</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "permission": {    "skill": {      "*": "allow",      "pr-review": "allow",      "internal-*": "deny",      "experimental-*": "ask"    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>

 权限| 行为  
---|---  
`allow`| 技能立即加载  
`deny`| 对代理隐藏技能，拒绝访问  
`ask`| 加载前提示用户确认  
模式支持通配符：`internal-*` 可匹配 `internal-docs`、`internal-tools` 等。
* * *
## 按代理覆盖权限
为特定代理授予与全局默认值不同的权限。
**自定义代理** （在代理 frontmatter 中）：


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="yaml"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">---</span></div></div><div class="ec-line"><div class="code"><span style="--0:#1E7734;--1:#85E89D">permission</span><span style="--0:#24292E;--1:#E1E4E8">:</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#1E7734;--1:#85E89D">skill</span><span style="--0:#24292E;--1:#E1E4E8">:</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#032F62;--1:#9ECBFF">"documents-*"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"allow"</span></div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">---</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='---permission:  skill:    "documents-*": "allow"---' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


**内置代理** （在 `opencode.json` 中）：


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"agent"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"plan"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"permission"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#005CC5;--1:#79B8FF">"skill"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">          </span><span style="--0:#005CC5;--1:#79B8FF">"internal-*"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#032F62;--1:#9ECBFF">"allow"</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">        </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "agent": {    "plan": {      "permission": {        "skill": {          "internal-*": "allow"        }      }    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


* * *
## 禁用技能工具
为不需要使用技能的代理完全禁用技能功能：
**自定义代理** ：


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="yaml"><code><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">---</span></div></div><div class="ec-line"><div class="code"><span style="--0:#1E7734;--1:#85E89D">tools</span><span style="--0:#24292E;--1:#E1E4E8">:</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#1E7734;--1:#85E89D">skill</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#005CC5;--1:#79B8FF">false</span></div></div><div class="ec-line"><div class="code"><span style="--0:#6F42C1;--1:#B392F0">---</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code="---tools:  skill: false---" data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


**内置代理** ：


<div class="expressive-code"><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="json"><code><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">{</span></div></div><div class="ec-line"><div class="code"><span class="indent">  </span><span style="--0:#005CC5;--1:#79B8FF">"agent"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">    </span><span style="--0:#005CC5;--1:#79B8FF">"plan"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">      </span><span style="--0:#005CC5;--1:#79B8FF">"tools"</span><span style="--0:#24292E;--1:#E1E4E8">: {</span></div></div><div class="ec-line"><div class="code"><span class="indent">        </span><span style="--0:#005CC5;--1:#79B8FF">"skill"</span><span style="--0:#24292E;--1:#E1E4E8">: </span><span style="--0:#005CC5;--1:#79B8FF">false</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">      </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">    </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span class="indent"><span style="--0:#24292E;--1:#E1E4E8">  </span></span><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div><div class="ec-line"><div class="code"><span style="--0:#24292E;--1:#E1E4E8">}</span></div></div></code></pre><div class="copy"><div aria-live="polite"></div><button data-code='{  "agent": {    "plan": {      "tools": {        "skill": false      }    }  }}' data-copied="Copied!" title="Copy to clipboard"><div></div></button></div></figure></div>


禁用后，`<available_skills>` 部分将被完全省略。
* * *
## 排查加载问题
如果某个技能没有显示：
  1. 确认 `SKILL.md` 文件名全部为大写字母
  2. 检查 frontmatter 是否包含 `name` 和 `description`
  3. 确保技能名称在所有位置中唯一
  4. 检查权限设置——设为 `deny` 的技能会对代理隐藏