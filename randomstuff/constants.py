BASE_URL = "https://api.pgamerx.com"

IMAGE_TYPES = [
    "aww",
    "duck",
    "dog",
    "cat",
    "memes",
    "dankmemes",
    "holup",
    "art",
    "harrypottermemes",
    "facepalm",
]
JOKE_TYPES = ["any", "dev", "spooky", "pun"]
WAIFU_TYPES = ["waifu", "neko", "shinobu", "megumin", "bully", "cuddle"]

PLANS = ["", "pro", "ultra", "biz", "mega"]  # Order lowest -> highest

VERSIONS = ["3", "4", "5"]
DISCONTINUED_VERSIONS = ["2"]  # Order: oldest -> newest

SERVERS_V4 = ["primary", "backup", "unstable"]
SERVERS_V5 = ["main", "backup"]

ONE_IMAGE_METHODS = [
    "affect",
    "beautiful",
    "wanted",
    "delete",
    "trigger",
    "facepalm",
    "blur",
    "hitler",
    # "kiss", # API Actually expects two image even tho the docs say 1
    "jail",
    "invert",
    "jokeOverHead",
]

TWO_IMAGE_METHODS = ["bed", "fuse", "kiss", "slap", "spank"]

THREE_IMAGE_METHODS = ["distracted"]

FOUR_IMAGE_METHODS = ["changemymind"]
