import markdown2 # https://github.com/trentm/python-markdown2
import os
import shutil

STATIC_PATH = "./static/"
CONTENT_PATH = "./content/"
BUILD_DIR = "./build/"
BUILD_PERSISTENT_DIRS = ["./build/style/", "./build/scripts/", "./build/imgs/"]
DOCTYPE_START = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{}</title>
    <link rel="stylesheet" href="./style/main.css">
    <link rel="stylesheet" href="./style/snowflake.css">
</head>
<body>
"""
DOCTYPE_END = """
</body>
</html>
"""

print("WELCOME TO THE WEBSITE BUILDER FOR THE: ")
print("""
     ___           ___           ___   
    /  /\         /  /\         /  /\  
   /  /:/        /  /::\       /  /::\ 
  /  /:/        /  /:/\:\     /  /:/\:\\
 /  /:/  ___   /  /:/~/::\   /  /:/~/:/
/__/:/  /  /\ /__/:/ /:/\:\ /__/:/ /:/ 
\  \:\ /  /:/ \  \:\/:/__\/ \  \:\/:/  
 \  \:\  /:/   \  \::/       \  \::/   
  \  \:\/:/     \  \:\        \  \:\   
   \  \::/       \  \:\        \  \:\  
    \__\/         \__\/         \__\/  
""")
print("")

# delete everything
print("Deleting old build...")
for file_name in os.listdir(BUILD_DIR):
    file_path = os.path.join(BUILD_DIR, file_name)
    if file_path in map(lambda dir: os.path.dirname(dir), BUILD_PERSISTENT_DIRS):
        print("\tSkipping directory " + file_path)
    else:
        if os.path.isfile(file_path):
            os.remove(file_path)        # Remove file
            print("\tDeleted file " + file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)    # Remove directory and its contents
            print("\tDeleted content of directory " + file_path)
print("")

# get all the file names inside static and put them in an array
print("Looking for static files...")
static_files = [f for f in os.listdir(STATIC_PATH) if os.path.isfile(os.path.join(STATIC_PATH, f))]
# put them inside a dictionary
static_dictionary = dict()
for file_name in static_files:
    print("\tFound a new static file: " + file_name)
    id = file_name[:2]
    static_dictionary[id] = file_name[3:-5]

print("The final dictionary for the static files is:")
print(static_dictionary)
print("")

print("Looking for content files...")
# get all the file names inside content and put them in an array
content_files = [f for f in os.listdir(CONTENT_PATH) if os.path.isfile(os.path.join(CONTENT_PATH, f))]
# put them inside a dictionary
content_dictionary = dict()
for file_name in content_files:
    print("\tFound a new content file: " + file_name)
    content_dictionary[file_name] = ""
    indexes = [f"{i:02}" for i in range(100)]
        
    for i in indexes:
        if i == "50":
            with open(CONTENT_PATH + file_name) as f:
                content = f.read()
                html = ""
                match file_name:
                    #case "gallery.md"
                    #    html = generateGalleryHTML(content)
                    case _:
                        html = markdown2.markdown(content, extras=["footnotes, header-ids, highlightjs-lang", "smarty-pants", "strike", "toc", "wiki-tables", "tables", "fenced-code-blocks", "latex"])
                content_dictionary[file_name] += html
            print("\t\tAdded actual content to content file: " + file_name)
        else:
            try:
                with open(STATIC_PATH + i + "-" + static_dictionary[i] + ".html") as f:
                    content = f.read()
                    content_dictionary[file_name] += content
                print("\t\tAdded static stuff with index " + str(i) + " to content file: " + file_name)
            except:
                pass
                #print("\t\tNo static file with index " + i)

    with open(BUILD_DIR + file_name[:-3] + ".html", "w") as f:
        # add doctype too
        f.write(DOCTYPE_START.format(file_name[:-3]) + content_dictionary[file_name] + DOCTYPE_END)        

# print("The final dictionary for the content (build) files is:")
# print(content_dictionary)

