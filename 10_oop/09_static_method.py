class ChaiUtils: 

    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    

raw = "  water ,  milk   , chal jana   "

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)