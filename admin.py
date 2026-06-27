from config import ADMIN_ID
from database import kino_qosh, kino_ochir, royxat

kutilayotgan = {}

def register(bot):

    @bot.message_handler(commands=["list"])
    def kinolar_royxat(msg):
        if msg.from_user.id != ADMIN_ID:
            return
        bot.send_message(msg.chat.id, royxat(), parse_mode="HTML")

    @bot.message_handler(commands=["del"])
    def kino_ochirish(msg):
        if msg.from_user.id != ADMIN_ID:
            return
        try:
            kod = msg.text.split()[1]
            if kino_ochir(kod):
                bot.send_message(msg.chat.id,
                    f"✅ <code>{kod}</code> o'chirildi!",
                    parse_mode="HTML")
            else:
                bot.send_message(msg.chat.id,
                    f"❌ <code>{kod}</code> topilmadi!",
                    parse_mode="HTML")
        except:
            bot.send_message(msg.chat.id,
                "❌ Format: <code>/del kod</code>",
                parse_mode="HTML")

    @bot.message_handler(content_types=["video", "document"])
    def video_qabul(msg):
        if msg.from_user.id != ADMIN_ID:
            return
        if msg.video:
            fid = msg.video.file_id
        else:
            fid = msg.document.file_id
        kutilayotgan[msg.from_user.id] = {"file_id": fid}
        bot.send_message(msg.chat.id,
            "✅ Video qabul qilindi!\n\n"
            "Kod va nomini yuboring:\n"
            "<code>kod nomi</code>\n\n"
            "Masalan: <code>7 Merlin</code>",
            parse_mode="HTML")

    @bot.message_handler(func=lambda m: m.from_user.id == ADMIN_ID and m.from_user.id in kutilayotgan)
    def kino_saqlash(msg):
        if msg.text.startswith('/'):
            return
        try:
            qismlar = msg.text.split(" ", 1)
            kod = qismlar[0]
            nomi = qismlar[1]
            file_id = kutilayotgan[msg.from_user.id]["file_id"]
            kino_qosh(kod, nomi, file_id, nomi)
            del kutilayotgan[msg.from_user.id]
            bot.send_message(msg.chat.id,
                f"🎬 <b>{nomi}</b> qo'shildi!\n"
                f"📌 Kod: <code>{kod}</code>",
                parse_mode="HTML")
        except:
            bot.send_message(msg.chat.id,
                "❌ Format: <code>kod nomi</code>\n"
                "Masalan: <code>7 Merlin</code>",
                parse_mode="HTML")