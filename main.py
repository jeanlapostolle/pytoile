class Site():
    template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
</head>
<body>
</body>
</html>"""
    def __init__(self, title="Pytoile"):
        self.title = title

    def generate(self, path="index.html"):
        with open(path, 'w+') as f:
            f.write(self.template.format(title = self.title))


if __name__=="__main__":
    site = Site()
    site.generate()
