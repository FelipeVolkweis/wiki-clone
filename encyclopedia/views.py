from django.http import QueryDict
from django.shortcuts import render

from . import util
import markdown2, re, random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request, entry):
    return render(request, "encyclopedia/wiki.html", {
        "entry1": entry,
        "entries": util.list_entries(),
        "content": markdown2.markdown(util.get_entry(entry))
    })


def search_wiki(request):
    search = request.GET['q']
    search = QueryDict(search).dict().keys()
    search = list(search)
    entries = util.list_entries()
    compare = [item.lower() for item in entries]

    if not search:
        return render(request, "encyclopedia/search_wiki.html")

    if search[0].lower() in compare:
        search = search[0].replace("+", "%20")
        return wiki(request, search)
    else:
        matches = []
        for entry in entries:
            if search[0].lower() in entry.lower():
                matches.append(entry)
        
        return render(request, "encyclopedia/search_wiki.html", {
                "matches": matches
        })


def create_page(request):
    if request.method == 'POST':
        title = request.POST['title_id']
        text = request.POST['text_id']
        text = '# ' + title + '\r\n' + text
        entries = util.list_entries()
        if title in entries:
            return already_exists(request, title)
        else:
            util.save_entry(title, text)
            return wiki(request, title)
    else:
        return render(request, "encyclopedia/create_page.html")


def already_exists(request, repeated_entry):
    return render(request, "encyclopedia/already_exists.html", {
        "repeated_entry": repeated_entry
    })


def edit_page(request):
    if request.method == 'POST':
        if 'edit_id' in request.POST:
            title = request.POST['edit_id']
            text = util.get_entry(title)
            return render(request, "encyclopedia/edit_page.html", {
                "text": text
            })
        elif 'save_edit' in request.POST:
            content = request.POST['text_edit_id']
            header = re.search("^# .*", content).group()[:-1][2:]
            util.save_entry(header, content)
            return wiki(request, header)


def random_page(request):
    entries = util.list_entries()
    selected_page = random.choice(entries)
    return wiki(request, selected_page)