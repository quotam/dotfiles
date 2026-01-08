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


# ======================
# Safety tor mode (tmp mode)
# ======================
if arg == "tmp":
    c.content.proxy = "socks5://localhost:9050/"
    c.content.proxy_dns_requests = True  # Обязательно разрешаем DNS через Tor

    c.content.headers.user_agent = (
        "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"
    )
    c.content.headers.accept_language = "en-US,en;q=0.9"

    config.set(
        "content.headers.custom",
        {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"},
    )  # Упростить заголовки

    # Параметры безопасности контента
    c.content.javascript.enabled = False
    c.content.webrtc_ip_handling_policy = "disable-non-proxied-udp"
    c.content.blocking.method = "both"
    c.content.canvas_reading = False
    c.content.webgl = False
    c.content.webgl = False
    c.content.canvas_reading = False  # Блокировка чтения данных с canvas
    c.content.local_storage = False
    c.content.media.audio_video_capture = False
    c.content.tls.certificate_errors = "ask-block-thirdparty"

    # Куки и трекинг
    c.content.cookies.accept = "no-3rdparty"
    c.content.cookies.store = False  # Не сохранять куки вообще
    c.content.headers.referer = "same-domain"
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
# Color theme
# ======================
BACKGROUND = "#000000"
FOREGROUND = "#FFFFFF"
ACCENT_PRIMARY = "#242424"
ACCENT_SECONDARY = "#767676"
ACCENT_POSITIVE = "#6E8D6B"
ACCENT_NEGATIVE = "#4E0102"
ACCENT_WARNING = "#FFFF00"
ACCENT_INFO = "red"
TAB_BAR_DEFAULT = BACKGROUND
TAB_BAR_ACTIVE = "#2A2A2A"
TAB_BAR_HOVER = "#1A1A1A"


# ======================
# Styling
# ======================

# Tabs
c.colors.tabs.bar.bg = (
    "#fff" if arg == "tmp" else "purple" if theme == "cherry" else BACKGROUND
)
c.colors.tabs.even.bg = c.colors.tabs.odd.bg = BACKGROUND
c.colors.tabs.even.fg = c.colors.tabs.odd.fg = "gray"
c.colors.tabs.selected.even.bg = c.colors.tabs.selected.odd.bg = ACCENT_PRIMARY
c.colors.tabs.selected.even.fg = c.colors.tabs.selected.odd.fg = FOREGROUND
c.colors.tabs.pinned.selected.even.bg = c.colors.tabs.pinned.selected.odd.bg = (
    ACCENT_PRIMARY
)
c.colors.tabs.pinned.even.bg = c.colors.tabs.pinned.odd.bg = TAB_BAR_HOVER

# Status bar
c.colors.statusbar.normal.bg = c.colors.statusbar.command.bg = BACKGROUND
c.colors.statusbar.normal.fg = c.colors.statusbar.command.fg = FOREGROUND
c.colors.statusbar.insert.bg = ACCENT_POSITIVE
c.colors.statusbar.insert.fg = BACKGROUND
c.colors.statusbar.passthrough.bg = ACCENT_NEGATIVE
c.colors.statusbar.passthrough.fg = FOREGROUND
c.colors.statusbar.caret.bg = ACCENT_INFO
c.colors.statusbar.caret.fg = FOREGROUND
c.colors.statusbar.url.success.https.fg = ACCENT_POSITIVE
c.colors.statusbar.url.error.fg = ACCENT_NEGATIVE
c.colors.statusbar.url.warn.fg = ACCENT_WARNING
c.colors.statusbar.url.hover.fg = ACCENT_SECONDARY

# Completion
c.colors.completion.even.bg = BACKGROUND
c.colors.completion.odd.bg = "#0A0A0A"
c.colors.completion.category.bg = ACCENT_PRIMARY
c.colors.completion.category.fg = FOREGROUND
c.colors.completion.item.selected.bg = ACCENT_SECONDARY
c.colors.completion.item.selected.fg = FOREGROUND
c.colors.completion.match.fg = ACCENT_INFO

# Context menu
c.colors.contextmenu.menu.bg = BACKGROUND
c.colors.contextmenu.menu.fg = FOREGROUND
c.colors.contextmenu.selected.bg = ACCENT_PRIMARY
c.colors.contextmenu.selected.fg = FOREGROUND

# Downloads
c.colors.downloads.bar.bg = BACKGROUND
c.colors.downloads.start.bg = ACCENT_INFO
c.colors.downloads.stop.bg = ACCENT_POSITIVE
c.colors.downloads.error.bg = ACCENT_NEGATIVE

# Messages
c.colors.messages.error.bg = ACCENT_NEGATIVE
c.colors.messages.error.fg = FOREGROUND
c.colors.messages.warning.bg = ACCENT_WARNING
c.colors.messages.warning.fg = BACKGROUND
c.colors.messages.info.bg = ACCENT_INFO
c.colors.messages.info.fg = FOREGROUND

# ======================
# URL tweaks
# ======================
c.url.start_pages = [f"http://localhost:4444"]

c.url.searchengines = {
    "DEFAULT": "https://duckduckgo.com/?q={}",
    "g": "https://www.google.com/search?q={}",
    "yt": "https://www.youtube.com/results?search_query={}",
    "ts": "https://translate.google.com/?sl=auto&text={}&op=translate",
    "wayback": "https://web.archive.org/web/*/{}",
}


# ======================
# Performance settings
# ======================
c.keyhint.delay = 0
c.qt.force_platformtheme = "dark"

if arg != "tmp":
    # Nvidia optimization
    c.qt.force_platform = "wayland-egl"
    c.qt.args = [
        "enable-features=Vulkan",
        "ignore-gpu-blocklist",
        "--use-vulkan=swiftshader",
    ]

# Keybinds
config.bind("J", "tab-prev")
config.bind("K", "tab-next")
config.bind("<Ctrl+Shift+d>", "config-cycle colors.webpage.darkmode.enabled True False")
config.bind("<Ctrl+Alt+t>", "spawn --userscript translate")
config.bind("<Ctrl+t>", "spawn --userscript translate --text", mode="insert")
config.bind("<Ctrl+d>", "devtools")
config.bind("<Alt+q>", "tab-only")
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


with config.pattern("http://localhost:4444") as p:
    p.content.notifications.enabled = False
    p.content.geolocation = False

with config.pattern("https://www.bybit.com") as p:
    p.content.notifications.enabled = True

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


# TLS
c.content.tls.certificate_errors = "block"

# Fonts
c.fonts.default_size = "15px"
c.fonts.default_family = "JetBrainsMono Nerd Font"
