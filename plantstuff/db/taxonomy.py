"""Taxonomy, naming categories."""

from marshmallow import Schema, fields
from marshmallow import validate


PLANT_CATEGORY = [
    "dicot",
    "fern",
    "green alga",
    "gymnosperm",
    "hornwort",
    "horsetail",
    "lichen",
    "liverwort",
    "lycopod",
    "monocot",
    "moss",
    "quillwort",
    "red algae",
    "whisk-fern",
]
PLANT_GENUSES = []
PLANT_SUBCLASSES = [
    "alismatidae",
    "andreaeidae",
    "arecidae",
    "bryidae",
    "caryophyllidae",
    "commelinidae",
    "dilleniidae",
    "hamamelididae",
    "jungermanniae",
    "liliidae",
    "magnoliidae",
    "marchantiae",
    "rosidae",
    "sphagnidae",
    "zingiberidae",
]
PLANT_CLASSES = [
    "andreaeopsida",
    "anthocerotopsida",
    "ascomycetes",
    "basidiomycetes",
    "bryopsida",
    "chlorophyceae",
    "cycadopsida",
    "equisetopsida",
    "filicopsida",
    "florideophyceae",
    "ginkgoopsida",
    "gnetopsida",
    "hepaticopsida",
    "liliopsida",
    "lycopodiopsida",
    "magnoliopsida",
    "pinopsida",
    "psilopsida",
    "sphagnopsida",
    "ulvophyceae",
    "ustomycetes",
]
PLANT_SUPERDIVISIONS = [
    "spermatophyta",
]
PLANT_SUBDIVISIONS = [
    "anthocerotae",
    "hepaticae",
    "musci",
]
PLANT_SUBKINGDOMS = ["tracheobionta"]
PLANT_KINGDOMS = [
    "plantae",
    "fungi",
]
PLANT_DIVISIONS = [
    "anthocerotophyta",
    "ascomycota",
    "basidiomycota",
    "bryophyta",
    "chlorophyta",
    "coniferophyta",
    "cycadophyta",
    "equisetophyta",
    "ginkgophyta",
    "gnetophyta",
    "hepaticophyta",
    "lycopodiophyta",
    "magnoliophyta",
    "mitosporic fungi",
    "psilophyta",
    "pteridophyta",
    "rhodophyta",
]
PLANT_ORDERS = [
    "agaricales",
    "alismatales",
    "andreaeales",
    "andreaeobryales",
    "anthocerotales",
    "apiales",
    "arales",
    "archidiales",
    "arecales",
    "aristolochiales",
    "arthoniales",
    "asterales",
    "atractiellales",
    "batales",
    "bromeliales",
    "bryales",
    "buxbaumiales",
    "caliciales",
    "callitrichales",
    "calobryales",
    "calycerales",
    "campanulales",
    "cantharellales",
    "capnodiales",
    "capparales",
    "caryophyllales",
    "casuarinales",
    "caulerpales",
    "celastrales",
    "commelinales",
    "cornales",
    "cycadales",
    "cyclanthales",
    "cyperales",
    "diapensiales",
    "dicranales",
    "dilleniales",
    "dipsacales",
    "dothideales",
    "ebenales",
    "ephedrales",
    "equisetales",
    "ericales",
    "eriocaulales",
    "euphorbiales",
    "eurotiales",
    "fabales",
    "fagales",
    "fissidentales",
    "funariales",
    "gentianales",
    "geraniales",
    "ginkgoales",
    "gnetales",
    "gracilariales",
    "graphidales",
    "grimmiales",
    "gyalectales",
    "haloragales",
    "halymeniales",
    "hamamelidales",
    "hookeriales",
    "hydrocharitales",
    "hydropteridales",
    "hypnales",
    "hypocreales",
    "illiciales",
    "isobryales",
    "isoetales",
    "juglandales",
    "juncales",
    "jungermanniales",
    "lamiales",
    "laurales",
    "lecanorales",
    "lecythidales",
    "leitneriales",
    "leotiales",
    "leucodontales",
    "lichinales",
    "liliales",
    "linales",
    "lycopodiales",
    "magnoliales",
    "malvales",
    "marattiales",
    "marchantiales",
    "melanommatales",
    "metzgeriales",
    "myricales",
    "myrtales",
    "najadales",
    "nepenthales",
    "nymphaeales",
    "onygenales",
    "opegraphales",
    "ophioglossales",
    "orchidales",
    "orthotrichales",
    "ostropales",
    "pandanales",
    "papaverales",
    "patellariales",
    "peltigerales",
    "pertusariales",
    "phyllachorales",
    "pinales",
    "piperales",
    "plantaginales",
    "platygloeales",
    "pleosporales",
    "plumbaginales",
    "podostemales",
    "polygalales",
    "polygonales",
    "polypodiales",
    "polytrichales",
    "pottiales",
    "primulales",
    "proteales",
    "psilotales",
    "pyrenulales",
    "rafflesiales",
    "ranunculales",
    "restionales",
    "rhamnales",
    "rhizophorales",
    "rosales",
    "rubiales",
    "salicales",
    "santalales",
    "sapindales",
    "schistostegiales",
    "scrophulariales",
    "selaginellales",
    "seligerales",
    "solanales",
    "sordariales",
    "sphaeriales",
    "sphaerocarpales",
    "sphagnales",
    "stereales",
    "taxales",
    "teloschistales",
    "tetraphidales",
    "theales",
    "tremellales",
    "triuridales",
    "typhales",
    "ulvales",
    "urticales",
    "verrucariales",
    "violales",
    "zingiberales",
]
PLANT_COMMON_FAMILY_NAMES = [
    "acanthus",
    "achatocarpus",
    "adder's-tongue",
    "aloe",
    "amaranth",
    "araucaria",
    "arrow-grass",
    "arum",
    "aster",
    "azolla",
    "balanophora",
    "banana",
    "barbados cherry",
    "barberry",
    "basella",
    "bayberry",
    "beech",
    "begonia",
    "bellflower",
    "birch",
    "bird of paradise flower",
    "birthwort",
    "bittersweet",
    "bladdernut",
    "bladderwort",
    "bloodwort",
    "borage",
    "boxwood",
    "bracken fern",
    "brazil-nut",
    "bromeliad",
    "broom-rape",
    "brunellia",
    "buckbean",
    "buckthorn",
    "buckwheat",
    "burmannia",
    "bur-reed",
    "buttercup",
    "butterfly-bush",
    "cacao",
    "cactus",
    "calamus",
    "calycera",
    "canella",
    "canna",
    "cannarus",
    "cape-pondweed",
    "caper",
    "carpet-weed",
    "carrot",
    "catbrier",
    "catkin-mistletoe",
    "cat-tail",
    "cecropia",
    "century-plant",
    "chain fern",
    "chinese gooseberry",
    "chloranthus",
    "christmas mistletoe",
    "clethra",
    "climbing fern",
    "club-moss",
    "coca",
    "cocoa-plum",
    "corkwood",
    "costus",
    "creosote-bush",
    "crossosoma",
    "crowberry",
    "cucumber",
    "cunonia",
    "curly-grass",
    "currant",
    "custard-apple",
    "cycad",
    "cypress",
    "cyrilla",
    "datisca",
    "diamond-leaf fern",
    "diapensia",
    "dillenia",
    "ditch-grass",
    "dodder",
    "dogbane",
    "dogwood",
    "duckweed",
    "east indian pitcher-plant",
    "ebony",
    "eel-grass",
    "elaeocarpus",
    "elm",
    "epacris",
    "evening primrose",
    "fig-marigold",
    "figwort",
    "filmy fern",
    "flacourtia",
    "flagellaria",
    "flax",
    "floating fern",
    "flowering fern",
    "flowering rush",
    "forking fern",
    "four o'clock",
    "frankenia",
    "frankincense",
    "fumitory",
    "gentian",
    "geranium",
    "gesneriad",
    "ginger",
    "ginkgo",
    "ginseng",
    "gnetum",
    "goodenia",
    "goosefoot",
    "grape",
    "grass",
    "greyia",
    "gunnera",
    "hanging fern",
    "hanguana",
    "heath",
    "heliconia",
    "hemp",
    "hernandia",
    "hippocratea",
    "holly",
    "honeysuckle",
    "horned pondweed",
    "hornwort",
    "horse-chestnut",
    "horse-radish tree",
    "horsetail",
    "hydrangea",
    "icacina",
    "indian almond",
    "indian pipe",
    "iris",
    "joinvillea",
    "jojoba",
    "kapok-tree",
    "karaka",
    "katsura-tree",
    "kihi fern",
    "krameria",
    "lardizabala",
    "laurel",
    "leadwort",
    "lennoa",
    "lily",
    "linden",
    "lipstick-tree",
    "lizard's-tail",
    "loasa",
    "logania",
    "loosestrife",
    "lotus-lily",
    "madder",
    "magnolia",
    "mahogany",
    "maidenhair fern",
    "mallow",
    "manatee-grass",
    "mangosteen",
    "maple",
    "mare's-tail",
    "marsh fern",
    "mayaca",
    "meadow-foam",
    "melastome",
    "melianthus",
    "meranti",
    "mezereum",
    "mignonette",
    "milkweed",
    "milkwort",
    "mint",
    "monimia",
    "moonseed",
    "mormon-tea",
    "morning-glory",
    "moschatel",
    "mulberry",
    "mustard",
    "myoporum",
    "myrsine",
    "myrtle",
    "nasturtium",
    "nettle",
    "nutmeg",
    "ochna",
    "ocotillo",
    "olax",
    "oleaster",
    "olive",
    "orchid",
    "palm",
    "panama hat",
    "papaya",
    "passion-flower",
    "pea",
    "peony",
    "pepper",
    "philydraceae",
    "phlox",
    "pine",
    "pink",
    "pipewort",
    "pitcher-plant",
    "pittosporum",
    "plane-tree",
    "plantain",
    "plum yew",
    "podocarpus",
    "pokeweed",
    "polypody",
    "pomegranate",
    "pondweed",
    "poppy",
    "posidonia",
    "potato",
    "prayer-plant",
    "primrose",
    "protea",
    "purslane",
    "quassia",
    "quillwort",
    "rafflesia",
    "red mangrove",
    "river-weed",
    "rock-rose",
    "rose",
    "royal fern",
    "rue",
    "rush",
    "sabia",
    "sago-palm",
    "saltwort",
    "sandalwood",
    "sapodilla",
    "saxifrage",
    "scheuchzeria",
    "schisandra",
    "screw-pine",
    "sedge",
    "sesame",
    "she-oak",
    "shingle plant",
    "shinleaf",
    "shoestring fern",
    "showy mistletoe",
    "silk tassel",
    "soapberry",
    "sonneratia",
    "souari",
    "spenoclea",
    "spiderwort",
    "spike-moss",
    "spleenwort",
    "spurge",
    "stackhousia",
    "star-anise",
    "stemona",
    "stonecrop",
    "storax",
    "strawberry-shrub",
    "sumac",
    "sundew",
    "suriana",
    "sweetleaf",
    "tacca",
    "tamarix",
    "tape-grass",
    "tea",
    "teasel",
    "theophrasta",
    "touch-me-not",
    "tree fern",
    "tree fern",
    "triurus",
    "trumpet-creeper",
    "turnera",
    "valerian",
    "verbena",
    "vessel fern",
    "violet",
    "walnut",
    "water chestnut",
    "water fern",
    "water milfoil",
    "water-clover",
    "water-hyacinth",
    "waterleaf",
    "water-lily",
    "water-nymph",
    "water-plantain",
    "water-poppy",
    "water-shield",
    "water-starwort",
    "waterwort",
    "whisk-fern",
    "willow",
    "wintera",
    "witch-hazel",
    "wood fern",
    "wood-sorrel",
    "yam",
    "yellow-eyed grass",
    "yew",
]
FAMILY_SYMBOLS = [
    "acanth",
    "acaros",
    "acerac",
    "achato",
    "acorac",
    "acrobo",
    "actini",
    "adeloc",
    "adoxac",
    "agavac",
    "agyria",
    "aizoac",
    "alecto",
    "alisma",
    "alliso",
    "aloace",
    "amaran",
    "amblys",
    "anacar",
    "andrea",
    "andrea2",
    "anemia",
    "aneura",
    "annona",
    "anomod",
    "anthel",
    "anthoc",
    "apiace",
    "apocyn",
    "aponog",
    "aquifo",
    "aracea",
    "aralia",
    "arauca",
    "archid",
    "arctom",
    "arecac",
    "aristo",
    "arnell",
    "arthon",
    "arthop",
    "arthro",
    "asclep",
    "asplen",
    "astera",
    "astero",
    "atheli",
    "aulaco",
    "aytoni",
    "azolla",
    "bacidi",
    "baeomy",
    "balano",
    "balsam",
    "bartra",
    "basell",
    "batace",
    "begoni",
    "berber",
    "betula",
    "biator",
    "bignon",
    "bixace",
    "blasia",
    "blechn",
    "bombac",
    "boragi",
    "brachy",
    "brassi",
    "brigan",
    "bromel",
    "bruchi",
    "brunel",
    "bryace",
    "bryoxi",
    "buddle",
    "burman",
    "burser",
    "butoma",
    "buxace",
    "buxbau",
    "cabomb",
    "cactac",
    "calici",
    "callic",
    "callit",
    "calyca",
    "calyce",
    "calymp",
    "calypo",
    "campan",
    "candel",
    "canell",
    "cannab",
    "cannac",
    "capnod",
    "cappar",
    "caprif",
    "carica",
    "caryoc",
    "caryop",
    "casuar",
    "catill",
    "catosc",
    "cauler",
    "cecrop",
    "celast",
    "cephal",
    "cephal2",
    "cephal3",
    "cerato",
    "cercid",
    "chenop",
    "chiono",
    "chlora",
    "chonec",
    "chryso",
    "chryso2",
    "cistac",
    "cladon",
    "clavar",
    "clethr",
    "clevea",
    "climac",
    "clusia",
    "coccoc",
    "coccot",
    "collem",
    "combre",
    "commel",
    "conioc",
    "connar",
    "conoce",
    "convol",
    "cornac",
    "corsin",
    "cortic",
    "coryno",
    "costac",
    "crassu",
    "crocyn",
    "crosso",
    "crypha",
    "cucurb",
    "cunoni",
    "cupres",
    "cuscut",
    "cyathe",
    "cycada",
    "cyclan",
    "cymodo",
    "cypera",
    "cyrill",
    "dacamp",
    "dactyl",
    "dalton",
    "datisc",
    "davall",
    "dendro",
    "dennst",
    "diapen",
    "dickso",
    "dicran",
    "dillen",
    "diosco",
    "dipsac",
    "dipter",
    "discel",
    "ditric",
    "droser",
    "dryopt",
    "ebenac",
    "ectole",
    "eigler",
    "elaeag",
    "elaeoc",
    "elatin",
    "empetr",
    "encaly",
    "entodo",
    "epacri",
    "ephedr",
    "epheme",
    "equise",
    "eremol",
    "ericac",
    "erioca",
    "erpodi",
    "erythr",
    "euphor",
    "fabace",
    "fabron",
    "fagace",
    "fissid",
    "flacou",
    "flagel",
    "fontin",
    "fossom",
    "fouqui",
    "franke",
    "fumari",
    "funari",
    "fuscid",
    "garrya",
    "gentia",
    "geocal",
    "gerani",
    "gesner",
    "gigasp",
    "ginkgo",
    "gleich",
    "gnetac",
    "gomphi",
    "gooden",
    "gracil",
    "grammi",
    "graphi",
    "greyia",
    "grimmi",
    "grossu",
    "gunner",
    "gyalec",
    "gymnom",
    "gypsop",
    "gyroth",
    "haemat",
    "haemod",
    "halora",
    "halyme",
    "hamame",
    "hangua",
    "haplom",
    "hedwig",
    "helico",
    "helodi",
    "heppia",
    "herber",
    "hernan",
    "hippoc",
    "hippoc2",
    "hippur",
    "hooker",
    "hydran",
    "hydroc",
    "hydrop",
    "hyloco",
    "hymene",
    "hymeno",
    "hypnac",
    "hypocr",
    "hypopt",
    "icacin",
    "illici",
    "iridac",
    "isoeta",
    "joinvi",
    "jubula",
    "juglan",
    "juncac",
    "juncag",
    "junger",
    "kramer",
    "lamiac",
    "lardiz",
    "laurac",
    "lecano",
    "lecide",
    "lecyth",
    "leitne",
    "lejeun",
    "lemnac",
    "lennoa",
    "lentib",
    "leotia",
    "lepido",
    "leptod",
    "leskea",
    "letrou",
    "leucob",
    "leucod",
    "lichen",
    "lichin",
    "liliac",
    "limnan",
    "limnoc",
    "linace",
    "loasac",
    "lobari",
    "logani",
    "lophos",
    "lorant",
    "lunula",
    "lycopo",
    "lygodi",
    "lythra",
    "magnol",
    "malpig",
    "malvac",
    "marant",
    "maratt",
    "marcgr",
    "marcha",
    "marsil",
    "mastig",
    "mastod",
    "mayaca",
    "meesia",
    "megalo",
    "melano",
    "melasp",
    "melast",
    "meliac",
    "melian",
    "menisp",
    "menyan",
    "mesopt",
    "meteor",
    "metzge",
    "micare",
    "microc",
    "mniace",
    "mollug",
    "monimi",
    "monobl",
    "monoso",
    "monotr",
    "morace",
    "moring",
    "musace",
    "mycobl",
    "mycoca",
    "mycopo",
    "mycosp",
    "myopor",
    "myrica",
    "myrini",
    "myrist",
    "myrsin",
    "myrtac",
    "myxotr",
    "najada",
    "necker",
    "nelumb",
    "nepent",
    "nephro",
    "nototh",
    "nyctag",
    "nympha",
    "ochnac",
    "odonto",
    "oedipo",
    "olacac",
    "oleace",
    "onagra",
    "opegra",
    "ophiog",
    "ophiop",
    "orchid",
    "oroban",
    "orthot",
    "osmund",
    "oxalid",
    "oxymit",
    "paeoni",
    "pallav",
    "pandan",
    "pannar",
    "papave",
    "parker",
    "parmel",
    "passif",
    "pedali",
    "pellia",
    "peltig",
    "peltul",
    "pertus",
    "philyd",
    "phlyct",
    "phylla",
    "physci",
    "phytol",
    "piloca",
    "pinace",
    "pipera",
    "pittos",
    "placyn",
    "plagio",
    "plagio2",
    "planta",
    "platan",
    "platyg",
    "pleoma",
    "pleosp",
    "pleuro",
    "pleuro2",
    "plumba",
    "poacea",
    "podoca",
    "podost",
    "polemo",
    "polyga",
    "polygo",
    "polypo",
    "polytr",
    "ponted",
    "porell",
    "porpid",
    "portul",
    "posido",
    "potamo",
    "pottia",
    "primul",
    "protea",
    "protot",
    "pseudo",
    "pseudo2",
    "psilot",
    "psorac",
    "pterid",
    "pterig",
    "pterob",
    "ptilid",
    "ptycho",
    "punica",
    "pyreno",
    "pyrenu",
    "pyrola",
    "racopi",
    "radula",
    "raffle",
    "ramali",
    "ranunc",
    "reseda",
    "rhachi",
    "rhamna",
    "rhizoc",
    "rhizog",
    "rhizop",
    "rhytid",
    "riccia",
    "riella",
    "rimula",
    "roccel",
    "rosace",
    "rubiac",
    "ruppia",
    "rutace",
    "sabiac",
    "salica",
    "salvin",
    "santal",
    "sapind",
    "sapota",
    "sarrac",
    "saurur",
    "saxifr",
    "scapan",
    "schaer",
    "scheuc",
    "schisa",
    "schist",
    "schiza",
    "scoule",
    "scroph",
    "selagi",
    "selige",
    "semato",
    "simaro",
    "simmon",
    "smilac",
    "solana",
    "solori",
    "sonner",
    "sparga",
    "sphaer",
    "sphaer2",
    "sphagn",
    "spheno",
    "sphinc",
    "splach",
    "splach2",
    "stackh",
    "staphy",
    "stemon",
    "stercu",
    "stereo",
    "stereo2",
    "sticti",
    "streli",
    "strigu",
    "styrac",
    "surian",
    "symplo",
    "syzygo",
    "taccac",
    "tamari",
    "targio",
    "taxace",
    "telosc",
    "tetrap",
    "thamno",
    "theace",
    "thelen",
    "thelia",
    "thelot",
    "thelyp",
    "theoph",
    "thromb",
    "thuidi",
    "thymel",
    "tiliac",
    "timmia",
    "trapac",
    "trapel",
    "tremel",
    "treubi",
    "tricho",
    "tricho2",
    "tricho3",
    "tricho4",
    "triuri",
    "tropae",
    "trypet",
    "turner",
    "typhac",
    "ulmace",
    "ulvace",
    "umbili",
    "uncerta",
    "uncertb",
    "urtica",
    "valeri",
    "verben",
    "verruc",
    "vezdae",
    "violac",
    "viscac",
    "vitace",
    "vittar",
    "winter",
    "xyrida",
    "zamiac",
    "zannic",
    "zingib",
    "zoster",
    "zygoph",
]
FAMILY = [
    "acanthaceae",
    "acarosporaceae",
    "aceraceae",
    "achatocarpaceae",
    "acoraceae",
    "acrobolbaceae",
    "actinidiaceae",
    "adelococcaceae",
    "adoxaceae",
    "agavaceae",
    "agyriaceae",
    "aizoaceae",
    "alectoriaceae",
    "alismataceae",
    "allisoniaceae",
    "aloaceae",
    "amaranthaceae",
    "amblystegiaceae",
    "anacardiaceae",
    "andreaeaceae",
    "andreaeobryaceae",
    "anemiaceae",
    "aneuraceae",
    "annonaceae",
    "anomodontaceae",
    "antheliaceae",
    "anthocerotaceae",
    "apiaceae",
    "apocynaceae",
    "aponogetonaceae",
    "aquifoliaceae",
    "araceae",
    "araliaceae",
    "araucariaceae",
    "archidiaceae",
    "arctomiaceae",
    "arecaceae",
    "aristolochiaceae",
    "arnelliaceae",
    "arthoniaceae",
    "arthopyreniaceae",
    "arthrorhaphidaceae",
    "asclepiadaceae",
    "aspleniaceae",
    "asteraceae",
    "asterothyriaceae",
    "atheliaceae",
    "aulacomniaceae",
    "aytoniaceae",
    "azollaceae",
    "bacidiaceae",
    "baeomycetaceae",
    "balanophoraceae",
    "balsaminaceae",
    "bartramiaceae",
    "basellaceae",
    "bataceae",
    "begoniaceae",
    "berberidaceae",
    "betulaceae",
    "biatorellaceae",
    "bignoniaceae",
    "bixaceae",
    "blasiaceae",
    "blechnaceae",
    "bombacaceae",
    "boraginaceae",
    "brachytheciaceae",
    "brassicaceae",
    "brigantiaceae",
    "bromeliaceae",
    "bruchiaceae",
    "brunelliaceae",
    "bryaceae",
    "bryoxiphiaceae",
    "buddlejaceae",
    "burmanniaceae",
    "burseraceae",
    "butomaceae",
    "buxaceae",
    "buxbaumiaceae",
    "cabombaceae",
    "cactaceae",
    "caliciaceae",
    "callicostaceae",
    "callitrichaceae",
    "calycanthaceae",
    "calyceraceae",
    "calymperaceae",
    "calypogeiaceae",
    "campanulaceae",
    "candelariaceae",
    "canellaceae",
    "cannabaceae",
    "cannaceae",
    "capnodiaceae",
    "capparaceae",
    "caprifoliaceae",
    "caricaceae",
    "caryocaraceae",
    "caryophyllaceae",
    "casuarinaceae",
    "catillariaceae",
    "catoscopiaceae",
    "caulerpaceae",
    "cecropiaceae",
    "celastraceae",
    "cephalotaxaceae",
    "cephaloziaceae",
    "cephaloziellaceae",
    "ceratophyllaceae",
    "cercidiphyllaceae",
    "chenopodiaceae",
    "chionosphaeraceae",
    "chloranthaceae",
    "chonecoleaceae",
    "chrysobalanaceae",
    "chrysotrichaceae",
    "cistaceae",
    "cladoniaceae",
    "clavariaceae",
    "clethraceae",
    "cleveaceae",
    "climaciaceae",
    "clusiaceae",
    "coccocarpiaceae",
    "coccotremataceae",
    "collemataceae",
    "combretaceae",
    "commelinaceae",
    "coniocybaceae",
    "connaraceae",
    "conocephalaceae",
    "convolvulaceae",
    "cornaceae",
    "corsiniaceae",
    "corticiaceae",
    "corynocarpaceae",
    "costaceae",
    "crassulaceae",
    "crocyniaceae",
    "crossosomataceae",
    "cryphaeaceae",
    "cucurbitaceae",
    "cunoniaceae",
    "cupressaceae",
    "cuscutaceae",
    "cyatheaceae",
    "cycadaceae",
    "cyclanthaceae",
    "cymodoceaceae",
    "cyperaceae",
    "cyrillaceae",
    "dacampiaceae",
    "dactylosporaceae",
    "daltoniaceae",
    "datiscaceae",
    "davalliaceae",
    "dendrocerotaceae",
    "dennstaedtiaceae",
    "diapensiaceae",
    "dicksoniaceae",
    "dicranaceae",
    "dilleniaceae",
    "dioscoreaceae",
    "dipsacaceae",
    "dipterocarpaceae",
    "disceliaceae",
    "ditrichaceae",
    "droseraceae",
    "dryopteridaceae",
    "ebenaceae",
    "ectolechiaceae",
    "eigleraceae",
    "elaeagnaceae",
    "elaeocarpaceae",
    "elatinaceae",
    "empetraceae",
    "encalyptaceae",
    "entodontaceae",
    "epacridaceae",
    "ephedraceae",
    "ephemeraceae",
    "equisetaceae",
    "eremolepidaceae",
    "ericaceae",
    "eriocaulaceae",
    "erpodiaceae",
    "erythroxylaceae",
    "euphorbiaceae",
    "fabaceae",
    "fabroniaceae",
    "fagaceae",
    "fissidentaceae",
    "flacourtiaceae",
    "flagellariaceae",
    "fontinalaceae",
    "fossombroniaceae",
    "fouquieriaceae",
    "frankeniaceae",
    "fumariaceae",
    "funariaceae",
    "fuscideaceae",
    "garryaceae",
    "gentianaceae",
    "geocalycaceae",
    "geraniaceae",
    "gesneriaceae",
    "gigaspermaceae",
    "ginkgoaceae",
    "gleicheniaceae",
    "gnetaceae",
    "gomphillaceae",
    "goodeniaceae",
    "gracilariaceae",
    "grammitidaceae",
    "graphidaceae",
    "greyiaceae",
    "grimmiaceae",
    "grossulariaceae",
    "gunneraceae",
    "gyalectaceae",
    "gymnomitriaceae",
    "gypsoplaceae",
    "gyrothyraceae",
    "haematommataceae",
    "haemodoraceae",
    "haloragaceae",
    "halymeniaceae",
    "hamamelidaceae",
    "hanguanaceae",
    "haplomitriaceae",
    "hedwigiaceae",
    "heliconiaceae",
    "helodiaceae",
    "heppiaceae",
    "herbertaceae",
    "hernandiaceae",
    "hippocastanaceae",
    "hippocrateaceae",
    "hippuridaceae",
    "hookeriaceae",
    "hydrangeaceae",
    "hydrocharitaceae",
    "hydrophyllaceae",
    "hylocomiaceae",
    "hymeneliaceae",
    "hymenophyllaceae",
    "hypnaceae",
    "hypocreaceae",
    "hypopterygiaceae",
    "icacinaceae",
    "illiciaceae",
    "iridaceae",
    "isoetaceae",
    "joinvilleaceae",
    "jubulaceae",
    "juglandaceae",
    "juncaceae",
    "juncaginaceae",
    "jungermanniaceae",
    "krameriaceae",
    "lamiaceae",
    "lardizabalaceae",
    "lauraceae",
    "lecanoraceae",
    "lecideaceae",
    "lecythidaceae",
    "leitneriaceae",
    "lejeuneaceae",
    "lemnaceae",
    "lennoaceae",
    "lentibulariaceae",
    "leotiaceae",
    "lepidoziaceae",
    "leptodontaceae",
    "leskeaceae",
    "letrouitiaceae",
    "leucobryaceae",
    "leucodontaceae",
    "lichenotheliaceae",
    "lichinaceae",
    "liliaceae",
    "limnanthaceae",
    "limnocharitaceae",
    "linaceae",
    "loasaceae",
    "lobariaceae",
    "loganiaceae",
    "lophosoriaceae",
    "loranthaceae",
    "lunulariaceae",
    "lycopodiaceae",
    "lygodiaceae",
    "lythraceae",
    "magnoliaceae",
    "malpighiaceae",
    "malvaceae",
    "marantaceae",
    "marattiaceae",
    "marcgraviaceae",
    "marchantiaceae",
    "marsileaceae",
    "mastigophoraceae",
    "mastodiaceae",
    "mayacaceae",
    "meesiaceae",
    "megalosporaceae",
    "melanommataceae",
    "melaspileaceae",
    "melastomataceae",
    "meliaceae",
    "melianthaceae",
    "menispermaceae",
    "menyanthaceae",
    "mesoptychiaceae",
    "meteoriaceae",
    "metzgeriaceae",
    "micareaceae",
    "microcaliciaceae",
    "mniaceae",
    "molluginaceae",
    "monimiaceae",
    "monoblastiaceae",
    "monosoleniaceae",
    "monotropaceae",
    "moraceae",
    "moringaceae",
    "musaceae",
    "mycoblastaceae",
    "mycocaliciaceae",
    "mycoporaceae",
    "mycosphaerellaceae",
    "myoporaceae",
    "myricaceae",
    "myriniaceae",
    "myristicaceae",
    "myrsinaceae",
    "myrtaceae",
    "myxotrichaceae",
    "najadaceae",
    "neckeraceae",
    "nelumbonaceae",
    "nepenthaceae",
    "nephromataceae",
    "notothyladaceae",
    "nyctaginaceae",
    "nymphaeaceae",
    "ochnaceae",
    "odontotremataceae",
    "oedipodiaceae",
    "olacaceae",
    "oleaceae",
    "onagraceae",
    "opegraphaceae",
    "ophioglossaceae",
    "ophioparmaceae",
    "orchidaceae",
    "orobanchaceae",
    "orthotrichaceae",
    "osmundaceae",
    "oxalidaceae",
    "oxymitraceae",
    "paeoniaceae",
    "pallaviciniaceae",
    "pandanaceae",
    "pannariaceae",
    "papaveraceae",
    "parkeriaceae",
    "parmeliaceae",
    "passifloraceae",
    "pedaliaceae",
    "pelliaceae",
    "peltigeraceae",
    "peltulaceae",
    "pertusariaceae",
    "philydraceae",
    "phlyctidaceae",
    "phyllachoraceae",
    "physciaceae",
    "phytolaccaceae",
    "pilocarpaceae",
    "pinaceae",
    "piperaceae",
    "pittosporaceae",
    "placynthiaceae",
    "plagiochilaceae",
    "plagiotheciaceae",
    "plantaginaceae",
    "platanaceae",
    "platygloeaceae",
    "pleomassariaceae",
    "pleosporaceae",
    "pleuroziaceae",
    "pleuroziopsidaceae",
    "plumbaginaceae",
    "poaceae",
    "podocarpaceae",
    "podostemaceae",
    "polemoniaceae",
    "polygalaceae",
    "polygonaceae",
    "polypodiaceae",
    "polytrichaceae",
    "pontederiaceae",
    "porellaceae",
    "porpidiaceae",
    "portulacaceae",
    "posidoniaceae",
    "potamogetonaceae",
    "pottiaceae",
    "primulaceae",
    "proteaceae",
    "protothelenellaceae",
    "pseudoditrichaceae",
    "pseudolepicoleaceae",
    "psilotaceae",
    "psoraceae",
    "pteridaceae",
    "pterigynandraceae",
    "pterobryaceae",
    "ptilidiaceae",
    "ptychomitriaceae",
    "punicaceae",
    "pyrenotrichaceae",
    "pyrenulaceae",
    "pyrolaceae",
    "racopilaceae",
    "radulaceae",
    "rafflesiaceae",
    "ramalinaceae",
    "ranunculaceae",
    "resedaceae",
    "rhachitheciaceae",
    "rhamnaceae",
    "rhizocarpaceae",
    "rhizogoniaceae",
    "rhizophoraceae",
    "rhytidiaceae",
    "ricciaceae",
    "riellaceae",
    "rimulariaceae",
    "roccellaceae",
    "rosaceae",
    "rubiaceae",
    "ruppiaceae",
    "rutaceae",
    "sabiaceae",
    "salicaceae",
    "salviniaceae",
    "santalaceae",
    "sapindaceae",
    "sapotaceae",
    "sarraceniaceae",
    "saururaceae",
    "saxifragaceae",
    "scapaniaceae",
    "schaereriaceae",
    "scheuchzeriaceae",
    "schisandraceae",
    "schistostegaceae",
    "schizaeaceae",
    "scouleriaceae",
    "scrophulariaceae",
    "selaginellaceae",
    "seligeriaceae",
    "sematophyllaceae",
    "simaroubaceae",
    "simmondsiaceae",
    "smilacaceae",
    "solanaceae",
    "solorinellaceae",
    "sonneratiaceae",
    "sparganiaceae",
    "sphaerocarpaceae",
    "sphaerophoraceae",
    "sphagnaceae",
    "sphenocleaceae",
    "sphinctrinaceae",
    "splachnaceae",
    "splachnobryaceae",
    "stackhousiaceae",
    "staphyleaceae",
    "stemonaceae",
    "sterculiaceae",
    "stereocaulaceae",
    "stereophyllaceae",
    "stictidaceae",
    "strelitziaceae",
    "strigulaceae",
    "styracaceae",
    "surianaceae",
    "symplocaceae",
    "syzygosporaceae",
    "taccaceae",
    "tamaricaceae",
    "targioniaceae",
    "taxaceae",
    "teloschistaceae",
    "tetraphidaceae",
    "thamnobryaceae",
    "theaceae",
    "thelenellaceae",
    "theliaceae",
    "thelotremataceae",
    "thelypteridaceae",
    "theophrastaceae",
    "thrombiaceae",
    "thuidiaceae",
    "thymelaeaceae",
    "tiliaceae",
    "timmiaceae",
    "trapaceae",
    "trapeliaceae",
    "tremellaceae",
    "treubiaceae",
    "trichocoleaceae",
    "trichocomaceae",
    "tricholomataceae",
    "trichotheliaceae",
    "triuridaceae",
    "tropaeolaceae",
    "trypetheliaceae",
    "turneraceae",
    "typhaceae",
    "ulmaceae",
    "ulvaceae",
    "umbilicariaceae",
    "urticaceae",
    "valerianaceae",
    "verbenaceae",
    "verrucariaceae",
    "vezdaeaceae",
    "violaceae",
    "viscaceae",
    "vitaceae",
    "vittariaceae",
    "winteraceae",
    "xyridaceae",
    "zamiaceae",
    "zannichelliaceae",
    "zingiberaceae",
    "zosteraceae",
    "zygophyllaceae",
]


class Category(Schema):
    """The plant category."""

    name = fields.Str(required=True,
                      validate=validate.OneOf(PLANT_CATEGORY))


class Class(Schema):
    """The plant class."""

    name = fields.Str(required=True,
                      validate=validate.OneOf(PLANT_CLASSES))


class Cultivar(Schema):
    """The plant cultivar."""

    name = fields.Str(required=True)
    common_name = fields.Str(required=True)
    description = fields.Str()

    # Maybe?
    # flower_colors = fields.List(fields.Str)


class Division(Schema):
    """The plant division."""

    name = fields.Str(required=True,
                      validate=validate.OneOf(PLANT_DIVISIONS))


class Family(Schema):
    """The plant family."""

    name = fields.Str(required=True,
                      validate=validate.OneOf(PLANT_COMMON_FAMILY_NAMES))


class Genus(Schema):
    """The plant genus."""

    name = fields.Str(required=True,
                      validate=validate.OneOf(PLANT_GENUSES))


class Order(Schema):
    """The plant order."""

    name = fields.Str(required=True,
                      validate=validate.OneOf(PLANT_ORDERS))


class Subdivision(Schema):
    """The plant subdivision."""

    name = fields.Str(required=True,
                      validate=validate.OneOf(PLANT_SUBDIVISIONS))


class Superdivision(Schema):
    """The plant subdivision."""

    name = fields.Str(required=True,
                      validate=validate.OneOf(PLANT_SUPERDIVISIONS))


class SubKingdom(Schema):
    """The plant subkingdom."""

    name = fields.Str(required=True,
                      validate=validate.OneOf(PLANT_SUBKINGDOMS))


class Kingdom(Schema):
    """The plant kingdom."""

    name = fields.Str(required=True,
                      validate=validate.OneOf(PLANT_KINGDOMS))
