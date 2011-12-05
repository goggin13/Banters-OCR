import gdata.data
import gdata.docs.service
import random
import re
import os
import sys
import json
from httplib2 import Http
from urllib import urlencode
root = os.path.dirname(os.path.abspath(__file__))

# Login to Google Docs
auth_file = os.path.join(root, 'auth.js')
auth = json.loads(open(auth_file, 'r').read())
client = gdata.docs.service.DocsService()
client.ClientLogin(auth['username'], auth['password'])

# Upload image file
img_path = os.path.join(root, 'photo.PNG')
img = gdata.data.MediaSource(file_path=img_path, content_type='image/png')                             
temp_file_name = "photo-%d" % int(round(random.random() * 100000, 0))                             
folder = "https://docs.google.com/feeds/default/private/full?v=3&ocr=true"
entry = client.Upload(img, temp_file_name, folder_or_uri=folder)
root = "https://docs.google.com/feeds/id/"
document_path = entry.id.text[len(root):]

# Download as text
file_path = '/Users/mattgoggin/Desktop/your_document.txt'
client.Export(document_path, file_path)
f = open(file_path, 'r')
raw_text = f.read()
print "*" * 40, " Raw Text ", "*" * 40, "\n"
print raw_text
print "\n", "=" * 91
f.close()
os.unlink(file_path)

# Delete google document
documents_feed = client.GetDocumentListFeed()
for document_entry in documents_feed.entry:
  if document_entry.title.text == temp_file_name:
    client.Delete(document_entry.GetEditLink().href) # works
    
# split lines and drop the first 2
lines = raw_text.split("\n")
lines = lines[3:len(lines)]

# Get rid of timestamps
#              N o v   1 4,   2 0 1 1   1 1: 1 5  P  M
date_regex = "\w\w\w\s\d?\d,\s\d\d\d\d\s\d\d:\d\d\s\w\w"
results = []
for line in lines:
  if not re.match(date_regex, line):
    results.append(line)

result_string = "\n".join(results)
print  "\n", "*" * 40, " formatted for 'posts/build' ", "*" * 40, "\n"
print result_string
print "\n", "=" * 91

# Get result from 'posts/build'
h = Http()
data = dict(text=result_string)
url = "https://staging.banters.com/posts/build.json"
resp, content = h.request(url, "POST", urlencode(data))
json_object = json.loads(content)

print  "\n", "*" * 40, " response from from 'posts/build' ", "*" * 40, "\n"
print json_object
print "\n", "=" * 91

# And post the conversation
h = Http()
json_object['session_id'] = auth['session_id']
data = json.dumps(json_object)
url = "https://staging.banters.com/posts.json"
resp, content = h.request(url, "POST", data, headers={'Content-Type': 'application/json'})

json_object = json.loads(content)
print  "\n", "*" * 40, " response from from 'posts/create' ", "*" * 40, "\n"
print "Created conversation %d" % json_object['id']
print "\n", "=" * 91
