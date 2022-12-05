
/* 
 static database of languages that DeepL can translate
 #"lang" is what should appear in drop down, code is 
 #what API recognizes when doing the translation
 # refer to: https://www.deepl.com/docs-api/translate-text/translate-text/ for list of languages
 */
db = sdb.getSiblingDB("langs");
db.langs.insertMany([{_id: 1,lang: "Bulgarian",code: "BG"},
                    {_id: 2,lang: "Czech",code: "CS"},
                    {_id: 3,lang: "Danish",code: "DA"},
                    {_id: 4,lang: "German",code: "DE"},
                    {_id: 5,lang: "Greek",code: "EL"},
                    {_id: 6,lang: "English",code: "EN"},
                    {_id: 7,lang: "Spanish",code: "ES"},
                    {_id: 9,lang: "Estonian",code: "ET"},
                    {_id: 10,lang: "Finnish",code: "FI"},
                    {_id: 11,lang: "French",code: "FR"},
                    {_id: 12,lang: "Hungarian",code: "HU"},
                    {_id: 13,lang: "Italian",code: "IT"},
                    {_id: 14,lang: "Japanese",code: "JA"},
                    {_id: 15,lang: "Lithuanian",code: "LT"},
                    {_id: 16,lang: "Latvian",code: "LV"},
                    {_id: 17,lang: "Dutch",code: "NL"},
                    {_id: 18,lang: "Polish",code: "PL"},
                    {_id: 19,lang: "Portuguese",code: "PT-BR"}, //Portuguese (Brazilian)
                    {_id: 20,lang: "Portuguese",code: "PT-PT"}, //Portuguese (all Portuguese varieties excluding Brazilian
                    {_id: 21,lang: "Romanian",code: "RO"},
                    {_id: 22,lang: "Russian",code: "RU"},
                    {_id: 23,lang: "Slovak",code: "SK"},
                    {_id: 24,lang: "Slovenian",code: "SL"},
                    {_id: 25,lang: "Swedish",code: "SV"},
                    {_id: 26,lang: "Turkish",code: "TR"},
                    {_id: 27,lang: "Ukrainian",code: "UK"},
                    {_id: 28,lang: "Chinese",code: "ZH"},
                    ]);