# -*- coding: utf-8 -*-
import os
import sys

# pyright tweaks
c = c  # type: ignore
config = config  # type: ignore

# ======================
# Config init
# ======================
config.load_autoconfig(False)

# ======================
# Color theme
# ======================
BACKGROUND = "#161C20"
FOREGROUND = "whitesmoke"
ACCENT_GREEN = "#6E8D6B"
ACCENT_RED = "#7B3D3C"
ACCENT_BLUE = "#24253C"
WARNING = "#EACA8C"
ERROR = "#4E0102"
TAB_BAR_DEFAULT = BACKGROUND
TAB_BAR_CHERRY = "#CD7685"
TAB_BAR_WHITE = "#F1F1F1"

# ======================
# Line args
# ======================
arg = "default"
theme = "orange"  # Значение по умолчанию

if len(sys.argv) > 1:
    if "tmp" in sys.argv[2].lower():
        arg = "tmp"
    elif "vite" in sys.argv[2].lower():
        theme = "cherry"

# ======================
# Core settings
# ======================
c.content.plugins = True
c.content.pdfjs = True
c.content.javascript.clipboard = "access"
c.content.blocking.enabled = True
c.content.blocking.method = "both"
c.tabs.last_close = "close"
c.statusbar.show = "in-mode"
c.tabs.favicons.scale = 1.0
c.tabs.max_width = 200
c.tabs.indicator.width = 2
c.editor.command = ["nvim", "{file}"]
c.window.title_format = "{perc}{current_title}"

# Custom filemanager
c.fileselect.handler = "external"
config.set(
    "fileselect.single_file.command",
    ["kitty", "--class", "yazi,yazi", "yazi", "--chooser-file", "{}"],
)
config.set(
    "fileselect.multiple_files.command",
    ["kitty", "--class", "yazi,yazi", "yazi", "--chooser-file", "{}"],
)
config.set(
    "fileselect.folder.command",
    ["kitty", "--class", "yazi,yazi", "yazi", "--chooser-file", "{}"],
)

# ======================
# Safety tor mode (tmp mode)
# ======================
if arg == "tmp":
    c.content.proxy = "socks5://localhost:9050/"
    c.content.proxy_dns_requests = True  # Обязательно разрешаем DNS через Tor

    # Параметры безопасности контента
    c.content.javascript.enabled = False
    c.content.webrtc_ip_handling_policy = "disable-non-proxied-udp"
    c.content.webgl = False
    c.content.canvas_reading = False  # Блокировка чтения данных с canvas
    c.content.local_storage = False
    c.content.tls.certificate_errors = "ask-block-thirdparty"

    # Куки и трекинг
    c.content.cookies.accept = "no-3rdparty"
    c.content.cookies.store = False  # Не сохранять куки вообще
    c.content.headers.referer = "same-domain"
    c.content.headers.custom = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }

    # Защита от утечек данных
    c.content.geolocation = False
    c.content.media.audio_capture = False
    c.content.media.video_capture = False
    c.content.media.audio_video_capture = False
    c.content.notifications.enabled = False

    # Управление сессией
    c.session.default_name = "temporary"
    c.session.lazy_restore = True
    c.auto_save.session = False  # Не сохранять сессию автоматически

    # Дополнительные меры безопасности
    c.content.autoplay = False  # Блокировка автовоспроизведения
    c.content.pdfjs = False  # Просмотр PDF внутри браузера

    c.content.site_specific_quirks.enabled = (
        False  # Отключить специальные правила для сайтов
    )

    # Очистка данных
    c.content.cache.size = 0  # Отключить кеш
    c.history_gap_interval = 0  # Не сохранять историю
    c.completion.web_history.max_items = 0

# ======================
# URL tweaks
# ======================
config_dir = os.path.dirname(__file__)
startpage_base = f"file://{config_dir}/aesthetic-startpage/main-themes"

if arg == "tmp":
    c.url.start_pages = [f"{startpage_base}/white/index.html"]
else:
    c.url.start_pages = [f"{startpage_base}/{theme}/index.html"]

c.url.searchengines = {
    "DEFAULT": "https://www.google.com/search?q={}",
    "yt": "https://www.youtube.com/results?search_query={}",
    "ts": "https://translate.google.com/?sl=auto&text={}&op=translate",
    "wayback": "https://web.archive.org/web/*/{}",
}

# ======================
# Styling
# ======================

# Tabs
c.colors.tabs.bar.bg = (
    TAB_BAR_WHITE
    if arg == "tmp"
    else TAB_BAR_CHERRY if theme == "cherry" else BACKGROUND
)
c.colors.tabs.even.bg = c.colors.tabs.odd.bg = BACKGROUND
c.colors.tabs.even.fg = c.colors.tabs.odd.fg = "gray"
c.colors.tabs.selected.even.bg = c.colors.tabs.selected.odd.bg = ACCENT_GREEN
c.colors.tabs.pinned.selected.even.bg = c.colors.tabs.pinned.selected.odd.bg = (
    ACCENT_GREEN
)

# Status bar
c.colors.statusbar.normal.bg = c.colors.statusbar.command.bg = BACKGROUND
c.colors.statusbar.insert.bg = ACCENT_GREEN
c.colors.statusbar.passthrough.bg = ACCENT_RED
c.colors.statusbar.caret.bg = ACCENT_BLUE
c.colors.statusbar.url.success.https.fg = FOREGROUND

# Completion
c.colors.completion.even.bg = BACKGROUND
c.colors.completion.odd.bg = "#1B2227"
c.colors.completion.category.bg = BACKGROUND

# Context menu
c.colors.contextmenu.menu.bg = BACKGROUND
c.colors.contextmenu.menu.fg = FOREGROUND

# Downloads
c.colors.downloads.bar.bg = BACKGROUND
c.colors.downloads.start.bg = BACKGROUND
c.colors.downloads.stop.bg = ACCENT_GREEN

# ======================
# Input settings
# ======================
c.keyhint.delay = 0
c.qt.force_platformtheme = "dark"
c.qt.force_platform = "wayland"

# Keybinds
config.bind("J", "tab-prev")
config.bind("K", "tab-next")
config.bind("<Ctrl+Shift+d>", "config-cycle colors.webpage.darkmode.enabled True False")
config.bind("<Ctrl+Alt+t>", "spawn --userscript translate")
config.bind("<Ctrl+t>", "spawn --userscript translate --text", mode="insert")
config.bind("<Ctrl+d>", "devtools")
config.bind("<Ctrl+o>", "config-source")
config.bind("<Ctrl+b>", "bookmark-list -t")
config.bind("<Ctrl+m>", "spawn mpv {url}")

# Aliases
c.aliases.update(
    {
        "ray": "set content.proxy socks://localhost:1080/",
        "dpi": "set content.proxy socks://localhost:987/",
        "system": "set content.proxy system",
    }
)

# ======================
# Domain rules
# ======================
with config.pattern("https://chatgpt.com") as p:
    p.content.javascript.enabled = True
    p.content.local_storage = True

with config.pattern("*://coub.com") as p:
    p.content.notifications.enabled = False

# TLS
c.content.tls.certificate_errors = "block"

# Fonts
c.fonts.default_size = "15px"
c.fonts.default_family = "JetBrainsMono Nerd Font"
