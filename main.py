from jinja2 import Environment, FileSystemLoader
import os

class Site():
    def __init__(self, title="Pytoile", template="templates/base.html"):
        self.variables = {"title" : title}

    def generate(self, path="index.html"):
        root = os.path.dirname(os.path.abspath(__file__))
        templates_dir = os.path.join(root, 'templates')
        env = Environment(loader=FileSystemLoader(templates_dir))
        template = env.get_template('menu.html')

        filename = os.path.join(root, 'html', 'index.html')
        with open(filename, 'w') as fh:
            rend = template.render(
                is_menu=True,
                menu_items=[{'name': "Accueil", 'link': "/accueil"}, {'name': "Blog", 'link': "/blog"}]
            )
            fh.write(rend)


if __name__ == "__main__":
    site = Site(template="templates/menu.html")
    site.generate()
