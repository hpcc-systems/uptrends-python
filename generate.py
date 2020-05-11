import json
import os
import shutil
from os.path import join
from textwrap import dedent
from urllib.request import Request, urlopen, urlretrieve
from zipfile import ZipFile

data = {
    "options": {
        "packageName": "uptrends",
        "projectName": "uptrends",
        "packageUrl": "https://github.com/hpcc-systems/uptrends-python",
    },
    "swaggerUrl": "https://api.uptrends.com/v4/swagger/v1/swagger.json",
}
request = Request(
    "https://generator.swagger.io/api/gen/clients/python",
    json.dumps(data).encode('ascii'),
    {"Content-Type": "application/json"}
)
with urlopen(request) as response:
    download_url = json.load(response)['link']

    tempfile = './temp.zip'

    filename, headers = urlretrieve(download_url, tempfile)

    with ZipFile(filename) as z:
        z.extractall()

    os.remove(tempfile)

    root_src_dir = "./python-client"
    root_dst_dir = "."
    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                # in case of the src and dst are the same file
                if os.path.samefile(src_file, dst_file):
                    continue
                os.remove(dst_file)
            shutil.move(src_file, dst_dir)

    shutil.rmtree("./python-client")

readme = "README.md"
readme_bak = f"{readme}.bak"
with open(readme) as f:
    lines = f.readlines()
    lines[0] = dedent("""\
        # Uptrends Python Library

        *The library in this repository was automatically generated using 
        [Swagger Codegen](https://github.com/swagger-api/swagger-codegen). However, to
        allow for upgrades and bugfixes, other scripts and documentation have been
        added. Please see [CONTRIBUTING.md](CONTRIBUTING.md) for more information.*
        
        ---
    """)

    with open(readme_bak, "w") as g:
        g.writelines(lines)

shutil.move(readme_bak, readme)
