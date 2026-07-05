import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, BotCommand

# --- CONFIGURATION (CONFIG) ---
# Yahan apka token (image_0.png se liya gaya)
# ⚠️ WARNING: Ise revoke karein aur naya token dalein.
BOT_TOKEN = "8929869494:AAELx_j5eJBLAYXgJDqR2L7TspBJt8mfpiE"

# Apka Vercel Web Link
WEB_LINK = "https://bseb-registration-2.vercel.app/"

bot = telebot.TeleBot(BOT_TOKEN)

# --- MESSAGES (PREMIUM STYLE) ---
# Welcome message with Markdown formatting
WELCOME_MESSAGE = """
Hello 👋 *{user_name}*!

🚀 *Bihar Board (BSEB) Class 10th* ke liye **ALL BATCHES FREE** hain!

🎯 Apni seat confirm karne aur classes shuru karne ke liye niche button par click karein. Ye ek sunehra mauka hai apke future ke liye! Do not miss it!

💡 *Important Instruction:* Jab aap link par click karein, to use apne phone ke normal browser (Jaise Chrome ya Safari) mein open karein, tabhi registration safe save hoga.
"""

# Text for the main action button
BUTTON_TEXT = "🚀 Start Registration"

# Message for help command
HELP_MESSAGE = """
🆘 *Need Help?*

 बिहार बोर्ड Class 10th फ्री बैच रजिस्ट्रेशन में कोई दिक्कत?

 💬 *Admin se Contact karein:* (Apna Admin link ya id yahan dalein, e.g., @admin_id)

 🔄 */start* daba kar registration link fir se payein.
"""

# --- MARKUPS (UI ELEMENTS) ---
# Markup for the main action button
def get_main_markup():
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton(text=BUTTON_TEXT, url=WEB_LINK)
    markup.add(btn)
    return markup

# --- HELPERS ---
def set_bot_menu(bot):
    """Sets the premium commands in the bot's menu."""
    commands = [
        BotCommand("start", "🚀 Registration Link"),
        BotCommand("help", "🆘 Contact Support / Help"),
        BotCommand("menu", "📋 Bot Menu")
    ]
    bot.set_my_commands(commands)
    print("📋 Bot commands menu set successfully.")

# --- HANDLERS ---
# Handle /start command
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_name = message.from_user.first_name
    formatted_msg = WELCOME_MESSAGE.format(user_name=user_name)
    
    # Send message with button
    bot.send_message(
        message.chat.id, 
        formatted_msg, 
        parse_mode="Markdown", 
        reply_markup=get_main_markup()
    )
    print(f"✅ User {user_name} started the bot.")

# Handle /menu command (can be same as start or slightly different)
@bot.message_handler(commands=['menu'])
def handle_menu(message):
    user_name = message.from_user.first_name
    # Can send a simpler version or just the main link again
    menu_msg = f"📋 *Premium Bot Menu* - Hello {user_name}! Aapka registration link: {WEB_LINK}"
    bot.send_message(
        message.chat.id, 
        menu_msg, 
        parse_mode="Markdown", 
        reply_markup=get_main_markup()
    )

# Handle /help command
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, HELP_MESSAGE, parse_mode="Markdown")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print("✅ Premium Bot started successfully...")
    
    # Set the bot menu once on startup
    try:
        set_bot_menu(bot)
    except Exception as e:
        print(f"❌ Error setting menu: {e}")
        
    # Start the bot's polling loop
    bot.infinity_polling()

