import requests
from bs4 import BeautifulSoup, Tag
import html2text
import os
import re
import time
import uuid

BASE_URL = "https://opencode.ai"

PAGES = [
    ("/docs/zh-cn/", "intro", "简介", "入门"),
    ("/docs/zh-cn/config/", "config", "配置", "基础"),
    ("/docs/zh-cn/providers/", "providers", "提供商", "基础"),
    ("/docs/zh-cn/network/", "network", "网络", "基础"),
    ("/docs/zh-cn/enterprise/", "enterprise", "企业版", "基础"),
    ("/docs/zh-cn/troubleshooting/", "troubleshooting", "故障排除", "基础"),
    ("/docs/zh-cn/windows-wsl", "windows-wsl", "Windows", "基础"),
    ("/docs/zh-cn/go/", "go", "Go", "使用"),
    ("/docs/zh-cn/tui/", "tui", "TUI", "使用"),
    ("/docs/zh-cn/cli/", "cli", "CLI", "使用"),
    ("/docs/zh-cn/web/", "web", "Web", "使用"),
    ("/docs/zh-cn/ide/", "ide", "IDE", "使用"),
    ("/docs/zh-cn/zen/", "zen", "Zen", "使用"),
    ("/docs/zh-cn/share/", "share", "分享", "使用"),
    ("/docs/zh-cn/github/", "github", "GitHub", "使用"),
    ("/docs/zh-cn/gitlab/", "gitlab", "GitLab", "使用"),
    ("/docs/zh-cn/tools/", "tools", "工具", "配置"),
    ("/docs/zh-cn/rules/", "rules", "规则", "配置"),
    ("/docs/zh-cn/agents/", "agents", "代理", "配置"),
    ("/docs/zh-cn/models/", "models", "模型", "配置"),
    ("/docs/zh-cn/themes/", "themes", "主题", "配置"),
    ("/docs/zh-cn/keybinds/", "keybinds", "快捷键", "配置"),
    ("/docs/zh-cn/commands/", "commands", "命令", "配置"),
    ("/docs/zh-cn/formatters/", "formatters", "格式化工具", "配置"),
    ("/docs/zh-cn/permissions/", "permissions", "权限", "配置"),
    ("/docs/zh-cn/policies/", "policies", "Policies", "配置"),
    ("/docs/zh-cn/lsp/", "lsp", "LSP 服务器", "配置"),
    ("/docs/zh-cn/mcp-servers/", "mcp-servers", "MCP 服务器", "配置"),
    ("/docs/zh-cn/acp/", "acp", "ACP 支持", "配置"),
    ("/docs/zh-cn/skills/", "skills", "代理技能", "配置"),
    ("/docs/zh-cn/references/", "references", "References", "配置"),
    ("/docs/zh-cn/custom-tools/", "custom-tools", "自定义工具", "配置"),
    ("/docs/zh-cn/sdk/", "sdk", "SDK", "开发"),
    ("/docs/zh-cn/server/", "server", "服务器", "开发"),
    ("/docs/zh-cn/plugins/", "plugins", "插件", "开发"),
    ("/docs/zh-cn/ecosystem/", "ecosystem", "生态系统", "开发"),
]

ORDER_MAP = {slug: i+1 for i, (_, slug, _, _) in enumerate(PAGES)}
OUTPUT_DIR = "src/content/docs"

CB_START = "%%%CB_START_"
CB_END = "_CB_END%%%"
TB_START = "%%%TB_START_"
TB_END = "_TB_END%%%"
PR_START = "%%%PR_START_"
PR_END = "_PR_END%%%"

code_blocks_store = {}
tab_blocks_store = {}
protected_store = {}

def make_html2text():
    h = html2text.HTML2Text()
    h.body_width = 0
    h.skip_internal_links = False
    h.ignore_links = False
    h.ignore_images = True
    h.ignore_emphasis = False
    h.protect_links = True
    h.unicode_snob = True
    h.single_line_break = True
    h.mark_code = False
    h.wrap_links = False
    h.use_automatic_links = False
    h.images_to_alt = False
    return h

def extract_protected_blocks(soup):
    """Extract starlight-aside and expressive-code as protected HTML blocks."""
    for aside in soup.find_all('aside', class_=lambda c: c and 'starlight-aside' in c):
        uid = str(uuid.uuid4())[:8]
        protected_store[uid] = str(aside)
        placeholder = soup.new_tag('span')
        placeholder.string = f"{PR_START}{uid}{PR_END}"
        aside.replace_with(placeholder)
    
    for ec in soup.find_all(class_='expressive-code'):
        uid = str(uuid.uuid4())[:8]
        protected_store[uid] = str(ec)
        placeholder = soup.new_tag('span')
        placeholder.string = f"{PR_START}{uid}{PR_END}"
        ec.replace_with(placeholder)

def restore_protected_blocks(text):
    def replacer(match):
        uid = match.group(1)
        html = protected_store.get(uid)
        if html:
            return '\n\n' + html + '\n\n'
        return ''
    text = re.sub(re.escape(PR_START) + r'([a-f0-9]+)' + re.escape(PR_END), replacer, text)
    return text

def extract_tab_blocks(soup):
    for tabs in soup.find_all('starlight-tabs'):
        panels = tabs.find_all(role='tabpanel')
        tab_links = tabs.find_all(role='tab')
        
        tabs_content = []
        for pi, panel in enumerate(panels):
            label = "tab"
            for link in tab_links:
                link_href = link.get('href', '')
                panel_id = panel.get('id', '')
                if link_href and panel_id and link_href.endswith(panel_id):
                    label = link.get_text(strip=True)
                    break
            
            inner = panel.decode_contents().strip()
            tabs_content.append({'label': label, 'content': inner})
        
        uid = str(uuid.uuid4())[:8]
        tab_blocks_store[uid] = tabs_content
        
        placeholder = soup.new_tag('span')
        placeholder.string = f"{TB_START}{uid}{TB_END}"
        tabs.replace_with(placeholder)

def convert_aside_to_callout(soup):
    """Convert starlight-aside elements to callout-style blocks."""
    for aside in soup.find_all('aside', class_=lambda c: c and 'starlight-aside' in c):
        # Get the type (tip, note, danger, caution, etc.)
        classes = aside.get('class', [])
        atype = 'note'
        for c in classes:
            if 'starlight-aside--' in c:
                atype = c.replace('starlight-aside--', '')
                break
        
        # Get the title
        title_el = aside.find(class_='starlight-aside__title')
        title_text = title_el.get_text(strip=True) if title_el else atype.capitalize()
        
        # Get the content
        content_el = aside.find(class_='starlight-aside__content')
        content_html = str(content_el) if content_el else aside.decode_contents()
        
        # Create a callout blockquote
        type_emoji = ''
        if atype == 'tip':
            type_emoji = '💡'
        elif atype == 'note':
            type_emoji = '📝'
        elif atype == 'danger':
            type_emoji = '⚠️'
        elif atype == 'caution':
            type_emoji = '⚠️'
        elif atype == 'success':
            type_emoji = '✅'
        
        # Replace aside with a styled blockquote (html2text will convert to > prefix)
        # Post-processing will convert these to styled HTML divs
        new_html = f'<blockquote class="callout callout-{atype}"><p class="callout-title">{type_emoji} <strong>{title_text}</strong></p>{content_html}</blockquote>'
        new_soup = BeautifulSoup(new_html, 'html.parser')
        aside.replace_with(new_soup)

def fix_links(soup):
    for a in soup.find_all('a', href=True):
        href = a['href']
        if re.match(r'^/docs/zh-cn/', href):
            a['href'] = href.replace('/docs/zh-cn/', '/docs/').rstrip('/')
        elif href == '/' or href.startswith('/#'):
            a['href'] = 'https://opencode.ai' + href

def clean_content_html(soup):
    # Keep aside SVGs (icon), remove other SVGs
    for tag in soup.find_all(['script', 'link', 'style', 'nav', 'header', 'footer', 'template']):
        tag.decompose()
    
    # Remove only SVGs NOT inside starlight-aside
    for svg in soup.find_all('svg'):
        if not svg.find_parent(class_=lambda c: c and 'starlight-aside' in c):
            svg.decompose()
    
    # Remove 'copy' spans (but not inside starlight-aside or expressive-code)
    for tag in soup.find_all(class_=['sr-only']):
        tag.decompose()
    
    # Remove expressive-code script/link elements (we serve our own)
    for ec in soup.find_all(class_='expressive-code'):
        for link in ec.find_all('link'):
            link.decompose()
        for script in ec.find_all('script'):
            script.decompose()
    
    extract_protected_blocks(soup)
    extract_tab_blocks(soup)
    
    for tag in soup.find_all(class_=['tablist-wrapper']):
        tag.decompose()
    
    for img in soup.find_all('img'):
        img.decompose()
    
    for badge in soup.find_all(class_='sl-badge'):
        badge.decompose()
    
    fix_links(soup)
    
    return soup

def extract_content(soup):
    content_div = soup.find('div', class_='sl-markdown-content')
    if not content_div:
        return None
    
    content_div = clean_content_html(content_div)
    return str(content_div)

def restore_code_blocks(text):
    def replacer(match):
        uid = match.group(1)
        info = code_blocks_store.get(uid)
        if not info:
            return ''
        lang = info['lang']
        code = info['code']
        return f"\n```{lang}\n{code}\n```\n"
    text = re.sub(re.escape(CB_START) + r'([a-f0-9]+)' + re.escape(CB_END), replacer, text)
    return text

def restore_tab_blocks(text):
    def replacer(match):
        uid = match.group(1)
        tabs = tab_blocks_store.get(uid)
        if not tabs:
            return ''
        
        parts = []
        h = make_html2text()
        for tab in tabs:
            label = tab['label']
            content = tab['content']
            sub_md = h.handle(content).strip()
            parts.append(f"**{label}:**\n\n{sub_md}")
        
        return '\n\n---\n\n'.join(parts)
    
    text = re.sub(re.escape(TB_START) + r'([a-f0-9]+)' + re.escape(TB_END), replacer, text)
    return text

def post_process_markdown(text):
    lines = text.split('\n')
    result = []
    
    for line in lines:
        stripped = line.strip()
        
        if stripped == '<!-- -->':
            continue
        if re.match(r'^\[//\]: # \(.*\)$', stripped):
            continue
        
        # Remove stray h1 headings that are actually command descriptions
        # Pattern: # description + command (no space between text and command)
        if re.match(r'^#\s+(opencode\s|查看|调试)', stripped):
            text_content = stripped.lstrip('# ')
            result.append(f'`{text_content}`')
            continue
        
        result.append(line)
    
    text = '\n'.join(result)
    
    # Fix link angle brackets: ](<url>) -> ](url)
    text = re.sub(r'\]\(<([^>]+)>\)', r'](\1)', text)
    # Fix internal links: https://opencode.ai/docs/... -> /docs/...
    text = re.sub(r'\]\(https://opencode\.ai/docs/([^)]+)\)', r'](/docs/\1)', text)
    
    # Fix callout blockquote: ensure nice formatting
    # Convert "> 💡 **提示**" style to proper callout format
    text = re.sub(r'> 💡 \*\*提示\*\*', r'> 💡 **提示**', text)
    
    # Remove excessive blank lines
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    
    # Fix headings - strip link syntax from headings
    text = re.sub(r'^(#{1,6})\s+\[([^\]]+)\]\(<#[^>]+>\)', r'\1 \2', text, flags=re.MULTILINE)
    text = re.sub(r'^(#{1,6})\s+\[([^\]]+)\]\(#[^)]+\)', r'\1 \2', text, flags=re.MULTILINE)
    
    # Fix SVG viewBox attribute
    text = text.replace('viewbox="', 'viewBox="')
    
    return text.strip()

def extract_title(soup):
    h1 = soup.find('h1')
    if h1:
        return h1.get_text(strip=True)
    title_tag = soup.find('title')
    if title_tag:
        return title_tag.get_text(strip=True).replace(' | OpenCode', '')
    return ''

def extract_description(soup):
    desc = soup.find('p', class_='page-description')
    if desc:
        return desc.get_text(strip=True)
    meta = soup.find('meta', attrs={'name': 'description'})
    if meta and meta.get('content'):
        return meta['content']
    return ''

def fetch_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/120.0.0.0 Safari/537.36'
    }
    for attempt in range(3):
        try:
            resp = requests.get(url, headers=headers, timeout=60)
            resp.encoding = 'utf-8'
            resp.raise_for_status()
            return resp.text
        except Exception as e:
            if attempt < 2:
                print(f"  Retry {attempt+1} after error: {e}")
                time.sleep(2)
            else:
                raise

def process_page(url_path, slug, title_override, category):
    global code_blocks_store, tab_blocks_store
    code_blocks_store = {}
    tab_blocks_store = {}
    
    url = BASE_URL + url_path
    print(f"Fetching: {url}")
    try:
        html = fetch_page(url)
    except Exception as e:
        print(f"  ERROR fetching: {e}")
        return None

    soup = BeautifulSoup(html, 'html.parser')
    title = title_override or extract_title(soup)
    description = extract_description(soup)
    content_html = extract_content(soup)

    if not content_html:
        print(f"  WARNING: No content found for {url}")
        return None

    h = make_html2text()
    content_md = h.handle(content_html)
    content_md = restore_protected_blocks(content_md)
    content_md = restore_tab_blocks(content_md)
    content_md = post_process_markdown(content_md)
    
    order = ORDER_MAP.get(slug, 99)

    title_esc = title.replace("'", "\\'")
    desc_esc = description.replace("'", "\\'")

    frontmatter = f"""---
title: '{title_esc}'
description: '{desc_esc}'
category: '{category}'
order: {order}
slug: '{slug}'
---

"""
    return frontmatter + content_md

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for f in os.listdir(OUTPUT_DIR):
        if f.endswith('.md'):
            os.remove(os.path.join(OUTPUT_DIR, f))

    for url_path, slug, title, category in PAGES:
        result = process_page(url_path, slug, title, category)
        if result:
            fname = f"{ORDER_MAP[slug]:02d}-{slug}.md"
            fpath = os.path.join(OUTPUT_DIR, fname)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"  Saved: {fpath}")
        else:
            print(f"  SKIPPED: {slug}")

        time.sleep(1)

    print("\nDone! All docs fetched.")

if __name__ == '__main__':
    main()
