# header.rpy contains MAS submod header as well as Submod Updater header.
#
# This file is part of Discord Presence Submod (see link below):
# https://github.com/friends-of-monika/discord-presence-submod

init -990 python in mas_submod_utils:
    Submod(
        author="Friends of Monika",
        name="Discord Presence Submod",
        description="展示谁才是陪伴你最久的人~",
        version="0.0.1",
        settings_pane="fom_presence_settings_pane"
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Discord Presence Submod",
            user_name="MAS-Submod-MoyuTeam",
            repository_name="mas-presence",
            extraction_depth=3
        )