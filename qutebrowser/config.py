import sys

arg = "default"

if len(sys.argv) > 1 and "tmp" in sys.argv[2].lower():
    arg = "tmp"

config.load_autoconfig(False)

config.set("content.plugins", True)
config.set("content.pdfjs", True)

config.set("content.javascript.clipboard", "access")

if arg != "default":
    config.set("content.proxy", "socks5://localhost:9050/")
    config.set("content.javascript.enabled", False)
    config.set("content.javascript.enabled", True, "https://chatgpt.com")
    config.set("content.javascript.enabled", True, "https://www.youtube.com")

    config.set("content.webrtc_ip_handling_policy", "disable-non-proxied-udp")

    config.set("content.cookies.accept", "no-3rdparty")

    config.set("content.local_storage", False)
    config.set("content.local_storage", True, "https://chatgpt.com")

    config.set("content.tls.certificate_errors", "ask-block-thirdparty")

    config.set("content.webgl", False)

    config.set("content.geolocation", False)
    config.set("content.notifications.enabled", False)
    config.set("content.media.audio_capture", False)
    config.set("content.media.video_capture", False)

    config.set("session.default_name", "temporary")
    config.set("session.lazy_restore", True)

    config.set("content.headers.referer", "same-domain")


config.set("content.blocking.enabled", True)
config.set("content.blocking.method", "both")  # Использует и host-based, и фильтры

config.set("content.notifications.enabled", False, "*://coub.com")
config.set("content.cookies.accept", "all", "chrome-devtools://*")
config.set("content.javascript.clipboard", "access")
config.set("qt.force_platformtheme", "dark")
config.set("qt.force_platform", "wayland")

c.content.tls.certificate_errors = "block"
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

config.set("content.cookies.accept", "all", "devtools://*")

config.set("content.headers.accept_language", "", "https://matchmaker.krunker.io/*")

config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}",
    "https://web.whatsapp.com/",
)

config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}; rv:90.0) Gecko/20100101 Firefox/90.0",
    "https://accounts.google.com/*",
)

# Load images automatically in web pages.
# Type: Bool
config.set("content.images", True, "chrome-devtools://*")

# Load images automatically in web pages.
# Type: Bool
config.set("content.images", True, "devtools://*")

# Enable JavaScript.
# Type: Bool
config.set("content.javascript.enabled", True, "chrome-devtools://*")

# Enable JavaScript.
# Type: Bool
config.set("content.javascript.enabled", True, "devtools://*")

# Enable JavaScript.
# Type: Bool
config.set("content.javascript.enabled", True, "chrome://*/*")

# Enable JavaScript.
# Type: Bool
config.set("content.javascript.enabled", True, "qute://*/*")

# Allow locally loaded documents to access remote URLs.
# Type: Bool
config.set(
    "content.local_content_can_access_remote_urls",
    True,
    "file:///" + __file__.replace("config.py", "") + "/userscripts/*",
)

c.tabs.last_close = "close"

if arg == "default":

    if len(sys.argv) > 1 and "vite" in sys.argv[2].lower():
        c.url.start_pages = [
            "file:///"
            + __file__.replace("config.py", "")
            + "/aesthetic-startpage/main-themes/cherry/index.html"
        ]
    else:
        c.url.start_pages = [
            "file:///"
            + __file__.replace("config.py", "")
            + "/aesthetic-startpage/main-themes/orange/index.html"
        ]
else:
    c.url.start_pages = [
        "file:///"
        + __file__.replace("config.py", "")
        + "/aesthetic-startpage/main-themes/white/index.html"
    ]


config.set(
    "content.local_content_can_access_file_urls",
    False,
    "file:///" + __file__.replace("config.py", "") + "/userscripts/*",
)

c.editor.command = ["nvim", "{file}"]
c.statusbar.show = "in-mode"
c.tabs.favicons.scale = 1.0

if arg == "default":
    c.tabs.title.format = "{audio}{current_title}"
else:
    c.tabs.title.format = "{audio}{current_title} | SECURE"

c.tabs.max_width = 200

c.tabs.indicator.width = 2

c.url.searchengines = {
    "DEFAULT": "https://www.google.com/search?q={}",
    "yt": "https://www.youtube.com/results?search_query={}",
    "ts": "https://translate.google.com/?sl=auto&text={}&op=translate",
}

c.window.title_format = "{perc}{current_title}"

c.colors.completion.category.bg = (
    "qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #888888, stop:1 #505050)"
)

c.colors.tooltip.bg = "#161C20"

c.colors.tooltip.fg = "whitesmoke"
c.colors.contextmenu.menu.bg = "#161C20"

c.colors.contextmenu.menu.fg = "whitesmoke"

c.colors.prompts.bg = "#161C20"

c.colors.statusbar.normal.bg = "#161C20"

c.colors.statusbar.insert.bg = "#6E8D6B"

c.colors.statusbar.passthrough.bg = "#7B3D3C"

c.colors.statusbar.command.bg = "#161C20"

c.colors.statusbar.caret.bg = "#24253C"

c.colors.statusbar.caret.selection.bg = "#24253C"

if arg == "default":
    if len(sys.argv) > 1 and "vite" in sys.argv[2].lower():
        c.colors.tabs.bar.bg = "#CD7685"
    else:
        c.colors.tabs.bar.bg = "#161C20"
else:
    c.colors.tabs.bar.bg = "#F1F1F1"

c.colors.tabs.odd.fg = "gray"
c.colors.tabs.odd.bg = "#161C20"
c.colors.tabs.even.fg = "gray"

c.colors.tabs.even.bg = "#161C20"


c.colors.tabs.pinned.selected.even.bg = "#6E8D6B"
c.colors.tabs.pinned.selected.odd.bg = "#6E8D6B"

c.colors.tabs.pinned.even.bg = "#161C20"
c.colors.tabs.pinned.odd.bg = "#161C20"

c.colors.tabs.selected.even.bg = "#6E8D6B"
c.colors.tabs.selected.odd.bg = "#6E8D6B"


c.colors.messages.error.bg = "#4E0102"
c.colors.downloads.error.bg = "#4E0102"
c.colors.statusbar.url.hover.fg = "white"
c.colors.messages.warning.bg = "#EACA8C"
c.colors.statusbar.url.warn.fg = "#EACA8C"
c.colors.completion.even.bg = "#161C20"
c.colors.completion.odd.bg = "#1B2227"

c.colors.completion.category.bg = "#161C20"


c.colors.downloads.bar.bg = "#161C20"

c.colors.downloads.start.bg = "#161C20"
c.colors.downloads.start.fg = "gray"

c.colors.statusbar.url.success.https.fg = "whitesmoke"
c.colors.downloads.stop.bg = "#6E8D6B"
c.colors.downloads.stop.fg = "whitesmoke"

config.set("downloads.position", "top")

c.colors.tabs.pinned.even.fg = "gray"

c.fonts.default_family = "JetBrainsMono Nerd Font"

c.bindings.key_mappings = {
    "<Ctrl+6>": "<Ctrl+^>",
    "<Ctrl+Enter>": "<Ctrl+Return>",
    "<Ctrl+[>": "<Escape>",
    "<Ctrl+i>": "<Tab>",
    "<Ctrl+j>": "<Return>",
    "<Ctrl+m>": "<Return>",
    "<Enter>": "<Return>",
    "<Shift+Enter>": "<Return>",
    "<Shift+Return>": "<Return>",
}

# Bindings for normal mode
config.bind("J", "tab-prev")
config.bind("K", "tab-next")

config.bind("<Ctrl+Alt+t>", "spawn --userscript translate")
config.bind("<Ctrl+t>", "spawn --userscript translate --text")

config.bind("<Ctrl+t>", "spawn --userscript translate --text", mode="insert")
config.bind("<Ctrl+t>", "spawn --userscript translate --text", mode="passthrough")

config.bind("<Ctrl+d>", "devtools")
config.bind("<Ctrl+o>", "config-source")


c.aliases["ray"] = "set content.proxy socks://localhost:1080/"
c.aliases["dpi"] = "set content.proxy socks://localhost:987/"
c.aliases["system"] = "set content.proxy system"

config.bind("<Ctrl+b>", "bookmark-list -t")
config.bind("<Ctrl+m>", "spawn mpv {url}")
