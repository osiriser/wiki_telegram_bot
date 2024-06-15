from os import getenv

TOKEN = getenv("BOT_TOKEN", "Your bot token")

start_text = """
<b>🐈‍⬛ Hi! Our Wikipedia bot provides quick and convenient access to information from Wikipedia.

Learn interesting facts, explore various topics and get reliable and verified information using our Wikipedia bot.</b>
"""

no_group = """<pre><code class="language-error">
<b>🎃 Group chats are disabled. Please contact me to continue.</b></pre><code>
"""
