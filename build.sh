git fetch origin
git merge origin/master

pip3 install -r requirements.txt

cd FunExhibition
python3 manage.py migrate --settings=backend.settings_prod
python3 manage.py collectstatic --no-input --settings=backend.settings_prod

supervisorctl restart fun
