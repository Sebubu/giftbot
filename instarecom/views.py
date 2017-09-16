from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
mock = [
  {
    "description": "Unicorn Darboard Eclipse HD2",
    "ean": "054722794488",
    "price": 9900,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/9e/78/09/9e780908c4fe34f3810f00029a201441.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/9e/78/09/9e780908c4fe34f3810f00029a201441.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/9e/78/09/9e780908c4fe34f3810f00029a201441.50x50.jpg"
    },
    "id": 2212306,
    "categories": [
      "Tischtennisplatten & Billardtische",
      "Ball & Teamsport",
      "Sport & Freizeit"
    ],
    "sku": "1724845-A",
    "name": "Unicorn Darboard Eclipse HD2",
    "url": "/sport-freizeit/ball-teamsport/tischtennisplatten-billardtische/unicorn-darboard-eclipse-hd2-01724845",
    "tags": [
      "Ball & Teamsport",
      "Sport & Freizeit",
      "Tischtennisplatten & Billardtische"
    ],
    "l1_category_url": "/sport-freizeit",
    "l2_category_url": "/sport-freizeit/ball-teamsport",
    "l3_category_url": "/sport-freizeit/ball-teamsport/tischtennisplatten-billardtische",
    "brand": "Unicorn"
  },
  {
    "description": "Unicorn Steel Dart Bullet, Menge: 3 Stk., Gewicht: 24 g, \"Gary Anderson\"-Pfeile, Material:",
    "ean": "054722273273",
    "price": 2690,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/f8/84/6b/f8846b381c1909f069d7ed4cb121ed6e.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/f8/84/6b/f8846b381c1909f069d7ed4cb121ed6e.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/f8/84/6b/f8846b381c1909f069d7ed4cb121ed6e.50x50.jpg"
    },
    "id": 1351412,
    "categories": [
      "Tischtennisplatten & Billardtische",
      "Ball & Teamsport",
      "Sport & Freizeit"
    ],
    "sku": "469308-A",
    "name": "Unicorn Steel Dart Bullet",
    "url": "/sport-freizeit/ball-teamsport/tischtennisplatten-billardtische/unicorn-steel-dart-bullet-0469308",
    "tags": [
      "Ball & Teamsport",
      "Sport & Freizeit",
      "Tischtennisplatten & Billardtische"
    ],
    "l1_category_url": "/sport-freizeit",
    "l2_category_url": "/sport-freizeit/ball-teamsport",
    "l3_category_url": "/sport-freizeit/ball-teamsport/tischtennisplatten-billardtische",
    "brand": "Unicorn"
  },
  {
    "description": "Unicorn Striker, offizielles Sisal Dartboard der PDC (Professional Darts<br>\nCorporation). Hochwertiges Wettkampf-Board wie das Unicorn Eclipse.<br>\n- Sisal-Board<br>\n- komplette krampenfreie Konstruktion<br>\n- Integrierte Spider Konstruktion<br>\n<br>\nVerpackung Stück: <br>\nL 46.5, W 46.5, H 5.5",
    "ean": "2000000036058",
    "price": 5000,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/6b/62/0a/6b620af629bc3a7d1a12cfc092f3a27e.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/6b/62/0a/6b620af629bc3a7d1a12cfc092f3a27e.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/6b/62/0a/6b620af629bc3a7d1a12cfc092f3a27e.50x50.jpg"
    },
    "id": 2219194,
    "categories": [
      "Tischtennisplatten & Billardtische",
      "Ball & Teamsport",
      "Sport & Freizeit"
    ],
    "sku": "1670690-A",
    "name": "Unicorn Striker Bristle Board",
    "url": "/sport-freizeit/ball-teamsport/tischtennisplatten-billardtische/unicorn-striker-bristle-board-01670690",
    "tags": [
      "Ball & Teamsport",
      "Sport & Freizeit",
      "Tischtennisplatten & Billardtische"
    ],
    "l1_category_url": "/sport-freizeit",
    "l2_category_url": "/sport-freizeit/ball-teamsport",
    "l3_category_url": "/sport-freizeit/ball-teamsport/tischtennisplatten-billardtische",
    "brand": "Unicorn"
  },
  {
    "description": "<h3>Papier-Dartboard</h3><ul><li>Aus hochwertigen Papierfasern</li><li>Zweiseitig mit Ziel-Spiel auf der Rückseite</li><li>Inklusive 2 Dartsets</li></ul>",
    "ean": "054722790855",
    "price": 1990,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/7c/1d/8a/7c1d8a59bf2ec0e308e2dacf866f95e9.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/7c/1d/8a/7c1d8a59bf2ec0e308e2dacf866f95e9.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/7c/1d/8a/7c1d8a59bf2ec0e308e2dacf866f95e9.50x50.jpg"
    },
    "id": 1282916,
    "categories": [
      "Tischtennisplatten & Billardtische",
      "Ball & Teamsport",
      "Sport & Freizeit"
    ],
    "sku": "279476-A",
    "name": "Unicorn Dart Board Paper",
    "url": "/sport-freizeit/ball-teamsport/tischtennisplatten-billardtische/unicorn-dart-board-paper-0279476",
    "tags": [
      "Ball & Teamsport",
      "Sport & Freizeit",
      "Tischtennisplatten & Billardtische"
    ],
    "l1_category_url": "/sport-freizeit",
    "l2_category_url": "/sport-freizeit/ball-teamsport",
    "l3_category_url": "/sport-freizeit/ball-teamsport/tischtennisplatten-billardtische",
    "brand": "UNICORN"
  },
  {
    "description": "Unicorn Soft Electronic Dartboard",
    "ean": "054722795270",
    "price": 4400,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/4f/23/e7/4f23e7acaf0ce702a4f40b826f2488c4.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/4f/23/e7/4f23e7acaf0ce702a4f40b826f2488c4.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/4f/23/e7/4f23e7acaf0ce702a4f40b826f2488c4.50x50.jpg"
    },
    "id": 1229856,
    "categories": [
      "Tischtennisplatten & Billardtische",
      "Ball & Teamsport",
      "Sport & Freizeit"
    ],
    "sku": "183041-A",
    "name": "Unicorn Soft Electronic Dartboard",
    "url": "/sport-freizeit/ball-teamsport/tischtennisplatten-billardtische/unicorn-soft-electronic-dartboard-0183041",
    "tags": [
      "Ball & Teamsport",
      "Sport & Freizeit",
      "Tischtennisplatten & Billardtische"
    ],
    "l1_category_url": "/sport-freizeit",
    "l2_category_url": "/sport-freizeit/ball-teamsport",
    "l3_category_url": "/sport-freizeit/ball-teamsport/tischtennisplatten-billardtische",
    "brand": "Unicorn"
  },
  {
    "description": "<h3>Dart Board aus Sisalfasern</h3><ul><li>Dart Board in Turnierqualität</li><li>Hochwertige Runddrahtkonstruktion</li><li>Extrem kleine Drahthalterungen</li><li>Tackerfreies Bullseye</li></ul>",
    "ean": "054722793832",
    "price": 5335,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/63/b4/d5/63b4d5b24444f094f2812b964ae53100.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/63/b4/d5/63b4d5b24444f094f2812b964ae53100.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/63/b4/d5/63b4d5b24444f094f2812b964ae53100.50x50.jpg"
    },
    "id": 1253123,
    "categories": [
      "Tischtennisplatten & Billardtische",
      "Ball & Teamsport",
      "Sport & Freizeit"
    ],
    "sku": "146605-A",
    "name": "Unicorn Dart Board Striker Bristle",
    "url": "/sport-freizeit/ball-teamsport/tischtennisplatten-billardtische/unicorn-dart-board-striker-bristle-0146605",
    "tags": [
      "Ball & Teamsport",
      "Sport & Freizeit",
      "Tischtennisplatten & Billardtische"
    ],
    "l1_category_url": "/sport-freizeit",
    "l2_category_url": "/sport-freizeit/ball-teamsport",
    "l3_category_url": "/sport-freizeit/ball-teamsport/tischtennisplatten-billardtische",
    "brand": "UNICORN"
  },
  {
    "description": "Unicorn Steel Dart Steel Tip S200",
    "ean": "054722718125",
    "price": 1190,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/c8/b2/b6/c8b2b6d93038966114c4e8810da87d92.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/c8/b2/b6/c8b2b6d93038966114c4e8810da87d92.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/c8/b2/b6/c8b2b6d93038966114c4e8810da87d92.50x50.jpg"
    },
    "id": 1055397,
    "categories": [
      "Tischtennisplatten & Billardtische",
      "Ball & Teamsport",
      "Sport & Freizeit"
    ],
    "sku": "151246-A",
    "name": "Unicorn Steel Dart Steel Tip S200",
    "url": "/sport-freizeit/ball-teamsport/tischtennisplatten-billardtische/unicorn-steel-dart-steel-tip-s200-0151246",
    "tags": [
      "Ball & Teamsport",
      "Sport & Freizeit",
      "Tischtennisplatten & Billardtische"
    ],
    "l1_category_url": "/sport-freizeit",
    "l2_category_url": "/sport-freizeit/ball-teamsport",
    "l3_category_url": "/sport-freizeit/ball-teamsport/tischtennisplatten-billardtische",
    "brand": "Unicorn"
  },
  {
    "description": "Unicorn Dartpfeile SOFT TIP E300",
    "ean": "054722719153",
    "price": 1890,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/bd/3b/1b/bd3b1beca3f3ffabcc6ce5fdc9126c91.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/bd/3b/1b/bd3b1beca3f3ffabcc6ce5fdc9126c91.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/bd/3b/1b/bd3b1beca3f3ffabcc6ce5fdc9126c91.50x50.jpg"
    },
    "id": 1981187,
    "categories": [
      "Tischtennisplatten & Billardtische",
      "Ball & Teamsport",
      "Sport & Freizeit"
    ],
    "sku": "1083654-A",
    "name": "Unicorn Dartpfeile SOFT TIP E300",
    "url": "/sport-freizeit/ball-teamsport/tischtennisplatten-billardtische/unicorn-dartpfeile-soft-tip-e300-01083654",
    "tags": [
      "Ball & Teamsport",
      "Sport & Freizeit",
      "Tischtennisplatten & Billardtische"
    ],
    "l1_category_url": "/sport-freizeit",
    "l2_category_url": "/sport-freizeit/ball-teamsport",
    "l3_category_url": "/sport-freizeit/ball-teamsport/tischtennisplatten-billardtische",
    "brand": "Unicorn"
  },
  {
    "description": "- 3-pack of soft-tip darts<br>\n- 17 g brass-plated steel barrels<br>\n- Polypropylene shafts<br>\n- Polyester flights<br>\n- Includes a slim-line case<br>\n- Made in China<br>\n- 6 sets per master carton",
    "ean": "2000000062075",
    "price": 1000,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/a7/e6/8b/a7e68bb781ea9ce5e17eeb859021b151.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/a7/e6/8b/a7e68bb781ea9ce5e17eeb859021b151.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/a7/e6/8b/a7e68bb781ea9ce5e17eeb859021b151.50x50.jpg"
    },
    "id": 2201750,
    "categories": [
      "Tischtennisplatten & Billardtische",
      "Ball & Teamsport",
      "Sport & Freizeit"
    ],
    "sku": "1723559-A",
    "name": "Unicorn SOFT TIP - E200 - 17g",
    "url": "/sport-freizeit/ball-teamsport/tischtennisplatten-billardtische/unicorn-soft-tip-e200-17g-01723559",
    "tags": [
      "Ball & Teamsport",
      "Sport & Freizeit",
      "Tischtennisplatten & Billardtische"
    ],
    "l1_category_url": "/sport-freizeit",
    "l2_category_url": "/sport-freizeit/ball-teamsport",
    "l3_category_url": "/sport-freizeit/ball-teamsport/tischtennisplatten-billardtische",
    "brand": "Unicorn"
  },
  {
    "description": "Art.-Nr. 79085<br>\n- Hochqualitäts Papierkonstruktion<br>\n- Doppelseitiges Dartboard<br>\n- inkl. 2 Dartsets<br>\n- Grösse: 46 x 2,5 cm",
    "ean": "2000000036061",
    "price": 2000,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/39/22/b0/3922b0dd07e273b453020c32136635b6.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/39/22/b0/3922b0dd07e273b453020c32136635b6.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/39/22/b0/3922b0dd07e273b453020c32136635b6.50x50.jpg"
    },
    "id": 2219204,
    "categories": [
      "Tischtennisplatten & Billardtische",
      "Ball & Teamsport",
      "Sport & Freizeit"
    ],
    "sku": "1672496-A",
    "name": "Unicorn PAPER DARTBOARD 17\"x 3/4\"XL",
    "url": "/sport-freizeit/ball-teamsport/tischtennisplatten-billardtische/unicorn-paper-dartboard-17x-34xl-01672496",
    "tags": [
      "Ball & Teamsport",
      "Sport & Freizeit",
      "Tischtennisplatten & Billardtische"
    ],
    "l1_category_url": "/sport-freizeit",
    "l2_category_url": "/sport-freizeit/ball-teamsport",
    "l3_category_url": "/sport-freizeit/ball-teamsport/tischtennisplatten-billardtische",
    "brand": "Unicorn"
  },
  {
    "description": "21g Gary Anderson<br>\nLength: 50.29mm<br>\nDiameter: 6.35mm<br>\n<br>\nGary Anderson Silver Star™<br>\nPlayer Endorsed darts offer affordable excellence for demanding players of all standards. Using World Class Unicorn engineering, this range provides unrivalled player appeal across a broad range of materials and configurations.<br>\n<br>\nGary Anderson ist Dart Weltmeister der Jahre 14/15 und 15/16",
    "ean": "2000000062248",
    "price": 6500,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/d8/fc/a5/d8fca5891dbf4341537fb69e6b2d5def.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/d8/fc/a5/d8fca5891dbf4341537fb69e6b2d5def.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/d8/fc/a5/d8fca5891dbf4341537fb69e6b2d5def.50x50.jpg"
    },
    "id": 2219249,
    "categories": [
      "Tischtennisplatten & Billardtische",
      "Ball & Teamsport",
      "Sport & Freizeit"
    ],
    "sku": "1674962-A",
    "name": "Unicorn GARY ANDERSON SILVER STAR 80% Tungsten",
    "url": "/sport-freizeit/ball-teamsport/tischtennisplatten-billardtische/unicorn-gary-anderson-silver-star-80-tungsten-01674962",
    "tags": [
      "Ball & Teamsport",
      "Sport & Freizeit",
      "Tischtennisplatten & Billardtische"
    ],
    "l1_category_url": "/sport-freizeit",
    "l2_category_url": "/sport-freizeit/ball-teamsport",
    "l3_category_url": "/sport-freizeit/ball-teamsport/tischtennisplatten-billardtische",
    "brand": "Unicorn"
  },
  {
    "description": "<p><strong>BAGGYMAX® Schulrucksack-Set Toploader Functional Niffty 3teilig</strong></p>Set bestehend aus: 1 Schulrucksack, aus PES, Volumen 18 l, B 280 x H 165 x T 360 mm, stabile Bodenplatte für mehr Standfestigkeit und Schutz vor Nässe und Schmutz, Rückenpartie besteht aus weicher Polsterung und Belüftungsrillen für einen angenehmen Tragekomfort, mit gepolsterten, längenverstellbaren Tragegurten mit Reflexstreifen, Lageverstellriemen, mit Höhenverstellung für die optimale Anpassung am Kinderrücken, höhenverstellbarer Brustgurt, Tragegriff, 2 offene Seitentaschen mit Auslaufloch, kleines Reissverschlussfach innen, Inneneinteiler im Hauptfach, Studenplan im Deckel, reflektierende Elemente, Leergewicht 900 g, 1 Schüleretui B 205 x H 38 x T 140 mm, unbestückt, 1 Klappe mit Sichtfenster für Stundenplan oder Geodreieck, mit Platz für 20 Blei- oder Farbstifte, 3 Radiergummis oder Spitzer, 1 Massstab, 1 Füllfederhalter und 4 Tintenpatronen, 1 Sportbeutel B 320 x H 420 mm. <br> <br> Unicorn Dream <br> <br> <br>",
    "ean": "4047443325426",
    "price": 14900,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/22/b3/2c/22b32c43c44a0f3235e18017a0185369.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/22/b3/2c/22b32c43c44a0f3235e18017a0185369.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/22/b3/2c/22b32c43c44a0f3235e18017a0185369.50x50.jpg"
    },
    "id": 1913241,
    "categories": [
      "Schulanfang",
      "Büromaterial & Papeterie",
      "Wohnen & Haushalt"
    ],
    "sku": "1022390-A",
    "name": "Schulrucks.Set Niffty Unicorn",
    "url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang/schulrucksset-niffty-unicorn-01022390",
    "tags": [
      "Büromaterial & Papeterie",
      "Schulanfang",
      "Wohnen & Haushalt"
    ],
    "l1_category_url": "/wohnen-haushalt",
    "l2_category_url": "/wohnen-haushalt/bueromaterial-papeterie",
    "l3_category_url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang",
    "brand": "BAGGYMAX"
  },
  {
    "description": "<p><strong>BAGGYMAX® Schulrucksack-Set Fabby 3teilig</strong></p>Set bestehend aus: 1 Schulrucksack, aus PES, Volumen 18 l, B 280 x H 170 x T 360 mm, stabile Bodenplatte für mehr Standfestigkeit und Schutz vor Nässe und Schmutz, Rückenpartie besteht aus weicher Polsterung und Belüftungsrillen für einen angenehmen Tragekomfort, mit gepolsterten, längenverstellbaren Tragegurten mit Reflexstreifen, Tragegriff, 2 offene Seitentaschen mit Auslaufloch, kleines Reissverschlussfach innen, Inneneinteiler im Hauptfach, Stundenplan im Deckel, reflektierende Elemente, Leergewicht 900 g, 1 Schüleretui B 205 x H 38 x T 140 mm, gefüllt mit EBERHARD FABER Produkten, 7 Jumbo-Stifte, 12 Farbstifte, Bleistift, Massstab, Geodreieck, Doppelspitzer, Radierer und 1 Sportbeutel B 320 x H 420 mm. <br> <br> Unicorn Dream <br> <br> <br>",
    "ean": "4047443325242",
    "price": 13900,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/c9/91/11/c991117f208ff128be9d3ec23235c359.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/c9/91/11/c991117f208ff128be9d3ec23235c359.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/c9/91/11/c991117f208ff128be9d3ec23235c359.50x50.jpg"
    },
    "id": 2056150,
    "categories": [
      "Schulanfang",
      "Büromaterial & Papeterie",
      "Wohnen & Haushalt"
    ],
    "sku": "1316360-A",
    "name": "Schulrucks.Set Fabby Unicorn",
    "url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang/schulrucksset-fabby-unicorn-01316360",
    "tags": [
      "Büromaterial & Papeterie",
      "Schulanfang",
      "Wohnen & Haushalt"
    ],
    "l1_category_url": "/wohnen-haushalt",
    "l2_category_url": "/wohnen-haushalt/bueromaterial-papeterie",
    "l3_category_url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang",
    "brand": "BAGGYMAX"
  },
  {
    "description": "<p><strong>STEP BY STEP® Schulrucksack-Set Comfort 4teilig</strong></p>Set bestehend aus: 1 Schulrucksack, aus PES, Volumen 21 l, B 330 x H 385 x T 230 mm, Anatomic Air System ergonomisch geformtes, weich gepolstertes Rückenteil mit Belüftungsrillen, Mesh Back Cooling System d. h. spezielles Netzmaterial sorgt für eine hohe Luftdurchlässigkeit der Rückenpolsterung, Reflexstreifen vorne, Schultergurte mit starker Polsterung, Brustgurt, D-Ring zur einfachen Befestigung des Hüftgurts (der Hüftgurt ist separat erhältlich), isolierte Vordertasche mit Adressfach innen, flexibler Inneneinteiler, 2 Seitentaschen, durch Magnetverschluss (Snap Push) kinderleichtes Öffnen und selbstständiges Schliessen, Tragegriff, Aufhängeschlaufe, Stundenplan im Deckel, Karabiner für Schlüssel und kleine Reissverschlusstaschen innen, Leergewicht 1,25 kg, 1 Schüleretui B 185 x H 30 x T 125 mm, 24teilig gefüllt mit MARKEN Produkten, 7 grosse Farbstifte und 12 Farbstifte mit bruchfesten Qualitätsminen, Bleistift, Massstab, Zeichendreieck, Doppelspitzer, Radierer, 1 Schlamperetui B 205 x H 65 x T 65 mm und 1 Sportbeutel B 310 x H 375 mm. <br> <br> Unicorn <br> <br> <br>",
    "ean": "4047443232090",
    "price": 24900,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/5f/9b/16/5f9b1619f516775531db66ea677c157d.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/5f/9b/16/5f9b1619f516775531db66ea677c157d.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/5f/9b/16/5f9b1619f516775531db66ea677c157d.50x50.jpg"
    },
    "id": 1090188,
    "categories": [
      "Schulanfang",
      "Büromaterial & Papeterie",
      "Wohnen & Haushalt"
    ],
    "sku": "188045-A",
    "name": "Schulrucks.Set Comfort Unicorn",
    "url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang/schulrucksset-comfort-unicorn-0188045",
    "tags": [
      "Büromaterial & Papeterie",
      "Schulanfang",
      "Wohnen & Haushalt"
    ],
    "l1_category_url": "/wohnen-haushalt",
    "l2_category_url": "/wohnen-haushalt/bueromaterial-papeterie",
    "l3_category_url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang",
    "brand": "Step by Step"
  },
  {
    "description": "<p><strong>STEP BY STEP® Schulrucksack-Set Touch 5teilig</strong></p>Set bestehend aus: 1 Schulrucksack, aus PES, Volumen 20 l, B 330 x H 385 x T 235 mm, Anatomic Air System ergonomisch geformtes, weich gepolstertes Rückenteil mit Belüftungsrillen, Mesh Back Cooling System d. h. spezielles Netzmaterial sorgt für eine hohe Luftdurchlässigkeit der Rückenpolsterung, Reflexstreifen vorne und seitlich, Schultergurte mit starker Polsterung, höhenverstellbarer Brustgurt, D-Ring zur einfachen Befestigung des Hüftgurts (der Hüftgurt ist separat erhältlich), isolierte Vordertasche mit Adressfach innen, flexibler Inneneinteiler, 2 Seitentaschen, Tragegriff, Aufhängeschlaufe, Stundenplan im Deckel, Karabiner für Schlüssel und kleine Reissverschlusstaschen innen, stabiler Metallsteck-Verschluss mit Reflektor, Gummibänder zur Fixierung des Schüleretuis unter dem Deckel, Leergewicht 1,2 kg, 1 Schüleretui B 185 x H 30 x T 125 mm, 23teilig gefüllt mit MARKEN Produkten, 7 grosse Farbstifte und 12 Farbstifte mit bruchfesten Qualitätsminen, Bleistift, Massstab, Zeichendreieck, Doppelspitzer, 1 Schlamperetui B 205 x H 65 x T 65 mm, 1 Sportbeutel B 310 x H 375 mm und 1 Brustbeutel B 135 x H 105 mm. <br> <br> Unicorn <br> <br> <br>",
    "ean": "4047443235442",
    "price": 23900,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/c9/77/79/c9777908fc3bed96c75edfd11c82dbdd.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/c9/77/79/c9777908fc3bed96c75edfd11c82dbdd.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/c9/77/79/c9777908fc3bed96c75edfd11c82dbdd.50x50.jpg"
    },
    "id": 1323147,
    "categories": [
      "Schulanfang",
      "Büromaterial & Papeterie",
      "Wohnen & Haushalt"
    ],
    "sku": "196399-A",
    "name": "Schulrucks.Set Touch Unicorn",
    "url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang/schulrucksset-touch-unicorn-0196399",
    "tags": [
      "Büromaterial & Papeterie",
      "Schulanfang",
      "Wohnen & Haushalt"
    ],
    "l1_category_url": "/wohnen-haushalt",
    "l2_category_url": "/wohnen-haushalt/bueromaterial-papeterie",
    "l3_category_url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang",
    "brand": "Step by Step"
  },
  {
    "description": "<p><strong>STEP BY STEP® Schulrucksack-Set Light 2 4teilig</strong></p>Set bestehend aus: 1 Schulrucksack extra leicht, aus PES, Volumen 18 l, B 330 x H 375 x T 230 mm, Easy Elastic Backsystem für eine optimale Formstabilität und perfekte ergonomische Passform, Lageverstellriemen, Anatomic Air System ergonomisch geformtes, weich gepolstertes Rückenteil mit Belüftungsrillen, Mesh Back Cooling System d. h. spezielles Netzmaterial sorgt für eine hohe Luftdurchlässigkeit der Rückenpolsterung, Reflexstreifen vorne, Schultergurte in körpergerechter Bananenform mit weicher Polsterung und Gurtenden-Einhängung, festintegrierter höhenverstellbarer Brustgurt, D-Ring zur einfachen Befestigung des Hüftgurts (der Hüftgurt ist separat erhältlich), stabile Bodenplatte für mehr Standfestigkeit und Schutz vor Nässe und Schmutz, isolierte Vordertasche mit Adressfach innen, geräumiges Hauptfach mit integriertem Bücherfach zur ergonomisch sinnvollen Platzierung schwerer Gegenstände, durch Magnetverschluss (Snap Push) kinderleichtes Öffnen und selbstständiges Schliessen, 2 offene Seitentaschen mit Auslauflöchern, Aufhängeschlaufe, Stundenplan im Deckel, kleine Reissverschlusstaschen innen, Leergewicht 900 g, 1 Schüleretui B 185 x H 30 x T 125 mm, 24-teilig gefüllt mit MARKEN Produkten, 7 grosse Farbstifte und 12 Farbstifte mit bruchfesten Qualitätsminen, Bleistift, Massstab, Zeichendreieck, Doppelspitzer, Radierer, 1 Schlamperetui B 205 x H 65 x T 65 mm, 1 Sportbeutel B 310 x H 375 mm. <br> <br> Unicorn <br> <br> <br>",
    "ean": "4047443328557",
    "price": 22900,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/6d/8b/41/6d8b41775a52908291d6b687ffb5d4f5.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/6d/8b/41/6d8b41775a52908291d6b687ffb5d4f5.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/6d/8b/41/6d8b41775a52908291d6b687ffb5d4f5.50x50.jpg"
    },
    "id": 1913423,
    "categories": [
      "Schulanfang",
      "Büromaterial & Papeterie",
      "Wohnen & Haushalt"
    ],
    "sku": "1021984-A",
    "name": "Schulrucks.Set Light 2 Unicorn",
    "url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang/schulrucksset-light-2-unicorn-01021984",
    "tags": [
      "Büromaterial & Papeterie",
      "Schulanfang",
      "Wohnen & Haushalt"
    ],
    "l1_category_url": "/wohnen-haushalt",
    "l2_category_url": "/wohnen-haushalt/bueromaterial-papeterie",
    "l3_category_url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang",
    "brand": "Step by Step"
  },
  {
    "description": "<p><strong>BAGGYMAX® Schulrucksack Speedy</strong></p>aus PES, dreigeteiltes Hauptfach mit Reissverschluss, lässt sich bis zum Boden hin öffnen, 2 Fronttaschen mit Reissverschluss, 2 Seitentaschen offen, Rückenpartie besteht aus weicher Polsterung und Belüftungsrillen für einen angenehmen Tragekomfort, mit gepolsterten, längenverstellbaren Tragegurten mit Reflexstreifen, Lageverstellriemen, höhenverstellbarer Brustgurt, Tragegriff, reflektierende Elemente, Volumen 27 l. Masse: B 280 x H 370 x T 160 mm. Gewicht: 800 g. <br> <br> Unicorn Dream <br> <br> <br>",
    "ean": "4047443323484",
    "price": 7900,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/35/d8/23/35d823aaa5ef9e417f5783d908969997.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/35/d8/23/35d823aaa5ef9e417f5783d908969997.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/35/d8/23/35d823aaa5ef9e417f5783d908969997.50x50.jpg"
    },
    "id": 2056161,
    "categories": [
      "Schulanfang",
      "Büromaterial & Papeterie",
      "Wohnen & Haushalt"
    ],
    "sku": "1316373-A",
    "name": "Schulrucksack Speedy Unicorn",
    "url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang/schulrucksack-speedy-unicorn-01316373",
    "tags": [
      "Büromaterial & Papeterie",
      "Schulanfang",
      "Wohnen & Haushalt"
    ],
    "l1_category_url": "/wohnen-haushalt",
    "l2_category_url": "/wohnen-haushalt/bueromaterial-papeterie",
    "l3_category_url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang",
    "brand": "BAGGYMAX"
  },
  {
    "description": "<p><strong>BAGGYMAX® Trolley-Rucksack</strong></p>aus PES, dreigeteiltes Hauptfach mit Reissverschluss, lässt sich bis zum Boden hin öffnen, 2 Fronttaschen mit Reissverschluss, Rückenpartie besteht aus weicher Polsterung und Belüftungsrillen für einen angenehmen Tragekomfort, mit gepolsterten, längenverstellbaren Tragegurten mit Reflexstreifen, Lageverstellriemen, höhenverstellbarer Brustgurt, Tragegriff, reflektierende Elemente, ausziehbarer Teleskopgriff, robuste Rollen, verstärkter Boden, die gepolsterten Schultergurte können im Rückenfach mit Klettverschluss verstaut werden, Volumen 24 l. Masse: B 330 x H 460 x T 200 mm. Gewicht: 2,1 kg. <br> <br> Unicorn Dream <br> <br> <br>",
    "ean": "4047443323538",
    "price": 12900,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/24/d5/1e/24d51e064a5e1e59750ccfd00e45ef53.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/24/d5/1e/24d51e064a5e1e59750ccfd00e45ef53.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/24/d5/1e/24d51e064a5e1e59750ccfd00e45ef53.50x50.jpg"
    },
    "id": 2056170,
    "categories": [
      "Schulanfang",
      "Büromaterial & Papeterie",
      "Wohnen & Haushalt"
    ],
    "sku": "1316380-A",
    "name": "Trolley-Rucksack Unicorn Dream",
    "url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang/trolley-rucksack-unicorn-dream-01316380",
    "tags": [
      "Büromaterial & Papeterie",
      "Schulanfang",
      "Wohnen & Haushalt"
    ],
    "l1_category_url": "/wohnen-haushalt",
    "l2_category_url": "/wohnen-haushalt/bueromaterial-papeterie",
    "l3_category_url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang",
    "brand": "BAGGYMAX"
  },
  {
    "description": "<p><strong>STEP BY STEP® Schulrucksack-Set 2 in 1 4teilig</strong></p>lässt sich im Handumdrehen vom klassischen Schulrucksack in einen Rucksack verwandeln, Reissverschluss hinter den seitlichen Taschen öffnen, Verstärkungen aus den Öffnungen links und rechts entfernen, Deckel öffnen und dritte Verstärkung aus dem Klettverschlussfach herausnehmen und schon ist ein flexibler Rucksack entstanden, die Verstärkungen dienen nun als Schablonen und Malvorlagen. Set bestehend aus: 1 Schulrucksack, aus PES, Volumen 19 l, B 290 x H 375 x T 210 mm, höhenverstellbares Tragesystem, ergonomisch geformtes, weich gepolstertes Rückenteil, Reflexstreifen vorne, Schultergurte mit starker Polsterung, höhenverstellbarer Brustgurt, isolierte Vordertasche mit Adressfach innen, 2 Seitentaschen, durch Magnetverschluss (Fidlock) kinderleichtes Öffnen und selbstständiges Schliessen, Aufhängeschlaufe, Stundenplan im Deckel, Leergewicht 1,18 kg, 1 Schüleretui B 185 x H 30 x T 125 mm, 24teilig gefüllt mit MARKEN Produkten, 7 grosse Farbstifte und 12 Farbstifte mit bruchfesten Qualitätsminen, Bleistift, Massstab, Zeichendreieck, Doppelspitzer, Radierer, 1 Schlamperetui B 205 x H 65 x T 65 mm und 1 Sportbeutel B 310 x H 375 mm. <br> <br> Unicorn <br> <br> <br>",
    "ean": "4047443298898",
    "price": 26900,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/4f/79/7a/4f797a72a9f06dc3b987319a41327a38.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/4f/79/7a/4f797a72a9f06dc3b987319a41327a38.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/4f/79/7a/4f797a72a9f06dc3b987319a41327a38.50x50.jpg"
    },
    "id": 1143547,
    "categories": [
      "Schulanfang",
      "Büromaterial & Papeterie",
      "Wohnen & Haushalt"
    ],
    "sku": "185438-A",
    "name": "Schulrucksackset 2in1 Unicorn",
    "url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang/schulrucksackset-2in1-unicorn-0185438",
    "tags": [
      "Büromaterial & Papeterie",
      "Schulanfang",
      "Wohnen & Haushalt"
    ],
    "l1_category_url": "/wohnen-haushalt",
    "l2_category_url": "/wohnen-haushalt/bueromaterial-papeterie",
    "l3_category_url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang",
    "brand": "Step by Step"
  },
  {
    "description": "Step by Step Touch Schulranzen - SetUnicorn<br><br>5-teiliges Schulranzen-Set mit Einhorn - Motiv, in den Farben bordeaux und pink, bestehend aus: <br>- Schulthek<br>- Federmäppchen, komplett bestückt <br>- Schlamperetui <br>- Schulsportbeutel <br>- Brustbeutel <br><br>Schulranzen: <br>- Anatomic Air System: ergonomisch geformtes Rückenteil und Polsterung mit Belüftungsrillen <br>- Mesh Back Cooling System: durch spezielles Netzmaterial optimale Luftzirkulation an der Rückenpolsterung <br>- Schultergurte in körpergerechter S-Form mit starker Polsterung, höhenverstellbar, mit Gurtenden-Einhängung <br>- fest integrierter, höhenverstellbarer Brustgurt <br>- D-Ring zur einfachen Befestigung des separat erhältlichen Hüftgurts <br>- stabile Metallverschlüsse ermöglichen schnellen Zugriff auf das Hauptfach <br>- isolierte Vordertasche zum Kühl- oder Warmhalten von Speisen und Getränken <br>- Adressfach innen <br>- zwei Seitentaschen, Tragegriff, Aufhängeschlaufe <br>- Stundenplan im Deckel, Gummibänder zur Fixierung des Federmäppchens unter dem Deckel <br>- Karabiner für Schlüssel und kleine Reissverschlusstaschen innen <br>- flexibler Inneneinteiler <br>- reflektierende Elemente vorn und an den Seiten für Sicherheit bei Dunkelheit <br><br>Lieferumfang<br>- 1 Schulrucksack<br>- 1 Federmäppchen, komplett bestückt mit Markenstiften <br>- 7 Jumbo Farb-Markenstifte <br>- 12 Farb-Markenstifte <br>- 1 Bleistift <br>- 1 Step by Step Lineal <br>- 1 Step by Step Dreieckslineal <br>- 1 Step by Step Doppelspitzer <br>- 1 Schlampermäppchen <br>- 1 Sportbeutel <br>- 1 Brustbeutel <br><br>Material Polyester  <br>Höhe 38,5 cm <br>Breite 33 cm <br>Tiefe 23,5 cm <br>Gewicht (Ranzen/Rucksack) 1200 g <br>Volumen (Ranzen/Rucksack) 20 l <br>Design/Motiv : Einhorn <br><br>",
    "ean": "4047443235442",
    "price": 21600,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/96/37/04/9637043ec6cd026c01cd6423a949bd80.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/96/37/04/9637043ec6cd026c01cd6423a949bd80.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/96/37/04/9637043ec6cd026c01cd6423a949bd80.50x50.jpg"
    },
    "id": 2111383,
    "categories": [
      "Schulanfang",
      "Büromaterial & Papeterie",
      "Wohnen & Haushalt"
    ],
    "sku": "1461943-A",
    "name": "Step by Step Touch Schulranzen - Set Unicorn 5-teilig",
    "url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang/step-by-step-touch-schulranzen-set-unicorn-5-teilig-01461943",
    "tags": [
      "Büromaterial & Papeterie",
      "Schulanfang",
      "Wohnen & Haushalt"
    ],
    "l1_category_url": "/wohnen-haushalt",
    "l2_category_url": "/wohnen-haushalt/bueromaterial-papeterie",
    "l3_category_url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang",
    "brand": "Step by Step"
  },
  {
    "description": "Step by Step Light 2 Schulranzen - Set Unicorn 4-teilig<br>Das Einhorn auf dem Schulthek begleitet die Mädchen in die Schule. Der Thek Unicorn / Einhorn ist der ideale Begleiter für Mädchen der 1. - 3. Klasse.<br><br>Mit dem geringen Gewicht von lediglich 0,9 Kg, den Abmessungen von 29 x 37,5 x 21 cm und einem Volumen von knapp 18 Litern eignet sich der liebevoll gestaltete Primarschulthek ranzen speziell für Kinder von der 1. bis zur 4. Klasse. Er ist besonders zu empfehlen für Kinder mit einem zierlichen Rücken. Er ist mit seinen 900g das Leichtgewicht im Step by Step Sortiment und verfügt über alles, was ein Schulranzen benötigt: Ein geräumiges Hauptfach mit integriertem Bücherfach, zwei Seitentaschen mit Auslaufösen und eine Fronttasche mit Thermofolie und Reflexstreifen. <br> <br><br>Easy Elastic Back System<br>Ein Highlight des neuen Light 2 ist das Easy-Elastic Backsystem. Das ergonomische und atmungsaktive Rückenteil überzeugt mit einer ultraleichten Fiberglas-Rückenkonstruktion, die dem Schulranzen optimale Formstabilität bei minimalstem Eigengewicht verleiht. Das elastische Material schmiegt sich beim Tragen des Schulranzens individuell an den Kinderrücken an und sorgt für hohen Tragekomfort. Die verstellbaren Schultergurte, Lageverstellriemen und der höhenverstellbare Brustgurt sorgen für optimalen Tragekomfort. Damit kann der Schulranzen perfekt an den Kinderrücken angepasst werden.<br><br>Der ergonomisch aufgebaute Schulranzen wird von der AKTION GESUNDER RÜCKEN E.V. (AGR) und der BUNDESARBEITSGEMEINSCHAFT FÜR HALTUNGS- UND BEWEGUNGSFÖRDERUNG E.V. (BAG) als besonders rückenschonend empfohlen.<br> <br>Das Innere der Schultasche erreicht man über den kinderleicht zu bedienenden Magnetverschluss, der sogar mit einer Hand zu bedienen ist. Hier findet man nicht nur das unterteilte Hauptfach des Step by Step Light 2, sondern auch eine kleine Reissverschlusstasche (z. B. für den Geldbeutel oder den Schlüsselbund) und einen praktischen Stundenplan, der sich unter dem Deckel befindet.<br> <br>Damit der Grundschulranzen stets angenehm befördert werden kann, ist auch das Tragesystem gut durchdacht. Hierzu zählt der Handtragegriff, welcher auch als Aufhängeschlaufe an der Schulbank verwendet werden kann, die gepolsterten Schulterträger, Lageverstellriemen, ein höhenverstellbarer Brustgurt und das atmungsative Rückenpolster. <br> <br>Gegen Nässe und Schmutz schützen den Schulthek das wasserabweisende Polyester und die stabile Bodenplatte. Die Bodenplatte des Ranzens hat erhöhte Stellfüsse und ermöglicht es, den Thek für Primarschüler auch auf dreckigen Boden zu stellen, ohne dass der Inhalt darunter leiden muss.<br> <br>Reflektierende Elemente an allen Seiten des Step by Step Light 2 Schulranzen ermöglichen eine bessere Sichtbarkeit der Schulkinder im Strassenverkehr. Somit sind die Kinder mit ihrer Schultasche für andere Verkehrsteilnehmer früher und besser zu erkennen.<br> <br>DAS SET:<br>Step by Step Light 2 Schulranzen-Set 4-teilig Unicorn inklusive Schulranzen, Etui gefüllt, Schlamperetui und Turnbeutel<br> <br>Schüleretui:<br>Das Federmäppchen hat eine Klappe und ist gefüllt mit Marken-Buntstiften, einem Bleistift, einem Doppelspitzer, einem Radierer, einem Lineal und einem Zeichendreieck. Zusätzlich hat es noch eine Schlaufe für einen Füller, und ein Klarsichtfach in der Klappe.<br>Aussenmass: 20,5 x 4 x 14 cm<br> <br>Sportbeutel:<br>Der Step by Step Turnbeutel wird einfach über den Ranzen gehängt oder am Rücken getragen. Er hat ein Hauptfach mit Kordelverschluss beidseitig und eine flache Reissverschlusstasche vorn.<br>Aussenmass: 31 x 1 x 37,5 cm<br>Volumen: 9 l<br> <br>Schlamperetui:<br>Dieses Schlampermäppchen ist einfach zu Öffnen und Schliessen durch einen RV und für alltägliche Schulutensilien, wie Stifte, Radiergummi etc. gedacht.<br>Aussenmass: 21 x 7,5 x 8 cm<br> <br>Der Step by Step Light 2 Schulranzen im Überblick:<br>- Volumen (Ranzen/Rucksack) \t18 l<br>- Gewicht (Ranzen/Rucksack) \t900 g<br>- Aussenmass Breite \t29 cm<br>- Aussenmass Höhe \t37,5 cm<br>- Aussenmass Tiefe \t21 cm<br>- Zertifizierung \tAGR-Gütesiegel/BAG-Gütesiegel<br>- Ausstattung: Anhebe-/Aufhängeschlaufe, Bücherfach, Isolierte Fronttasche, Magnetverschluss, Stabile, standfeste Bodenplatte, Stundenplanfach, Zwei Seitentaschen<br>- Ergonomie: Abnehmbarer, höhenverstellbarer Brustgurt, Atmungsaktives, ergonomisches Rückenpolster, Befestigungsmöglichkeit für optionalen Hüftgurt, Lageverstellriemen, Ultraleichte, elastische Fiberglas-Rückenkonstruktion, Verstellbare, ergonomische Schultergurte<br><br>",
    "ean": "4047443328557",
    "price": 21500,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/0e/ee/45/0eee455521bfa4c03dce0479ffafd250.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/0e/ee/45/0eee455521bfa4c03dce0479ffafd250.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/0e/ee/45/0eee455521bfa4c03dce0479ffafd250.50x50.jpg"
    },
    "id": 2115397,
    "categories": [
      "Schulanfang",
      "Büromaterial & Papeterie",
      "Wohnen & Haushalt"
    ],
    "sku": "1467988-A",
    "name": "Step by Step Light 2 Schulranzen Unicorn 4-teilig",
    "url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang/step-by-step-light-2-schulranzen-unicorn-4-teilig-01467988",
    "tags": [
      "Büromaterial & Papeterie",
      "Schulanfang",
      "Wohnen & Haushalt"
    ],
    "l1_category_url": "/wohnen-haushalt",
    "l2_category_url": "/wohnen-haushalt/bueromaterial-papeterie",
    "l3_category_url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang",
    "brand": "Step by Step"
  },
  {
    "description": "<p><strong>ERGOFLEX XL Schulthek - Set</strong><br> </p><p>Die XL-Variante hat alle Vorteile des ErgoFlex und ist der ideale Schulrucksack für grössere Kinder. Bei einem Gewicht von ca. 850 Gramm bietet er rund 25 % mehr Volumen als sein kleiner Bruder. Genauso ergonomisch, komfortabel und flexibel ist er natürlich auch - und genauso einfach verstellbar.</p><ul><li>Körpergerecht geformte, atmungsaktive Rückenpolsterung mit Mesh-Besatz</li><li>Abnehmbarer Beckengurt mit gepolsterten Seitenflügeln</li><li>Einfache Verstellung in mehreren Stufen auf die Rückenlänge des Kindes anpassbar</li><li>Seitentaschen für Regenschirm, Trinkflaschen o. Ä</li><li>Zwei grosse Hauptfächer für ergonomisches, rückenschonendes Packen</li><li>5-teiliges Set, bestehend aus: Ranzen, Sporttasche, Schüleretui, Faulenzermäppchen und Heftebox</li></ul>  <br> <table><tr> <td>Typ</td> <td>Schulthek </td> </tr><tr> <td>Zielgruppe</td> <td>Neutral</td> </tr><tr> <td>Fassungsvermögen</td> <td>25.5l</td> </tr><tr> <td>Set</td> <td>ja</td> </tr><tr> <td>Set-Inhalt</td> <td>Etui<br> Faulenzer-Etui<br> Schulthek <br> Sporttasche</td> </tr></table><br> <br>",
    "ean": "4006047406580",
    "price": 26800,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/3c/0e/ff/3c0eff6eacb2f7c934f132f69ddf72ac.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/3c/0e/ff/3c0eff6eacb2f7c934f132f69ddf72ac.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/3c/0e/ff/3c0eff6eacb2f7c934f132f69ddf72ac.50x50.jpg"
    },
    "id": 1633722,
    "categories": [
      "Schulanfang",
      "Büromaterial & Papeterie",
      "Wohnen & Haushalt"
    ],
    "sku": "568205-A",
    "name": "DERDIEDAS Schulrucksackset Ergoflex XL 40658 Happy Unicorn 5-teilig",
    "url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang/derdiedas-schulrucksackset-ergoflex-xl-40658-happy-unicorn-5-teilig-0568205",
    "tags": [
      "Büromaterial & Papeterie",
      "Schulanfang",
      "Wohnen & Haushalt"
    ],
    "l1_category_url": "/wohnen-haushalt",
    "l2_category_url": "/wohnen-haushalt/bueromaterial-papeterie",
    "l3_category_url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang",
    "brand": "DERDIEDAS"
  },
  {
    "description": "Step by Step Comfort Schulranzen - Set Unicorn<br><br>4-teiliges Schulranzen-Set Einhorn in den Farben bordeaux / rosa bestehend aus: <br>- Schulrucksack<br>- Federmäppchen, komplett bestückt <br>- Schlamperetui <br>- Sportbeutel <br><br>Schulranzen: <br>- ergonomisch geschwungene Rückenpartie mit weicher Polsterung und Belüftungsrillen <br>- Schultergurte in körpergerechter S-Form mit weicher Polsterung, höhenverstellbar, mit Gurtenden-Einhängung <br>- fest integrierter, höhenverstellbarer Brustgurt <br>- D-Ring zur einfachen Befestigung des separat erhältlichen Hüftgurts <br>- reflektierende Elemente vorn und an den Seiten für Sicherheit bei Dunkelheit <br>- stabiler Kunststoffboden mit erhöhten Stellfüssen zum Schutz vor Schmutz und Nässe <br>- einhändig bedienbarer Magnetverschluss ermöglicht schnellen Zugriff auf das Hauptfach <br>- geräumiges Hauptfach mit flexiblem Inneneinteiler zur ergonomisch sinnvollen Platzierung schwerer Gegenstände <br>- variabel befüllbares Frontfach mit zusätzlichen Taschen für Kleinteile <br>- isolierte Vordertasche zum Kühl- oder Warmhalten von Speisen und Getränken mit innenliegendem Adressfach <br>- zwei Seitentaschen, Tragegriff, Aufhängeschlaufe <br>- Stundenplan im Deckel, Gummibänder zur Fixierung des Federmäppchens unter dem Deckel <br>- Karabiner für Schlüssel und kleine Reissverschlusstaschen innen <br><br>Lieferumfang<br>- 1 Schulranzen <br>- 1 Federmäppchen, komplett bestückt mit Markenstiften <br>- 7 Jumbo Farb-Markenstifte <br>- 12 Farb-Markenstifte <br>- 1 Bleistift <br>- 1 Step by Step Lineal <br>- 1 Step by Step Dreieckslineal <br>- 1 Step by Step Doppelspitzer <br>- 1 Schlampermäppchen <br>- 1 Sportbeutel <br><br>Material Polyester  <br>Breite 33 cm <br>Höhe 38,5 cm<br>Tiefe 23 cm <br>Gewicht (Ranzen/Rucksack) 1250 g <br>Volumen (Ranzen/Rucksack) 21 l <br><br>Design/Motiv : Einhorn<br><br><br>",
    "ean": "4047443232090",
    "price": 22900,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/ba/5d/81/ba5d81b0eda42f275523a0cf5d4af787.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/ba/5d/81/ba5d81b0eda42f275523a0cf5d4af787.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/ba/5d/81/ba5d81b0eda42f275523a0cf5d4af787.50x50.jpg"
    },
    "id": 1877416,
    "categories": [
      "Schulanfang",
      "Büromaterial & Papeterie",
      "Wohnen & Haushalt"
    ],
    "sku": "958004-A",
    "name": "Step by Step Comfort Schulranzen - Set Unicorn 4 - teiliges Set",
    "url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang/step-by-step-comfort-schulranzen-set-unicorn-4-teiliges-set-0958004",
    "tags": [
      "Büromaterial & Papeterie",
      "Schulanfang",
      "Wohnen & Haushalt"
    ],
    "l1_category_url": "/wohnen-haushalt",
    "l2_category_url": "/wohnen-haushalt/bueromaterial-papeterie",
    "l3_category_url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang",
    "brand": "Step by Step"
  },
  {
    "description": "<p><strong>ERGOFLEX - Schulthek - Set</strong><br> Unicorn</p><p>Der Schulrucksack ErgoFlex ist so komfortabel wie ein Ranzen - bei einem Gewicht von nur ca. 800 Gramm. Damit er auch perfekt sitzt, können die gepolsterten Gurte schnell und einfach verstellt werden. Sitzt, passt und hat Platz für alles, was zum perfekten Schultag gehört.</p><ul><li>Körpergerecht geformte, atmungsaktive Rückenpolsterung mit Mesh-Besatz</li><li>Abnehmbarer Beckengurt mit gepolsterten Seitenflügeln</li><li>Einfache Verstellung in mehreren Stufen auf die Rückenlänge des Kindes anpassbar</li><li>Seitentaschen für Regenschirm, Trinkflaschen o. Ä</li><li>Zwei grosse Hauptfächer für ergonomisches, rückenschonendes Packen</li><li>Masse ca. 33 x 40 x 23 cm</li><li>Gewicht ca. 800 g</li><li>5-teiliges Set, bestehend aus: Ranzen, Sporttasche, Schüleretui, Faulenzermäppchen und Heftebox</li></ul>  <br> <table><tr> <td>Typ</td> <td>Schulthek </td> </tr><tr> <td>Zielgruppe</td> <td>Mädchen</td> </tr><tr> <td>Fassungsvermögen</td> <td>20.0l</td> </tr><tr> <td>Set</td> <td>ja</td> </tr><tr> <td>Set-Inhalt</td> <td>Etui<br> Faulenzer-Etui<br> Schulthek <br> Sporttasche<br> Andere</td> </tr></table><br> <br>",
    "ean": "4006047405583",
    "price": 25700,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/88/30/e3/8830e32ab332bbfc7b3b18db0b04d4dc.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/88/30/e3/8830e32ab332bbfc7b3b18db0b04d4dc.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/88/30/e3/8830e32ab332bbfc7b3b18db0b04d4dc.50x50.jpg"
    },
    "id": 1633058,
    "categories": [
      "Schulanfang",
      "Büromaterial & Papeterie",
      "Wohnen & Haushalt"
    ],
    "sku": "568049-A",
    "name": "DERDIEDAS Schulrucksack-Set 33x40x23cm 405-58 Unicorn 5-teilig",
    "url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang/derdiedas-schulrucksack-set-33x40x23cm-405-58-unicorn-5-teilig-0568049",
    "tags": [
      "Büromaterial & Papeterie",
      "Schulanfang",
      "Wohnen & Haushalt"
    ],
    "l1_category_url": "/wohnen-haushalt",
    "l2_category_url": "/wohnen-haushalt/bueromaterial-papeterie",
    "l3_category_url": "/wohnen-haushalt/bueromaterial-papeterie/schulanfang",
    "brand": "DERDIEDAS"
  },
  {
    "description": "Skip Hop Thermobehälter «Unicorn» 325 ml",
    "ean": "816523023804",
    "price": 2395,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/32/04/8f/32048fb1b90780a44d29b3c6df8e7046.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/32/04/8f/32048fb1b90780a44d29b3c6df8e7046.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/32/04/8f/32048fb1b90780a44d29b3c6df8e7046.50x50.jpg"
    },
    "id": 2959768,
    "categories": [
      "Babyflaschen & Schoppen",
      "Baby- & Kinderernährung",
      "Baby & Spielzeug"
    ],
    "sku": "2818249-A",
    "name": "Skip Hop Thermobehälter «Unicorn» 325 ml",
    "url": "/baby-spielzeug/baby-kinderernaehrung/babyflaschen-schoppen/skip-hop-thermobehaelter-unicorn-325-ml-02818249",
    "tags": [
      "Baby & Spielzeug",
      "Baby- & Kinderernährung",
      "Babyflaschen & Schoppen"
    ],
    "l1_category_url": "/baby-spielzeug",
    "l2_category_url": "/baby-spielzeug/baby-kinderernaehrung",
    "l3_category_url": "/baby-spielzeug/baby-kinderernaehrung/babyflaschen-schoppen",
    "brand": "Skip Hop"
  },
  {
    "description": "Skip Hop Trinkflasche «Unicorn» 300 ml",
    "ean": "879674020443",
    "price": 995,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/b2/e4/e7/b2e4e7726a7be9943e7b536cf652c226.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/b2/e4/e7/b2e4e7726a7be9943e7b536cf652c226.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/b2/e4/e7/b2e4e7726a7be9943e7b536cf652c226.50x50.jpg"
    },
    "id": 1742552,
    "categories": [
      "Babyflaschen & Schoppen",
      "Baby- & Kinderernährung",
      "Baby & Spielzeug"
    ],
    "sku": "780798-A",
    "name": "Skip Hop Trinkflasche «Unicorn» 300 ml",
    "url": "/baby-spielzeug/baby-kinderernaehrung/babyflaschen-schoppen/skip-hop-trinkflasche-unicorn-300-ml-0780798",
    "tags": [
      "Baby & Spielzeug",
      "Baby- & Kinderernährung",
      "Babyflaschen & Schoppen"
    ],
    "l1_category_url": "/baby-spielzeug",
    "l2_category_url": "/baby-spielzeug/baby-kinderernaehrung",
    "l3_category_url": "/baby-spielzeug/baby-kinderernaehrung/babyflaschen-schoppen",
    "brand": "Skip Hop"
  },
  {
    "description": "Skip Hop Behälter Snack Cup «Unicorn» 220 ml",
    "ean": "879674023116",
    "price": 1095,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/cc/cc/b5/ccccb51c2dc11ce15bb6d87ff1492d65.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/cc/cc/b5/ccccb51c2dc11ce15bb6d87ff1492d65.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/cc/cc/b5/ccccb51c2dc11ce15bb6d87ff1492d65.50x50.jpg"
    },
    "id": 2959773,
    "categories": [
      "Babyflaschen & Schoppen",
      "Baby- & Kinderernährung",
      "Baby & Spielzeug"
    ],
    "sku": "2818250-A",
    "name": "Skip Hop Behälter Snack Cup «Unicorn» 220 ml",
    "url": "/baby-spielzeug/baby-kinderernaehrung/babyflaschen-schoppen/skip-hop-behaelter-snack-cup-unicorn-220-ml-02818250",
    "tags": [
      "Baby & Spielzeug",
      "Baby- & Kinderernährung",
      "Babyflaschen & Schoppen"
    ],
    "l1_category_url": "/baby-spielzeug",
    "l2_category_url": "/baby-spielzeug/baby-kinderernaehrung",
    "l3_category_url": "/baby-spielzeug/baby-kinderernaehrung/babyflaschen-schoppen",
    "brand": "Skip Hop"
  },
  {
    "description": "Skip Hop Schale Unicorn",
    "ean": "879674020382",
    "price": 795,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/bf/45/42/bf4542f71ef7dc4fbd20045d53fe850b.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/bf/45/42/bf4542f71ef7dc4fbd20045d53fe850b.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/bf/45/42/bf4542f71ef7dc4fbd20045d53fe850b.50x50.jpg"
    },
    "id": 1742876,
    "categories": [
      "Kindergeschirr",
      "Baby- & Kinderernährung",
      "Baby & Spielzeug"
    ],
    "sku": "780961-A",
    "name": "Skip Hop Schale Unicorn",
    "url": "/baby-spielzeug/baby-kinderernaehrung/kindergeschirr/skip-hop-schale-unicorn-0780961",
    "tags": [
      "Baby & Spielzeug",
      "Baby- & Kinderernährung",
      "Kindergeschirr"
    ],
    "l1_category_url": "/baby-spielzeug",
    "l2_category_url": "/baby-spielzeug/baby-kinderernaehrung",
    "l3_category_url": "/baby-spielzeug/baby-kinderernaehrung/kindergeschirr",
    "brand": "Skip Hop"
  },
  {
    "description": "Skip Hop Teller Unicorn",
    "ean": "879674020368",
    "price": 995,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/06/dc/45/06dc45d41e63b5169db45e1dfb96928a.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/06/dc/45/06dc45d41e63b5169db45e1dfb96928a.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/06/dc/45/06dc45d41e63b5169db45e1dfb96928a.50x50.jpg"
    },
    "id": 1742869,
    "categories": [
      "Kindergeschirr",
      "Baby- & Kinderernährung",
      "Baby & Spielzeug"
    ],
    "sku": "780959-A",
    "name": "Skip Hop Teller Unicorn",
    "url": "/baby-spielzeug/baby-kinderernaehrung/kindergeschirr/skip-hop-teller-unicorn-0780959",
    "tags": [
      "Baby & Spielzeug",
      "Baby- & Kinderernährung",
      "Kindergeschirr"
    ],
    "l1_category_url": "/baby-spielzeug",
    "l2_category_url": "/baby-spielzeug/baby-kinderernaehrung",
    "l3_category_url": "/baby-spielzeug/baby-kinderernaehrung/kindergeschirr",
    "brand": "Skip Hop"
  }
]

def get_product_list(username, password, target_user):
    from instarecom.instagram.hashscrapper import InstaApi
    from instarecom.siroop.siroopapi import getproductlist
    api = InstaApi()
    api.login(username, password)
    hashtags = api.get_hashtags(target_user)
    products = getproductlist(hashtags)
    return products

@csrf_exempt
def recommendations(request):
    if request.method == 'POST':
        anfrage = request.body.decode('unicode_escape')
        anfrage = json.loads(anfrage)
        username = anfrage['userName']
        password = anfrage['password']
        target = anfrage['targetUser']
        print('userName', username)
        print('password', password)
        print('targetUser', target)
    else:
        username = 'severinbuhler'
        password = 'HackZurich2017'
        target = 'rebeka_gubser_10'
    products = get_product_list(username, password, target)
    return JsonResponse(products, safe=False)
    return JsonResponse(mock, safe=False)