#this will be templates

import os



def get_template_path(path):
    file_path = os.path.join(os.getcwd(),path)
    if not os.path.isfile(file_path):
        raise Exception('This is not a valid template path "{what}"'.format(what=file_))
    return file_path

def get_template(path):
    file_path = get_template_path(path)
    return open(file_path).read()

def adjust_string(template_string, context):
    return template_string.format(**context)

file_html_ = 'template/email_message.html'
template_content_html =get_template(file_html_)


file_ = 'template/email_message.txt'
template_content = get_template(file_)
context = {
    "insert_name": "Bohdan",
    "insert_total":55.3,
    "insert_date":"27/11/2017"
}


print(adjust_string(template_content, context))
print("")
print(adjust_string(template_content_html, context))