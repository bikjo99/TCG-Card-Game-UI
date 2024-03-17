from enum import Enum


class OpponentFieldAreaActionProcess(Enum):
    Dummy = 0
    REQUIRED_FIRST_PASSIVE_SKILL_PROCESS = 1
    CHECK_MULTIPLE_UNIT_REQUIRED_FIRST_PASSIVE_SKILL_PROCESS = 2
    PLAY_ANIMATION = 3
    REQUIRE_TO_PROCESS_PASSIVE_SKILL_PROCESS = 4
    REQUIRE_TO_PROCESS_GENERAL_ATTACK_TO_MAIN_CHARACTER_PROCESS = 5
    REQUIRE_TO_PROCESS_GENERAL_ATTACK_TO_YOUR_UNIT_PROCESS = 6
    REQUIRE_TO_PROCESS_VALRN_ACTIVE_TARGETING_SKILL_TO_YOUR_UNIT = 7


