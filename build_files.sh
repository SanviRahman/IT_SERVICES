echo "BUILD START"
python3.13.1 -m pip install -r requirments.txt
python3.13.1 manage.py collectstatic --noinput --clear
echo "BUILD END"