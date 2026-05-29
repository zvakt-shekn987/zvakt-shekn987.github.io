import os
from datetime import datetime, timezone

def create_leaf(post_name="new-post", timeformat1="%Y-%m-%d", timeformat2="%Y %m %d"):

    dt = datetime.now(timezone.utc)
    time_str = dt.strftime("%Y-%m-%d")
    time_str2 = dt.strftime("%Y %m %d")
    dir_path = f"content/post/{time_str}-{post_name}"
    index_fp = f"{dir_path}/index.md"

    archetype = f"""---
title: {post_name.replace('-', ' ')}
subtitle: ""
date: {time_str2}
draft: true
author: ""
description: ""
categories: []
tags: []
bigimg: []
comments: true
---
"""

    os.mkdir(dir_path)
    with open(index_fp, 'w') as f:
        f.write(archetype)
    print(f"Leaf bundle created on {dir_path}")