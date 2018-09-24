For installasjon på Windows:

1) Installer Python 3.5.4 (MERK: Dvs. ikke nyeste versjon)
2) Installer "Windows Visual Studio Biuld Tools" ( https://visualstudio.microsoft.com/downloads/ )
3) Installer "Swigwin" og legg installasjonsmappen til "PATH" ( http://www.swig.org/download.html )
4) Opprett et "Virtual Environment" et sted. F.eks. i samme mappe som "nlp-toolbox". Gi kommando for å opprette: "python -m venv winvenv"
5) Aktiver miljøet ved å gi kommando: "winvenv\Scripts\activate" (deaktiverer ved å gi kommando: "deactivate")
6) Installer EbookLib 0.15 manuelt. -> Manøvrer til installasjonsmappen og gi kommando: "pip install ."
7) Installer alle nødvendige pakker: "pip install -r requirements.txt"