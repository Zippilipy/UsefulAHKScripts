import pyautogui
from PIL import Image
import pytesseract
import time

# Define the region of the screen to capture (left, top, width, height)
chat_log_region = (0, 770, 580, 1030)  # Adjust these values as needed

typing_interval = 0.05

qa_pairs = [
        ("When mining, what depletes with each strike on a rock?", "Stamina"),
        ("How many skills in Ataraxia have levels past 99 up to 120?", "6"),
        ("Where do I go to start Invention?", "Falador"),
        ("Where do I go if I want to upgrade my T90 power armour?", "Elite dungeons"),
        ("What minimum Divination level do you need in order to participate in Guthixian Caches?", "1"),
        ("What is the maximum amount of charges that the charge pack holds at level 1 Invention?", "200k"),
        ("What is the maximum total level on Ataraxia?", "2898"),
        ("What skill provides you with perks for weapons, armours and tools?", "Invention"),
        ("After completing the Archaeology tutorial, what is the first dig site you gain access to?", "Kharid-et"),
        ("What tool do you use to excavate materials and artefacts at dig sites?", "Mattock"),
        ("How should I start my Ataraxia journey?", "Slayer"),
        ("What item can you create via the Smithing skill that'll hold your ores for you?", "Ore box"),
        ("How much do you have to donate in order to become a bronze member?", "20"),
        ("How many hours do I have to wait between Voting for Ataraxia?", "12"),
        ("What is the easiest passive money maker?", "Voting"),
        ("Solve the riddle; I have no end but I am the ending of all that begins.", "Death"),
        ("There's no staff online, where do I get help?", "Discord"),
        ("What solo boss can you fight under GWD2 that drops T92 two-handed weapons?", "Telos"),
        ("How much gold does it cost to create a private instance at Araxxor?", "200k"),
        ("What is the name of a god that fought in Lumbridge and created the crater?", "Zamorak"),
        ("Which of the original GWD bosses can attack with all combat styles", "Kree'arra"),
        ("What is the maximum amount of experience you can get in any skill?", "200m"),
        ("How many scales or energies can you use to make T90 power armour", "84"),
        ("Name a Developer of Ataraxia.", "Jaedmo"),
        ("Who is your favourite administrator?", "Jaedmo"),
        ("Who should I talk to if I have account or donation issues?", "Jaedmo"),
        ("Who killed Guthix?", "Sliske"),
        ("Who is the oldest NPC in Runescape?", "Hans"),
        ("How many coins are required to retune the boss portals at home?", "3m"),
        ("Where do you go in order to edit your Donator settings?", ";;settings"),
        ("After donating 100m coins into the portal at home, how long does 1.5x xp last?", "2 hrs"),
        ("Who sells skill capes and mastery skill capes?", "Max"),
        ("How many vote points is an Ataraxia Dollar?", "10"),
        ("What is the maximum total level you can achieve after typing ;;virtual", "3390"),
        ("What Donator rank do you have to have in order to use the permanent portable skilling stations?", "Diamond"),
        ("What boss drops the codex needed in order to unlock the 3 t99 curses?", "Aod"),
        ("Which slayer master assigns the monster that drops glacor boot upgrades?", "Morvran"),
        ("What skill rewards you with permanent passive buffs when activated?", "Archaeology"),
        ("What Agility level is required in order to use the Hefin Agility Course?", "77"),
        ("Be the first to type: 7z@zD%lmi$Kn5", "7z@zD%lmi$Kn5"),
        ("Be the first to type: r0?6B^k&4alJb", "r0?6B^k&4alJb"),
        ("What total level is required to access the crystal city of the elves?", "2250"),
        ("What is the name of the minigame that provides void equipment?", "Pest Control"),
        ("What rock can be mined to receive all possible ores at $50 donated?", "Blurite"),
        ("What item can be used to communicate with Death for reaper tasks?", "Grim gem"),
        ("How much Harmonic dust is required to make a Crystal fishing rod?", "150"),
        ("How much Harmonic dust is required to make a Crystal mattock?", "4k"),
        ("What Amulet can be purchased for Vote points/Trivia points/Ataraxia dollars to teleport to all Farming patches?", "Amulet of farming"),
        ("Which boss drops attachments which are needed to create the best-in-slot boots?", "Raksha"),
        ("What type of metal can be used to create a T70 augmented pickaxe and mattock?", "Imcando"),  # corrected note: T80
        ("What Elite dungeons boss drops the Bladed dive codex?", "Bsd"),
        ("How much Harmonic dust is required to make an Attuned crystal bow?", "2000"),
        ("Lady Ithell in Prifddinas will provide you with a free Attuned crystal weapon seed at what Smithing level?", "90"),
        ("What weapon from the Vote shop can be used to gain Prayer & Firemaking experience from Vyrewatch?", "Sunspear"),
        ("How do I configure Alt1 with Ataraxia?", ";;alt1"),
        ("What level of achievements do I need to create an Enhanced excalibur?", "Easy"),  # corrected note: Easy
        ("What tree can be cut to receive all possible logs at $50 donated?", "Wonky"),
        ("What age should I sell my Player Owned Farms animals for the most bean yield?", "Adolescent"),
        ("Where can you purchase bulk raw meat for Player Owned Farms?", "Oo'glog"),
        ("Deaths cost money.. Unless I ____?", "Vote"),
        ("Right clicking the world map allows me to edit what?", "Skybox")
    ]

def check_answer(text):
    cleaned_text = text.replace("\n", " ").replace("\r", " ").lower()
    for question, answer in qa_pairs:
        if question.lower() in cleaned_text:
            return answer
    return None

def answer(result):
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.typewrite(";;answer " + result, interval=typing_interval)
    time.sleep(0.5)
    pyautogui.press('enter')

while True:
    # Capture the screen region
    screenshot = pyautogui.screenshot(region=chat_log_region)

    # Perform OCR on the image
    chat_text = pytesseract.image_to_string(screenshot)
    
    result = check_answer(chat_text)
    if result is not None:
        answer(result)
        time.sleep(3 * 60)
    
    # Optional: print the entire cleaned text for debugging
    #print(cleaned_text)

    # Sleep for 1 second before taking the next screenshot
    time.sleep(1)
