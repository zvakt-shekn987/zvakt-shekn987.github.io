+++
date = '{{ .Date.UTC.Format "2006-01-02T" }}'
draft = true
title = '{{ replace .File.ContentBaseName "-" " " | title }}'
+++
