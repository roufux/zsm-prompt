#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  completion.py
#  
#  Copyright 2024 Ryan <ryan@ubuntu>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
#!/usr/bin/env python
"""
Example of a colored prompt.
"""

from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import ANSI, HTML
from prompt_toolkit.styles import Style

style = Style.from_dict(
    {
        # Default style.
        "": "#ff0066",
        # Prompt.
        "username": "#884444 italic",
        "at": "#00aa00",
        "colon": "#00aa00",
        "pound": "#00aa00",
        "host": "#000088 bg:#aaaaff",
        "path": "#884444 underline",
        # Make a selection reverse/underlined.
        # (Use Control-Space to select.)
        "selected-text": "reverse underline",
    }
)


def example_1():
    """
    Style and list of (style, text) tuples.
    """
    # Not that we can combine class names and inline styles.
    prompt_fragments = [
        ("class:username", "john"),
        ("class:at", "@"),
        ("class:host", "localhost"),
        ("class:colon", ":"),
        ("class:path", "/user/john"),
        ("bg:#00aa00 #ffffff", "#"),
        ("", " "),
    ]

    answer = prompt(prompt_fragments, style=style)
    print(f"You said: {answer}")


def example_2():
    """
    Using HTML for the formatting.
    """
    answer = prompt(
        HTML(
            "<username>john</username><at>@</at>"
            "<host>localhost</host>"
            "<colon>:</colon>"
            "<path>/user/john</path>"
            '<style bg="#00aa00" fg="#ffffff">#</style> '
        ),
        style=style,
    )
    print(f"You said: {answer}")


def example_3():
    """
    Using ANSI for the formatting.
    """
    answer = prompt(
        ANSI(
            "\x1b[31mjohn\x1b[0m@"
            "\x1b[44mlocalhost\x1b[0m:"
            "\x1b[4m/user/john\x1b[0m"
            "# "
        )
    )
    print(f"You said: {answer}")


if __name__ == "__main__":
    example_1()
    example_2()
    example_3()
