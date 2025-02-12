echo "BUILD START"
python3.13 -m pip install -r requirments.txt
python3.13 manage.py collectstatic --noinput --clear
echo "BUILD END"