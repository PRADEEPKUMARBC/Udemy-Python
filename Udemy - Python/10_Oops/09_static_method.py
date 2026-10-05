class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]

raw = " water , milk , sugar , tea leaves "

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)  # Output: ['water', 'milk', 'sugar', 'tea leaves']
