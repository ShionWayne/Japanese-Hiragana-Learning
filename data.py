import os

learn_data = [
    {
        'id': 'a',
        'hiragana': 'あ',
        'sounds_like': 'ah',
        'audio': os.path.join("../"+app.config['learn_audio'], 'a.mp3')
    },
    {
        'id': 'i',
        'hiragana': 'い',
        'sounds_like': 'e',
        'audio': os.path.join("../"+app.config['learn_audio'], 'i.mp3')
    },
    {
        'id': 'u',
        'hiragana': 'う',
        'sounds_like': 'woo',
        'audio': os.path.join("../"+app.config['learn_audio'], 'u.mp3')
    },
    {
        'id': 'e',
        'hiragana': 'え',
        'sounds_like': 'i',
        'audio': os.path.join("../"+app.config['learn_audio'], 'e.mp3')
    },
    {
        'id': 'o',
        'hiragana': 'お',
        'sounds_like': 'o',
        'audio': os.path.join("../"+app.config['learn_audio'], 'o.mp3')
    }
]

quiz_1_data = [
    {
        "q_type": 1,
        "id": 1,
        "type": "drag",
        "problem_text": "Drag the hiragana to corresponding Romanization:",
        "problem_and_answer": [
            {"hiragana": "あい", "Romanization": "ai", "English": "love"},
            {"hiragana": "うお", "Romanization": "uo", "English": "fish"},
            {"hiragana": "いえ", "Romanization": "ie", "English": "home"}
        ]
    }
]

quiz_2_data = [
    {
        "q_type": 2,
        "hiragana": "おい",
        "roman": "hey",
        "audio": os.path.join("../" + app.config['quiz_2_audio'], 'oi.mp3')
    },
    {
        "q_type": 2,
        "hiragana": "うえ",
        "roman": "up",
        "audio": os.path.join("../" + app.config['quiz_2_audio'], 'ue.mp3')
    },
    {
        "q_type": 2,
        "hiragana": "あう",
        "roman": "Meet",
        "audio": os.path.join("../" + app.config['quiz_2_audio'], 'au.mp3')
    }
]


quiz_3_data = [
    {
        "q_type": 3,
        "hiragana": "あおい",
        "roman": "aoi"
    }
]

quiz_4_data = [
    {
        "q_type": 4,
        "roman": "iie"
    }
]


q_data = quiz_1_data + quiz_2_data + quiz_3_data + quiz_4_data

user_result = []
