import os

file_ = 'utils/template/email_message.txt'
file_html_ = 'utils/template/email_message.html'

def get_template_path(path):
    file_path = os.path.join(os.path.dirname(__file__), file_)
    #file_path = os.path.join(os.getcwd(),file_)
    if not os.path.isfile(file_path):
        raise Exception('This is not a valid template path "{what}"'.format(what=file_))
    return file_path

def get_template(path):
    file_path = get_template_path(path)
    return open(file_path).read()

def adjust_string(template_string, context):
    return template_string.format(**context)

#print(adjust_string(template_content, context))
#print("")
#print(adjust_string(template_content_html, context))