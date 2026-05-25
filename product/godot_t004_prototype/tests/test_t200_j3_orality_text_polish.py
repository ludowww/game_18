#!/usr/bin/env python3
"""T200: text-only J3 V2 orality polish stays scoped and keeps player choice text mirrored."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

REPLACEMENTS = {
    "sarah_j3_v2_experimental.json": [
        ("Mais le temps, pour toi, c’est parfois un endroit où tu peux respirer.", "Mais quand tu demandes du temps, toi, ça te laisse respirer."),
        ("Pour moi, c’est un endroit où j’attends.", "Moi, pendant ce temps-là, j’attends."),
        ("Et je ne sais pas combien de fois je peux accepter que mon malaise soit trop grand pour ta version.", "Et je sais pas combien de fois je peux entendre que mon malaise est trop grand pour ta version."),
        ("Hier, ta phrase la moins solide était peut-être celle qui m’a le moins abîmée.", "Hier, bizarrement, c’est ta phrase la plus fragile qui m’a fait le moins mal."),
        ("Je crois que j’ai moins besoin d’une version parfaite que d’une présence qui ne se sauve pas dès qu’elle tremble.", "Je crois que j’ai pas besoin d’une version parfaite. J’ai surtout besoin que tu restes là quand ça tremble."),
        ("Tu as raison. Aujourd’hui, je veux arrêter de te répondre seulement avec des phrases. Je vais te le montrer dans les gestes.", "Tu as raison. Aujourd’hui, je veux arrêter de répondre juste avec des phrases. Je vais essayer de te le montrer."),
        ("Pour voir si je peux arrêter de traduire chaque silence.", "Pour voir si je peux arrêter de devoir deviner derrière chaque silence."),
        ("Sarah accepte l’incertitude parce qu’elle n’est pas déguisée en certitude.", "Sarah accepte mieux l’incertitude quand elle est dite clairement."),
    ],
    "nico_j3_v2_experimental.json": [
        ("et je vais faire très attention à ne pas devenir le SAV de tes tremblements.", "et je vais faire gaffe à pas devenir celui qui gère tes tremblements à ta place."),
        ("c’est souvent le couloir entre les deux qui coûte cher.", "et c’est souvent là que ça commence à coûter cher."),
        ("je peux t’aider un peu. Mais je vais pas vivre dans ce couloir.", "je peux t’aider un peu. Mais je vais pas rester coincé là-dedans avec toi."),
        ("les radars, ça flashe. Les gens, ça lâche.", "elle cherche peut-être pas à te flasher. Elle est peut-être juste fatiguée."),
    ],
    "camille_j3_v2_experimental.json": [
        ("Mais ça m’a évité de me sentir seule avec la scène.", "Mais au moins, j’avais pas l’impression d’être la seule à avoir senti quelque chose."),
        ("Mais une limite, ça peut protéger. Ou ça peut juste ranger quelque chose qu’on ne veut pas regarder.", "Mais une limite, ça peut protéger. Ou juste servir à ne plus regarder le problème."),
        ("Je ne veux pas effacer ce moment. Mais je ne veux pas non plus t’utiliser pour sortir de ce que je n’arrive pas à régler ailleurs.", "Je ne veux pas effacer ce moment. Mais je ne veux pas non plus faire de toi une sortie parce que je n’arrive pas à gérer le reste."),
        ("Mais au moins, elle me laisse une place qui n’est pas seulement pratique.", "Mais au moins, j’ai pas l’impression d’être juste pratique."),
        ("Mais je préfère une limite qui me regarde en face à une ouverture qui m’utilise mal.", "Mais je préfère une limite claire à une ouverture où je me sens utilisée."),
        ("Et me demander de devenir l’endroit où tu vérifies.", "Et me demander d’être celle avec qui tu vérifies."),
    ],
    "maya_j3_v2_experimental.json": [
        ("juste plus de petits détails qui refusent de rester chacun dans leur coin.", "juste plus de petits détails qui commencent à se répondre."),
        ("les trucs tus ne deviennent pas invisibles. ils deviennent juste plus silencieux.", "les trucs qu’on tait ne disparaissent pas. ils font juste moins de bruit."),
        ("et toi, tu regardes parfois les messages comme s’ils avaient une température.", "parfois, on dirait que tu vérifies si tes messages brûlent."),
    ],
    "ines_j3_v2_experimental.json": [
        ("parce que ça me laisse exister comme quelqu’un, pas comme un endroit.", "parce que j’ai l’impression d’être quelqu’un, pas juste un endroit où tu viens te poser."),
        ("mais je ne veux pas devenir le nom que tu donnes à ta fuite.", "mais je ne veux pas que tu appelles “moi” le fait de fuir le reste."),
        ("sans que ça devienne plus grand que ce qu’on sait tenir.", "sans que ça devienne plus grand que ce qu’on peut tenir."),
        ("Je veux être là clairement. Pas pour fuir le reste, et pas pour te demander de porter ce que je n’ai pas réglé.", "Je veux être là clairement. Pas pour fuir le reste. Et pas pour te faire porter ce que je n’ai pas réglé."),
        ("juste pour savoir que je ne suis pas en train d’ouvrir une porte pendant que tu cours ailleurs.", "juste pour savoir que je ne suis pas en train de m’ouvrir à toi pendant que tu regardes ailleurs."),
        ("plutôt qu’une proximité qui demande ensuite pardon d’avoir été trop facile.", "plutôt qu’une proximité trop facile qu’on regrette après."),
        ("mais c’est plus propre qu’une présence qui me prendrait la main en regardant ailleurs.", "mais c’est plus propre que quelqu’un qui me prend la main sans vraiment être là."),
    ],
}

MIRRORED_CHOICES = {
    "sarah_j3_v2_experimental.json": ("j3_01_sarah_show_with_actions", "j3_01_sarah_player_show_with_actions"),
    "camille_j3_v2_experimental.json": ("j3_03_camille_recognize_without_using", "j3_03_camille_player_recognize_without_using"),
    "ines_j3_v2_experimental.json": ("j3_05_ines_clear_presence", "j3_05_ines_player_clear_presence"),
}


def load(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def nodes_by_id(dialogue: dict) -> dict:
    return {node["id"]: node for node in dialogue["nodes"]}


def serialized(name: str) -> str:
    return json.dumps(load(name), ensure_ascii=False)


def test_t200_old_texts_removed_and_new_texts_present() -> None:
    for name, replacements in REPLACEMENTS.items():
        text = serialized(name)
        for old, new in replacements:
            assert old not in text, f"old text still present in {name}: {old}"
            assert new in text, f"new text missing in {name}: {new}"


def test_t200_specified_choices_match_player_nodes() -> None:
    for name, (choice_id, player_id) in MIRRORED_CHOICES.items():
        dialogue = load(name)
        nodes = nodes_by_id(dialogue)
        matching_options = [
            choice
            for node in dialogue["nodes"]
            if node.get("type") == "choice"
            for choice in node.get("choices", [])
            if choice["id"] == choice_id
        ]
        assert len(matching_options) == 1
        assert matching_options[0]["next"] == player_id
        assert matching_options[0]["text"] == nodes[player_id]["text"]


def test_t200_all_j3_choices_keep_player_text_mirrors_and_no_media() -> None:
    for name in REPLACEMENTS:
        dialogue = load(name)
        nodes = nodes_by_id(dialogue)
        assert all(node.get("type") != "media" for node in dialogue["nodes"])
        for node in dialogue["nodes"]:
            if node.get("type") != "choice":
                continue
            for choice in node.get("choices", []):
                target = nodes[choice["next"]]
                if target.get("sender") == "player":
                    assert target["text"] == choice["text"], f"{name} {choice['id']} mirror mismatch"


if __name__ == "__main__":
    test_t200_old_texts_removed_and_new_texts_present()
    test_t200_specified_choices_match_player_nodes()
    test_t200_all_j3_choices_keep_player_text_mirrors_and_no_media()
    print("T200 J3 orality text polish tests OK")
