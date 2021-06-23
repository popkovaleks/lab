Mostly, preprocessed and not preprocessed questions gives similar responses. Sometimes, preprocessed questions gives better result:

        "id": "486",
        "question": "How many mammals are in the Chordate phylum?",
        "question_preprocessed": ["How", "many", "mammal", "Chordate","phylum"],
        "named_entities": {
            "http://dbpedia.org/resource/Chordate": "Chordate",
            "http://dbpedia.org/resource/Phylum": "phylum"
        },
        "named_entities_preprocessed": {
            "http://dbpedia.org/resource/Mammal": "mammal",
            "http://dbpedia.org/resource/Chordate": "Chordate",
            "http://dbpedia.org/resource/Phylum": "phylum"
	}

Also, sometimes preprocessed and not preprocessed questions gives completly different results:

        "id": "1962",
        "question": "List the battles fought by Roh Tae-woo ?",
        "question_preprocessed": ["List", "battle", "fought", "Roh", "Taewoo"],
        "named_entities": {
            "http://dbpedia.org/resource/Roh_Tae-woo": "Roh Tae-woo"
        },
        "named_entities_preprocessed": {
            "http://dbpedia.org/resource/Battle": "battle"
        }
    

Randomly taken questions:
Question ID: 655
List some leaders of regions in the Indian Standard Time Zone?
Manualy: { "http://dbpedia.org/resource/Indian": "Indian", "http://dbpedia.org/resource/Time_Zone": "Time Zone"}
"named_entities": {"http://dbpedia.org/resource/Indian_Standard_Time": "Indian Standard Time"}
------------------------------
Question ID: 373
What is the awards given to the horse whose grandson is the famous Counterpoint?
Manualy: {"http://dbpedia.org/resource/Counterpoint": "Counterpoint", "http://dbpedia.org/resource/horse": "horse"}
"named_entities": { "http://dbpedia.org/resource/Horse": "horse", "http://dbpedia.org/resource/Counterpoint": "Counterpoint"}
------------------------------
Question ID: 3049
Who was the silver medalist of Gymnastics at the 2008 Summer Olympics  Women's artistic individual all-around ?
Manualy: {"http://dbpedia.org/resource/medalist": "medalist", "http://dbpedia.org/resource/Gymnastics": "Gymnastycs", "http://dbpedia.org/resource/Olympics": "Olympics"}
"named_entities": {"http://dbpedia.org/resource/Gymnastics_at_the_2008_Summer_Olympics": "2008 Summer Olympics"}
------------------------------
Question ID: 3024
Who have children named James Roosevelt and Franklin Delano Roosevelt, Jr.?
Manualy: {"http://dbpedia.org/resource/James_Roosevelt": "James Roosevelt", "http://dbpedia.org/resource/Franklin_Delano_Roosevelt,_Jr"}
"named_entities": {"http://dbpedia.org/resource/James_Roosevelt_I": "James Roosevelt", "http://dbpedia.org/resource/Franklin_Delano_Roosevelt_Jr.": "Franklin Delano Roosevelt, Jr."}
------------------------------
Question ID: 3181
What are the television shows whose distributer is HBO?
Manualy: {"http://dbpedia.org/resource/television": "television", "http://dbpedia.org/resource/HBO": "HBO"}
"named_entities": {"http://dbpedia.org/resource/HBO": "HBO"}