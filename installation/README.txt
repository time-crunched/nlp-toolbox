For installasjon p� Windows:

1) Installer Python 3.5.4 (MERK: Dvs. ikke nyeste versjon)
2) Installer "Windows Visual Studio Biuld Tools" ( https://visualstudio.microsoft.com/downloads/ )
3) Installer "Swigwin" og legg installasjonsmappen til "PATH" ( http://www.swig.org/download.html )
4) Opprett et "Virtual Environment" et sted. F.eks. i samme mappe som "nlp-toolbox". Gi kommando for � opprette: "python -m venv winvenv"
5) Aktiver milj�et ved � gi kommando: "winvenv\Scripts\activate" (deaktiverer ved � gi kommando: "deactivate")
6) Installer EbookLib 0.15 manuelt. -> Man�vrer til installasjonsmappen og gi kommando: "pip install ."
7) Installer alle n�dvendige pakker: "pip install -r requirements.txt"