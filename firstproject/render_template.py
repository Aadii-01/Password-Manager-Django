from jinja2 import Environment, FileSystemLoader

# Load templates from the 'templates' directory
env = Environment(loader=FileSystemLoader('passgen/templates'))

# Load a specific template file
template = env.get_template('template.html')

# Define context variables
context = {
    'title': 'Welcome Page',
    'name': 'Alice',
    'items': ['Item 1', 'Item 2', 'Item 3']
}

# Render the template with the given data
output = template.render(context)

# Print or save the rendered output
print(output)

# Optionally, save to an HTML file
with open('output.html', 'w') as f:
    f.write(output)
