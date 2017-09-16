from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

mock = [
  {
    "description": "<br> <br> <strong>Autor:</strong> Strasser, Christoph <br> <table><tr> <td>Seitenangabe</td> <td>272 S.</td> </tr><tr> <td>Masse</td> <td>H18.0 cm x B12.2 cm x D1.9 cm 244 g</td> </tr><tr> <td>Erscheinungsjahr</td> <td>2009</td> </tr><tr> <td>Einband</td> <td>Kartonierter Einband (Kt)</td> </tr><tr> <td>EAN</td> <td>9783866081048</td> </tr><tr> <td>ISBN</td> <td>978-3-86608-104-8</td> </tr></table><br> <br>",
    "ean": "9783866081048",
    "price": 650,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/00/29/bf/0029bfdfadd94f079cf14a674a33bde2.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/00/29/bf/0029bfdfadd94f079cf14a674a33bde2.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/00/29/bf/0029bfdfadd94f079cf14a674a33bde2.50x50.jpg"
    },
    "id": 2767924,
    "categories": [
      "Belletristik",
      "Bücher",
      "Medien & Unterhaltung"
    ],
    "sku": "2590356-A",
    "name": "Pornostern",
    "url": "/medien-unterhaltung/buecher/belletristik/pornostern-02590356",
    "tags": [
      "Belletristik",
      "Bücher",
      "Medien & Unterhaltung"
    ],
    "l1_category_url": "/medien-unterhaltung",
    "l2_category_url": "/medien-unterhaltung/buecher",
    "l3_category_url": "/medien-unterhaltung/buecher/belletristik",
    "brand": "Ubooks-Verlag U-line"
  },
  {
    "description": "Edition Rouge<br> <br> <strong>Zusammenfassung:</strong><br> <p> <br> Prickelnde Erotikkomödie aus Frankreich <br> mit Nathalie Baye (\"Catch Me If You Can\") und Sergi López (\"Tango Libre\").</p><br> <br> <strong>Autoren:</strong> Baye, Nathalie (Schausp.) ; López, Sergi (Schausp.) <br> <table><tr> <td>Ausgabekennzeichen</td> <td>Deutsch</td> </tr><tr> <td>Masse</td> <td>H19.0 cm x B13.7 cm x D1.7 cm 74 g; 78 Min.</td> </tr><tr> <td>Erscheinungsjahr</td> <td>2014</td> </tr><tr> <td>Einband</td> <td>DVD Video</td> </tr><tr> <td>EAN</td> <td>4260229591826</td> </tr></table><br> <br>",
    "ean": "4260229591826",
    "price": 890,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/66/60/33/66603399d796375e87bf0d9f5721b9cf.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/66/60/33/66603399d796375e87bf0d9f5721b9cf.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/66/60/33/66603399d796375e87bf0d9f5721b9cf.50x50.jpg"
    },
    "id": 2815812,
    "categories": [
      "Dokumentation",
      "Filme",
      "Medien & Unterhaltung"
    ],
    "sku": "2632341-A",
    "name": "Eine pornographische Beziehung",
    "url": "/medien-unterhaltung/filme/dokumentation/eine-pornographische-beziehung-02632341",
    "tags": [
      "Dokumentation",
      "Filme",
      "Medien & Unterhaltung"
    ],
    "l1_category_url": "/medien-unterhaltung",
    "l2_category_url": "/medien-unterhaltung/filme",
    "l3_category_url": "/medien-unterhaltung/filme/dokumentation",
    "brand": "Al!ve AG"
  },
  {
    "description": "CD - Stil: Hip-Hop - Tracks: 1. Inntrovaliv, 2. Wir Laufen Wie Stars, 3. Jung, Schön, Stylisch Feat.Justus, 4. Wer Sind Die Jungs Feat. Din Smexer, 5. Lustlos, 6. Select, 7. Ich Pay Deuce, 8. Fu Manalog, 9. Treues Geld, 10. Ziggi Digital Mode, 11. Synthiebank 83, 12. Eiskalt, 13. Wir, 14. Schöne Büros, 15. Wunderkind, 16. Outro, 17. Kein Style",
    "ean": "4041054802031",
    "price": 1990,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/72/cc/1b/72cc1b1700ef1f4236e8abe9a3f67228.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/72/cc/1b/72cc1b1700ef1f4236e8abe9a3f67228.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/72/cc/1b/72cc1b1700ef1f4236e8abe9a3f67228.50x50.jpg"
    },
    "id": 2758891,
    "categories": [
      "Hip Hop & Rap",
      "Musik",
      "Medien & Unterhaltung"
    ],
    "sku": "2571310-A",
    "name": "Prinz Porno (Prinz Pi) - Blackbook 2",
    "url": "/medien-unterhaltung/musik/hip-hop-rap/prinz-porno-prinz-pi-blackbook-2-02571310",
    "tags": [
      "Hip Hop & Rap",
      "Medien & Unterhaltung",
      "Musik"
    ],
    "l1_category_url": "/medien-unterhaltung",
    "l2_category_url": "/medien-unterhaltung/musik",
    "l3_category_url": "/medien-unterhaltung/musik/hip-hop-rap",
    "brand": "royab cd"
  },
  {
    "description": "CD - Stil: Hip-Hop - Tracks: 1. La Colere Des Dieux, 2. Dieux Dans L'arene, 3. Boumbadaboumclickboumtchikitakbooyabouctcha, 4. Maria, 5. J'suis Hostile, 6. Tire Tize, 7. Vous Etes Chauds, 8. Portos Ricos, 9. Ils Sont Dangereux, 10. Pas De Limite, 11. Le Clan Des Portugais, 12. Un Tour Sur L'avenue, 13. Les Pires Fils, 14. Arme D'un Micro J'tailee, 15. O Emigrante, 16. Dedicace",
    "ean": "3700409808586",
    "price": 2290,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/b6/cb/03/b6cb0306dabd17484ebd73688508f62a.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/b6/cb/03/b6cb0306dabd17484ebd73688508f62a.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/b6/cb/03/b6cb0306dabd17484ebd73688508f62a.50x50.jpg"
    },
    "id": 1836404,
    "categories": [
      "Hip Hop & Rap",
      "Musik",
      "Medien & Unterhaltung"
    ],
    "sku": "839910-A",
    "name": "La Harissa - Portos Ricos",
    "url": "/medien-unterhaltung/musik/hip-hop-rap/la-harissa-portos-ricos-0839910",
    "tags": [
      "Hip Hop & Rap",
      "Medien & Unterhaltung",
      "Musik"
    ],
    "l1_category_url": "/medien-unterhaltung",
    "l2_category_url": "/medien-unterhaltung/musik",
    "l3_category_url": "/medien-unterhaltung/musik/hip-hop-rap",
    "brand": "invcd"
  },
  {
    "description": "Perversion im Klassenzimmer<br> <br> <strong>Zusammenfassung:</strong><br> Grosse JF-TV-Dokumentation, ein Film von Marco Pino<br> <br> Viele Menschen glauben, dass Gender Mainstreaming nur ein neuer Begriff für Emanzipation und Gleichberechtigung der Frau sei. Ein fundamentaler Irrtum von den Schöpfern dieses Begriffes so gewollt! Gender stellt auch die normale Beziehung zwischen Mann und Frau als sexistische Unterdrückung dar. Das Modell Ehe und Familie wird aktiv in Frage gestellt, alles ist möglich. Gender Mainstreaming stellt unsere Gesellschaft auf den Kopf: Keine persönliche Identität, keine familiäre Bindung, keine gesellschaftliche Solidarität: <br> Der einzelne im Mittelpunkt bei totaler sexueller Freiheit. <br> <br> Kinder sind leicht zu manipulieren. Das machen sich die Gender-Ideologen zunutze und verankern sexuelle Vielfalt in den Bildungsplänen der Bundesländer. Sexuelle Vielfalt im Lehrplan will nicht aufklären, sondern gezielt die Frühsexualität fördern.<br> <br> 1. Hauptfilm: Perversion im Klassenzimmer, ca. 52 min.<br> 2. Kommentar von JF-Chefredakteur Dieter Stein, ca. 5 min.<br> 3. Gender-Gaga: Publizistin Birgit Kelle auf der Leipziger Buchmesse 2015, ca. 45 min.<br> <br> <strong>Autor:</strong> Pino, Marco <br> <table><tr> <td>Ausgabekennzeichen</td> <td>Deutsch</td> </tr><tr> <td>Masse</td> <td>H10.3 cm x B2.3 cm x D0.5 cm 24 g</td> </tr><tr> <td>Erscheinungsjahr</td> <td>2016</td> </tr><tr> <td>Einband</td> <td>Video</td> </tr><tr> <td>EAN</td> <td>9783929886610</td> </tr><tr> <td>ISBN</td> <td>978-3-929886-61-0</td> </tr></table><br> <br>",
    "ean": "9783929886610",
    "price": 1390,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/fa/c1/d4/fac1d4cdfd0040950ff8fc51b678d9ca.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/fa/c1/d4/fac1d4cdfd0040950ff8fc51b678d9ca.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/fa/c1/d4/fac1d4cdfd0040950ff8fc51b678d9ca.50x50.jpg"
    },
    "id": 3067634,
    "categories": [
      "Dokumentation",
      "Filme",
      "Medien & Unterhaltung"
    ],
    "sku": "2892250-A",
    "name": "Porno, Peitsche, Pädophilie",
    "url": "/medien-unterhaltung/filme/dokumentation/porno-peitsche-paedophilie-02892250",
    "tags": [
      "Dokumentation",
      "Filme",
      "Medien & Unterhaltung"
    ],
    "l1_category_url": "/medien-unterhaltung",
    "l2_category_url": "/medien-unterhaltung/filme",
    "l3_category_url": "/medien-unterhaltung/filme/dokumentation",
    "brand": "Junge Freiheit Verlag"
  },
  {
    "description": "CD - Stil: Hip-Hop - Tracks: 1. Erstes Element, 2. Picknick Im Park (Rap Ist Pt.1), 3. Herren Der Welt, 4. 23 (Rap Ist Pt.2) - Feat.Joker,Kobra,Smx,Asek, 5. Wake Up, 6. Morgens, 7. Nachtaktion - Feat.Kobra,Smx,B.A.D, 8. H Eiskalt, 9. Skitt, 10. Hightech Rapclick, 11. 20.000 Meilen, 12. Einefam (Rap Ist Pt.3) - Feat.Kobra,Smx, 13. Redoxreaktion, 14. 4Er Raps - Feat.Kobra,Smx,Ro, 15. Wir Kommen Wieder - Feat.Kobra,Smx, 16. Bondbeat, 17. Blind - Feat.Kobra,Smx, 18. Mooglove",
    "ean": "4041054802017",
    "price": 1990,
    "images": {
      "highres": "https://cdn.siroop.ch/media/images/sized/29/7b/4c/297b4c645661123475c9b82934035974.400x400.jpg",
      "lowres": "https://cdn.siroop.ch/media/images/sized/29/7b/4c/297b4c645661123475c9b82934035974.200x200.jpg",
      "thumbnails": "https://cdn.siroop.ch/media/images/sized/29/7b/4c/297b4c645661123475c9b82934035974.50x50.jpg"
    },
    "id": 2752988,
    "categories": [
      "Hip Hop & Rap",
      "Musik",
      "Medien & Unterhaltung"
    ],
    "sku": "2571311-A",
    "name": "Prinz Porno (Prinz Pi) - Radiumreaktion",
    "url": "/medien-unterhaltung/musik/hip-hop-rap/prinz-porno-prinz-pi-radiumreaktion-02571311",
    "tags": [
      "Hip Hop & Rap",
      "Medien & Unterhaltung",
      "Musik"
    ],
    "l1_category_url": "/medien-unterhaltung",
    "l2_category_url": "/medien-unterhaltung/musik",
    "l3_category_url": "/medien-unterhaltung/musik/hip-hop-rap",
    "brand": "royab cd"
  }
]

@csrf_exempt
def recommendations(request):
    return JsonResponse(mock)