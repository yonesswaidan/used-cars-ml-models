# Used Cars ML Models
Dette projekt indeholder en analyse og forudsiger priser på brugte biler baseret på data fra et stort datasæt. Projektet anvender forskellige modeller som Random Forest og Gradient Boosting.

Opret mappen data i roden af projektet og kald det "Data", også hent datasættet fra https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data og kald filen "vehicles.csv" og den skal være i mappen "data" og grunden til det er netop fordi filen er 1.4 gb.

Projektstruktur:

data/ Indeholder datasæt 
results/ indeholder resultater fra vores modeller
requirements.txt/ Indeholder vores afhængigheder
Allcode.ipynb/ Vores notebook fil der indeholder alt logik

Kør projektet:

git clone https://github.com/yonesswaidan/used-cars-ml-models.git
cd used-cars-ml-models

Opret virtuelt miljø:

python -m venv .venv
.venv\Scripts\activate # Windows
source .venv/bin/activate # macOS/Linux
Også kør:
pip install -r requirements.txt

Også kan du kør vores notebook fil, for at se resultaterne fra modellerne. 

