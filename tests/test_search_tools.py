from tools.search_tools import DuckDuckGoSearch


def test_search_internet():
    response = DuckDuckGoSearch()._run("bananas")
    assert response == [
        {
            "FirstURL": "https://duckduckgo.com/Banana",
            "Icon": {"Height": "", "URL": "/i/8b26b6d5.jpg", "Width": ""},
            "Result": '<a href="https://duckduckgo.com/Banana">Banana</a> An elongated, edible fruit – botanically a berry – produced by several kinds of large...',
            "Text": "Banana An elongated, edible fruit – botanically a berry – produced by several kinds of large...",
        },
        {
            "FirstURL": "https://duckduckgo.com/Savannah_Bananas",
            "Icon": {"Height": "", "URL": "", "Width": ""},
            "Result": '<a href="https://duckduckgo.com/Savannah_Bananas">Savannah Bananas</a>An exhibition barnstorming baseball team based in Savannah, Georgia.',
            "Text": "Savannah Bananas An exhibition barnstorming baseball team based in Savannah, Georgia.",
        },
        {
            "FirstURL": "https://duckduckgo.com/Banana_equivalent_dose",
            "Icon": {"Height": "", "URL": "/i/6774b256.jpg", "Width": ""},
            "Result": '<a href="https://duckduckgo.com/Banana_equivalent_dose">Banana equivalent dose</a>An informal unit of measurement of ionizing radiation exposure, intended as a general educational...',
            "Text": "Banana equivalent dose An informal unit of measurement of ionizing radiation exposure, intended as a general educational...",
        },
        {
            "Name": "In nature",
            "Topics": [
                {
                    "FirstURL": "https://duckduckgo.com/Ensete_ventricosum",
                    "Icon": {"Height": "", "URL": "/i/5b89aac1.jpg", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Ensete_ventricosum">Ensete ventricosum</a> A species of flowering plant in the banana family Musaceae.',
                    "Text": "Ensete ventricosum A species of flowering plant in the banana family Musaceae.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Nymphoides_aquatica",
                    "Icon": {"Height": "", "URL": "/i/f15c3d19.jpg", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Nymphoides_aquatica">Nymphoides aquatica</a> An aquatic plant in the Menyanthaceae, native to the southeastern United States from Texas to...',
                    "Text": "Nymphoides aquatica An aquatic plant in the Menyanthaceae, native to the southeastern United States from Texas to...",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Strelitzia_nicolai",
                    "Icon": {"Height": "", "URL": "/i/65fe33f6.jpg", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Strelitzia_nicolai">Strelitzia nicolai</a> A species of banana-like plants with erect woody stems reaching a height of 7–8 m, and the...',
                    "Text": "Strelitzia nicolai A species of banana-like plants with erect woody stems reaching a height of 7–8 m, and the...",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Banana_spider",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Banana_spider">Banana spider</a>Banana spider may refer to: • Cupiennius, a South and Central American genus of spiders •...',
                    "Text": "Banana spider Banana spider may refer to: • Cupiennius, a South and Central American genus of spiders •...",
                },
            ],
        },
        {
            "Name": "Places",
            "Topics": [
                {
                    "FirstURL": "https://duckduckgo.com/Banana%2C_Cape_Verde",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Banana%2C_Cape_Verde">Banana, Cape Verde</a>A settlement in the central part of the island of Santiago, Cape Verde.',
                    "Text": "Banana, Cape Verde A settlement in the central part of the island of Santiago, Cape Verde.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Banana%2C_Democratic_Republic_of_the_Congo",
                    "Icon": {"Height": "", "URL": "/i/d6e53b9c.png", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Banana%2C_Democratic_Republic_of_the_Congo">Banana, Democratic Republic of the Congo</a>A small seaport in the Kongo Central province of the Democratic Republic of the Congo on the...',
                    "Text": "Banana, Democratic Republic of the Congo A small seaport in the Kongo Central province of the Democratic Republic of the Congo on the...",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Banana%2C_Florida",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Banana%2C_Florida">Banana, Florida</a>An unincorporated community in Putnam County, Florida, located one mile south of Melrose on State...',
                    "Text": "Banana, Florida An unincorporated community in Putnam County, Florida, located one mile south of Melrose on State...",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Banana%2C_Kiribati",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Banana%2C_Kiribati">Banana, Kiribati</a>A village in Kiribati, located on the island of Kiritimati, within the Archipelago of Line Islands.',
                    "Text": "Banana, Kiribati A village in Kiribati, located on the island of Kiritimati, within the Archipelago of Line Islands.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Banana_Lake",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Banana_Lake">Banana Lake</a>A 268-acre natural freshwater lake in southeast Lakeland, Florida.',
                    "Text": "Banana Lake A 268-acre natural freshwater lake in southeast Lakeland, Florida.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Banana_River",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Banana_River">Banana River</a>A 31-mile-long lagoon that lies between Cape Canaveral and Merritt Island in Brevard County...',
                    "Text": "Banana River A 31-mile-long lagoon that lies between Cape Canaveral and Merritt Island in Brevard County...",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Shire_of_Banana",
                    "Icon": {"Height": "", "URL": "/i/8598af23.png", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Shire_of_Banana">Shire of Banana</a>A local government area located in the Capricorn region of Queensland, Australia, inland from the...',
                    "Text": "Shire of Banana A local government area located in the Capricorn region of Queensland, Australia, inland from the...",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Banana%2C_Queensland",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Banana%2C_Queensland">Banana, Queensland</a>A rural town and locality in the Shire of Banana, Queensland, Australia.',
                    "Text": "Banana, Queensland A rural town and locality in the Shire of Banana, Queensland, Australia.",
                },
            ],
        },
        {
            "Name": "Arts and entertainment",
            "Topics": [
                {
                    "FirstURL": "https://duckduckgo.com/Bananas_(film)",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Bananas_(film)">Bananas (film)</a>A 1971 American comedy film directed by Woody Allen and starring Allen, Louise Lasser, and Carlos...',
                    "Text": "Bananas (film) A 1971 American comedy film directed by Woody Allen and starring Allen, Louise Lasser, and Carlos...",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Bananas!*",
                    "Icon": {"Height": "", "URL": "/i/30184979.jpg", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Bananas!*">Bananas!*</a> Bananas! is a 2009 Swedish documentary directed by Fredrik Gertten about a conflict between...',
                    "Text": "Bananas!* Bananas! is a 2009 Swedish documentary directed by Fredrik Gertten about a conflict between...",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Banana_(film)",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Banana_(film)">Banana (film)</a>A 2015 comedy-drama film written and directed by Andrea Jublin.',
                    "Text": "Banana (film) A 2015 comedy-drama film written and directed by Andrea Jublin.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/The_Bananas_(TV_series)",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/The_Bananas_(TV_series)">The Bananas (TV series)</a> A Canadian children\'s television series which aired on CBC Television in 1969.',
                    "Text": "The Bananas (TV series) A Canadian children's television series which aired on CBC Television in 1969.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Banana_(TV_series)",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Banana_(TV_series)">Banana (TV series)</a>A 2015 British television series created by Russell T Davies and aired on E4.',
                    "Text": "Banana (TV series) A 2015 British television series created by Russell T Davies and aired on E4.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Banana_(band)",
                    "Icon": {"Height": "", "URL": "/i/57e8e2f5.jpg", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Banana_(band)">Banana (band)</a>A Yugoslav pop rock band formed in Belgrade in 1985.',
                    "Text": "Banana (band) A Yugoslav pop rock band formed in Belgrade in 1985.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Bananas_(Deep_Purple_album)",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Bananas_(Deep_Purple_album)">Bananas (Deep Purple album)</a>The 17th studio album by English rock band Deep Purple, released on 25 August 2003 via EMI...',
                    "Text": "Bananas (Deep Purple album) The 17th studio album by English rock band Deep Purple, released on 25 August 2003 via EMI...",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Bananas_(Malcolm_Middleton_album)",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Bananas_(Malcolm_Middleton_album)">Bananas (Malcolm Middleton album)</a>The tenth studio album by Scottish singer-songwriter Malcolm Middleton, and the seventh under his...',
                    "Text": "Bananas (Malcolm Middleton album) The tenth studio album by Scottish singer-songwriter Malcolm Middleton, and the seventh under his...",
                },
                {
                    "FirstURL": "https://duckduckgo.com/The_Velvet_Underground_%26_Nico",
                    "Icon": {"Height": "", "URL": "/i/dd887e52.jpg", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/The_Velvet_Underground_%26_Nico">The Velvet Underground & Nico</a> The debut studio album by the American rock band the Velvet Underground and the German singer...',
                    "Text": "The Velvet Underground & Nico The debut studio album by the American rock band the Velvet Underground and the German singer...",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Banana_(Anitta_song)",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Banana_(Anitta_song)">"Banana" (Anitta song)</a>A song by Brazilian singer Anitta featuring American singer Becky G. It was released through...',
                    "Text": '"Banana" (Anitta song) A song by Brazilian singer Anitta featuring American singer Becky G. It was released through...',
                },
                {
                    "FirstURL": "https://duckduckgo.com/Banana_(Conkarah_song)",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Banana_(Conkarah_song)">"Banana" (Conkarah song)</a>A song by the Jamaican reggae artist Conkarah featuring the Jamaican international artist Shaggy.',
                    "Text": '"Banana" (Conkarah song) A song by the Jamaican reggae artist Conkarah featuring the Jamaican international artist Shaggy.',
                },
                {
                    "FirstURL": "https://duckduckgo.com/?q=Bananas%20(Who%20You%20Gonna%20Call%3F)",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '"<a href="https://duckduckgo.com/?q=Bananas%20(Who%20You%20Gonna%20Call%3F)">Bananas (Who You Gonna Call?)</a>" The first single from Queen Latifah\'s fourth studio album, Order in the Court.',
                    "Text": '"Bananas (Who You Gonna Call?) " The first single from Queen Latifah\'s fourth studio album, Order in the Court.',
                },
                {
                    "FirstURL": "https://duckduckgo.com/Day-O_(The_Banana_Boat_Song)",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '"<a href="https://duckduckgo.com/Day-O_(The_Banana_Boat_Song)">Day-O (The Banana Boat Song)</a>" A traditional Jamaican folk song.',
                    "Text": '"Day-O (The Banana Boat Song) " A traditional Jamaican folk song.',
                },
                {
                    "FirstURL": "https://duckduckgo.com/WWBN",
                    "Icon": {"Height": "", "URL": "/i/25ce079f.jpg", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/WWBN">WWBN</a>A radio station broadcasting mainstream rock to Flint and The Thumb areas of Michigan.',
                    "Text": "WWBN A radio station broadcasting mainstream rock to Flint and The Thumb areas of Michigan.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Bananas_(literary_magazine)",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Bananas_(literary_magazine)">Bananas (literary magazine)</a>A British literary magazine that ran for 26 issues from January 1975 until April 1981.',
                    "Text": "Bananas (literary magazine) A British literary magazine that ran for 26 issues from January 1975 until April 1981.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Banana_(magazine)",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Banana_(magazine)">Banana (magazine)</a>An Asian American themed magazine founded by Vicki Ho and Kathleen Tso.',
                    "Text": "Banana (magazine) An Asian American themed magazine founded by Vicki Ho and Kathleen Tso.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Banana_(1986_video_game)",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Banana_(1986_video_game)">Banana (1986 video game)</a>A fixed screen puzzle video game produced by Victor Musical Industries that was released...',
                    "Text": "Banana (1986 video game) A fixed screen puzzle video game produced by Victor Musical Industries that was released...",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Banana_(2024_video_game)",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Banana_(2024_video_game)">Banana (2024 video game)</a>A 2024 free-to-play clicker game released through Steam.',
                    "Text": "Banana (2024 video game) A 2024 free-to-play clicker game released through Steam.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Bananas_Comedy_Club",
                    "Icon": {
                        "Height": 16,
                        "URL": "/i/www.bananascomedyclub.com.ico",
                        "Width": 16,
                    },
                    "Result": '<a href="https://duckduckgo.com/Bananas_Comedy_Club">Bananas Comedy Club</a>Bananas Comedy Club are two venues for stand-up comedy: the original founded in 1986 in...',
                    "Text": "Bananas Comedy Club Bananas Comedy Club are two venues for stand-up comedy: the original founded in 1986 in...",
                },
            ],
        },
        {
            "Name": "People",
            "Topics": [
                {
                    "FirstURL": "https://duckduckgo.com/Banana_(gamer)",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Banana_(gamer)">Banana (gamer)</a>A Chinese Dota 2 player who is currently the coach for Newbee.',
                    "Text": "Banana (gamer) A Chinese Dota 2 player who is currently the coach for Newbee.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Banana%2C_Coconut%2C_and_Twinkie",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Banana%2C_Coconut%2C_and_Twinkie">Banana (slur)</a>Banana, Coconut, and Twinkie are pejorative terms, primarily used for Asian Americans who are...',
                    "Text": "Banana (slur) Banana, Coconut, and Twinkie are pejorative terms, primarily used for Asian Americans who are...",
                },
            ],
        },
        {
            "Name": "Other uses",
            "Topics": [
                {
                    "FirstURL": "https://duckduckgo.com/Banana_equivalent_dose",
                    "Icon": {"Height": "", "URL": "/i/6774b256.jpg", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Banana_equivalent_dose">Banana equivalent dose</a>An informal unit of measurement of ionizing radiation exposure, intended as a general educational...',
                    "Text": "Banana equivalent dose An informal unit of measurement of ionizing radiation exposure, intended as a general educational...",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Savannah_Bananas",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Savannah_Bananas">Savannah Bananas</a>An exhibition barnstorming baseball team based in Savannah, Georgia.',
                    "Text": "Savannah Bananas An exhibition barnstorming baseball team based in Savannah, Georgia.",
                },
            ],
        },
        {
            "Name": "See also",
            "Topics": [
                {
                    "FirstURL": "https://duckduckgo.com/Joseph_Bonanno",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Joseph_Bonanno">Joseph Bonanno</a>An Italian-American crime boss of the Bonanno crime family, which he ran from 1931 to 1968.',
                    "Text": "Joseph Bonanno An Italian-American crime boss of the Bonanno crime family, which he ran from 1931 to 1968.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Antonio_Caponigro",
                    "Icon": {"Height": "", "URL": "/i/f3893821.jpg", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Antonio_Caponigro">Antonio Caponigro</a>The consigliere of Angelo Bruno in the Philadelphia crime family.',
                    "Text": "Antonio Caponigro The consigliere of Angelo Bruno in the Philadelphia crime family.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Bannana",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Bannana">Bannana</a> A genus of goblin spiders native to Xishuangbanna prefecture, Yunnan Province, China, where it...',
                    "Text": "Bannana A genus of goblin spiders native to Xishuangbanna prefecture, Yunnan Province, China, where it...",
                },
                {
                    "FirstURL": "https://duckduckgo.com/Banania",
                    "Icon": {"Height": "", "URL": "/i/44907cf1.jpg", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/Banania">Banania</a>A popular chocolate drink found most widely distributed in France.',
                    "Text": "Banania A popular chocolate drink found most widely distributed in France.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/d/Banana_Island",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": "<a href=\"https://duckduckgo.com/d/Banana_Island\">Banana Island</a> See related meanings for the phrase 'Banana Island'.",
                    "Text": "Banana Island See related meanings for the phrase 'Banana Island'.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/d/Banana_(name)",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": '<a href="https://duckduckgo.com/d/Banana_(name)">Banana (name)</a> A list of people with the given name, surname, pen name or stage name.',
                    "Text": "Banana (name) A list of people with the given name, surname, pen name or stage name.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/d/Banana_boat",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": "<a href=\"https://duckduckgo.com/d/Banana_boat\">Banana boat</a> See related meanings for the phrase 'Banana boat'.",
                    "Text": "Banana boat See related meanings for the phrase 'Banana boat'.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/d/Banana_fish",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": "<a href=\"https://duckduckgo.com/d/Banana_fish\">Banana fish</a> See related meanings for the phrase 'Banana fish'.",
                    "Text": "Banana fish See related meanings for the phrase 'Banana fish'.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/d/Banana_Joe",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": "<a href=\"https://duckduckgo.com/d/Banana_Joe\">Banana Joe</a> See related meanings for the phrase 'Banana Joe'.",
                    "Text": "Banana Joe See related meanings for the phrase 'Banana Joe'.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/d/Banana_Man",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": "<a href=\"https://duckduckgo.com/d/Banana_Man\">Banana Man</a> See related meanings for the phrase 'Banana Man'.",
                    "Text": "Banana Man See related meanings for the phrase 'Banana Man'.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/d/Banana_republic",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": "<a href=\"https://duckduckgo.com/d/Banana_republic\">Banana republic</a> See related meanings for the phrase 'Banana republic'.",
                    "Text": "Banana republic See related meanings for the phrase 'Banana republic'.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/d/Banana_Split",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": "<a href=\"https://duckduckgo.com/d/Banana_Split\">Banana Split</a> See related meanings for the phrase 'Banana Split'.",
                    "Text": "Banana Split See related meanings for the phrase 'Banana Split'.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/d/Anana",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": "<a href=\"https://duckduckgo.com/d/Anana\">Anana</a> See related meanings for the word 'Anana'.",
                    "Text": "Anana See related meanings for the word 'Anana'.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/d/Bana",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": "<a href=\"https://duckduckgo.com/d/Bana\">Bana</a> See related meanings for the word 'Bana'.",
                    "Text": "Bana See related meanings for the word 'Bana'.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/d/Banan",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": "<a href=\"https://duckduckgo.com/d/Banan\">Banan</a> See related meanings for the word 'Banan'.",
                    "Text": "Banan See related meanings for the word 'Banan'.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/d/Bananana",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": "<a href=\"https://duckduckgo.com/d/Bananana\">Bananana</a> See related meanings for the word 'Bananana'.",
                    "Text": "Bananana See related meanings for the word 'Bananana'.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/d/Banani",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": "<a href=\"https://duckduckgo.com/d/Banani\">Banani</a> See related meanings for the word 'Banani'.",
                    "Text": "Banani See related meanings for the word 'Banani'.",
                },
                {
                    "FirstURL": "https://duckduckgo.com/d/Going_bananas",
                    "Icon": {"Height": "", "URL": "", "Width": ""},
                    "Result": "<a href=\"https://duckduckgo.com/d/Going_bananas\">Going bananas</a> See related meanings for the phrase 'Going bananas'.",
                    "Text": "Going bananas See related meanings for the phrase 'Going bananas'.",
                },
            ],
        },
    ]
