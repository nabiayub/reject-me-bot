import json
import random
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton


router = Router()


def get_reject_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Reject me 🙅‍♂️")]
        ],
        resize_keyboard=True
    )


@router.message(CommandStart())
async def cmd_start(message: Message):
    welcome_text = (
        "👋 Welcome to Reject Me — the bot that says NO so the world doesn't have to.\n\n"
        "Feeling bold? Press the button below and receive a fresh, handcrafted rejection. No mercy. No exceptions."
    )
    await message.answer(welcome_text, reply_markup=get_reject_keyboard(), parse_mode="Markdown")


@router.message(F.text == "Reject me 🙅‍♂️")
async def handle_reject_request(message: Message):
    try:
        with open("reasons.json", "r", encoding="utf-8") as f:
            rejections = json.load(f)
        rejection = random.choice(rejections)
        await message.answer(f"{rejection}")
    except Exception as e:
        await message.answer("Oops! Even the rejection service is saying 'no' to me right now. Try again in a moment! 🔌")
        print(f"Error reading rejections: {e}")
