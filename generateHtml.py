import os
import markdownToHtml

def getSubdirectories(path):
    dirs = []
    for file in os.listdir(path):
        d = os.path.join(path, file)
        if os.path.isdir(d) and file != "img":
            dirs.append((d, getSubdirectories(d)))
    return dirs

def makeHomePages(folder):
    for subfolder in folder:
        pages = []
        for page in os.listdir(subfolder[0]):
            if ".md" in page:
                pages.append(page)
        markdownToHtml.createHomePage(subfolder[0], pages, subfolder[1])
        makeHomePages(subfolder[1])

def makePages(folder):
    for subfolder in folder:
        for file in os.listdir(subfolder[0]):
            if ".md" in file:
                markdownToHtml.convert(os.path.join(subfolder[0], file))
        makePages(subfolder[1])

dirs = [("markdown", getSubdirectories("markdown"))]
makeHomePages(dirs)
makePages(dirs)