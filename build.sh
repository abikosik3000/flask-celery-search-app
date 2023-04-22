#!/bin/bash
app="the_searcher"
docker build -t ${app} .
docker run -d -p 5000:5000 ${app}