import json
import os

DB_FILE = "kinolar.json"

def _load():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump({}, f)
    with open(DB_FILE, "r") as f:
        return json.load(f)

def _save(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def kino_top(kod: str):
    return _load().get(kod)

def kino_qosh(kod, nomi, file_id, tavsif):
    data = _load()
    data[kod] = {"nomi": nomi, "file_id": file_id, "tavsif": tavsif}
    _save(data)

def kino_ochir(kod):
    data = _load()
    if kod in data:
        del data[kod]
        _save(data)
        return True
    return False

def royxat() -> str:
    data = _load()
    if not data:
        return "🎬 Hozircha kino yo'q!"
    matn = "🎬 <b>Kinolar ro'yxati:</b>\n\n"
    for kod, info in data.items():
        matn += f"<code>{kod}</code> — {info['nomi']}\n"
    matn += "\n📩 Kino kodini yuboring!"
    return matn