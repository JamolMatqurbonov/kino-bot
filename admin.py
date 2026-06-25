from config import ADMIN_ID
from database import kino_qosh, kino_ochir, royxat

def register(bot):

    @bot.message_handler(commands=["add"])
    def kino_qoshish(msg):
        if msg.from_user.id != ADMIN_ID:
            return
        try:
            # /add kod nomi file_id tavsif
            qismlar = msg.text.split(" ", 4)
            kod = qismlar[1]
            nomi = qismlar[2]
            file_id = qismlar[3]
            tavsif = qismlar[4]
            kino_qosh(kod, nomi, file_id, tavsif)
            bot.send_message(msg.chat.id,
                f"✅ <b>{nomi}</b> qo'shildi!\n"
                f"📌 Kod: <code>{kod}</code>",
                parse_mode="HTML")
        except:
            bot.send_message(msg.chat.id,
                "❌ Xato! To'g'ri format:\n"
                "<code>/add kod nomi file_id tavsif</code>\n\n"
                "Masalan:\n"
                "<code>/add 8 Batman BAACAgIA... Batman filmi</code>",
                parse_mode="HTML")

    @bot.message_handler(commands=["del"])
    def kino_ochirish(msg):
        if msg.from_user.id != ADMIN_ID:
            return
        try:
            kod = msg.text.split()[1]
            if kino_ochir(kod):
                bot.send_message(msg.chat.id,
                    f"✅ <code>{kod}</code> kod o'chirildi!",
                    parse_mode="HTML")
            else:
                bot.send_message(msg.chat.id,
                    f"❌ <code>{kod}</code> kod topilmadi!",
                    parse_mode="HTML")
        except:
            bot.send_message(msg.chat.id,
                "❌ Format: <code>/del kod</code>",
                parse_mode="HTML")

    @bot.message_handler(commands=["list"])
    def kinolar_royxat(msg):
        if msg.from_user.id != ADMIN_ID:
            return
        bot.send_message(msg.chat.id, royxat(), parse_mode="HTML")

    @bot.message_handler(commands=["getid"])
    def getid(msg):
        if msg.from_user.id != ADMIN_ID:
            return
        bot.send_message(msg.chat.id,
            "✅ Endi botga video yuboring — file_id ni olasiz!")

    @bot.message_handler(content_types=["video", "document"])
    def file_id_ol(msg):
        if msg.from_user.id != ADMIN_ID:
            return
        if msg.video:
            fid = msg.video.file_id
        else:
            fid = msg.document.file_id
        bot.send_message(msg.chat.id,
            f"📋 <b>File ID:</b>\n<code>{fid}</code>\n\n"
            "⬆️ Endi /add buyrug'i bilan qo'shing!",
            parse_mode="HTML")