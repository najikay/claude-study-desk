"""The promises Study Desk makes, checked as the exact sentences that carry them.

Each check reads the body of a skill (the text after the frontmatter) for the sentence that does the
work. Deleting or weakening a rule makes a test fail; a looser check ("the word 'material' appears
somewhere") would pass with the rule gone.
"""

import os
import unittest
from pathlib import Path

ROOT = Path(os.environ.get("PLUGIN_ROOT") or Path(__file__).resolve().parents[1])
SKILLS = sorted((ROOT / "skills").glob("*/SKILL.md"))
NAMES = ("study-cards", "study-quiz", "study-grade", "study-explain", "study-plan", "study-exam")


def body(name: str) -> str:
    return (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8").split("---\n", 2)[2]


class Rules(unittest.TestCase):
    def test_the_rule_of_the_desk_is_in_every_skill(self):
        for name in NAMES:
            text = body(name)
            for sentence in (
                "**Every question comes from the material.**",
                "label it `from outside the material:`",
                "Do not guess what the material \"probably\" says",
                "A wrong answer is called wrong, with the passage that shows it",
                "do not call a partial answer complete",
                "Do not work from memory of a textbook you were not given.",
                "Never put the student's material into a web search.",
                "Do not guess their level, age or course from their name or their language",
                "do not state how an exam will be set, what an examiner wants, or what the student's grade will be",
                "**Real assessments.**",
                "say that you will not give model answers for it",
                "**Predictions.**",
                "say plainly that you cannot predict that",
                "Do not substitute a review of the material's correctness or completeness against your own knowledge",
                "**A student under strain.**",
                "**Between conversations** you keep nothing",
                "your own commentary follows the language the student writes in",
                "- **Ending.** End the reply with one line starting **Next:**, giving the words the student can type to take the next step, with the skill in brackets. If the student sounds under strain, the next step is rest, not another task.",
            ):
                self.assertIn(sentence, text, f"{name}: missing {sentence!r}")

    def test_each_skill_keeps_its_own_load_bearing_rule(self):
        for name, sentences in {
            "study-cards": ["**One fact per card.**", "no yes/no questions, no multiple choice", "Do not fill those gaps yourself:", "without a guess at what is implied", "question<TAB>answer<TAB>source", "with real tab characters between the fields", "Cloze cards go in a second block of their own", "*quiz me on this* (study-quiz)", "*plan my revision to <date>* (study-plan)"],
            "study-quiz": ["**Keep the answers to yourself**", "Do not hint.", "no percentage", "A question whose answer is not in the material is not a question for this quiz, however good it is: leave it out.", "**result line in one block**", "*make flashcards from the ones I missed* (study-cards)", "Do not ask for a direction, a sign, a unit or a convention the material does not state", "which stays last"],
            "study-grade": ["**Build the model answer from the material** and settle it before you judge", "do not grade against your memory", "No letter grade, no percentage, no \"would probably get\"", "I cannot confirm this from your material", "for each point marked missing or wrong, one flashcard in an Anki block", "6. **Next:**"],
            "study-explain": ["**Start from the material's own words**", "do not rename variables", "say what the analogy does not capture", "**End with one question**", "is outside content, and so are worked numbers of your own", "**Only if the material's own account is not enough**", "**two to four flashcards** on the concept", "*quiz me on this section* (study-quiz)"],
            "study-plan": ["**Ask for today's date and the exam date if either is missing; do not assume the date.**", "do not assume them", "Do not invent sections.", "rather than squeezing the hours", "Do not promise an outcome.", "state the rate you assume as an assumption", "The plan is not kept between conversations", "`type this` · `done`", "In `done`, an empty box `[ ]`.", "**Next:** today's row"],
            "study-exam": ["**You cannot keep time**", "Ask for the length if missing; do not assume it.", "No percentage, no letter, no \"would pass\"", "do not reuse questions", "**result line in one block**", "*make flashcards for <weakest section>* (study-cards)"],
        }.items():
            for s in sentences:
                self.assertIn(s, body(name), f"{name}: missing {s!r}")

    def test_no_skill_scrapes_or_needs_a_tool(self):
        for f in SKILLS:
            text = f.read_text(encoding="utf-8").lower()
            for word in ("scrape", "selenium", "playwright", "mcp__", "allowed-tools"):
                self.assertNotIn(word, text, f"{f}: {word!r}")

    def test_every_skill_is_present(self):
        self.assertEqual(sorted(p.parent.name for p in SKILLS), sorted(NAMES))
