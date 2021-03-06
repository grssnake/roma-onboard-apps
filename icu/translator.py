from espeakng import ESpeakNG


words = {
    "carrot": "морковь",
    "tomato": "помидор",
    "cucumber": "огурец",
    "watermelon": "арбуз",
    "fish": "рыба",
    "bread": "хлеб",
    "tumbler": "неваляшка",
    "car": "машина",
    "tree": "дерево",
    "ship": "корабль",
    "airplane": "самолет",
    "satellite": "спутник",
    "moon": "луна",
    "sun": "солнце",
    "cosmonaut": "космонавт",
}

engine = ESpeakNG()
engine.speed = 100
engine.pitch = 32
engine.voice = 'russian'

engine.say('Привет! Меня зовут Рома. Я очень рад вас видеть!', sync=True)
engine.voice = 'english'
engine.say('Hello! My name is Roma. I am glad to see you!', sync=True)

