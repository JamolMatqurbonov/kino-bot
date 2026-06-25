from telebot import types
from database import kino_top, royxat

KANAL = "@buxoro_ish_bor_elon"
KANAL_LINK = "https://t.me/buxoro_ish_bor_elon"

def obuna_tekshir(bot, user_id):
    try:
        member = bot.get_chat_member(KANAL, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

def kanal_tugma():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📢 Kanalga o'tish", url=KANAL_LINK))
    markup.add(types.InlineKeyboardButton("✅ Tasdiqlash", callback_data="tekshir"))
    return markup

def register(bot):

    @bot.message_handler(commands=["start"])
    def start(msg):
        ism = msg.from_user.first_name or "Do'stim"
        bot.send_message(msg.chat.id,
            f"👋 Salom <b>{ism}</b>!\n\n"
            "🎬 Kino olish uchun kod yuboring!\n\n"
            "📩 Masalan: <code>7</code>",
            parse_mode="HTML")

    @bot.message_handler(commands=["kinolar"])
    def kinolar(msg):
        bot.send_message(msg.chat.id, royxat(), parse_mode="HTML")

    @bot.callback_query_handler(func=lambda c: c.data == "tekshir")
    def tekshir(call):
        if obuna_tekshir(bot, call.from_user.id):
            bot.answer_callback_query(call.id, "✅ Tasdiqlandi!")
            bot.edit_message_text(
                "✅ Obuna tasdiqlandi! Endi kino kodini yuboring.",
                call.message.chat.id,
                call.message.message_id)
        else:
            bot.answer_callback_query(call.id, "❌ Hali obuna emassiz!", show_alert=True)

    @bot.message_handler(func=lambda m: not m.text.startswith('/'))
    def kino_yuborish(msg):
        if not obuna_tekshir(bot, msg.from_user.id):
            bot.send_message(msg.chat.id,
                "❌ <b>Siz hali kanalga obuna emassiz!</b>\n\n"
                "👇 Kanalga obuna bo'ling va tasdiqlang:",
                parse_mode="HTML",
                reply_markup=kanal_tugma())
            return

        kino = kino_top(msg.text.strip())

        if not kino:
            bot.send_message(msg.chat.id,
                "❌ Bunday kod topilmadi!\n"
                "📋 /kinolar — ro'yxatni ko'ring")
            return

        if not kino["file_id"]:
            bot.send_message(msg.chat.id,
                f"⏳ <b>{kino['nomi']}</b> tez orada qo'shiladi!",
                parse_mode="HTML")
            return

        bot.send_video(msg.chat.id,
            video=kino["file_id"],
            caption=f"🎬 <b>{kino['nomi']}</b>\n{kino['tavsif']}",
            parse_mode="HTML")