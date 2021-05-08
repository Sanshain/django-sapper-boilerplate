from django.shortcuts import render
from pathlib import Path

from django.urls import path

import os
from os.path import isfile, join


APP_DIR = Path(__file__).resolve().parent

# Create your views here.
def main(request):
	return render(request, '__sapper__/export/index.html')


def blog():

	return [
		path(
			'blog.json', lambda r: render(r, '__sapper__/export/blog.json')
		),
		path(
			'blog', lambda r: render(r, '__sapper__/export/blog/index.html')
		)
	]





blog_path = APP_DIR / '/'.join(['templates', '__sapper__', 'export', 'blog'])

files = os.listdir(blog_path)

json_files = [f for f in files if f[-5:] == '.json']
folds = [f for f in files if not isfile(blog_path / f)]

# TODO change `contexts` to annotation or reuse only for func declaration. Must be immutable

def blog_app(base_url = 'blog', contexts = {}):						# to be carefull on `contexts = {}`
	base_path = '/'.join(['__sapper__', 'export', 'blog'])
	
	views = [
		path(
			'/'.join([base_url, fl]), 
			lambda r: render(r, '/'.join([base_path, fl])), 
			name=fl) for fl in json_files]

	views.extend([
		path(
			'/'.join([base_url, f]), 
			lambda r: render(r, '/'.join([base_path, f, 'index.html'])),
			name=f) for f in folds])
		
	return views