import os 
import markdown
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify


app = Flask(__name__)
app.debug = True

base_dir = os.path.abspath(os.path.dirname(__file__)) + '/../snippets'

def get_snippet_slugs(): 
    slugs = []
    for prefix, dirs, files in os.walk(base_dir): 
        for f in files: 
            slugs.append(prefix + '.' + f.split('.md')[0])
    return [s.split('/snippets/')[1] for s in slugs]


@app.route('/')
def snippetlist(): 
    slugs = get_snippet_slugs()
    return render_template('snippetlist.html', snippetslugs = get_snippet_slugs())

@app.route('/snippet/<slug>')
def snippet(slug):
    snippet_md = open('{}/{}.md'.format(base_dir, slug.replace('.', '/'))).read()
    snippet_html = markdown.markdown(snippet_md)
    return render_template('snippet.html', snippet_html=snippet_html, slug=slug)  

if __name__ == "__main__":
    app.run(host='localhost', port=4444)