#!/usr/bin/env python
from padhu_auto_blog.crew import PadhuAutoBlogCrew

def load_html_template(): 
    
    with open('src/padhu_auto_blog/config/blog_template.html', 'r') as file:
        html_template = file.read()
        return html_template

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': input('Enter your Blog Topic: '),
        'personal_message': input('Enter a personal message for your newsletter: '),
        'html_template': load_html_template()
    }
    PadhuAutoBlogCrew().crew().kickoff(inputs=inputs)