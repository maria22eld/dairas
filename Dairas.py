state_transition_model = {

    "Blida": {
        "Coordinates": (36.4741032067536, 2.826586552782758),
        "Neighbors": [
            {"Chiffa": 9.4}, 
            {"Bouarfa": 2.4}, 
            {"Chrea": 19.0}, 
            {"Ouled Yaich": 4.2}, 
            {"Beni Mered": 6.3},  # Ajout d'une virgule ici
            {"Beni Tamou": 9.3}, 
            {"Oued Alleug": 14.2}
        ],
        "Willaya": "Blida"
    },

    "Chebli": {
        "Coordinates": (36.57831599655627, 3.01152857562588),
        "Neighbors": [
            {"Boufarik": 9.6}, 
            {"Bouinan": 6.0}, 
            {"Hammam Melouane": 18.6}, 
            {"Bougara": 11.5},
            {"Birtouta": 8.6}
        ],
        "Willaya": "Blida"
    },

    "Oued Djer": {
        "Coordinates": (36.428906765802076, 2.5621818269117917),
        "Neighbors": [
            {"El Affroun": 9.9},
            {"Ahmar El Ain": 14.3},
            {"Boumedfaa": 15.4}
        ],
        "Willaya": "Blida"
    },

    "El Affroun": {
        "Coordinates": (36.47047492005072, 2.633583337599322),
        "Neighbors": [{"Oued Djer": 9.9}, {"Mouzaia": 6.0}, {"Ain Romana": 11.5}, {"Ahmar El Ain": 5.6},{"Kolea": 28.9},{"Boumedfaa":23}],
        "Willaya": "Blida"
    },

    "Ain Romana": {
        "Coordinates": (36.40732062250372, 2.6888110254239312),
        "Neighbors": [{"El Affroun": 11.5}, {"Mouzaia": 7.0}, {"Chiffa": 12.0}, {"Boumedfaa": 31.6}, {"Medea": 39.1}],
        "Willaya": "Blida"
    },

    "Chiffa": {
        "Coordinates": (36.46539908778476, 2.7393049114350028),
        "Neighbors": [{"Ain Romana": 12.0}, {"Mouzaia": 4.6}, {"Oued Alleug": 15.2}, {"Blida": 9.3}, {"Bouarfa": 7.9}, {"Medea": 28.0}],
        "Willaya": "Blida"
    },

    "Mouzaia": {
        "Coordinates": (36.46539908778476, 2.690783442846239),
        "Neighbors": [{"El Affroun": 6.0}, {"Ain Romana": 7.0}, {"Chiffa": 4.6}, {"Oued Alleug": 21.5}, {"Kolea": 32.7}],
        "Willaya": "Blida"
    },



   "Bouarfa" :{
        "Coordinates" : (36.4652381720533, 2.816596178892667),
        "Neighbors": [{"Chiffa": 7.9 }, {"Blida": 2.4 }, {"Chrea": 20.1 },{"Ouzera": 37.9 }],
        "Willaya" : "Blida"

    },



   "Oued Alleug" :{
        "Coordinates" : (36.553325499473914, 2.7888957995566512),
        "Neighbors": [{"Mouzaia": 14.4 }, {"Chiffa": 13.7 }, {"Blida": 14.2 }, {"Beni Tamou": 4.3 }, {"Ben Khellil": 18.2},{"Kolea":10.5 }],
        "Willaya" : "Blida"

    },



   "Beni Tamou" :{
        "Coordinates" : (36.53432349833731, 2.8172781178199635),
        "Neighbors": [{"Oued Alleug": 4.3 }, {"Ben Khellil": 20.6 }, {"Blida": 9.0 }, {"Beni Mered": 5.0 }],
        "Willaya" : "Blida"

    },



   "Ben Khellil" :{
        "Coordinates" : (36.62106125660057, 2.875882351020216),
        "Neighbors": [{"Oued Alleug": 18.3 }, {"Beni Tamou": 19.6 }, {"Beni Mered": 14.3 }, {"Boufarik": 6.9 },{"Zeralda": 13.8 },{"Birtouta": 22.1 },{"Kolea": 18.2 }],
        "Willaya" : "Blida"

    },



  "Beni Mered" :{
        "Coordinates" : (36.525509751664785, 2.863136436227628),
        "Neighbors": [{"Beni Tamou": 8.0 }, {"Ouled Yaich": 2.8}, {"Ben Khellil": 14.3}, {"Boufarik": 9.7 }, {"Guerouaou": 2.3},{"Blida":6.3}],
        "Willaya" : "Blida"

    },



   "Ouled Yaich" :{
        "Coordinates" : (36.50081661154862, 2.863914429326328),
        "Neighbors": [{"Beni Mered": 2.6 }, {"Blida": 4.1 }, {"Chrea": 23.4 }, {"Guerouaou": 4.9 }],
        "Willaya" : "Blida"

    },



   "Chrea" :{
        "Coordinates" : (36.427305785214045, 2.8763505194564667),
        "Neighbors": [{"Bouarfa": 20.1 }, {"Hammam Melouane": 29.2}, {"Blida": 19.0 }, {"Bouinan": 33.3}, {"Guerouaou": 27.6}, {"Soumaa": 28.1 }, {"Ouled Yaich": 23.4 },{"Ouzera": 57.2 }],
        "Willaya" : "Blida"

    },
   "Boufarik" :{
        "Coordinates" : (36.58374500919057, 2.9121042790330156),
        "Neighbors": [{"Beni Mered": 10.2 }, {"Soumaa": 7.6}, {"Bouinan": 11.6 }, {"Chebli": 10.3 }, {"Ben Khellil": 6.9 }, {"Guerouaou": 11.7 },{"Birtouta": 10.8 }],
        "Willaya" : "Blida"

    },



   "Guerouaou" :{
        "Coordinates" : (36.53127139744326, 2.8792220560315003),
        "Neighbors": [{"Soumaa": 4.5 }, {"Ouled Yaich": 4.9}, {"Beni Mered": 2.3}, {"Boufarik": 11.7}, {"Chrea": 27.7}],
        "Willaya" : "Blida"

    },


   "Soumaa" :{
        "Coordinates" : (36.51996313002439, 2.9069456488336565),
        "Neighbors": [{"Chrea": 28.2}, {"Bouinan": 8.1 }, {"Boufarik": 14.6 }, {"Guerouaou": 4.5 }],
        "Willaya" : "Blida"

    },



   "Bouinan" :{
        "Coordinates" : (36.53199178317244, 2.9654799637533356),
        "Neighbors": [{"Hammam Melouane": 12.5 }, {"Chebli": 6.0 }, {"Boufarik": 11.6 }, {"Chrea": 33.4 }, {"Soumaa": 8.1 }],
        "Willaya" : "Blida"

    },


    "Hammam Melouane" :{
        "Coordinates" : (36.489714207271746, 3.046979885509021),
        "Neighbors": [{"Chrea": 29.2 }, {"Bouinan": 12.5 }, {"Bougara": 8.0 }, {"Chebli": 18.6},{"Ouzera":93.6 },{"El Omaria": 31.4 }],
        "Willaya" : "Blida"

    },


    "Bougara" :{
        "Coordinates" : (36.54193775035584, 3.0811357835448168),
        "Neighbors": [{"Ouled Selama": 3.0 }, {"Chebli": 11.6 }, {"Hammam Melouane": 8.0 },{"El Omaria": 56.9 },{"Tablat": 43.3 }],
        "Willaya" : "Blida"

    },


    "Larbaa" :{
        "Coordinates" : (36.56759024798607, 3.153057547644913),
        "Neighbors": [{"Djebabra": 14.5 }, {"Meftah": 10.0}, {"Souhane": 16.3}, {"Ouled Selama": 4.5 },{"Baraki": 12.7 }],
        "Willaya" : "Blida"

    },

    "Meftah" :{
        "Coordinates" : (36.622881427422485, 3.223590862872602),
        "Neighbors": [{"Djebabra": 10.6}, {"Larbaa": 9.8 },{"Dar El Beida": 24.9 },{"Khemis El Khechna": 10.4}],
        "Willaya" : "Blida"

    },



    "Ouled Selama" :{
        "Coordinates" : (36.55197669884579, 3.1114040183958958),
        "Neighbors": [{"Souhane": 21.2}, {"Larbaa": 4.4 }, {"Bougara": 3.1 },{"Baraki": 16.4 },{"Tablat": 40.2 }],
        "Willaya" : "Blida"

    },



    "Djebabra" :{
        "Coordinates" : (36.583231348877376, 3.2666665493422817),
        "Neighbors": [{"Meftah": 10.6 }, {"Larbaa": 16.2 }, {"Souhane": 17.6 },{"Lakhdaria": 64.1 },{"Khemis El Khechna": 15.7 }],
        "Willaya" : "Blida"

    },


    "Souhane" :{
        "Coordinates" : (36.50983509174763, 3.2386198383405964),
        "Neighbors": [{"Djebabra": 17.6 }, {"Larbaa": 16.3 }, {"Ouled Selama": 21.2 },{"Lakhdaria": 79.8 },{"Tablat": 19.1 }],
        "Willaya" : "Blida"

    },
  

    "In Salah" :{
        "Coordinates" : (27.210060406284356, 2.4904632612330087),
        "Neighbors": [{"In Ghar": 63.0 }, {"In Amguel": 536 }, {"Foggaret Ezzaouia": 47.0 },{"Aoulef": 151.0 },{"Hassi Massouad": 887 },{"El Meniaa": 402}],
        "Willaya" : "Tamanrasset"

    },




    "In Ghar" :{
        "Coordinates" : (27.311406076968243, 1.9896187543853023),
        "Neighbors": [{"In Salah": 63.0 }, {"In Amguel": 599 },{"Aoulef": 91.4 },{"Reggane": 188.0 }],
        "Willaya" : "Tamanrasset"

    },




    "In Amguel" :{
        "Coordinates" : (23.830361320318797, 5.297627935226057),
        "Neighbors": [{"In Ghar": 599 }, {"In Salah": 536 }, {"Idles": 105 }, {"Tamanrasset": 130 }, {"Foggaret Ezzaouia": 581 },{"Abalessa": 129 },{"Reggane": 783}],
        "Willaya" : "Tamanrasset"

    },



    "In Guezzam" :{
        "Coordinates" : (19.7627243849607, 5.797436786473662),
        "Neighbors": [{"Tamanrasset": 389 }, {"Tazrouk": 673 }, {"Abalessa": 476 }, {"Tin Zaouatine": 889 }],
        "Willaya" : "Tamanrasset"

    },



    "Idles" :{
        "Coordinates" : (23.939014196530856, 5.880438431645519),
        "Neighbors": [{"Tamanrasset": 219 }, {"Foggaret Ezzaouia": 685 }, {"In Amguel": 105 }, {"Tazrouk": 75.7 },{"Djanet": 470 },{"In Amenas": 846 },{"Illizi": 603 }],
        "Willaya" : "Tamanrasset"

    },


    "Foggaret Ezzaouia" :{
        "Coordinates" : (27.337004950100958, 3.2375335091589426),
        "Neighbors": [{"In Salah": 47.0 }, {"Idles": 685 }, {"In Amguel": 581 },{"Hassi Massouad": 914 },{"In Amenas": 846}],
        "Willaya" : "Tamanrasset"

    },






    "Abalessa" :{
        "Coordinates" : (22.912774124431873, 4.449115234270823),
        "Neighbors": [{"Tamanrasset": 88.6}, {"Tin Zaouatine": 418 }, {"In Guezzam": 476 }, {"In Amguel": 129 },{"Reggane": 912 }],
        "Willaya" : "Tamanrasset"

    },


    "Tin Zaouatine" :{
        "Coordinates" : (20.017830895267796, 2.9696181635987604),
        "Neighbors": [{"Abalessa": 418 }, {"In Guezzam": 889 }],
        "Willaya" : "Tamanrasset"

    },




    "Tamanrasset" :{
        "Coordinates" : (22.810627815230415, 5.543631085044264),
        "Neighbors": [{"In Guezzam": 390 }, {"Tazrouk": 290 }, {"Idles": 223 }, {"In Amguel": 135 }, {"Abalessa": 93.0 }],
        "Willaya" : "Tamanrasset"

    },



    "Tazrouk" :{
        "Coordinates" : (23.616934238353828, 6.157816611866387),
        "Neighbors": [{"In Guezzam": 673 }, {"Tamanrasset": 286 }, {"Idles": 75.7 },{"Djanet": 544 }],
        "Willaya" : "Tamanrasset"

    },
   

    "Tindouf" :{
        "Coordinates" : (27.677991009618154, -8.127715705660009),
        "Neighbors": [{"Oum El Assel": 174 },{"Reggane": 1167},{"Abadla": 540 }],
        "Willaya" : "Tindouf"

    },


  
    "Oum El Assel" :{
        "Coordinates" : (28.612939113919552, -6.971936931153814),
        "Neighbors": [{"Tindouf": 174 },{"Reggane": 1338}],
        "Willaya" : "Tindouf"

    },

    "Lakhdaria" :{
        "Coordinates" : (36.56400796072136, 3.596628948344861),
        "Neighbors": [{"Kadiria": 9.7 },{"Souk El Khemis": 48.3 },{"Djebabra": 64.1 },{"Souhane": 79.8 },{"Khemis El Khechna": 39.7},{"Tablat": 50.1 },{"El Azizia": 77.7 }],
        "Willaya" : "Bouira"

    },



    "Kadiria" :{
        "Coordinates" : (36.53420399247343, 3.679143922473989),
        "Neighbors": [{"Lakhdaria": 9.7 },{"Souk El Khemis": 35.9 },{"Ain Bessem": 54.6 },{"Bouira": 35.5},{"Tizi Ghenif": 16.6},{"Dra Lmizan": 22.4},{"Boudouaou": 61.8 }],
        "Willaya" : "Bouira"

    },




    "Souk El Khemis" :{
        "Coordinates" : (36.38449691281237, 3.633728704154857),
        "Neighbors": [{"Lakhdaria": 48.3 },{"Kadiria": 35.9},{"Ain Bessem": 12.4 },{"Bir Ghbalou": 25.3 },{"El Azizia": 34.3 }],
        "Willaya" : "Bouira"

    },

  


    "Bouira" :{
        "Coordinates" : (36.373167102583814, 3.8966252549024842),
        "Neighbors": [{"Kadiria": 36.4 },{"Ain Bessem": 24.9 },{"El Hachimia": 26.0 },{"Bechloul": 19.5 },{"Haizer": 11.1 },{"Boghni": 32.8 }],
        "Willaya" : "Bouira"

    },



    "Ain Bessem" :{
        "Coordinates" : (36.29535889002294, 3.6714681161935463),
        "Neighbors": [{"Bouira": 24.9 },{"Kadiria": 54.0},{"Souk El Khemis": 12.4 },{"Bir Ghbalou": 10.1},{"Sour El Ghozlane": 20.6},{"El Hachimia": 20.0}],
        "Willaya" : "Bouira"

    },



    "Bir Ghbalou" :{
        "Coordinates" : (36.26287288854417, 3.587673838282049),
        "Neighbors": [{"Sour El Ghozlane": 20.2 },{"Ain Bessem": 10.1},{"Souk El Khemis": 23.1 },{"El Azizia": 9.1 },{"El Guelb El Kebir": 16.4 }],
        "Willaya" : "Bouira"

    },




    "Haizer" :{
        "Coordinates" : (36.398399420041, 3.9989694107043503),
        "Neighbors": [{"Bouira": 10.0 },{"Bechloul": 18.0 },{"Ouadhia": 53.1 },{"Ouacifs": 53.5 },{"El Hachimia": 32.5 }],
        "Willaya" : "Bouira"

    },




    "Bechloul" :{
        "Coordinates" : (36.31249399031412, 4.074893851760491),
        "Neighbors": [{"Haizer": 18.0 },{"M'Chedallah": 22.2 },{"M'Chedallah": 19.5 },{"Bordj Okhriss": 39.7 },{"El Hachimia": 33.8 },{"Ouacifs": 56.3 },{"Ouadhia": 64.6 },{"Mansoura": 60 }],
        "Willaya" : "Bouira"

    },




    "El Hachimia" :{
        "Coordinates" : (36.21885995887722, 3.8140733005609304),
        "Neighbors": [{"Bouira": 26.1 },{"Ain Bessem": 17.5 },{"Sour El Ghozlane": 15.7 },{"Bordj Okhriss": 26.7 },{"Bechloul": 33.8 },{"Haizer": 32.5 }],
        "Willaya" : "Bouira"

    },





    "Sour El Ghozlane" :{
        "Coordinates" : (36.14459382326377, 3.6904771088091852),
        "Neighbors": [{"Bordj Okhriss": 30.3 },{"El Hachimia": 17.8 },{"Ain Bessem": 22.1 },{"Bir Ghbalou": 20.1 },{"Chellalet El Adhaoura": 60.9 },{"Souagui": 45.7 },{"El Guelb El Kebir": 35.9 },{"Sidi Aissa": 32.2 }],
        "Willaya" : "Bouira"

    },



    "Bordj Okhriss" :{
        "Coordinates" : (36.08334570799294, 3.977260972789044),
        "Neighbors": [{"Sour El Ghozlane": 30.1 },{"El Hachimia": 26.7 },{"Bechloul": 39.1 },{"Mansoura": 53.2 },{"Sidi Aissa": 41.4 }],
        "Willaya" : "Bouira"

    },




    "M'Chedallah" :{
        "Coordinates" : (36.3647137838156, 4.2700449074208455),
        "Neighbors": [{"Bechloul": 22.2 },{"Ouacifs": 42.6 },{"Beni Yenni": 15.2 },{"Ain El Hammam": 28.8 },{"Iferhounene": 39.1 },{"Tazmalt": 14.3 },{"M'Chedallah": 53.0 }],
        "Willaya" : "Bouira"

    },


    "Ouenza" :{
        "Coordinates" : (35.95048590661305, 8.130555912962752),
        "Neighbors": [{"El Aouinet": 29.7 },{"El Meridj": 25.3 },{"Taoura": 30.0},{"Merahna": 41.3}],
        "Willaya" : "Tebessa"

    },



    "El Aouinet" :{
        "Coordinates" : (35.87066587756279, 7.889364412298685),
        "Neighbors": [{"Ouenza": 29.7 },{"Bou Khadra": 27.8 },{"Morsott": 28.4 },{"Meskiana": 36.3 },{"Oum El Adhaim": 45.8},{"Taoura": 50 }],
        "Willaya" : "Tebessa"

    },

     


    "El Meridj" :{
        "Coordinates" : (35.7954985497434, 8.230404013640545),
        "Neighbors": [{"Ouenza": 25.3 },{"Bou Khadra": 20.1 },{"Morsott": 30.3 },{"Ain Zerga": 17.1}],
        "Willaya" : "Tebessa"

    },



    "Bou Khadra" :{
        "Coordinates" : (35.74234257910496, 8.030482890485919),
        "Neighbors": [{"Morsott": 10.6 },{"El Aouinet": 28.4 },{"El Meridj": 20.1}],
        "Willaya" : "Tebessa"

    },



    "Morsott" :{
        "Coordinates" : (35.664442945748114, 8.011905257587427),
        "Neighbors": [{"El Aouinet": 28.9 },{"Bou Khadra": 10.7 },{"El Meridj": 30.4 },{"Ain Zerga": 38.4 },{"Boulhaf Dir": 23.4 },{"Bir Dheb": 20.4 },{"Meskiana": 34.1 }],
        "Willaya" : "Tebessa"

    },



    "Ain Zerga" :{
        "Coordinates" : (35.65001165684308, 8.259039890635181),
        "Neighbors": [{"El Meridj": 17.1 },{"Morsott": 38.4 },{"Boulhaf Dir": 33.0 },{"El Kouif": 30.9 }],
        "Willaya" : "Tebessa"

    },


    "Boulhaf Dir" :{
        "Coordinates" : (35.4898949210567, 8.074148225411761),
        "Neighbors": [{"Ain Zerga": 32.9 },{"Morsott": 23.3 },{"Bir Dheb": 19.6 },{"Hammamet": 15.0 },{"Tebessa": 11.8 },{"El Kouif": 35.6 }],
        "Willaya" : "Tebessa"

    },



    "Hammamet" :{
        "Coordinates" : (35.4497637622175, 7.946420468339662),
        "Neighbors": [{"Bir Dheb": 8.8 },{"Guorriguer": 40.4 },{"Bir Mokkadem": 19.0 },{"Tebessa": 19.0 },{"Boulhaf Dir": 15.0 }],
        "Willaya" : "Tebessa"

    },


     "Bir Dheb" :{
        "Coordinates" : (35.52367404404145, 7.936695004603208),
        "Neighbors": [{"Guorriguer": 49.1 },{"Morsott": 20.4 },{"Boulhaf Dir": 19.6 },{"Hammamet": 8.8 },{"Meskiana": 38.9 }],
        "Willaya" : "Tebessa"

    },


     "Bir Mokkadem" :{
        "Coordinates" : (35.37472821303949, 7.80702215218886),
        "Neighbors": [{"Guorriguer": 21.4 },{"Ogla Melha": 61.8 },{"Cheria": 14.2},{"Tebessa": 39.7 },{"Hammamet": 19.0 }],
        "Willaya" : "Tebessa"

    },



    "Cheria" :{
        "Coordinates" : (35.27389655351125, 7.753436986606377),
        "Neighbors": [{"El Mezeraa": 20.0 },{"Bir Mokkadem": 14.2 },{"Guorriguer": 23.9 },{"Tlidjene": 17.8 },{"Ogla Melha": 47.6 }],
        "Willaya" : "Tebessa"

    },


    "Tebessa" :{
        "Coordinates" : (35.40062865621105, 8.118885358599451),
        "Neighbors": [{"El Ma Labiodh": 28.6 },{"Bekkaria": 13.2 },{"El Kouif": 29.5 },{"Boulhaf Dir": 11.8 },{"Ogla Melha": 56.6 },{"Bir Mokkadem": 39.5 },{"Hammamet": 19.0 }],
        "Willaya" : "Tebessa"

    },



    "El Kouif" :{
        "Coordinates" : (35.50045242627126, 8.321823374601921),
        "Neighbors": [{"Ain Zerga": 30.9 },{"Boulhaf Dir": 36.0 },{"Tebessa": 29.1 },{"Bekkaria": 17.5 }],
        "Willaya" : "Tebessa"

    },




    "Bekkaria" :{
        "Coordinates" : (35.375256876682066, 8.242074565927872),
        "Neighbors": [{"El Kouif": 17.5 },{"Tebessa": 12.8 },{"El Ma Labiodh": 29.3 },{"El Houidjbet": 10.9 }],
        "Willaya" : "Tebessa"

    },



    "Guorriguer" :{
        "Coordinates" : (35.42811587281691, 7.591484336636114),
        "Neighbors": [{"Bir Dheb": 49.1 },{"Hammamet": 40.4 },{"Bir Mokkadem": 21.4 },{"Cheria": 24.0 },{"El Mezeraa": 20.0 },{"Bedjene": 14.5 },{"Ain Touila": 20.3},{"Meskiana": 29.8 },{"Dhalaa": 6.5 }],
        "Willaya" : "Tebessa"

    },


    "Bedjene" :{
        "Coordinates" : (35.352839219697294, 7.471329179401719),
        "Neighbors": [{"El Ogla": 20.6 },{"El Mezeraa": 20.0},{"Guorriguer": 14.5 },{"Ouled Rechache": 17.0 },{"El Mahmal":30.0 },{"Ain Touila": 17.5 }],
        "Willaya" : "Tebessa"

    },



    "El Ogla" :{
        "Coordinates" : (35.185255169436076, 7.462415476089008),
        "Neighbors": [{"Bedjene": 20.6 },{"El Mezeraa": 20.0 },{"Stah Guentis": 27.9 },{"Ouled Rechache": 30.6 }],
        "Willaya" : "Tebessa"

    },



    "El Mezeraa" :{
        "Coordinates" : (35.26785589986735, 7.575042446427516),
        "Neighbors": [{"El Ogla": 20.0 },{"Bedjene": 20.0},{"Guorriguer": 20.0 },{"Cheria": 20.0 },{"Stah Guentis": 20.0 },{"Tlidjene": 20.0 }],
        "Willaya" : "Tebessa"

    },



    "Ogla Melha" :{
        "Coordinates" : (34.99025453635625, 7.943252051202326),
        "Neighbors": [{"Cheria": 47.5 },{"Bir Mokkadem": 62.3 },{"Tebessa": 56.6 },{"El Ma Labiodh": 48.5 },{"Safsaf El Ouesra": 57.4 },{"Bir El-Ater": 29.8 },{"Tlidjene":29.8}],
        "Willaya" : "Tebessa"

    },




    "El Ma Labiodh" :{
        "Coordinates" : (35.203738106527354, 8.16160531769289),
        "Neighbors": [{"Tebessa": 28.6 },{"Ogla Melha": 48.5 },{"Bekkaria": 29.3 },{"El Houidjbet": 20.1 },{"Oum Ali": 26.1 },{"Safsaf El Ouesra": 31.3 }],
        "Willaya" : "Tebessa"

    },



    "El Houidjbet" :{
        "Coordinates" : (35.29062666119749, 8.281624790149586),
        "Neighbors": [{"Oum Ali": 40.4 },{"El Ma Labiodh": 20.1 },{"Bekkaria": 10.9 }],
        "Willaya" : "Tebessa"

    },




    "Stah Guentis" :{
        "Coordinates" : (34.995041552325475, 7.303142757314905),
        "Neighbors": [{"El Ogla": 27.9 },{"El Mezeraa":20.0  },{"Tlidjene": 78.4 },{"Ferkane": 75.9 },{"Negrine": 90.7 },{"Babar": 59.0 },{"El Mahmal": 55.7 },{"Ouled Rechache": 40.6 }],
        "Willaya" : "Tebessa"

    },



    "Negrine" :{
        "Coordinates" : (34.489370126673116, 7.520024493028704),
        "Neighbors": [{"Ferkane": 14.8 },{"Stah Guentis": 90.7 },{"Tlidjene": 120 },{"Bir El-Ater": 60.8 },{"Beni Guecha": 70.2 }],
        "Willaya" : "Tebessa"

    },




    "Bir El-Ater" :{
        "Coordinates" : (34.74814450731699, 8.057806620807273),
        "Neighbors": [{"Negrine": 60.8 },{"Tlidjene": 59.3 },{"El Ogla": 29.8 },{"Safsaf El Ouesra": 29.5 }],
        "Willaya" : "Tebessa"

    },



    "Safsaf El Ouesra" :{
        "Coordinates" : (34.96775008231896, 8.20417733820363),
        "Neighbors": [{"Bir El-Ater": 29.5 },{"Ogla Melha": 56.6 },{"El Ma Labiodh":31.3 },{"Oum Ali": 16.2 }],
        "Willaya" : "Tebessa"

    },



    "Oum Ali" :{
        "Coordinates" : (35.01837640554283, 8.298934416114628),
        "Neighbors": [{"El Houidjbet": 56.7 },{"El Ma Labiodh": 26.1 },{"Safsaf El Ouesra": 16.2 }],
        "Willaya" : "Tebessa"

    },


    "Tlidjene" :{
        "Coordinates" : (35.11728845071092, 7.766097514238285),
        "Neighbors": [{"Stah Guentis": 78.5 },{"Negrine": 120 },{"Bir El-Ater": 59.3 },{"El Mezeraa": 20.0 },{"Cheria": 17.7 },{"Ogla Melha": 29.8 }],
        "Willaya" : "Tebessa"

    },



     "Ferkane" :{
        "Coordinates" : (34.55777924582635, 7.413152187852429),
        "Neighbors": [{"Stah Guentis": 75.9 },{"Negrine": 14.8 },{"Beni Guecha": 76.3 },{"Babar": 134 }],
        "Willaya" : "Tebessa"

    },

     "Hamraia" :{
        "Coordinates" : (34.12062553209183, 6.229619613479309),
        "Neighbors": [{"Reguiba": 87.9 },{"Guemar": 95.5 },{"Sidi Aoun": 102 },{"Megrane": 105 },{"Babar": 228 },{"Sidi Okba": 101 },{"Zeribet El Oued": 130},{"Taibet": 171 },{"El M'Ghair": 76.0}],
        "Willaya" : "El Oued"

    },



     "Reguiba" :{
        "Coordinates" : (33.57025887208644, 6.7070797699228715),
        "Neighbors": [{"Guemar": 13.5 },{"Taghzout": 16.5 },{"Taibet": 88.8 }],
        "Willaya" : "El Oued"

    },



     "Guemar" :{
        "Coordinates" : (33.48851680401159, 6.795514856299922),
        "Neighbors": [{"Hamraia": 96.3 },{"Reguiba": 14.5 },{"Taghzout": 2.2},{"Sidi Aoun": 16.1 }],
        "Willaya" : "El Oued"

    },



     "Sidi Aoun" :{
        "Coordinates" : (33.54580107198752, 6.903221177945972),
        "Neighbors": [{"Hamraia": 102 },{"Guemar": 16.1 },{"Hassani Abdelkrim": 7.7 },{"Debila": 7.5 },{"Megrane": 3.8 }],
        "Willaya" : "El Oued"

    },

    "Megrane": {
        "Coordinates": (33.56762142136831, 6.917576683729581),
        "Neighbors": [
            {"Sidi Aoun": 3.8},
            {"Debila": 6.7},
            {"Hamraia": 105},
            {"Beni Guecha": 120},
            {"Hassi Khalifa": 7.5},  # Ajout d'une virgule ici
            {"Babar": 281}
        ],
        "Willaya": "El Oued"
    },

    "Beni Guecha": {
        "Coordinates": (34.204900253307, 7.613281079976172),
        "Neighbors": [
            {"Megrane": 120},
            {"Hassi Khalifa": 114},
            {"Taleb Larbi": 59.0},
            {"Negrine": 70.2},
            {"Ferkane": 76.3},  # Ajout d'une virgule ici
            {"Babar": 211}
        ],
        "Willaya": "El Oued"
    },

     "Hassani Abdelkrim" :{
        "Coordinates" : (33.48025648483958, 6.895174153914946),
        "Neighbors": [{"Taghzout": 18.8 },{"Kouinine": 16.8 },{"Guemar": 13.4 },{"Sidi Aoun": 10.0 },{"El Oued": 15.4 },{"Trifaoui": 8.9 },{"Debila": 5.7 }],
        "Willaya" : "El Oued"

    },



     "Taghzout" :{
        "Coordinates" : (33.47271813997294, 6.803002461311188),
        "Neighbors": [{"Reguiba": 16.1 },{"Guemar": 1.9 },{"Hassani Abdelkrim": 12.9 },{"Ourmas": 11.2 },{"Kouinine": 8.9 },{"Taibet": 73.1 }],
        "Willaya" : "El Oued"

    },



     "Debila" :{
        "Coordinates" : (33.50165897739656, 6.938151570041515),
        "Neighbors": [{"Hassani Abdelkrim": 5.4 },{"Sidi Aoun": 7.6 },{"Trifaoui": 10.3 },{"Megrane": 6.5 },{"Hassi Khalifa": 8.2 }],
        "Willaya" : "El Oued"

    },



     "Hassi Khalifa" :{
        "Coordinates" : (33.561387859062386, 6.988538073369828),
        "Neighbors": [{"Megrane": 7.3 },{"Taleb Larbi": 55.2 },{"Trifaoui": 20.4 },{"Debila": 8.2 },{"Beni Guecha": 114 }],
        "Willaya" : "El Oued"

    },



     "Taleb Larbi" :{
        "Coordinates" : (33.72967463805489, 7.5000042411927375),
        "Neighbors": [{"Hassi Khalifa": 55.3 },{"Beni Guecha": 59.0 },{"Trifaoui": 74.7 },{"Douar El Ma": 45.6 }],
        "Willaya" : "El Oued"

    },



     "Ourmas" :{
        "Coordinates" : (33.407211131038544, 6.779495218813646),
        "Neighbors": [{"Kouinine":5.4 },{"Taghzout": 10.8 },{"Mih Ouansa": 27.8 },{"Taibet": 63.9 }],
        "Willaya" : "El Oued"

    },


     "Kouinine" :{
        "Coordinates" : (33.401317131919, 6.823134755531971),
        "Neighbors": [{"Ourmas": 5.4 },{"Taghzout": 8.5 },{"Hassani Abdelkrim": 15.0 },{"El Oued": 5.1 },{"Oued El Alenda": 23.8 }],
        "Willaya" : "El Oued"

    },



     "Mih Ouansa" :{
        "Coordinates" : (33.208178887098725, 6.708662453485327),
        "Neighbors": [{"Ourmas": 27.6 },{"Oued El Alenda": 8.5 }],
        "Willaya" : "El Oued"

    },



     "Oued El Alenda" :{
        "Coordinates" : (33.229189219116876, 6.765952085946214),
        "Neighbors": [{"Mih Ouansa": 8.5 },{"Robbah": 30.0},{"Bayadha": 24.3 },{"El Oued": 20.2 },{"Kouinine": 23.6 },{"Taibet": 44.8 }],
        "Willaya" : "El Oued"

    },



     "El Oued" :{
        "Coordinates" : (33.42479736363828, 6.844511500104768),
        "Neighbors": [{"Oued El Alenda": 20.1 },{"Bayadha": 8.7 },{"Trifaoui":12.4 },{"Hassani Abdelkrim": 14.1 },{"Kouinine": 4.7 }],
        "Willaya" : "El Oued"

    },



     "Trifaoui" :{
        "Coordinates" : (33.430724662049904, 6.938895448653995),
        "Neighbors": [{"Hassani Abdelkrim": 9.6 },{"El Oued": 12.3 },{"Bayadha": 12.9 },{"Douar El Ma": 88.2 },{"Taleb Larbi": 74.6 },{"Hassi Khalifa": 18.6 },{"Debila": 10.4 }],
        "Willaya" : "El Oued"

    },




     "Bayadha" :{
        "Coordinates" : (33.33290681767051, 6.890927152269225),
        "Neighbors": [{"Douar El Ma": 81.5 },{"Nakhla": 9.3},{"Robbah": 9.3 },{"El Oued": 8.6 },{"Trifaoui": 13.5 },{"Oued El Alenda": 26.5 }],
        "Willaya" : "El Oued"

    },


     "Nakhla" :{
        "Coordinates" : (33.277317494487576, 6.949666466028754),
        "Neighbors": [{"Bayadha": 9.3},{"Douar El Ma": 74.0 },{"Robbah": 5.2 },{"El Ogla": 282}],
        "Willaya" : "El Oued"

    },


     "El Ogla" :{
        "Coordinates" : (33.243368939046306, 6.946211212278195),
        "Neighbors": [{"Robbah": 284 },{"Douar El Ma": 273 },{"Nakhla": 282 },{"Taibet": 79.1 }],
        "Willaya" : "El Oued"

    },


     "Robbah" :{
        "Coordinates" : (33.292144905523756, 6.901142687410905),
        "Neighbors": [{"Douar El Ma": 77.3 },{"Oued El Alenda": 26.8 },{"El Ogla": 284 },{"Nakhla": 5.1 },{"Bayadha": 9.3 },{"Taibet": 73.1 }],
        "Willaya" : "El Oued"

    },


     "Douar El Ma" :{
        "Coordinates" : (33.43351506496582, 7.69818030943111),
        "Neighbors": [{"Robbah": 77.3 },{"El Ogla": 273 },{"Nakhla": 74.1 },{"Trifaoui": 88.1 },{"Taleb Larbi": 45.6 },{"Bayadha": 81.7 },{"El Borma": 702 },{"Taibet": 153 }],
        "Willaya" : "El Oued"

    },


    "El M'Ghair" :{
        "Coordinates" : (33.43351506496582, 7.69818030943111),
        "Neighbors": [{"Djamaa": 47.3 },{"Hamraia": 75.7},{"El Outaya": 90},{"Ouled Djellal": 45},{"Ourlal": 75}],
        "Willaya" : "El M'Ghair"

    },


     "Djamaa" :{
        "Coordinates" : (33.43351506496582, 7.69818030943111),
        "Neighbors": [{"El M'Ghair": 47.3 },{"Taibet": 88.3},{"El Hadjira": 149},{"Megarine": 44.2},{"El Outaya": 194}],
        "Willaya" : "El M'Ghair"

    },

     "Babar" :{
        "Coordinates" : (35.12251204286038, 7.1125077049583485),
        "Neighbors": [{"Djellal": 43.9},{"Chechar": 20.3 },{"Khirane": 43.4},{"Ensigha": 25.1 },{"El Mahmal": 30.1 },{"Ouled Rechache": 35.6 }, {"Tamza": 46.1 },{"Ferkane": 134},{"Stah Guentis": 59.0 },{"Hamraia": 228 },{"Megrane": 281 },{"Beni Guecha": 211 },{"Zeribet El Oued": 98.3}],
        "Willaya" : "Khenchela"

    },




     "Djellal" :{
        "Coordinates" : (34.93053521398077, 6.89920992604655),
        "Neighbors": [{"Babar": 43.9 },{"Chechar": 23.7},{"Khirane": 51.5 },{"Zeribet El Oued": 55.9}],
        "Willaya" : "Khenchela"

    },



     "Chechar" :{
        "Coordinates" : (35.05204781807638, 6.89351257892932),
        "Neighbors": [{"Djellal": 23.7 },{"Babar": 20.3 },{"Khirane": 31.4 }],
        "Willaya" : "Khenchela"

    },





     "Khirane" :{
        "Coordinates" : (35.00644192570462, 6.765411989866541),
        "Neighbors": [{"Djellal": 50.6 },{"El Ouldja": 20.0 },{"Chechar": 31.4 },{"Babar": 43.4 },{"Bouhmama": 61.2 },{"Tamza": 70.0 },{"M'Sara": 75.2 }],
        "Willaya" : "Khenchela"

    },





     "Ouled Rechache" :{
        "Coordinates" : (35.29536516236954, 7.336626255865803),
        "Neighbors": [{"El Mahmal": 15.2 },{"Stah Guentis": 40.6 },{"El Ogla": 30.6 },{"Bedjene": 17.0 }],
        "Willaya" : "Khenchela"

    },




     "El Mahmal" :{
        "Coordinates" : (35.360292049672225, 7.403645393612432),
        "Neighbors": [{"Ouled Rechache": 15.2 },{"Babar": 29.9 },{"Ain Touila": 24.1 },{"Ensigha": 8.8 },{"Stah Guentis": 55.7 },{"Bedjene":30.0 }],
        "Willaya" : "Khenchela"

    },





     "El Ouldja" :{
        "Coordinates" : (34.92209679424398, 6.6710672912780735),
        "Neighbors": [{"M'Sara": 20.0 },{"Khirane": 20.0},{"T'kout": 184 }],
        "Willaya" : "Khenchela"

    },





     "M'Sara" :{
        "Coordinates" : (35.24430976708128, 6.568332217237607),
        "Neighbors": [{"Bouhmama": 18.8 },{"Khirane": 75.2 },{"El Ouldja": 20.0 },{"T'kout": 53.6 },{"Ichmoul": 32.7 }],
        "Willaya" : "Khenchela"

    },


     "Bouhmama" :{
        "Coordinates" : (35.319214412663655, 6.741225058436859),
        "Neighbors": [{"M'Sara": 18.8 },{"Yabous": 26.1 },{"Chelia":7.1 },{"Tamza": 15.5 },{"Khirane": 61.2 },{"Ichmoul": 30.5 }],
        "Willaya" : "Khenchela"

    },





     "Tamza" :{
        "Coordinates" : (35.31464235881329, 6.832120563970217),
        "Neighbors": [{"Chelia": 22.0 },{"Kais": 32.9 },{"El Hamma": 33.5 },{"Bouhmama": 15.5 },{"Khirane": 70.0 },{"Ensigha": 50.4 },{"Babar": 46.6 }],
        "Willaya" : "Khenchela"

    },





     "Yabous" :{
        "Coordinates" : (35.409913805107415, 6.643061524743732),
        "Neighbors": [{"Taouizient": 27.1 },{"Bouhmama": 26.1},{"Ichmoul": 21.7 },{"Timgad": 27.9 }],
        "Willaya" : "Khenchela"

    },





     "Taouizient" :{
        "Coordinates" : (35.50799092175352, 6.811028453087089),
        "Neighbors": [{"Yabous": 27.1 },{"Chelia": 26.9 },{"Remila": 14.2 },{"Timgad": 34.7 }],
        "Willaya" : "Khenchela"

    },




     "Ensigha" :{
        "Coordinates" : (35.382306973112634, 7.146580740688127),
        "Neighbors": [{"Khenchela": 5.3 },{"El Hamma": 12.7 },{"Tamza": 50.4 },{"Babar": 4.3 },{"El Mahmal": 10.2 },{"Ain Touila": 27.4 },{"Beghai": 18.9 }],
        "Willaya" : "Khenchela"

    },




     "Ain Touila" :{
        "Coordinates" : (35.44502472529606, 7.46566962178706),
        "Neighbors": [{"M'Toussa": 30.0 },{"Beghai": 33.1 },{"Ensigha": 27.5 },{"El Mahmal": 24.8 },{"Bedjene": 17.5 },{"Guorriguer": 20.3},{"Fkirina": 44.8},{"Dhalaa": 17.4}],
        "Willaya" : "Khenchela"

    },




     "Khenchela" :{
        "Coordinates" : (35.427468295281194, 7.144908832648417),
        "Neighbors": [{"El Hamma": 8.3 },{"Beghai": 14.1 },{"Ensigha": 5.3 }],
        "Willaya" : "Khenchela"

    },




     "Chelia" :{
        "Coordinates" : (35.36604461969416, 6.778369142804429),
        "Neighbors": [{"Taouizient": 26.9 },{"Bouhmama": 7.1 },{"Tamza": 22.0 },{"Kais": 27.4 },{"Remila": 36.4 }],
        "Willaya" : "Khenchela"

    },




     "Remila" :{
        "Coordinates" : (35.57094036908271, 6.896829001682706),
        "Neighbors": [{"Taouizient": 14.2 },{"Chelia": 36.4 },{"Kais": 9.0 },{"Timgad": 48.8 },{"Chemora": 32.4 },{"Oum El Bouaghi": 62.5},{"Ain Fakroun": 75.1}],
        "Willaya" : "Khenchela"

    },



     "Kais" :{
        "Coordinates" : (35.49553833349222, 6.924098225903094),
        "Neighbors": [{"Remila": 9.0 },{"Chelia": 27.4 },{"Tamza": 32.9 },{"El Hamma": 15.6 },{"Oum El Bouaghi": 52.3}],
        "Willaya" : "Khenchela"

    },



     "El Hamma" :{
        "Coordinates" : (35.4635426613627, 7.081556008706317),
        "Neighbors": [{"Kais": 15.6 },{"Khenchela": 7.8 },{"Tamza": 33.5 },{"Ensigha": 12.7 },{"Beghai": 11.9},{"Oum El Bouaghi": 52.8}],
        "Willaya" : "Khenchela"

    },



     "Beghai" :{
        "Coordinates" : (35.521793917196675, 7.113516712386049),
        "Neighbors": [{"M'Toussa": 17.2 },{"Ain Touila": 33.1 },{"Khenchela": 14.3 },{"Ensigha": 19.0},{"El Hamma": 11.9},{"Oum El Bouaghi": 48.3}],
        "Willaya" : "Khenchela"

    },



     "M'Toussa" :{
        "Coordinates" : (35.60038319978592, 7.250086108724515),
        "Neighbors": [{"Beghai": 17.2 },{"Ain Touila": 30.0 },{"Oum El Bouaghi": 46.2},{"Fkirina": 9.2}],
        "Willaya" : "Khenchela"

    },


     "Bab El Oued" :{
        "Coordinates" : (36.79428231730759, 3.052274257205219),
        "Neighbors": [{"Bouzareah": 6.9 },{"Sidi M'Hamed": 5.6 },{"Cheraga": 11.3 }],
        "Willaya" : "Algiers"

    },



     "Bouzareah" :{
        "Coordinates" : (36.78740029440832, 3.017611977507601),
        "Neighbors": [{"Bab El Oued": 6.9 },{"Cheraga": 8.9 },{"Bir Mourad Rais": 14.9 },{"Sidi M'Hamed": 10.2 }],
        "Willaya" : "Algiers"

    },



     "Cheraga" :{
        "Coordinates" : (36.76660040259015, 2.9589428076991524),
        "Neighbors": [{"Bab El Oued": 10.6 },{"Zeralda": 15.3 },{"Bouzareah": 10.1 },{"Draria": 9.4 }],
        "Willaya" : "Algiers"

    },



     "Zeralda" :{
        "Coordinates" : (36.713419486871004, 2.844489837089228),
        "Neighbors": [{"Cheraga": 16.4 },{"Draria": 18.8 },{"Ben Khellil": 13.8 },{"Fouka": 14.4 },{"Kolea": 13.3 },{"Beni Mered":34.2}],
        "Willaya" : "Algiers"

    },



     "Draria" :{
        "Coordinates" : (36.72001915977464, 2.995026026303088),
        "Neighbors": [{"Zeralda": 18.8 },{"Cheraga": 9.7 },{"Bir Mourad Rais": 11.8 },{"Birtouta": 13.8}],
        "Willaya" : "Algiers"

    },



     "Birtouta" :{
        "Coordinates" : (36.64234876775695, 2.9947709605466364),
        "Neighbors": [{"Baraki": 15.7 },{"Bir Mourad Rais": 15.6 },{"Draria": 18.7 },{"Ben Khellil": 22.1 },{"Boufarik":10.8},{"Chebli": 8.6 }],
        "Willaya" : "Algiers"

    },



     "Bir Mourad Rais" :{
        "Coordinates" : (36.734879744292655, 3.0488957921158613),
        "Neighbors": [{"Birtouta": 15.1 },{"Draria": 10.8 },{"Baraki": 13.4 },{"Bouzareah": 14.2 },{"Sidi M'Hamed": 4.8 },{"Hussein Dey": 6.4 },{"El Harrach": 9.8}],
        "Willaya" : "Algiers"

    },



     "Sidi M'Hamed" :{
        "Coordinates" : (36.76186578755923, 3.0562994328665978),
        "Neighbors": [{"Bab El Oued": 5.9  },{"Bouzareah": 8.7 },{"Bir Mourad Rais": 4.5 },{"Hussein Dey": 4.7 }],
        "Willaya" : "Algiers"

    },



     "Hussein Dey" :{
        "Coordinates" : (36.74069090651906, 3.0962085513861815),
        "Neighbors": [{"Sidi M'Hamed": 4.7 },{"Bir Mourad Rais": 5.9 },{"El Harrach": 7.7 },{"Dar El Beida": 14.8 }],
        "Willaya" : "Algiers"

    },



     "El Harrach" :{
        "Coordinates" : (36.720528981851636, 3.1359966368206478),
        "Neighbors": [{"Baraki": 8.5 },{"Bir Mourad Rais": 9.5 },{"Hussein Dey": 7.4 },{"Dar El Beida": 11.7 }],
        "Willaya" : "Algiers"

    },




     "Baraki" :{
        "Coordinates" : (36.66804964267034, 3.1024701536391652),
        "Neighbors": [{"Birtouta": 12.3 },{"Bir Mourad Rais": 12.0},{"El Harrach": 9.7 },{"Dar El Beida": 13.9 },{"Chebli": 17.9 },{"Ouled Selama": 16.4 },{"Larbaa": 12.7 }],
        "Willaya" : "Algiers"

    },



     "Dar El Beida" :{
        "Coordinates" : (36.721683427444894, 3.2062788354805973),
        "Neighbors": [{"Rouiba": 9.6 },{"El Harrach": 8.0 },{"Baraki": 13.9 },{"Hussein Dey": 14.5 },{"Meftah": 24.9},{"Khemis El Khechna": 18.4 }],
        "Willaya" : "Algiers"

    },




     "Rouiba" :{
        "Coordinates" : (36.740944322024895, 3.2790632576441183),
        "Neighbors": [{"Dar El Beida": 11.3 },{"Khemis El Khechna": 17.5  },{"Boudouaou": 13.5 }],
        "Willaya" : "Algiers"

    },



     "Tigzirt" :{
        "Coordinates" : (36.90448042750494, 4.118777959580642),
        "Neighbors": [{"Azeffoun": 35.5 },{"Ouaguenoun": 20.3 },{"Makouda": 19.3 },{"Dellys": 26.8 }],
        "Willaya" : "Tizi Ouzou"

    },




     "Makouda" :{
        "Coordinates" : (36.79116193280426, 4.063218421008604),
        "Neighbors": [{"Tigzirt": 19.3 },{"Ouaguenoun": 20.7 },{"Draa Ben Khedda": 18.6 },{"Dellys": 29.9 }],
        "Willaya" : "Tizi Ouzou"

    },



     "Azeffoun" :{
        "Coordinates" : (36.89353249438549, 4.423320656242425),
        "Neighbors": [{"Tigzirt": 35.6 },{"Ouaguenoun": 41.1 },{"Azazga": 35.3 },{"Adekar": 65.7 }],
        "Willaya" : "Tizi Ouzou"

    },




     "Ouaguenoun" :{
        "Coordinates" : (36.775564307214175, 4.170985354627599),
        "Neighbors": [{"Azeffoun": 41.1 },{"Azazga": 32.1 },{"Tizi Ouzou":24.7  },{"Draa Ben Khedda": 37.3 },{"Makouda": 20.5 },{"Tigzirt": 20.3 }],
        "Willaya" : "Tizi Ouzou"

    },




     "Azazga" :{
        "Coordinates" : (36.744584377986186, 4.372713838833571),
        "Neighbors": [{"Azeffoun": 35.3 },{"Ouaguenoun": 32.0 },{"Tizi Ouzou": 35.4 },{"Tizi Rached": 22.8 },{"Mekla": 22.5 },{"Ain El Hammam": 34.4 },{"Bouzeguene": 27.6 },{"Adekar": 42.1 }],
        "Willaya" : "Tizi Ouzou"

    },



     "Draa Ben Khedda" :{
        "Coordinates" : (36.72936255765004, 3.9664778858141982),
        "Neighbors": [{"Makouda": 18.0 },{"Ouaguenoun": 36.2 },{"Tizi Ouzou": 10.3 },{"Maatkas": 19.1 },{"Dra Lmizan": 33.2 },{"Baghlia": 19.3 },{"Naciria": 15.6 }],
        "Willaya" : "Tizi Ouzou"

    },



     "Tizi Ouzou" :{
        "Coordinates" : (36.71257216670369, 4.048134717304529),
        "Neighbors": [{"Draa Ben Khedda": 10.3 },{"Ouaguenoun": 16.7 },{"Azazga": 35.3 },{"Tizi Rached": 17.8 },{"Larbaa Nath Irathen": 25.8 },{"Beni Douala": 16.9 },{"Maatkas": 25.4 }],
        "Willaya" : "Tizi Ouzou"

    },




     "Mekla" :{
        "Coordinates" : (36.68831799742856, 4.267897475633366),
        "Neighbors": [{"Azazga": 19.3 },{"Ain El Hammam": 24.0 },{"Tizi Rached": 10.8 },{"Larbaa Nath Irathen": 21.7 }],
        "Willaya" : "Tizi Ouzou"

    },



     "Tizi Rached" :{
        "Coordinates" : (36.679399099719475, 4.20650626035216),
        "Neighbors": [{"Tizi Ouzou": 18.0 },{"Azazga": 23.1 },{"Larbaa Nath Irathen": 10.0 },{"Mekla": 11.2 }],
        "Willaya" : "Tizi Ouzou"

    },





     "Larbaa Nath Irathen" :{
        "Coordinates" : (36.64296383718827, 4.199834509288965),
        "Neighbors": [{"Tizi Rached": 10.0},{"Mekla": 21.7 },{"Ain El Hammam": 19.7 },{"Beni Yenni": 27.6 },{"Beni Douala": 35.3 },{"Tizi Ouzou": 26.1 }],
        "Willaya" : "Tizi Ouzou"

    },




     "Beni Douala" :{
        "Coordinates" : (36.6215769679533, 4.082121405569226),
        "Neighbors": [{"Maatkas": 19.2 },{"Ouadhia": 18.8 },{"Tizi Ouzou": 16.9 },{"Larbaa Nath Irathen": 34.5},{"Beni Yenni": 29.2}],
        "Willaya" : "Tizi Ouzou"

    },


     "Maatkas" :{
        "Coordinates" : (36.605613981828874, 3.9833482625725725),
        "Neighbors": [{"Dra Lmizan": 29.8},{"Boghni": 17.2 },{"Ouadhia": 22.2 },{"Beni Douala": 19.2 },{"Tizi Ouzou": 24.9 },{"Draa Ben Khedda": 19.1 }],
        "Willaya" : "Tizi Ouzou"

    },





     "Dra Lmizan" :{
        "Coordinates" : (36.536463541018485, 3.836818332601534),
        "Neighbors": [{"Tizi Ghenif": 10.1 },{"Draa Ben Khedda": 33.3 },{"Maatkas": 29.8 },{"Boghni": 13.6 },{"Kadiria": 22.4},{"Naciria": 46.3 },{"Isser": 37.2 }],
        "Willaya" : "Tizi Ouzou"

    },




     "Tizi Ghenif" :{
        "Coordinates" : (36.588585521481704, 3.7712142549121213),
        "Neighbors": [{"Dra Lmizan": 10.1 },{"Kadiria": 16.6},{"Isser": 27.1 }],
        "Willaya" : "Tizi Ouzou"

    },



     "Boghni" :{
        "Coordinates" : (36.54581155340859, 3.95316967356731),
        "Neighbors": [{"Dra Lmizan": 13.6 },{"Maatkas": 17.5 },{"Ouadhia": 13.5 },{"Bouira": 32.8 }],
        "Willaya" : "Tizi Ouzou"

    },



     "Ouadhia" :{
        "Coordinates" : (36.55951992431097, 4.078829117710288),
        "Neighbors": [{"Boghni": 13.5 },{"Maatkas": 17.6 },{"Beni Douala": 18.8 },{"Beni Yenni": 21.9 },{"Ouacifs": 21.6 },{"Bechloul": 64.6 },{"Haizer": 53.1 }],
        "Willaya" : "Tizi Ouzou"

    },




     "Ouacifs" :{
        "Coordinates" : (36.518387517680715, 4.207591264177785),
        "Neighbors": [{"Beni Yenni": 15.2 },{"Ouadhia": 21.6},{"M'Chedallah": 42.6 },{"Bechloul": 56.3 },{"Haizer": 53.5 }],
        "Willaya" : "Tizi Ouzou"

    },



     "Beni Yenni" :{
        "Coordinates" : (36.57447665820277, 4.205422108273701),
        "Neighbors": [{"Ouacifs": 15.2 },{"Ouadhia": 21.9 },{"Beni Douala": 30.1 },{"Larbaa Nath Irthan": 27.6 },{"Ain El Hammam": 21.7},{"M'Chedallah": 15.2 }],
        "Willaya" : "Tizi Ouzou"

    },




     "Ain El Hammam" :{
        "Coordinates" : (36.57101617924628, 4.309498508487117),
        "Neighbors": [{"Iferhounene": 8.6},{"Bouzeguene": 29.3 },{"Azazga": 34.4 },{"Mekla": 24.1 },{"Larbaa Nath Irathen": 20.1 },{"Beni Yenni": 21.7 },{"M'Chedallah": 28.8 }],
        "Willaya" : "Tizi Ouzou"

    },




     "Iferhounene" :{
        "Coordinates" : (36.53272402162574, 4.366604763879674),
        "Neighbors": [{"Bouzeguene": 27.6},{"Ain El Hammam": 8.6 },{"M'Chedallah": 39.1 },{"Akbou": 44.3 },{"Tazmalt": 37.3 }],
        "Willaya" : "Tizi Ouzou"

    },



     "Bouzeguene" :{
        "Coordinates" : (36.61993237461428, 4.47985339872458),
        "Neighbors": [{"Azazga": 27.6},{"Ain El Hammam": 29.3 },{"Iferhounene": 27.6 },{"Adekar": 54.0 },{"Chemini": 22.8 },{"Ouzellaguen": 25.1 },{"Akbou": 37.1 }],
        "Willaya" : "Tizi Ouzou"

    },

     "Ain Deheb" :{
        "Coordinates" : (34.84310221428498, 1.5381678071417741),
        "Neighbors": [{"Ain Kermes": 44.3},{"Sougueur": 40.5},{"Gueltet Sidi Saad": 92.2},{"Boualem": 178}],
        "Willaya" : "Tiaret"

    },

     "Ain Kermes" :{
        "Coordinates" : (34.90302836923863, 1.1067655423371365),
        "Neighbors": [{"Frenda": 21.9 },{"Ain Deheb": 44.3},{"Sougueur": 58.3 },{"El Hassasna": 83.6},{"Ouled Brahim": 72.1},{"Rogassa": 126},{"Boualem":203}],
        "Willaya" : "Tiaret"

    },

     "Sougueur" :{
        "Coordinates" : (35.18464150330174, 1.4935124654120682),
        "Neighbors": [{"Ain Deheb": 40.5 },{"Ain Kermes": 57.8 },{"Frenda": 50.9 },{"Medroussa": 38.9 },{"Dahmouni": 36.6 },{"Mahdia": 43.3 },{"Ksar Chellala": 115},{"Gueltet Sidi Saad": 132}],
        "Willaya" : "Tiaret"

    },


     "Ksar Chellala" :{
        "Coordinates" : (35.22268919852356, 2.304784254159348),
        "Neighbors": [{"Hamadia": 59.5},{"Mahdia": 70.6},{"Sougueur": 115},{"Sidi Ladjel": 59.5 },{"Ain Oussara": 65.6}],
        "Willaya" : "Tiaret"

    },


     "Hamadia" :{
        "Coordinates" : (35.456598502099105, 1.8759109364180215),
        "Neighbors": [{"Ksar Chellala": 59.5},{"Mahdia": 11.3},{"Tissemsilt": 18.7 },{"Sidi Ladjel": 61.6}],
        "Willaya" : "Tiaret"

    },



     "Mahdia" :{
        "Coordinates" : (35.428382013938965, 1.7567713189373377),
        "Neighbors": [{"Hamadia": 11.3},{"Ksar Chellala": 70.6 },{"Sougueur": 43.3},{"Dahmouni": 30.2 },{"Meghila": 55.0 },{"Ammari": 23.4},{"Tissemsilt": 27.4 }],
        "Willaya" : "Tiaret"

    },



     "Dahmouni" :{
        "Coordinates" : (35.410304947525525, 1.4746760559864027),
        "Neighbors": [{"Meghila": 33.3 },{"Oued Lilli": 34.4 },{"Tiaret": 16.0 },{"Medroussa": 41.7 },{"Mahdia": 30.6 },{"Sougueur": 36.8 }],
        "Willaya" : "Tiaret"

    },



    "Tiaret" :{
        "Coordinates" : (35.36031053891969, 1.327286383154247),
        "Neighbors": [{"Oued Lilli": 22.5 },{"Rahouia": 38.2 },{"Mechraa Safa": 30.3 },{"Medroussa": 25.7},{"Dahmouni": 16.0 }],
        "Willaya" : "Tiaret"

    },



     "Medroussa" :{
        "Coordinates" : (35.18074413579538, 1.1994100740362768),
        "Neighbors": [{"Mechraa Safa": 42.5 },{"Tiaret": 25.7 },{"Frenda": 22.7 },{"Dahmouni": 41.1 },{"Sougueur": 38.3 }],
        "Willaya" : "Tiaret"

    },



     "Frenda" :{
        "Coordinates" : (35.05981149176186, 1.0595994865165141),
        "Neighbors": [{"Mechraa Safa": 50.0 },{"Ain Kermes": 22.0 },{"Sougueur": 50.1 },{"Medroussa": 22.7 },{"Ouled Brahim": 64.6},{"Hachem": 84.2},{"Aouf": 74.5}],
        "Willaya" : "Tiaret"

    },


     "Mechraa Safa" :{
        "Coordinates" : (35.392152787231424, 1.0585912952786058),
        "Neighbors": [{"Rahouia": 19.6 },{"Tiaret": 30.3 },{"Medroussa": 42.4 },{"Frenda": 50.0 },{"Oued El Abtal": 47.4},{"Mendes": 41.6}],
        "Willaya" : "Tiaret"

    },



     "Rahouia" :{
        "Coordinates" : (35.5291083043609, 1.0238867654161925),
        "Neighbors": [{"Oued Lilli": 28.6 },{"Tiaret": 37.7 },{"Mechraa Safa": 19.6 },{"Mendes": 22.1}],
        "Willaya" : "Tiaret"

    },


     "Oued Lilli" :{
        "Coordinates" : (35.513273882137966, 1.269393294190999),
        "Neighbors": [{"Meghila": 23.3 },{"Dahmouni": 34.8 },{"Tiaret": 22.5 },{"Rahouia": 28.6 },{"Melaab": 35.7 },{"Ain Tarek": 41.2}],
        "Willaya" : "Tiaret"

    },



     "Meghila" :{
        "Coordinates" : (35.36326739886036, 1.326979322130446),
        "Neighbors": [{"Oued Lilli": 23.3 },{"Dahmouni": 42.5 },{"Mahdia": 55.0},{"Melaab": 18.7 },{"Sidi Lantri": 41.0 },{"Maacem": 33.1 },{"Ammari": 31.6 }],
        "Willaya" : "Tiaret"

    },


     "Marsa Ben M'Hidi" :{
        "Coordinates" : (35.09739374457427, -2.19994154297754),
        "Neighbors": [{"Bab El Assa": 27.1 }],
        "Willaya" : "Tlemcen"

    },



     "Bab El Assa" :{
        "Coordinates" : (34.96432478272859, -2.033477521508158),
        "Neighbors": [{"Marsa Ben M'Hidi": 27.1 },{"Ghazaouet": 32.6 },{"Nedroma": 33.7 },{"Maghnia": 37.0}],
        "Willaya" : "Tlemcen"

    },




     "Ghazaouet" :{
        "Coordinates" : (35.09251090674898, -1.8639979900272121),
        "Neighbors": [{"Hanaine": 44.2},{"Bab El Assa": 32.6},{"Nedroma": 16.1}],
        "Willaya" : "Tlemcen"

    },

     "Honaine" :{
        "Coordinates" : (35.17866599793506, -1.6519166974430026),
        "Neighbors": [{"Ghazaouet": 44.2},{"Ramchi": 35.3},{"Oulhaca El Gheraba": 18.6 }],
        "Willaya" : "Tlemcen"

    },

     "Nedroma" :{
        "Coordinates" : (35.014074580924486, -1.749632680811353),
        "Neighbors": [{"Ghazaouet": 16.9 },{"Bab El Assa": 36.9 },{"Remchi": 40.0 },{"Fellaoucene": 20.3 },{"Maghnia": 29.5}],
        "Willaya" : "Tlemcen"

    },

     "Maghnia" :{
        "Coordinates" : (34.848990090478466, -1.731390211477131),
        "Neighbors": [{"Bab El Assa": 36.9 },{"Nedroma": 29.7 },{"Fellaoucene": 32.2 },{"Hennaya": 49.2 },{"Sabra": 23.7 },{"Beni Boussaid": 23.5 }],
        "Willaya" : "Tlemcen"

    },

     "Fellaoucene" :{
        "Coordinates" : (35.036253457678775, -1.6018828564891545),
        "Neighbors": [{"Remchi": 20.2 },{"Nedroma": 19.9 },{"Maghnia": 32.1 },{"Hennaya": 27.3 }],
        "Willaya" : "Tlemcen"

    },

     "Remchi" :{
        "Coordinates" : (35.06675086420339, -1.4289312329898882),
        "Neighbors": [{"Honaine": 35.3 },{"Bensekrane": 30.4 },{"Hennaya": 14.0 },{"Fellaoucene": 20.7 },{"Nedroma": 40.1},{"Chetouane": 27.0},{"Beni Saf": 39.3 },{"Oulhaca El Gheraba": 28.1 },{"Ain Kihal":48.5}],
        "Willaya" : "Tlemcen"

    },

     "Bensekrane" :{
        "Coordinates" : (35.07194220267789, -1.2272234104716873),
        "Neighbors": [{"Remchi": 25.1 },{"Chetouane": 24.3 },{"Ouled Mimoun": 35.3 },{"Ain Tallout": 43.9 },{"Ain Kihal":19.9}],
        "Willaya" : "Tlemcen"

    },

     "Hennaya" :{
        "Coordinates" : (34.95338009377155, -1.3734882699927895),
        "Neighbors": [{"Remchi": 14.0 },{"Fellaoucene": 28.7 },{"Sabra": 37.5 },{"Chetouane": 13.3},{"Tlemcen": 10.3 },{"Mansourah": 10.9 }],
        "Willaya" : "Tlemcen"

    },

     "Sabra" :{
        "Coordinates" : (34.82938997183131, -1.528358138670707),
        "Neighbors": [{"Hennaya": 37.4 },{"Maghnia": 23.7 },{"Beni Boussaid": 37.2 },{"Beni Snous": 34.8},{"Mansourah": 26.1 }],
        "Willaya" : "Tlemcen"

    },



     "Beni Boussaid" :{
        "Coordinates" : (34.64953513747886, -1.7480836533466915),
        "Neighbors": [{"Maghnia": 23.7 },{"Sabra":37.5  },{"Beni Snous": 41.4 },{"Sidi Djilali": 52.8}],
        "Willaya" : "Tlemcen"

    },




     "Chetouane" :{
        "Coordinates" : (34.92556175648105, -1.3003300543304357),
        "Neighbors": [{"Bensekrane": 24.3 },{"Remchi": 25.2},{"Hennaya": 11.4},{"Tlemcen": 8.8 },{"Mansourah": 9.4 },{"Ouled Mimoun": 30.5 }],
        "Willaya" : "Tlemcen"

    },



     "Tlemcen" :{
        "Coordinates" : (34.88049130973882, -1.3137172160376809),
        "Neighbors": [{"Hennaya": 10.2 },{"Chetouane": 6.9 },{"Mansourah": 3.4 }],
        "Willaya" : "Tlemcen"

    },




     "Mansourah" :{
        "Coordinates" : (34.878678931311136, -1.349153831413027),
        "Neighbors": [{"Tlemcen": 3.5 },{"Hennaya": 11.1 },{"Sabra": 26.0 },{"Beni Snous": 40.3 },{"Sebdou": 36.9 },{"Ouled Mimoun": 37.8 },{"Chetouane": 11.1 }],
        "Willaya" : "Tlemcen"

    },



     "Beni Snous" :{
        "Coordinates" : (34.66451726724494, -1.5439081125986043),
        "Neighbors": [{"Beni Boussaid": 41.1 },{"Sidi Djilali": 52.7 },{"Sabra": 34.8 },{"Mansourah": 40.3 },{"Sebdou": 30.8 }],
        "Willaya" : "Tlemcen"

    },




     "Sidi Djilali" :{
        "Coordinates" : (34.449704024959516, -1.5704891172001514),
        "Neighbors": [{"Beni Boussaid": 47.9 },{"Beni Snous": 47.7 },{"Sebdou": 38.0 },{"Mekmene Ben Amar": 132}],
        "Willaya" : "Tlemcen"

    },



     "Sebdou" :{
        "Coordinates" : (34.6368711368736, -1.3348086811153805),
        "Neighbors": [{"Sidi Djilali": 33.0 },{"Beni Snous": 30.8 },{"Mansourah":37.0  },{"Ouled Mimoun": 47.0 },{"Ain Tellout": 55.6 },{"Mekmene Ben Amar": 128},{"Ras El Ma": 56.0 }],
        "Willaya" : "Tlemcen"

    },




     "Ouled Mimoun" :{
        "Coordinates" : (34.910887153455555, -1.0347482650549447),
        "Neighbors": [{"Ain Tellout": 8.6 },{"Bensekrane": 35.3 },{"Sebdou": 47.0 },{"Chetouane": 30.6 },{"Mansourah": 37.8 }],
        "Willaya" : "Tlemcen"

    },



     "Ain Tellout" :{
        "Coordinates" : (34.92381021886822, -0.9526315764321143),
        "Neighbors": [{"Bensekrane": 43.9},{"Ouled Mimoun": 8.6 },{"Sebdou": 55.6},{"Ras El Ma": 74.8 },{"Moulay Slissen": 42.1},{"Sidi Ali Boussidi": 29.4},{"Ben Badis": 6.3}],
        "Willaya" : "Tlemcen"

    },

     "Lazharia" :{
        "Coordinates" : (35.93321961174845, 1.5653332353563865),
        "Neighbors": [{"Larbaa": 16.3},{"Lardjem": 33.6},{"Bordj Bounaama": 15.0 },{"Boucaid": 9.4 },{"Chlef": 41.6},{"El Karimia": 32.4}],
        "Willaya" : "Tissemsilt"

    },

     "Melaab" :{
        "Coordinates" : (35.71708393662898, 1.3360818065490176),
        "Neighbors": [{"Lardjem": 30.8 },{"Sidi Lantri": 20.4 },{"Oued Lilli ": 35.7 },{"Meghila": 18.7 },{"Ain Tarek": 29.2 },{"Ammi Moussa": 42.3 },{"Ramka": 28.1 },{"Ouled Ben Abdelkader": 71.3 }],
        "Willaya" : "Tissemsilt"

    },

     "Tamalaht" :{
        "Coordinates" : (35.81345955702604, 1.6251338761206493),
        "Neighbors": [{"Bordj Bounaama": 7.4 },{"Lardjem": 12.0 },{"Beni Lahcene": 11.2},{"Sidi Abed": 23.4 }],
        "Willaya" : "Tissemsilt"

    },

    "Beni Chaib" :{
        "Coordinates" : (35.81923410619948, 1.7916982895907332),
        "Neighbors": [{"Sidi Boutouchent": 23.1 },{"Khemisti": 31.6 },{"Ouled Bessem": 25.0 },{"Beni Lahcene": 28.4 },{"Sidi Slimane": 18.0 },{"Boucaid": 28.5 },{"Bathia": 37.0 }],
        "Willaya" : "Tissemsilt"

    },




    "Maacem" :{
        "Coordinates" : (35.66178765497059, 1.5535343309869636),
        "Neighbors": [{"Sidi Lantri": 9.2 },{"Lardjem": 14.4 },{"Ammari": 20.7 },{"Meghila": 33.1 }],
        "Willaya" : "Tissemsilt"

    },


     "Bordj El Emir Abdelkader" :{
        "Coordinates" : (35.867070444770185, 2.263364912017837),
        "Neighbors": [{"Youssoufia": 47.2 },{"Theniet El Had": 33.9 },{"Aziz": 21.0 },{"Chahbounia": 79.3 },{"Bordj Emir Khaled": 68.7 }],
        "Willaya" : "Tissemsilt"

    },

    "Tissemsilt" :{
        "Coordinates" : (35.60627885083578, 1.803692779759696),
        "Neighbors": [{"Khemisti": 21.3 },{"Ouled Bessem": 14.1 },{"Sidi Abed": 21.2 },{"Ammari": 15.9},{"Mahdia": 27.4 },{"Hamadia": 18.7 }],
        "Willaya" : "Tissemsilt"

    },





    "Larbaa" :{
        "Coordinates" : (35.90944493829677, 1.4757165619465282),
        "Neighbors": [{"Lazharia": 16.3 },{"Lardjem": 257 },{"Chlef": 52.6},{"Ouled Ben Abdelkader": 27.2},{"Lazharia":16.3}],
        "Willaya" : "Tissemsilt"

    },



    "Sidi Slimane" :{
        "Coordinates" : (35.86225636043489, 1.6813690436248),
        "Neighbors": [{"Boucaid":13.2 },{"Bordj Bounaama": 8.1 },{"Beni Lahcene": 10.4 },{"Beni Chaib": 18.0 }],
        "Willaya" : "Tissemsilt"

    },

     "Sidi Abed" :{
        "Coordinates" : (35.744832913557936, 1.7083784040004493),
        "Neighbors": [{"Tamalaht": 23.4},{"Beni Lahcene": 13.8 },{"Ouled Bessem": 21.9 },{"Tissemsilt": 21.2 },{"Ammari": 36.8 },{"Lardjem": 21.9 }],
        "Willaya" : "Tissemsilt"

    },

     "Sidi Boutouchent" :{
        "Coordinates" : (35.82314578905784, 1.9502661105804826),
        "Neighbors": [{"Beni Chaib": 23.1 },{"Khemisti": 25.6 },{"Theniet El Had": 14.6 },{"Bathia": 40.7 }],
        "Willaya" : "Tissemsilt"

    },


    "Boucaid" :{
        "Coordinates" : (35.88917602933468, 1.6205531403220519),
        "Neighbors": [{"Lazharia": 9.3 },{"Beni Chaib": 31.3 },{"Sidi Slimane": 13.2 },{"Bordj Bounaama": 5.6 },{"El Karimia": 41.8}],
        "Willaya" : "Tissemsilt"

    },

    "Beni Lahcene" :{
        "Coordinates" : (35.8140100066706, 1.6870199625225502),
        "Neighbors": [{"Sidi Slimane": 10.4 },{"Bordj Bounaama": 14.1 },{"Tamalaht": 11.4 },{"Sidi Abed": 13.8 },{"Ouled Bessem": 33.9 },{"Beni Chaib": 28.4 }],
        "Willaya" : "Tissemsilt"

    },

     "Ammari" :{
        "Coordinates" : (35.581122858964, 1.66030892544625),
        "Neighbors": [{"Maacem": 20.7 },{"Sidi Abed": 37.0 },{"Lardjem": 29.0 },{"Tissemsilt": 16.9 },{"Meghila": 31.6 },{"Mahdia": 23.4}],
        "Willaya" : "Tissemsilt"

    },

     "Laayoune" :{
        "Coordinates" : (35.69183756517791, 2.004195689840115),
        "Neighbors": [{"Theniet El Had": 25.8 },{"Khemisti": 5.2 },{"Chahbounia": 79.9 }],
        "Willaya" : "Tissemsilt"

    },


    "Lardjem" :{
        "Coordinates" : (35.747914520716286, 1.5517516957092659),
        "Neighbors": [{"Larbaa": 174 },{"Melaab": 110 },{"Sidi Lantri": 89.9 },{"Maacem": 86.4 },{"Ammari":69.2 },{"Sidi Abed": 64.1 },{"Tamalaht": 77.2 },{"Bordj Bounaama": 70.2 },{"Ramka": 32.9 },{"Ouled Ben Abdelkader": 67.3 }],
        "Willaya" : "Tissemsilt"

    },



    "Theniet El Had" :{
        "Coordinates" : (35.87017511294194, 2.026987749866004),
        "Neighbors": [{"Youssoufia": 13.2 },{"Bordj El Emid Abdelkader": 34.0 },{"Laayoune": 25.8 },{"Khemisti": 29.5 },{"Sidi Boutouchent": 14.5 },{"Chahbounia": 87.1 },{"Bathia": 27.3 },{"Bordj Emir Khaled": 39.3 }],
        "Willaya" : "Tissemsilt"

    },


     "Ouled Bessem" :{
        "Coordinates" : (35.68734229394798, 1.8717297107397604),
        "Neighbors": [{"Beni Chaib": 25.0 },{"Khemisti": 12.7 },{"Beni Lahcene": 33.9 },{"Sidi Abed": 21.9 },{"Tissemsilt": 13.7 }],
        "Willaya" : "Tissemsilt"

    },


     "Bordj Bounaama" :{
        "Coordinates" : (35.86620670144178, 1.6154500543485963),
        "Neighbors": [{"Lazharia": 15.0 },{"Boucaid": 5.6 },{"Sidi Slimane": 7.7},{"Beni Lahcene": 13.7 },{"Tamalaht": 7.4 },{"Lardjem": 19.4 }],
        "Willaya" : "Tissemsilt"

    },





    "Sidi Lantri" :{
        "Coordinates" : (35.69703617011286, 1.5052402938416443),
        "Neighbors": [{"Melaab": 20.4 },{"Lardjem": 10.4 },{"Maacem": 9.2 },{"Meghila": 41.0 }],
        "Willaya" : "Tissemsilt"

    },




    "Khemisti" :{
        "Coordinates" : (35.666962645434005, 1.965054332073991),
        "Neighbors": [{"Sidi Boutouchent": 25.6 },{"Theniet El Had": 29.6 },{"Laayoune": 5.2 },{"Tissemsilt": 21.7 },{"Ouled Bessem": 13.0 },{"Beni Chaib": 31.9 }],
        "Willaya" : "Tissemsilt"

    },

     "Youssoufia" :{
        "Coordinates" : (35.944700431661865, 2.110758504979362),
        "Neighbors": [{"Theniet El Had": 13.2 },{"Bordj El Emir Abdelkader": 47.2},{"Bordj Emir Khaled":26.0 }],
        "Willaya" : "Tissemsilt"

    },

    "Djelfa":
    {"Coordinates": (34.66776239309275, 3.244830003440457),
    "Neighbors": [{"Ain El Ibel" : 36.8} , {"Charef" : 51.7}, {"Hassi Bahbah" : 53.5}, {"Charef" : 51.7}],
    "Willaya": "Djelfa"},

    "Ain El Ibel":{
       "Coordinates": (34.36077995345297, 3.2326217770940526),
       "Neighbors": [{"El Idrissia" :75.2}, {"Charef" : 88.1}, {"Hassi Bahbah" :89.6}, {"Djelfa" : 36.8}, {"Charef" :88.1}, {"Ain Madhi" :136}, {"Sidi Makhlouf" :39.9}],
       "Willaya": "Djelfa"},

    "Ain Oussara":
       {
        "Coordinates": (35.43581730750858, 2.8770777208011173),
       "Neighbors": [{"Sidi Ladjel" : 40.2 }, {"Birine" :37.1 }, {"Had Sahary" : 45.7 }, {"Hassi Bahbah" : 45.2 }, {"Ksar Chellala" :65.6}, {"Chahbounia" :43.0 }, {"Ksar Boukhari":60.7}],
       "Willaya": "Djelfa"
       },

    "Birine":
       {
        "Coordinates": (35.63515151047458, 3.2240121603744627),
        "Neighbors": [{"Sidi Aissa" :85.6}, {"Ain Oussara" :37.1}, {"Had Sahary" :36.4}, {"Ksar Boukhari" :64.5}, {"Ain Boucif" :30.6}],
        "Willaya": "Djelfa"
        },

    "Charef":
      {
        "Coordinates": (34.61728006160189, 2.8078945141243272),
        "Neighbors": [{"Hassi Bahbah" :71.9}, {"Ain El Ibel": 88.1}, {"El Idrissia" : 35.7},{"Ain Madhi" :135}, {"Ksar Chellala" :113}],
        "Willaya": "Djelfa"
     },

    "Dar Chioukh":
    {
    "Coordinates": (34.8917186791102, 3.4837799520541246),
    "Neighbors": [{"Hassi Bahbah" :72.5}, {"Djelfa":41.5}, {"Ain El Ibel" :78.0}, {"Faidh El Botma" :80.0} , {"Medjedel":39.0}, {"Ain El Melh":89.4}],
    "Willaya": "Djelfa"
    },

    "El Idrissia":
    {
    "Coordinates": (34.447860363449976, 2.531927482841634),
    "Neighbors": [{"Charef":35.7}, {"Ain El Ibel":75.2},{ "Ain Madhi":104}, {"Sidi Makhlouf":79.6}],
    "Willaya": "Djelfa"
    },

    "Faidh El Botma":
    {
    "Coordinates": (34.52791955790591, 3.7829701143515218),
    "Neighbors": [{"Messaad": 51.6}, {"Ain El Ibel":90.5}, {"Dar Chioukh":80.0}, {"Ain El Melh" :55.2}, {"Ouergla":464}],
    "Willaya": "Djelfa"
    },

    "Had Sahary":
    {
    "Coordinates": (35.341677609957344, 3.383290496518867),
    "Neighbors": [{"Birine" :36.3}, {"Ain Oussara":45.7}, {"Hassi Bahbah":52.7} , {"Sidi Aissa":119}, {"Ain El Hadjel" :92.8}, {"Sidi Ameur" :59.0} , {"Medjedel" :97.2 }],
    "Willaya": "Djelfa"
    },

    "Hassi Bahbah":
    {
    "Coordinates": (35.06950367520502, 3.0258397389261242),
    "Neighbors": [{"Ain Oussara" :45.8}, {"Had Sahary" : 52.3} , {"Charef" :71.6}, {"Djelfa": 53.2}, {"Dar Chioukh" :72.2}, {"Ksar Chellala" :107}, {"Medjedel":89.4}],
    "Willaya": "Djelfa"
    },

    "Messaad":
    {
    "Coordinates": (34.15634118182557, 3.4833504806162026),
    "Neighbors": [{"Faidh El Botma": 51.5}, {"Ain El Ibel" :39.0}, {"Sidi Makhlouf" :57.6}, {"Ksar El Hirane" :66.4}, {"Ouergla" :470 },{ "Hassi R'Mel" :191}, {"Guerrara" : 216}],
    "Willaya": "Djelfa"
    },

    "Sidi Ladjel":
    {
    "Coordinates": (35.444012143216916, 2.529364855299953),
    "Neighbors": [{"Ain Oussara" :36.3}, {"Ksar Chellala": 31.9}, {"Chahbounia":13.4}],
    "Willaya": "Djelfa"
    },

    #jijel

    "Ziama Mansouriah": {
        "Coordinates": (36.67282627568828, 5.466261484890847),
        "Neighbors": [{"El Aouana" :22.0}, {"Texenna" :62.6}, {"Djimla":81.5} ,{ "Souk El Tenine":16.4}, {"Beni Ourtilane" :105}, {"Bouandas" :67.3}, {"Maoklane" :71.7}, {"Bougaa" : 80.1}, {"Ain Arnat" :85.8},{ "Amoucha" : 63.6}, {"Babor" :51.2}, {"Beni Aziz" :63.2}],
        "Willaya": "Jijel"
    },
    "El Aouana": {
        "Coordinates": (36.83110076465094, 5.565198812481819),
        "Neighbors": [{"Ziama Mansouriah" : 22.0}, {"Texenna": 40.3 }, {"Jijel":17.7}],
        "Willaya": "Jijel"
    },
    "Djimla": {
        "Coordinates": (36.57982085245279, 5.8849474402418025),
        "Neighbors": [{"Ziama Mansouriah" :82.3} , {"Taher" :43.9}, {"Texenna" :19.2}, {"Tassadane Haddada" :20.1}, {"Terrai Bainen" :31.7}],
        "Willaya": "Jijel"
    },
    "Texenna": {
        "Coordinates": (36.65988124149758, 5.787762470900542),
        "Neighbors": [{"Ziama Mansouriah" : 63.2}, {"Djimla": 19.2},{ "Jijel": 23.0},{ "El Aouana": 41.2}, {"Taher": 32.5}],
        "Willaya": "Jijel"
    },
    "Jijel": {
        "Coordinates": (36.819162495239354, 5.76303353795212),
        "Neighbors": [{"El Aouana": 17.7},{ "Texenna" :23.0}, {"Taher" :17.5}],
        "Willaya": "Jijel"
    },
    "Taher": {
        "Coordinates": (36.771898497264104, 5.899046471705657),
        "Neighbors": [{"Djimla":43.9},{ "Jijel" :17.4}, {"Texenna" : 33.1},{"Chekfa" :7.1 }, {"El Anceur" :32.8}, {"El Milia": 46.6}, {"Sidi Maarouf":62.2 }, {"Terrai Bainen" :49.8 }],
        "Willaya": "Jijel"
    },
    "Chekfa": {
        "Coordinates": (36.77173521539827, 5.959795173364028),
        "Neighbors": [{"Taher" :7.1},{ "El Anceur":30.9 }],
        "Willaya": "Jijel"
    },
    "El Anceur": {
        "Coordinates": (36.801437928559565, 6.155820081196583),
        "Neighbors": [{"Chekfa" :36.4}, {"Taher" :38.2}, {"El Milia" :19.3}, {"Sidi Maarouf" : 34.9}],
        "Willaya": "Jijel"
    },
    "El Milia": {
        "Coordinates": (36.75543147716313, 6.268135580322173),
        "Neighbors": [{"El Anceur" :14.3} , {"Taher" :46.7} ,{ "Sidi Maarouf":16.1}, {"Settara" :14.1}, {"Ouled Attia" :49.8}, {"Ain Kechra" :24.3} ],
        "Willaya": "Jijel"
    },
    "Sidi Maarouf": {
        "Coordinates": (36.64097584078952, 6.277155395916767),
        "Neighbors": [{"Taher" :62.4}, {"El Milia" :16.1}, {"Settara" :25.5} , {"Terrai Bainen" :29.7}  , {"Sidi Merouane" :28.0}, {"Grarem Gouga" :21.1}],
        "Willaya": "Jijel"
    },
    "Settara": {
        "Coordinates": (36.71991291565145, 6.333180742217417),
        "Neighbors": [{"El Milia" :10.9}, {"Sidi Maarouf":25.5}, {"Ain Kechra":11.6}, {"Oum Toub" :37.2}, {"Sidi Mezghiche" :55.4}, {"Grarem Gouga":45.1}],
        "Willaya": "Jijel"
    },


    #Skikda

    "Ain Kechra": {
        "Coordinates": (36.74613991115544, 6.440712844083357),
        "Neighbors": [{"Oum Toub" :25.6}, {"Tamalous" :25.1}, {"Collo" :48.9}, {"Ouled Attia" :50.6}, {"Settara" :11.6}, {"El Milia" :21.3}],
        "Willaya": "Skikda"
    },
    "Azzaba": {
        "Coordinates": (36.7302756243882, 7.11426085433153),
        "Neighbors": [{"El Harrouch" :28.4}, {"Ramdane Djamel" :25.8}, {"Skikda" :31.9}, {"Ben Azzouz" :25.0} , {"Ain Abid" :122}, {"Zighoud Youcef": 48.8}],
        "Willaya": "Skikda"
    },
    "Ben Azzouz": {
        "Coordinates": (36.8510189841856, 7.252857321021174),
        "Neighbors": [{"Azzaba" :25.4}, {"Ain Berda" :57.3}, {"Berrahal" :16.8}, {"Chetaibi" :40.7}],
        "Willaya": "Skikda"
    },
    "Collo": {
        "Coordinates": (36.99593665565768, 6.560718620726485),
        "Neighbors": [{"Zitouna" :78.8}, {"Ouled Attia" :94.1}, {"Ain Kechra" :68.0}, {"Tamalous" :43.3}],
        "Willaya": "Skikda"
    },
    "El Hadaiek": {
        "Coordinates": (36.81578957567842, 6.891805411291137),
        "Neighbors": [{"Tamalous" :38.8} , {"Sidi Mezghiche" :27.9}, {"El Harrouch" :26.9 }, {"Ramdane Djamel" :10.9}, {"Skikda" :5.1} ],
        "Willaya": "Skikda"
    },
    "El Harrouch": {
        "Coordinates": (36.650756972878035, 6.802417849400821),
        "Neighbors": [{"Sidi Mezghiche" :17.4 }, {"El Hadaiek" :26.7}, {"Ramdane Djamel" :14.9} , {"Azzaba" :28.0}, {"Hammam Debagh" :64.9}, {"Oued Zenati" :66.9}],
        "Willaya": "Skikda"
    },
    "Ouled Attia": {
        "Coordinates": (37.00200574929042, 6.353024108746074),
        "Neighbors": [{"Zitouna" :63.2} , {"Collo": 217}, {"Ain Kechra" :140}, {"El Milia" :120 }],
        "Willaya": "Skikda"
    },
    "Oum Toub": {
        "Coordinates": (36.690410700623296, 6.544239127862326),
        "Neighbors": [{"Ain Kechra" :25.6},{ "Tamalous" :33.7} , {"Sidi Mezghiche" :25.6}, {"Settara" :37.3 }],
        "Willaya": "Skikda"
    },
    "Ramdane Djamel": {
        "Coordinates": (36.74545141446928, 6.904041388729802),
        "Neighbors": [{"El Hadaiek" :10.7 }, {"Skikda" :13.9}, {"Azzaba" :25.3 }, {"El Harrouch" :14.9}],
        "Willaya": "Skikda"
    },
    "Sidi Mezghiche": {
        "Coordinates": (36.67944661236133, 6.723063732389039),
        "Neighbors": [{"Zighoud Youcef" :23.8},{ "Oum Toub" :25.6}, {"Tamalous" :26.2}, {"El Hadaiek" :27.8} , {"Ramdane Djamel" :25.1} , {"El Harrouch" :17.4}],
        "Willaya": "Skikda"
    },
    "Skikda": {
        "Coordinates": (36.85541447471929, 6.923267463737989),
        "Neighbors": [{"El Hadaiek" :5.2}, {"Ramdane Djamel" :14.1}, {"Azzaba" :32.6}],
        "Willaya": "Skikda"
    },
    "Tamalous": {
        "Coordinates": (36.83445379603984, 6.652637811321391),
        "Neighbors": [{"Collo" :43.1}, {"Ain Kechra": 25.1}, {"Oum Toub": 33.7}, {"Sidi Mezghiche": 26.2} , {"El Hadaiek" : 37.6}],
        "Willaya": "Skikda"
    },
    "Zitouna": {
        "Coordinates": (36.985182424152434, 6.463846768388473),
        "Neighbors": [{"Ouled Attia" :15.3}, {"Collo" :12.3}],
        "Willaya": "Skikda"
    },

    "Annaba": {
        "Coordinates": (36.890012203259424, 7.744571655236133),
        "Neighbors": [
            {"Berrahal": 30.6},
            {"El Bouni": 5.8}
        ],
        "Willaya": "Annaba"
    },
    "Ain Berda": {
        "Coordinates": (36.6513704772059, 7.6161594989333254),
        "Neighbors": [
            {"Berrahal": 43.3},
            {"El Hadjar": 23.3}
        ],
        "Willaya": "Annaba"
    },
    "El Hadjar": {
        "Coordinates": (36.78158992339118, 7.71443732044553),
        "Neighbors": [
            {"Ain Berda": 23.0},
            {"Berrahal": 32.4},
            {"El Bouni": 8.0},
            {"Ben Mehidi": 17.8},
            {"Besbes": 18.1},
            {"Drean": 16.5}
        ],
        "Willaya": "Annaba"
    },
    "Berrahal": {
        "Coordinates": (36.83247705036744, 7.468913559706108),
        "Neighbors": [
            {"Chetaibi": 34.3},
            {"Annaba": 30.8},
            {"El Bouni": 28.9},
            {"El Hadjar": 32.0},
            {"Ain Berda": 40.6},
            {"Ben Azzouz": 19.7}
        ],
        "Willaya": "Annaba"
    },
    "Chetaibi": {
        "Coordinates": (37.061847634825675, 7.382058875853706),
        "Neighbors": [
            {"Ben Azzouz": 41.3},
            {"Berrahal": 34.4}
        ],
        "Willaya": "Annaba"
    },
    "El Bouni": {
        "Coordinates": (36.85273688603536, 7.740559589492626),
        "Neighbors": [
            {"Annaba": 6.8},
            {"Berrahal": 29.4},
            {"El Hadjar": 6.9},
            {"Ben Mehidi": 20.9}
        ],
        "Willaya": "Annaba"
    },




    #El Tarf

    "El Tarf": {
        "Coordinates": [36.76379308628625, 8.31941482579453],
        "Neighbors": [
            {"El Kala": 112},
            {"Bouteldja": 11.9},
            {"Bouhadjar": 41.7}
        ],
        "Willaya": "El Tarf"
    },
    "El Kala": {
        "Coordinates": [36.88030670207156, 8.449003828245976],
        "Neighbors": [
            {"Ben Mehidi": 69.0},
            {"Bouteldja": 33.2},
            {"El Tarf": 112}
        ],
        "Willaya": "El Tarf"
    },
    "Ben Mehidi": {
        "Coordinates": [36.767063151024054, 7.878305164915042],
        "Neighbors": [
            {"Besbes": 10.4},
            {"Bouteldja": 31.6},
            {"El Kala": 70.3}
        ],
        "Willaya": "El Tarf"
    },
    "Besbes": {
        "Coordinates": [36.707800988383276, 7.839722720070134],
        "Neighbors": [
            {"Drean": 10.3},
            {"Ben Mehidi": 10.3},
            {"Bouteldja": 38.9},
            {"Bouhadjar": 53.5},
            {"El Hadjar": 53.5}
        ],
        "Willaya": "El Tarf"
    },
    "Drean": {
        "Coordinates": [36.67041655188626, 7.767380635985931],
        "Neighbors": [
            {"El Hadjar": 17.0},
            {"Besbes": 10.3},
            {"Bouhadjar": 63.8}
        ],
        "Willaya": "El Tarf"
    },
    "Bouhadjar": {
        "Coordinates": [36.50906886808329, 8.090508611562036],
        "Neighbors": [
            {"Drean": 63.8},
            {"Besbes": 53.5},
            {"Bouteldja": 49.5},
            {"El Tarf": 41.6},
            {"Bouchegouf": 44.9}
        ],
        "Willaya": "El Tarf"
    },
    "Bouteldja": {
        "Coordinates": [36.78637787579464, 8.206255946096762],
        "Neighbors": [
            {"Besbes": 38.1},
            {"Ben Mehidi": 30.2},
            {"Bouhadjar": 46.4},
            {"El Tarf": 13.6},
            {"El Kala": 34.7}
        ],
        "Willaya": "El Tarf"
    },



  #Guelma
    "Guelma": {
        "Coordinates": (36.46550401172991, 7.415006142051135),
        "Neighbors": [
            {"Ain Makhlouf": 48.1},
            {"Houari Boumediene": 20.0},
            {"Heliopolis": 5.8},
            {"Guelaat Bou Sbaa": 11.8}
        ],
        "Willaya": "Guelma"
    },
    "Khezarra": {
        "Coordinates": (36.36299924523962, 7.524321911296529),
        "Neighbors": [
            {"Guelaat Bou Sbaa": 29.7},
            {"Ain Makhlouf": 40.4},
            {"Hammam N'Bails": 28.7},
            {"Sedrata": 42.2}
        ],
        "Willaya": "Guelma"
    },
    "Guelaat Bou Sbaa": {
        "Coordinates": (36.49183053944409, 7.542078882670495),
        "Neighbors": [
            {"Heliopolis": 6.8},
            {"Guelma": 12.6},
            {"Ain Makhlouf": 62.1},
            {"Khezarra": 29.7},
            {"Hammam N'Bails": 46.2},
            {"Bouchegouf": 41.3},
            {"Ain Berda": 18.2}
        ],
        "Willaya": "Guelma"
    },
    "Heliopolis": {
        "Coordinates": (36.51864500778295, 7.448497258596629),
        "Neighbors": [
            {"Hammam Debagh": 24.1},
            {"Houari Boumediene": 23.5},
            {"Guelma": 6.7},
            {"Guelaat Bou Sbaa": 6.7},
            {"Ain Berda": 24.7}
        ],
        "Willaya": "Guelma"
    },
    "Oued Zenati": {
        "Coordinates": (36.30490542707151, 7.180527947409818),
        "Neighbors": [
            {"Hammam Debagh": 27.1},
            {"Houari Boumediene": 20.1},
            {"Ain Makhlouf": 15.8},
            {"Ain Abid": 24.6}
        ],
        "Willaya": "Guelma"
    },
    "Ain Makhlouf": {
        "Coordinates": (36.243430200287754, 7.254435231009681),
        "Neighbors": [
            {"Oued Zenati": 22.9},
            {"Houari Boumediene": 30.6},
            {"Guelma": 47.7},
            {"Guelaat Bou Sbaa": 11.8},
            {"Khezarra": 15.0},
            {"Ain Abid": 63.7},
            {"Sigus": 97.9},
            {"Ain Babouche": 50.0},
            {"Ksar Sbahi": 27.1}
        ],
        "Willaya": "Guelma"
    },
    "Hammam Debagh": {
        "Coordinates": (36.46757793395778, 7.286063601271998),
        "Neighbors": [
            {"Oued Zenati": 27.1},
            {"Houari Boumediene": 7.6},
            {"Heliopolis": 23.8},
            {"Ben Azzouz": 64.6},
            {"Azzaba": 54.3},
            {"El Harrouch": 64.9}
        ],
        "Willaya": "Guelma"
    },
    "Bouchegouf": {
        "Coordinates": (36.488314104569305, 7.696100880949654),
        "Neighbors": [
            {"Guelaat Bou Sbaa": 31.1},
            {"Hammam N'Bails": 51.6},
            {"Ain Berda": 47.7},
            {"Drean": 69.8},
            {"Bouhadjar": 101}
        ],
        "Willaya": "Guelma"
    },
    "Hammam N'Bails": { 
        "Coordinates": (36.34161901877942, 7.6982656195984696),
        "Neighbors": [
            {"Khezarra": 24.2},
            {"Guelaat Bou Sbaa": 41.6},
            {"Bouchegouf": 24.2},
            {"Mechroha": 25.8},
            {"Sedrata": 36.7}
        ],
        "Willaya": "Guelma"
    },
    "Houari Boumediene": {
        "Coordinates": (36.422676530202914, 7.281499354196),
        "Neighbors": [
            {"Hammam Debagh": 7.6},
            {"Oued Zenati": 19.9},
            {"Ain Makhlouf": 33.4},
            {"Khezarra": 35.4},
            {"Guelma": 19.8},
            {"Heliopolis": 23.0}
        ],
        "Willaya": "Guelma"
    },





    #Tipaza
    "Ahmar El Ain": {
        "Coordinates": [36.479091869599436, 2.5706876639061593],
        "Neighbors": [
            {"Hadjout": 14.1},
            {"Tipaza": 25.5},
            {"Bou Ismail": 34.9},
            {"Kolea": 38.6},
            {"El Affroun": 5.6},
            {"Mouzaia": 11.6},
            {"Oued Djer":14.2}
        ],
        "Willaya": "Tipaza"
    },
    "Bou Ismail": {
        "Coordinates": [36.64384347819544, 2.702828459372382],
        "Neighbors": [
            {"Tipaza": 35.3},
            {"Hadjout": 36.0},
            {"Ahmar El Ain": 35.4},
            {"Kolea": 8.8},
            {"Fouka": 6.1}
        ],
        "Willaya": "Tipaza"
    },
    "Cherchell": {
        "Coordinates": [36.59543702339444, 2.2002119789471997],
        "Neighbors": [
            {"Gouraya": 28.5},
            {"Sidi Amar": 14.7},
            {"Tipaza": 27.8},
            {"El Amra": 69.7}
        ],
        "Willaya": "Tipaza"
    },
    "Damous": {
        "Coordinates": [36.54949536175499, 1.706335132727365],
        "Neighbors": [
            {"Gouraya": 19.4},
            {"El Abadia": 47.3},
            {"Beni Haoua": 16.2}
        ],
        "Willaya": "Tipaza"
    },
    "Fouka": {
        "Coordinates": [36.66122227656188, 2.743753170729661],
        "Neighbors": [
            {"Bou Ismail": 7.1},
            {"Kolea": 3.7},
            {"Oued Alleug": 16.2},
            {"Zeralda": 14.4}
        ],
        "Willaya": "Tipaza"
    },
    "Gouraya": {
        "Coordinates": [36.57063754614868, 1.9032774635866785],
        "Neighbors": [
            {"Cherchell": 30.7},
            {"Damous": 19.4},
            {"El Amra": 61.5},
            {"El Abadia": 66.7}
        ],
        "Willaya": "Tipaza"
    },
    "Hadjout": {
        "Coordinates": [36.51327450386588, 2.417952721527025],
        "Neighbors": [
            {"Sidi Amar": 12.4},
            {"Tipaza": 11.9},
            {"Ahmar El Ain": 14.1},
            {"Hammam Righa": 23.8},
            {"Miliana": 52.8},
            {"El Amra": 106}
        ],
        "Willaya": "Tipaza"
    },


    "Kolea": {
        "Coordinates": [36.637156747941845, 2.7700612030128835],
        "Neighbors": [
            {"Ahmar El Ain": 39.1},
            {"Bou Ismail": 7.1},
            {"Fouka": 3.7},
            {"El Affroun": 28.9},
            {"Mouzaia": 32.7},
            {"Oued Alleug": 10.5}
        ],
        "Willaya": "Tipaza"
    },
    "Sidi Amar": {
        "Coordinates": [36.54391007488069, 2.301206457833742],
        "Neighbors": [
            {"Cherchell": 14.9},
            {"Tipaza": 17.3},
            {"Hadjout": 12.5},
            {"Hammam Righa": 36.3},
            {"Miliana": 50.4},
            {"El Amra": 119}
        ],
        "Willaya": "Tipaza"
    },
    "Tipaza": {
        "Coordinates": [36.59530761734122, 2.4472205483439047],
        "Neighbors": [
            {"Cherchell": 26.5},
            {"Sidi Amar": 17.2},
            {"Hadjout": 12.0},
            {"Ahmar El Ain": 20.4},
            {"Bou Ismail": 35.6}
        ],
        "Willaya": "Tipaza"
    },
    "Ain Defla": {
        "Coordinates": [36.2606924857707, 1.948149478884838],
        "Neighbors": [
            {"El Amra": 15.1},
            {"Rouina": 14.4},
            {"Djelida": 16.9},
            {"Khemis Miliana": 27.7},
            {"Miliana": 32.8}
        ],
        "Willaya": "Ain Defla"
    },
    "Ain Lechiekh": {
        "Coordinates": [36.16204357442098, 2.391151918635883],
        "Neighbors": [
            {"Bordj Emir Khaled": 26.5},
            {"Khemis Miliana": 25.6},
            {"Miliana": 33.5},
            {"Hammam Righa": 41.6},
            {"Boumedfaa": 33.3},
            {"Aziz": 83.2},
            {"Ouled Antar": 93.8}
        ],
        "Willaya": "Ain Defla"
    },
    "Bathia": {
        "Coordinates": [35.91463670418284, 1.8395382086088887],
        "Neighbors": [
            {"Rouina": 63.9},
            {"Djelida": 55.2},
            {"Bordj Emir Khaled": 66.6},
            {"El Karimia": 90.8},
            {"Lazharia": 49.5},
            {"Bordj Bounaama": 35.1},
            {"Theniet El Had": 27.3}
        ],
        "Willaya": "Ain Defla"
    },
    "Bordj Emir Khaled": {
        "Coordinates": [36.124481177942776, 2.2039203037730886],
        "Neighbors": [
            {"Bathia": 66.6},
            {"Djelida": 20.1},
            {"Khemis Miliana": 18.1},
            {"Ain Lechiekh": 26.6},
            {"Theniet El Had": 39.3},
            {"Bordj El Emir Abdelkader": 68.6},
            {"Aziz": 66.2}
        ],
        "Willaya": "Ain Defla"
    },
    "Boumedfaa": {
        "Coordinates": [36.36920232929514, 2.472277663262933],
        "Neighbors": [
            {"Hammam Righa": 11.1},
            {"Khemis Miliana": 35.0},
            {"Ain Lechiekh": 33.3},
            {"Djendel": 26.4},
            {"Ouamri": 34.0},
            {"Medea": 58.8},
            {"El Affroun": 23.0},
            {"Oued Djer":15.4}
        ],
        "Willaya": "Ain Defla"
    },
    "Djelida": {
        "Coordinates": [36.204416708540506, 2.088779454854845],
        "Neighbors": [
            {"Ain defla": 17.7},
            {"Rouina": 31.8},
            {"Bathia": 55.1},
            {"Bordj Emir Khaled": 20.1},
            {"Khemis Miliana": 17.5},
            {"El Amra": 32.4}
        ],
        "Willaya": "Ain Defla"
    },
    "Djendel": {
        "Coordinates": [36.220768230379406, 2.416173180446216],
        "Neighbors": [
            {"Hammam Righa": 34.7},
            {"Boumedfaa": 26.4},
            {"Ain Lechiekh": 8.5},
            {"Ouled Antar": 90.5},
            {"Si Mahdjoub": 42.7},
            {"Ouamri": 19.1}
        ],
        "Willaya": "Ain Defla"
    },
    "El Abadia": {
        "Coordinates": [36.27285866449264, 1.6861483704278095],
        "Neighbors": [
            {"El Amra": 15.3},
            {"Rouina": 17.5},
            {"El Attaf": 6.8},
            {"Gouraya": 67.1},
            {"Beni Haoua": 52.0},
            {"Zeboudja": 35.0},
            {"Oued Fodda": 20.3}
        ],
        "Willaya": "Ain Defla"
    },
    "El Amra": {
        "Coordinates": [36.30474279377104, 1.841815687521703],
        "Neighbors": [
            {"El Abadia": 15.3},
            {"El Attaf": 20.7},
            {"Rouina": 12.5},
            {"Ain Defla": 15.1},
            {"Djelida": 32.4},
            {"Khemis Miliana": 42.6},
            {"Miliana": 47.8},
            {"Gouraya": 61.5},
            {"Hadjout": 107},
            {"Sidi Amar": 124}
        ],
        "Willaya": "Ain Defla"
    },
    "El Attaf": {
        "Coordinates": [36.22425583060551, 1.675471850485315],
        "Neighbors": [
            {"El Abadia": 6.8},
            {"El Amra": 20.7},
            {"Rouina": 12.5},
            {"Oued Fodda": 35.0},
            {"El Karimia": 38.7}
        ],
        "Willaya": "Ain Defla"
    },
    "Hammam Righa": {
        "Coordinates": [36.377453540610695, 2.392516962587513],
        "Neighbors": [
            {"Miliana": 38.0},
            {"Khemis Miliana": 42.8},
            {"Ain Lechiekh": 41.6},
            {"Djendel": 34.7},
            {"Boumedfaa": 11.1},
            {"Hadjout": 23.8},
            {"Sidi Amar": 36.2}
        ],
        "Willaya": "Ain Defla"
    },
    "Khemis Miliana": {
        "Coordinates": [36.26048527623002, 2.2363591795446585],
        "Neighbors": [
            {"El Amra": 43.9},
            {"Ain Defla": 29.1},
            {"Djelida": 20.2},
            {"Bordj Emir Khaled": 18.6},
            {"Ain Lechiekh": 26.1},
            {"Hammam Righa": 37.4},
            {"Djendel": 26.1}
        ],
        "Willaya": "Ain Defla"
    },
    "Miliana": {
        "Coordinates": [36.30853890866669, 2.228662943470032],
        "Neighbors": [
            {"El Amra": 46.4},
            {"Ain Defla": 31.7},
            {"Khemis Miliana": 9.5},
            {"Ain Lechiekh": 33.4},
            {"Hammam Righa": 38.1},
            {"Hadjout": 52.9},
            {"Sidi Amar": 50.5}
        ],
        "Willaya": "Ain Defla"
    },
    "Rouina": {
        "Coordinates": [36.24126863755733, 1.815308311304965],
        "Neighbors": [
            {"El Attaf": 13.3},
            {"El Abadia": 16.7},
            {"El Amra": 12.6},
            {"Ain Defla": 14.4},
            {"Djelida": 31.3},
            {"Bathia": 63.8},
            {"El Karimia": 31.3}
        ],
        "Willaya": "Ain Defla"
    },



    #Sidi Bel Abbes
    "Ain el Berd": {
        "Coordinates": [35.3676470566797, -0.5149534338649147],
        "Neighbors": [
            {"Tessala": 33.6},
            {"Sidi Bel Abbes": 23.3},
            {"Mostefa Ben Brahim": 49.1},
            {"Sfisef": 49.1},
            {"Gdyel": 72.4},
            {"Oggaz": 40.1}
        ],
        "Willaya": "Sidi Bel Abbes"
    },
    "Ben Badis": {
        "Coordinates": [34.95023500765756, -0.9142461838907768],
        "Neighbors": [
            {"Sidi Ali Boussidi": 23.4},
            {"Sidi Ali Benyoub": 20.3},
            {"Moulay Slissen": 35.5},
            {"Ain Tallout": 6.0}
        ],
        "Willaya": "Sidi Bel Abbes"
    },
    "Marhoum": {
        "Coordinates": [34.44462551789637, -0.19158540828519072],
        "Neighbors": [
            {"Ras El Ma": 63.7},
            {"Telagh": 60.7},
            {"Merine": 49.9},
            {"Makman Ben Amer": 137},
            {"Mecheria": 120},
            {"Bougtoub": 54.9},
            {"Ain El Hadjar": 51.2}
        ],
        "Willaya": "Sidi Bel Abbes"
    },
    "Merine": {
        "Coordinates": [34.780727425444965, -0.4544527689324326],
        "Neighbors": [
            {"Tenira": 34.1},
            {"Telagh": 12.0},
            {"Marhoum": 50.2},
            {"Ain El Hadjar": 67.1}
        ],
        "Willaya": "Sidi Bel Abbes"
    },
    "Mostefa Ben Brahim": {
        "Coordinates": [35.19087309053898, -0.36138614359508386],
        "Neighbors": [
            {"Ain el Berd": 43.1},
            {"Sidi Bel Abbes": 26.7},
            {"Sidi Lahcene": 31.6},
            {"Tenira": 39.2},
            {"Sfisef": 12.0}
        ],
        "Willaya": "Sidi Bel Abbes"
    },
    "Moulay Slissen": {
        "Coordinates": [34.81349243407858, -0.7621925807952785],
        "Neighbors": [
            {"Ben Badis": 36.3},
            {"Sidi Ali Benyoub": 17.4},
            {"Telagh": 20.0},
            {"Ras El Ma": 40.6},
            {"Ain Tallout": 43.0}
        ],
        "Willaya": "Sidi Bel Abbes"
    },
    "Ras El Ma": {
        "Coordinates": [34.49986618434724, -0.8188576820837059],
        "Neighbors": [
            {"Moulay Slissen": 40.6},
            {"Telagh": 42.6},
            {"Marhoum": 63.8},
            {"Ain Tallout": 74.8},
            {"Sebdou": 56.0},
            {"Makman Ben Amer": 115},
            {"Mecheria": 153}
        ],
        "Willaya": "Sidi Bel Abbes"
    },
    "Sfisef": {
        "Coordinates": [35.23171644330794, -0.24036249950103336],
        "Neighbors": [
            {"Ain el Berd": 55.1},
            {"Mostefa Ben Brahim": 12.0},
            {"Tenira": 40.2},
            {"Youb": 39.4},
            {"Sidi Boubekeur": 54.5},
            {"Ain Fekan": 27.6},
            {"Bou Hanifia": 22.3},
            {"Sig": 52.6},
            {"Oggaz": 63.8}
        ],
        "Willaya": "Sidi Bel Abbes"
    },
    "Sidi Ali Benyoub": {
        "Coordinates": [34.94401247649824, -0.717037835291523],
        "Neighbors": [
            {"Ben Badis": 20.3},
            {"Moulay Slissen": 17.4},
            {"Telagh": 24.4},
            {"Tenira": 20.8},
            {"Sidi Lahcene": 29.9},
            {"Sidi Ali Boussidi": 24.2}
        ],
        "Willaya": "Sidi Bel Abbes"
    },
    "Sidi Ali Boussidi": {
        "Coordinates": [35.10219855708, -0.8269879078261507],
        "Neighbors": [
            {"Tessala": 35.1},
            {"Ain el Berd": 52.1},
            {"Sidi Ali Benyoub": 24.3},
            {"Ben Badis": 23.4},
            {"Hammam Bou Hadjar": 44.5},
            {"Ain Kihal": 42.3},
            {"Ain Tallout": 29.4}
        ],
        "Willaya": "Sidi Bel Abbes"
    },
    "Sidi Bel Abbes": {
        "Coordinates": [35.209584324455136, -0.6293360166754199],
        "Neighbors": [
            {"Ain el Berd": 23.3},
            {"Tessala": 15.1},
            {"Sidi Lahcene": 9.7},
            {"Mostefa Ben Brahim": 26.7}
        ],
        "Willaya": "Sidi Bel Abbes"
    },
    "Sidi Lahcene": {
        "Coordinates": [35.168214402754465, -0.6928760388273897],
        "Neighbors": [
            {"Tessala": 18.7},
            {"Sidi Bel Abbes": 8.7},
            {"Sidi Ali Boussidi": 15.6},
            {"Mostefa Ben Brahim": 31.6},
            {"Tenira": 32.1},
            {"Sidi Ali Benyoub": 29.9}
        ],
        "Willaya": "Sidi Bel Abbes"
    },

     "Telagh": {
        "Coordinates": [34.78099455404931, -0.5743138050434418],
        "Neighbors": [
            {"Sidi Ali Benyoub": 24.4},
            {"Moulay Slissen": 20.0},
            {"Ras El Ma": 42.6},
            {"Marhoum": 60.6},
            {"Merine": 11.7},
            {"Tenira": 28.5}
        ],
        "Willaya": "Sidi Bel Abbes"
    },
    "Tenira": {
        "Coordinates": [35.023510350522365, -0.5289220520138695],
        "Neighbors": [
            {"Sfisef": 97.3},
            {"Mostefa Ben Brahim": 109},
            {"Sidi Bel Abbes": 144},
            {"Sidi Lahcene": 149},
            {"Sidi Ali Benyoub": 152},
            {"Telagh": 125},
            {"Merine": 113},
            {"Youb": 89.6},
            {"Sidi Boubekeur": 55.2}
        ],
        "Willaya": "Sidi Bel Abbes"
    },
    "Tessala": {
        "Coordinates": [35.24880790819445, -0.7770684882122681],
        "Neighbors": [
            {"Sidi Ali Boussidi": 35.1},
            {"Sidi Bel Abbes": 15.1},
            {"Sidi Lahcene": 17.9},
            {"Ain el Berd": 41.4},
            {"Gdyel": 105},
            {"Ain El Arbaa": 30.6},
            {"Hammam Bou Hadjar": 30.9},
            {"Ain Kihal": 58.6}
        ],
        "Willaya": "Sidi Bel Abbes"
    },

    #Saida

    "Saida": {
        "Coordinates": [34.89500798875628, 0.126526281534326],
        "Neighbors": [
            {"Youb": 29.3},
            {"Sidi Boubekeur": 43.1},
            {"Ouled Brahim": 40.2},
            {"El Hassasna": 49.3},
            {"Ain El Hadjar": 43.1}
        ],
        "Willaya": "Saida"
    },
    "Ain El Hadjar": {
        "Coordinates": [34.7539499843392, 0.13974415420692413],
        "Neighbors": [
            {"Youb": 43.1},
            {"Saida": 29.3},
            {"El Hassasna": 49.3},
            {"Merine": 71.0},
            {"Marhoum": 91.5}
        ],
        "Willaya": "Saida"
    },
    "Sidi Boubekeur": {
        "Coordinates": [35.02722625812154, 0.060439709237937206],
        "Neighbors": [
            {"Youb": 32.7},
            {"Saida": 29.3},
            {"El Hassasna": 49.3},
            {"Ouled Brahim": 55.7},
            {"Tenira": 74.0},
            {"Sfisef": 54.6},
            {"Ain Fekan": 27.0},
            {"Oued Taria": 0.0},
            {"Aouf": 40.4}
        ],
        "Willaya": "Saida"
    },
    "El Hassasna": {
        "Coordinates": [34.848647628363324, 0.3155524784634614],
        "Neighbors": [
            {"Ain El Hadjar": 21.6},
            {"Saida": 193},
            {"Sidi Boubekeur": 221},
            {"Ouled Brahim": 412},
            {"Frenda": 148},
            {"Ain Kermes": 126},
            {"Rogassa": 225},
            {"Bougtoub": 104}
        ],
        "Willaya": "Saida"
    },
    "Ouled Brahim": {
        "Coordinates": [34.9890885866458, 0.48448341298404],
        "Neighbors": [
            {"Sidi Boubekeur": 55.7},
            {"El Hassasna": 29.3},
            {"Aouf": 22.0},
            {"Frenda": 64.3},
            {"Ain Kermes": 72.1}
        ],
        "Willaya": "Saida"
    },
    "Youb": {
        "Coordinates": [34.923707628301905, -0.20531790119271437],
        "Neighbors": [
            {"Sidi Boubekeur": 32.7},
            {"Saida": 41.0},
            {"Ain El Hadjar": 43.6},
            {"Sfisef": 39.4},
            {"Tenira": 41.3}
        ],
        "Willaya": "Saida"
    },



    # Souk Ahras
    "Bir Bou Haouch": {
        "Coordinates": (36.006996468669726, 7.439764513880183),
        "Neighbors": [
            {"Sedrata": 19.9},
            {"Oum El Adhaim": 22.5},
            {"Ain Makhlouf": 62.8},
            {"Ain Beida": 27.1},
            {"Ksar Sbahi": 21.0}
        ],
        "Willaya": "Souk Ahras"
    },
    "Heddada": {
        "Coordinates": (36.22399657212742, 8.31689498241057),
        "Neighbors": [
            {"Ouled Driss": 56.2},
            {"Merahna": 18.8}
        ],
        "Willaya": "Souk Ahras"
    },
    "M'daourouch": {
        "Coordinates": (36.07424430295405, 7.837114599942476),
        "Neighbors": [
            {"Sedrata": 28.3},
            {"Oum El Adhaim": 21.5},
            {"Taoura": 24.5},
            {"Mechroha": 55.4}
        ],
        "Willaya": "Souk Ahras"
    },
    "Mechroha": {
        "Coordinates": (36.358002889530326, 7.873977292099075),
        "Neighbors": [
            {"Sedrata": 63.4},
            {"M'daourouch": 55.1},
            {"Taoura": 39.6},
            {"Souk Ahras": 16.2},
            {"Ouled Driss": 31.9},
            {"Bouhadjar": 41.3},
            {"Bouchegouf": 22.2},
            {"Hammam N'Bails": 21.1},
            {"Khezarra": 49.0},
            {"Ain Makhlouf": 71.6}
        ],
        "Willaya": "Souk Ahras"
    },
    "Merahna": {
        "Coordinates": (36.19965919919199, 8.172616654302129),
        "Neighbors": [
            {"Taoura": 11.9},
            {"Souk Ahras": 26.0},
            {"Ouled Driss": 37.4},
            {"Heddada": 18.8},
            {"El Aouinet": 62.8},
            {"Ouenza": 41.3}
        ],
        "Willaya": "Souk Ahras"
    },
    "Ouled Driss": {
        "Coordinates": (36.35491777535199, 8.032380269324024),
        "Neighbors": [
            {"Mechroha": 32.3},
            {"Souk Ahras": 18.9},
            {"Taoura": 33.4},
            {"Merahna": 37.6},
            {"Heddada": 56.4},
            {"Bouhadjar": 24.6}
        ],
        "Willaya": "Souk Ahras"
    },
    "Oum El Adhaim": {
        "Coordinates": (36.02523421902211, 7.584658358706594),
        "Neighbors": [
            {"Bir Bou Haouch": 22.5},
            {"Sedrata": 16.8},
            {"M'daourouch": 25.2},
            {"Taoura": 53.0},
            {"Meskiana": 51.0},
            {"Ain Berda": 105},
            {"El Aouinet": 45.8},
            {"Ouenza": 67.4}
        ],
        "Willaya": "Souk Ahras"
    },
    "Sedrata": {
        "Coordinates": (36.14141150160344, 7.547277855595063),
        "Neighbors": [
            {"Bir Bou Haouch": 19.6},
            {"Oum El Adhaim": 16.8},
            {"M'daourouch": 28.3},
            {"Mechroha": 63.6},
            {"Khezarra": 42.3},
            {"Ain Makhlouf": 37.5},
            {"Ksar Sbahi": 35.4},
            {"Ain Beida": 46.7}
        ],
        "Willaya": "Souk Ahras"
    },
    "Souk Ahras": {
        "Coordinates": (36.28210263205616, 7.974191843173926),
        "Neighbors": [
            {"Mechroha": 16.5},
            {"M'daourouch": 38.9},
            {"Taoura": 23.3},
            {"Merahna": 27.5},
            {"Ouled Driss": 17.5}
        ],
        "Willaya": "Souk Ahras"
    },
    "Taoura": {
        "Coordinates": (36.16838522312246, 8.030090980350199),
        "Neighbors": [
            {"Oum El Adhaim": 50.2},
            {"M'daourouch": 25.4},
            {"Mechroha": 36.9},
            {"Souk Ahras": 21.9},
            {"El Aouinet": 51.3},
            {"Ouenza": 30.0},
            {"Merahna": 11.7}
        ],
        "Willaya": "Souk Ahras"
    },

    # Mila
    "Mila": {
        "Coordinates": (36.444942409099525, 6.266273889694538),
        "Neighbors": [
            {"Grarem Gouga": 13.1},
            {"Sidi Merouane": 13.1},
            {"Oued Endja": 27.2},
            {"Chelghoum Laid": 46.7},
            {"Ibn Ziad": 30.5}
        ],
        "Willaya": "Mila"
    },
    "Chelghoum Laid": {
        "Coordinates": (36.15373898525904, 6.198232263523235),
        "Neighbors": [
            {"Mila": 46.7},
            {"Oued Endja": 53.1},
            {"Bouhatem": 25.2},
            {"Tadjenanet": 19.8},
            {"Teleghma": 18.8},
            {"Ibn Ziad": 49.6},
            {"El Khroub": 65.8}
        ],
        "Willaya": "Mila"
    },
    "Ferdjioua": {
        "Coordinates": (36.412849980554235, 5.982376070152208),
        "Neighbors": [
            {"Tassadane Haddada": 20.7},
            {"Ain Beida Harriche": 5.9},
            {"Bouhatem": 16.6},
            {"Rouached": 16.5}
        ],
        "Willaya": "Mila"
    },
    "Grarem Gouga": {
        "Coordinates": (36.505315686492644, 6.353085619637233),
        "Neighbors": [
            {"Sidi Merouane": 9.0},
            {"Mila": 13.2},
            {"Settara": 41.7},
            {"Sidi Maarouf": 17.9},
            {"Ibn Ziad": 41.1},
            {"Zighoud Youcef": 45.1}
        ],
        "Willaya": "Mila"
    },
    "Oued Endja": {
        "Coordinates": (36.504385048826585, 6.0731865779402145),
        "Neighbors": [
            {"Terrai Bainen": 8.7},
            {"Rouached": 17.2},
            {"Bouhatem": 45.0},
            {"Chelghoum Laid": 53.0},
            {"Mila": 27.0},
            {"Sidi Merouane": 31.3}
        ],
        "Willaya": "Mila"
    },
    "Rouached": {
        "Coordinates": (36.45987769790455, 6.049422396897867),
        "Neighbors": [
            {"Terrai Bainen": 20.4},
            {"Tassadane Haddada": 25.7},
            {"Ferdjioua": 16.5},
            {"Bouhatem": 32.8},
            {"Oued Endja": 17.1}
        ],
        "Willaya": "Mila"
    },
    "Terrai Bainen": {
        "Coordinates": (36.53429135310799, 6.126418251788934),
        "Neighbors": [
            {"Tassadane Haddada": 52.5},
            {"Rouached": 20.5},
            {"Oued Endja": 8.7},
            {"Sidi Merouane": 34.6},
            {"Taher": 55.3},
            {"Sidi Maarouf": 29.7},
            {"Djimla": 31.7}
        ],
        "Willaya": "Mila"
    },
    "Tassadane Haddada": {
        "Coordinates": (36.50229869698304, 5.8735354815407845),
        "Neighbors": [
            {"Ain Beida Harriche": 18.9},
            {"Ferdjioua": 20.8},
            {"Rouached": 25.7},
            {"Terrai Bainen": 52.5},
            {"Djimla": 20.1},
            {"Taher": 60.2},
            {"Beni Aziz": 48.7}
        ],
        "Willaya": "Mila"
    },
    "Ain Beida Harriche": {
        "Coordinates": (36.39641384477348, 5.889624206216944),
        "Neighbors": [
            {"Tassadane Haddada": 18.9},
            {"Ferdjioua": 5.9},
            {"Bouhatem": 19.4},
            {"Beni Aziz": 33.6},
            {"Djemila": 22.0}
        ],
        "Willaya": "Mila"
    },
    "Sidi Merouane": {
        "Coordinates": (36.520743384675015, 6.27477899491999),
        "Neighbors": [
            {"Terrai Bainen": 34.7},
            {"Oued Endja": 31.3},
            {"Mila": 13.1},
            {"Grarem Gouga": 8.9},
            {"Settara": 48.0},
            {"Sidi Maarouf": 24.1}
        ],
        "Willaya": "Mila"
    },
    "Teleghma": {
        "Coordinates": (36.1165050415204, 6.342557930520938),
        "Neighbors": [
            {"Chelghoum Laid": 19.2},
            {"Tadjenanet": 38.6},
            {"Souk Naamane": 43.1},
            {"Ain Mlila": 22.3},
            {"El Khroub": 47.3}
        ],
        "Willaya": "Mila"
    },
    "Bouhatem": {
        "Coordinates": (36.301098493951976, 5.998056329155836),
        "Neighbors": [
            {"Ain Beida Harriche": 19.5},
            {"Ferdjioua": 16.6},
            {"Rouached": 32.8},
            {"Oued Endja": 45.0},
            {"Chelghoum Laid": 25.1},
            {"Bir El Arch": 27.9},
            {"Djemila": 33.8},
            {"Tadjenanet": 26.1}
        ],
        "Willaya": "Mila"
    },


    "Tadjenanet": {
        "Coordinates": (36.12714398378235, 5.985696710506715),
        "Neighbors": [{"Bouhatem" :26.2}, {"Chelghoum Laid" :19.7}, {"Teleghma" :38.6}, {"Bir El Arch": 14.0} , {"Hammam Souhna" :37.1}, {"Seriana" :61.8 },{ "Ain Djasser" :34.9}],
        "Willaya": "Mila"
    },

    #Setif
    "Beni Ourtilane": {
        "Coordinates": (36.443882618631655, 4.858046848064909),
        "Neighbors": [{"Bouandas" :40.5}, {"Hammam Guergour" :32.2},{ "Guenzet" :30.6}, {"Amizour" :52.5}, {"Beni Maouche": 24.4} , {"Djaafra" :49.2},{ "Bordj Zemoura" :43.9}],
        "Willaya": "Setif"
    },
    "Bouandas": {
        "Coordinates": (36.497371269667, 5.1042083838947185),
        "Neighbors": [{"Beni Ourtilane" :41.0} , {"Hammam Guergour": 41.8}, {"Maoklane" :28.2 }, {"Kherrata" :34.8}, {"Darguina" :34.8}, {"Aokas" :48.0}, {"Tichy" :45.5}, {"Barbacha" :25.2}],
        "Willaya": "Setif"
    },
    "Guenzet": {
        "Coordinates": (36.31926761834304, 4.836814324418948),
        "Neighbors": [{"Beni Ourtilane" :30.1}, {"Hammam Guergour" :28.0}, {"Djaafra" :34.4}, {"Bordj Zemoura" :13.3}, {"Bir Kasdali" :44.9} ],
        "Willaya": "Setif"
    },
    "Hammam Guergour": {
        "Coordinates": (36.32805218271321, 5.040806408101203),
        "Neighbors": [{"Beni Ourtilane" :32.2}, {"Bouandas" :30.3}, {"Guenzet" :28.0} , {"Maoklane" :13.0}, {"Bougaa" :5.2}, {"Bir Kasdali" :38.1}],
        "Willaya": "Setif"
    },
    "Maoklane": {
        "Coordinates": (36.39663818456605, 5.0749458742949285),
        "Neighbors": [{"Bouandas" :16.8} , {"Hammam Guergour" :13.0}, {"Bougaa" :15.2}, {"Kherrata" :33.6}],
        "Willaya": "Setif"
    },
    "Bougaa": {
        "Coordinates": (36.335921063165365, 5.096659598269766),
        "Neighbors": [{"Maoklane" :15.2}, {"Hammam Guergour" :5.2}, {"Ain Arnat" :39.7}, {"Kherrata" :41.6 }, {"Bir Kasdali" :32.9}, {"Ain Taghrout" :33.6}],
        "Willaya": "Setif"
    },
    "Ain Arnat": {
        "Coordinates": (36.17672928439793, 5.294021744025028),
        "Neighbors": [{"Bougaa" :39.6}, {"Amoucha" :31.6} , {"Ain El Kebira" :34.2}, {"Djemila" :63.2}, {"Setif" :9.8 }, {"Guidjel" :24.7} , {"Ain Oulmane" :37.2}, {"Kherrata" :47.4}, {"Bir Kasdali" :35.3},{ "Ain Taghrout" :30.7}],
        "Willaya": "Setif"
    },
    "Amoucha": {
        "Coordinates": (36.38343362097566, 5.4134398661292344),
        "Neighbors": [{"Ain Arnat" :30.9}, {"Babor" :82.6 }, {"Ain El Kebira" :13.3}, {"Djemila" :46.1}, {"Darguina" :36.5}, {"Kherrata" :25.1}],
        "Willaya": "Setif"
    },
    "Babor": {
        "Coordinates": (36.49526672419836, 5.533475336024416),
        "Neighbors": [{"Amoucha" :31.5}, {"Beni Aziz" :16.0}, {"Ain El Kebira" :20.6}, {"Darguina" :67.4}],
        "Willaya": "Setif"
    },
    "Beni Aziz": {
        "Coordinates": (36.46348668735427, 5.649858604298713),
        "Neighbors": [{"Babor" :16.0}, {"Ain El Kebira" :27.5}, {"Djemila" :35.2} , {"Tassadane Haddada" :48.7 }, {"Ain Beida Harriche" :33.6} ],
        "Willaya": "Setif"
    },
    "Ain El Kebira": {
        "Coordinates": (36.374050038289184, 5.568739715830615),
        "Neighbors": [{"Ain Arnat" :33.5}, {"Amoucha" :13.2}, {"Babor" :20.6}, {"Beni Aziz" :27.5} , {"Djemila" :38.5}],
        "Willaya": "Setif"
    },
    "Djemila": {
        "Coordinates": (36.3275501359257, 5.725164568831408),
        "Neighbors": [{"Beni Aziz" :37.2} , {"Ain El Kebira": 35.2}, {"Ain Arnat" :63.8}, {"Setif" :48.2}, {"Guidjel": 33.7}, {"El Eulma" :20.7}, {"Bir El Arch" :30.3}, {"Ain Beida Harriche" :22.0} , {"Bouhatem" :33.8}],
        "Willaya": "Setif"
    },
    "Setif": {
        "Coordinates": (36.18186550265154, 5.39583368729507),
        "Neighbors": [{"Ain Arnat" :9.7} , {"Djemila" :47.1} , {"Guidjel" :15.1}],
        "Willaya": "Setif"
    },
    "Guidjel": {
        "Coordinates": (36.11709985480307, 5.524794401526191),
        "Neighbors": [{"Djemila" :33.7 }, {"Setif":15.0 }, {"Ain Arnat" :24.8 }, {"Ain Oulmane" :34.1}, {"Ain Azel" :38.2}, {"El Eulma" :15.5} ],
        "Willaya": "Setif"
    },
    "El Eulma": {
        "Coordinates": (36.15259146728865, 5.675856419447651),
        "Neighbors": [{"Djemila" :20.7}, {"Bir El Arch" :14.7} , {"Setif" :25.8}, {"Guidjel" :15.5}, {"Ain Azel" :42.8 }, {"Hammam Souhna" :32.7}],
        "Willaya": "Setif"
    },
    "Bir El Arch": {
        "Coordinates": (36.12449496061512, 5.835737879907064),
        "Neighbors": [{"Djemila" :30.3}, {"Guidjel" :32.5} , {"Hammam Souhna" :43.0}, {"Bouhatem" :27.9}, {"Tadjenanet" :14.1 }],
        "Willaya": "Setif"
    },
    "Hammam Souhna": {
        "Coordinates": (35.9779362652413, 5.793165860847394),
        "Neighbors": [{"El Eulma" :28.5 }, {"Bir El Arch" :38.6}, {"Ain Azel": 45.8}, {"Tadjenanet" :37.6 }],
        "Willaya": "Setif"
    },
    "Ain Azel": {
        "Coordinates": (35.81440230083919, 5.4937884086145985),
        "Neighbors": [{"Hammam Souhna" :58.6}, {"El Eulma" :42.7} , {"Guidjel" :38.1}, {"Ain Oulmane" :26.8} ,{ "Salah Bey" :23.3} , {"Ras El Aioun" :23.5}, {"Ain Djasser" :65.2}],
        "Willaya": "Setif"
    },
    "Ain Oulmane": {
        "Coordinates": (35.91559646802633, 5.296093477458351),
        "Neighbors": [{"Ain Arnat" : 34.8}, {"Setif": 33.3}, {"Guidjel" :34.7},{ "Ain Azel" :26.8}, {"Salah Bey" : 8.0}, {"Ain Taghrout":40.2}],
        "Willaya": "Setif"
    },
    "Salah Bey": {
        "Coordinates": (35.84967327177129, 5.291004966162516),
        "Neighbors": [{"Ain Oulmane": 8.0}, {"Ain Azel" :23.3}, {"Ain Taghrout" :49.4 }, {"Bordj Ghedir" :58.8}, {"Ouled Derradj":68.3}, {"Magra" :40.1} , {"El Madher" :134}, {"Ras El Aioun" :46.9}],
        "Willaya": "Setif"
    },
    
"Beni Haoua": 
{
    "Coordinates": (36.52898995394597, 1.573059823030802),
    "Neighbors": [{"El Abadia":52 },{"Damous": 16.2},{"Tenes": 37.9}, {"Zeboudja": 42.1}],
    "Willaya" : "Chlef"
},

"Tenes": {
    "Coordinates": (36.520091395849185, 1.3335749058364381),
    "Neighbors": [{"Abou El Hassen": 19.3}, {"El Marsa": 281},{"Beni Haoua": 37.9}, {"Zeboudja": 34.4}],
    "Willaya" : "Chlef"
},

"Zeboudja": {
    "Coordinates": (36.382030119885606, 1.4149071749526012),
    "Neighbors": [{"El Abadia":56.4 },{"Tenes": 34.4}, {"Beni Haoua": 42.1},  {"Abou El Hassen": 32.8}, {"Ouled Fares":29.3}, {"Oued Fodda": 36.4}],
    "Willaya" : "Chlef"
},

"Abou El Hassen": {
    "Coordinates": (36.433244719209725, 1.1714178865535474),
    "Neighbors": [{"Tenes": 19.3}, {"Zeboudja": 32.8},{"Ouled Fares": 34}, {"Ain Merane": 48.4},{"El Marsa": 227}],
    "Willaya" : "Chlef"
},


"El Marsa": {
    "Coordinates": (36.84188745648639, 3.23805712959987523),
    "Neighbors": [{"Tenes": 201 }, {"Abou El Hassen": 287},{"Taougrite": 303 }, {"Ain Merane": 285 }],
    "Willaya" : "Chlef"
},


"Taougrite": {
    "Coordinates": (36.24580706725865, 0.9170579363176736),
    "Neighbors": [{"Achaacha": 38.8 }, {"Sidi M'Hamed Ben Ali": 16.9},{"El Marsa": 292 }, {"Ain Merane": 19.1}],
    "Willaya" : "Chlef"
},


"Oued Fodda": {
    "Coordinates": (36.18719966716232, 1.5320911623868831),
    "Neighbors": [{"El Abadia": 21 },{"El Attaf": 14.5 },{"Zeboudja": 36.2}, {"Ouled Fares": 33.5},{"Chlef": 21.1}, {"El Karimia": 11.4}],
    "Willaya" : "Chlef"
},


"Ouled Fares": {
    "Coordinates": (36.24038347412689, 1.2279153500840427),
    "Neighbors": [{"Zeboudja": 29.3}, {"Abou El Hassen": 34},{"Oued Fodda": 36.6 }, {"Ain Merane": 35.9},{"Chlef": 15.3}, {"Boukadir": 36.2}],
    "Willaya" : "Chlef"
},


"Ain Merane": {
    "Coordinates": (36.16602333455236, 0.9326620588308254),
    "Neighbors": [{"Mazouna": 12.8 }, {"Sidi M'Hamed Ben Ali": 15.2},{"El Marsa": 274}, {"Abou El Hassen": 48.4},{"Ouled Fares": 39.5 }, {"Boukadir": 26.7},{"Taougrite": 18.3}],
    "Willaya" : "Chlef"
},


"El Karimia": {
    "Coordinates": (36.11623171241601, 1.5630839398737384),
    "Neighbors": [{"Lazharia": 32.4 },{"Bathia": 89.6 },{"Rouina": 31.2},{"El Attaf": 19.5},{"Oued Fodda": 11.3}, {"Chlef": 25.2}],
    "Willaya" : "Chlef"
},


"Chlef": {
    "Coordinates": (36.12510621851637, 1.3123892325446098),
    "Neighbors": [{"Lazharia": 41.6},{"El Karimia": 25}, {"Oued Fodda": 21},{"Ouled Fares": 15.3 }, {"Boukadir": 28.5}, {"Ouled Ben Abdelkader": 25.7}],
    "Willaya" : "Chlef"
},

 "Boukadir": {
    "Coordinates": (36.05063666672219, 1.110184056212536),
    "Neighbors": [{"Mazouna": 52.6 }, {"Oued Rhiou": 29.5},{"Ammi Moussa": 34.3}, {"Ramka": 35.3 },{"Chlef": 28.2 }, {"Ouled Fares": 34.7},{"Ouled Ben Abdelkader": 22.2 }, {"Ain Merane": 26.7 }],
    "Willaya" : "Chlef"
},

"Ouled Ben Abdelkader": {
    "Coordinates": (36.00621206258997, 1.27665653605480123),
    "Neighbors": [{"Lardjem": 67.3 }, {"Ramka": 34.7},{"Lazharia": 41.9 },{"Chlef": 26.2}, {"Boukadir": 23}],
    "Willaya" : "Chlef"
},

 "El Kala": {
    "Coordinates": (36.90887575464112, 8.415261830701715),
    "Neighbors": [{"El Tarf": 20.7}, {"Bouteldja": 33.2},{"Ben Mehidi": 69}],
    "Willaya" : "El Tarf"
},

 "El Tarf": {
    "Coordinates": (36.79757479819536, 8.329347787049059),
    "Neighbors": [{"El Kala": 20.7}, {"Bouteldja": 11.9},{"Bouhadjar": 41.7}],
    "Willaya" : "El Tarf"
},

 "Bouteldja": {
    "Coordinates": (36.82607650581568, 8.2039575398732),
    "Neighbors": [{"El Kala": 33.2}, {"El Tarf": 11.9},{"Bouhadjar": 48.8},{"Ben Mehidi": 30.2},{"Besbes": 38.1}],
    "Willaya" : "El Tarf"
},

 "Bouhadjar": {
    "Coordinates": (36.5065328304601, 8.117930781079568),
    "Neighbors": [{"Bouchegouf": 44.9},{"Hammam N'Bails": 69.1}, {"Mechroha": 41.5},{"Ouled Driss": 25},{"Bouteldja": 48.8}, {"El Tarf": 41.7},{"Drean": 63.8},{"Besbes": 53.5}],
    "Willaya" : "El Tarf"
},

"Ben Mehidi": {
    "Coordinates": (36.78734852239529, 7.9354621389530315),
    "Neighbors": [{"El Bouni": 20.8}, {"El Hadjar": 17.7},{"El Kala": 69}, {"Bouteldja": 30.2},{"Besbes": 10.4}],
    "Willaya" : "El Tarf"
},



 "Besbes": {
    "Coordinates": (36.71933696349612, 7.819503906070062),
    "Neighbors": [{"Ben Mehidi": 10.4}, {"Bouteldja": 38.1},{"Drean": 10.3},{"Bouhadjar": 53.5}],
    "Willaya" : "El Tarf"
},

 "Drean": {
    "Coordinates": (36.68662171602383, 7.736318189362537),
    "Neighbors": [{"El Hadjar": 17},{"Ain Berda": 16.7},{"Bouchegouf": 30.2},{"Besbes": 10.3},{"Bouhadjar": 63.8}],
    "Willaya" : "El Tarf"
},


 
 "Dellys": {
    "Coordinates": (36.912665128963674, 3.9101823931797988),
    "Neighbors": [{"Tigzirt": 26.8},{"Baghlia": 17.3}],
    "Willaya" : "Boumerdes"
},

 "Baghlia": {
    "Coordinates": (36.84560174372779, 3.8772136231398986),
    "Neighbors": [{"Tigzirt": 37.1},{"Makouda": 35.2},{"Draa Ben Khedda": 19.1},{"Dellys": 17.3},{"Naciria": 10.2},{"Bordj Menaiel": 20.9}],
    "Willaya" : "Boumerdes"
},

    
 "Naciria": {
    "Coordinates": (36.725483161630606, 3.8222756406183707),
    "Neighbors": [{"Draa Ben Khedda": 15.6},{"Draa El Mizan": 46.3},{"Baghlia": 10.2},{"Bordj Menaiel": 11.2},{"Isser": 17.7}],
    "Willaya" : "Boumerdes"
},
        
 "Bordj Menaiel": {
    "Coordinates": (36.774282781449045, 3.734384227850571),
    "Neighbors": [{"Baghlia": 20.9},{"Naciria": 11.2},{"Isser": 6},{"Thenia": 16.1}],
    "Willaya" : "Boumerdes"
},


 "Thenia": {
    "Coordinates": (36.76433992750215, 3.553704575390609),
    "Neighbors": [{"Boumerdes": 11},{"Isser": 11.7},{"Bordj Menaiel":16.1},{"Boudouaou": 17.9}],
    "Willaya" : "Boumerdes"
},

    
 "Boumerdes": {
    "Coordinates": (36.74863510350736, 3.4350167823857283),
    "Neighbors": [{"Thenia": 11},{"Boudouaou": 13.1}],
    "Willaya" : "Boumerdes"
},



 "Boudouaou": {
    "Coordinates": (36.74817259970753, 3.428905981485161),
    "Neighbors": [{"Rouiba": 13.3},{"Lakhdaria":40.7},{"Kadiria": 60.5},{"Boumerdes": 13.1},{"Khemis El Khechna":21.4},{"Thenia": 17.9}],
    "Willaya" : "Boumerdes"
},


    
 "Khemis El Khechna": {
    "Coordinates":(36.639053791814256, 3.2968397270671015),
    "Neighbors": [{"Rouiba": 17.8},{"Dar El Beida": 19.5},{"Meftah": 10.5},{"Larbaa": 27.9},{"Lakhdaria": 39.7},{"Kadiria": 46.5},{"Boudouaou": 21.4},{"Djebabra": 15.7 }],
    "Willaya" : "Boumerdes"
},

 "Isser": {
    "Coordinates": (36.71313034526276, 3.6464919639786553),
    "Neighbors": [{"Bordj Menaiel": 6.3},{"Naciria": 17.9},{"Thenia": 11.7},{"Tizi Ghenif": 27.1}],
    "Willaya" : "Boumerdes"
},



 

 "Bordj Omar Driss": {
    "Coordinates": (28.096026232516813, 6.871165484194098),
    "Neighbors": [{"Debdeb": 530}, {"In Amenas": 448},{"Illizi": 686}, {"Hassi Massouad": 431},{"Tamanrasset": 1978}],
    "Willaya" : "Illizi"
},


 "Debdeb": {
    "Coordinates": (29.949686349143914, 9.42532063991489),
    "Neighbors": [{"Bordj Omar Driss": 530}, {"In Amenas": 224}, {"El Borma": 277}],
    "Willaya" : "Illizi"
},


 
 "In Amenas": {
    "Coordinates": (28.080200802117915, 9.585380775926303),
    "Neighbors": [{"Debdeb": 224}, {"Bordj Omar Driss": 448},{"Illizi": 244},{"Idles": 846 },{"Foggaret Ezzaouia": 846}],
    "Willaya" : "Illizi"
},


  "Illizi": {
    "Coordinates": (26.472528951185897, 8.17613868876719),
    "Neighbors": [{"In Amenas": 244}, {"Bordj Omar Driss": 686}, {"Tamanrasset": 820}, {"Djanet": 407},{"Idles": 603 }],
    "Willaya" : "Illizi"
},





 "Djanet": {
    "Coordinates": (24.54106246446664, 9.374500187919427),
    "Neighbors": [{"Illizi": 407},{"Idles": 470 },{"Tazrouk": 544 }],
    "Willaya" : "Illizi"
},
 "Tsabit": {
    "Coordinates": (28.340453709458394, -0.22877564368780984),
    "Neighbors": [{"Tabelbala": 717},{"Ouled Khoudir": 171},{"Adrar": 59.8},{"Aougrout": 77.2},{"Charouine": 96.4}, {"Fenoughil": 94.4}],
    "Willaya" : "Adrar"
},

 "Adrar": {
    "Coordinates": (27.84407360772675, -0.41227968146522365),
    "Neighbors": [{"Tsabit": 59.8}, {"Fenoughil": 33.5}],
    "Willaya" : "Adrar"
},

 "Fenoughil": {
    "Coordinates": (27.74031459102894, -0.32511920199999866),
    "Neighbors": [{"Adrar": 33.5}, {"Aoulef": 213}],
    "Willaya" : "Adrar"
},

 "Zaouiet Kounta": {
    "Coordinates": (27.235288200499856, -0.15032243437078716),
    "Neighbors": [{"Reggane": 68.8}, {"Aoulef": 169}],
    "Willaya" : "Adrar"
},

 "Reggane": {
    "Coordinates": (26.69026877671192, 0.2419337208956897),
    "Neighbors": [{"Tindouf": 1339},{"Tazrouk": 954},{"Bordj Badji Mokhtar": 632},{"In Ghar": 188},{"Zaouiet Kounta": 68.8}, {"Aoulef": 101},{"In Amguel": 783},{"Abalessa": 912 },{"Oum El Assel": 1338}],
    "Willaya" : "Adrar"
},

 "Aoulef": {
    "Coordinates": (27.128851160269146, 1.0108174085811945),
    "Neighbors": [{"In Ghar": 91.4},{"Fenoughil": 213}, {"Zaouiet Kounta": 169},{"Reggane": 101},{"In Salah": 151.0 }],
    "Willaya" : "Adrar"
},

 "Bordj Badji Mokhtar": {
    "Coordinates": (21.39456328180617, 0.7397672029471736),
    "Neighbors": [{"Tsabit": 213},{"Reggane": 632}],
    "Willaya" : "Adrar"
},
 
 "Timimoun": {
    "Coordinates": (29.33294679698365, 0.11757567263561662),
    "Neighbors": [{"El Meniaa": 360},{"Tinerkouk": 75}, {"Charouine": 63.1}, {"Aougrout": 69.1}],
    "Willaya" : "Timimoun"
},

 "Tinerkouk": {
    "Coordinates": (29.80829915451877, 0.7668934946519124),
    "Neighbors": [{"El Abiodh Sidi Cheikh": 429}, {"Brezina": 502}, {"El Meniaa": 390},{"Timimoun": 75}, {"Charouine": 173}],
    "Willaya" : "Timimoun"
},

 "Charouine": {
    "Coordinates": (29.012803753132747, -0.36025829699257306),
    "Neighbors": [{"Kerzaz": 169},{"Ouled Khoudir": 132},{"Tsabit": 96.4},{"Timimoun": 63.1}, {"Tinerkouk": 173}, {"Aougrout": 111}],
    "Willaya" : "Timimoun"
},

 "Aougrout": {
    "Coordinates": (28.68692396294338, 0.38048617140061736),
    "Neighbors": [{"Tsabit": 77},{"Fenoughil": 162},{"Aoulef": 376},{"In Saleh": 522},{"Tsabit": 77.2},{"Timimoun": 69.1}, {"Charouine": 111}],
    "Willaya" : "Timimoun"
}, 

 "Mansoura": {
    "Coordinates": (36.07937703402272, 4.452148963918167),
    "Neighbors": [{"M'Chedallah": 53.1},{"Bechloul": 60.4},{"Bordj Okhriss": 53.2},{"Medjana": 30.2},{"El Hamadia": 41.5}],
    "Willaya" : "Bordj Bou Arreridj"
},


 "El Hamadia": {
    "Coordinates": (35.9999957254213, 4.739454870163115),
    "Neighbors": [{"Hammam Dalaa": 49.9},{"Msila": 51.8},{"Ouled Derradj": 70.9},{"Magra": 75.3},{"Medjana": 27.8},{"Mansoura": 41.5},{"Bordj Bou Arreridj": 14},{"Bordj Ghedir": 27.2}],
    "Willaya" : "Bordj Bou Arreridj"
},




 "Bordj Ghedir": {
    "Coordinates": (35.89592253515999, 4.859390765386585),
    "Neighbors": [{"Ouled Derradj": 45.3},{"Magra": 48.4},{"Ras El Oued": 24},{"El Hamadia": 27.2},{"Bordj Bou Arreridj": 26.5},{"Bir Kasdali": 36.6}],
    "Willaya" : "Bordj Bou Arreridj"
},



 "Ras El Oued": {
    "Coordinates": (35.928858666355204, 5.039744141235669),
    "Neighbors": [{"Bordj Ghedir": 24},{"Ain Taghrout": 24.2},{"Bir Kasdali": 25.8}],
    "Willaya" : "Bordj Bou Arreridj"
},


 "Ain Taghrout": {
    "Coordinates": (36.14150666158315, 5.062692583550123),
    "Neighbors": [{"Bougaa": 33.5},{"Ain Arnat": 30.7},{"Ain Oulmane": 40},{"Salah Bey": 49.4},{"Ras El Oued": 24.2},{"Bir Kasdali": 5.3}],
    "Willaya" : "Bordj Bou Arreridj"
},


 "Medjana": {
    "Coordinates": (36.142077456428666, 4.675692323959127),
    "Neighbors": [{"El Hamadia": 27.8},{"Mansoura": 30.2},{"Bordj Bou Arreridj": 11.5},{"Bir Kasdali": 40.8},{"Djaafra": 32.2},{"Bordj Zemoura": 38.8}],
    "Willaya" : "Bordj Bou Arreridj"
},


 "Bordj Bou Arreridj": {
    "Coordinates": (36.071068672606856, 4.753279256419697),
    "Neighbors": [{"El Hamadia": 14},{"Medjana": 11.5},{"Bordj Ghedir": 26.5},{"Bir Kasdali": 28.7}],
    "Willaya" : "Bordj Bou Arreridj"
},


 "Bir Kasdali": {
    "Coordinates": (36.16868919781276, 5.012964672518539),
    "Neighbors": [{"Guenzet": 44.8},{"Hammam Guergour": 38.1},{"Bougaa": 32.9},{"Ain Arnat": 35.3},{"Ras El Oued": 25.8},{"Ain Taghrout": 5.3},{"Bordj Ghedir": 36.6},{"Bordj Bou Arreridj": 28.7},{"Bordj Zemoura": 31.7}],
    "Willaya" : "Bordj Bou Arreridj"
},


"Bordj Zemoura": {
    "Coordinates": (36.26575053870385, 4.863634976846086),
    "Neighbors": [{"Beni Ourtilane": 39},{"Guenzet": 13.3},{"Hammam Guergour": 39.6},{"Medjana": 38.8},{"Bir Kasdali": 31.7},{"Djaafra": 37.8}],
    "Willaya" : "Bordj Bou Arreridj"
},

"Djaafra": {
    "Coordinates": (36.29218815060777, 4.664637588786705),
    "Neighbors": [{"Ighil Ali": 40.2},{"Akbou": 45.5},{"Barbacha": 105},{"Beni Maouche": 62.3},{"Amizour": 87.9},{"Beni Ourtilane": 48.7},{"Guenzet": 34.3},{"Medjana": 32.2},{"Bordj Zemoura": 38.8}],
    "Willaya" : "Bordj Bou Arreridj"
},
 "Beni Ounif": {
    "Coordinates": (32.03917868689221, -1.3027963229073425),
    "Neighbors": [{"Kerzaz": 429}, {"El Ouata": 365},{"Beni Abbes": 339}, {"Igli": 262},{"Moghrar": 91.4}, {"El Abiodh Sidi Cheikh": 285},{"Taghit": 188}, {"Bechar": 108}, {"Mougheul": 124}],
    "Willaya" : "Bechar"
},

 "Taghit": {
    "Coordinates": (30.95386562294611, -2.186180887748678),
    "Neighbors": [{"Tabelbala": 422},{"Kerzaz": 234}, {"El Ouata": 170},{"Beni Abbes": 144}, {"Igli": 67.1},{"Beni Ounif": 188}, {"Bechar": 97.5},{"Abadla": 135}],
    "Willaya" : "Bechar"
},

 "Bechar": {
    "Coordinates": (31.645550533422533, -2.092778070201416),
    "Neighbors": [{"Beni Ounif": 108}, {"Taghit": 97.5}, {"Lahmar": 35.3}, {"Kenadsa": 22.8}, {"Mougheul": 49.6}],
    "Willaya" : "Bechar"
},

 "Lahmar": {
    "Coordinates": (32.018907038106505, -2.2898105099911166),
    "Neighbors": [{"Kenadasa": 57}, {"Bechar": 35.3}, {"Mougheul": 14.9}, {"Boukais": 23.3}],
    "Willaya" : "Bechar"
},

 "Mougheul": {
    "Coordinates": (32.09339682359487, -2.2954745599911157),
    "Neighbors": [{"Beni Ounif": 124}, {"Bechar": 49.6},{"Lahmar": 14.9}, {"Boukais": 38}],
    "Willaya" : "Bechar"
},

 "Boukais": {
    "Coordinates": (32.056159511681344, -2.5263804398333796),
    "Neighbors": [{"Mougheul": 38},  {"Lahmar": 23.3},{"Kenadsa": 77.4}],
    "Willaya" : "Bechar"
},

 "Kenadsa": {
    "Coordinates": (31.502722104150088, -2.461300108624906),
    "Neighbors": [{"Abadla": 106},  {"Lahmar": 57},{"Boukais": 77.4},{"Meridja": 55.6}],
    "Willaya" : "Bechar"
},

 "Meridja": {
    "Coordinates": (31.470276403059252, -3.0732509384386373),
    "Neighbors": [{"Abadla":162},  {"Erg Ferradj": 170},{"Kenadasa": 55.6}],
    "Willaya" : "Bechar"
},

 "Abadla": {
    "Coordinates": (31.029679966967276, -2.753768136285508),
    "Neighbors": [{"Tabelbala": 287},{"Kerzaz": 239}, {"El Ouata": 175},{"Beni Abbes": 149}, {"Igli": 133},{"Taghit": 135},  {"Meridja": 162},{"Kenadasa": 59.8},{"Mechraa Houari Boumedienne": 11.8},{"Erg Ferradj": 8.8},{"Tindouf": 540 }],
    "Willaya" : "Bechar"
},

 "Erg Ferradj": {
    "Coordinates": (31.070043621317076, -2.9536200176442797),
    "Neighbors": [ {"Meridja": 170},{"Mechraa Houari Boumedienne": 15.2},{"Abadla": 8.8}],
    "Willaya" : "Bechar"
},

 "Mechraa Houari Boumedienne": {
    "Coordinates": (30.88049150384428, -2.726649115388401),
    "Neighbors": [{"Tabelbala": 287},{"Kerzaz": 227}, {"El Ouata": 163},{"Beni Abbes": 137}, {"Igli": 121},{"Abadla": 11.8},{"Erg Ferradj": 15.2}],
    "Willaya" : "Bechar"
},


 "Zeribet El Oued": {
    "Coordinates": (34.69213720484508, 6.4793295043760715),
    "Neighbors": [{"Reguiba": 218},{"Babar": 97.7},{"Chechar": 77.8},{"T'kout": 82.6},{"Sidi Okba": 56.6}, {"M'Chouneche": 90.3}],
    "Willaya" : "Biskra"
},


 "M'Chouneche": {
    "Coordinates": (34.9091676293986, 5.929100381890084),
    "Neighbors": [{"T'kout": 47.2}, {"Menaa": 89.8},{"Sidi Okba": 33.7}, {"Zeribet El Oued": 90.3}, {"Djemorah":67}],
    "Willaya" : "Biskra"
},

    
 "Sidi Okba": {
    "Coordinates": (34.75534546041836, 5.917090163408676),
    "Neighbors": [{"Reguiba": 189},{"M'Chouneche": 33.7}, {"Zeribet El Oued": 56.6}, {"Djemorah": 59.3}, {"Biskra": 22}, {"Ourlal": 51.9}],
    "Willaya" : "Biskra"
},


"Djemorah": {
    "Coordinates": (35.07939375913884, 5.8279980831697715),
    "Neighbors": [{"M'Chouneche": 67}, {"El Kantara": 46.2}, {"El Outaya": 40.3}, {"Biskra": 38.9}, {"Sidi Okba": 60.2}],
    "Willaya": "Biskra"
},

"El Kantara": {
    "Coordinates": (35.22122444912463, 5.710913609219962),
    "Neighbors": [{"Seggana": 45.7}, {"Barika": 53.8}, {"Ain Touta": 29.9}, {"Menaa": 68.9}, {"Djemorah": 46.2}, {"El Outaya": 26}],
    "Willaya": "Biskra"
},

"El Outaya": {
    "Coordinates": (35.0391837498973, 5.575198724796684),
    "Neighbors": [{"Barika": 60.3}, {"Djemorah": 40.3}, {"El Kantara": 26}, {"Tolga": 43.9}, {"Biskra": 25.4}],
    "Willaya": "Biskra"
},

"Biskra": {
    "Coordinates": (34.8590826194841, 5.718020982125815),
    "Neighbors": [{"Djemorah": 38.9}, {"Sidi Okba": 22}, {"Tolga": 36.9}, {"El Outaya": 25.4}, {"Ourlal": 40.9}],
    "Willaya": "Biskra"
},

"Ourlal": {
    "Coordinates": (34.69264797667978, 5.517199399236361),
    "Neighbors": [{"Ouled Djellal": 53.8}, {"El M'Ghair": 117}, {"Biskra": 40.9}, {"Sidi Okba": 51.4}, {"Tolga": 17.2}, {"Foughala": 23.9}],
    "Willaya": "Biskra"
},

"Tolga": {
    "Coordinates": (34.72877267450675, 5.366374941907242),
    "Neighbors": [{"Barika": 104}, {"Ben Srour": 91.2}, {"Biskra": 36.9}, {"Ourlal": 17.2}, {"El Outaya": 43.9}, {"Foughala": 4.7}],
    "Willaya": "Biskra"
},

"Foughala": {
    "Coordinates": (34.737801383444676, 5.329768614420376),
    "Neighbors": [{"Ouled Djellal": 52.3}, {"Ourial": 23.9}, {"Tolga": 4.7}],
    "Willaya": "Biskra"
},

 

 "Darguina": {
    "Coordinates": (36.55354990644341, 5.289410599123713),
    "Neighbors": [{"Amoucha": 36.6},{"Babor": 67.5}, {"Ziama Mansouriah": 27.6},{"Bouandas": 40.3},{"Aokas": 22.3}, {"Souk El Tenine": 12},{"Kherrata": 11.9}],
    "Willaya" : "Bejaia"
},

"Souk El Tenine": {
    "Coordinates": (36.64610623713425, 5.333361970718581),
    "Neighbors": [ {"Babor": 67}, {"Ziama Mansouriah": 16.4},{"Darguina": 12},{"Aokas": 10.3}],
    "Willaya" : "Bejaia"
},


"Kherrata": {
    "Coordinates": (36.50161786730233, 5.267738392165238),
    "Neighbors": [ {"Bougaa":41}, {"Ain Arnat": 47.3},{"Amoucha": 25.1},{"Bouandas": 9.2},{"Maoklane": 33.6},{"Darguina": 11.9}],
    "Willaya" : "Bejaia"
},


"Aokas": {
    "Coordinates": (36.663774211269306, 5.2331882452352945),
    "Neighbors": [ {"Bouandas": 48.1},{"Souk El Tenine": 10.3},{"Darguina": 22.3},{"Tichy": 9.2}],
    "Willaya" : "Bejaia"
},


"Tichy": {
    "Coordinates": (36.68385619851103, 5.128738442649395),
    "Neighbors": [{"Bouandas": 45.3}, {"Aokas": 9.2},{"Barbacha": 47.4}
    ,{"Amizour": 34.7},{"Bejaia": 24.2}],
    "Willaya" : "Bejaia"
},

"Bejaia": {
    "Coordinates": (36.79852983324341, 5.0238663196247),
    "Neighbors": [ {"Tichy": 24.2},{"El Kseur": 29.4},{"Amizour": 23.9}],
    "Willaya" : "Bejaia"
},


"Amizour": {
    "Coordinates": (36.6560381323528, 4.901894054268516),
    "Neighbors": [ {"Beni Ourtilane": 53},{"Bouandas": 41.8},{"Bejaia": 23.9},{"El Kseur": 15},{"Barbacha": 16.7},{"Seddouk": 37.8},{"Beni Maouche": 41.2}],
    "Willaya" : "Bejaia"
},

    
"Barbacha": {
    "Coordinates": (36.58608987184367, 4.977025361831615),
    "Neighbors": [{"Beni Ourtilane": 36.8},{"Bouandas": 25.2}, {"Tichy": 47.4},{"Amizour": 16.7}],
    "Willaya" : "Bejaia"
},


"El Kseur": {
    "Coordinates": (36.71998545281109, 4.82610560844716),
    "Neighbors": [ {"Bejaia": 29.4},{"Adekar": 27.2},{"Amizour": 15},{"Sidi Aich": 24.2}],
    "Willaya" : "Bejaia"
},



"Adekar": {
    "Coordinates": (36.73258568833086, 4.66130970770405),
    "Neighbors": [ {"Bouzeguene": 54.1},{"Azeffoun": 65.7},{"Azazga": 42.2}, {"El Kseur": 27.2},{"Chemini": 31.3},{"Sidi Aich": 24.6}],
    "Willaya" : "Bejaia"
},



"Beni Maouche": {
    "Coordinates": (36.494752068197435, 4.7955748851283415),
    "Neighbors": [ {"Beni Ourtilane": 24.9},{"Bouandas": 47},{"Seddouk": 19.4},{"Amizour": 41.2}],
    "Willaya" : "Bejaia"
},


"Seddouk": {
    "Coordinates": (36.543578333844295, 4.714843769004549),
    "Neighbors": [ {"Djaafra": 78},{"Akbou": 20},{"Amizour":37.8},{"Beni Maouche": 19.4},{"Sidi Aich": 13.3},{"Chemini": 17.7},{"Ighil Ali": 39.5}],
    "Willaya" : "Bejaia"
},

    
"Chemini": {
    "Coordinates": (36.59989348206008, 4.579339240696224),
    "Neighbors": [ {"Bouzeguene": 22.8},{"Sidi Aich": 13.3},{"Adekkar": 31.3},{"Seddouk": 17.7},{"Akbou": 22.8}],
    "Willaya" : "Bejaia"
},

        
"Sidi Aich": {
    "Coordinates": (36.635190745726106, 4.684464557093519),
    "Neighbors": [ {"Adekar": 24.7},{"El Kseur": 24.2},{"Seddouk": 13.3},{"Chemini": 13.3}],
    "Willaya" : "Bejaia"
},


"Akbou": {
    "Coordinates": (36.48299857114762, 4.541848766618213),
    "Neighbors": [{"Djaafra": 45.5},{"Bouzeguene": 37.2}, {"Tazmalt": 16.8},{"Ighil Ali": 22.6},{"Seddouk": 20},{"Chemini": 22.8}],
    "Willaya" : "Bejaia"
},

"Tazmalt": {
    "Coordinates": (36.386990720580805, 4.368548000868408),
    "Neighbors": [{"Bouzeguene": 65.7},{"Iferhounene": 37.3},{"M'Chedallah": 14.6}, {"Akbou": 16.8},{"Ighil Ali": 18.8}],
    "Willaya" : "Bejaia"
},


"Ighil Ali": {
    "Coordinates": (36.3373094102197, 4.4826672277386495),
    "Neighbors": [ {"Mansoura": 56},{"Medjana": 45.9},{"Djaafra": 40.2},{"Akbou": 22.6},{"Tazmalt": 18.8},{"Seddouk": 39.5}],
    "Willaya" : "Bejaia"
},

 
 "Djezzar": {
    "Coordinates": (35.49307710539402, 5.2635527963418465),
    "Neighbors": [{"Khoubana": 97.5},{"Ouled Derradj": 74.1},{"Magra": 24.5},{"Salah Bey": 62.2},{"Ras El Aioun": 55.2}, {"N'Gaous": 53.4},{"Seggana": 49.9},{"Barika": 29.7}],
    "Willaya" : "Batna"
},

"Barika": {
    "Coordinates": (35.37670915609646, 5.315114646341841),
    "Neighbors": [{"Djezzar": 29.7},{"Ben Srour": 94.2},{"Tolga": 104},{"El Outaya": 60.1},{"El Kantara": 53.8},{"Seggana": 19.2},{"Ras El Aioun": 47.1}],
    "Willaya" : "Batna"
},


"Seggana": {
    "Coordinates": (35.37223010801385, 5.546488131157826),
    "Neighbors": [{"El Kantara": 45.7},{"Barika": 19.3},{"N'Gaous": 28},{"Djezzar": 40.5},{"Ain Touta": 33.2}],
    "Willaya" : "Batna"
},



  "N'Gaous": {
    "Coordinates": (35.56501912980223, 5.613019173281498),
    "Neighbors": [{"Ras El Aioun": 16.3},{"Seggana": 33.2},{"Djezzar": 49.1},{"Ain Touta": 40.5},{"Ouled Si Slimane": 6.9}],
    "Willaya" : "Batna"
},


"Ras El Aioun": {
    "Coordinates": (35.66772748358402, 5.655273378255213),
    "Neighbors": [{"Salah Bey": 47},{"Ain Azel": 23.5},{"Hammam Souhna": 53.8},{"N'Gaous": 16.3},{"Djezzar": 55.4},{"Merouana": 25.4},{"Ain Djasser": 55.2},{"Ouled Si Slimane": 9.4}],
    "Willaya" : "Batna"
},


"Ouled Si Slimane": {
    "Coordinates": (35.61862255259336, 5.6407827145117935),
    "Neighbors": [{"N'Gaous": 6.9},{"Ras El Aioun": 9.4},{"Merouana": 30},{"Ain Touta": 47.1}],
    "Willaya" : "Batna"
},


"Ain Touta": {
    "Coordinates": (35.38125099414251, 5.892378475721671),
    "Neighbors": [{"El Kantara": 32.7},{"N'Gaous": 44.7},{"Ouled Si Slimane": 51.3},{"Merouana": 47.5},{"Seggana": 35.8},{"Batna": 31.6},{"Tazoult": 42.7},{"Teniet El Abed": 66.6},{"Bouzina": 47.6}],
    "Willaya" : "Batna"
},


"Ain Djasser": {
    "Coordinates": (35.85716730114614, 6.001540154301472),
    "Neighbors": [{"Tadjenanet": 35.2},{"Hammam Souhna": 22.5},{"Ras El Aioun": 55},{"Seriana": 27.9},{"Merouana": 33.9}],
    "Willaya" : "Batna"
},


"Merouana": {
    "Coordinates": (35.638714580926155, 5.908614762482335),
    "Neighbors": [{"Ras El Aioun": 25.4},{"Seriana": 31.4},{"Ain Djasser": 34.2},{"Ouled Si Slimane": 30},{"Ain Touta": 46.5},{"Batna": 42.4}],
    "Willaya" : "Batna"
},


"Seriana": {
    "Coordinates": (35.70487493540093, 6.189285936666549),
    "Neighbors": [{"Souk Naamane": 39.2},{"Tadjenanet": 61.8},{"Merouana": 31.2},{"El Madher": 21.7},{"Ain Djasser": 27.7},{"Batna": 33.3}],
    "Willaya" : "Batna"
},


"Batna": {
    "Coordinates": (35.54710148324673, 6.159462390124612),
    "Neighbors": [{"Tazoult": 14.4},{"Ain Touta": 32},{"Merouana": 42.3},{"El Madher": 25.4},{"Seriana": 33.4}],
    "Willaya" : "Batna"
},


"El Madher": {
    "Coordinates": (35.63088502724228, 6.3681296003771723),
    "Neighbors": [{"Souk Naamane": 52.1},{"Tazoult": 34.6},{"Batna": 25.3},{"Seriana": 21.7},{"Chemora": 30.4},{"Timgad": 57.6}],
    "Willaya" : "Batna"
},


"Tazoult": {
    "Coordinates": (35.48454672616024, 6.253429188528607),
    "Neighbors": [{"Teniet El Abed": 48.5},{"Batna": 14.3},{"Ain Touta": 53.1},{"El Madher": 34.4},{"Timgad": 23.9}],
    "Willaya" : "Batna"
},


"Bouzina": {
    "Coordinates": (35.27761049441365, 6.115781308910318),
    "Neighbors": [{"El Kantara": 73.6},{"Teniet El Abed": 19.4},{"Tazoult": 66.4},{"Ain Touta": 47.5},{"Menaa": 17.9}],
    "Willaya" : "Batna"
},


"Menaa": {
    "Coordinates": (35.178124827906075, 5.998355038449387),
    "Neighbors": [{"El Kantara": 68.9},{"Djemorah": 22.7},{"M'Chouneche": 90.8},{"Teniet El Abed": 21.7},{"Bouzina": 17.9},{"Arris": 44.4},{"T'kout": 80.2}],
    "Willaya" : "Batna"
},


"T'kout": {
    "Coordinates": (35.13011312552, 6.325627340172185),
    "Neighbors": [{"Bouhmama": 73.2},{"M'Chouneche": 47.2},{"Zeribet El Oued": 82.9},{"Menaa": 80.2},{"Ichmoul": 56},{"Arris": 36}],
    "Willaya" : "Batna"
},


"Arris": {
    "Coordinates": (35.258524380507296, 6.324695031200676),
    "Neighbors": [{"Teniet El Abed": 24.3},{"Menaa": 44.4},{"Ichmoul": 22},{"T'kout": 36}],
    "Willaya" : "Batna"
},


"Teniet El Abed": {
    "Coordinates": (35.246083146653085, 6.180144040141718),
    "Neighbors": [{"Bouzina": 19.4},{"Menaa": 21.7},{"Ichmoul": 46.2},{"Arris": 24.3},{"Tazoult": 48.5},{"Timgad": 53.4}],
    "Willaya" : "Batna"
},


"Ichmoul": {
    "Coordinates": (35.30956830508852, 6.463517522506839),
    "Neighbors": [{"Bouhmama": 30.5},{"T'kout": 56.1},{"Arris": 21.9},{"Teniet El Abed": 46.2},{"Timgad": 47.2}],
    "Willaya" : "Batna"
},


"Timgad": {
    "Coordinates": (35.50020045707722, 6.468446545268877),
    "Neighbors": [{"Bouhmama": 51.5},{"Kais": 45.4},{"Ichmoul": 47.2},{"Teniet El Abed": 53.4},{"Tazoult": 24.3},{"El Madher":57.7},{"Chemora": 27.3}],
    "Willaya" : "Batna"
},


"Chemora": {
    "Coordinates": (35.67282112203969, 6.631995834688343),
    "Neighbors": [{"Kais": 39.3},{"Ain Fakroun": 47.6},{"Ain Kercha": 31.9},{"Souk Naamane": 69.6},{"Tazoult": 48.6},{"El Madher": 30.4},{"Timgad": 27.3}],
    "Willaya" : "Batna"
},




  "Gueltet Sidi Saad": {
    "Coordinates": (34.277103124658254, 1.9531419133306727),
    "Neighbors": [{"Ain Deheb": 73.5},{"Sougueur": 114},{"Charef": 107},{"Boualem": 103},{"Rogassa": 112},{"Aflou": 26.9}, {"Brida": 64.9},{"Ain Madhi": 99.5}],
    "Willaya" : "Laghouat"
},

"Aflou": {
    "Coordinates": (34.159062749305754, 2.194434004520605),
    "Neighbors": [ {"Gueltet Sidi Saad": 26.9},{"Brida": 38.4}
    ,{"Ain Madhi":73.1},{"El Ghicha": 37.3},{"Oued Morra": 26.2}],
    "Willaya" : "Laghouat"
},


"Brida": {
    "Coordinates": (33.999501723928454, 1.7968019160612576),
    "Neighbors": [ {"Boualem": 37.9},{"Gueltet Sidi Saad": 64.9},{"Aflou": 38.4},{"Ain Madhi": 95.8},{"El Ghicha": 60.1}],
    "Willaya" : "Laghouat"
},


"Oued Morra": {
    "Coordinates": (34.18505196984349, 2.3001716907948206),
    "Neighbors": [ {"Aflou": 26.2},{"Ain Madhi": 90.8},{"El Ghicha": 65}],
    "Willaya" : "Laghouat"
},


"El Ghicha": {
    "Coordinates": (33.93286934250902, 2.157939972615198),
    "Neighbors": [ {"Aflou": 37.3},{"Ain Madhi": 35.7},{"Brida": 60},{"Oued Morra": 64.9}],
    "Willaya" : "Laghouat"
},

"Ain Madhi": {
    "Coordinates": (33.81728231456553, 2.188175684061199),
    "Neighbors": [ {"Metlili": 297},{"Brezina": 241},{"Boualem": 134}, {"Charef": 135},{"El Idrissia": 104},{"Gueltet Sidi Saad": 99.5},{"Brida": 95.8},{"Aflou": 73.1},{"El Ghicha": 35.7},{"Oued Morra": 90.8},{"Sidi Makhlouf": 96.8},{"Laghouat": 70.4},{"Ksar El Hirane": 94.8},{"Hassi R'Mel": 190}],
    "Willaya" : "Laghouat"
},


"Sidi Makhlouf": {
    "Coordinates": (34.234019881192495, 2.983179314082189),
    "Neighbors":  [ {"El Idrissia": 79.8},{"Ain El Ibel": 40},{"Messaad": 57.7},{"Ain Madhi": 96.8},{"Laghouat": 41.4}],
    "Willaya" : "Laghouat"
},

"Laghouat": {
    "Coordinates": (33.80071509266779, 2.895023253345238),
    "Neighbors":  [ {"Sidi Makhlouf": 41.4},{"Ain Madhi": 70.4},{"Ksar El Hirane": 12}],
    "Willaya" : "Laghouat"
},



"Ksar El Hirane": {
    "Coordinates": (33.81875296194071, 3.1464682719066563),
    "Neighbors": [{"Messaad": 66.3},{"Sidi Makhlouf": 12},{"Ain Madhi": 10.3},{"Laghouat": 30.8},{"Hassi R'Mel": 137}],
    "Willaya" : "Laghouat"
},



"Hassi R'Mel": {
    "Coordinates": (32.918810616169566, 3.1726830061645788),
    "Neighbors": [{"Guerrara": 155},{"Berriane": 83.1},{"Daia Ben Dahoua": 122},{"Messaad": 191},{"Ain Madhi": 190},{"Ksar El Hirane": 137}],
    "Willaya" : "Laghouat"
},


 
 "Meskiana": {
    "Coordinates": (35.64359663641165, 7.670478998330736),
    "Neighbors": [{"Bir Mokkadem": 51.2},{"Morsott": 34.1},{"El Aouinet": 36.8},{"Dhalaa": 23.3}, {"Ain Beida": 36.7}],
    "Willaya" : "Oum El Bouaghi"
},


 
 "Dhalaa": {
    "Coordinates": (35.45937785346298, 7.547204374862414),
    "Neighbors": [{"Bir Mokkadem": 27.9},{"Ain Touila": 46.3},{"Meskiana": 36.7}, {"Ain Beida": 60}, {"Fkirina": 46.2}],
    "Willaya" : "Oum El Bouaghi"
},


 "Ain Beida": {
    "Coordinates": (35.791030914446125, 7.345748663070484),
    "Neighbors": [{"Bir Bou Haouch": 32.4},{"Oum El Adhaim ": 51.1},{"Meskiana": 36.7}, {"Dhalaa": 60}, {"Fkirina": 17.2},{"Ksar Sbahi": 36.2}, {"Ain Babouche": 32.5}, {"Oum El Bouaghi": 27.6}],
    "Willaya" : "Oum El Bouaghi"
},


 "Fkirina": {
    "Coordinates": (35.66722912146684, 7.301427967708381),
    "Neighbors": [{"Ain Touila": 35.6},{"Ain Beida": 17.2}, {"Dhalaa": 46.2}, {"Oum El Bouaghi": 37.1}],
    "Willaya" : "Oum El Bouaghi"
},

 "Ksar Sbahi": {
    "Coordinates": (36.08075017310709, 7.252201285596572),
    "Neighbors": [{"Bir Bou Haouch": 21.4}, {"Sedrata": 35.7},{"Ain Makhlouf": 27.1}, {"Ain Beida": 36.2}, {"Ain Babouche": 20.4}],
    "Willaya" : "Oum El Bouaghi"
},

 "Ain Babouche": {
    "Coordinates": (35.95330196432428, 7.1814117097795425),
    "Neighbors": [{"Ain Makhlouf": 50},{"Ain Beida": 32.5}, {"Ksar Sbahi": 20.4},{"Oum El Bouaghi": 12.3}, {"Ain Fakroun": 35.4}, {"Sigus": 55.5}],
    "Willaya" : "Oum El Bouaghi"
},


 "Oum El Bouaghi": {
    "Coordinates": (35.87244110957285, 7.1124971644222073),
    "Neighbors": [{"Kais": 52.3},{"El Hamma": 53.1},{"Ain Touila": 67.9},{"Ain Beida": 27.6}, {"Ain Babouche": 12.3},{"Fkirina": 36.4}, {"Ain Fakroun": 25.4}, {"Sigus": 45.6}],
    "Willaya" : "Oum El Bouaghi"
},


 "Sigus": {
    "Coordinates": (36.13256658446823, 6.801302082883304),
    "Neighbors": [{"Ain Makhlouf": 61.4},{"Ain Abid": 34.2},{"El Khroub": 20.7},{"Ain Mlila": 25.9}, {"Ain Babouche": 55.5},{"Ain Kercha": 36.9}, {"Ain Fakroun": 23.6}],
    "Willaya" : "Oum El Bouaghi"
},


 "Ain Fakroun": {
    "Coordinates": (35.96842926742834, 6.854949404130079),
    "Neighbors": [{"Chemora": 48.9},{"Oum El Bouaghi": 25.4}, {"Ain Babouche": 35.4},{"Ain Kercha": 16.4}, {"Sigus": 23.6}],
    "Willaya" : "Oum El Bouaghi"
},


 "Ain Mlila": {
    "Coordinates": (36.0397602924083, 6.575134765256122),
    "Neighbors": [{"El Khroub": 32.7},{"Teleghma": 22.3},{"Souk Naamane": 27.9}, {"Ain Kercha": 18.4}, {"Sigus": 25.9}],
    "Willaya" : "Oum El Bouaghi"
},

 "Ain Kercha": {
    "Coordinates": (35.92654301509272, 6.701601989030212),
    "Neighbors": [{"El Madher": 54.3},{"Chemora": 31.9},{"Souk Naamane": 33.5}, {"Ain Mlila": 18.4}, {"Sigus": 36.9}, {"Ain Fakroun": 16.4}],
    "Willaya" : "Oum El Bouaghi"
},


 "Souk Naamane": {
    "Coordinates": (35.90090110114669, 6.387254293406816),
    "Neighbors": [{"Teleghma": 44.2},{"Tadjenanet": 57.8},{"Seriana": 39.3},{"El Madher": 53.4},{"Chemora": 69.6},{"Ain Kercha": 33.5}, {"Ain Mlila": 27.9}],
    "Willaya" : "Oum El Bouaghi"
},

   
   
    "Zighoud Youcef" : {
        "Coordinates" : (36.53232959731541, 6.708359274280542),
        "Neighbors" : [{"Ibn Ziad" : 28.2},{"Hamma Bouziane" : 14.2}, {"Constantine": 1.5 }, {"Ain Abid" : 41.2},{"El Harrouch": 54.1},{"Grarem Gouga": 50.6}],
        "Wilaya":"Constantine"
    },
     "Ibn Ziad" : {
        "Coordinates" : (36.53232959731541, 6.708359274280542),
        "Neighbors" : [{"El Khroub" :40.8},{"Hamma Bouziane" :18.0 }, {"Constantine":28.2 }, {"Zighoud Youcef" : 35.6},{"Grarem Gouga":52.6},{"Mila":30.8},{"Chelghoum Laid":49.9}],
        "Wilaya":"Constantine"
    },
      "Hamma Bouziane" : {
        "Coordinates" : (36.53232959731541, 6.708359274280542),
        "Neighbors" : [{"Ibn Ziad" : 17.9}, {"Constantine":13.5 }, {"Zighoud Youcef" :19.1}],
        "Wilaya":"Constantine"
    },
     "Constantine" : {
        "Coordinates" : (36.53232959731541, 6.708359274280542),
        "Neighbors" : [{"Ibn Ziad" : 30.9}, {"El Khroub":21.6 }, {"Ain Abid" :39.9},{"Hamma Bouziane":14.4}],
        "Wilaya":"Constantine"
    },
      "El Khroub" : {
        "Coordinates" : (36.53232959731541, 6.708359274280542),
        "Neighbors" : [{"Ibn Ziad" :45.8 }, {"Constantine": 15.6}, {"Ain Abid" :25.8},{"Ain Mlila": 33.6},{"Sigus":21.4},{"Chelghoum Laid": 66.1},{"Teleghma":46.6}],
        "Wilaya":"Constantine"
    },
      "Ain Abid" : {
        "Coordinates" : (36.53232959731541, 6.708359274280542),
        "Neighbors" : [{"El Khroub" : 25.8 }, {"Constantine": 40.5}, {"Zighoud Youcef" :82.8},{"Oued Zenati":24.5},{"Ain Makhlouf":39.2},{"El Harrouch":100},{"Sigus":34.3}],
        "Wilaya":"Constantine"
    },
    

    #medea = tissemsilt, ain defla ,blida,bouira , Msila, djelfa , tiaret
    "Chahbounia" : {
        "Coordinates" :(35.530552874110775, 2.60593299213237),
        "Neighbors":[{"Aziz":73},{"Ksar Boukhari":53.7},{"Sidi Ladjel":13.5},{"Khemisti":171},{"Theniet El Had": 87.1},{"Bordj El Emir Abdelkader":79.3},{"Ain Romana":37.2}],
        "Wilaya": "Medea"
    },
    "Aziz" : {
        "Coordinates" :(35.82396996259972, 2.464458396934665),
        "Neighbors":[{"Chahbounia":63.9},{"Ksar Boukhari":33.2},{"Ouled Antar":52.8},{"Khemisti": 151},{"Bordj El Emir Abdelkader":21},{"Bordj Emir Khaled":66.2},{"Ain Lechiekh":83.2}],
        "Wilaya": "Medea"
    },
    "Ksar Boukhari" : {
        "Coordinates" :(35.89227858659034, 2.741387391789747),
        "Neighbors":[{"Chahbounia":50.8},{"Aziz":32.2},{"Ouled Antar": 22.8},{"Seghouane":25.1},{"Ain Boucif":55.4},{"Birine":64.5},{"Ain Oussara":57.8}],
        "Wilaya": "Medea"
    },
      "Ain Boucif" : {
        "Coordinates" :(35.88987683283685, 3.1497784612214152),
        "Neighbors":[{"Ksar Boukhari": 55.6},{"Berrouaghia":49.3},{"Souagui":38.7},{"Seghouane": 32.2},{"Chellalet El Adhaoura": 26.6},{"Sour El Ghozlane":86.7},{"Birine":30.6},{"Ain Oussara":87}],
        "Wilaya": "Medea"
    },
    "Chellalet El Adhaoura" : {
        "Coordinates" :(35.94144263041228, 3.3990933053832926),
        "Neighbors":[{"Ain Boucif": 26.6 },{"Souagui":30.5},{"Sour El Ghozlane":60.9},{"Adekar":214}],
        "Wilaya": "Medea"
    },
    "Ouled Antar" : {
        "Coordinates":(35.949841661187584, 2.5984113780306672),
        "Neighbors":[{"Aziz":53.0},{"Ksar Boukhari": 22.7},{"Seghouane": 41.4}, { "Si Mahdjoub":87.0},{"Ain Lechiekh":93.8},{"Djendel":90.3}],
        "Wilaya": "Medea"
    },
    "Seghouane" : {
        "Coordinates":(36.00513743705529, 2.8989801722298827),
        "Neighbors":[{"Ouled Antar": 40.3},{"Ksar Boukhari": 25.2},{"Berrouaghia": 17.6}, { "Si Mahdjoub": 45.5},{"Ain Boucif": 32.1}],
        "Wilaya": "Medea"
    },
   "Berrouaghia" : {
        "Coordinates":(36.1416126328555, 2.9107106134942518),
        "Neighbors":[{"Seghouane": 17.6}, { "Ouzera":17.0},{"El Omaria": 22.9},{"Sidi Naamane": 24.4}, {"Souagui": 37.1},{"Ain Boucif":49.2}],
        "Wilaya": "Medea"
    },
     "Souagui" : {
        "Coordinates":(36.1265846266654, 3.266470622750958),
        "Neighbors":[{"Berrouaghia":43.0}, { "Sidi Naamane": 29.0},{"Beni Slimane": 24.3},{"El Guelb El Kebir": 37.6}, {"Chellalet El Adhaoura": 24.5},{"Ain Boucif": 48.9},{"Sour El Ghozlane":45.7}],
        "Wilaya": "Medea"
    },
    "Si Mahdjoub" : {
        "Coordinates":(36.1618504452157, 2.71867765425278),
        "Neighbors":[{"Ouled Antar": 87.6}, { "Seghouane": 41.9},{"Berrouaghia":24.4 },{"Ouzera": 28.6}, {"Ouamri": 35.6},{"Djendel":42.8}],
        "Wilaya": "Medea"
    },

    "Ouamri" : {
        "Coordinates":(36.23240740208607, 2.5614392860536155),
        "Neighbors":[{"Si Mahdjoub":35.6}, { "Medea": 28.5},{"Ouzera": 42.4},{"Mouzaia":60.9},{"Djendel":19.1},{"Boumedfaa": 57.0}],
        "Wilaya": "Medea"
    },
    "Ouzera" : {
        "Coordinates":(36.253838426178625, 2.8447570351341223),
        "Neighbors":[{"Si Mahdjoub": 28.4}, { "Medea":8.9},{"Ouamri":42.1},{"Seghouane":35.8},{"Berrouaghia":17.3},{"El Omaria":31.6},{"Ouled Yaich":45},{"Blida":38.8},{"Chrea": 57.2 },{"Hammam Melouane":93.6 }],
        "Wilaya": "Medea"
    },
     "Medea" : {
        "Coordinates":(36.2640194695291, 2.7566269695555743),
        "Neighbors":[{"Ouamri": 28.5},{"Ouzera": 9.2},{"Mouzaia":35},{"Ain Romana":37.3}],
        "Wilaya": "Medea"
    },

     "El Omaria" : {
        "Coordinates":(36.27185731497328, 3.0244725665995635),
        "Neighbors":[{"Ouzera": 31.4},{"Berrouaghia": 22.8}, {"Sidi Naamane": 14.1},{"Tablat": 60.3},{"Bougara":56.9},{"Hammam Melouane": 31.4 }],
        "Wilaya": "Medea"
    },
     "Sidi Naamane" : {
        "Coordinates":(36.21891153468776, 3.124117306061312),
        "Neighbors":[{"Berrouaghia":24.3},{"El Omaria":14.1}, {"Beni Slimane": 21.5},{"Tablat":47.8}],
        "Wilaya": "Medea"
    },
     "Beni Slimane" : {
        "Coordinates":(36.2371909184076, 3.3103951443218924),
        "Neighbors":[{"Souaghi":26.8},{"Sidi Naamane":21.4}, {"El Guelb El Kebir": 11.0},{"Tablat":34.7}],
        "Wilaya": "Medea"
    },
     "Tablat" : {
        "Coordinates":(36.41511242016637, 3.3103629260842355),
        "Neighbors":[{"El Omaria":60.1},{"Sidi Naamane":47.6}, {"El Guelb El Kebir":29.4},{"Beni Slimane":33.8},{"El Azizia":26.1},{"Bougara":42.9},{"Larbaa":36.2},{"Lakhdaria": 46.1},{"Ouled Selama": 40.2 },{"Souhane": 19.1 }],
        "Wilaya": "Medea"
    },
     "El Azizia" : {
        "Coordinates":(36.28575913268733, 3.495372722309083),
        "Neighbors":[{"Tablat":26.3}, {"El Guelb El Kebir":11},{"Lakhdaria":76.7},{"Souk El Khemis":34.1},{"Bir Ghbalou":8.9}],
        "Wilaya": "Medea"
    },
     "El Guelb El Kebir" : {
        "Coordinates":(36.257243478789476, 3.414052218459702),
        "Neighbors":[{"Tablat":29.5}, {"Beni Slimane":11},{"El Azizia":10.6},{"Souagui":31.7},{"Bir Ghbalou":16.5},{"Sour El Ghozlane":35.9}],
        "Wilaya": "Medea"
    },
#mostaganem =mascara , relizane , chlef
   "Ain Nouissy":{
       "Coordinates":(35.80551609293692, 0.044635316950195444),
       "Neighbors":[{"Hassi Maameche":6.9},{"Mesra":14.4},{"Bouguirat":23.3},{"Mohammadia":25.8}],
       "Wilaya":"Mostaganem"
   },
     "Hassi Maameche":{
       "Coordinates":(35.838355056257214, 0.026694926890360123),
       "Neighbors":[{"Ain Nouissy":6.9},{"Mesra":16.7},{"Bouguirat":31.5},{"mostaganem":14.7},{"Kheirddine":25.2}],
       "Wilaya":"Mostaganem"
   },
     "Mesra":{
       "Coordinates":(35.838355056257214, 0.026694926890360123),
       "Neighbors":[{"Hassi Maameche":18.2},{"Kheireddine":18.3},{"Bouguirat":14.2},{"Ain Tedles":25.4}],
       "Wilaya":"Mostaganem"
   },
     "Bouguirat":{
       "Coordinates":(35.75282511279706, 0.251197579264401),
       "Neighbors":[{"Hassi Maameche": 31.4},{"Mesra":14.3},{"Ain Tedles":35.7},{"El Matmar":21.5},{"Yellel":11.3},{"Mohammadia":31.3}],
       "Wilaya":"Mostaganem"
   },
   "mostaganem":{
       "Coordinates":(35.93138943625694, 0.0902930882068597),
       "Neighbors":[{"Hassi Maameche":14.8},{"Kheireddine":9.5},{"Sidi Lakhdar":49.2},{"Ain Tedles":21.4}],
       "Wilaya":"Mostaganem"
   },
     "Kheireddine":{
       "Coordinates":(35.980884197956435, 0.16830118820685971),
       "Neighbors":[{"Hassi Maameche":25.9},{"Mesra":18.3},{"Ain Tedles":12.7},{"Sidi Lakhdar":45.9}],
       "Wilaya":"Mostaganem"
   },
    "Ain Tedles" :{
       "Coordinates":(35.995896704008075, 0.3009830242650519),
       "Neighbors":[{"Kheireddine":12.7},{"Mesra":25.4},{"Bouguirat":35.7},{"Sidi Lakhdar":30.6},{"Sidi Ali":21.7},{"Mostaganem":21.6},{"El Matmar":52}],
       "Wilaya":"Mostaganem"
   },
     "Sidi Lakhdar" :{
       "Coordinates":(36.16041850382115, 0.43733812160061136),
       "Neighbors":[{"Achaacha":27.2},{"Ain Tedles":30.6},{"Sidi Ali":9.6},{"Mostaganem":49.7}],
       "Wilaya":"Mostaganem"
   },
     "Sidi Ali" :{
       "Coordinates":(36.10034743369129, 0.4196588382068596),
       "Neighbors":[{"Achaacha":"36.8"},{"Ain Tedles":21.6},{"Sidi Lakhdar":9.6},{"Djidioua":46.8},{"El Matmar":68.4}],
       "Wilaya":"Mostaganem"
   },
     "Achaacha" :{
       "Coordinates":(36.243071257974655, 0.6368691442681631),
       "Neighbors": [{"Sidi Ali":36.9},{"Sidi Lakhdar":27.2},{"Sidi Mhamed Ben Ali":34.8},{"Taougrite":38.8},{"El Marsa":340}],
       "Wilaya":"Mostaganem"
   },
    #Msila = djelfa , medea ,bouira , bordj bou arreridj , batna , biskra , ouled djellal
     "Ain El Melh" :{
       "Coordinates":(34.84673378396778, 4.161586017524983),
       "Neighbors":[{"Medjedel":79.6},{"Djebel Messaad":18.9},{"Ben Srour":47.6},{"Ouled Djellal":140},{"Dar Chioukh":89.3},{"Faidh El Botma":55.1}],
       "Wilaya":"Msila"
   },
     
       "Ouled Djellal" :{
       "Coordinates":(34.42911221988833, 5.060424071228931),
       "Neighbors":[{"Ain El Melh":140},{"Ben Srour":102},{"El M'Ghair":107},{"Foughala":52.3},{"Ourlal":53.6}],
       "Wilaya":"Msila"
   }, 
    "Medjedel" :{
       "Coordinates":(35.15235325904576, 3.6716260832414194),
       "Neighbors":[{"Sidi Ameur":38.1},{"Djebel Messaad":62.3},{"Had Sahary":96.9},{"Dar Chioukh":39},{"Hassi Bahbah": 89.8}],
       "Wilaya":"Msila"
   },
     "Djebel Messaad" :{
       "Coordinates":(34.98855296458749, 4.091589252551673),
       "Neighbors":[{"Sidi Ameur":72.3},{"Medjedel":62.4},{"Ain El Melh":18.9},{"Ben Srour": 65.3},{"Bou Saada": 31.8},{"Khoubana": 61.4}],
       "Wilaya":"Msila"
   },
    "Ben Srour" :{
       "Coordinates":(35.05563021563846, 4.556587280858081),
       "Neighbors":[{"Djebel Messaad":65.4},{"Ain El Melh":47.6},{"Khoubana":59.5},{"Ouled Djellal":102},{"Tolga":91.2},{"Djezzar":106},{"Barika":94.3}],
       "Wilaya":"Msila"
   },
     "Sidi Ameur" :{
       "Coordinates":(35.38632303551293, 3.9062622777548834),
       "Neighbors":[{"Djebel Messaad":72.3},{"Medjedel":38.1},{"Bou Saada":34.5},{"Ouled Sidi Brahim": 162},{"Ain El Hadjel": 33.8},{"Had Sahary": 58.8}],
       "Wilaya":"Msila"
   },
    "Bou Saada" :{
       "Coordinates":(35.21886037885146, 4.181180505817156),
       "Neighbors":[{"Djebel Messaad":31.8},{"Sidi Ameur":34.5},{"Khoubana":30},{"Ouled Sidi Brahim":155},{"Chellal":41.5}],
       "Wilaya":"Msila"
   },
    "Khoubana" :{
       "Coordinates":(35.322456929366304, 4.416071488812112),
       "Neighbors":[{"Djebel Messaad":61.2},{"Bou Saada":29.9},{"Ouled Derradj":75.8},{"Chellal":29.8},{"Djezzar":94.8}],
       "Wilaya":"Msila"
   },
     "Ouled Sidi Brahim" :{
       "Coordinates":(36.2193931674357, 4.327256713823733),
       "Neighbors":[{"Sidi Ameur":162},{"Bou Saada": 152},{"Ain El Hadjel":129},{"Chellal":111}],
       "Wilaya":"Msila"
   },
     "Chellal" :{
       "Coordinates":(35.5166634813475, 4.3866471791067045),
       "Neighbors":[{"Ouled Sidi Brahim":112},{"Bou Saada":41.5},{"Ain El Hadjel":63.3},{"Hammam Dalaa":56.5},{"Msila":28.2},{"Ouled Derradj":46.6},{"Khoubana":29.9}],
       "Wilaya":"Msila"
   },
    "Ouled Derradj" :{
       "Coordinates":(35.689547643778376, 4.7764156999999905),
       "Neighbors":[{"Chellal":47.1},{"Msila":23.9},{"Magra":34.6},{"Khoubana":76.5},{"Djezzar":60},{"Salah Bey":68.3}],
       "Wilaya":"Msila"
   },
     "Magra" :{
       "Coordinates":(35.61634011876031, 5.096897366237514),
       "Neighbors":[{"Ouled Derradj":34.3},{"Djezzar":25.8},{"Salah Bey":39.8}],
       "Wilaya":"Msila"
   },
     "Msila" :{
       "Coordinates":(35.72069685321012, 4.523749008804584),
       "Neighbors":[{"Ouled Derradj":23.9},{"Chellal":28.2},{"Hammam Dalaa":28.2}],
       "Wilaya":"Msila"
   },
    "Ain El Hadjel" :{
       "Coordinates":(35.67557384604894, 3.8823032396859114),
       "Neighbors":[{"Sidi Ameur":33.8},{"Chellal":63.2},{"Hammam Dalaa":93.8},{"Ouled Sidi Brahim":129},{"Sidi Aissa":26.1},{"Had Sahary":92.5}],
       "Wilaya":"Msila"
   },
     "Sidi Aissa" :{
       "Coordinates":(35.88453864133726, 3.773452927754884),
       "Neighbors":[{"Ain El Hadjel":26.1},{"Hammam Dalaa":72},{"Chellalet El Adhaoura":35},{"Mansoura":93.8},{"El Mhir":84.5},{"Bordj Okhriss":40},{"Sour El Ghozlane":32.2},{"Had Sahary":119},{"Birine":84.4}],
       "Wilaya":"Msila"
   },
    "Hammam Dalaa" :{
       "Coordinates":(35.91903655817128, 4.379699118567121),
       "Neighbors":[{"Sidi Aissa":72},{"Ain El Hadjel":94},{"Chellal":55.7},{"Msila":28.3},{"Mansoura":42.9},{"Ksour":30.5},{"Bordj Okhriss":68.5}],
       "Wilaya":"Msila"
   },
    #Ouergla = in salah , ilizi , el meniaa , gherdaia , djelfa , ouled djellal, el mghair , tougourt , el oued 
      "Hassi Massouad" :{
       "Coordinates":(31.71461511150553, 6.046260037064519),
       "Neighbors":[{"El Borma":342},{"Rouissat":85.2},{"Ain Beida":75.3},{"Hassi Ben Abdellah":80.9},{"Taibet":211},{"Zelfana":219},{"El Meniaa":494},{"In Salah":883},{"In Amenas":735},{"Foggaret Ezzaouia": 914 }],
       "Wilaya":"Ouergla"
   },
    "El Borma" :{
       "Coordinates":(31.601777242386838, 9.176620840153275),
       "Neighbors":[{"Hassi Massouad":341},{"Taibet":552},{"Taleb Larbi":388},{"In Amenas":500}],
       "Wilaya":"Ouergla"
   },
    "Rouissat" :{
       "Coordinates":(31.922262669865336, 5.3353611418026805),
       "Neighbors":[{"Hassi Massouad":86},{"Ain Beida":7.5},{"Ouergla":4.2}],
       "Wilaya":"Ouergla"
   },
     "Ain Beida" :{
       "Coordinates":(31.93033848413761, 5.3891608921149246),
       "Neighbors":[{"Hassi Massouad":78.6},{"Rouissat":8.2},{"Sidi Khouiled":7.4},{"Hassi Ben Abdellah":20.3}],
       "Wilaya":"Ouergla"
   },
    "Hassi Ben Abdellah" :{
       "Coordinates":(32.02935264383348, 5.474304934352502),
       "Neighbors":[{"Hassi Massouad":82.7},{"Ain Beida":18.6},{"Sidi Khouiled":9.5},{"N'Goussa":33.7}],
       "Wilaya":"Ouergla"
   },
    "Sidi Khouiled" :{
       "Coordinates":(31.97918228424428, 5.418003585601479),
       "Neighbors":[{"Ain Beida":5.7},{"Hassi Ben Abdellah":9.9},{"N'Goussa":26.1},{"Ouergla":10.9},{"El Hadjira":106}],
       "Wilaya":"Ouergla"
   },
    "Ouergla" :{
       "Coordinates":(31.961355840754504, 5.322459373502096),
       "Neighbors":[{"Rouissat":5.3},{"Ain Beida":7.7},{"Sidi Khouiled":12.7},{"N'Goussa":23.8},{"El Hadjira":132},{"Guerrara":196},{"Zelfana":135},{"Mansoura":210},{"Messaad":411},{"Faidh El Botma":462}],
       "Wilaya":"Ouergla"
   },
    "N'Goussa" :{
       "Coordinates":(32.19185876569648, 5.303381087745327),
       "Neighbors":[{"Ouergla":23.8},{"Sidi Khouiled":25.5},{"Hassi Ben Abdellah":33.6},{"El Hadjira":81.7},{"Djamaa":235}],
       "Wilaya":"Ouergla"
   },
    #Naama = tlemcen, sidi bel abbes , El Bayadh , bechar 
    "Moghrar" :{
       "Coordinates":(32.515860387182464, -0.5807598360688431),
       "Neighbors":[{"Sfissifa":70.1},{"Ain Sefra":55.8},{"Assela":94.7},{"Beni Ounif":91.3}],
       "Wilaya":"Naama"
   },
    "Assela" :{
       "Coordinates":(33.00578599132145, -0.08326174727671597),
       "Neighbors":[{"Moghrar":94.7},{"Ain Sefra":65.9},{"Naama":54.5},{"El Abiodh Sidi Cheikh":106}],
       "Wilaya":"Naama"
   },
    "Sfissifa" :{
       "Coordinates":(32.7370257764856, -0.8690544028506811),
       "Neighbors":[{"Moghrar":70.1},{"Ain Sefra":30.4},{"Mecheria":130}],
       "Wilaya":"Naama"
   },
     "Ain Sefra" :{
       "Coordinates":(32.75827856537566, -0.5823368177165651),
       "Neighbors":[{"Moghrar":55.4},{"Sfissifa":30.5},{"Naama":70.2},{"Assela":65.5}],
       "Wilaya":"Naama"
   },
     "Naama" :{
       "Coordinates":(33.269419593877224, -0.31434446297317664),
       "Neighbors":[{"Sfissifa":95.9},{"Ain Sefra":70.2},{"Mecheria":32.7},{"Assela":54.5},{"Chellala":73.6},{"Boussemghoun":93}],
       "Wilaya":"Naama"
   },
     "Mecheria" :{
       "Coordinates":(33.54976665209375, -0.2788837765379194),
       "Neighbors":[{"Naama":31.7},{"Sfissifa":129},{"Makman Ben Amer":59.1},{"Marhoum":120},{"Ras El Ma":152},{"Bougtoub":65.7},{"Chellala":106},{""}],
       "Wilaya":"Naama"
   },
     "Makman Ben Amer" :{
       "Coordinates":(33.71790541380561, -0.7298828975325085),
       "Neighbors":[{"Mecheria":60.3},{"Sidi Djillali":132},{"Sebdou":128},{"Ras El Ma": 114}],
       "Wilaya":"Naama"
   },
    #gherdaia = el meniaa , El Bayadh , laghouat ,djelfa , Ouergla

     "Metlili" :{
       "Coordinates":(32.260446611693574, 3.660479099339418),
       "Neighbors":[{"Zelfana":68.7},{"Bounoura":41.2},{"Gherdaia":47.1},{"Daia Ben Dahoua": 65.4},{"Mansoura":44.5},{"Ain Madhi":298},{"Brezina":305}],
       "Wilaya":"Gherdaia"
   },
     "Daia Ben Dahoua" :{
       "Coordinates":(32.564217106676125, 3.5900664789954195),
       "Neighbors":[{"Metlili":65},{"Gherdaia":9.5},{"Berriane":49.9},{"Hassi R'Mel":124},{"Ain Madhi":264}],
       "Wilaya":"Gherdaia"
   },
     "Gherdaia" :{
       "Coordinates":(32.49626700062439, 3.643886156420403),
       "Neighbors":[{"Daia Ben Dahoua":9.5},{"Bounoura":6.4},{"Berriane":45.1}],
       "Wilaya":"Gherdaia"
   },
    "Bounoura" :{
       "Coordinates":(32.48165753147458, 3.7033123069656964),
       "Neighbors":[{"Daia Ben Dahoua":24.2},{"Gherdaia":6.6},{"Berriane":42.8},{"Guerrara":115},{"Zelfana":65}],
       "Wilaya":"Gherdaia"
   },
     "Zelfana" :{
       "Coordinates":(32.39820992037097, 4.223789584002745),
       "Neighbors":[{"Metlili":69.5},{"Bounoura":64.5},{"Guerrara":61.8},{"Hassi Massouad":223},{"Ouergla":137}],
       "Wilaya":"Gherdaia"
   },
     "Berriane" :{
       "Coordinates":(32.82597266177409, 3.761897492381516),
       "Neighbors":[{"Daia Ben Dahoua":40.8},{"Bounoura":43.5},{"Guerrara":72.3},{"Gherdaia":45.1},{"Hassi R'Mel":76.2}],
       "Wilaya":"Gherdaia"
   },
     "Guerrara" :{
       "Coordinates":(32.781791102973, 4.489430589985356),
       "Neighbors":[{"Berriane":72.4},{"Bounoura":116},{"Zelfana":61.7},{"Ouergla":198},{"Messaad":216},{"Hassi R'Mel":149}],
       "Wilaya":"Gherdaia"
  },

    #El Bayadh = bechar , naama , sidi bel abbes , saida , tiaret , laghouat ,Gherdaia , el meniaa , timimoun
     "El Abiodh Sidi Cheikh" :{
       "Coordinates":(32.91046635084897, 0.534316972467512),
       "Neighbors":[{"Brezina":93.4},{"Boussemghoun":110},{"El Bayadh":121},{"Chellala":90.1},{"Metlili":366},{"Tinerkouk":429},{"El Meniaa":605},{"Naama":160},{"Assela":106},{"Beni Ounif":285}],
       "Wilaya":"El Bayadh"
  },
     "Brezina" :{
       "Coordinates":(33.09788635010883, 1.268997504080861),
       "Neighbors":[{"Boualem":109},{"El Bayadh":86.2},{"Chellala":184},{"El Abiodh Sidi Cheikh":93.4},{"Metlili":305},{"Mansoura":581},{"El Meniaa":544},{"Ain Madhi":240}],
       "Wilaya":"El Bayadh"
  },
     "Boussemghoun" :{
       "Coordinates":(32.86942536475378, 0.022692270749772505),
       "Neighbors":[{"Chellala":19.4},{"El Abiodh Sidi Cheikh":109},{"Assela":35}],
       "Wilaya":"El Bayadh"
  },
     "Chellala" :{
       "Coordinates":(33.039761599881366, 0.05766261012633418),
       "Neighbors":[{"Boussemghoun":19.4},{"El Abiodh Sidi Cheikh":90},{"El Bayadh":140},{"Rogassa":181},{"Bougtoub":152},{"Naama":70},{"Mecheria":104}],
       "Wilaya":"El Bayadh"
  },
     "El Bayadh" :{
       "Coordinates":(33.6875149462135, 1.028883701958371),
       "Neighbors":[{"Chellala":140},{"El Abiodh Sidi Cheikh":121},{"Brezina":86.2},{"Boualem":58.7},{"Rogassa":42.6}],
       "Wilaya":"El Bayadh"
  },
      "Boualem" :{
       "Coordinates":(33.73014277383567, 1.5417427306312808),
       "Neighbors":[{"El Bayadh":57.3},{"Brezina":108},{"Rogassa":99.5},{"Ain Madhi":135},{"Brida":39.2},{"Gueltet Sidi Saad":97.5},{"Ain Deheb":178},{"Ain Kermes":203}],
       "Wilaya":"El Bayadh"
  },
     "Bougtoub" :{
       "Coordinates":(34.040204844250674, 0.0769180095162882),
       "Neighbors":[{"Chellala":152},{"Rogassa":96.5},{"Ain El Hadjar":83.1},{"Marhoum":54.9},{"Mecheria":65.8},{"Chellala":152},],
       "Wilaya":"El Bayadh"
  },
     "Rogassa" :{
       "Coordinates":(34.01959444640209, 0.9296887117502225),
       "Neighbors":[{"Chellala":181},{"El Bayadh":42.3},{"Boualem":101},{"Bougtoub":96.5},{"Ain Kermes":126},{"El Hassasna":225}],
       "Wilaya":"El Bayadh"
  },
    #oran =ain temouchent , sidi bel abbess , mascara , mostaganem 
    "Boutlelis" :{
       "Coordinates":(35.67992557635043, -0.41247072266800017),
       "Neighbors":[{"Ain El Turk":27.3},{"oran":31.9},{"Es Senia":28.2},{"Ain El Arbaa":38.3},{"Hammam Bou Hadjar":36.0},{"El Amria":11.9}],
       "Wilaya":"Oran"
    },
    "Ain El Turk" :{
       "Coordinates":(35.74261568118377, -0.7743764713270805),
       "Neighbors":[{"Boutlelis":39.2},{"oran":19.4}],
       "Wilaya":"Oran"
    },
     "Oran" :{
       "Coordinates":(35.69857559861002, -0.6339574698045524),
       "Neighbors":[{"Boutlelis":25.3+2},{"Es Senia":7.2},{"Bir El Djir":8.8},{"Ain EL Turk":19.8}],
       "Wilaya":"Oran"
    },
   "Es Senia" :{
       "Coordinates":(35.64789265414181, -0.6233807609427982),
       "Neighbors":[{"Boutlelis":22.8},{"oran":7.2},{"Bir El Djir":14},{"Oued Tlelat":22}],
       "Wilaya":"Oran"
    },
   "Oued Tlelat" :{
       "Coordinates":(35.551447114893165, -0.44932755576160993),
       "Neighbors":[{"Es Senia":22},{"Bir El Djir":29.7},{"Gdyel":32.8},{"Bethioua":35.1},{"Ain El Berd":29.4},{"Tessala":75.7},{"Oggaz":20.9},{"Zahana":7}],
       "Wilaya":"Oran"
    },
     "Bir El Djir" :{
       "Coordinates":(35.71806895294574, -0.5655303755164486),
       "Neighbors":[{"Es Senia":16.1},{"oran":8},{"Oued Tlelat":30.2},{"Gdyel":18.1}],
       "Wilaya":"Oran"
    },
     "Gdyel" :{
       "Coordinates":(35.78270059206135, -0.4222883885742449),
       "Neighbors":[{"Bir El Djir":15.9},{"Oued Tlelat":32.8},{"Bethioua":22.6},{"Arzew":15.6}],
       "Wilaya":"Oran"
    },
     "Arzew" :{
       "Coordinates":(35.85742008587122, -0.31801071050034274),
       "Neighbors":[{"Gdyel":14.8},{"Bethioua":17.2}],
       "Wilaya":"Oran"
    },
     "Bethioua" :{
       "Coordinates":(35.758856552718115, -0.2383598343310846),
       "Neighbors":[{"Arzew":17.5},{"Gdyel":22.3},{"Oued Tlelat":35.1},{"Zahana":45.5},{"Mohammadia":47.4},{"Ain Nouissy":30}],
       "Wilaya":"Oran"
    },
  #ain temouchent = tlemcen , sidi bel abbes , oran 
    "Oulhaça El Gheraba" :{
       "Coordinates":(35.234594494098886, -1.50574034907459),
       "Neighbors":[{"Beni Saf":32},{"Honaine":18.6},{"Remchi":28.1}],
       "Wilaya":"Ain Temouchent"
    },
      "Beni Saf" :{
       "Coordinates":(35.234594494098886, -1.50574034907459),
       "Neighbors":[{"Oulhaça El Gheraba":32},{"Ain Kihal":20.1},{"ain temouchent":28.5},{"Remchi":39.3}],
       "Wilaya":"Ain Temouchent"
    },
     "Ain Kihal" :{
       "Coordinates":(35.20243888985978, -1.1990030183895242),
       "Neighbors":[{"Beni Saf":28.3},{"Hammam Bou Hadjar":38.3},{"ain temouchent":16.1},{"Remchi":48.5}  ,{"Bensekrane":19.9},{"Ain Tallout":61.5},{"Tessala":58.6},{""}],
       "Wilaya":"Ain Temouchent"
    },
     "ain temouchent" :{
       "Coordinates":(35.30336903222508, -1.1389215385204716),
       "Neighbors":[{"Beni Saf":28.5},{"Hammam Bou Hadjar":21.2},{"El Malah":11.3},{"Ain Kihal":15.7}],
       "Wilaya":"Ain Temouchent"
    },
    "Hammam Bou Hadjar" :{
       "Coordinates":(35.30336903222508, -1.1389215385204716),
       "Neighbors":[{"El Amria":24.6},{"ain temouchent":21},{"El Malah":12.6},{"Ain Kihal":36},{"Ain El Arbaa":9.4},{"Tessala":30.9},{"Ain El Berd":71.5},{"Boutelis":36.2}],
        "Wilaya":"Ain Temouchent"
    },
    "El Malah" :{
       "Coordinates":(35.386464836769306, -1.0977850071269435),
       "Neighbors":[{"El Amria":19.6},{"ain temouchent":10.9},{"Hammam Bou Hadjar":12.7}],
       "Wilaya":"Ain Temouchent"
    },
    "El Amria" :{
       "Coordinates":(35.5252269515436, -1.0127766219261212),
       "Neighbors":[{"El Malah":19.7},{"Hammam Bou Hadjar":24.2},{"Boutelis":12.4}],
       "Wilaya":"Ain Temouchent"
    },
    "Ain El Arbaa" :{
       "Coordinates":(35.30336903222508, -1.1389215385204716),
       "Neighbors":[{"Hammam Bou Hadjar":9.3},{"Boutelis":38.1},{"Oued Tlelat":53.6}],
       "Wilaya":"Ain Temouchent"
    },
    #mascara = tiaret , saida , sidi bel abbes , oran , mostaganem , relizane 
     "Oggaz" :{
       "Coordinates":(35.562045795506336, -0.258104912839886),
       "Neighbors":[{"Zahana":15.6},{"Sig":8},{"Ain El Berd":38.4},{"Sfisef":61.8},{"Oued Tlelat":18.8}],
       "Wilaya":"Mascara"
    },
    "Zahana" :{
       "Coordinates":(35.52205854795306, -0.4049937694761874),
       "Neighbors":[{"Oggaz":17.7},{"Sig":21.9},{"Mohammadia":56.1},{"Oued Tlelat":7.5},{"Bethioua":45.6}],
       "Wilaya":"Mascara"
    },
     "Sig" :{
       "Coordinates":(35.531318193062695, -0.18944036441811177),
       "Neighbors":[{"Oggaz":7.8},{"Zahana":21.8},{"Mohammadia":25.1},{"Bou Hnifia":42},{"Sfisef":52.6}],
       "Wilaya":"Mascara"
    },
    "Mohammadia" :{
       "Coordinates":(35.52205854795306, -0.4049937694761874),
       "Neighbors":[{"Sig":25},{"Zahana":56.2},{"Ain Fares":31.3},{"Bou Hnifia":42.7},{"El Bordj":38.9},{"Bethioua":47.8},{"Ain Nouissy":25.9},{"Yellel":32.8}],
       "Wilaya":"Mascara"
    },
    "Bou Hnifia" :{
       "Coordinates":(35.3226572605766, -0.04770624227401617),
       "Neighbors":[{"Sig":42},{"Mohammadia":42.7},{"Ain Fares":40.3},{"Ain Fekan":27.8},{"Tizi":14.9},{"Sfisef":22.3}],
       "Wilaya":"Mascara"
    },
    "Ain Fares" :{
       "Coordinates":(35.48380665529466, 0.24724146690576773),
       "Neighbors":[{"Bou Hnifia":40.2},{"Mohammadia":31.5},{"mascara":14.6},{"Ghriss":36.7},{"Tizi":29.4},{"Tighennif":20.3},{"El Bordj":7.5}],
       "Wilaya":"Mascara"
    },
    "Ain Fekan" :{
       "Coordinates":(35.22792161510731, -0.006381422206544565),
       "Neighbors":[{"Bou Hnifia":27.9},{"Oued Taria":16.1},{"Tizi":12.8},{"Sidi Boubekeur":26.9},{"Sfisef":27.6}],
       "Wilaya":"Mascara"
    },
     "Tizi" :{
       "Coordinates":(35.31559978950211, 0.07210828672529832),
       "Neighbors":[{"Bou Hnifia":14.9},{"Oued Taria":28.4},{"Ain Fekan":12.8},{"Ghriss":13.2},{"mascara":12.4},{"Ain Fares":29.6}],
       "Wilaya":"Mascara"
    },
     "mascara" :{
       "Coordinates":(35.402461777175226, 0.14057619695299597),
       "Neighbors":[{"Ain Fares":14.6},{"Ghriss":19.6},{"Tizi":12.3}],
       "Wilaya":"Mascara"
    },
    "El Bordj" :{
       "Coordinates":(35.51764686358424, 0.2981149374588413),
       "Neighbors":[{"Ain Fares":7.5},{"Mohammadia":38.9},{"Tighennif":12.8},{"Oued El Abtal":49.1},{"Yellel":30.2},{"El Matmar":38.1}],
       "Wilaya":"Mascara"
    },
    "Oued Taria" :{
       "Coordinates":(35.11666595677117, 0.08619728509331848),
       "Neighbors":[{"Ain Fekan":16.1},{"Tizi":28.4},{"Ghriss":16.9},{"Aouf":29.6},{"Sidi Boubekeur":11.1}],
       "Wilaya":"Mascara"
    },
     "Ghriss" :{
       "Coordinates":(35.24844709363791, 0.15904040567513758),
       "Neighbors":[{"Oued Taria":17},{"Tizi":13.3},{"mascara":19.6},{"Aouf":29.7},{"Ain Fares":36.8},{"Tighennif":26.3},{"Hachem":38.4},{"El Bordj":37.8}],
       "Wilaya":"Mascara"
    },
     "Tighennif " :{
       "Coordinates":(35.41485399444267, 0.3271817691517621),
       "Neighbors":[{"Ain Fares":20.3},{"El Bordj":12.8},{"Ghriss":26.3},{"Hachem":16.5},{"Oued El Abtal":33.8}],
       "Wilaya":"Mascara"
    },
     "Aouf" :{
       "Coordinates":(35.09869072809135, 0.356735605875109),
       "Neighbors":[{"Oued Taria":29.6},{"Ghriss":30.5},{"Hachem":49.0},{"Frenda":76.3},{"Sidi Boubekeur":40.3},{"Ouled Brahim":22}],
       "Wilaya":"Mascara"
    },
      "Hachem" :{
       "Coordinates":(35.37203317186838, 0.4919766853640202),
       "Neighbors":[{"Oued El Abtal":23.9},{"Ghriss":38.5},{"Aouf":49},{"Tighennig":16.5},{"Frenda":86.8}],
       "Wilaya":"Mascara"
    },
      "Oued El Abtal" :{
       "Coordinates":(35.51764686358424, 0.2981149374588413),
       "Neighbors":[{"El Bordj":46.5},{"Tighennif":33.8},{"Hachem":23.9},{"Mechraa Safa":47.4},{"El Matmar":51.6},{"Mendes":39.8}],
       "Wilaya":"Mascara"
    },
    #relizane = tiaret , mascara , mostaganem , chlef , tissemsilt 
      "Yellel" :{
       "Coordinates":(35.72354387233527, 0.35644233868367586),
       "Neighbors":[{"El Matmar":9.7},{"relizane":21.2},{"El Matmar":9.7},{"El Bordj":30.5},{"Mohammadia":33.8},{"Bouguirat":12.3}],
       "Wilaya":"Relizane"
    },
    "El Matmar" :{
       "Coordinates":(35.73190516548051, 0.4597824840584456),
       "Neighbors":[{"Yellel":9.7},{"relizane":10.7},{" Mendes":49.3},{"El Bordj":38.1},{"Oued El Abtal":51.6}],
       "Wilaya":"Relizane"
    },
    "relizane" :{
       "Coordinates":(35.73190516548051, 0.4597824840584456),
       "Neighbors":[{"Yellel":19.8},{"El Matmar":10.7},{"El Matmar":10.7},{"El Hamadna":29},{"Zemmora":20.8}],
       "Wilaya":"Relizane"
    },
    "El Matmar" :{
       "Coordinates":(35.73597115497399, 0.45878767633484235),
       "Neighbors":[{"Yellel":9.7},{"relizane":10.7},{" El Hamadna":44.4},{"Djidioua":50.2},{"Bouguirat":21.5},{"Ain Tedles":51.8},{"Sidi Ali":68.2}],
       "Wilaya":"Relizane"
    },
    "Mendes" :{
       "Coordinates":(35.65225513816575, 0.8623946857461219),
       "Neighbors":[{"El Matmar":50.9},{"Zemmora":16.1},{"Ammi Moussa":58.2},{"Ain Tarek":70.9},{"Mechraa safa":41.6},{"Rahouia":22.1},{"Oued Lilli":51.1},{"Oued El Abtal":39.8},{"El Matmar":50.7}],
       "Wilaya":"Relizane"
    },
     "Zemmora" :{
       "Coordinates":(35.72364144640002, 0.7584703406957826),
       "Neighbors":[{"El Matmar":34.4},{"Mendes":16.6},{"Ammi Moussa":43.1},{"Djidioua":30},{"El Hamadna":24.2},{"relizane":20.8}],
       "Wilaya":"Relizane"
    },
     "El Hamadna" :{
       "Coordinates":(35.905952121844, 0.7746513802323529),
       "Neighbors":[{"El Matmar":44.4},{"Zemmora":24.2},{"relizane":29},{" Djidioua":5.8}],
       "Wilaya":"Relizane"
    },
    "Djidioua" :{
         "Coordinates":(35.93272223449134, 0.8305668414863044),
         "Neighbors":[{"Zemmora":30},{"El Hamadna":5.8},{"El Matmar":50.3},{"Ammi Moussa":38.7},{"Oued Rhiou":8.8},{"Mazouna":31.4},{"Sidi M'Hamed Ben Ali":36.4},{"Sidi Ali"}],
         "Wilaya":"Relizane"
    },
     "Sidi M'Hamed Ben Ali" :{
         "Coordinates":(36.14580437522596, 0.8406619380846172),
         "Neighbors":[{"Djidioua":35.7},{"Mazouna":5.2},{"Sid Ali":50.4},{"Achaacha":46.6},{"Taougrite":18.6},{"Ain Merane":14.6}],
         "Wilaya":"Relizane"
    },
     "Ain Tarek" :{
         "Coordinates":(35.78047985592164, 1.1288131336226057),
         "Neighbors":[{"Mendes":72.6},{"Ammi Moussa":13.7},{"Oued Lilli":41.2},{"Meghila":48.4},{"Lardjem":69.0}],
         "Wilaya":"Relizane"
    },
     "Ammi Moussa" :{
         "Coordinates":(35.87188739885282, 1.1070238174103388),
         "Neighbors":[{"Mendes":61.1},{"Ain Tarek":13.7},{"Ramka":26.9},{"Oued Rhiou":29.6},{"Djidioua":38.7},{"Zemmora":43.1},{"Boukadir":52.4},{"Lardjem":59.6}],
         "Wilaya":"Relizane"
    },
     "Oued Rhiou" :{
         "Coordinates":(35.961922782166276, 0.9172950648529273),
         "Neighbors":[{"Djidioua":8.8},{"Ammi Moussa":29.5},{"Mazouna":25.2},{"Boukadir":28.9}],
         "Wilaya":"Relizane"
    },
     "Mazouna" :{
         "Coordinates":(36.12182395121297, 0.8740363993472096),
         "Neighbors":[{"Djidioua":31.3},{"Oued Rhiou":25.3},{"Sidi M'Hamed Ben Ali":6},{"Ain Merane":13}],
         "Wilaya":"Relizane"
    },
     "Ramka" :{
         "Coordinates":(35.8692171438334, 1.282058949237762),
         "Neighbors":[{"Ain Tarek":36.3},{"Ammi Moussa":26.9},{"Ouled Ben Abdelkader":34.7},{"Lardjem":32.9}],
         "Wilaya":"Relizane"
    },
#el meniaa
  "El Meniaa" :{
         "Coordinates":(30.59351020511544, 2.8635460963608854),
         "Neighbors":[{"Mansoura":200},{"In Salah": 402}],
         "Wilaya":"El Meniaa"
    },
     "Mansoura" :{
         "Coordinates":(31.979819883721106, 3.7420376207857755),
         "Neighbors":[{"El Meniaa":200}],
         "Wilaya":"El Meniaa"
    },   


#tougourt
     
 "El Hadjira" :{
         "Coordinates":(32.62407277409955, 5.510798623070446),
         "Neighbors":[{"Megarine":117},{"Touggourt":98.8},{"Tamacine":90.5},{"Taibet":138}],
         "Wilaya":"Touggourt"
    }, 
  "Megarine" :{
         "Coordinates":(33.19131608431216, 6.093073993687091),
         "Neighbors":[{"El Hadjira":117},{"Touggourt":13.9},{"Taibet":44.2}],
         "Wilaya":"Touggourt"
    }, 
     "Touggourt" :{
         "Coordinates":(33.19131608431216, 6.093073993687091),
         "Neighbors":[{"El Hadjira":99},{"Tamacine":13.5},{"Megarine":13.5},{"Taibet":37.5}],
         "Wilaya":"Touggourt"
    }, 
      "Tamacine" :{
         "Coordinates":(33.010478144482384, 6.012144871436528),
         "Neighbors":[{"El Hadjira":101},{"Touggourt":12.6},{"Taibet":50.9}],
         "Wilaya":"Touggourt"
    }, 
      "Taibet" :{
         "Coordinates":(33.0783216263128, 6.384357032151859),
         "Neighbors":[{"Megarine":43.9},{"Touggourt":37.3},{"Tamacine":50.8},{"El Hadjira":138}],
         "Wilaya":"Touggourt"
    }, 


  #beni abbes
   "Tabelbala" :{
         "Coordinates":(29.38615904692561, -3.2511527536731366),
         "Neighbors":[{"Igli":408},{"beni Abbes":424},{"Kerzaz":514},{"Ouled Khoudir":565}],
         "Wilaya":"Beni Abbes"
    }, 
     "Igli" :{
         "Coordinates":(30.454072599645887, -2.290886604535841),
         "Neighbors":[{"Tabelbala":408},{"beni Abbes":76.8}],
         "Wilaya":"Beni Abbes"
    }, 
     "beni Abbes" :{
         "Coordinates":(30.13873761515584, -2.1654723718723705),
         "Neighbors":[{"Tabelbala":425},{"Igli":77.7},{"El Ouata":50.8}],
         "Wilaya":"Beni Abbes"
    }, 
     "El Ouata" :{
         "Coordinates":(29.86055548086046, -1.854234342699185),
         "Neighbors":[{"beni Abbes":50.8},{"Kerzaz":64.3}],
         "Wilaya":"Beni Abbes"
    }, 
     "Kerzaz" :{
         "Coordinates":(29.453663005121108, -1.416336436018758),
         "Neighbors":[{"Tabelbala":514},{"beni Abbes":115},{"El Ouata":64.3},{"Ouled Khoudir":55.7}],
         "Wilaya":"Beni Abbes"
    }, 
   "Ouled Khoudir" :{
         "Coordinates":(29.255252153516793, -1.0612761859296649),
         "Neighbors":[{"Tabelbala":565},{"Kerzaz":55.7}],
         "Wilaya": "Beni Abbes"
    }


}
