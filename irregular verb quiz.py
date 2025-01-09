import random
import time
import colorama
import msvcrt
from colorama import Fore
colorama.init(autoreset=True)

# Irregular verb list (verb, past simple, past participle, Turkish meaning)
irregular_verbs = [
    ("arise", "arose", "arisen", "ortaya çıkmak"),
    ("awake", "awoke", "awoken", "uyanmak"),
    ("be", "was/were", "been", "olmak"),
    ("become", "became", "become", "olmak/haline gelmek"),
    ("begin", "began", "begun", "başlamak"),
    ("bend", "bent", "bent", "eğmek"),
    ("bet", "bet", "bet", "bahse girmek"),
    ("bind", "bound", "bound", "bağlamak"),
    ("bite", "bit", "bitten", "ısırmak"),
    ("bleed", "bled", "bled", "kanamak"),
    ("blow", "blew", "blown", "esmek, üflemek"),
    ("break", "broke", "broken", "kırmak"),
    ("breed", "bred", "bred", "yetiştirmek"),
    ("bring", "brought", "brought", "getirmek"),
    ("broadcast", "broadcast", "broadcast", "yayınlamak"),
    ("build", "built", "built", "inşa etmek"),
    ("burn", "burnt/burned", "burnt/burned", "yanmak, yakmak"),
    ("burst", "burst", "burst", "patlamak"),
    ("buy", "bought", "bought", "satın almak"),
    ("can", "could", "been able", "ebilmek"),
    ("catch", "caught", "caught", "yakalamak"),
    ("choose", "chose", "chosen", "seçmek"),
    ("cling", "clung", "clung", "yapışmak"),
    ("come", "came", "come", "gelmek"),
    ("cost", "cost", "cost", "mal olmak"),
    ("creep", "crept", "crept", "sürünmek"),
    ("cut", "cut", "cut", "kesmek"),
    ("deal", "dealt", "dealt", "anlaşmak, başa çıkmak"),
    ("dig", "dug", "dug", "kazmak"),
    ("dive", "dived/dove", "dived", "dalmak"),
    ("do", "did", "done", "yapmak"),
    ("draw", "drew", "drawn", "çizmek"),
    ("dream", "dreamt/dreamed", "dreamt/dreamed", "rüya görmek"),
    ("drink", "drank", "drunk", "içmek"),
    ("drive", "drove", "driven", "sürmek"),
    ("eat", "ate", "eaten", "yemek"),
    ("fall", "fell", "fallen", "düşmek"),
    ("feed", "fed", "fed", "beslemek"),
    ("feel", "felt", "felt", "hissetmek"),
    ("fight", "fought", "fought", "dövüşmek"),
    ("find", "found", "found", "bulmak"),
    ("fly", "flew", "flown", "uçmak"),
    ("forbid", "forbade", "forbidden", "yasaklamak"),
    ("forecast", "forecast", "forecast", "tahmin etmek"),
    ("forget", "forgot", "forgotten", "unutmak"),
    ("forgive", "forgave", "forgiven", "affetmek"),
    ("foresee", "foresaw", "foreseen", "önceden görmek"),
    ("freeze", "froze", "frozen", "donmak"),
    ("get", "got", "gotten/got", "almak"),
    ("gild", "gilt/gilded", "gilt/gilded", "yaldızlamak"),
    ("give", "gave", "given", "vermek"),
    ("go", "went", "gone", "gitmek"),
    ("grind", "ground", "ground", "öğütmek"),
    ("grow", "grew", "grown", "büyümek"),
    ("hang", "hung", "hung", "asmak"),
    ("have", "had", "had", "sahip olmak"),
    ("hear", "heard", "heard", "duymak"),
    ("hew", "hewed", "hewn/hewed", "yontmak"),
    ("hide", "hid", "hidden", "saklamak"),
    ("hit", "hit", "hit", "vurmak"),
    ("hold", "held", "held", "tutmak"),
    ("hurt", "hurt", "hurt", "incitmek"),
    ("keep", "kept", "kept", "saklamak"),
    ("kneel", "knelt/kneeled", "knelt/kneeled", "diz çökmek"),
    ("knit", "knit/knitted", "knit/knitted", "örmek"),
    ("know", "knew", "known", "bilmek"),
    ("lay", "laid", "laid", "sermek, yatırmak"),
    ("lead", "led", "led", "yönetmek, liderlik etmek"),
    ("lean", "leant/leaned", "leant/leaned", "yaslanmak"),
    ("leap", "leapt/leaped", "leapt/leaped", "sıçramak"),
    ("learn", "learnt/learned", "learnt/learned", "öğrenmek"),
    ("leave", "left", "left", "ayrılmak"),
    ("lend", "lent", "lent", "ödünç vermek"),
    ("let", "let", "let", "izin vermek"),
    ("lie", "lay", "lain", "uzanmak"),
    ("light", "lit/lighted", "lit/lighted", "aydınlatmak"),
    ("lose", "lost", "lost", "kaybetmek"),
    ("make", "made", "made", "yapmak"),
    ("may", "might", " - ", "olabilmek"),
    ("mean", "meant", "meant", "anlamına gelmek"),
    ("meet", "met", "met", "tanışmak"),
    ("mislead", "misled", "misled", "yanıltmak"),
    ("mow", "mowed", "mown/mowed", "biçmek"),
    ("offset", "offset", "offset", "dengelemek"),
    ("overcome", "overcame", "overcome", "üstesinden gelmek"),
    ("overdo", "overdid", "overdone", "aşırıya kaçmak"),
    ("overtake", "overtook", "overtaken", "yetişmek, geçmek"),
    ("pay", "paid", "paid", "ödemek"),
    ("prove", "proved", "proven/proved", "kanıtlamak"),
    ("put", "put", "put", "koymak"),
    ("quit", "quit", "quit", "bırakmak, vazgeçmek"),
    ("read", "read", "read", "okumak"),
    ("rebuild", "rebuilt", "rebuilt", "yeniden inşa etmek"),
    ("redo", "redid", "redone", "yeniden yapmak"),
    ("relay", "relaid", "relaid", "tekrar sermek"),
    ("remake", "remade", "remade", "yeniden yapmak"),
    ("rend", "rent", "rent", "yırtmak, parçalamak"),
    ("ride", "rode", "ridden", "binmek"),
    ("ring", "rang", "rung", "çalmak"),
    ("rise", "rose", "risen", "yükselmek"),
    ("run", "ran", "run", "koşmak"),
    ("saw", "sawed", "sawn/sawed", "testere ile kesmek"),
    ("say", "said", "said", "söylemek"),
    ("see", "saw", "seen", "görmek"),
    ("seek", "sought", "sought", "aramak"),
    ("sell", "sold", "sold", "satmak"),
    ("send", "sent", "sent", "göndermek"),
    ("set", "set", "set", "kurmak, ayarlamak"),
    ("shake", "shook", "shaken", "sallamak"),
    ("shave", "shaved", "shaven/shaved", "tıraş etmek"),
    ("shear", "shore/sheared", "shorn/sheared", "kırkmak"),
    ("shed", "shed", "shed", "dökmek"),
    ("shine", "shone", "shone", "parlamak"),
    ("shoot", "shot", "shot", "ateş etmek"),
    ("show", "showed", "shown/showed", "göstermek"),
    ("shrink", "shrank/shrunk", "shrunk", "çekmek (küçülmek)"),
    ("shut", "shut", "shut", "kapatmak"),
    ("sightsee", "sightaw", "sightseen", "gezip görmek"),
    ("sing", "sang", "sung", "şarkı söylemek"),
    ("sink", "sank", "sunk", "batmak"),
    ("sit", "sat", "sat", "oturmak"),
    ("slay", "slew", "slain", "öldürmek"),
    ("sleep", "slept", "slept", "uyumak"),
    ("slide", "slid", "slid", "kaymak"),
    ("smell", "smelt/smelled", "smelt/smelled", "koklamak"),
    ("sow", "sowed", "sown/sowed", "ekmek"),
    ("speak", "spoke", "spoken", "konuşmak"),
    ("speed", "sped/speeded", "sped/speeded", "hızlanmak"),
    ("spend", "spent", "spent", "harcamak, geçirmek"),
    ("spin", "spun", "spun", "döndürmek"),
    ("spit", "spat", "spat", "tükürmek"),
    ("split", "split", "split", "bölmek, ayrılmak"),
    ("spoil", "spoilt/spoiled", "spoilt/spoiled", "bozmak"),
    ("spread", "spread", "spread", "yaymak"),
    ("spring", "sprang", "sprung", "fırlamak, sıçramak"),
    ("stand", "stood", "stood", "ayakta durmak"),
    ("steal", "stole", "stolen", "çalmak"),
    ("stick", "stuck", "stuck", "yapışmak, takılmak"),
    ("sting", "stung", "stung", "sokmak"),
    ("stink", "stank/stunk", "stunk", "kokuşmak"),
    ("stride", "strode", "stridden", "uzun adımlarla yürümek"),
    ("strike", "struck", "struck/stricken", "vurmak"),
    ("strive", "strove/strived", "striven/strived", "çabalamak"),
    ("swear", "swore", "sworn", "yemin etmek"),
    ("sweat", "sweat/sweated", "sweat/sweated", "terlemek"),
    ("sweep", "swept", "swept", "süpürmek"),
    ("swim", "swam", "swum", "yüzmek"),
    ("swing", "swung", "swung", "sallanmak"),
    ("take", "took", "taken", "almak"),
    ("teach", "taught", "taught", "öğretmek"),
    ("tear", "tore", "torn", "yırtmak"),
    ("tell", "told", "told", "anlatmak"),
    ("think", "thought", "thought", "düşünmek"),
    ("thrive", "throve/thrived", "thriven/thrived", "gelişmek, serpilmek"),
    ("throw", "threw", "thrown", "atmak"),
    ("thrust", "thrust", "thrust", "itmek, saplamak"),
    ("tread", "trod", "trodden", "basmak"),
    ("undergo", "underwent", "undergone", "geçirmek"),
    ("understand", "understood", "understood", "anlamak"),
    ("undertake", "undertook", "undertaken", "üstlenmek"),
    ("upset", "upset", "upset", "üzmek, altüst etmek"),
    ("wake", "woke/waked", "woken/waked", "uyanmak"),
    ("wear", "wore", "worn", "giymek"),
    ("weave", "wove", "woven", "örmek, dokumak"),
    ("weep", "wept", "wept", "ağlamak"),
    ("wet", "wet/wetted", "wet/wetted", "ıslatmak"),
    ("win", "won", "won", "kazanmak"),
    ("withdraw", "withdrew", "withdrawn", "geri çekmek"),
    ("withhold", "withheld", "withheld", "alıkoymak"),
    ("wring", "wrung", "wrung", "burkmak, sıkmak"),
    ("write", "wrote", "written", "yazmak")
]

def quiz(verbs, score):
    # Pick a random verb
    verb, past, participle, meaning = random.choice(verbs)
    verbs.remove((verb, past, participle, meaning))  # Remove the asked verb from the list

    # Ask the user
    print(Fore.WHITE + "Verb:", Fore.CYAN + f"{verb}", Fore.WHITE + "Meaning:", Fore.CYAN + f"{meaning}")
    answer = input(Fore.MAGENTA + "Your answer: " + Fore.WHITE).strip().lower()

    # Check the answer
    past_forms = past.lower().split('/')
    participle_forms = participle.lower().split('/')
    correct_answers = [f"{p} {pt}" for p in past_forms for pt in participle_forms]

    if answer in correct_answers:
        print(Fore.GREEN + "Correct!\n")
        score["correct"] += 1
    else:
        correct_display = [f"{p} {pt}" for p in past_forms for pt in participle_forms]
        print(Fore.RED + "Wrong! The correct answers are:", Fore.GREEN + f"{', '.join(correct_display)}\n")
        score["wrong"] += 1

if __name__ == "__main__":
    print(Fore.YELLOW + f"Welcome to the Irregular Verb Quiz!\n")
    total_verbs = len(irregular_verbs)
    while True:
        try:
            num_verbs = int(input(Fore.CYAN + f"How many verbs would you like to solve (1-{total_verbs}): " + Fore.WHITE))
            if 1 <= num_verbs <= total_verbs:
                break
            else:
                print(Fore.RED + "Please enter a valid number within the range.\n")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.\n")

    print(Fore.YELLOW + f"Quiz is starting...\n")
    time.sleep(1)
    print("\n\n")
    print(Fore.GREEN + "Quiz has started. Good luck!\n")

    score = {"correct": 0, "wrong": 0}
    remaining_verbs = random.sample(irregular_verbs, num_verbs)

    while remaining_verbs:
        quiz(remaining_verbs, score)

    print("\nQuiz finished. Results will be displayed shortly!\n")
    time.sleep(2)
    print(Fore.CYAN + f"Correct answers: " + Fore.GREEN + f"{score['correct']}\n" + Fore.CYAN + "Wrong answers: " + Fore.RED + f"{score['wrong']}")
    total = score['correct'] + score['wrong']
    accuracy = (score['correct'] / total) * 100
    print(Fore.CYAN + "Accuracy: " + Fore.GREEN + f"%{accuracy:.1f}\n")
    print(Fore.YELLOW + "Congratulations! #ahmetemre3829")
    print(Fore.RED + "Press any key to quit...")
    while True:
        if msvcrt.kbhit():
            break
