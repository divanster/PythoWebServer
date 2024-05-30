import os


class TemplateEngine:
    def render(self, template_name, context):
        path = os.path.join(os.path.dirname(__file__), template_name)
        with open(path, 'r') as template_file:
            template_content = template_file.read()
        return template_content.format(**context)
