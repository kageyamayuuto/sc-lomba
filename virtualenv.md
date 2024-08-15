#Menginstall virtual environment
###(windows)
pip install virtualenv
###(linux)
python3 -m pip install --user virtualenv

#Membuat virtual environment
python -m venv myvenv

#Menjalankan visrtual environment
###(windows)
myvenv\Scripts\activate
###(linux)
source myvenv/bin/activate

#menginstall django dan Pillow untuk upload gambar
pip install django Pillow

#menginstall library yang diperlukan
pip install -r requirements.txt