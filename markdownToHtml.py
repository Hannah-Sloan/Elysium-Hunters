import os

def replaceLineWithImages(content):
    imageEnd = content
    while content.count("![") > 0:
        preText = content[:content.find("![")]

        imageEnd = imageEnd[imageEnd.find("![")+2:]
        imageName = imageEnd[:imageEnd.find("](")]
        imageEnd = imageEnd[imageEnd.find("](")+2:]
        imageSrc = imageEnd[:imageEnd.find(")")]
        imageEnd = imageEnd[imageEnd.find(")")+1:]
        
        content = preText + f"<img src = \"{imageSrc}\" alt=\"{imageName}\"/>" + imageEnd
    return content

def replaceLineWithLinks(content):
    linkEnd = content
    while content.count("[") > 0:
        preText = content[:content.find("[")]

        linkEnd = linkEnd[linkEnd.find("[")+1:]
        linkName = linkEnd[:linkEnd.find("](")]
        linkEnd = linkEnd[linkEnd.find("](")+2:]
        linkSrc = linkEnd[:linkEnd.find(")")]
        linkSrc = linkSrc.replace(".md", ".html")
        linkEnd = linkEnd[linkEnd.find(")")+1:]

        content = preText + f"<a href=\"{linkSrc}\">{linkName}</a>" + linkEnd
    return content

def replaceLineWithBold(content):
    boldEnd = content
    while content.count("**") > 0:
        preText = content[:content.find("**")]

        boldEnd = boldEnd[boldEnd.find("**")+2:]
        boldText = boldEnd[:boldEnd.find("**")]
        boldEnd = boldEnd[boldEnd.find("**")+2:]

        content = preText + f"<b>{boldText}</b>" + boldEnd
    return content

def replaceLineWithItalic(content):
    italicEnd = content
    while content.count("*") > 0:
        preText = content[:content.find("*")]

        italicEnd = italicEnd[italicEnd.find("*")+1:]
        italicText = italicEnd[:italicEnd.find("*")]
        italicEnd = italicEnd[italicEnd.find("*")+1:]

        content = preText + f"<em>{italicText}</em>" + italicEnd
    return content

def header_indent(header_depth_in):
    return "\t"*(header_depth_in-1)

def pageBoilerPlate(title, isHomePage, style_depth = 0):
    indent_depth = ""

    goBack = "../" * style_depth

    # Boilerplate
    html = "<!DOCTYPE html>\n"
    html += "<html lang=\"en\">\n"
    indent_depth += "\t"
    html += indent_depth + "<head>\n"
    indent_depth += "\t"
    html += indent_depth + f"<link rel=\"stylesheet\" type=\"text/css\" href=\"{goBack}style.css\" />\n" #Adding Stylesheet
    #html += indent_depth + "<link rel=\"shortcut icon\" href=\"https://raw.githubusercontent.com/Hannah-Sloan/Teenage-Coven-Knights/master/docs/img/moon_chrome.ico\" type=\"image/x-icon\"/>\n" #Adding Favicon
    #html += indent_depth + "<link rel=\"icon\" href=\"https://raw.githubusercontent.com/Hannah-Sloan/Teenage-Coven-Knights/master/docs/img/moon_chrome.ico\" type=\"image/x-icon\"/>\n"
    html += indent_depth + "<title> "
    html += title + " - Elysium Hunters"
    html += " </title>\n"
    html += indent_depth + f"<meta name=\"description\" content=\"Elysium Hunters - {title}\" >\n"
    html += indent_depth + "<meta name=\"keywords\" content=\"HTML, CSS, RPG, open, Elysium Hunters, Elysium, Hunters, rules-lite, sci-fi, scifi, indie\">\n"
    html += indent_depth + "<meta name=\"author\" content=\"Hannah Ava Sloan\">\n"
    html += indent_depth + "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
    indent_depth = indent_depth.replace("\t", "", 1)
    html += indent_depth + "</head>\n"

    #Body
    html += indent_depth + "<body>\n"
    indent_depth += "\t"

    html += indent_depth + f"<p><a href=\"https://github.com/Hannah-Sloan/Elysium-Hunters\">GITHUB</a>\n"
    
    if(not(isHomePage)):
        html += indent_depth + f"<a href=\"{goBack}index.html\">HOME</a></p>\n"

    html += indent_depth + "<main>\n"
    indent_depth += "\t"

    return html, indent_depth

def endingBoilerPlate(html, indent_depth, input_file):
    indent_depth = indent_depth.replace("\t", "", 1)
    html += indent_depth + "</main>\n"

    html += indent_depth + "<div id=\"license\"> <a rel=\"license\" href=\"https://github.com/Hannah-Sloan/Elysium-Hunters/blob/master/LICENSE.md\"><img alt=\"Creative Commons License\" style=\"border-width:0\" src=\"https://i.creativecommons.org/l/by-nc/4.0/88x31.png\" /></a><br /><span xmlns:dct=\"http://purl.org/dc/terms/\" href=\"http://purl.org/dc/dcmitype/Text\" property=\"dct:title\" rel=\"dct:type\">The <b>text</b> contents of Elysium Hunters</span> is licensed under a <a rel=\"license\" href=\"https://github.com/Hannah-Sloan/Elysium-Hunters/blob/master/LICENSE.md\">Creative Commons Attribution-NonCommercial 4.0 International License</a>.</div>\n"

    indent_depth = indent_depth.replace("\t", "", 1)
    html += indent_depth + "</body>\n"
    html += "</html>"

    output_file = input_file.replace(".md", ".html")
    output_file = output_file.replace("markdown\\", "docs\\")

    print("CREATING PAGE: " + output_file)
    path = os.path.dirname(f"{output_file}")
    if not (os.path.exists(path)) and not(".html" in output_file):
        os.makedirs(path)
    # Write the output to a file
    with open(f"{output_file}", "w", encoding="utf8") as f:
        f.write(html)

def createHomePage(path, pages, subfolders):
    title = path.split("\\")[-1]

    title = title.replace("_", " ")
    title = title.upper()

    isHomePage = False
    if title == "MARKDOWN":
        title = "HOME"
        isHomePage = True
    print("HOME PAGE: " + title)
    
    html, indent_depth = pageBoilerPlate(title, isHomePage)

    html += indent_depth + f"<h1>{title}</h1>\n"

    for subfolder in subfolders:
        linkPath = subfolder[0] + ".html"
        linkPath = os.path.join(path, linkPath).replace("markdown\\", "")
        linkName = subfolder[0].split("\\")[-1]
        linkName = linkName.replace("_", " ")
        linkName = linkName.upper()
        html += indent_depth + f"<p><a href={linkPath}>{linkName}</a></p>\n"

    for page in pages:
        pageName = page.replace("_", " ")
        pageName = pageName.replace(".md", "")
        pageName = pageName.upper()
        page = page.replace(".md", ".html")
        link = os.path.join(path, page).replace("markdown\\", "")
        html += indent_depth + f"<p><a href={link}>{pageName}</a></p>\n"

    if title == "HOME":
        html += indent_depth + "<p>Read more about Elysium Hunters' Game License on Github: <a href=\"https://github.com/Hannah-Sloan/Elysium-Hunters/blob/master/LICENSE.md\">LICENSE</a></p>"

    path = path + ".html"
    path = path.replace("markdown.html", "markdown\\index.html")
    endingBoilerPlate(html, indent_depth, path)

def convert(input_file):
    title = (input_file[:len(input_file)-3])
    title = title.replace("_", " ")
    title = title.upper()

    html, indent_depth = pageBoilerPlate(title, False, len(input_file.split("\\"))-2)

    with open(f"{input_file}", "r", encoding="utf8") as f:
        md = f.read()

    counter = 0

    header_depth = 1

    lines = md.split("\n")
    curSection = False

    for line in lines:
        if line.startswith("#"):
            level = line.count("#")
            header_depth = level
            content = line[level+1:]
            content = replaceLineWithImages(content)
            content = replaceLineWithLinks(content)
            content = replaceLineWithBold(content)
            content = replaceLineWithItalic(content)
            if(curSection):
                html += indent_depth + header_indent(level) + "</section>\n"
                curSection = False

            if(level > 1):
                id = content.lower().replace(" ", "-")
                html += indent_depth + header_indent(level) + f"<section id=\"{id}\">\n"
                curSection = True

            html += indent_depth + header_indent(level) + f"<h{level}>{content}</h{level}>\n"
        else:
            if(line != ""):
                line = replaceLineWithImages(line)
                line = replaceLineWithLinks(line)
                line = replaceLineWithBold(line)
                line = replaceLineWithItalic(line)

                html += indent_depth + header_indent(header_depth+1) + f"<p>{line}</p>\n"

    endingBoilerPlate(html, indent_depth, input_file)