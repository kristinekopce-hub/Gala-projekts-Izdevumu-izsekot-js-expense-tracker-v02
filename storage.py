import json
import os
import os

# Fails, kur glabāsies izdevumi, lasīšanas režīmā "r"
izdevumu_fails = "izdevumi.json"
def load_expenses():
    if not os.path.exists(izdevumu_fails):
        return []
    try:
        with open(izdevumu_fails, "r", encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        else:
            return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON in expenses file.")
        return []

# Saglabā izdevumus datubāzē, raksīšanas režīmā "w"
def save_expenses(izdevumi, izdevumu_fails = "izdevumi.json"):
    try: 
        with open(izdevumu_fails, "w", encoding='utf-8') as f:
            json.dump(izdevumi, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error: Failed to save expenses. {e}")

#Nolasām JSON failu
with open(izdevumu_fails, "r", encoding='utf-8') as f:   
    loaded = json.load(f)
print(loaded)