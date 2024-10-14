import requests

url = "http://localhost:19002/query/service"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Define data for the query
data = {
"statement": "drop dataverse testopen2gb if exists; create dataverse testopen2gb;USE testopen2gb;CREATE TYPE Opentype AS {uid:uuid};CREATE DATASET testdefopen2gb(Opentype) PRIMARY KEY uid autogenerated with {'storage-block-compression': {'scheme': 'none'}};LOAD DATASET testdefopen2gb USING localfs (('path' = 'localhost:///home/dbis-nuc10/DBIS/data/wiscon_moregroups_2gb.adm'),  ('format' = 'adm'));",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)

# Define data for the query
data = {
"statement": "drop dataverse testopen4gb if exists; create dataverse testopen4gb;USE testopen4gb;CREATE TYPE Opentype AS {uid:uuid};CREATE DATASET testdefopen4gb(Opentype) PRIMARY KEY uid autogenerated with {'storage-block-compression': {'scheme': 'none'}};LOAD DATASET testdefopen4gb USING localfs (('path' = 'localhost:///home/dbis-nuc10/DBIS/data/wiscon_moregroups_4gb.adm'),  ('format' = 'adm'));",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)

# Define data for the query
data = {
"statement": "drop dataverse testopen8gb if exists; create dataverse testopen8gb;USE testopen8gb;CREATE TYPE Opentype AS {uid:uuid};CREATE DATASET testdefopen8gb(Opentype) PRIMARY KEY uid autogenerated with {'storage-block-compression': {'scheme': 'none'}};LOAD DATASET testdefopen8gb USING localfs (('path' = 'localhost:///home/dbis-nuc10/DBIS/data/wiscon_moregroups_8gb.adm'),  ('format' = 'adm'));",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)

# Define data for the query
data = {
"statement": "drop dataverse testopen16gb if exists; create dataverse testopen16gb;USE testopen16gb;CREATE TYPE Opentype AS {uid:uuid};CREATE DATASET testdefopen16gb(Opentype) PRIMARY KEY uid autogenerated with {'storage-block-compression': {'scheme': 'none'}};LOAD DATASET testdefopen16gb USING localfs (('path' = 'localhost:///home/dbis-nuc10/DBIS/data/wiscon_moregroups_16gb.adm'),  ('format' = 'adm'));",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)

# Define data for the query
data = {
"statement": "drop dataverse testopen32gb if exists; create dataverse testopen32gb;USE testopen32gb;CREATE TYPE Opentype AS {uid:uuid};CREATE DATASET testdefopen32gb(Opentype) PRIMARY KEY uid autogenerated with {'storage-block-compression': {'scheme': 'none'}};LOAD DATASET testdefopen32gb USING localfs (('path' = 'localhost:///home/dbis-nuc10/DBIS/data/wiscon_moregroups_32gb.adm'),  ('format' = 'adm'));",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)

# Define data for the query
data = {
"statement": "drop dataverse testopen64gb if exists; create dataverse testopen64gb;USE testopen64gb;CREATE TYPE Opentype AS {uid:uuid};CREATE DATASET testdefopen64gb(Opentype) PRIMARY KEY uid autogenerated with {'storage-block-compression': {'scheme': 'none'}};LOAD DATASET testdefopen64gb USING localfs (('path' = 'localhost:///home/dbis-nuc10/DBIS/data/wiscon_moregroups_64gb.adm'),  ('format' = 'adm'));",
    "pretty": "true",
    "client_context_id": "xyz"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)