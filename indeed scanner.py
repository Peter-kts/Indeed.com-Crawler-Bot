from bs4 import BeautifulSoup as bs
import requests
import re

originalurl = "https://www.indeed.com/jobs?q=web+developer&l=fort+lee+nj"
results = {'Javascript': 0, 'Python': 0, 'PHP': 0, 'C#': 0, 'Java': 0}

def get_html_parser(url) :
	response = requests.get(url)
	soup = bs(response.content, "html.parser")
	return (soup)

def extract_keywords(arg_list):
	for page in arg_list:
		newurl = ('https://www.indeed.com' + page)
		parsed_single = get_html_parser(newurl)
		keyword_haystack = parsed_single

		if re.search(r'javascript[\W]', keyword_haystack.get_text(), re.IGNORECASE):
			results['Javascript'] += 1

		if re.search(r'Python[\W]', keyword_haystack.get_text(), re.IGNORECASE):
			results['Python'] += 1

		if re.search(r'PHP[\W]', keyword_haystack.get_text(), re.IGNORECASE):
			results['PHP'] += 1

		if re.search(r'.net[\W]', keyword_haystack.get_text(), re.IGNORECASE):
			results['C#'] += 1

		if re.search(r'java[\W]', keyword_haystack.get_text(), re.IGNORECASE):
			results['Java'] += 1

def get_next_page(url):
	data = url.findAll('div',attrs={'class':'pagination'})

	for page_link in data:
		print (page_link.a['href'])

def get_job_links(url):
	parse = get_html_parser(url)
	data = parse.findAll('a',attrs={'class':'turnstileLink'})
	link_list = []

	for link in data:
		link_list.append(link['href'])

	extract_keywords(link_list)
	get_next_page(parse)


get_job_links(originalurl)
print(results)

