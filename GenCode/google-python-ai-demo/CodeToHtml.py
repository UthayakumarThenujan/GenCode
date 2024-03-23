from Code import *
import os


def getCode(topic):
    y = []
    main = []
    for i in to_markdown(generate_code(topic).text):
        if i != "\n":
            y.append(i)
        else:
            result = "".join(y)
            characters_to_remove = ["", " ", "  "]
            result_string = "".join(
                char for char in result if char not in characters_to_remove
            )
            main.append(result)
            y = []
    return main


def mainDo(topic):
    codepara = getCode(topic)
    code = convert_pptx_to_html(codepara)
    return code


def convert_pptx_to_html(code):
    # Load the PowerPoint presentation

    # Convert each slide to HTML
    html_content = []
    for i in code:
        html_content.append(f"<p>{i}</p>")

    final = "".join(html_content)
    return f"<div>{final}</div>"
