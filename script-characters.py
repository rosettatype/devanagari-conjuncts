script_characters = {}
script_characters["Armenian"] = {
    "type": "direct",
    "uppercase": range(int("0531", 16), int("0556", 16)),
    "lowercase": range(int("0561", 16), int("0587", 16)),
    # "ligatures": range(int("FB13", 16), int("FB17", 16)),
}

languages_scripts = {
    "hy": "Armenian",
    "ar": "Arabic",
    "bn": "Bengali",
    "hi": "Devanagari",
    "mr": "Marathi",
    "ne": "Nepali",
    "gu": "Gujarati",
}
