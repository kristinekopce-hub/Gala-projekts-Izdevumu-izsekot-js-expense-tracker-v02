import json
import os

# faila atrašnās vietas noteikšana
izdevumu_fails = os.path.join(os.path.dirname(__file__), "izdevumi.json")
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
def save_expenses(izdevumi):
    try: 
        with open(izdevumu_fails, "w", encoding='utf-8') as f:
            json.dump(izdevumi, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error: Failed to save expenses. {e}")

