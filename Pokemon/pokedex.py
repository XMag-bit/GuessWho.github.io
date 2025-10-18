import json
import os

# === Cari file JSON berdasarkan lokasi script ===
base_path = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(base_path, "pokedex.json")

# === Load file pokedex.json ===
with open(json_path, "r", encoding="utf-8") as f:
    pokedex = json.load(f)


# === Fungsi menentukan metode evolusi ===
def determine_evo_method(evo_data):
    if not evo_data or (("next" not in evo_data) and ("prev" not in evo_data)):
        return "Cannot Evolve"
    entries = []
    if "next" in evo_data:
        entries += evo_data["next"]
    if "prev" in evo_data:
        entries.append(evo_data["prev"])

    for entry in entries:
        if isinstance(entry, list) and len(entry) > 1:
            condition = entry[1].lower()
            if "use" in condition:
                return "Use Item"
            elif "friendship" in condition:
                return "Happiness"
            elif "knowing" in condition or "move" in condition:
                return "Knowing Move"
    return "Naturally"


# === GEN & REGION mapping ===
generation_region_map = {
    1: "Kanto",
    2: "Johto",
    3: "Hoenn",
    4: "Sinnoh",
    5: "Unova",
    6: "Kalos",
    7: "Alola",
    8: "Galar",
    9: "Paldea"
}

# === Fungsi untuk menentukan gen & region berdasarkan ID nasional ===
def get_gen_region(id_num):
    if 1 <= id_num <= 151:
        return 1, generation_region_map[1]
    elif 152 <= id_num <= 251:
        return 2, generation_region_map[2]
    elif 252 <= id_num <= 386:
        return 3, generation_region_map[3]
    elif 387 <= id_num <= 493:
        return 4, generation_region_map[4]
    elif 494 <= id_num <= 649:
        return 5, generation_region_map[5]
    elif 650 <= id_num <= 721:
        return 6, generation_region_map[6]
    elif 722 <= id_num <= 809:
        return 7, generation_region_map[7]
    elif 810 <= id_num <= 905:
        return 8, generation_region_map[8]
    elif 906 <= id_num <= 1025:
        return 9, generation_region_map[9]
    else:
        return "Unknown", "Unknown"

# === STARTERS (semua generasi, beserta evolusi penuh) ===
starters = {
    "Bulbasaur", "Ivysaur", "Venusaur",
    "Charmander", "Charmeleon", "Charizard",
    "Squirtle", "Wartortle", "Blastoise",
    "Chikorita", "Bayleef", "Meganium",
    "Cyndaquil", "Quilava", "Typhlosion",
    "Totodile", "Croconaw", "Feraligatr",
    "Treecko", "Grovyle", "Sceptile",
    "Torchic", "Combusken", "Blaziken",
    "Mudkip", "Marshtomp", "Swampert",
    "Turtwig", "Grotle", "Torterra",
    "Chimchar", "Monferno", "Infernape",
    "Piplup", "Prinplup", "Empoleon",
    "Snivy", "Servine", "Serperior",
    "Tepig", "Pignite", "Emboar",
    "Oshawott", "Dewott", "Samurott",
    "Chespin", "Quilladin", "Chesnaught",
    "Fennekin", "Braixen", "Delphox",
    "Froakie", "Frogadier", "Greninja",
    "Rowlet", "Dartrix", "Decidueye",
    "Litten", "Torracat", "Incineroar",
    "Popplio", "Brionne", "Primarina",
    "Grookey", "Thwackey", "Rillaboom",
    "Scorbunny", "Raboot", "Cinderace",
    "Sobble", "Drizzile", "Inteleon",
}

# === FOSSIL Pokémon (semua generasi, evolusi penuh) ===
fossils = {
    "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl",
    "Lileep", "Cradily", "Anorith", "Armaldo",
    "Cranidos", "Rampardos", "Shieldon", "Bastiodon",
    "Tirtouga", "Carracosta", "Archen", "Archeops",
    "Tyrunt", "Tyrantrum", "Amaura", "Aurorus",
    "Dracozolt", "Arctozolt", "Dracovish", "Arctovish"
}

# === PSEUDO-LEGENDARY Pokémon (beserta evolusi penuh) ===
pseudo = {
    "Dratini", "Dragonair", "Dragonite",
    "Larvitar", "Pupitar", "Tyranitar",
    "Bagon", "Shelgon", "Salamence",
    "Beldum", "Metang", "Metagross",
    "Gible", "Gabite", "Garchomp",
    "Deino", "Zweilous", "Hydreigon",
    "Goomy", "Sliggoo", "Goodra",
    "Jangmo-o", "Hakamo-o", "Kommo-o",
    "Dreepy", "Drakloak", "Dragapult",
}

# === ULTRA BEASTS ===
ultra_beasts = {
    "Nihilego", "Buzzwole", "Pheromosa", "Xurkitree",
    "Celesteela", "Kartana", "Guzzlord", "Poipole", "Naganadel",
    "Stakataka", "Blacephalon"
}

# === LEGENDARY Pokémon ===
legendary = {
    "Articuno", "Zapdos", "Moltres", "Mewtwo",
    "Raikou", "Entei", "Suicune", "Lugia", "Ho-Oh",
    "Regirock", "Regice", "Registeel", "Latias", "Latios",
    "Kyogre", "Groudon", "Rayquaza",
    "Uxie", "Mesprit", "Azelf", "Dialga", "Palkia",
    "Heatran", "Regigigas", "Giratina", "Cresselia",
    "Cobalion", "Terrakion", "Virizion", "Tornadus",
    "Thundurus", "Reshiram", "Zekrom", "Landorus", "Kyurem",
    "Xerneas", "Yveltal", "Zygarde",
    "Tapu Koko", "Tapu Lele", "Tapu Bulu", "Tapu Fini",
    "Solgaleo", "Lunala", "Necrozma",
    "Zacian", "Zamazenta", "Eternatus", "Regieleki", "Regidrago", "Calyrex",
}

# === MYTHICAL Pokémon ===
mythical = {
    "Mew", "Celebi", "Jirachi", "Deoxys",
    "Manaphy", "Phione", "Darkrai", "Shaymin", "Arceus",
    "Victini", "Keldeo", "Meloetta", "Genesect",
    "Diancie", "Hoopa", "Volcanion",
    "Magearna", "Marshadow", "Zeraora", "Meltan", "Melmetal",
    "Zarude",
}


# === EVOLUTION METHODS ===
evolve_with_item = {
    "Eevee", "Vulpix", "Ninetales", "Growlithe", "Arcanine",
    "Poliwhirl", "Poliwrath", "Slowpoke", "Slowbro",
    "Gloom", "Vileplume", "Weepinbell", "Victreebel",
    "Exeggcute", "Exeggutor", "Clefairy", "Clefable",
    "Jigglypuff", "Wigglytuff", "Togetic", "Togekiss",
    "Scyther", "Scizor", "Feebas", "Milotic",
    "Roselia", "Roserade", "Murkrow", "Honchkrow",
    "Misdreavus", "Mismagius", "Sneasel", "Weavile",
    "Electabuzz", "Electivire", "Magmar", "Magmortar",
    "Rhydon", "Rhyperior", "Dusclops", "Dusknoir",
    "Lampent", "Chandelure", "Petilil", "Lilligant",
    "Cottonee", "Whimsicott", "Applin", "Flapple", "Appletun"
}

evolve_with_happiness = {
    "Eevee", "Espeon", "Umbreon", "Sylveon",
    "Pichu", "Pikachu", "Cleffa", "Clefairy",
    "Igglybuff", "Jigglypuff", "Togepi", "Togetic",
    "Budew", "Roserade", "Riolu", "Lucario", "Snom", "Frosmoth"
}

evolve_knowing_move = {
    "Piloswine", "Mamoswine",
    "Aipom", "Ambipom",
    "Yanma", "Yanmega",
    "Bonsly", "Sudowoodo",
    "Mime Jr.", "Mr. Mime",
    "Steenee", "Tsareena",
    "Clobbopus", "Grapploct"
}

cannot_evolve = {
    "Farfetch’d", "Jynx", "Lapras", "Ditto", "Snorlax", "Mewtwo", "Mew",
    "Torkoal", "Zangoose", "Seviper", "Absol", "Rotom", "Druddigon",
    "Audino", "Hawlucha", "Minior", "Komala", "Palafin", "Tinkaton"
}

# === EGG GROUPS ===

monster_egg = {
    "Charmander", "Charmeleon", "Charizard",
    "Squirtle", "Wartortle", "Blastoise",
    "Bulbasaur", "Ivysaur", "Venusaur",
    "Rhyhorn", "Rhydon", "Rhyperior",
    "Kangaskhan", "Nidoking", "Nidoqueen",
    "Lapras", "Tyrunt", "Tyrantrum",
    "Amaura", "Aurorus", "Larvitar", "Pupitar", "Tyranitar",
    "Bagon", "Shelgon", "Salamence",
    "Gible", "Gabite", "Garchomp",
    "Axew", "Fraxure", "Haxorus",
    "Turtwig", "Grotle", "Torterra",
    "Goomy", "Sliggoo", "Goodra",
    "Hakamo-o", "Jangmo-o", "Kommo-o",
    "Dracozolt", "Dracovish", "Tyrantrum",
    "Sandaconda", "Copperajah"
}

human_like_egg = {
    "Machop", "Machoke", "Machamp",
    "Magmar", "Electabuzz", "Jynx",
    "Hitmonlee", "Hitmonchan", "Hitmontop",
    "Lucario", "Riolu", "Conkeldurr",
    "Toxicroak", "Mr. Mime", "Mr. Rime",
    "Medicham", "Grimsnarl", "Throh", "Sawk",
    "Scrafty", "Scraggy", "Falinks"
}

water1_egg = {
    "Squirtle", "Wartortle", "Blastoise",
    "Psyduck", "Golduck",
    "Poliwag", "Poliwhirl", "Poliwrath", "Politoed",
    "Tentacool", "Tentacruel", "Slowpoke", "Slowbro", "Slowking",
    "Horsea", "Seadra", "Kingdra",
    "Goldeen", "Seaking", "Lapras",
    "Totodile", "Croconaw", "Feraligatr",
    "Mudkip", "Marshtomp", "Swampert",
    "Froakie", "Frogadier", "Greninja",
    "Sobble", "Drizzile", "Inteleon",
    "Wishiwashi", "Basculin", "Barraskewda"
}

water2_egg = {
    "Remoraid", "Octillery", "Qwilfish", "Overqwil",
    "Chinchou", "Lanturn", "Whiscash", "Huntail", "Gorebyss",
    "Clamperl", "Luvdisc", "Finneon", "Lumineon",
    "Bruxish", "Alomomola"
}

water3_egg = {
    "Magikarp", "Gyarados", "Feebas", "Milotic",
    "Barboach", "Whiscash", "Wishiwashi", "Basculin",
    "Dracovish", "Arctovish", "Dondozo", "Tatsugiri"
}

bug_egg = {
    "Caterpie", "Metapod", "Butterfree",
    "Weedle", "Kakuna", "Beedrill",
    "Paras", "Parasect", "Venonat", "Venomoth",
    "Scyther", "Scizor", "Pinsir", "Heracross",
    "Wurmple", "Silcoon", "Beautifly", "Cascoon", "Dustox",
    "Sewaddle", "Swadloon", "Leavanny",
    "Venipede", "Whirlipede", "Scolipede",
    "Grubbin", "Charjabug", "Vikavolt"
}

mineral_egg = {
    "Magnemite", "Magneton", "Magnezone",
    "Voltorb", "Electrode", "Geodude", "Graveler", "Golem",
    "Onix", "Steelix", "Nosepass", "Probopass",
    "Beldum", "Metang", "Metagross",
    "Roggenrola", "Boldore", "Gigalith",
    "Carbink", "Minior", "Duraludon"
}

flying_egg = {
    "Pidgey", "Pidgeotto", "Pidgeot",
    "Spearow", "Fearow", "Zubat", "Golbat", "Crobat",
    "Farfetch’d", "Sirfetch’d", "Doduo", "Dodrio",
    "Hoothoot", "Noctowl", "Taillow", "Swellow",
    "Starly", "Staravia", "Staraptor",
    "Pidove", "Tranquill", "Unfezant",
    "Rookidee", "Corvisquire", "Corviknight"
}

amorphous_egg = {
    "Gastly", "Haunter", "Gengar",
    "Grimer", "Muk", "Koffing", "Weezing",
    "Drifloon", "Drifblim",
    "Litwick", "Lampent", "Chandelure",
    "Solosis", "Duosion", "Reuniclus",
    "Shuppet", "Banette", "Mimikyu", "Cursola", "Runerigus"
}

field_egg = {
    "Eevee", "Vaporeon", "Jolteon", "Flareon", "Leafeon", "Glaceon", "Sylveon",
    "Vulpix", "Ninetales", "Growlithe", "Arcanine",
    "Meowth", "Persian", "Lillipup", "Herdier", "Stoutland",
    "Zigzagoon", "Linoone", "Obstagoon",
    "Rockruff", "Lycanroc",
    "Zangoose", "Seviper", "Absol",
    "Nickit", "Thievul", "Yamper", "Boltund"
}

fairy_egg = {
    "Clefairy", "Clefable",
    "Jigglypuff", "Wigglytuff",
    "Snubbull", "Granbull",
    "Ralts", "Kirlia", "Gardevoir",
    "Togepi", "Togetic", "Togekiss",
    "Mimikyu", "Hatenna", "Hattrem", "Hatterene"
}

ditto_egg = {
    "Ditto"
}

grass_egg = {
    "Oddish", "Gloom", "Vileplume", "Bellossom",
    "Bellsprout", "Weepinbell", "Victreebel",
    "Exeggcute", "Exeggutor",
    "Roselia", "Roserade",
    "Cherubi", "Cherrim",
    "Foongus", "Amoonguss",
    "Lilligant", "Petilil", "Leafeon"
}

dragon_egg = {
    "Dratini", "Dragonair", "Dragonite",
    "Bagon", "Shelgon", "Salamence",
    "Gible", "Gabite", "Garchomp",
    "Axew", "Fraxure", "Haxorus",
    "Deino", "Zweilous", "Hydreigon",
    "Goomy", "Sliggoo", "Goodra",
    "Jangmo-o", "Hakamo-o", "Kommo-o",
    "Dreepy", "Drakloak", "Dragapult"
}

no_eggs_discovered_egg = {
    "Articuno", "Zapdos", "Moltres", "Mewtwo", "Mew",
    "Lugia", "Ho-Oh", "Kyogre", "Groudon", "Rayquaza",
    "Dialga", "Palkia", "Giratina", "Arceus",
    "Reshiram", "Zekrom", "Kyurem",
    "Xerneas", "Yveltal", "Zygarde",
    "Solgaleo", "Lunala", "Necrozma",
    "Zacian", "Zamazenta", "Eternatus",
    "Kubfu", "Urshifu", "Calyrex"
}

gender_unknown_egg = {
    "Magnemite", "Magneton", "Magnezone",
    "Beldum", "Metang", "Metagross",
    "Porygon", "Porygon2", "Porygon-Z",
    "Rotom", "Staryu", "Starmie",
    "Bronzor", "Bronzong", "Cryogonal",
    "Carbink", "Minior", "Dhelmise"
}


# === Fungsi Kategori Tambahan ===
def get_category(name):
    if name in starters:
        return "Starter"
    elif name in fossils:
        return "Fossil"
    elif name in pseudo:
        return "Pseudo"
    elif name in ultra_beasts:
        return "Ultra Beast"
    elif name in legendary:
        return "Legendary"
    elif name in mythical:
        return "Mythical"
    elif name in evolve_with_item:
        return "Item Evolution"
    elif name in evolve_with_happiness:
        return "Happiness Evolution"
    elif name in evolve_knowing_move:
        return "Move Evolution"
    elif name in cannot_evolve:
        return "Cannot Evolve"
    else:
        return "Basic"
    
    # === Fungsi Kategori Tambahan ===
def get_egg_group(name):
    if name in monster_egg:
        return "Monster"
    elif name in human_like_egg:
        return "Human-Like"
    elif name in water1_egg:
        return "Water 1"
    elif name in water2_egg:
        return "Water 2"
    elif name in water3_egg:
        return "Water 3"
    elif name in bug_egg:
        return "Bug"
    elif name in mineral_egg:
        return "Mineral"
    elif name in flying_egg:
        return "Flying"
    elif name in amorphous_egg:
        return "Amorphous"
    elif name in field_egg:
        return "Field"
    elif name in fairy_egg:
        return "Fairy"
    elif name in ditto_egg:
        return "Ditto"
    elif name in grass_egg:
        return "Grass"
    elif name in dragon_egg:
        return "Dragon"
    elif name in no_eggs_discovered_egg:
        return "No Eggs Discovered"
    elif name in gender_unknown_egg:
        return "Gender Unknown"
    else:
        return "Unknown"


# === Konversi ke format sederhana ===
simplified = []
for p in pokedex:
    profile = p.get("profile", {})
    egg_groups = profile.get("egg", ["Unknown"])
    evo_method = determine_evo_method(p.get("evolution", {}))
    gen, region = get_gen_region(p["id"])

    # === Ganti format type: jika 2 tipe, gabungkan pakai "/" ===
    types = p.get("type", [])
    if isinstance(types, list):
        type_str = "/".join(types)
    else:
        type_str = types

    simplified.append({
        "id": p["id"],
        "name": p["name"]["english"],
        "type": type_str,  # sudah diformat pakai "/"
        "eggGroup": egg_groups,
        "category": get_category(p["name"]["english"]),
        "evoMethod": evo_method,
        "generation": gen,
        "region": region
    })

# === Tampilkan hasil satu baris per Pokémon ===
for entry in simplified:
    print(json.dumps(entry, ensure_ascii=False))