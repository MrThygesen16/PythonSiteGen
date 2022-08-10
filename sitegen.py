from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
from json import load
from os import walk


def read_markdown(md_file: str) -> markdown:
    with open(md_file) as markdown_file:
        article = markdown(markdown_file.read(), extras=['codehilite', 'tables', 'fenced-code-blocks', 'code-friendly'])
    
    return article


def read_json_config(json_file: str) -> dict:
    
    with open(json_file) as config_file:
        config = load(config_file)

    return config



def get_file_names(input_dir: str) -> list[(str, str)]:
    files = []
    for (dirpath, dirnames, filenames) in walk(input_dir):
        files = filenames   
    
    html_files: list[(str, str)] = []
        
    for item in files:
        name, extentions = item.split('.')
        html_files.append((name + ".html", item))
        
    return html_files


def write_single_file_to_html(html_file: str, config: dict, article: markdown) -> None:
            
    with open(html_file, 'w') as output_file:
        output_file.write(template.render(
            title = config['title'],
            description = config['description'],
            author = config['author'],
            # heading = config['heading'], 
            article = article))


def write_list_files_to_html(files: list[(str, str)], config: dict, input_dir: str, output_dir: str) -> None:    
    
   for item in files:
       article = read_markdown(input_dir + item[1])
       html_file = output_dir + item[0]
       write_single_file_to_html(html_file, config, article)


if __name__ == '__main__':

    template_env = Environment(loader=FileSystemLoader(searchpath='./'))
    
    template_folder = 'templates/'
    name_of_template = 'blog_post_base.html'
    
    template = template_env.get_template(template_folder + name_of_template)

    config = read_json_config('templates/config.json')

    folder_to_read_from = 'blogs/'
    folder_to_output_to = 'docs/blog/'    

    # files = get_file_names(folder_to_read_from)
    # write_list_files_to_html(files, config, folder_to_read_from, folder_to_output_to)
    
    name_of_file = 'pattern-matching'
    
    file_to_read = read_markdown(folder_to_read_from + name_of_file + '.MD')
    
    write_single_file_to_html(folder_to_output_to + name_of_file + ".html", config, file_to_read)

    print("Success")