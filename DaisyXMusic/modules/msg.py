# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from DaisyXMusic.config import SOURCE_CODE
from DaisyXMusic.config import ASSISTANT_NAME
from DaisyXMusic.config import PROJECT_NAME
from DaisyXMusic.config import SUPPORT_GROUP
from DaisyXMusic.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "**Merhaba 👋 [{}](tg://user?id={})!**\n\n🤖 Ben telegram gruplarına Sesli sohbetlerde Müzik calmak icin yapıldım & Hoşgeldin\n\n✅ Bana  /help yazarak bilgi alabirsin."
      HELP_MSG = [
        ".",
'''
𝓎𝒶𝓇𝚤𝓃𝓁𝒶𝓇 𝒷𝒾𝓏ℯ 𝚤𝓂𝓊𝓉 ℴ𝓁𝓈𝓊𝓃🦋19:03 ●━━━━━━──────01:00 ꨄ︎      ⇆ㅤ◁ㅤ❚❚ㅤ▷ㅤ↻
ᴋᴏᴍᴜᴛʟᴀʀ

☞ /oynat ⇝ Yanıtladığınız şarkıyı çalar
☞ /oynat ⇝ <şarkı ismi> istediğiniz şarkıyı bulur
☞ /skip    ⇝ Şarkıyı atlar
☞ /pause ⇝ Müzik durur 
☞/resume ⇝Müzik devam eder
☞ /playlist ⇝Çalma listesinj gösterir
☞/song ⇝ Şarkıyı indirir
☞/admincache  ⇝ Grubunuzun yönetici bilgilerini günceller 
☞/userbotjoin ⇝ Asistanı grubunuza davet eder 
  
  ♡Assistant adı >> @Adonisasistann

Click next for instructions
 '''
           ]
