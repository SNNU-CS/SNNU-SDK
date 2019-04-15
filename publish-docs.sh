#!/bin/bash
export GH_REF="github.com/snnucs/SNNU-SDK.git"
cd docs && make html
git clone https://${GH_REF} html
cd html
git checkout  gh-pages
git pull origin
rm -rf *
sudo mv  ./../SNNU-SDK-docs/html/* ./
git status
git config  --global user.name "Qi Zhao"
git config  --global user.email "956361916@qq.com" 
git add . 
git commit -m "Travis CI Auto Builder at `date +"%Y-%m-%d %H:%M"`" 
git push  --quiet "https://${GH_TOKEN}@${GH_REF}" gh-pages:gh-pages