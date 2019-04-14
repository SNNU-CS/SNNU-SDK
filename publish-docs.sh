#!/bin/bash
export GH_REF="github.com/snnucs/SNNU-SDK.git"
cd docs && make html
pwd
git clone https://${GH_REF} html
cd html
git checkout  gh-pages
git pull origin
cd ..
pwd
ls
sudo cd SNNU-SDK-docs && sudo mkdir .git
sudo mv html/.git/ SNNU-SDK-docs/.git/
sudo cd SNNU-SDK-docs
pwd
rm -rf doctrees
git config  --global user.name "Qi Zhao"
git config  --global user.email "956361916@qq.com" 
git add . 
git commit -m "Travis CI Auto Builder at `date +"%Y-%m-%d %H:%M"`" 
git push  --quiet "https://${GH_TOKEN}@${GH_REF}" gh-pages:gh-pages